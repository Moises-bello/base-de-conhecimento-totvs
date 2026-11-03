---
content_hash: c4fc08d69be7e9dde57e5f05a9031001dedcbe1c8a3965199e53d71e715536d7
fetched_at: '2026-06-29T00:11:46.577259+00:00'
page_id: '822689038'
product: rm
source: tdn-rm
title: totTrib/indTotTrib
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=822689038
version: 5
---

Indicador de informação de valor total de tributos. Este campo é utilizado para informar que o emitente não possui ou optou por não informar os valores estimados dos tributos (conforme Decreto 8.264/2014) ou que os valores resultaram em zero.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Nome** | **Pai** | **Obrigatório** | **Origem** | **Máscara** | **Descrição** |
| **indTotTrib** | **NFSe/infNFSe/DPS/infDPS/valores/trib/totTrib/** | **Sim**  **(Condicional)** | **Valor Fixo: 0** | **1** | **Indicador de ausência de informação de tributos (0 = Não informado).** |

### Regras de Negócio (Lógica de Geração)

Este campo será gerado automaticamente pelo sistema quando **nenhuma** das condições para geração dos grupos de valores (`vTotTrib`) ou alíquotas (`pTotTrib` / `pTotTribSN`) for atendida. É a última opção na árvore de decisão.

**Cenários de Ocorrência:**

1. **Cenário Simples Nacional:**

   * A Filial é optante pelo Simples Nacional, **MAS** não há alíquota informada no cadastro do serviço (`TPRDCODFISCAL.ALIQIBPTSIMPLES` não preenchido ou igual a zero).
2. **Cenário Regime Normal:**

   * A Filial não é optante pelo Simples Nacional;
   * **E** o parâmetro "Calcula Lei da Transparência" está desmarcado (ou a soma dos valores calculados é zero);
   * **E** não há alíquotas (Federal, Estadual, Municipal) informadas no cadastro do produto.

> **Resumo:** Se o sistema não encontrar dados válidos para calcular o valor monetário (R$) nem encontrar percentuais (%) cadastrados, ele enviará `indTotTrib = 0` para garantir a validação do esquema XML.

### Detalhes Técnicos

* **Valor Fixo:** Sempre será gerado com o valor **0**.
* **Significado:** O valor "0" corresponde à opção "Não" (Não informa valor estimado), conforme layout da NFS-e.
* **Exclusividade:** A presença deste campo invalida a existência dos grupos `vTotTrib`, `pTotTrib` e `pTotTribSN`.
