---
content_hash: 11a0da0992a37838342fdf08a6425419013961d3dd64721e68b8f51f55f06f6a
fetched_at: '2026-06-29T00:10:19.343242+00:00'
page_id: '4813439'
product: rm
source: tdn-rm
title: Gráfico – Quantidade de emissão de Notas fiscais diárias durante o mês anterior
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4813439
version: 5
---

BLOCK

Gráfico – Quantidade de emissão de Notas fiscais diárias durante o mês anterior

FAQ: **Gráfico – Quantidade de emissão de Notas fiscais diárias durante o mês anterior**

|  |  |
| --- | --- |
| Produto: | RM |
| Ambiente: | Unspecified |
| Versão: | 11.20 |

Avaliação

***Como Fazer***

Como parametrizar o sistema para execução de gráfico para visualização da quantidade de emissão de Notas Fiscais diárias durante o mês anterior.

Solução

***Descrição do Processo***

Tem por finalidade a obtenção de informação em forma gráfica.

É necessário que haja um critério para configuração dos Gráficos, visto que, ao utilizar uma consulta SQL muito complexa o desempenho do sistema pode ficar comprometido na execução deste gráfico.

O Gráfico será visualizado manualmente através do menu **| Gestão | Gráfico|** e execução do gráfico em questão

Importante:

- Caso a consulta vinculada ao gráfico não retorne nenhum valor o sistema emitirá a seguinte mensagem:

