---
content_hash: 87e4058284ce89f2589bcc54a9312b575cf0d29b32b545631c3d71263da871fa
fetched_at: '2026-06-29T00:05:54.758333+00:00'
page_id: '1084164051'
product: rm
source: tdn-rm
title: Empreendimentos - Mapa revitalizado - Funcionalidades
type: documentation
url: https://tdn.totvs.com/display/LRM/Empreendimentos+-+Mapa+revitalizado+-+Funcionalidades
version: 4
---

# **Filtros e Estatísticas:**

---

O painel lateral reúne os filtros de busca, as estatísticas do empreendimento e a legenda de status.

| **Filtro** | **Descrição** |
| --- | --- |
| **Bloco** | Filtra as unidades por bloco do empreendimento. |
| **Unidade** | Busca uma unidade específica código. |
| **Status** | Exibe apenas unidades na situação selecionada. |

## Visualização em Cards

A área principal exibe as unidades em formato de cards organizados em grade. Cada card apresenta as informações essenciais da unidade de forma compacta.

| **Campo no card** | **Descrição** |
| --- | --- |
| **Descrição** | Nome/descrição da subunidade cadastrada. |
| **Bloco** | Identificação do bloco ao qual a unidade pertence. |
| **Status** | Badge colorido indicando a situação atual da unidade. |
| **Área** | Metragem da unidade em m². |
| **Preço** | Valor inicial da unidade em R$. |
| **Simular** | Atalho para simulação de proposta — disponível apenas para unidades com status **Disponível**. |

## Mapa Interativo

Acima dos cards é exibido o mapa visual do empreendimento (quando parametrizado). Os marcadores coloridos representam cada unidade, seguindo a mesma legenda de cores dos cards.

### Interações no mapa

* **Zoom:** Scroll do mouse para aproximar ou afastar.
* **Seleção:** Clique em um marcador para ver os detalhes da unidade.
* **Popup:** Exibição de janela flutuante com área, preço e botão direto para Simular.

### Cores dos marcadores

* **Verde:** Unidade Disponível.
* **Amarelo:** Unidade Em Proposta.
* **Vermelho:** Unidade Vendida.
