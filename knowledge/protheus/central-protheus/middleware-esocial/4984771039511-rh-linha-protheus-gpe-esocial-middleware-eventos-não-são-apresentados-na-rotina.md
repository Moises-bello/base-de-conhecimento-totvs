---
article_id: 4984771039511
category: MIDDLEWARE eSocial
content_hash: a728d41dae3105a89a4b2f7e649e10df60d5740b18b00e275cca922007ccf340
fetched_at: '2026-06-28T22:43:05.009641+00:00'
product: protheus
section_id: 360005445753
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - Middleware - Eventos não são apresentados
  na rotina de exclusão
type: support-article
updated_at: '2025-07-24T20:48:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4984771039511-RH-Linha-Protheus-GPE-eSocial-Middleware-Eventos-n%C3%A3o-s%C3%A3o-apresentados-na-rotina-de-exclus%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25827886143383) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Alguns eventos não são apresentados na rotina de exclusão **(GPEM922)**.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**A regra do sistema/rotina é:   
**Eventos**: S-2190, S-2200, S-2205, S-2206, S-2250, S-2260, S-2298, S-2300, S-2306 serão apresentados na rotina, exceto quando seu status for igual a 2 **(aguardando retorno do governo)**.   
**Eventos**: S-1200, S-1210 serão apresentados na rotina, exceto status 2 e 4 **(aguardando retorno do governo e transmitido com sucesso ao governo)**, para estes dois periódicos a exclusão quando o evento já tiver transmitido será feita pela rotina dos eventos periódicos **(GPEM034)**.   
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
