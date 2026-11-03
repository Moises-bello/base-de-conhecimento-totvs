---
article_id: 35791880461463
category: Materiais - Compras (SIGACOM)
content_hash: 1f8c6658b3e5bb86bdd31d0f399e00ce71fb8d5b571c1dda2e111d60ea127806
fetched_at: '2026-06-28T22:41:21.743952+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - Como incluir
  ou deduzir o valor dos impostos no total da Cotação no NFC?
type: support-article
updated_at: '2026-03-03T18:27:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35791880461463-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-Como-incluir-ou-deduzir-o-valor-dos-impostos-no-total-da-Cota%C3%A7%C3%A3o-no-NFC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35791880440727) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Existe a possibilidade de somar ou subtrair o valor dos Impostos no Valor Total da Cotação no Novo Fluxo de Compras? Como realizar esse procedimento de creditar os Impostos no Novo Fluxo de Compras?  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Gestão de Compras - Protheus Release 12.1.2310  
  
**Solução**  
Apenas os valores dos impostos **IPI (C8\_VALIPI)** e **ICMS Solidário (C8\_VALSOL)** serão somados no valor total da cotação.

Os impostos **ICMS, ICMS Complementar, ISS e ICMS DIFAL** não serão incluídos nem descontados do Valor Total da Cotação, ou seja, eles não farão parte da composição do valor total da Cotação. Se trata do conceito de funcionamento da rotina.

Se o imposto (ICMS, ICMS Complementar, ISS ou ICMS DIFAL) deve ser acrescido ou abatido no valor da Nota Fiscal ou Duplicata - devemos salientar que essa configuração funcionará somente na geração do Documento de Entrada e Duplicatas, não nas telas de Cotação, Análise de Cotação ou Pedido de Compra.

Importante frisar que na tela de Pedido de Compra (MATA120), caso adicione um fornecedor e item que possua uma configuração de tributo - que agregue ou abata valor - o sistema irá mostrar no campo Total o valor mais a soma ou abatimento do imposto com essa configuração, apenas para mostrar uma "prévia" do total.  Mas ao clicar em Confirmar na tela de Pedido de Compra, o sistema vai salvar no campo total o valor total do Pedido, sem considerar o abatimento ou soma desse imposto, que deve ser considerado apenas na Nota Fiscal ou Duplicata, conforme configuração.

Logo, ao gerar o Pedido de Compra no NFC, ao visualizar o Pedido de Compra na rotina MATA120, o valor total vai ser o valor total do Pedido, conforme o legado já faz hoje, pois **os cálculos de abatimento ou soma devem ser executados na geração da Nota Fiscal ou duplicata, não nessas etapas anteriores.**

***Obs1:***

No Novo Fluxo de Compra, ao Analisar a Cotação, existe a possibilidade de ordenar por **Melhor Preços Com Impostos**. Nesse caso o sistema irá considerar o valor dos impostos **IPI e ICMS Solidário** como critério de ordenação

***Obs2:***

No Novo Fluxo de Compra, o Cálculo de Imposto é baseado nas configurações fiscais cadastradas, no produto e no Fornecedor para ser realizado o cálculo. Não é validada TES inteligente.

***Obs3:***

PIS e COFINS não são atualizados no momento da cotação. Eles podem ser calculados apenas no Pedido de Compra e no Documento de Entrada.

***Saiba Mais:***

[DMANMAT02-53639 DT NFC Implementar a apresentação dos tributos CBS / IBS na tela de análise da cotação](https://tdn.totvs.com/pages/viewpage.action?pageId=981002683)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Novo Fluxo de Compras - NFC (PGCA010)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19838751317655-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Novo-Fluxo-de-Compras-NFC-PGCA010)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
