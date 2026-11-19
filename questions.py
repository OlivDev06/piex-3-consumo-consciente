import streamlit as st

if "pontuacao" not in st.session_state:
    st.session_state.pontuacao = 0

if "pergunta_respondida" not in st.session_state:
    st.session_state.perguntas_respondidas = set()

if "resultados_perguntas" not in st.session_state:
    st.session_state.resultados_perguntas = {}

def pergunta1():    
    montar_pergunta(
        numero=1,
        texto_pergunta="Uma pessoa deseja adotar hábitos de consumo mais sustentáveis e" 
                        "diminuir a quantidade de resíduos que produz no dia a dia."
                        "Qual das atitudes abaixo representa a melhor estratégia para alcançar esse objetivo?", 
        alternativas=[
            "A) Substituir produtos descartáveis por versões recicláveis, mesmo que sejam utilizadas em grandes quantidades.",
            "B) Avaliar a necessidade de cada compra, priorizar produtos duráveis e aproveitar os objetos pelo maior tempo possível.",
            "C) Separar os resíduos recicláveis somente quando houver grande quantidade acumulada em casa.",
            "D) Descartar produtos antigos sempre que surgirem versões mais modernas e eficientes no mercado."
        ],
        resposta_correta="B) Avaliar a necessidade de cada compra, priorizar produtos" 
                         " duráveis e aproveitar os objetos pelo maior tempo possível.",
        explicacao_correta="Muito bem! O consumo consciente começa antes mesmo da compra. Avaliar a real necessidade de um produto," 
                           " escolher opções duráveis e prolongar sua vida" 
                           " útil são atitudes importantes para reduzir o desperdício e diminuir a geração de resíduos.",
        explicacao_errada="Lembre-se de que reduzir a geração de resíduos envolve pensar em todas as etapas do consumo," 
                          " desde a escolha do produto até o seu descarte. Priorizar produtos duráveis e" 
                          " evitar compras desnecessárias são atitudes fundamentais para a sustentabilidade."
    )

def pergunta2():
    montar_pergunta(
        numero=2,
        texto_pergunta="Qual atitude representa uma prática de consumo consciente?", 
        alternativas=[
            "A) Comprar produtos em promoção mesmo sem precisar deles.",
            "B) Substituir produtos antigos por novos sempre que surgir um modelo diferente.",
            "C) Escolher produtos considerando sua durabilidade, necessidade e impacto ambiental.",
            "D) Priorizar produtos com mais embalagens para garantir sua conservação."
        ],
        resposta_correta="C) Escolher produtos considerando sua durabilidade, necessidade e impacto ambiental.",
        explicacao_correta="Isso mesmo! Sempre que pensarmos em comprar algo novo devemos refletir se realmente estamos precisando daquilo.",
        explicacao_errada="O consumo consciente envolve refletir sobre a necessidade de uma compra, a durabilidade do produto e seus impactos ambientais, evitando compras desnecessárias e desperdícios."
    )

def pergunta3():
    montar_pergunta(
        numero=3,
        texto_pergunta="Qual das ações abaixo contribui diretamente para reduzir a geração de resíduos no dia a dia?",
        alternativas=[
            "A) Utilizar copos descartáveis em vez de copos reutilizáveis",
            "B) Trocar aparelhos eletrônicos anualmente, mesmo quando funcionam bem.",
            "C) Levar uma garrafa reutilizável para evitar o consumo frequente de garrafas descartáveis.",
            "D) Descartar roupas antigas sempre que comprar roupas novas."
        ],
        resposta_correta="C) Levar uma garrafa reutilizável para evitar o consumo frequente de garrafas descartáveis.",
        explicacao_correta="Perfeito! Sempre que possível evite o uso de produtos descartáveis para gerar menos lixo",
        explicacao_errada="Uma garrafa reutilizável pode ser utilizada diversas vezes,"
                          "diminuindo a necessidade de consumir garrafas descartáveis e reduzindo a geração de resíduos."
    )

