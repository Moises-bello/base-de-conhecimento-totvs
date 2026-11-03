---
article_id: 40803995015959
category: Rental by ItUp Business
content_hash: 2a8c61006a1545449cbe066fe0aefd7b8d435b8665f1a2f0594c13c2a5a9b665
fetched_at: '2026-06-28T22:36:20.492770+00:00'
product: protheus
section_id: 25916336867863
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGALOC - Ao gerar contrato apresenta
  mensagem Falta o preenchimento do campo parcelas.
type: support-article
updated_at: '2026-05-28T18:13:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40803995015959-Cross-Segmentos-Backoffice-Protheus-SIGALOC-Ao-gerar-contrato-apresenta-mensagem-Falta-o-preenchimento-do-campo-parcelas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40804003633559) Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
 Ao gerar contrato, apresenta mensagem falta o preenchimento do campo parcelas.  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGALOC - Todas as versões.  
  
**Solução**  
A mensagem é apresentada devido à ausência da quantidade de parcelas no campo **FPA\_QTDPRC**, ocasionada por fonte ou dicionário de dados desatualizado.

Para corrigir a inconsistência e restabelecer o preenchimento automático do campo, é necessário aplicar o pacote de **Expedição Contínua** atualizado e executar o **compatibilizador****(UPDDISTR)** de dicionários de dados.

[Release 12.1.2410](https://%09%20https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1172656)  
[Release 12.1.2510](https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1222735)  
  
Saiba mais:  
[Prestadores de Serviços - SIGATEC - Como atualizar o dicionário com o patch de acumulados.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/24754233847063-Prestadores-de-Servi%C3%A7os-SIGATEC-Como-atualizar-o-dicion%C3%A1rio-com-o-patch-de-acumulados)
