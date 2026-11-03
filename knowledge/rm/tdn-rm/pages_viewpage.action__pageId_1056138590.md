---
content_hash: 3d5d8ee5e07aa53a503429a6545873b24f45c0e4cda7d54dac5817fe654076ca
fetched_at: '2026-06-29T00:05:51.862776+00:00'
page_id: '1056138590'
product: rm
source: tdn-rm
title: Grupo de informações destinado a informar o percentual total aproximado dos
  tributos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1056138590
version: 8
---

### Voltar para [Layout único de integração da NFS-e com o TSS](https://tdn.totvs.com/pages/viewpage.action?pageId=560652116)

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Nome** | **Pai** | **Obrigatório** | **Origem** | **Máscara** | **Descrição** |
| **pTotTrib** | **[totTrib](https://tdn.totvs.com/pages/viewpage.action?pageId=1056135617)** | **Sim**  **(Condicional)** | **Grupo** | **--** | **Grupo de valores percentuais aproximados dos tributos (%).** |
| pTotTribFed | pTotTrib | Sim | TPRDCODFISCAL.ALIQIBPTFEDERAL | 1-2v2 | Valor percentual aproximado dos tributos federais (%). |
| pTotTribEst | pTotTrib | Sim | TPRDCODFISCAL.ALIQIBPTESTADUAL | 1-2v2 | Valor percentual aproximado dos tributos estaduais (%). |
| pTotTribMun | pTotTrib | Sim | TPRDCODFISCAL.ALIQIBPTMUNICIPAL | 1-2v2 | Valor percentual aproximado dos tributos municipais (%). |

Regras de Negócio (Lógica de Geração)

Este grupo será gerado para empresas do **Regime Normal** (Não Optantes pelo Simples Nacional) quando a geração por "Valores Monetários" (`vTotTrib`) não for aplicada.

**Condições Específicas:**

1. **Regime:** A Filial **não** é optante pelo Simples Nacional.
2. **Prioridade:** O sistema identificou que deve gerar o grupo p`TotTrib` quando o parâmetro "Calcula Lei da Transparência" está marcado OU porque existe alguma aliquota diferente de zero na aba lei da transparência.
3. **Existência de Dados:** Existem alíquotas cadastradas no Produto para a UF da filial.

   * *Caminho no sistema:* Cadastro do Produto | Anexo Dados Fiscais por UF | Aba Lei da Transparência.

> **Resumo:** Se o parametro:  Calcula Lei da Transparência no tipo de movimento esta marcado ou tem a alíquota (%) no cadastro do produto, envia este grupo `pTotTrib`.

### Detalhes Técnicos

* **Tipo de Dado:** Numérico (Percentual).
* **Tamanho:** Suporta até 2 inteiros e 2 decimais (Ex: `18.00` para 18%).
* **Obrigatoriedade dos Filhos:** Ao gerar o grupo `pTotTrib`, é obrigatório o envio das três alíquotas (Federal, Estadual e Municipal). Caso alguma seja zero, deve ser enviada como `0.00`.
