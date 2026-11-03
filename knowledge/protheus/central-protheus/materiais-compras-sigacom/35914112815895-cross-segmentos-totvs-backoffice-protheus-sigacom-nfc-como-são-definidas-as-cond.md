---
article_id: 35914112815895
category: Materiais - Compras (SIGACOM)
content_hash: 414474e9479e7a052e602114e6f1c9932026ff70ecfea83c2990909ca55c7a15
fetched_at: '2026-06-28T22:41:21.761319+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - Como são definidas
  as Condições de Pagamento exibidas no formulário HTML do Workflow enviado ao fornecedor?
type: support-article
updated_at: '2026-03-04T17:07:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35914112815895-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-Como-s%C3%A3o-definidas-as-Condi%C3%A7%C3%B5es-de-Pagamento-exibidas-no-formul%C3%A1rio-HTML-do-Workflow-enviado-ao-fornecedor
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35914152689175) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como são definidas as Condições de Pagamento exibidas no formulário HTML do Workflow enviado ao fornecedor? Como o sistema identifica qual condição de pagamento deve ser levada no formulário para seleção do fornecedor?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - a partir da Release 12.1.2310  
  
**Solução**  
As condições de pagamento exibidas no formulário são estabelecidas de acordo com o que foi **selecionado no envio do E-mail via Novo Fluxo de Compras.** Caso o usuário não tenha pré-estabelecido as condições que o fornecedor poderá visualizar, **todas as condições que possuem "Adic WF NFC = Sim"** (campo E4\_ATVWF da tabela SE4), determinadas a partir do cadastro de condições de pagamento no Protheus, serão enviadas aos fornecedores, como ilustrado nas imagens abaixo.

![](https://tdn.totvs.com.br/download/attachments/680260500/Condicoes%20pagamento%20WF.gif?version=1&modificationDate=1711484062877&api=v2)  
  
  
  
![](https://tdn.totvs.com.br/download/attachments/680260500/CADASTRO%20CP.png?version=1&modificationDate=1711484086070&api=v2)

**Obs1.** A seleção das condições de pagamento mencionadas acima estará disponível a partir da expedição contínua de 05/04/2024.

**Obs2.** O preenchimento da Condição de pagamento é obrigatório para a salvar a atualização da cotação, tanto via formulário quanto manualmente.

**Obs3.** Caso não deseje utilizar alguma condição de pagamento no envio do formulário do Novo Fluxo de Compras, basta preencher o campo E4\_ATVWF com Não no cadastro da condição de pagamento.

**Obs4.** O campo E4\_ATVWF efetua o controle da condição de pagamento ser ou não enviada via workflow para o fornecedor. Dentro da rotina do Novo Fluxo de Compra, a condição de pagamento continua apresentada na lista no momento de começar a cotação. Apenas no momento de enviar a cotação para o fornecedor via Workflow que essa condição é barrada pela configuração do campo E4\_ATVWF.

***Saiba Mais:***

[Novo Fluxo de Compras: Guia de Referência](https://tdn.totvs.com.br/pages/releaseview.action?pageId=680260500)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
