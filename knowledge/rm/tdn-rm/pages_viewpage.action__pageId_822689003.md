---
content_hash: 82e14eb857bfd0d7690860fa329aa2a27be55c290f31587366fc25e502755ea3
fetched_at: '2026-06-29T00:11:46.566263+00:00'
page_id: '822689003'
product: rm
source: tdn-rm
title: trib/totTrib
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=822689003
version: 19
---

Grupo de informações para totais aproximados dos tributos relacionados ao serviço prestado, em conformidade com a Lei nº 12.741/2012 (Lei da Transparência).

Este é um grupo de escolha. O sistema preencherá **apenas uma** das opções abaixo por nota, dependendo da parametrização e do regime tributário da filial.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Nome | Pai | Obrigatório | Origem | Descrição |
| pTotTribSN | NFSe/infNFSe/DPS/infDPS/valores/trib/totTrib/ | Não | TPRDCODFISCAL.ALIQIBPTSIMPLES | Gerado exclusivamente para optantes do Simples Nacional que possuem alíquota informada. |
| vTotTrib | NFSe/infNFSe/DPS/infDPS/valores/trib/totTrib/ | Não | Tabela TITMMOVFISCAL | Gerado quando o parâmetro "Calcula Lei da Transparência" está ativo. |
| pTotTrib | NFSe/infNFSe/DPS/infDPS/valores/trib/totTrib/ | Não | Tabela TPRDCODFISCAL | Gerado para empresas do Regime Normal quando não há cálculo por valor, utilizando alíquotas do cadastro. |
| indTotTrib | NFSe/infNFSe/DPS/infDPS/valores/trib/totTrib/ | Não | Fixo "0". | Gerado com valor fixo **0** (zero) quando nenhuma das condições anteriores for atendida. |

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
| **Regime Normal** | Parâmetro Ativo + Valores > 0 | `vTotTrib` | Valor total monetário |
| **Regime Normal** | Possui Alíquotas IBPT | `pTotTrib` | Alíquotas percentuais |
| **Regime Normal** | Parâmetro Ativo + Sem Dados | `vTotTrib` | Valor total zerado |
| **Regime Normal** | Parâmetro Desativado | `indTotTrib = 0` | Não informa tributos |

---

### Observações Técnicas

* **Exclusividade:** Os campos/grupos acima são mutuamente exclusivos. O XML não será validado se mais de um deles for enviado simultaneamente.
* **Links Detalhados:** Para ver a composição dos grupos de valores e alíquotas (campos federais, estaduais e municipais), acesse as sub-páginas:
