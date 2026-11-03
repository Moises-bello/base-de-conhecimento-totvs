---
article_id: 7407888045207
category: Evento S-2210
content_hash: 0c369dbd4fa3aff117683627a86909461ea592dbdc9fe8e35c9f8e55107c3652
fetched_at: '2026-06-28T22:45:24.520877+00:00'
product: protheus
section_id: 8260521640983
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2210 - Quais os parâmetros que auxiliam
  na definição do evento S-2210
type: support-article
updated_at: '2023-12-21T17:17:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7407888045207-RH-Linha-Protheus-MDT-eSocial-S-2210-Quais-os-par%C3%A2metros-que-auxiliam-na-defini%C3%A7%C3%A3o-do-evento-S-2210
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20033524905495) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Quais os parâmetros que auxiliam na definição do evento S-2210?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**Cada empresa pode ter um cenário específico portanto é importante avaliar nossa documentação centralizadora sobre a geração do eventos S-2220, os parâmetros que podem interferir ou configurar para atender as diferentes necessidades de cada empresa.  
Consulte a documentação no link <https://tdn.totvs.com/display/PROT/S-1.0-+eSocial+%7C+Protheus+-+Entregas+Legais+-+S-2210>  
  
**Parâmetros:**  
  
**\*** **MV\_NG2ESOC=** Indica se o sistema de Medicina e Segurança do Trabalho irá gerar registros no SIGATAF ou Middleware. 1 = Sim, 2 = Não.

**\* MV\_MID=** Habilita a integração de dados do eSocial com o Middleware. Se .T. Integra e se .F. não integra.

**\* MV\_NG2DTES=** Define a data incial de obrigatoriedade de envio dos eventos de SST ao eSocial.

**\* MV\_NG2AVIS=** Na ocorrência de inconsistência no envio ao eSocial. 0= Emite Aviso; 1= Avisa e impede processo; 2= Não emite aviso.

**\* MV\_NG2NENV=** Indica quais categorias de funcionários não terão os eventos de SST comunicados ao SIGATAF/Middleware.

**\* MV\_NG2IATE=** Indica qual documento será considerado para envio das informações de atendimento médico no evento S-2210. 1-Diagnóstico; 2-Atestado; 3-Mais recente.

**Saiba Mais**

[Artigos Atendimento Médico](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010945694-MDT-Atendimento-M%C3%A9dico?page=1#articles)  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206971487-RH-Medicina-e-Seguran%C3%A7a-do-Trabalho%20)  
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206971487-RH-Medicina-e-Seguran%C3%A7a-do-Trabalho)
