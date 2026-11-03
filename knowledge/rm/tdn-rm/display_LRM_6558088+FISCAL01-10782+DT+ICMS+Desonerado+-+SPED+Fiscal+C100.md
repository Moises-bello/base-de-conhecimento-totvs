---
content_hash: e378d062c6b1d0dad4c998cf4f07088267dd2ccee69cd067eafb47cc5a38b629
fetched_at: '2026-06-29T00:10:27.702366+00:00'
page_id: '516634247'
product: rm
source: tdn-rm
title: 6558088 FISCAL01-10782 DT ICMS Desonerado - SPED Fiscal C100
type: documentation
url: https://tdn.totvs.com/display/LRM/6558088+FISCAL01-10782+DT+ICMS+Desonerado+-+SPED+Fiscal+C100
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | SPED Fiscal |
| Ticket: | FISCAL01-10782 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-10782 |

## **02. SITUAÇÃO/REQUISITO**

Ao escriturar o movimento com duas CFOPs o sistema diminui o valor do ICMS Desonerado do campo Valor Total da Situação tributária. Porém, ao escriturar um movimento com apenas uma CFOP o valor do ICMS Desonerado não afetou o campo Valor total da situação tributária. Segundo o cliente, o ICMS desonerado não deve afetar o valor total da situação tributária. Segundo ele, a Sefaz do RJ permite emitir NF sem descontar o desonerado do valor total da NF. Legislação: Nota Técnica 2016.002 – Página 62. Exeção 3 (NT 2013/005 V 1.22): Essa validação não deverá causar rejeição caso não tenha sido subtraído o valor do ICMS Desonerado (vICMSDeson) do valor total da NF-e. ![]([https://atendimento.totvs.com/attachments/token/3wsvJJ8AzV1MXm3wcqGPCgOBt/?name=image002.png](https://atendimento.totvs.com/attachments/token/3wsvJJ8AzV1MXm3wcqGPCgOBt/?name=image002.png "Follow link"))

## **03. SOLUÇÃO**

Ajuste na geração do campo VL\_ABAT\_NT, do registro C100 no SPED, onde agora será consistido o novo parâmetro "ICMS Deson. NÃO afeta Valor Contábil", na Regra de ICMS da CFOP. Caso ela esteja marcada, o valor do ICMS Desonerado não será considerada na totalização deste campo.
