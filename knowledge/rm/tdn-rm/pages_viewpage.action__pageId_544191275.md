---
content_hash: bae738e0030da0f6bdc3bc1561a2a83a26a20a533671065172dfb1dca8a00866
fetched_at: '2026-06-29T00:10:38.181760+00:00'
page_id: '544191275'
product: rm
source: tdn-rm
title: 8277476 FISCAL01-12635 DT - Sped Fiscal - Geração do Registro C870
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=544191275
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Sped Fiscal |
| Ticket: | 8277476 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-12635 |

## **02. SITUAÇÃO/REQUISITO**

Ao validar o Arquivo do Sped Fiscal ocorre a seguinte mensagem: "Obrigatório informar um registro H005 com o MOT\_INV igual a 06 e DT\_INV igual a um dia anterior ao DT\_INI do Registro 0000, sempre que houver ressarcimento ou complemento de ST".

Atualmente geramos o Registro C870 para todos os lançamentos Fiscais de (CF-E-SAT) (CÓDIGO 59), mas este Registros somente deve ser gerado para o Ressarcimento ou Complemento de ST.

## **03. SOLUÇÃO**

Ajuste para geração do C870 para que o mesmo respeite o parâmetro "Gerar ressarcimento/complemento ICMS ST". O mesmo somente será gerado se a flag estiver marcada.
