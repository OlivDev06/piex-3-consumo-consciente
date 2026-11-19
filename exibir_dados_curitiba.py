import streamlit as st
import altair as alt
import pandas as pd

def exibir_dados():
    introducao_dados()
    st.divider()
    criar_grafico_reciclagem()
    st.divider()
    criar_grafico_rejeitos()
    st.divider()
    criar_grafico_aterro()
    st.divider()
    criar_grafico_destinacao()
    st.divider()
    criar_grafico_arvores()
    st.divider()
    exibir_conclusão()
    

def introducao_dados():
    st.title("♻️ Como Curitiba está cuidando dos seus resíduos?")

    st.write("""
    A gestão adequada dos resíduos sólidos é um desafio importante para as cidades,
    pois está diretamente relacionada à preservação do meio ambiente e à qualidade
    de vida da população.

    Nesta página, vamos conhecer alguns indicadores de Curitiba relacionados à reciclagem,
    à coleta seletiva e à destinação dos resíduos. Por meio de gráficos e dados de diferentes anos,
    será possível observar a evolução desses indicadores,
    identificar avanços e perceber quais desafios ainda precisam de atenção.

    Mais do que apresentar números, o objetivo é compreender como nossas escolhas e
    hábitos de consumo podem contribuir para uma cidade mais sustentável.
    """)

    st.image("imagens/reciclagem_curitiba.jpg", caption="Separação de resíduos recicláveis em Curitiba." 
    " Foto: Zaf / Wikimedia commons (CC BY-SA 3.0).", width=700)

def criar_grafico_reciclagem():
    df = pd.read_csv("dados/reciclagem_curitiba.csv")

    df["ano"] = df["ano"].astype(str)

    df["indice_formatado"] = df["indice_reciclagem"].map(lambda valor: f"{valor:.2f}%")

    grafico_reciclagem = alt.Chart(df).mark_line(point=True).encode(
        x=alt.X("ano:N", title="Ano", axis=alt.Axis(labelAngle=0)), 
        y=alt.Y("indice_reciclagem:Q", scale=alt.Scale(domain=[20, 28]),
        title="Índice de reciclagem", axis=alt.Axis(values=[20, 22.5, 25, 27.5], format=".0f", labelExpr="datum.value + '%'")),
        tooltip=[alt.Tooltip("ano:N", title="Ano"), alt.Tooltip
        ("indice_formatado:N", title="índice de reciclagem")]).properties(width=500, height=300).interactive()

    st.subheader("Evolução dos indíces de reciclagem")

    st.write("""
    O índice de reciclagem representa a porcentagem dos resíduos que são recuperados e encaminhados
    para a reciclagem em relação ao total considerado no cálculo desse indicador. Em outras palavras,
    ele ajuda a entender quanto do material descartado está sendo reaproveitado,
    em vez de simplesmente ser destinado ao lixo comum.

    Observe que, quanto maior esse percentual, maior é a participação da
    reciclagem no conjunto de resíduos analisado.
    """)

    st.altair_chart(grafico_reciclagem, width='stretch')

    st.info("""
    Os dados de Curitiba mostram uma evolução de 22,50% em 2021 para 24,90% em 2024. 
    Isso indica um aumento no índice ao longo do período, embora que a meta de 2024 era chegar a 25%,
    mostrando que ainda existe espaço para ampliar a reciclagem na cidade.
    """)

