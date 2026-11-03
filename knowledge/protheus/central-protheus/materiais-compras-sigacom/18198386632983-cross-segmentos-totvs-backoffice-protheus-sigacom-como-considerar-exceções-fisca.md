---
article_id: 18198386632983
category: Materiais - Compras (SIGACOM)
content_hash: 41952acf01402a006488e5d8847788ecb13b4aa6a306308d057ace033b2fdce3
fetched_at: '2026-06-28T22:41:25.448679+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM-  Como considerar exceções
  fiscais e demais cálculos de impostos para formulação do valor total da cotação
  no Processo Legado de Cotação?
type: support-article
updated_at: '2025-11-03T13:42:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18198386632983-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-considerar-exce%C3%A7%C3%B5es-fiscais-e-demais-c%C3%A1lculos-de-impostos-para-formula%C3%A7%C3%A3o-do-valor-total-da-cota%C3%A7%C3%A3o-no-Processo-Legado-de-Cota%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18198403338391) Tempo aproximado para leitura: **00:05:00 min** **Dúvida** Como considerar exceções fiscais e demais cálculos de impostos para formulação do valor total da cotação no **Processo Legado de cotação**?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Compras - Todas as versões

**Solução**

Como considerar exceções fiscais e demais cálculos de impostos para formulação do valor total da cotação no **Processo Legado de cotação**?

**Passo a passo:**

A análise da cotação **considera o Tipo de Entrada (TES) informada na proposta para calcular os impostos** e definir o valor total da cotação, que é o **fator determinante na escolha do fornecedor vencedor**.

Ao definir, por exemplo, uma TES para calcular ICMS e IPI (**F4\_ICM = S e F4\_IPI=S**) e também tomar crédito desses impostos (**F4\_CREDICM = S e F4\_CREDIPI = S**), na análise de cotação somente será realizado o cálculo e descontado o valor de impostos a creditar se a TES tiver sido informada, conforme a seguir:

**Atualização da Cotação:**

![](https://tdn.totvs.com/download/attachments/565742431/image2020-9-30_14-24-57.png?version=1&modificationDate=1601487642007&api=v2)

**Análise de Cotação:**

![](https://tdn.totvs.com/download/attachments/565742431/image2020-9-30_14-14-50.png?version=1&modificationDate=1601487642137&api=v2)

**Os documentos oriundos de cotação (Pedido de Compras e/ou Contratos) somente terão seus impostos gravados se o campo** **C8\_TES** **da proposta vencedora tiver preenchido e configurado para realizar os cálculos**.

A TES pode ser informada no processo de Atualização da Cotação, ou automaticamente na Geração de Cotação caso esteja vinculada ao produto, tabela de preços ou amarração produto x fornecedor.

**Importante**

Este calculo é realizado APENAS no Processo Legado de Cotação.

No **Novo Fluxo de Compras**, apenas os valores dos impostos IPI (C8\_VALIPI) e ICMS Solidário (C8\_VALSOL) serão somados no valor total da cotação.

Os impostos ICMS, ICMS Complementar, ISS e ICMS DIFAL não serão incluídos nem descontados do Valor Total da Cotação, ou seja, eles não farão parte da composição do valor total da Cotação. Se trata do conceito de funcionamento da rotina.

Para maiores informações consulte as documentações abaixo,

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - Como incluir ou deduzir o valor dos impostos no total da Cotação no NFC?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35791880461463-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-Como-incluir-ou-deduzir-o-valor-dos-impostos-no-total-da-Cota%C3%A7%C3%A3o-no-NFC)

***Saiba Mais:***

***[PCOM10013 - Como considerar exceções fiscais e demais cálculos de impostos para formulação do valor total da cotação?](https://tdn.totvs.com/pages/releaseview.action?pageId=565742431)***

Gerar cotação: [Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Como Gerar Cotação ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417420194455-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACOM-Como-Gerar-Cota%C3%A7%C3%A3o-)

Atualizar cotação: [Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Como incluir Novo participante na Cotação?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417441454103)

**Pontos de entrada:**

Gerar cotação:

[MP - SIGACOM - Pontos de Entrada disponíveis na rotina Gera Cotação - MATA131](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001417762-MP-SIGACOM-Pontos-de-Entrada-dispon%C3%ADveis-na-rotina-Gera-Cota%C3%A7%C3%A3o-MATA131)

Atualizar cotação:

[Cross Segmento - Totvs Backoffice Protheus - SIGACOM - Pontos de Entrada na rotina de Atualiza Cotações ( MATA150 )](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028037612-Cross-Segmento-Totvs-Backoffice-Protheus-SIGACOM-Pontos-de-Entrada-na-rotina-de-Atualiza-Cota%C3%A7%C3%B5es-MATA150-)

Analise de cotação:

[MP - SIGACOM - Pontos de Entrada para Análise de Cotação (MATA161)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026227233-MP-SIGACOM-Pontos-de-Entrada-para-An%C3%A1lise-de-Cota%C3%A7%C3%A3o-MATA161-)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
