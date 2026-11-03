---
content_hash: b748510337861d281abb66f1258324f4e7dcf86735d905ed874fddda796eff20
fetched_at: '2026-06-29T00:11:10.168730+00:00'
page_id: '641695095'
product: rm
source: tdn-rm
title: FISCAL01-16339 DT Envio do Evento do Comprovante de Entrega da NF-e
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-16339+DT+Envio+do+Evento+do+Comprovante+de+Entrega+da+NF-e
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Envio do Evento da NF-e |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-15372 |

## **02. SITUAÇÃO/REQUISITO**

Gerar e transmitir o Evento de Comprovante de Entrega da NF-e

## **03. SOLUÇÃO**

Foi implementado o envio do Comprovante de entrega da NF-e padrão TSS e Sefaz.

Em ***RM → Backoffice → Gestão de Estoque, Compras e Faturamento → Vendas → Faturamento → SPED (Estadual) → Processos → Envio de Eventos*** foi implementado a opção de enviar o evento Comprovante de Entrega da NF-e

* Regras do Processo:

1. Só é possível enviar 1 evento do tipo comprovante de entrega da NF-e por vez.
2. Só é permitido envio do evento para documento modelo 55 NF-e.
3. Na tag dhEntrega será preenchido com a concatenação dos campos Data da Entrega + Hora da Entrega + Time Zone conforme parametrização Ambiente Evento do campo Identificação do Horário.

* Regras da Tela do Processo:

1. O campo Documento deve ser preenchido somente com números.
2. O campo Latitude pode ser preenchido com a coordenada GPS em decimal com valores de -90 a 90.
3. O campo Longitude pode ser preenchido com a coordenada GPS em decimal com valores de -180 a 180.

Tela do preenchimento do Evento:

# →
