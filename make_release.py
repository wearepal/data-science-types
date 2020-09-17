"""Bump version and create tag in git."""
from pathlib import Path

from git import Repo


def main() -> None:
    """Run the script."""
    repo = Repo()
    assert not repo.is_dirty(), "please commit or stash all other changes"
    assert repo.active_branch.name == "master", "only tag versions on master"

    # merge master into release branch
    git = repo.git
    git.checkout("release")
    git.merge("--no-ff", "master", "--no-edit")
    print("updated release branch")

    # find out the version number
    tags_minor_versions = [tag.name.split(".")[-1] for tag in repo.tags]
    latest_minor_version = max(int(mv) for mv in tags_minor_versions if mv.isdigit())
    old_version = f"0.2.{latest_minor_version}"
    new_version = f"0.2.{latest_minor_version + 1}"
    print(f"new version will be: {new_version}")

    # change version in setup.py
    setup_path = Path("setup.py")
    with setup_path.open("r") as fhandle:
        file_content = fhandle.read()
        count = 0
        while old_version in file_content:
            file_content = file_content.replace(old_version, new_version, 1)
            count += 1
        assert count == 1, "couldn't properly change the version in setup.py... aborting"
    with setup_path.open("w") as fhandle:
        fhandle.write(file_content)
    print("modified setup.py")

    # commit change
    repo.index.add(["setup.py"])
    repo.index.commit(f"Bump version to {new_version}")

    # # create tag and push
    tag_name = f"v{new_version}"
    repo.create_tag(tag_name)
    print(f"git push origin release {tag_name}")
    git.push("origin", "release", tag_name)

    # clean up
    git.checkout("master")


if __name__ == "__main__":
    main()
