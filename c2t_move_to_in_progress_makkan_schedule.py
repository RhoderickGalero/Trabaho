import subprocess
import json
import os


def list_items():
    cmd = 'gh project item-list 8 --owner RhoderickGalero --format json'
    return run_cmd(cmd)


def move_to_in_progress(issue_id):
    cmd = 'gh project item-edit --id {0} --field-id "PVTSSF_lAHOBbg8Ns4AT02azgMqiD8" --project-id PVT_kwHOBbg8Ns4AVCc- --single-select-option-id "47fc9ee4"'.format(issue_id)
    return run_cmd(cmd)
    

def run_cmd(cmd):
    print('Running cmd "{0}"'.format(cmd))
    result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True, text=True)
    out, err = result.stdout, result.stderr
    # For debugging
    #print("Out: {0}".format(out))
    #print("Err: {0}".format(err))
    return out


def main():
    #issue_nr = int(os.getenv("ISSUE_NR"))
    project_items = json.loads(list_items())
    #print (project_items)
    for item in project_items["items"]:
        if item['assignees'] not in item:
            print(" No issue in assigned")
        elif item['content']['type'] == "Issue" and item['status'] == "Todo issue" and item['assignees'] is not None:
            #move_to_in_progress(item['id'])
            print(f"Moved Issue {item['id']} to 'InProgress'")
            #break


if __name__ == "__main__":
    main()
