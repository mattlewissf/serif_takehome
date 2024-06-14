import gzip
import urllib.request
import json
import datetime

# TODO: the provided url throws a 403 error, so I am using an update file name I derived
ANTHEM_URL = "https://antm-pt-prod-dataz-nogbd-nophi-us-east1.s3.amazonaws.com/anthem/2024-06-01_anthem_index.json.gz"


def read_json():

    # open the url and return a http.client.HTTPResponse object
    url_obj = urllib.request.urlopen(ANTHEM_URL)

    with gzip.open(url_obj, "r", compresslevel=1) as f:
        # set up some counter and collections
        counter = 0
        url_collector = set()
        ein_collector = set()

        # Stream through the file
        for _row in f:
            counter += 1
            # decode byte code into string, basic munging
            row = _row.decode("utf8").replace("'", '"')
            try:
                clean = row.strip(", \n")
                # load chunk as python object
                row_dict = json.loads(clean)
                ein = row_dict["reporting_plans"][0]["plan_id"]
                # don't reprocess EINs we've seen before
                if ein not in ein_collector:
                    ein_collector.add(ein)
                    # search through python object for description file matching New York and PPO
                    results = [
                        v["location"]
                        for v in row_dict["in_network_files"]
                        if "New York" in v["description"] and "PPO" in v["description"]
                    ]
                    url_collector.update(results)
                else:
                    pass
            except:
                pass
                # print(f"Error parsing this row: {row[0:100]}")

            if counter % 1000 == 0:
                print(f"{counter} | urls: {len(url_collector)}")
                print(f"urls: {len(url_collector)}")

    # at end of script, write to text file
    with open("anthem_ppo_urls.txt", "a", buffering=20 * (1024**2)) as myfile:
        urls = "\n".join(list(url_collector))
        myfile.write(urls)

    # Some summary printing at the end of the script
    print("*" * 50)
    print("finished:")
    print(counter)
    print(len(url_collector))
    print("*" * 50)


if __name__ == "__main__":
    start = datetime.datetime.now()
    read_json()
    total_time = datetime.datetime.now() - start
    print(f"finished in {total_time}")
