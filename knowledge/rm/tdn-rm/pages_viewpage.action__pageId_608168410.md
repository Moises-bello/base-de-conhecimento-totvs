---
content_hash: 055aa1aa34478d8ede3a7cb6376675c7423557240b0a071b92650279ecb9bf4f
fetched_at: '2026-06-29T00:10:58.958104+00:00'
page_id: '608168410'
product: rm
source: tdn-rm
title: 1055260 FISCAL01-15268 - DT NFC-e - Campo operação presencial foi preenchido
  incorretamente ou não foi preenchido.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=608168410
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | NFC-e |
| Ticket: | 11055260 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-15268 |

## **02. SITUAÇÃO/REQUISITO**

Ao enviar a NFC-e modelo 65 para a Sefaz MG de acordo com NT2020.006 a seguinte mensagem de erro abaixo está sendo apresentada.

Enviar NF-e: Erro no envio da NF-e.   
Não foi possível preencher os dados de identificação da NF-e.  
Campo operação presencial foi preenchido incorretamente ou não foi preenchido.

O sistema está barrando a transmissão de NFC-e caso a operação não seja presencial. A nota somente é enviada e autorizada quando definirmos o campo Operação Presencial como Operação Presencial ou NFC-e em operação com entrega a domicilio.

## **03. SOLUÇÃO**

As operações não presenciais não serão mais barradas pelo sistema ao realizar a transmissão da NFC-e, e sim validadas pela própria SEFAZ.
