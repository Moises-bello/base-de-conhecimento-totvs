---
content_hash: bdb935267f599e3e3b58d9900334655db559568fd4935cdca9c4069f6406f961
fetched_at: '2026-06-29T00:05:56.629360+00:00'
page_id: '155582819'
product: rm
source: tdn-rm
title: Stored Procedure no RM Reports com tabela máster sendo consulta sql
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=155582819
version: 5
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                         **Versão:**11.82 |
| **Processo** | **:** | Relatório .Net |
| **Subprocesso** | **:** | Stored Procedure no RM Reports com tabela máster sendo consulta sql |
| **Data da publicação** | **:** | 26/08/2014 |

Crie a procedure em seu banco de dados (exemplo anexo - procedure.sql):

Crie uma consulta SQL para o retorno dos dados no Relatório .Net:

**Observação:** Neste exemplo, se a tabela não for criada antes de salvar a consulta sql, pode ser apresentada uma mensagem informando que não existe tal tabela.

Para que isso não ocorra, a tabela deve ser criada no Banco de Dados:

Execute a procedure, dessa forma a tabela será criada e não ocorrerá erro ao salvar a consulta SQL:

Consulta SQL salva com sucesso:

Após criar um Relatório .Net, insira a consulta sql no mesmo:

Adicione os campos desejados da consulta sql ao relatório:

No Menu Ferramentas, em Controles Avançados, selecione e arraste o componente **Stored Procedure** para o Relatório e associe a Stored Procedure ao mesmo:

Crie o parâmetro conforme elaborado na Stored Procedure no Relatório .Net.

No exemplo será o @SITUACAO. Para o relatório, vamos criar o parâmetro SITUACAO.

Nas propriedades do parâmetro, escreva na descrição o mesmo nome do parâmetro relacionado à procedure sem o **@**.

Se for executar o relatório por dentro do editor, não se esqueça de inserir um valor fixo ao parâmetro **(A)**:

Neste exemplo a Stored Procedure será executada com o parâmetro de situação igual a 'A', ou seja, será executada para os funcionários com codsituacao diferente de Ativo,

pois ao executar a Stored Procedure, a mesma realiza a consulta abaixo.

Note que a condição é "diferente de" (**<>**), onde a nomenclatura para o parâmetro em SQL é "**@**" e Oracle é "**I**", de Inglês:

Por fim, salve e gere o Relatório:

Exemplo para Stored Procedure:

Exemplo para Relatório .Net:

|  |  |
| --- | --- |
|  | **Para maiores informações:**  Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)    **COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****    **Canais de Atendimento:**  **Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha). |
