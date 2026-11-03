---
article_id: 360018567072
category: Materiais - Compras (SIGACOM)
content_hash: 353593e00feba160de0064f97f220a3d0e711baf782c16fc032fc45acee8ed5d
fetched_at: '2026-06-28T22:41:20.198528+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Mensagem: Documento
  de Entrada atrelado a título do tipo PA ao incluir uma Nota com Pedido vinculado
  a um PA'
type: support-article
updated_at: '2026-04-22T18:19:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018567072-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Mensagem-Documento-de-Entrada-atrelado-a-t%C3%ADtulo-do-tipo-PA-ao-incluir-uma-Nota-com-Pedido-vinculado-a-um-PA
---

**Dúvida**

Na inclusão do documento de entrada é apresentado mensagem:  
"**Este documento de Entrada está atrelado há um título do tipo PA. Caso seja gerado, não irá realizar a baixa automática desse título, deseja prosseguir com a inclusão do documento."**

Como realizar inclusão do documento e a compensação automática?

**Ambiente**

Microsiga Protheus – Compras – A partir da versão 12

**Solução**

Para que o sistema realize a compensação automática é necessário que os parâmetros **(F12) da rotina Contas a Pagar (FINA050)**, a qual é executada no pedido de compras para a inclusão do título PA e posterior vínculo do pedido de compras estejam configurados conforme abaixo, para que, na inclusão do título PA seja gerado o movimento bancário de pagamento desse PA, para que aí sim, na inclusão do documento de entrada com esse PC vinculado, possa haver a compensação automática do PA e do título NF ( gerado pelo documento de entrada):

**Gerar Chq. p/Adiant.?= NÃO**  
**Mov. Banc. sem Cheque?= SIM**

**Obs:**

Esta configuração na inclusão do Título, se trata de uma Premissa para o uso da funcionalidade de Adiantamento no Pedido de compras e Compensação Automática dos títulos ao incluir do Doc de Entrada.

***Saiba Mais :***

* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Adiantamento no Pedido de Compras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015664151-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Adiantamento-no-Pedido-de-Compras)
* [MP - SIGACOM - Pedido de Compra com PA em outra Moeda e Compensação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016361432-MP-SIGACOM-Pedido-de-Compra-com-PA-em-outra-Moeda-e-Compensa%C3%A7%C3%A3o)
* [MP - SIGACOM - É possível compensar NF de PA vinculado ao PC com processo Entrega por Terceiro ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058160793)
* [MP - SIGACOM - Como Incluir ou Excluir o relacionamento do Pagamento Antecipado no Pedido de Compras ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015664151)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