def criar_grafico_rejeitos():
    df = pd.read_csv("dados/rejeitos_curitiba.csv")
    
    df["ano"] = df["ano"].astype(str)

    df_linhas = df.melt(id_vars="ano", value_vars=["rejeitos", "previsao"], var_name="tipo", value_name="percentual")
    
    df_linhas["tipo"] = df_linhas["tipo"].replace({"rejeitos": "Rejeitos na coleta", "previsao": "Previsão"})
    
    grafico_rejeitos = alt.Chart(df_linhas).mark_line(point=True).encode(
        x=alt.X("ano:N", title="Ano", axis=alt.Axis(labelAngle=0)),
        y=alt.Y("percentual:Q", title="Rejeitos na coleta seletiva (%)", scale=alt.Scale(domain=[10, 40]),
        axis=alt.Axis(values=[10, 15, 20, 25, 30, 35, 40], labelExpr="datum.value + '%'")),
        color=alt.Color("tipo:N", title="Indicador"),
        strokeDash=alt.StrokeDash("tipo:N", title="Indicador", scale=alt.Scale(domain=["Resultado realizado", "Previsão"], range=[[1, 0], [6, 4]])),
        tooltip=[alt.Tooltip("ano:N", title="Ano"), alt.Tooltip("tipo:N", title="Tipo"),
        alt.Tooltip("percentual:Q", title="Percentual", format=".2f")]
    ).properties(width=500, height=300).interactive()

    
    st.subheader("Evolução dos rejeitos na coleta seletiva")
    
    st.write("""
    O percentual de rejeitos da coleta seletiva representa a quantidade de materiais
    que são separados para reciclagem, mas acabam sendo considerados inadequados para
    o reaproveitamento e precisam receber outra destinação,
    geralmente sendo encaminhados ao aterro sanitário.

    Isso pode acontecer quando materiais não recicláveis são colocados junto aos 
    recicláveis ou quando os resíduos chegam contaminados por restos de alimentos,
    gordura e outros materiais que dificultam o processo de separação.

    Diferente do índice de reciclagem, quanto menor o percentual dos rejeitos de coleta 
    melhor, pois significa que uma parcela menor dos materiais encaminhados à
    coleta seletiva está sendo descartada como rejeito.
    Separar corretamente os resíduos em casa é uma atitude simples que ajuda a reduzir esse problema.

    No gráfico a seguir, os dois valores representam a porcentagem total de resíduos rejeitados na coleta, 
    e também mostrando a previsão dos respectivos anos.
    """)
    
    st.altair_chart(grafico_rejeitos, width='stretch')

    st.info("""
    Em Curitiba, os dados mostram que o percentual de rejeitos foi de 33.44% em 2021, menor do que era a prévia de 35%.
    Caiu para 28% em 2022, porém a prévia era de 25%. Subiu para 35% em 2023, ficando ainda mais distante da prévia daquele ano
    que era de 20%, e chegou a 30% em 2024, continuando distante da prévia que dessa vez era de 15%.
    Isso demonstra que ainda existe um desafio importante na separação correta dos resíduos em Curitiba.
    """)

def criar_grafico_aterro():
    df = pd.read_csv("dados/residuos_depositados.csv")

    df["ano"] = df["ano"].astype(str)

    df_linhas = df.melt(id_vars="ano", value_vars=["residuos_depositados", "meta"], var_name="tipo", value_name="percentual")

    df_linhas["tipo"] = df_linhas["tipo"].replace({"residuos_depositados": "Resultado realizado", "meta": "Meta"})

    grafico_aterro = alt.Chart(df_linhas).mark_line(point=True).encode(
        x=alt.X("ano:N", title="Ano", axis=alt.Axis(labelAngle=0)),
        y=alt.Y("percentual:Q", title="Resíduos destinados ao aterro (%)", scale=alt.Scale(domain=[88, 95]),
        axis=alt.Axis(values=[88, 89, 90, 91, 92, 93, 94, 95], labelExpr="datum.value + '%'")),
        color=alt.Color("tipo:N", title="Indicador"),
        strokeDash=alt.StrokeDash("tipo:N", title="Indicador", scale=alt.Scale(domain=["Resultado realizado", "Meta"], range=[[1, 0], [6, 4]])),
        tooltip=[alt.Tooltip("ano:N", title="Ano"), alt.Tooltip("tipo:N", title="Tipo"),
        alt.Tooltip("percentual:Q", title="Percentual", format=".2f")]
    ).properties(width=500, height=300).interactive()

    st.subheader("Resíduos destinados ao aterro sanitário")

    st.write("""
    Este indicador apresenta o percentual de resíduos destinados ao aterro sanitário em Curitiba,
    permitindo comparar os resultados registrados em cada ano com as metas estabelecidas pelo município.

    É importante destacar que os valores apresentados como meta representam objetivos planejados,
    enquanto os demais correspondem aos resultados efetivamente registrados.

    Essa comparação permite observar a diferença entre o planejamento e os resultados alcançados.
    Além disso, é importante lembrar que a redução da quantidade de resíduos enviados aos aterros,
    por meio da prevenção, reutilização e reciclagem, também é fundamental para uma gestão mais sustentável.
    """)

    st.altair_chart(grafico_aterro, width="stretch")

    st.info("""
    Em 2022, Curitiba registrou 93% de resíduos destinados ao aterro, enquanto a meta era de 92%.
    Em 2023, o resultado foi de 91,66%, diante de uma meta de 90%.  Já em 2024, o percentual chegou a 91,82%,
    mantendo-se próximo da meta estabelecida, também de 90%.
    """)

