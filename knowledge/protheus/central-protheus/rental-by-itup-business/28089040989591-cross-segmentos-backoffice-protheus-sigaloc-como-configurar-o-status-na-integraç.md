---
article_id: 28089040989591
category: Rental by ItUp Business
content_hash: 0dd64a16bec146d94a4eb8af487544b9f1dbbd40a833112b56f1a925bbd54663
fetched_at: '2026-06-28T22:36:20.523396+00:00'
product: protheus
section_id: 25916336867863
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGALOC - Como configurar o Status
  na integração SIGALOC x SIGAMNT
type: support-article
updated_at: '2026-04-08T14:38:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28089040989591-Cross-Segmentos-Backoffice-Protheus-SIGALOC-Como-configurar-o-Status-na-integra%C3%A7%C3%A3o-SIGALOC-x-SIGAMNT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28089047421335) Tempo aproximado para leitura: **00:05:00 min**  
  
**Ocorrência**  
Como configurar o Status na integração SIGALOC x SIGAMNT.  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGALOC - A partir da release P12.1.2310.  
  
**Causa**  
Quando realizamos a pesquisa do **BEM** dentro do projeto no campo **Equipamento** (**FPA\_GRUA**), o sistema não exibe os BENS relacionados ao produto para serem incluídos no projeto.  
  
**Solução**  
Para resolver essa ocorrência, siga os passos abaixo:

**1.** Acesse a rotina **Cadastro de Status** (**LOCA081**);  
**2.** Inclua o registro para relacionar a tabela **"FQD"** com a tabela **"TQY"**.  
  
A rotina de gerenciamento de status é responsável por criar e administrar os registros de status, os quais serão utilizados na gestão do ciclo de locação no sistema **Rental by ITUP (SIGALOC)**.  
  
**Saiba mais:** [***Cadastro de Status***](https://tdn.totvs.com/display/public/PROT/Cadastro+de+Status)
