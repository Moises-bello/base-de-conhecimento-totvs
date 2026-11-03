---
content_hash: 505f4da77d1da8d9d21c6856e66bde79220671ceaf792b74bdda514a6f7ad4fc
fetched_at: '2026-06-29T00:05:48.176741+00:00'
page_id: '1023308311'
product: rm
source: tdn-rm
title: totTrib/pTotTribSN
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1023308311
version: 2
---

Campo destinado a informar a alíquota aproximada total dos tributos para empresas optantes pelo Simples Nacional.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Nome** | **Pai** | **Obrigatório** | **Origem** | **Máscara** | **Descrição** |
| pTotTribSN | NFSe/infNFSe/DPS/infDPS/valores/trib/totTrib/ | Sim (Condicional) | TPRDCODFISCAL.ALIQIBPTSIMPLES | 1-2v2 | Valor percentual aproximado do total dos tributos da alíquota do Simples Nacional (%). |

Regras de Negócio (Lógica de Geração)

Este campo será gerado no XML exclusivamente se **todas** as condições abaixo forem atendidas:

1. **Regime da Filial:** A Filial emissora da nota deve estar parametrizada como **"Optante Regime Simplificado"** (Simples Nacional).
2. **Cadastro do Serviço:** O campo "Percentual aproximado de tributos do Simples Nacional" deve estar preenchido com valor maior que zero no cadastro do serviço vinculado ao item.

   * *Caminho no sistema:* Cadastro do Produto | Anexo Dados Fiscais por UF | Aba Lei da Transparência.

> **Nota:** Caso a Filial seja do Simples Nacional mas o campo de alíquota não esteja preenchido, o sistema gerará automaticamente a tag `indTotTrib` com valor **0**.

### Detalhes Técnicos

* **Tipo de Dado:** Numérico (Percentual).
* **Tamanho:** Suporta até 2 casas inteiras e 2 decimais (Ex: `15.50`).
* **Exclusividade:** A presença deste campo invalida a existência dos grupos `vTotTrib` e `pTotTrib`.
