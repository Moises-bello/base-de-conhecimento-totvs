---
content_hash: 287f0f9f56d9e47c7b6fce9d141d35b8aaf6edd346a02434f8cf0281cfb22db5
fetched_at: '2026-06-29T00:11:37.453465+00:00'
page_id: '777935872'
product: rm
source: tdn-rm
title: DT - Avisos Automáticos - Férias em dobro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=777935872
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Avisos Automáticos |
| País: | Brasil |
| Story | [DRHCALCRM-3111](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-3111) |

## **01.** **VERSÕES**

**A partir da Versão:**

* + **12.1.2310.1**

## **02. SITUAÇÃO/REQUISITO**

Ao realizar o processo de aviso automático de férias em dobro, o sistema não está considerando a data limite início de gozo, e sim a data Fim do período aquisitivo para o disparo do email e também não respeita a quantidade de dias informado no campo "Nro. Dias Ref".

## **03. SOLUÇÃO**

Possibilitar que o aviso automático de férias em dobro seja enviado, considerando a data limite de gozo das férias e a quantidade de dias informada no campo "Nro. Dias Ref".

## **07. EXEMPLO**

Vamos considerar o funcionário com os períodos de férias cadastrados  (Férias em Dobro à vencer):

Log de período de férias (Vencimento de férias em Dobro):

Em **RM| RH|Folha de Pagamento|Configurações|Comunicação|Avisos Automáticos**, foi cadastrado o envio de  e-mail - **Tipo** **3 - Férias em Dobro**:

Após clicar em '**Enviar Mensagens**', foi disparado o e-mail para o chefe cadastrado:

## **06.** **ASSUNTOS RELACIONADOS**

* [Avisos Automáticos](https://tdn.totvs.com/pages/viewpage.action?pageId=126190652)
* [Parametrização - Avisos Automáticos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024969912-RH-RM-FOP-Parametriza%C3%A7%C3%A3o-de-Avisos-Autom%C3%A1ticos)
