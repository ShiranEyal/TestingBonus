import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_NAME = os.getenv('REPO_NAME')

if __name__ == "__main__":
    g = Github(ACCESS_TOKEN)

    # Specify the repository details
    curr_user = g.get_user()
    repo = curr_user.get_repo(REPO_NAME)
    branch = repo.get_branch(repo.default_branch)

    # File details
    file_path = "example.txt"
    file_content = "This is an example file."
    commit_message = "Add or update example.txt"

    # Get the SHA of the existing file if it exists
    try:
        contents = repo.get_contents(file_path, ref=branch.name)
        sha = contents.sha
    except:
        sha = None

    # Create or update the file
    repo.create_file(
        path=file_path,
        message=commit_message,
        content=file_content,
        branch=branch.name,
        sha=sha
    )

    print("File has been committed and pushed to the main branch.")