# 2. Uma Playlist


class Musica:
    def __init__(self, titulo: str, artista: str, album: str):
        self.titulo = titulo
        self.artista = artista
        self.album = album

    def __str__(self) -> str:
        return f"{self.titulo} - {self.artista} ({self.album})"


class Playlist:
    def __init__(self, nome: str, desc: str, musicas: list[Musica]):
        self.nome = nome
        self.descricao = desc
        self.musicas = musicas

    def inserir(self, m: Musica) -> None:
        self.musicas.append(m)

    def listar(self) -> list[Musica]:
        return self.musicas

    def __str__(self) -> str:
        return f'Playlist "{self.nome}"'
