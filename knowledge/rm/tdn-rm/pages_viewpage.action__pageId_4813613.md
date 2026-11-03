---
content_hash: 2da6e477903c7f816143d009cce86a178cd677ef414bec76f138dc9c463bc9cb
fetched_at: '2026-06-29T00:10:19.391188+00:00'
page_id: '4813613'
product: rm
source: tdn-rm
title: Gráfico – Clientes TOP 5 durante determinado período
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4813613
version: 6
---

BLOCK

Gráfico – Clientes TOP 5 durante determinado período

FAQ: **Gráfico – Clientes TOP 5 durante determinado período**

|  |  |
| --- | --- |
| Produto: | RM |
| Ambiente: | Unspecified |
| Versão: | 11.20 |

Avaliação

***Como Fazer***

Como parametrizar o sistema para execução de um gráfico que demonstre os 05 cliente que mais compraram durante determinado período.

Solução

***Descrição do Processo***

Tem por finalidade a obtenção de informação em forma gráfica.

É necessário que haja um critério para configuração dos Gráficos, visto que, ao utilizar uma consulta SQL muito complexa o desempenho do sistema pode ficar comprometido na execução deste gráfico.

O Gráfico será visualizado manualmente através do menu **| Gestão | Gráfico|** e execução do gráfico em questão

Importante:

- Caso a consulta vinculada ao gráfico não retorne nenhum valor o sistema emitirá a seguinte mensagem:

