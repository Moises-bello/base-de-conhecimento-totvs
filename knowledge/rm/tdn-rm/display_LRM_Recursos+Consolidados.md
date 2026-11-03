---
content_hash: fb8cfd6e8432047d5669050b91be59c57597d87f5bcb51ee1934ba507df36dda
fetched_at: '2026-06-29T00:09:54.407242+00:00'
page_id: '444617374'
product: rm
source: tdn-rm
title: Recursos Consolidados
type: documentation
url: https://tdn.totvs.com/display/LRM/Recursos+Consolidados
version: 5
---

As composições cadastradas no TOTVS Obras e Projetos podem ser associadas dentro de uma Composição como composições auxiliares. O anexo de Recursos Consolidados tem por finalidade exibir todos os Recursos associados à Composição até o último nível de Composição auxiliar associada a ele, ou seja, no anexo de Recursos Consolidados serão exibidos todos os Insumos associados a Composição. Caso a Composição não possua composições auxiliares os Recursos Consolidados terão quantidades iguais as dos Recursos associados a Composição.

*Exemplo:*

*O Insumo **F00001 - Servente** está **associado em 3 composições** do projeto:*

* ***000001 - Escavação de tubulões** com **quantidade** **4,7900**,*
* ***000002 - Escavação para blocos** com **quantidade 3,6571**,*
* ***000013 - Concreto estrutural de tubulões** com **quantidade 2,500**.*

*A Composição **000001 - Escavação de tubulões** possui entre seus **Recursos associados** a Composição **000002 - Escavação para blocos** com **quantidade 4,22**.**A Composição**000002 - Escavação para blocos** possui entre seus **Recursos associados** a Composição **000013 - Concreto estrutural de tubulões** com **quantidade 1,00**.*

*Ao abrir o anexo de Recursos Consolidados da Composição é possível visualizar os impactos dos Insumos na Composição considerando todas as composições auxiliares. Considerando o exemplo citado, no anexo Recursos Consolidados da Composição **000001 - Escavação de tubulões**o Insumo **F00001 - Servente** será exibido apenas uma vez e sua quantidade será a quantidade total do Insumo em todas as composições. A **quantidade do Insumo** exibida será definida pelo cálculo **Quantidade da Composição Associada**(quando estiver associada a outra) **x Quantidade do Insumo.***

* ***000013 - Concreto estrutural de*** ***tubulões** - Quantidade 1,0000 da Composição associada a Composição 000002. Quantidade do Insumo na Composição = 2,500 = 2,5000*  
  + ***000002 - Escavação para blocos**- Quantidade 4,2200 da Composição associada a Composição 000001. Quantidade do Insumo na Composição = 4,2200 x (3,6571+2,5000) = 25,9830*
    - ***000001 - Escavação de tubulões**- Insumo tem quantidade 4,7900.*
* ***Quantidade Total Consolidada do Insumo F00001 na Composição 000001 - Escavação de tubulões = 4,7900 + 25,9830 = 30,7730***

Colunas Exibidas no Anexo de Recursos Consolidados:

* **Código do Insumo**: Código do Insumo associado a Composição
* **Descrição:** Descrição do Insumo na Composição
* **Quantidade:** Quantidade totalizada do Insumo em todos os níveis da Composição
* **Preço Unitário:** Valor unitário do Insumo
* **Impacto:** Impacto do Insumo em todos os níveis da Composição
* **Unidade:**Unidade de medida do Insumo
* **Grupo DNIT:**Grupo DNIT informado no Insumo
* **Valor sem Leis:**Valor da Composição sem Leis aplicadas

.
