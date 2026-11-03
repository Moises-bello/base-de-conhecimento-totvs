---
article_id: 9005560212119
category: GPE - eSocial - Não Periódicos
content_hash: 20a228e49d4291937c04ed9bf0378932feaafc852b7d8beef88eda70d2626e55
fetched_at: '2026-06-28T22:45:04.813919+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2206/S-2230 - Quais os parâmetros auxiliam
  na geração dos eventos via job
type: support-article
updated_at: '2026-06-16T11:51:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9005560212119-RH-Linha-Protheus-GPE-eSocial-S-2206-S-2230-Quais-os-par%C3%A2metros-auxiliam-na-gera%C3%A7%C3%A3o-dos-eventos-via-job
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25244433400087)**Tempo aproximado para leitura: **00:05:00** min **Dúvida**Quais os parâmetros auxiliam na geração dos eventos S-2206 / S-2230 via *job*?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Abaixo os parâmetros que impactam na integração dos eventos pelo *Job* Schedule GPEM026B

* **MV\_DTCGINI** - Parâmetro eSocial que determina a data que a carga inicial foi enviada para o governo e concluída.
* **MV\_DTCGTNO** - Parâmetro eSocial que determina a data inicial que será considerada para o envio da troca de turno no *job* GPEM026B.
* **MV\_DTFIMA** - Gerar evento S-2230 com Data Fim : **.F.** - Não gerar o evento S-2230 já com a data fim do afastamento;**.T.** - Gerar o evento S-2230 já com a data fim do afastamento;
* **MV\_EFDAVIS** - Na ocorrência de inconsistência na eSocial.  
  **0** - Emite aviso;   
  **1** - Avisa e impede processo;   
  **2** - Não emite aviso.
* **MV\_RHTAF** - Habilita a integração de dados do eSocial com TAF. Se .T. passa a integrar dados de eventos não periódicos do SIGAGPE com o SIGATAF

Documentação de apoio os parâmetros o *job* *Schedule*:

* [RH - Linha Protheus - GPE - eSocial - Saneamento de Base - Como consultar, configurar ou alterar os parâmetros do Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25252443928855-RH-Linha-Protheus-GPE-eSocial-Saneamento-de-Base-Como-consultar-configurar-ou-alterar-os-par%C3%A2metros-do-Protheus)
* [RH - Linha Protheus - GPE - eSocial - S-2206/S-2230 - Como configurar o job schedule GPEM026B;](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5220215589527-RH-Linha-Protheus-GPE-eSocial-S-2206-S-2230-Como-configurar-o-job-schedule-GPEM026B?source=search)
* [RH - Linha Protheus - GPE - eSocial - S-2206/S-2230 - Como executar o Job/Schedule manualmente;](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035161473-RH-Linha-Protheus-GPE-eSocial-S-2206-S-2230-Como-executar-o-Job-Schedule-manualmente?source=search)
* [RH - Linha Protheus - GPE - eSocial - S-2206/S-2230 - Como configurar o job schedule GPEM026B na tela PO UI;](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21979795766167-RH-Linha-Protheus-GPE-eSocial-S-2206-S-2230-Como-configurar-o-job-schedule-GPEM026B-na-tela-PO-UI?source=search)
* [RH - Linha Protheus - GPE - eSocial - S-2206/S-2230 - Como executar o Job/Schedule manualmente na tela PO UI;](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21983515224727-RH-Linha-Protheus-GPE-eSocial-S-2206-S-2230-Como-executar-o-Job-Schedule-manualmente-na-tela-PO-UI?source=search)

**Saiba Mais**

Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[Agenda de Eventos Tira Dúvidas Suporte](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-1-consolidada-ate-a-no-s-1-1-01-2023-retificada-em-20230124.pdf)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
