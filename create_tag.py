"""Bump version and create tag in git."""
from pathlib import Path

from git import Repo


def main() -> None:
    """Run the script."""
    repo = Repo()
    assert not repo.is_dirty(), "please commit or stash all other changes"
    assert repo.active_branch.name == "master", "only tag versions on master"

    # find out the version number
    latest_minor_version = int(sorted(repo.tags, key=lambda x: x.name)[-1].name.split(".")[-1])
    new_version = f"0.2.{latest_minor_version + 1}"
    print(f"new version will be: {new_version}")

    # change version in setup.py
    setup_path = Path("setup.py")
    with setup_path.open("r") as fhandle:
        new_content = fhandle.read().replace("0.3.0.dev1", new_version)
    with setup_path.open("w") as fhandle:
        fhandle.write(new_content)
    print("modified setup.py")

    # commit change
    git = repo.git
    branch_name = f"releases/{new_version}"
    print(f"commit to branch {branch_name}")
    git.checkout("-b", branch_name)
    repo.index.add(["setup.py"])
    repo.index.commit("Bump version")

    # create tag and push
    tag_name = f"v{new_version}"
    repo.create_tag(tag_name)
    print(f"git push origin {tag_name} {branch_name}")
    git.push("origin", tag_name, branch_name)

    # clean up
    git.checkout("master")
    git.branch("-D", branch_name)
    print(f"Deleted branch {branch_name}")


if __name__ == "__main__":
    main()
