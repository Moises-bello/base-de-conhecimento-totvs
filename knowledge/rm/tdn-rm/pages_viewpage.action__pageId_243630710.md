---
content_hash: f6ceb242ef340b7d36443a75441f2396c62f79395b6096d87e88ef8f6f8d6775
fetched_at: '2026-06-29T00:08:11.891360+00:00'
page_id: '243630710'
product: rm
source: tdn-rm
title: RPT00035 - Sub-Relatórios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243630710
version: 46
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       Esta página tem por finalidade descrever a usabilidade do controle Sub-relatório utilizada no Reports.

# Introdução:

---

       O controle Sub-Relatório possibilita a inclusão de um ou mais relatórios na estrutura de um relatório principal.

       Informações úteis sobre o funcionamento de sub-relatórios:

* A ferramenta não transfere ao sub-relatório o filtro cadastrado no relatório principal. Ele transfere apenas a chave da tabela da banda em que o sub-relatório está inserido.
* Relatórios filhos baseados em consultas SQL que esperam parâmetros do relatório pai, não podem possuir campos em sua estrutura com a mesma nomenclatura do parâmetro do relatório pai.

       Para exemplificarmos a utilização desse controle chamaremos o relatório principal de relatório “Pai” e qualquer relatório acionado pelo controle Sub-Relatório de relatório “Filho”

# Exemplos:

---

falseExemplosExemplo 1Exemplo 1Exemplo 1

       Criamos o relatório ***pai*** com a seguinte estrutura:

       Detalhe1 – Tabela de Seções (PSECAO).

       -- RodapédoDetalhe1 - Incluso o controle Sub-Relatório.

Obs.: Para inclusão do controle Sub-Relatório:

       Acesse o menu “Caixa de Ferramentas | Controles Avançados”, selecione o controle “Sub-Relatório”. Clique sobre o controle e mantendo o botão esquerdo do mouse pressionado, arraste o controle para o local desejado da estrutura do relatório.

false

Caso o menu “Caixa de Ferramentas” não esteja visível acesse o menu “Exibição | Janelas | Caixa de Ferramentas”.

       Em seguida foi criado o relatório ***filho*** com a seguinte estrutura:  
       Detalhe1 – Tabela de Funcionários (PFUNC).

       Concluído a elaboração dos relatórios filho é necessário fazer associação de ambos através do controle Sub-Relatório.

Obs.: Como realizar a associação do relatório filho no Sub-Relatório

       Para realizar a associação do relatório filho ao controle Sub-Relatório, clique sobre o controle e acesse suas propriedades pela smart tag, clique sobre a caixa na propriedade "relatório" e em reticências na pesquisa pelo registro.

       Ou selecione o controle e tecle F4 para apresentação das propriedades do controle. Na grade de propriedades selecione “Dados | Relatório”. Na caixa de pesquisas procure pelo código do relatório filho.

       Concluída a escolha do relatório lembre-se de informar qual o “Caminho” (relacionamento entre as tabelas dos relatórios) será utilizado.

       Concluída a associação dos relatórios através do controle Sub-Relatório, basta gera-lo. Ao final do nosso exemplo, no preview, teremos o relatório pai grifado na cor laranja e as informações do relatório filho em azul.

Exemplo 2Exemplo 2Exemplo 2

       No exemplo seguinte vamos utilizar um relatório com mais bandas e com o relatório filho constituído por consulta SQL a fim de exemplificarmos a passagem de parâmetros do relatório pai para filho.

       No relatório pai utilizaremos a seguinte estrutura;

       - Detalhe1 – Tabela de Seções (PSECAO).

       -- Sub-Detalhe1 – Sem ligação.

       ---- Detalhe2 – Controle Sub-Relatório.

Obs.: Para inclusão do controle Sub-Relatório:

       Acesse o menu “Caixa de Ferramentas | Controles Avançados”, selecione o controle “Sub-Relatório”. Clique sobre o controle e mantendo o botão esquerdo do mouse pressionado, arraste o controle para o local desejado da estrutura do relatório.

false

Caso o menu “Caixa de Ferramentas” não esteja visível acesse o menu “Exibição | Janelas | Caixa de Ferramentas”.

       No relatório filho, criaremos uma consulta SQL para retornar as informações do relatório. A consulta SQL terá o seguinte contexto;

sql

       Na consulta SQL acima retornaremos dados dos funcionários de uma determinada seção. Utilizaremos o campo CODIGO1 como parâmetro para definir de qual seção os funcionários litados são correspondentes. Este campo, CODIGO1 (Código identificador da seção) está incluso no relatório pai.

Obs.: Como realizar a associação do relatório filho no Sub-Relatório

       Para realizar a associação do relatório filho ao controle Sub-Relatório, clique sobre o controle e acesse suas propriedades pela smart tag, clique sobre a caixa na propriedade "relatório" e em reticências na pesquisa pelo registro.

       Ou selecione o controle e tecle F4 para apresentação das propriedades do controle. Na grade de propriedades selecione “Dados | Relatório”. Na caixa de pesquisas procure pelo código do relatório filho.

       Diferente do relatório constituído por campo da base, quando fazemos a associação do relatório filho através do controle “Sub-relatório” não é necessário informar o “caminho”, o próprio campo do relatório pai utilizado como parâmetro na consulta SQL do relatório filho fará essa função.

|  |  |
| --- | --- |

       Concluída a associação do relatório pai com relatório filho através do controle “Sub-Relatório”, basta salvar e gera-lo. Ao final do nosso exemplo, no preview, teremos o relatório pai grifado na cor verde e as informações do relatório filho em vermelha.

false

       Reforçamos que relatórios filhos baseados em consultas SQL que esperam parâmetros do relatório pai, não podem possuir campos em sua estrutura com a mesma nomenclatura do parâmetro do relatório pai.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.XX

false

**Processo:** Sub- Relatórios

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
