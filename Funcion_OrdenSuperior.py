# -*- coding: utf -8 -*-


def saludo(idioma):
    def saludo_es():
        print("Hola")

    def saludo_en():
        print("Hello")
    idioma_func = {"es": saludo_es,
                   "en": saludo_en}
    return idioma_func[idioma]


if __name__ == "__main__":
    saludar = saludo("es")
    saludar()
    saludarq = saludo("en")
    saludarq()
