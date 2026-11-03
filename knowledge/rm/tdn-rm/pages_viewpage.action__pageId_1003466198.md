---
content_hash: fd768f2354ec21778f58defc5eeca8f59662f59402018b9c5a161e60e93a6533
fetched_at: '2026-06-29T00:05:45.072629+00:00'
page_id: '1003466198'
product: rm
source: tdn-rm
title: DT- Integração RM X Quirons - API Exclusão de Abono AllowanceControl
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1003466198
version: 30
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | RM |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Função: | Permitir a Exclusão do Abono utilizando a API de Abono AllowanceControl |
| País: | Brasil |
| Requisito/Story/Issue: | [DRHJORNRM-8548](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-8674)  [DRHJORNRM-9155](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-9155) |

## **02. SITUAÇÃO/REQUISITO**

Ao excluir um abono no Quírons a exclusão não é efetivada no RM e não retorna mensagem para o usuário.

## **03. SOLUÇÃO**

Adequado o método Delete da API  de Abono AllowanceControle padronizado o parâmetro referente a data na  Requisição .

Importante

Exemplo da estrutura da chave para execução do Delete:  
[http://localhost:8051/api/rh/v1/allowancecontrol/1;1;1|00007;**2026-01-05T08:00:00.000Z**;08:00;1|0001](http://localhost:8051/api/rh/v1/allowancecontrol/1;1;1%7C00007;2026-01-05T08:00:00.000Z;08:00;1%7C0001)

O parâmetro de Data Inicio do Abono (5° parâmetro, em negrito), deverá ser enviado em um dos seguintes formatos aceitos:

* 2026-01-05
* 2026-01-05 08:00:00
* 2026-01-05 08:00
* 2026-01-05T08:00:00.000Z
* 2026-01-05T08:00:00Z

## **04. VERSÕES**

12.1.2502.272

12.1.2506.233

12.1.2510.161  e superiores.

## **05. UTILIZAÇÃO**

11Exemplo 1 : Excluindo Abono 

Funcionário possui Abono cadastrado na data 03/10/2025

Para a realização de testes foi utilizado a ferramenta POSTMAN . A  requisição deverá ser semelhante a imagem abaixo:

**{protocolo}://{host}/{api}/rh/v1/allowanceControl{allowanceId}**

O abono será excluído e demonstrará a seguinte mensagem 204 No Content.

Ao visualizar o espelho do funcionário o abono foi excluído.

2Exemplo 2 : Excluindo Abono Inexistente 

Funcionário não possui Abono cadastrado.

Para a realização de testes foi utilizado a ferramenta POSTMAN . A  requisição deverá ser semelhante a imagem abaixo:

**{protocolo}://{host}/{api}/rh/v1/allowanceControl{allowanceId}**

2Exemplo 3 : Mensagens de ValidaçãoImportante

As mensagens de validações serão retornadas sempre que algum campo passado que seja obrigatório não tenha sido informado na requisição ou esteja informado erroneamente.

| Retorno API | Mensagem |
| --- | --- |
| 204- No Content | "Abono foi excluido com sucesso" |
| 404- Not Found | "Abono não encontrado na base de dados" |
| 500- Internal Server Error | "Os parâmetros da requisição não foram informados corretamente" |