***[![1](http://lh5.ggpht.com/_G7KXZLoZDsY/TQItqatNiAI/AAAAAAAAFQo/gN9pZrpROGg/13_thumb.png?imgmax=800 "1")](http://lh4.ggpht.com/_G7KXZLoZDsY/TQItpOmxiEI/AAAAAAAAFQk/-f-ykd07tdU/s1600-h/13%5B1%5D.png)***

***Parametrizações Necessárias***

* Acessar diretório **| CORPORERM\RM.NET |** e clicar no ícone [![2](http://lh3.ggpht.com/_G7KXZLoZDsY/TQItr9Mh_1I/AAAAAAAAElc/rqvx135-J58/2_thumb.png?imgmax=800 "2")](http://lh4.ggpht.com/_G7KXZLoZDsY/TQItrnQXvUI/AAAAAAAAElY/f56u1hr_1Ag/s1600-h/2%5B2%5D.png) | para acessar Nova MDI. A seguir clicar no ícone | [![3](http://lh3.ggpht.com/_G7KXZLoZDsY/TQItuRj_mdI/AAAAAAAAElk/Scs95PuVnUQ/3_thumb%5B1%5D.jpg?imgmax=800 "3")](http://lh3.ggpht.com/_G7KXZLoZDsY/TQIttH88kQI/AAAAAAAAElg/FgJl6sSnSwE/s1600-h/3%5B5%5D.jpg) | e escolher opção **| Serviços Globais |**
* Acessar o menu **| Gestão | Visões de Dados |** **Inserir |** e cadastrar Consulta SQL que será considerada para geração deste Gráfico com o conteúdo:

SELECT TOP 5(COUNT(DISTINCT(T.IDMOV))) AS QTDE\_NF, FC.NOMEFANTASIA AS CLIENTE

FROM FCFO FC

INNER JOIN TMOV T ON

FC.CODCFO = T.CODCFO AND

FC.CODCOLIGADA = T.CODCOLIGADA AND

(T.DATASAIDA >=:DATA\_INICIO AND

T.DATASAIDA >=:DATA\_FIM)

INNER JOIN TTMV TT ON

T.CODCOLIGADA = TT.CODCOLIGADA AND

T.CODTMV = T.CODTMV AND

TT.CLASSIFICACAO IN ('04.08.02', '04.08.03')

GROUP BY FC.NOMEFANTASIA

ORDER BY QTDE\_NF DESC

Importante:

- A consulta em questão demonstra a quantidade de Notas Fiscais emitidas para determinado cliente, ou seja, os cinco clientes que mais compraram no período informado.

- Foram considerados como tipo de movimento para emissão de Notas Fiscais de Venda, movimentos cuja etapa **| Mov-Identificação|,** parâmetro **|** **Classificação |** está informado *Faturamento ou Exportação**,*** que no banco de dados correspondem consecutivamente a *'04.08.02'* e *'04.08.03'*.

- Acessar menu **| Gestão**, clicar no ícone |[![4](http://lh6.ggpht.com/_G7KXZLoZDsY/TQItwoCt4iI/AAAAAAAAEls/IAGMlCBQGVU/4_thumb%5B1%5D.jpg?imgmax=800 "4")](http://lh3.ggpht.com/_G7KXZLoZDsY/TQItvlj2AvI/AAAAAAAAElo/orum-R44fS8/s1600-h/4%5B5%5D.jpg) | e escolher opção **| Incluir |** para cadastrar e configurar o Gráfico.

Ao escolher opção “Incluir Gráfico” será apresentado tela com parametrizações específicas para geração do Gráfico, onde deve ser informado:

**Aba – Identificação**

Preencher Título, Descrição, Categoria, Fonte de Dados e a Consulta SQL.

**- Consulta SQL:** campo de preenchimento obrigatório, onde o usuário tem que referenciar a consulta SQL inclusa anteriormente, onde o resultado apresentado vai determinar a montagem do Gráfico.

[![5](http://lh4.ggpht.com/_G7KXZLoZDsY/TQIt0Aa98QI/AAAAAAAAFQ0/zMMCcNL64oE/5_thumb%5B1%5D.jpg?imgmax=800 "5")](http://lh6.ggpht.com/_G7KXZLoZDsY/TQItxSpiLHI/AAAAAAAAFQw/ETpeLHElo9A/s1600-h/5%5B1%5D.jpg)

|  |
| --- |
| O usuário deve clicar em [6](http://lh4.ggpht.com/_G7KXZLoZDsY/TQIt171e5-I/AAAAAAAAEl4/Ho1eQqbBZEM/s1600-h/6%5B2%5D.jpg) e escolher a sentença SQL inclusa anteriormente no aplicativo para este fim. Esta consulta vai selecionar os movimentos que se adequam ao resultado da consulta para geração do Gráfico.  Se a consulta em questão utilizar parâmetros o usuário deverá informá-los no momento de execução do gráfico. |

Tela Configurada

[![7](http://lh3.ggpht.com/_G7KXZLoZDsY/TQIuBW2XNCI/AAAAAAAAFRI/2Q9uf_M4Jz0/7_thumb%5B1%5D.jpg?imgmax=800 "7")](http://lh6.ggpht.com/_G7KXZLoZDsY/TQIuApFBImI/AAAAAAAAFQ4/jOq-gjLq9WA/s1600-h/7%5B1%5D.jpg)

Importante:

Ao salvar a tela acima, o sistema perguntará se o usuário deseja executar o assistente de configuração de gráfico.

[![8](http://lh6.ggpht.com/_G7KXZLoZDsY/TQIuDmY9QXI/AAAAAAAAFRU/u5S5GmKp-Fg/8_thumb%5B1%5D.jpg?imgmax=800 "8")](http://lh3.ggpht.com/_G7KXZLoZDsY/TQIuCEOcZ6I/AAAAAAAAFRQ/OuEFPAiTO0U/s1600-h/8%5B1%5D.jpg)

***Configuração do Gráfico***

Depois de feitas parametrizações anteriores, o Gráfico deverá ser modelado através do wizard para sua execução posterior.

**Primeira etapa:**

Informar o tipo de gráfico a ser utilizado, no exemplo LINHAS.

[![9](http://lh3.ggpht.com/_G7KXZLoZDsY/TQIuLPV0WXI/AAAAAAAAFRk/3d9V8HSE2Uw/9_thumb%5B1%5D.jpg?imgmax=800 "9")](http://lh6.ggpht.com/_G7KXZLoZDsY/TQIuI-x0axI/AAAAAAAAFRg/wL9RkB9QVQk/s1600-h/9%5B1%5D.jpg)

Obs: o parâmetro | **Inverter linhas e colunas |** fará com que o sistema inverta os dados do eixo X com os dados do eixo Y e vice-versa.

**Segunda etapa:**

Nessa etapa, especificam-se os dados que serão visíveis no gráfico (legenda, valores, etc.)

[![10](http://lh5.ggpht.com/_G7KXZLoZDsY/TQIuTricxgI/AAAAAAAAFRs/ONLaXY0thvM/10_thumb%5B1%5D.jpg?imgmax=800 "10")](http://lh4.ggpht.com/_G7KXZLoZDsY/TQIuSz9eDwI/AAAAAAAAFRo/NZBZq4MdRQg/s1600-h/10%5B1%5D.jpg)

**Terceira etapa:**

Definição de títulos.

Para verificar o resultado da parametrização, basta concluir o processo e acessar o menu **Gestão | Gráfico|** e executar o gráfico em questão.

[![11](http://lh3.ggpht.com/_G7KXZLoZDsY/TQIuZdg3hZI/AAAAAAAAFSA/0p4vV-2MMG4/11_thumb%5B1%5D.jpg?imgmax=800 "11")](http://lh3.ggpht.com/_G7KXZLoZDsY/TQIuY5hlgsI/AAAAAAAAFR4/TW2rJVaysLQ/s1600-h/11%5B1%5D.jpg)
