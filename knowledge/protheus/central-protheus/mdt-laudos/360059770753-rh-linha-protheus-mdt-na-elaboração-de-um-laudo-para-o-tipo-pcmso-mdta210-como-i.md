---
article_id: 360059770753
category: MDT - Laudos
content_hash: b0ffa3249c9a4c8855d729301030eacd9071244db9a92964d657d58c9d79e2f3
fetched_at: '2026-06-28T22:44:26.387757+00:00'
product: protheus
section_id: 360012070273
source: central-protheus
title: RH - Linha Protheus - MDT - Na elaboração de um Laudo para o tipo PCMSO (MDTA210)
  como incluir o atalho Risco
type: support-article
updated_at: '2023-12-11T11:14:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059770753-RH-Linha-Protheus-MDT-Na-elabora%C3%A7%C3%A3o-de-um-Laudo-para-o-tipo-PCMSO-MDTA210-como-incluir-o-atalho-Risco
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19674030496407)** Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Quais os vínculos tabelas e campos utilizados para o **Atalho Risco** na elaboração de um Laudo para o tipo PCMSO?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Os Atalhos são consultas prontas no sistema para geração de laudos, e são gerados de acordo com o Tipo Laudo **(TO0\_TIPREL)**. Abaixo segue informações sobre os atalhos que podem ser utilizados na definição de um Laudo do **Tipo PCMSO**, as rotinas e campos envolvidos nesse processo e os seus vínculos.  
**Atalho**: Risco  
  
**Tabelas:**TMA - Agente   
TN7 - Fonte Geradora de Risco  
TN0 - Risco  
SRJ - Funções  
TN5 - Tarefas   
TNE - Ambiente Físico de Risco  
TO1 - Laudos x Riscos   
  
**Campos:**TMA\_NOMAGE - Nome Agente  
TN7\_NOMFON - Nome Fonte   
TN0\_CC - Centro Custo  
RJ\_DESC - Descrição  
TN5\_NOMTAR - Nome Tarefa  
TNE\_NOME - Nome Ambiente  
TN0\_DTAVAL - Data Aval.   
TN0\_QTAGEN - Agente   
TO1\_RECOME - Recomendação  
  
**Vínculos:**  
Em **Atualizações > Ppra > Riscos**. Incluir um risco utilizando as informações anteriormente cadastradas e preencher o campo Mapa Risco **(TN0\_MAPRIS)** como **"2=SESMT"**.   
  
Em **Atualizações > Laudos > Laudos.** Incluir um laudo tendo o campo Tipo Laudo **(TO0\_TIPREL)** como **2=PCMSO**. Na aba de Conteúdo Laudo, adicionar o atalho "**Risco**".   
  
Em **Atualizações > Laudos > Laudos x Riscos**. Relacionar um risco ao laudo.  
  
Exemplo de cadastro: Como incluir um **atalho**  **Risco** em um Laudo do tipo **PCMSO**.  
  
![aOO4DblqV2.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360100720273)  
 **Saiba Mais**  
[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos Laudos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012070273-MDT-Laudos)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
