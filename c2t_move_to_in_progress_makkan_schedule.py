import subprocess
import json
import os


def list_items():
    cmd = 'gh project item-list 8 -L 200 --owner RhoderickGalero --format json'
    return run_cmd(cmd)


def move_to_in_progress(issue_id):
    cmd = 'gh project item-edit --id {0} --field-id "PVTSSF_lAHOBbg8Ns4AVCc-zgNcWS4" --project-id PVT_kwHOBbg8Ns4AVCc- --single-select-option-id "47fc9ee4"'.format(issue_id)
    return run_cmd(cmd)
    
def move_back_to_Todo(issue_id):
    cmd = 'gh project item-edit --id {0} --field-id "PVTSSF_lAHOBbg8Ns4AVCc-zgNcWS4" --project-id PVT_kwHOBbg8Ns4AVCc- --single-select-option-id "f75ad846"'.format(issue_id)
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
        if 'assignees' in item:
           if item['content']['type'] == "Issue" and item['status'] == "Todo issue" and item['assignees'] is not None:
            move_to_in_progress(item['id'])
            print(f"{item['id']} will be Move to 'InProgress issue'")
        elif item['content']['type'] == 'Issue' and item['status'] == 'In Progress issue':
            move_back_to_Todo(item['id'])
            print(f"{item['title']} will be Move back to 'To do issue'") 
        else:
             print(f"{item['title']} Issue is not assigned")
            #break


if __name__ == "__main__":
    main()