def pergunta4():
    montar_pergunta(
        numero=4,
        texto_pergunta="Você possui um móvel antigo que ainda está em boas condições, "
                       "mas deseja mudar a decoração da sua casa. Qual seria a alternativa mais sustentável?",
        alternativas=[
            "A) Descartar o móvel e comprar outro imediatamente.",
            "B) Deixar o móvel na rua para que alguém decida o que fazer com ele.",
            "C) Desmontar o móvel e descartar todas as peças no lixo comum.",
            "D) Reformar, personalizar ou doar o móvel para prolongar sua vida útil."
        ],
        resposta_correta="D) Reformar, personalizar ou doar o móvel para prolongar sua vida útil.",
        explicacao_correta="Muito bom! Sempre que possível é bom evitar que materiais em bom estado sejam descartados para o lixo",
        explicacao_errada= "Reformar, reutilizar ou doar um móvel prolonga sua vida útil,"
        "reduz a necessidade de consumir novos produtos e pode evitar que materiais aproveitáveis se transformem em resíduos."
    )

def pergunta5():
    montar_pergunta(
        numero=5,
        texto_pergunta="Por que é importante separar corretamente os materiais recicláveis dos resíduos comuns?",
        alternativas = [
            "A) Porque todos os materiais e resíduos podem ser reciclados independentemente de sua composição.",
            "B) Porque a separação facilita a triagem e o encaminhamento dos materiais recicláveis para a reciclagem.",
            "C) Porque os materiais recicláveis não precisam de qualquer tratamento antes de serem reutilizados.",
            "D) Porque a separação elimina completamente a produção de resíduos nas residências."
            ],
        resposta_correta="B) Porque a separação facilita a triagem e o encaminhamento dos materiais recicláveis para a reciclagem.",
        explicacao_correta="Ótimo! Fazer a separação correta ajuda consideravelmente no tratamento dos materiais recicláveis.",
        explicacao_errada="A separação adequada facilita o trabalho de triagem e o encaminhamento dos materiais para a reciclagem. "
                                "Entretanto, nem todo material é reciclável em qualquer condição, "
                                "e a destinação correta depende das características do resíduo e das regras locais de coleta."
    )

def pergunta6():
    montar_pergunta(
        numero=6,
        texto_pergunta="Ao separar resíduos domésticos, "
                       "qual atitude é mais adequada antes de encaminhar embalagens recicláveis para a coleta seletiva?",
        alternativas= [
            "A) Misturar restos de comida às embalagens para facilitar o transporte.",
            "B) Colocar todos os resíduos, inclusive pilhas e medicamentos, junto com os recicláveis comuns.",
            "C) Descartar as embalagens com grande quantidade de restos de alimentos sem verificar as orientações de separação.",
            "D) Retirar os restos de alimentos das embalagens e seguir as orientações locais para a separação e o descarte."
            ],
        resposta_correta="D) Retirar os restos de alimentos das embalagens e seguir as orientações locais para a separação e o descarte.",
        explicacao_correta="Perfeito! Nunca esqueça de limpar as embalagens com restos de comida antes de descartá-las!",
        explicacao_errada="Restos de alimentos podem contaminar outros materiais e dificultar a triagem."
                              " Seguir as orientações da coleta seletiva local ajuda a encaminhar os resíduos corretamente."
                              " Pilhas e medicamentos, por exemplo, podem exigir pontos de coleta específicos."
    )

def pergunta7():
    montar_pergunta(
        numero=7,
        texto_pergunta="Uma pessoa encontrou pilhas usadas e baterias antigas guardadas em uma gaveta. "
                       "Qual é a maneira mais adequada de descartá-las?",
        alternativas=[
            "A) Colocá-las na lixeira de resíduos recicláveis comuns, junto com papel e plástico.",
            "B) Jogá-las no lixo orgânico, pois são objetos pequenos e não ocupam muito espaço.",
            "C) Entregá-las em pontos de coleta específicos que recebam pilhas e baterias usadas.",
            "D) Enterrá-las no quintal para evitar que entrem em contato com outros resíduos."   
        ],
        resposta_correta="C) Entregá-las em pontos de coleta específicos que recebam pilhas e baterias usadas.",
        explicacao_correta="Muito bem! Pilhas e baterias usadas precisam de uma destinação específica," 
                           " pois podem conter substâncias capazes de contaminar o solo e a água."  
                           " Ao encaminhá-las para pontos de coleta apropriados," 
                           " você contribui para evitar danos ambientais e permite que esses materiais recebam o tratamento adequado.",
        explicacao_errada="Pilhas e baterias podem conter substâncias que oferecem riscos ao meio ambiente quando descartadas incorretamente."
                          " Por isso, devem ser encaminhadas a pontos de coleta apropriados,"
                          " que possibilitem sua destinação ambientalmente adequada."
    )

