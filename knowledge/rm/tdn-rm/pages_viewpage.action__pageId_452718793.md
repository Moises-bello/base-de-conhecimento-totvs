---
content_hash: 5966a7b3b4ab706c706d77f2d3f1157e110043c03c0ba893178f15be92c96bea
fetched_at: '2026-06-29T00:10:01.915985+00:00'
page_id: '452718793'
product: rm
source: tdn-rm
title: Pensão Alimentícia
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718793
version: 8
---

**Parâmetros**

**Base de IRRF utilizada no cálculo da Pensão Alimentícia não exclui eventos desconsiderados**

**Considera percentual total nas pensões com mais de um dependente, que utilizam ordenado líquido**

Com o parâmetro marcado serão considerados os dependentes que utilizam o ordenado líquido na base do cálculo da pensão, unificando o cálculo para que o valor total componha a base para desconto do IRRF. Após o cálculo unificado será feita a proporcionalização do valor da pensão por dependente.

**Observação:** O parâmetro é considerado apenas quando existem dois ou mais dependentes utilizando o cálculo por ordenado líquido.

Veja Exemplo no link: [EXEMPLO DE CÁLCULO](https://tdn.totvs.com.br/pages/viewpage.action?pageId=628961697)

**Valor da Diferença Salarial de outros períodos entra no cálculo do IRRF deduzido na Base da Pensão**

O evento de CC 37, Diferença Salarial, não deve incidir em pensão, porque o valor atualizado do evento original já foi considerado na Base de Pensão do recálculo no processo de diferença, e portanto já considerado no evento de Diferença de Pensão.

Mas o CC 37 incide em IRRF, para entrar na base de cálculo do CC 4 - IRRF. Dentro da fórmula da pensão é calculado o valor do IRRF para ser abatido na base. Este cálculo considera todos os eventos que estão com a incidência em IRRF marcada.

A marcação deste parâmetro indica se o CC 37 deve entrar ou não para a base de cálculo do IRRF deduzido da base de pensão. Entretanto o parâmetro só tem efeito quando o CC 37 está no mesmo período do evento de pensão, CC 13.

O valor será demonstrado na seção abaixo do log de cálculo do evento de CC 13:

-> Considera proventos do período atual, com incidência somente em IRRF: Incide apenas IRRF (IncideApenasIRRF) : 0,00

|  |  |
| --- | --- |
|  | Informações Complementares |

---

<<Voltar para tela anterior **Folha Normal**
