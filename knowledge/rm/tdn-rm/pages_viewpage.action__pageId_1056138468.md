---
content_hash: fab1e35bbe059a03182bbd9d6a7f15b384fccdcacabcc78f62518111f39690df
fetched_at: '2026-06-29T00:05:51.850920+00:00'
page_id: '1056138468'
product: rm
source: tdn-rm
title: Layout único totTrib/pTotTrib
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1056138468
version: 2
---

Grupo de informações destinado a informar as alíquotas percentuais aproximadas dos tributos (Federal, Estadual e Municipal). Utilizado prioritariamente quando o cálculo monetário por item não é realizado.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Nome** | **Pai** | **Obrigatório** | **Origem** | **Máscara** | **Descrição** |
| **pTotTrib** | **totTrib** | **Sim**  **(Condicional)** | **Grupo** | **--** | **Grupo de valores percentuais aproximados dos tributos (%).** |
| pTotTribFed | pTotTrib | Sim | TPRDCODFISCAL.ALIQIBPTFEDERAL | 1-2v2 | Valor percentual aproximado dos tributos federais (%). |
| pTotTribEst | pTotTrib | Sim | TPRDCODFISCAL.ALIQIBPTESTADUAL | 1-2v2 | Valor percentual aproximado dos tributos estaduais (%). |
| pTotTribMun | pTotTrib | Sim | TPRDCODFISCAL.ALIQIBPTMUNICIPAL | 1-2v2 | Valor percentual aproximado dos tributos municipais (%). |

Regras de Negócio (Lógica de Geração)

Este grupo será gerado para empresas do **Regime Normal** (Não Optantes pelo Simples Nacional) quando a geração por "Valores Monetários" (`vTotTrib`) não for aplicada.

**Condições Específicas:**

1. **Regime:** A Filial **não** é optante pelo Simples Nacional.
2. **Prioridade:** O sistema identificou que **não** deve gerar o grupo `vTotTrib` (seja porque o parâmetro "Calcula Lei da Transparência" está desmarcado OU porque os valores calculados no item resultaram em zero).
3. **Existência de Dados:** Existem alíquotas cadastradas no Produto para a UF da filial.

   * *Caminho no sistema:* Cadastro do Produto | Anexo Dados Fiscais por UF | Aba Lei da Transparência.

> **Resumo:** Se não calculou o valor (R$) no movimento, mas tem a alíquota (%) no cadastro do produto, envia este grupo `pTotTrib`.

### Detalhes Técnicos

* **Tipo de Dado:** Numérico (Percentual).
* **Tamanho:** Suporta até 2 inteiros e 2 decimais (Ex: `18.00` para 18%).
* **Obrigatoriedade dos Filhos:** Ao gerar o grupo `pTotTrib`, é obrigatório o envio das três alíquotas (Federal, Estadual e Municipal). Caso alguma seja zero, deve ser enviada como `0.00`.
