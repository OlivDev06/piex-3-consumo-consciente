import streamlit as st

def apresentacao():
    st.title("🌱 Pequenas atitudes, grandes mudanças")

    st.image("imagens/pequenas_atitudes.jpg", width=700)

    st.write("""
    O consumo faz parte do nosso cotidiano. Diariamente, adquirimos
    produtos, utilizamos embalagens e descartamos materiais que já
    não são necessários. Entretanto, nossas escolhas de consumo
    podem gerar impactos significativos no meio ambiente.

    O consumo consciente consiste em refletir sobre aquilo que
    compramos, avaliar nossas necessidades e considerar os impactos
    ambientais envolvidos na produção, utilização e descarte dos produtos.

    Atitudes simples, como evitar desperdícios, reutilizar objetos,
    escolher produtos duráveis e separar corretamente os materiais
    recicláveis, contribuem para reduzir a quantidade de resíduos gerados.

    Mais do que consumir menos, é importante consumir melhor e
    compreender que nossas escolhas individuais também fazem parte
    de um esforço coletivo pela preservação ambiental.
    """)

    st.divider()

    st.header("Por que esse assunto é importante?")

    st.image("imagens/importancia_tema.jpg", width=700)

    st.write("""
    O descarte inadequado de resíduos sólidos é um problema ambiental
    que afeta cidades e comunidades de diferentes tamanhos.

    Quando os materiais são descartados incorretamente, podem provocar
    a contaminação do solo e da água, contribuir para o entupimento
    de sistemas de drenagem e favorecer a proliferação de animais
    transmissores de doenças.

    Além disso, muitos materiais que poderiam ser reaproveitados
    ou reciclados acabam sendo desperdiçados quando não recebem
    a destinação adequada.

    Por isso, a participação da população é fundamental. Separar
    os resíduos, respeitar os dias e locais de coleta, encaminhar
    materiais especiais aos pontos apropriados e reduzir o desperdício
    são atitudes que ajudam a melhorar a gestão dos resíduos sólidos.

    A sustentabilidade não depende apenas de grandes iniciativas
    governamentais ou empresariais. Ela também começa nas decisões
    que tomamos diariamente.
    """)    

    st.divider()

    st.header("O cenário de Curitiba")

    st.image("imagens/cenario_curitiba.jpg", width=700)

    st.write("""
    Curitiba possui uma estrutura de coleta e gerenciamento de
    resíduos sólidos que inclui a coleta domiciliar, a coleta seletiva,
    os Ecopontos e programas de incentivo à reciclagem.

    De acordo com informações divulgadas pela Prefeitura com base
    em dados do IBGE, a coleta de resíduos atendia 100% dos domicílios
    da cidade. A Prefeitura também informou que são coletadas, em
    média, 2.500 toneladas de resíduos por dia.

    Outro dado importante é o índice de reciclagem de Curitiba,
    que chegou a 24,90% em 2024, próximo da meta municipal de 25%.
    Entretanto, o mesmo relatório aponta que 30% dos materiais recebidos
    pela coleta seletiva eram rejeitos, acima da meta municipal de 15%.
    Isso demonstra que ainda existem desafios relacionados à separação
    correta dos resíduos. 

    Esses resultados mostram que, mesmo com uma estrutura de coleta
    abrangente, a redução da geração de resíduos e a destinação
    adequada continuam sendo fundamentais.
    """)

    st.info("""Acesse a página (Dados de Curitiba) no menu lateral
    para conferir os dados sobre coleta de resíduos em Curitiba!""")

    st.divider()

    st.header("Aprenda e teste seus conhecimentos")

    st.image("imagens/teste_conhecimentos.jpg", width=700)

    st.write("""
    Agora que você conhece um pouco mais sobre consumo consciente
    e gestão de resíduos, que tal testar seus conhecimentos?

    Preparamos um quiz interativo com perguntas sobre separação
    de materiais, reciclagem, reutilização, compostagem e descarte correto.

    Ao responder às perguntas, você poderá descobrir o quanto conhece
    sobre sustentabilidade e aprender novas maneiras de contribuir
    para um ambiente mais limpo e saudável.
    """)

    st.info("Acesse a página (Quiz) no menu lateral e participe!")