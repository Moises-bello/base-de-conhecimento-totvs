---
article_id: 4403790076567
category: PMS - Projetos
content_hash: 38a3ae07f0930a2705fcc0030e489ce8f1d0e8481ef19e655575fb0850fdad9d
fetched_at: '2026-06-28T22:37:14.831055+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - PMS - Como Gerar Cronograma
  Por Período '
type: support-article
updated_at: '2021-07-06T17:54:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403790076567-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-PMS-Como-Gerar-Cronograma-Por-Per%C3%ADodo
---

**Dúvida**Como gerar cronograma por período no PMS?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - PMS - Todas as versões  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
1. Cadastre um Calendário;

![calendario.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4403789877143/calendario.gif)  
2. Cadastre um Recurso;

![recurso.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4403789880215/recurso.gif)  
3. Crie um Projeto;  
Nele deve preencher os campos do cabeçalho:

* Calendário AF8\_CALEND;
* Tipo Períodos AF8\_TPPERI;
* Inicio Períodos AF8\_INIPER;
* Fim Períodos AF8\_FIMPER.

Na tarefa deve preencher os campos:

* Calendário AF9\_CALEND;
* Método Medição AF9\_TPMEDI - **Preencher como Cronograma por Período**;
* Esforço Horas AF9\_HESF.

Preencher a aba de recurso e ao salvar o sistema ira calcular o Cronograma por Período.

![projeto.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4403796729495/projeto.gif)
