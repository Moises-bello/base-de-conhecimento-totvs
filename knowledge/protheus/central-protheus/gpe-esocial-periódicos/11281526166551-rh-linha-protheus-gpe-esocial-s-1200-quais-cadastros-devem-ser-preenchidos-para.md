---
article_id: 11281526166551
category: GPE - eSocial - Periódicos
content_hash: 972706e7d4b305fc53ecf4f743e3f03257a9d4e3cf3eff6902f227864dfdd206
fetched_at: '2026-06-28T22:45:08.740611+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200 - Quais cadastros devem ser preenchidos
  para geração do evento S-1200 contemplando o processamento de RRA
type: support-article
updated_at: '2025-07-24T17:23:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11281526166551-RH-Linha-Protheus-GPE-eSocial-S-1200-Quais-cadastros-devem-ser-preenchidos-para-gera%C3%A7%C3%A3o-do-evento-S-1200-contemplando-o-processamento-de-RRA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22847016561943) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Quais cadastros devem ser preenchidos para geração do evento S-1200 contemplando o processamento de RRA?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Geração do evento S-1200 Eventos Periódicos para atender ao Leiaute S.1-1, contemplando o processamento de RRA. O que analisar para gerar o xml S-1200 com RRA?  
  
No processamento do RRA (Rendimentos Recebidos Acumuladamente), será gerado o **grupo <infoRRA>** com o grupo **infoPerApur** com o valor de **IRRF de RRA** e no grupo **infoPerAnt** com os demais valores.

Ajuste na rotina de geração de eventos periódicos para contemplar o processamento do RRA. As verbas referente ao RRA serão geradas em um novo grupo dmDev especifico para RRA. Para a geração do grupo infoRRA, será necessário o preenchimento dos seguintes cadastros:

* Complemento trabalhista - RF1

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11280572538775)

* Cadastro de Processos - RE0

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11280656010263)

* Cadastro de Advogados - RE4

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11280752226455)

* Cadastro de Escritório de Advocacia - RE3

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11281178612631)

Veja também: [Manutenção dos Rendimentos Recebidos Acumulados (RRA) (GPEA840 - SIGAGPE - V12)](https://tdn.totvs.com.br/pages/viewpage.action?pageId=450142286)  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
