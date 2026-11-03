---
content_hash: 951d51e161a1973b1d1932b1ebf25ef5a39c9a6d5ac25df2f95fceaef7bb7509
fetched_at: '2026-06-29T00:05:56.608481+00:00'
page_id: '155582692'
product: rm
source: tdn-rm
title: Visualização de parâmetro impresso em campo de relatório reports
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=155582692
version: 7
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                         **Versão:**11.82 |
| **Processo** | **:** | Reports Parâmetros |
| **Subprocesso** | **:** | Visualização de parâmetro em campo de um relatório |
| **Data da publicação** | **:** | 25/08/2014 |

**Visualização de parâmetro (impresso) em campo de relatório (reports)**

Este procedimento permitirá visualizar impreso em um relatório o resultado de um parâmetro retornado através de uma consulta SQL.

Para realizar este procedimento siga as orientações disponibilizadas abaixo.

**1)** Inclua uma consulta SQL que possua um parâmetro:

**Ex: SELECT \* FROM PFUNC WHERE DATAADMISSAO =:DATAADIMIS\_D**

**2)** Acesse o Menu Gestão e insita um novo relatório (Reports) -> Adicione a consulta ao mesmo:

**3)** Clique na coluna Lista de Campos e insira um novo parâmetro

**4)** Renomeie o Parâmetro nas propriedades, lembre-se que o nome do parâmetro deverá ser o mesmo informado na consulta SQL.

Para relembrarmos veja a consulta: SELECT \* FROM PFUNC WHERE DATAADMISSAO =:**DATAADIMIS\_D**

**5)** Ao retornar para a lista de Campos observe que o o parâmetro já se encontra-rá renomeado.

**6)** Inclua um Texto no relatório. Este texto será associado ao parâmetro, ou seja, **será o campo que irá retornar o valor inserido no parâmetro no momento da geração do relatório.**

**7)** Para associar o Parâmetro no campo clique nas propriedades deste campo Texto e realizar a ligação com o parâmetro.

**8)** Para uma melhor visualização dos dados que serão gerados no relatório inclua um campo Nome e Chapa (conforme exemplo).

**9)** Salve as configurações realizadas e realize a geração do relatório informando o parâmetro no ato da geração.

**10)** O relatório será gerado imprimindo a data informada no parâmetro:
