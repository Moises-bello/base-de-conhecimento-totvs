---
content_hash: 8790dcd2b8c00490cb33c2276293ccc5db86c81d94fd7ce50b3b09e0797e1e6a
fetched_at: '2026-06-29T00:11:33.369340+00:00'
page_id: '757239997'
product: rm
source: tdn-rm
title: Relatório - Eficiência Financeira da Locação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=757239997
version: 8
---

## **Introdução**

---

O relatório de Eficiência Financeira da Locação compara os valores sugeridos para locação de imóveis com o valor real efetivado nos contratos.

É possível filtrar as informações por coligada e o sistema apresenta um totalizador consolidado com informações como contratos ativos, valor sugerido, valor locado, eficiência e conclusão (ganho, perda ou neutro).

Além disso, o relatório apresenta detalhamento dos contratos ativos por coligada, incluindo número de contrato de locação e data de efetivação, considerando a soma dos valores de locação dos imóveis e o valor M² para contratos de locação de áreas fracionadas.

O objetivo é analisar a eficiência financeira das locações e identificar possíveis ganhos ou perdas.

## **Procedimentos para utilização**

---

Este relatório pode ser acessado em Aluguel / Relatórios / SmartView. Este menu possui permissão, então o usuário deve ter a sua respectiva permissão habilitada para utilizá-lo.

Ao acessar este relatório é possível de se aplicar como filtro o *Parâmetro de Visualização* abaixo:

* **Código da Coligada:** Neste parâmetro é possível de se filtrar as Coligadas, onde o valor padrão -1, processa todas as coligadas e caso o usuário queira filtrar uma ou mais coligadas específicas, pode-se realizar esta ação alterando este valor e/ou acrescentando as demais coligadas, através do botão "+" localizado em frente à descrição do mesmo;

Após definir estes parâmetros e gerar o relatório, o sistema apresentará as seguintes informações:

* Agrupador **Consolidado**: É um totalizador com um resumo das informações de todas as coligadas filtradas no *parâmetro* acima:
  + **Contratos Ativos:**É a quantidade de contratos ativos de todas as coligadas;
  + **Valor Sugerido:** É a soma dos *Valores de Locação Sugeridos* de todos os Contratos de Locação listados no detalhamento dos *Contratos Ativos por Coligada*;
  + **Valor Locado:** É a soma dos *Valores dos Contratos* de Locação da coligada filtrada nos parâmetros;
  + **Eficiência:** É a soma das diferenças entre o Valor Sugerido e o Valor Locado;
  + **Conclusão:** É o  resultado geral da comparação da diferença dos valores acima:
    - **Ganho:** Se a diferença for igual ou maior que zero;
    - **Perda:**  Se essa diferença for menor que zero;
    - **Neutro:** Se a diferença for igual a zero.

* **Detalhamento:** São os contratos de locação ativos por coligada com as informações dos campos acima (Valor Sugerido, Valor Locado, Eficiência e Conclusão), acrescidos das informações dos campos abaixo:

* + **Nº Contrato Locação:** É o campo *Contrato de Locação* concatenado com o campo *Número Contrato de Locação*, da aba [*Identificação*](https://tdn.totvs.com/pages/viewpage.action?pageId=520659174) deste cadastro;
  + **Data Efetivação:** É a data de Início Vigência do Contrato cadastrada na aba [*Identificação*](https://tdn.totvs.com/pages/viewpage.action?pageId=520659174) do Contrato de Locação;

Se o contrato de locação tiver mais de um imóvel, o sistema considerará a soma dos *Valores de Locaçã*o desses imóveis.

Se o Contrato de Locação for Área Fracionada (m²), o sistema considerará o Valor M², multiplicado pelo percentual do M² Locado, em relação ao M² Total, definido nesta mesma  aba de Identificação, do cadastro da [*Área do Imóvel*](https://tdn.totvs.com/pages/viewpage.action?pageId=435105057).
