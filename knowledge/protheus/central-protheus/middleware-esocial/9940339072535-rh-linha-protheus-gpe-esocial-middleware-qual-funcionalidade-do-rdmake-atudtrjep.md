---
article_id: 9940339072535
category: MIDDLEWARE eSocial
content_hash: f8682c628890b5a4b527ed685a20877f8c8449cb15cad969c9736cc0bcf05916
fetched_at: '2026-06-28T22:43:05.031085+00:00'
product: protheus
section_id: 360005445753
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - Middleware - Qual funcionalidade do rdmake
  ATUDTRJE.PRW
type: support-article
updated_at: '2025-07-24T20:00:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9940339072535-RH-Linha-Protheus-GPE-eSocial-Middleware-Qual-funcionalidade-do-rdmake-ATUDTRJE-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25159883885207) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Qual funcionalidade do *rdmake* ATUDTRJE.PRW para *Middleware*?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O *rdmake,* foi criado para realizar essa atualização de data, foi alterado o rdmake **ATUDTRJE.PRW** para gravar a **Data de Admissão no campo Data Efetiva do Evento** (RJE\_DTEVE)  dos registros gerado para o **evento S-2200**.  
Um dos campos criados para possibilitar a execução de filtro por período no monitor do *Middleware* foi o campo **Data Efetiva do Evento** (RJE\_DTEVE), atualmente temos a necessidade de atualizar este campo com a **Data de Admissão gerada no XML do evento S-2200** nos registos já existentes na base.  
  
**A rotina ATUDTRJE é um *rdmake***, portanto deve ser compilada no ambiente e incluída no menu do módulo. A rotina só será executada para os registros que possuem o arquivo XML gravado no campo RJE\_XML.  
  
**Saiba Mais**[Middleware Linha Protheus RH](http://click.mktmail.totvs.com.br/?qs=60e3b9d66fa9ba5c5a8c76d2f3c0f9ec7821bc0f7ba910b98527a00641eb9486792a6ea25dd66638df293136b0e12a34)  
[eSocial | Protheus - Entregas Legais - Informações TAF/Middleware](https://tdn.totvs.com/pages/viewpage.action?pageId=390408489#Parametrizacoes-parametrizacoesMID)  
[Boletim Técnico - ATUDTRJE.PRW](https://tdn.totvs.com/pages/viewpage.action?pageId=675569614)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
Essa documentação também pode ser **acessada 24h**, através da Carolina **diretamente do Protheus:** [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
