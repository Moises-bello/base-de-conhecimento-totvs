---
article_id: 39956495017751
category: Manufatura
content_hash: 146530bd05c77110bc76e3ed56e089263c665ac2c811025e34946b6e31114709
fetched_at: '2026-06-28T22:42:23.500637+00:00'
product: protheus
section_id: 360005696214
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Desabilitar a geração automática de
  solicitações de compras ao abrir uma ordem de produção
type: support-article
updated_at: '2026-04-23T13:45:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39956495017751-Manufatura-Linha-Protheus-SIGAPCP-Desabilitar-a-gera%C3%A7%C3%A3o-autom%C3%A1tica-de-solicita%C3%A7%C3%B5es-de-compras-ao-abrir-uma-ordem-de-produ%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39956453501591) Tempo aproximado para leitura: **00:00:59 min**  
  
**Dúvida**  
Como desabilitar a geração automática de solicitações de compras originadas ao abrir uma ordem de produção?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
Para desabilitar a geração automática de solicitações de compras originadas pela inclusão de ordens de produção na rotina **MATA650 - Ordem de Produção**, orientamos localizar o parâmetro **MV\_GERASC - Gera Solicitação de Compras a partir da inclusão da ordem de produção** e alterar o conteúdo para a letra **F**.  
  
Após realizar este ajuste e salvar as alterações, o Sistema deixará de gerar as solicitações de compras de forma automática ao realizar a inclusão de novas ordens de produção.
