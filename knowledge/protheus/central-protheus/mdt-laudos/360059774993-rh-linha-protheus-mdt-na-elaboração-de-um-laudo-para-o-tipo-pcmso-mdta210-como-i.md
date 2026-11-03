---
article_id: 360059774993
category: MDT - Laudos
content_hash: 14fd80187b5783f219c7dff774ed2f4b69db7939610ce74e86a048452cbf4339
fetched_at: '2026-06-28T22:44:26.374425+00:00'
product: protheus
section_id: 360012070273
source: central-protheus
title: RH - Linha Protheus - MDT - Na elaboração de um Laudo para o tipo PCMSO (MDTA210)
  como incluir o atalho Programação Vacinas
type: support-article
updated_at: '2023-12-06T19:27:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059774993-RH-Linha-Protheus-MDT-Na-elabora%C3%A7%C3%A3o-de-um-Laudo-para-o-tipo-PCMSO-MDTA210-como-incluir-o-atalho-Programa%C3%A7%C3%A3o-Vacinas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19613688191767)**Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Quais os vínculos de tabelas e campos utilizados para o **Atalho Programação Vacinas** na elaboração de um Laudo para o tipo PCMSO?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Os Atalhos são consultas prontas no sistema para geração de laudos, e são gerados de acordo com o Tipo Laudo **(TO0\_TIPREL)**.   
Abaixo segue informações sobre os atalhos que podem ser utilizados na definição de um Laudo do Tipo PCMSO, as rotinas e campos envolvidos nesse processo e os seus vínculos.  
  
**Atalho**: Programação Vacinas  
  
**Tabelas:**TL9 - Vacinas do Funcionário  
TM0 - Ficha Medica  
  
**Campos:**TL9\_VACINA - Cod. Vacina   
TL6\_NOMVAC - Nome Vacina   
TL9\_DTPREV - Data Prev.   
TL9\_NUMFIC - Ficha Medica  
TM0\_NOMFIC - Nome  
TM0\_CC - Centro Custo  
TL9\_DOSE - Dose   
  
**Vínculos:**  
Em **Atualizações > Medicamentos > Vacinas**. Incluir uma vacina.   
  
Em **Atualizações > Medicamentos > Calendário Vacinas**. Incluir um calendário.   
  
Em **Atualizações > Medicamentos > Gerar Prog. Vacina**. Gerar uma programação.   
  
**Em Atualizações > Laudos > Laudos.** Incluir um laudo tendo o campo Tipo Laudo **(TO0\_TIPREL)** como **2=PCMSO**. - Na aba de Conteúdo Laudo, adicionar o atalho "**PROGRAMACAO VACINAS**".  
  
Exemplo de cadastro: Como incluir um atalho **Programação Vacinas** em um Laudo do tipo PCMSO.  
  
![7Rwnqf98yC.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360098484674)

**Saiba Mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Consulte artigos PCMSO](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010945214-MDT-PCMSO)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
