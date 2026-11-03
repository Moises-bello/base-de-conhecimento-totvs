---
content_hash: 1ef5e1b015cba766838d45d0fd3ec5742d5e825a7e47b021dd812e7f7bcce07c
fetched_at: '2026-06-29T00:11:06.310650+00:00'
page_id: '633547070'
product: rm
source: tdn-rm
title: FISCAL01-15530 DT Consumir WebService e Gerar Token - Processo NFS-e
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-15530+DT+Consumir+WebService+e+Gerar+Token+-+Processo+NFS-e
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Envio, Consulta, Cancelamento da NFS-e |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-15530 |

## **02. SITUAÇÃO/REQUISITO**

Implementar autenticação do TSS nos processos da NFS-e Envio, Consulta e Cancelamento

## **03. SOLUÇÃO**

Foi implementado a Autenticação do TSS no Envio, Consulta, Cancelamento da NFS-e. contemplando a legislação da LGPD

Observações.

* Para que o processo de Autenticação seja realizado é necessário informar o Client Id e Secret nos Parâmetros da NF-e
* O TSS reconhece Autenticação a partir da versão 12.1.33
