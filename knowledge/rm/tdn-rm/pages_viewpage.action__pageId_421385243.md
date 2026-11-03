---
content_hash: c8e8bbbdf5974795ff554337a2f4ade1b3ad4d468203df60bd60577fb6cbe813
fetched_at: '2026-06-29T00:09:14.730339+00:00'
page_id: '421385243'
product: rm
source: tdn-rm
title: Aplicação do Fator K do Insumo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385243
version: 2
---

---

Informe se o fator K não será utilizado, se será utilizado somente em insumos de mão-de-obra de composições por produção ou se será utilizado como fator multiplicador dos coeficientes dos insumos nas composições.  
    
 **Somente Insumos Mão-de-Obra de Composições por Produção:**

O campo só ficará visível para os recursos do grupo de custo de mão-de-obra, em composições por produção. Será considerado como fator multiplicador dos coeficientes, portanto, alteram o valor da composição e, conseqüentemente o valor do projeto, se a mesma estiver associada a algum item de tarefa.

Como Fator Multiplicador aos Coeficientes dos Insumos nas Composições:

O campo ficará visível para todos os recursos, em composições por produção e de preço unitário. Será considerado como fator multiplicador dos coeficientes, portanto, alteram o valor da composição e, conseqüentemente o valor do projeto, se a mesma estiver associada a algum item de tarefa.

**Observações:**

Se o BDI do grupo de custo, o diferenciado (por tarefa) e o do projeto forem utilizados ao mesmo tempo e, se houver incidência de leis sociais sobre o insumo, primeiro será aplicada à taxa de leis sociais, em seguida será aplicado o BDI do grupo de custo sobre o preço do insumo (preço do insumo com leis x taxa de BDI). Este será o valor unitário do insumo na composição. Depois será aplicado o BDI diferenciado sobre o valor unitário da composição e, finalmente, será aplicado o BDI do projeto se estiver parametrizado para ser aplicado sobre o valor unitário da tarefa. Se o BDI do projeto estiver sendo aplicado sobre o total do projeto, será somado o preço de todas as tarefas e depois será aplicado o BDI.

Os valores do BDI do projeto, do grupo de custo e diferenciado devem ser maiores que zero.

**Fator K de Composição:**

Informe se o fator K da composição será utilizado. Ao confirmar a utilização do fator k da composição, o campo ficará visível em todas as composições.

Esse fator será considerado como fator multiplicador dos coeficientes, portanto, alteram o valor da composição e, conseqüentemente o valor do projeto.

Esse fator não incide sobre insumos percentuais.

**Fator K na Curva ABC de Insumos:**

Marque essa opção se desejar utilizar Fator K na Curva ABC de Insumos. Ao ativar essa opção, o cálculo da curva ABC de Insumos passa a considerar o fator k do insumo, de acodo com a parametrização do Fator K de Insumo, nesta mesma pasta.

---
