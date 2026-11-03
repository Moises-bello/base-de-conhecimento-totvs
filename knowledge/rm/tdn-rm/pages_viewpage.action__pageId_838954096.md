---
content_hash: 7349802fbedb1e25564c08d430c6cb70cf5736134137bba8c990574aa1556149
fetched_at: '2026-06-29T00:11:49.813963+00:00'
page_id: '838954096'
product: rm
source: tdn-rm
title: DT - S-2206 e S-2306 - Geração da tag <vrSalFx>
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=838954096
version: 9
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | S-2206 e S-2306 - Geração da tag <vrSalFx> |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-9304](https://jiraproducao.totvs.com.br/browse/DRHROTRM-9304) |

## **02. SITUAÇÃO/REQUISITO**

O cliente observou uma inconsistência entre a informação de salário hora no cadastro do funcionário, relacionada ao salário composto, e a informação gerada no XML S-2206.

## **03. SOLUÇÃO**

Ajuste da documentação referente à geração da tag <**vrSalFx**>, que representa o "Salário base do trabalhador, correspondente à parte fixa da remuneração", nos eventos "S-2206 - Alteração de Contrato de Trabalho" e "S-2306 - Trabalhador Sem Vínculo de Emprego/Estatutário".

Com base na data da alteração registrada no evento, o sistema verificará no histórico salarial do funcionário todos os registros com datas anteriores a essa data.

Para os funcionários com salário composto, o sistema retornará o último salário de cada número de salário registrado anteriormente a essa data.

Com base no exemplo acima, o valor da tag <**vrSalFx>** será a soma de todas as linhas destacadas.

## **04. DEMAIS INFORMAÇÕES**