[![image](http://lh3.ggpht.com/_G7KXZLoZDsY/TQI-bRyLKTI/AAAAAAAAFKs/afGvK_DDwxk/image_thumb%5B1%5D.png?imgmax=800 "image")](http://lh4.ggpht.com/_G7KXZLoZDsY/TQI-a8G6TVI/AAAAAAAAFKk/PYb1M7YU5ME/s1600-h/image%5B1%5D.png)

***Parametrizações Necessárias***

Acessar diretório **| CORPORERM\RM.NET |** e clicar no ícone |[![image](http://lh3.ggpht.com/_G7KXZLoZDsY/TQI-cc2LHUI/AAAAAAAAEqM/nmd3ZA7uPe4/image_thumb%5B1%5D.png?imgmax=800 "image")](http://lh5.ggpht.com/_G7KXZLoZDsY/TQI-b-D3C5I/AAAAAAAAEqI/N8unciL4FNU/s1600-h/image%5B5%5D.png) | para acessar Nova MDI. A seguir clicar no ícone |[![image](http://lh5.ggpht.com/_G7KXZLoZDsY/TQI-de_V1fI/AAAAAAAAEqU/BdPA9MljWB4/image_thumb%5B2%5D.png?imgmax=800 "image")](http://lh4.ggpht.com/_G7KXZLoZDsY/TQI-c4u6irI/AAAAAAAAEqQ/YxvEdM-Lk94/s1600-h/image%5B8%5D.png) | e escolher opção **| Serviços Globais |**

Acessar o menu **| Gestão | Visões de Dados |** **Inserir |** e cadastrar Consulta SQL que será considerada para geração deste Gráfico com o conteúdo:

SELECT (DATENAME (DD,T.DATAEMISSAO) + ' / ' + CAST(DATEPART (MM, T.DATAEMISSAO) AS VARCHAR)),

COUNT(T.IDMOV) AS QUANTIDADE\_DE\_NOTAS

FROM TMOV T

INNER JOIN TTMV TT

ON T.CODCOLIGADA = TT.CODCOLIGADA AND

T.CODTMV = TT.CODTMV AND

DATEPART (MM, T.DATAEMISSAO) = (DATEPART (MM, GETDATE())-1) AND

DATEPART(YYYY, T.DATAEMISSAO) = DATEPART (YYYY, GETDATE()) AND

TT.CLASSIFICACAO IN ('04.08.02', '04.08.03')

GROUP BY T.DATAEMISSAO, DATENAME (YYYY, T.DATAEMISSAO)

ORDER BY T.DATAEMISSAO, DATENAME (YYYY, T.DATAEMISSAO)

Importante:

- A consulta em questão demonstra a quantidade de Notas Fiscais emitidas diariamente no mês anterior ao mês corrente.

- Foram considerados como tipo de movimento para emissão de Notas Fiscais, movimentos cuja etapa **| Mov-Identificação|,** parâmetro **|** **Classificação |** está informado *Faturamento ou Exportação**,*** que no banco de dados correspondem consecutivamente a *'04.08.02'* e *'04.08.03'*.

- Acessar menu **| Gestão**, clicar no ícone |[![image](http://lh3.ggpht.com/_G7KXZLoZDsY/TQI-fMic5EI/AAAAAAAAEqc/buqLV-0F4uE/image_thumb%5B3%5D.png?imgmax=800 "image")](http://lh3.ggpht.com/_G7KXZLoZDsY/TQI-d2mNleI/AAAAAAAAEqY/SpomMbLKx58/s1600-h/image%5B11%5D.png) | e escolher opção **| Incluir |** para cadastrar e configurar o Gráfico.

Ao escolher opção “Incluir Gráfico” será apresentada tela com parametrizações específicas para geração do Gráfico, onde deve ser informado:

**Aba – Identificação**

Preencher Título, Descrição, Categoria, Fonte de Dados e a Consulta SQL.

**- Consulta SQL:** campo de preenchimento obrigatório, onde o usuário tem que referenciar a consulta SQL inclusa anteriormente, onde o resultado apresentado vai determinar a montagem do Gráfico.

[![image](http://lh6.ggpht.com/_G7KXZLoZDsY/TQI-gHIzMEI/AAAAAAAAFK0/cFy_I-mfOd8/image12_thumb.png?imgmax=800 "image")](http://lh6.ggpht.com/_G7KXZLoZDsY/TQI-fqLVybI/AAAAAAAAFKw/UwRWDJHNUo8/s1600-h/image12%5B1%5D.png)

|  |
| --- |
| O usuário deve clicar em [image](http://lh6.ggpht.com/_G7KXZLoZDsY/TQI-g_g0EuI/AAAAAAAAEqo/Maf4Zsaxywc/s1600-h/image%5B17%5D.png) e escolher a sentença SQL inclusa anteriormente no aplicativo para este fim. Esta consulta vai selecionar os movimentos que se adequam ao resultado da consulta para geração do Gráfico.  Se a consulta em questão utilizar parâmetros o usuário deverá informá-los no momento de execução do gráfico. |

Tela Configurada

[![image](http://lh3.ggpht.com/_G7KXZLoZDsY/TQI-ktUq4uI/AAAAAAAAFLM/ok8bpCCCFXI/image24_thumb.png?imgmax=800 "image")](http://lh4.ggpht.com/_G7KXZLoZDsY/TQI-jl37-xI/AAAAAAAAFLA/ESnp3CIAy6Y/s1600-h/image24%5B1%5D.png)

Importante:

Ao salvar a tela acima, o sistema perguntará se o usuário deseja executar o assistente de configuração de gráfico.

[![image](http://lh3.ggpht.com/_G7KXZLoZDsY/TQI-mcVbrJI/AAAAAAAAFLY/GaZ-tAzthsU/image27_thumb.png?imgmax=800 "image")](http://lh4.ggpht.com/_G7KXZLoZDsY/TQI-l5EmV5I/AAAAAAAAFLQ/k_uYbx_lB2A/s1600-h/image27%5B1%5D.png)

***Configuração do Gráfico***

Depois de feitas parametrizações anteriores, o Gráfico deverá ser modelado através do wizard para sua execução posterior.

**Primeira etapa:**

Informar o tipo de gráfico a ser utilizado, no exemplo LINHAS.

[![image](http://lh4.ggpht.com/_G7KXZLoZDsY/TQI-qHUZqGI/AAAAAAAAFLk/mHp4gfFzx14/image30_thumb.png?imgmax=800 "image")](http://lh6.ggpht.com/_G7KXZLoZDsY/TQI-ngUhl_I/AAAAAAAAFLg/Zb3yZUVRmOw/s1600-h/image30%5B1%5D.png)

Obs: o parâmetro | **Inverter linhas e colunas |** fará com que o sistema inverta os dados do eixo X com os dados do eixo Y e vice-versa.

**Segunda etapa:**

Nessa etapa, especificam-se os dados que serão visíveis no gráfico (legenda, valores, etc.)

[![image](http://lh6.ggpht.com/_G7KXZLoZDsY/TQI-s3w0h4I/AAAAAAAAFL4/2wM91SK--HU/image33_thumb.png?imgmax=800 "image")](http://lh5.ggpht.com/_G7KXZLoZDsY/TQI-rvmYTwI/AAAAAAAAFLw/XIFsn9GuNN4/s1600-h/image33%5B1%5D.png)

**Terceira etapa:**

Definição de títulos.

Para verificar o resultado da parametrização, basta concluir o processo e acessar o menu **Gestão | Gráfico|** e executar o gráfico em questão.

[![image](http://lh6.ggpht.com/_G7KXZLoZDsY/TQI-vVHmBgI/AAAAAAAAFME/Q2PMRERXQkM/image36_thumb.png?imgmax=800 "image")](http://lh6.ggpht.com/_G7KXZLoZDsY/TQI-urktTdI/AAAAAAAAFMA/_sEnSLbbe68/s1600-h/image36%5B1%5D.png)

Observações

Link para o TOTVS Connect: http://totvsconnect.blogspot.com/2010/12/como-fazer-grafico-quantidade-de.html
