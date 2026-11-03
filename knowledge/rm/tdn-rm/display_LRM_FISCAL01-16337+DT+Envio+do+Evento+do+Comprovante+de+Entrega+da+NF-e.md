---
content_hash: c835131fee92a4ee24e3d9c8a40581a3f8cd778b807b565a27c3bbe1fe508e21
fetched_at: '2026-06-29T00:11:09.490701+00:00'
page_id: '639951032'
product: rm
source: tdn-rm
title: FISCAL01-16337 DT Envio do Evento do Comprovante de Entrega da NF-e
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-16337+DT+Envio+do+Evento+do+Comprovante+de+Entrega+da+NF-e
version: 2
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

Adicionar o novo Evento "Comprovante de Entrega da NF-e" na tela de Envio de Eventos da NF-e.

A tela deverá apresentar os campos necessário para a geração do Evento.

## **03. SOLUÇÃO**

* Implementação da tela de processo do Evento de Comprovante de Entrega da NF-e.

Em ***RM → Backoffice → Gestão de Estoque, Compras e Faturamento → Vendas → Faturamento → SPED (Estadual) → Processos → Envio de Eventos*** foi implementado a opção de enviar o evento Comprovante de Entrega da NF-e

* O campo **UF do Autor** será preenchido com o default da UF da filial da NF-e.
* Todos os campos em negrito presente na tela devem ser preenchidos obrigatoriamente para o processo prosseguir.
* A imagem do Comprovante de Entrega deve ter algum dos seguintes formatos: jpg, jpeg, gif, bmp ou png.
