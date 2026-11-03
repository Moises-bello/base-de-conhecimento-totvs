---
article_id: 21222567813271
category: Gestão de Distribuição (SIGAOMS)
content_hash: 1e0f9f8861e4decd3117e96acee888006d9881522627ae18db130c0fb810b0f7
fetched_at: '2026-06-28T22:45:49.717916+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Como integrar uma Carga gerada no SIGAOMS
  para criar um Romaneio no SIGAGFE
type: support-article
updated_at: '2026-05-27T17:36:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21222567813271-Log%C3%ADstica-Linha-Protheus-OMS-Como-integrar-uma-Carga-gerada-no-SIGAOMS-para-criar-um-Romaneio-no-SIGAGFE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21222567792919) Tempo aproximado para leitura: **00:02:20 min****Dúvida**Como integrar uma Carga gerada no **SIGAOMS - Gestão de Distribuição** para criar um Romaneio no **SIGAGFE - Gestão de Frete Embarcador**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões.  
  
**Solução**Para que a Carga gerada no programa **OMSA200 - Montagem de Carga** do **SIGAOMS** seja integrada ao **SIGAGFE**, abaixo destacamos os procedimentos a serem realizados:

1. Ter um ambiente com a integração do **ERP Protheus** com **SIGAGFE** ativa. Mais informações sobre as demais parametrizações, consulte o *link* no Saiba Mais;
2. Acesse o **GFEX000 -** **Parâmetros GFE**, aba **Integração Protheus**, parâmetro **Carga - MV\_GFEI12,** marcar com **1-Integrar**;
3. Acesse o **GFEX000 -** **Parâmetros GFE**, pasta **Integração Protheus**, parâmetro **Nota Fiscal - MV\_GFEI11**, marcar com **1-integrar**;
4. Na rotina **MATA410-Pedido de Venda**, incluir um Pedidos de Venda. O **Frete** deverá ser igual a **CIF**, preencher o campo **C5-TPFRETE - Tipo Frete**;
5. Na rotina **OMSA200**, criar a carga inserindo o pedido de venda criado no item 4;
6. Com a carga criada na rotina **OMSA200**, informe o **Transportador**. O **Transportador** poderá ser informado na criação da carga ou após a sua criação. O **Transportador é o gatilho para criar o Romaneio no GFE**, no programa **GFEA050**;
7. Consulte o programa **GFEA050-Romaneio de Carga**, se foi gerado o romaneio com base na carga do OMS. Nesse momento o Romaneio será criado vazio. O código do Romaneio será formado pelo **código da carga + sequencia da carga que é 01**;
8. Na rotina **MATA460B-Documento de Saída Carga**, fature a carga. Após Faturar a Carga, consulte o **Romaneio de Carga** e verifique se está vinculado o **Documento de Carga.**

**Saiba mais**Mais informações sobre a integração do **Protheus ERP x GFE** e a rotina de Montagem de Carga, acesse os *links* abaixo:[DI Integração Protheus x GFE](https://tdn.totvs.com/pages/releaseview.action?pageId=412886875)[Montagem de Carga - OMSA200](https://tdn.totvs.com/pages/viewpage.action?pageId=551446517)