def pergunta8():
    montar_pergunta(
        numero=8,
        texto_pergunta="Uma residência possui medicamentos vencidos e um aparelho eletrônico que não funciona mais. "
                       "Considerando os riscos ambientais e a necessidade de destinação adequada, "
                       "qual alternativa apresenta a conduta mais correta?",
        alternativas=[
            "A) Descartar os medicamentos no vaso sanitário e colocar o aparelho eletrônico no lixo comum.",
            "B) Encaminhar os medicamentos a pontos de coleta em farmácias ou locais habilitados e procurar pontos de recebimento de resíduos eletrônicos.",
            "C) Colocar os medicamentos e o aparelho eletrônico juntos na coleta seletiva, pois ambos contêm materiais que podem ser reciclados.",
            "D) Guardar os medicamentos até que se acumulem em grande quantidade e desmontar o aparelho eletrônico em casa para descartar suas peças separadamente."
        ],
        resposta_correta="B) Encaminhar os medicamentos a pontos de coleta em farmácias ou locais habilitados e procurar pontos de recebimento de resíduos eletrônicos.",
        explicacao_correta="Excelente! Medicamentos vencidos e resíduos eletrônicos exigem cuidados especiais no descarte." 
                           " Os medicamentos devem ser entregues em pontos de coleta habilitados, enquanto os eletrônicos precisam ser encaminhados a locais especializados." 
                           " Essas práticas ajudam a prevenir a contaminação ambiental e favorecem a destinação adequada dos materiais.",
        explicacao_errada="Medicamentos vencidos não devem ser descartados no lixo comum, na pia ou no vaso sanitário, pois podem contaminar o solo e a água." 
                          " Eles devem ser entregues em pontos de coleta apropriados." 
                          " Já os equipamentos eletrônicos precisam ser encaminhados a locais que recebam esse tipo de resíduo," 
                          " permitindo o aproveitamento de componentes e evitando a liberação inadequada de substâncias potencialmente perigosas."
    )

def pergunta9():
    montar_pergunta(
        numero=9,
        texto_pergunta="Qual é o principal objetivo do processo de compostagem dos resíduos orgânicos?",
        alternativas=[
            "A) Transformar resíduos orgânicos em um material que pode ser utilizado para melhorar a qualidade do solo.",
            "B) Eliminar todos os resíduos domésticos por meio da queima controlada.",
            "C) Transformar materiais plásticos e metálicos em fertilizantes naturais.",
            "D) Armazenar restos de alimentos até que possam ser descartados junto com o lixo comum."
        ],
        resposta_correta="A) Transformar resíduos orgânicos em um material que pode ser utilizado para melhorar a qualidade do solo.",
        explicacao_correta="Muito bem! A compostagem é um processo de decomposição da matéria orgânica realizado por organismos decompositores."
                           " Como resultado, é produzido um composto que pode ser utilizado para enriquecer o solo,"
                           " contribuindo para o aproveitamento dos resíduos orgânicos.",
        explicacao_errada="A compostagem não consiste em queimar ou simplesmente armazenar resíduos." 
                          " Ela aproveita a decomposição natural da matéria orgânica para produzir um composto que pode ser utilizado na melhoria do solo."
    )

