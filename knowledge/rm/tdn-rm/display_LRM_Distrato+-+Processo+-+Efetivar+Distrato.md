---
content_hash: e6e5d4db78370a86d200687a67df586586988a273deb0ec6225ad67b415536b4
fetched_at: '2026-06-29T00:09:47.092209+00:00'
page_id: '435104918'
product: rm
source: tdn-rm
title: Distrato - Processo - Efetivar Distrato
type: documentation
url: https://tdn.totvs.com/display/LRM/Distrato+-+Processo+-+Efetivar+Distrato
version: 3
---

Após executar o processo Efetivar Distrato, o Distrato passar a ter como Situação do distrato Efetivado.

Os lançamentos financeiros da Venda  serão bloqueados e os lançamentos do Distrato serão desbloqueados

## Parcelas de Pagamento e Efetivação do Distrato

A seção "Parcelas de Pagamento" está disponível a partir da versão **2602**.

**Parcelas de Pagamento:** Foi criada a seção de **Parcelas de Pagamento** para os lançamentos do distrato. Esta tela funciona como uma "foto" (um registro histórico) exata das parcelas no momento da operação.

* **Importante:** É justamente a criação deste registro que possibilita executar o processo de **Desfazer a Efetivação** de um distrato, pois o sistema consegue restaurar os dados com base nessa "foto".

**Comportamento das Parcelas da Venda ao Efetivar o Distrato** O status que as parcelas da venda assumirão após a efetivação do distrato depende da seguinte parametrização:

**Caminho:** `Ambiente > Parâmetros > Gestão De Imóveis > 22.02 - Contrato de venda > 22.02.06 Plano de financiamento > Plano de financiamento`

* **Parâmetro (CANCELAR PARCELAS DA VENDA AO EFETIVAR DISTRATO) DESMARCADO:** O sistema terá o comportamento de preencher o status das parcelas da venda como **Bloqueado** ao efetivar o distrato.
* **Parâmetro (CANCELAR PARCELAS DA VENDA AO EFETIVAR DISTRATO) MARCADO:** O sistema terá o comportamento de cancelar as parcelas da venda ao efetivar o distrato.
