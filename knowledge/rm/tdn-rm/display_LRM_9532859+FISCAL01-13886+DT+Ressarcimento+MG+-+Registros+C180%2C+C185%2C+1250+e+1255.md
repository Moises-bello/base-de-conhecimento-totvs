---
content_hash: bed56e5883fba3e1b6968db6689ffb11e6567d66cd098bc4417d98acd8f12d46
fetched_at: '2026-06-29T00:10:50.742428+00:00'
page_id: '562965737'
product: rm
source: tdn-rm
title: 9532859 FISCAL01-13886 DT Ressarcimento MG - Registros C180, C185, 1250 e 1255
type: documentation
url: https://tdn.totvs.com/display/LRM/9532859+FISCAL01-13886+DT+Ressarcimento+MG+-+Registros+C180%2C+C185%2C+1250+e+1255
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | SPED Fiscal |
| Ticket: | 9532859 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-13886 |

## **02. SITUAÇÃO/REQUISITO**

Atualmente estávamos gerando os campos de 03 a 07 do Registro 1255, é gerado somente somando o valor dos campos 12, 15, 16, 17 e 18 do Registro C185. O correto é somar e multiplicar pela quantidade do Registro C185.

## **03. SOLUÇÃO**

Ajuste no cálculo dos campos do registro 1255 do SPED Fiscal para considerar a quantidade total, baseado no registro C185. Os campos de 03 a 07 do Registro 1255 foram gerados conforme informações dos campos 12, 15, 16, 17 e 18 do Registro C185 e multiplicados pelo campo QUANT\_CONV deste mesmo registro.
