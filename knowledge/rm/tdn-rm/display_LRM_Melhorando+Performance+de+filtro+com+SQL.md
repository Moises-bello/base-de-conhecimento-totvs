---
content_hash: bb997d3cd343c07b958d0b7d69b936f6369ecf89debd2ac8d4ec4763036da8bc
fetched_at: '2026-06-29T00:05:59.341356+00:00'
page_id: '189312730'
product: rm
source: tdn-rm
title: Melhorando Performance de filtro com SQL
type: documentation
url: https://tdn.totvs.com/display/LRM/Melhorando+Performance+de+filtro+com+SQL
version: 7
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Framework |
| **Processo** | **:** | Filtro de Action |
| **Subprocesso** | **:** | Utilizando filtro com SQL |
| **Data da publicação** | **:** | 15/06/2015 |

|  |  |
| --- | --- |
| Status do Documento: | Em Produção |
| Data: | 15/06/2015 |
| Versão: | 1.0 |
| Versão Anterior: | 1.0 |
| Autores: | [Diego Henrique Almeida de Oliveira](http://tdn.totvs.com/display/~diego.henrique)  [Fábio Augusto Amaral Melo Nunes](http://tdn.totvs.com/display/~fabio.nunes)  [Welbert Marques Silva](http://tdn.totvs.com/display/~welbert.silva)  [Wesley Avelino De Carvalho](http://tdn.totvs.com/display/~wesley.carvalho) |

# Objetivo

Ao utilizar um filtro de visão que possua como parâmetro o operador IN(SQL) ou NOT IN (SQL), corre-se o risco de tornar a visualização extremamente lenta. Isso ocorre devido a independência das Sentenças geradas na execução do banco de dados.

Toda visão ao ser carregada, executa uma Consulta no banco de dados. Quando os operadores IN(SQL) ou NOT IN(SQL) são utilizados, uma Sentença SQL é montada. A Sentença gerada ao abrir a visão é mesclada com a Sentença inserida no operador do filtro, para então, executar a Consulta no banco de dados.

Pelo fato das sentenças (da visão e a do operador SQL) não possuírem nenhuma conexão, o plano de execução gerado pelo SGBD não será adequado. Por esse fato ocorrem casos de extrema lentidão quando usuários executam este processo.

Para que isso não ocorra, é necessário adaptar a Consulta SQL utilizada com o operador escolhido, otimizando-a de forma que exista uma conexão entre as Sentenças SQL.

# Caso Inadequado

Este é o caso **Inadequado** e comumente utilizado

DeckPasso 1

Acesse “Serviços Globais | Gestão | Visões de Dados” e insira a seguinte consulta SQL:

Passo 2

Agora acesse “Serviços Globais | Administração | Coligadas” e selecione “Novo filtro”:

Passo 3

Na edição do filtro selecione o campo Código, o operador IN(SQL) e a consulta criada anteriormente (SUBQUERY):

Passo 4

Este modo é inadequado, pois não possui conexão com a Sentença da action. Como exemplo, considere a imagem abaixo como a Sentença gerada. Em negrito destacamos a sentença gerada pela action e sublinhado a Sentença adicionada pelo filtro. Em vermelho, encontra-se a linha que pode ser otimizada. Percebe-se que a “SUBQUERY” não possui conexão com a Sentença principal, isso torna a consulta do SGBD muito mais lenta.

# Caso Adequado

Este é o caso **Adequado** e recomendado para melhor performance do sistema.

Deck2Passo 1

Acesse “Serviços Globais | Gestão | Visões de Dados” e insira a seguinte consulta SQL:

Ao clicar em salvar, o sistema ira retornar uma mensagem de aviso pois ela não possui a tabela GCOLIGADA como parâmetro, clique em Sim e salve a consulta:

Passo 2

Agora acesse “Serviços Globais | Administração | Coligadas” e selecione “Novo filtro”:

Passo 3

Na edição do filtro selecione o campo Código, o operador IN(SQL) e a consulta criada anteriormente (SUBQUERY):

Passo 4

Este modo é o mais adequado, pois possui conexão com a Sentença da action. Como exemplo, considere a imagem abaixo como a Sentença que é gerada. Em negrito destacamos a sentença gerada pela action e sublinhado a Sentença adicionada pelo filtro. Em vermelho, encontra-se a linha que foi otimizada para melhorar a performance da Sentença, consequentemente uma resposta melhor do sistema ao se utilizar tais tipos de filtro.

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/GLB/GLB.Perfis.aspx)

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha)
