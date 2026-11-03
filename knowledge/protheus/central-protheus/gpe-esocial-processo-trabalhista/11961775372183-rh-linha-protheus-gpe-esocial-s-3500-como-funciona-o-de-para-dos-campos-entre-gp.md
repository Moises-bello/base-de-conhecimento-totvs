---
article_id: 11961775372183
category: GPE - eSocial - Processo Trabalhista
content_hash: 7a8480ddd5b61b362a41fa97a1f63b3a2b5e08f4526093218afee67dc2783a61
fetched_at: '2026-06-28T22:45:00.327031+00:00'
product: protheus
section_id: 10604669539479
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-3500 - Como funciona o De / Para dos
  campos entre GPE x TAF
type: support-article
updated_at: '2025-03-27T18:05:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11961775372183-RH-Linha-Protheus-GPE-eSocial-S-3500-Como-funciona-o-De-Para-dos-campos-entre-GPE-x-TAF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24445709383319) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Para o evento S-3500 como funciona o De / Para de campos Protheus com leiaute eSocial, entre GPExTAF?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Consulte abaixo detalhadamente a estrutura de campos entre GPE e TAF para o evento S-3500:

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **eSocial** | **Protheus Recursos Humanos** | | | | **Protheus TAF** | | | |
| **tag xml** | **Rotina** | **Tabela** | **Campo** | **Nome** | **Rotina** | **Tabela** | **Campo** | **Nome** |
| tpEvento | APTA100/GPEM038 |  |  | Nome do Evento | TAFA610 | V7J | V7J\_TPEVEN | Tipo do Evento |
| nrRecEvt | APTA100/GPEM038 |  |  | Numero do Recibo | TAFA610 | V7J | V7J\_NRRECI | Nr. Recibo |
| nrProcTrab | APTA100/GPEM038 |  |  | Numero do Processo | TAFA610 | V7J | V7J\_PROCTR | Numero Proc. Trabalhista |
| cpftrab | APTA100 | RD0 | RD0\_CIC | CPF do Reclamante | TAFA610 | V7J | V7J\_CPF | CPF |
| perApurPgto | GPEM038 |  |  | Período de Apuração | TAFA610 | V7J | V7J\_PERAPU | Período da Apuração |
|  |  |  |  |  |  |  |  |  |

**Saiba Mais**  
Para saber mais consulte os *links* abaixo:   
[RH - Linha Protheus - GPE - eSocial - Como se adequar ao eSocial leiaute S-1.0 NT 06/2022 e leiaute S-1.1](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8658568031127)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
  
Essa documentação também pode ser acessada 24h, através da Carolina:[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
