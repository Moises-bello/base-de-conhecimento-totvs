---
content_hash: 78bbc77982329592f841526d6072138e66958b5503122045f7e89fd7022cc733
fetched_at: '2026-06-29T00:10:41.667836+00:00'
page_id: '546263006'
product: rm
source: tdn-rm
title: FISCAL01-12830 DT SubApuração - Valor Total das Deduções
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=546263006
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Encerramento da SubApuração do Período ICMS |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-12830 |

## **02. SITUAÇÃO/REQUISITO**

O valor da dedução não é considerado na apuração da subapuração do ICMS:

VALOR APURADO NO MÊS 02/2020 - 100.493,88  
**VALOR CORRETO**  
TOTAL AJUSTE ESTORNO DE CRÉDITO 1.574,04  
TOTAL DO AJUSTE A DÉBITO 111.417,30  
TOTAL DE AJUSTE A CRÉDITO 2.994,46  
SALDO CREDOR ANTERIOR 9.050,00  
TOTAL DAS DEDUÇÕES 453,00  
SALDO APURADO 02/2020 -100.040,88

## **03. SOLUÇÃO**

No registro 1920 da EFD ICMS|IPI foi ajustado o campo (09) VL\_SLD\_APURADO\_OA para somar também o VL\_TOT\_DED (10) além do Saldo da Apuração da SubApuração.

Considerar ajuste de Dedução do Lançamento Fiscal ou Item quando o código de ajuste for 04. Exemplo: “RS04” na apuração e na rotina EFD ICMS & IPI.
