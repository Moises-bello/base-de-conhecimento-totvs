---
article_id: 10260431162263
category: MDT - Laudos
content_hash: 83a76507361aa7a15841db951c97065b7014f43cdbd3408b4f816d7049675815
fetched_at: '2026-06-28T22:44:26.271321+00:00'
product: protheus
section_id: 360012070273
source: central-protheus
title: RH - Linha Protheus - MDT - Como gerar atalho de Dosimetria por Atividades
  no relatório PGR
type: support-article
updated_at: '2025-03-03T18:17:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10260431162263-RH-Linha-Protheus-MDT-Como-gerar-atalho-de-Dosimetria-por-Atividades-no-relat%C3%B3rio-PGR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30372844175127) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Como gerar atalho de Dosimetria por Atividade (Tarefa) no relatório PGR, rotina MDTR851?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Incluir um Laudo, através da rotina **Atualizações - Laudos - Laudos** *(MDTA210)* onde o campo de **Tipo Laudo (TO0\_TIPREL)** seja igual a **6-PGR** e deve incluir o atalho em questão na pasta de **Conteúdo**. **![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30372808852631)  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10260315345047)**Na rotina Tarefa por Func., no menu **Atualizações > PPRA > Tarefas por Funcionário** *(MDTA090)*, incluir um registro:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10260389243543)  
  
Na rotina Medição Dosimetro, no menu **Atualizações - PPRA - Medição Dosimetro** *(MDTA997)*, incluir registro e preencher o campo **Registro (TJ7\_TIPREG)** igual a Tarefa e vincular a Tarefa cadastrado.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10260386540951)  
  
Ao gerar o relatório PGR, será apresentado o atalho no formato abaixo:  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10260487126167)  
  
**Saiba Mais**[Consulte os atalhos disponíveis no relatório PGR](https://tdn.totvs.com/pages/viewpage.action?pageId=667375614)  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-) **[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)**
