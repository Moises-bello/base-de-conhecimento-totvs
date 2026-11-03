---
content_hash: ecfb5aed2edea5e2983fef0e70e619da1c59963d6c436773e9152affcd5f0e22
fetched_at: '2026-06-29T00:10:37.263052+00:00'
page_id: '538504832'
product: rm
source: tdn-rm
title: 2328080 FISCAL01-3812 DT Compensação de saldo negativo de imposto de renda
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=538504832
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Compensação de tributos federais |
| Ticket: | 2328080 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-3812 |

## **02. SITUAÇÃO/REQUISITO**

Cliente solicita implementação de compensação de tributos federais para os tipos de Crédito:

Saldo negativo de IRPJ;  
Saldo negativo de CSLL;  
Solicita também que a compensação possa ser realizada em qualquer guia de tributo federal, no exemplo o cliente necessita compensar no tributo CSRF (Retenções de PIS, COFINS e CSLL)

## **03. SOLUÇÃO**

Dado que:  
1) Existe lançamento de entrada de IRRFPJ   
2) O período de apuração do IRRFPJ foi encerrado  
3) A Guia do Período foi gerada  
4) Foi cadastrado/parametrizado a compensação de tributo federal para o IRRFPJ com o tipo: Saldo Negativo IRPJ ou CSLL  
5) Foi associada a guia do IRRFPJ gerada no encerramento do período no cadastro de compensação de tributo federal (anexo guias de débito para compensação)  
Ao executar o cálculo das compensações de tributos federais, os valores calculados (aba Valores) devem estar corretos  
E a guia DARF do período deve compensar o valor correspondente.
