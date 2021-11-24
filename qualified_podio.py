
# Pódio Olímpico Versão 1

def podio_olimpico(tempo_chegada1,tempo_chegada2,tempo_chegada3):
    # Implemente aqui a lógica da função
    lista_de_tempos= [tempo_chegada1, tempo_chegada2, tempo_chegada3]
    ordem_em_modo_de_sorte = sorted(lista_de_tempos) 
    return(
            f"1 - {ordem_em_modo_de_sorte[0]} minutos\n"
            f"2 - {ordem_em_modo_de_sorte[1]} minutos\n"
            f"3 - {ordem_em_modo_de_sorte[2]} minutos\n"
        )