def criar_grafico_destinacao():
    df = pd.read_csv("dados/destinacao_inadequada.csv")

    df["ano"] = df["ano"].astype(str)

    df_linhas = df.melt(id_vars="ano", value_vars=["destinacao_inadequada", "meta"], var_name="tipo", value_name="quantidade")

    df_linhas["tipo"] = df_linhas["tipo"].replace({"destinacao_inadequada": "Lugares registrados", "meta": "Meta"})

    grafico_destinacao = alt.Chart(df_linhas).mark_line(point=True).encode(
        x=alt.X("ano:N", title="Ano", axis=alt.Axis(labelAngle=0)),
        y=alt.Y("quantidade:Q", title="Áreas com destinação inadequada de resíduos", scale=alt.Scale(domain=[45, 85]),), 
        color=alt.Color("tipo:N", title="Indicador"),
        strokeDash=alt.StrokeDash("tipo:N", title="Indicador", scale=alt.Scale(domain=["Lugares registrados", "Meta"], range=[[1, 0], [6, 4]])),
        tooltip=[alt.Tooltip("ano:N", title="Ano"), alt.Tooltip("tipo:N", title="Tipo"),
        alt.Tooltip("quantidade:Q", title="Quantidade")]
    ).properties(width=500, height=350).interactive()

    st.subheader("Números de locais como áreas de destinação inadequada de resíduos")

    st.write("""
    Este indicador apresenta a quantidade de locais identificados em Curitiba onde ocorre a destinação inadequada de resíduos.
    O objetivo estabelecido pelo município era reduzir esses pontos de 81 para 50 até 2024, contribuindo para uma cidade mais
    limpa e para a diminuição dos impactos ambientais causados pelo descarte irregular.

    A presença desses locais pode causar problemas como poluição do solo e da água, proliferação de animais transmissores
    de doenças e degradação dos espaços urbanos. Por isso, além das ações de fiscalização e da implantação de Ecopontos,
    é fundamental que a população faça o descarte correto dos resíduos e utilize os serviços de coleta disponíveis.
    """)

    st.altair_chart(grafico_destinacao, width="stretch")

    st.info("""
    Em 2021, foram registrados 81 locais, exatamente o número previsto na meta daquele ano. Em 2022,
    esse total caiu para 59, atingindo a meta de 70 locais. Em 2023, houve uma nova redução,
    chegando a 51 locais, também superando a meta estabelecida de 60.

    Entretanto, em 2024, o número aumentou para 70 locais, não atingindo a meta de 50.
    Esse resultado demonstra que, apesar dos avanços observados nos anos anteriores,
    ainda existem desafios para manter a redução dos pontos de descarte inadequado.
    """)

