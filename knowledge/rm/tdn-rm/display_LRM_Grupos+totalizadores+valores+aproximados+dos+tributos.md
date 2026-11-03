---
content_hash: 821bf55a2f8600777446038cfae31fe943c79b259086fde227c34c508ce0e807
fetched_at: '2026-06-29T00:05:51.835085+00:00'
page_id: '1056135617'
product: rm
source: tdn-rm
title: Grupos totalizadores valores aproximados dos tributos
type: documentation
url: https://tdn.totvs.com/display/LRM/Grupos+totalizadores+valores+aproximados+dos+tributos
version: 12
---

### Voltar para [Layout único de integração da NFS-e com o TSS](https://tdn.totvs.com/pages/viewpage.action?pageId=560652116)

| Nome | Pai | Obrigatório | Origem | Descrição |
| --- | --- | --- | --- | --- |
| totTrib | **[rps](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143227)** | Não |  | Grupos totalizadores valores aproximados dos tributos |
| vTotTrib | totTrib | Não |  |  |
| pTotTrib | totTrib | Não |  |  |
|  | totTrib | Não | Fixo "0". | Gerado com valor fixo **0** (zero) quando nenhuma das condições anteriores for atendida. |
|  | totTrib | Não | TPRDCODFISCAL.ALIQIBPTSIMPLES | Gerado exclusivamente para optantes do Simples Nacional que possuem alíquota informada. |

Fluxograma de Decisão (Lógica do Sistema)

A definição de qual campo será gerado no XML segue a seguinte ordem de prioridade:

1. **Cenário: Simples Nacional**

   * **Critério:** filial Optante pelo Simples Nacional.
   * **Ação:** Se houver alíquota configurada (`ALIQIBPTSIMPLES`), gera o campo **`pTotTribSN`**. Caso contrário, informa o (**`indTotTrib = 0`**).
2. **Cenário: Regime Normal com Valores Calculados**

   * **Critério:** Parâmetro "Lei da Transparência" ativo para o movimento **E** a soma dos tributos (Federal/Estadual/Municipal) for maior que zero.
   * **Ação:** Gera o grupo **`vTotTrib`** com os valores calculados.
3. **Cenário: Regime Normal com Alíquotas Informadas**

   * **Critério:** Existência de alíquotas de tributação no cadastro/tabela IBPT para os itens da nota.
   * **Ação:** Gera o grupo **`pTotTrib`** com as alíquotas.
4. **Cenário: Regime Normal sem Valores ou Alíquotas (Lei da Transparência Ativa)**

   * **Critério:** Parâmetro "Lei da Transparência" ativo, mas não foram encontrados valores ou alíquotas.
   * **Ação:** Gera o grupo **`vTotTrib`** com valores zerados.
5. **Cenário: Indicador de Não Informação**

   * **Critério:** Nenhum dos critérios anteriores atendidos (ex: Parâmetro da Lei da Transparência desativado para o Regime Normal).
   * **Ação:** Define o indicador **`indTotTrib = 0`**, sinalizando que o total de tributos não foi informado.

Resumo da Regra

| **Enquadramento** | **Condição Adicional** | **Campo/Grupo gerado no XML** | **Descrição** |
| --- | --- | --- | --- |
| **Simples Nacional** | Possui Alíquota | `pTotTribSN` | Alíquota do Simples Nacional |
| **Simples Nacional** | Sem Alíquota | `indTotTrib = 0` | Não informa tributos |
| **Regime Normal** | Parâmetro Ativo | `vTotTrib` | Valor total monetário |
| **Regime Normal** | Possui Alíquotas IBPT | `pTotTrib` | Alíquotas percentuais |
| **Regime Normal** | Parâmetro Ativo + Sem Dados | `vTotTrib` | Valor total zerado |
| **Regime Normal** | Parâmetro Desativado | `indTotTrib = 0` | Não informa tributos |

---

### Observações Técnicas

* **Links Detalhados:** Para ver a composição dos grupos de valores e alíquotas (campos federais, estaduais e municipais), acesse as sub-páginas:
