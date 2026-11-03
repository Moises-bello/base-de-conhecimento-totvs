---
article_id: 360004975652
category: GPE - eSocial - Periódicos
content_hash: 99824fd4fbdee5cffd37ff57373c8089f16e376dc7288d3707922e8442fda7f6
fetched_at: '2026-06-28T22:45:09.079295+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2200 - Inconsistência do RET - 130
  - É necessário existir informação cadastral do empregador para o período
type: support-article
updated_at: '2025-07-21T14:45:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004975652-RH-Linha-Protheus-GPE-eSocial-S-2200-Inconsist%C3%AAncia-do-RET-130-%C3%89-necess%C3%A1rio-existir-informa%C3%A7%C3%A3o-cadastral-do-empregador-para-o-per%C3%ADodo
---

**Ocorrência**Inconsistência do RET - 130 - É necessário existir informação cadastral do empregador para o período  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**Ocorre por algum problema na identificação cadastral da empresa no RET, ou pode estar relacionado ao preenchimento incorreto do parâmetro **MV\_DTCGINI**.  
  
**Solução  
O que deve ser verificado para corrigir o erro:**

* Analise se foi enviado o evento S-1000 para o RET;
* Verifique se os parâmetros abaixo encontram-se conforme o grupo pertencente a empresa:

[MP - GPE - eSocial - Parâmetros 1ª Fase esocial (Tabelas Iniciais)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005048411)[MP - GPE - eSocial - Parâmetros 2ª Fase esocial (Não Periódicos)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004980892)[MP - GPE - eSocial - Parâmetros 3ª Fase esocial (Periódicos)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004981112)Exemplo: Na carga inicial deve ser colocado a data de **01/01/2018** (faturamento > 78 milhões) ou **01/07/2018** (faturamento < 78 milhões) para os eventos iniciais de S-1005 até S-1050. Para os eventos S-2200 e S-2230 deve ser utilizada a data igual ou superior a 01/03/2018.  
Caso ocorra algum ajuste no parâmetro **MV\_DTCGINI** e o erro persista, retransmita o evento S-2200 ao TAF, em caso de dúvida verifique o artigo abaixo:  
[RH - Linha Protheus - GPE - eSocial - S-2200 - Como retificar evento S-2200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033905013-RH-Linha-Protheus-GPE-eSocial-S-2200-S-2300-Como-retificar-evento-S-2200-ou-S-2300)**Saiba Mais**Para saber mais consulte os links abaixo:   
[Artigos S-2200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052505613)   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)   
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