def pergunta10():
    montar_pergunta(
        numero=10,
        texto_pergunta="Uma família decidiu começar a fazer compostagem em casa para aproveitar os restos de alimentos."
                       "Qual das alternativas apresenta a prática mais adequada para esse processo?",
        alternativas=[
            "A) Colocar restos de alimentos, plásticos, vidros e metais juntos na composteira para aumentar a variedade de materiais.",
            "B) Adicionar apenas alimentos cozidos e carnes, mantendo a composteira completamente fechada e sem ventilação.",
            "C) Misturar resíduos orgânicos adequados, como cascas de frutas e restos de vegetais, com materiais secos, mantendo condições apropriadas de umidade e ventilação.",
            "D) Adicionar grandes quantidades de água diariamente para acelerar a decomposição dos resíduos."
        ],
        resposta_correta="C) Misturar resíduos orgânicos adequados, como cascas de frutas e restos de vegetais, com materiais secos, mantendo condições apropriadas de umidade e ventilação.",
        explicacao_correta="Excelente! Uma compostagem adequada depende do equilíbrio entre materiais orgânicos úmidos," 
                           " como restos de frutas e vegetais, e materiais secos, como folhas secas." 
                           " Também é importante manter condições adequadas de umidade e ventilação para favorecer a atividade dos organismos decompositores.",
        explicacao_errada="A compostagem exige alguns cuidados. Misturar materiais orgânicos adequados com materiais secos ajuda a equilibrar o processo."
                          " Excesso de água, falta de ventilação ou presença de materiais inadequados podem prejudicar a decomposição."
    )

def montar_pergunta(numero, texto_pergunta, alternativas, resposta_correta, explicacao_correta, explicacao_errada):
    st.subheader(f"Pergunta {numero} de 10")

    if numero in st.session_state.perguntas_respondidas:
        resultado = st.session_state.resultados_perguntas[numero]

        if resultado["correta"]:
            st.success("Resposta correta! 🎉")
        else:
            st.error("Resposta incorreta. ❌")

        st.write(resultado["explicacao"])

        st.info("Você já respondeu essa pergunta.")

    else:
        resposta = st.radio(texto_pergunta, alternativas, index=None, key=f"radio_{numero}")
        
        if st.button("Verificar resposta", key=f"btn_{numero}"):
            if resposta is None:
                st.warning("Selecione uma alternativa primeiro.")

            else:
                st.session_state.perguntas_respondidas.add(numero)
            
                if resposta == resposta_correta:
                    st.session_state.pontuacao += 1

                    st.session_state.resultados_perguntas[numero] = {
                        "correta": True,
                        "explicacao": explicacao_correta
                    }

                else:
                    st.session_state.resultados_perguntas[numero] = {
                        "correta": False,
                        "explicacao": explicacao_errada
                    }

                st.rerun() 


def mostrar_resultado():
    
    pontuacao = st.session_state.pontuacao
    erros = 10 - pontuacao

    st.title("Resultado do quiz")

    col1, col2 = st.columns(2)

    col1.metric("Acertos", pontuacao)
    col2.metric("Erros", erros)

    if pontuacao <= 2:
        st.warning("Continue aprendendo! Ainda há muito para descobrir sobre consumo consciente.")

    elif pontuacao <= 4:
        st.info("Nada mal! Você já conhece alguns conceitos sobre consumo consciente, mas pode aprofundar os seus conhecimentos.")

    elif pontuacao <= 7:
        st.success("Bom desempenho! Você demonstrou bons conhecimentos sobre sustentabilidade e gestão de resíduos.")

    elif pontuacao <= 9:
        st.success("Muito bem! Você entende muito sobre a importância e motivos das práticas sustentáveis.")

    else:
        st.balloons()

        st.success("Parabéns! Você acertou todas as perguntas! 🥳")


def exibir_perguntas():
    st.title("Teste seus conhecimentos sobre consumo consciente, "
              "Reciclagem e descarte de resíduos")
    st.divider()

    pergunta1()
    st.divider()
    pergunta2()
    st.divider()
    pergunta3()
    st.divider()
    pergunta4()
    st.divider()
    pergunta5()
    st.divider()
    pergunta6()
    st.divider()
    pergunta7()
    st.divider()
    pergunta8()
    st.divider()
    pergunta9()
    st.divider()
    pergunta10()
    st.divider()

    if len(st.session_state.perguntas_respondidas) == 10:
        mostrar_resultado()


def mostrar_detalhes():
    return st.session_state.perguntas_respondidas, st.session_state.resultados_perguntas





    