def criar_grafico_arvores():
    df = pd.read_csv("dados/arvores_curitiba.csv")

    df["ano"] = df["ano"].astype(str)

    df_linhas = df.melt(id_vars="ano", value_vars=["arvores", "meta"], var_name="tipo", value_name="quantidade")

    df_linhas["tipo"] = df_linhas["tipo"].replace({"arvores": "Árvores plantadas", "meta": "Meta"})

    grafico_arvores = alt.Chart(df_linhas).mark_line(point=True).encode(
        x=alt.X("ano:N", title="Ano", axis=alt.Axis(labelAngle=0)),
        y=alt.Y("quantidade:Q", title="Árvores plantadas", scale=alt.Scale(domain=[25000, 575000]), 
        axis=alt.Axis(values=[50000, 150000, 250000, 350000, 450000, 555000])),
        color=alt.Color("tipo:N", title="Indicador"),
        strokeDash=alt.StrokeDash("tipo:N", title="Indicador", scale=alt.Scale(domain=["árvores plantadas", "Meta"], range=[[1, 0], [6, 4]])),
        tooltip=[alt.Tooltip("ano:N", title="Ano"), alt.Tooltip("tipo:N", title="Tipo"),
        alt.Tooltip("quantidade:Q", title="Quantidade")]
    ).properties(width=500, height=350).interactive()

    st.subheader("Além dos resíduos: Árvores e infraestrutura verde em Curitiba🌳")

    st.write("""
    Por que esse indicador está aqui? Embora não esteja diretamente relacionado à gestão de resíduos, 
    ele amplia a discussão sobre sustentabilidade urbana. Afinal, uma cidade mais sustentável não é apenas aquela que descarta menos lixo,
    mas também aquela que investe na preservação ambiental e na melhoria da qualidade de vida de seus habitantes.

    As árvores desempenham funções importantes no ambiente urbano: proporcionam sombra,
    ajudam a reduzir a temperatura, contribuem para a qualidade do ar,
    favorecem a biodiversidade e tornam os espaços públicos mais agradáveis.

    Este gráfico apresenta a contribuição de Curitiba para o incremento da infraestrutura verde por meio do plantio de árvores.
    A meta estabelecida era contribuir com 200 mil árvores até 2024,
    buscando ampliar a presença de áreas verdes e fortalecer os benefícios ambientais proporcionados pela vegetação.
    """)

    st.altair_chart(grafico_arvores, width="stretch")

    st.info("""
    Em 2021, foram registradas 64 mil árvores, superando a meta de 50 mil. Em 2022, o número chegou a 164.779,
    enquanto a meta era de 100 mil. Em 2023, foram contabilizadas 309.256 árvores, diante de uma meta de 150 mil. Já em 2024,
    foram plantadas 532.871 árvores, ultrapassando significativamente a meta de 200 mil.
    
    Os resultados demonstram que Curitiba superou as metas estabelecidas em todos os anos apresentados,
    com um crescimento expressivo ao longo do período.
    """)

def exibir_conclusão():
    st.title("Conclusão: construir uma Curitiba mais sustentável depende de todos nós 🌱")
    
    st.write("""
    Ao observar os indicadores apresentados, podemos perceber que Curitiba alcançou avanços importantes
    em algumas áreas da gestão ambiental, mas também continua enfrentando desafios. 
    Os dados mostram melhorias no índice de reciclagem e na redução dos locais de descarte inadequado entre 2021 e 2023.
    Por outro lado, o aumento desses pontos em 2024 reforça a importância de manter ações contínuas de conscientização,
    fiscalização e destinação correta dos resíduos.

    Também vimos que a sustentabilidade vai além do cuidado com o lixo. O crescimento do número de árvores
    registrado no período demonstra a importância de iniciativas que contribuem para ampliar a infraestrutura
    verde e melhorar a qualidade de vida na cidade.

    Esses indicadores nos ajudam a compreender que a construção de uma cidade mais sustentável depende
    tanto das políticas públicas quanto das atitudes de cada cidadão. Separar corretamente os resíduos, evitar o desperdício,
    reutilizar materiais e utilizar os pontos de coleta disponíveis são exemplos de pequenas ações que,
    quando praticadas coletivamente, podem gerar grandes mudanças.

    Mais do que observar números e gráficos, o importante é entender que nossas escolhas fazem parte da transformação da cidade.
    Uma Curitiba mais limpa, verde e sustentável começa também com as atitudes de cada um de nós!
    """)

    st.image("imagens/curitiba_sustentavel.jpg", width=700)

    st.success("""Uma cidade mais sustentável é construída com atitudes conscientes,
    cuidado com os resíduos e preservação dos espaços verdes!🪴""")
