---
article_id: 4405807303575
category: GPE - eSocial - Periódicos
content_hash: a066fcf00212b1e0e7025237cb775f79e014a674a766547e89e23445b618cc05
fetched_at: '2026-06-28T22:45:07.172094+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - Por que o evento S-5002 (Imposto de Renda
  Retido na Fonte por Trabalhador) está retornando vazio após alteração de leiaute
type: support-article
updated_at: '2025-07-24T20:49:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405807303575-RH-Linha-Protheus-GPE-eSocial-Por-que-o-evento-S-5002-Imposto-de-Renda-Retido-na-Fonte-por-Trabalhador-est%C3%A1-retornando-vazio-ap%C3%B3s-altera%C3%A7%C3%A3o-de-leiaute
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25852969379735) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Por que o evento **S-5002** (Imposto de Renda Retido na Fonte por Trabalhador) está retornando vazio após alteração de leiaute?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O evento **S-5002** é retornado após o envio do evento **S-1210** que transmite as informações prestadas **relativas aos pagamentos** feitos a trabalhadores, com ou sem vínculo empregatício. Esses pagamentos estão relacionados aos eventos remuneratórios **(S-1200, S-2299 e S-2399).**Dessa forma, quando existe alteração da versão do leiaute é importante que ambos eventos **(remuneratório e pagamento)**sejam enviados na mesma versão. Caso seja enviado em versões diferentes o totalizador S-5002 retornará “**zerado**” (no grupo infoIR, o campo {valor} retornará com ZERO).  
  
  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
