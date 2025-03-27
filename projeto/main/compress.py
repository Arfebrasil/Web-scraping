import os
import zipfile

folder = "projeto/files"  # the folder that will have the files zipped


def to_zip() -> None:  # get files in the folder files and turn into one zip

    os.makedirs(
        "projeto/zip", exist_ok=True
    )  # creates a folder that will contain the zip

    with zipfile.ZipFile(
        "projeto/zip/Anexos.zip", "w", zipfile.ZIP_DEFLATED
    ) as zip:  # creates the file zip, not flatting just joing all files

        for file in os.listdir(folder):  # search for every file in folder

            if file.endswith(".pdf"):  # get only .pdf files

                zip.write(
                    os.path.join(folder, file), arcname=file
                )  # gets the path of the file to zip it


def main() -> None:
    to_zip()


if __name__ == "__main__":
    main()
