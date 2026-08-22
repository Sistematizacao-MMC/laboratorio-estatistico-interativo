import os
import zipfile
import requests

REPO_OWNER = "Sistematizacao-MMC"
REPO_NAME = "laboratorio-estatistico-interativo"
RELEASE_TAG = "v1.0.0"
DEST_DIR = "data"

ZIP_FILES = [
    "0-EMPRE.zip",
    "0-ESTABELE.zip",
    "0-SOCIO.zip",
    "dataset_complementary.zip",
]


def download_file(url: str, dest_path: str, chunk_size: int = 1024 * 1024) -> None:
    """Baixa o arquivo em partes (chunks) mostrando o progresso em MB."""
    print(f"Baixando: {url}")
    response = requests.get(url, stream=True)
    response.raise_for_status()

    total_size = int(response.headers.get("content-length", 0))
    downloaded = 0

    with open(dest_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=chunk_size):
            if chunk:
                f.write(chunk)
                downloaded += len(chunk)
                if total_size > 0:
                    percent = (downloaded / total_size) * 100
                    print(
                        f"\rProgresso: {downloaded / (1024*1024):.1f} MB / "
                        f"{total_size / (1024*1024):.1f} MB ({percent:.1f}%)",
                        end="",
                    )
                else:
                    print(f"\rBaixados: {downloaded / (1024*1024):.1f} MB", end="")
    print("\nDownload concluido.")


def extract_zip(zip_path: str, extract_to: str) -> None:
    """Descompacta o arquivo .zip na pasta de destino."""
    print(f"Extraindo {zip_path} em {extract_to}...")
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_to)
    print("Extracao concluida.")


def main():
    os.makedirs(DEST_DIR, exist_ok=True)

    base_url = f"https://github.com/{REPO_OWNER}/{REPO_NAME}/releases/download/{RELEASE_TAG}"

    for file_name in ZIP_FILES:
        url = f"{base_url}/{file_name}"
        zip_path = os.path.join(DEST_DIR, file_name)

        download_file(url, zip_path)

        extract_zip(zip_path, DEST_DIR)

        if os.path.exists(zip_path):
            os.remove(zip_path)
            print(f"Arquivo temporario {file_name} removido.\n")


if __name__ == "__main__":
    main()
