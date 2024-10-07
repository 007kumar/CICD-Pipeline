import requests
import os

def get_latest_commit():
    url = f"https://api.github.com/repos/007kumar/CICD-Pipeline/commits"
    headers = {'Authorization': f'token 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'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        commits = response.json()
        return commits[0]['sha']
    else:
        print(f"Failed to fetch commits: {response.status_code}")
        return None

def is_new_commit(latest_commit):
    if os.path.exists(LAST_COMMIT_FILE):
        with open(LAST_COMMIT_FILE, 'r') as f:
            last_commit = f.read().strip()
        return last_commit != latest_commit
    return True

def save_latest_commit(latest_commit):
    with open(LAST_COMMIT_FILE, 'w') as f:
        f.write(latest_commit)

def main():
    latest_commit = get_latest_commit()
    if latest_commit and is_new_commit(latest_commit):
        print("New commit detected. Deploying...")
        os.system("/path/to/deploy.sh")  # Call the deployment script
        save_latest_commit(latest_commit)
    else:
        print("No new commits.")

if __name__ == "__main__":
    main()

