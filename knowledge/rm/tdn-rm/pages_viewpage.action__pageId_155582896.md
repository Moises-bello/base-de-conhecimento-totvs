---
content_hash: 36fab39507da086e60ffce43b72ca7270174c20eaced1a36c6ac8636df54ac97
fetched_at: '2026-06-29T00:05:56.636840+00:00'
page_id: '155582896'
product: rm
source: tdn-rm
title: Stored Procedure em Relatório Delphi
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=155582896
version: 3
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                         **Versão:**11.82 |
| **Processo** | **:** | Gerador de Relatórios Delphi |
| **Subprocesso** | **:** | Como utilizar Stored Procedure em Relatório Delphi |
| **Data da publicação** | **:** | 26/08/2014 |

Crie a procedure em seu banco de dados (exemplo anexo - procedure.sql):

Crie uma consulta SQL para o retorno dos dados no relatório delphi:

**Observação:** Neste exemplo, se a tabela não for criada antes de salvar a consulta sql, pode ser apresentada uma mensagem informando que não existe tal tabela.

Para que isso não ocorra, a tabela deve ser criada no Banco de Dados:

Execute a procedure, dessa forma a tabela será criada e não ocorrerá erro ao salvar a consulta SQL.

No Gerador de Relatórios, crie um relatório e selecione o menu Editar:

Selecione o Menu "Editar configurações do relatório":

No campo "Stored Procedure", informe o nome da Stored Procedure a ser utilizada:

**Observação:** Neste exemplo, a Stored Procedure será executa apenas uma vez, ao gerar o relatório.

Caso deseje que a mesma seja executa, por exemplo, para cada LD, a Stored Procedure deverá ser inserida em um grupo no relatório, através do menu inserir -> Stored Procedure:

Localize a Stored Procedure:

Adicione a consulta SQl criada anteriormente na estrutura do relatório:

Ao gerar o relatório, será solicitado o parâmetro exigido na Stored Procedure:

Neste exemplo a Stored Procedure será executada com o parâmetro de situação igual a 'A', ou seja, será executada para os funcionários com codsituacao diferente de Ativo, pois ao executar a Stored Procedure, a mesma realiza a consulta abaixo.

Note que a condição é "diferente de" (**<>**), onde a nomenclatura para o parâmetro em SQL é "**@**" e Oracle é "**I**", de Inglês:

Relatório gerado:

Exemplo Stored Procedure:

Exemplo Relatório Delphi:

|  |  |
| --- | --- |
|  | **Para maiores informações:**  Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)    **COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****    **Canais de Atendimento:**  **Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha). |
