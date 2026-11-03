---
content_hash: ca368b7b81f64c88be7fd17df1193cc241b5cc6e811cba82eaa13733a8ad3743
fetched_at: '2026-06-29T00:11:03.254593+00:00'
page_id: '619766741'
product: rm
source: tdn-rm
title: DT - Salário Maternidade por Adoção 13º pago pelo INSS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=619766741
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | RM |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | Totvs Folha de Pagamento |
| Função: | Parametrizador /Folha Normal / Salário Maternidade 1/2 |
| País: | Brasil |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | [FOPCALCULO01-13274](https://jiraproducao.totvs.com.br/browse/FOPCALCULO01-13274) |

## **02. SITUAÇÃO/REQUISITO**

Cliente criou uma base de cálculo de licença maternidade paga pelo INSS e enviou para o governo com o codIncCP incorreto. Agora, entrou em contato conosco questionando como fazer para gerar nesta verba o codIncCP "26 - Salário Maternidade - 13º Salário, pago pelo INSS".

## **03. SOLUÇÃO**

Criado no parametrizador em Folha Normal, Salário Maternidade 1/2, dois campos para informar os eventos “13º Salário Licença Maternidade pago pela Previdência” e “13º Rescisão Licença Maternidade pago pela Previdência”, que estarão habilitados quando o parâmetro “Salário Maternidade por adoção pago pela previdência” estiver marcado.

Os eventos serão lançados no envelope de pagamento do funcionário houver afastamento por licença maternidade e o motivo do afastamento for o mesmo cadastrado no parametrizador em Folha Normal, Salário Maternidade 2/2, campo “Motivo de afastamento ref. licença maternidade por adoção”.

Os eventos devem ser calculados pelo usuário, podendo utilizar fórmulas.

## **04. DEMAIS INFORMAÇÕES**

[Parametrizador / Folha Normal / Salário Maternidade 1/2](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719554)
