---
article_id: 360059776113
category: MDT - Laudos
content_hash: e8a499ca953b5916c78295fc9c73dc1b53234d94b5d6ef2864f4fbbb0a734945
fetched_at: '2026-06-28T22:44:26.395586+00:00'
product: protheus
section_id: 360012070273
source: central-protheus
title: RH - Linha Protheus - MDT - Na elaboração de um Laudo para o tipo PCMSO (MDTA210)
  como incluir o atalho Turnos
type: support-article
updated_at: '2023-12-06T19:27:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059776113-RH-Linha-Protheus-MDT-Na-elabora%C3%A7%C3%A3o-de-um-Laudo-para-o-tipo-PCMSO-MDTA210-como-incluir-o-atalho-Turnos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19613902456983)** Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Quais os vínculos tabelas e campos utilizados para o **Atalho Turnos** na elaboração de um Laudo para o tipo PCMSO?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Os Atalhos são consultas prontas no sistema para geração de laudos, e são gerados de acordo com o Tipo Laudo **(TO0\_TIPREL)**.   
Abaixo segue informações sobre os atalhos que podem ser utilizados na definição de um Laudo do Tipo PCMSO, as rotinas e campos envolvidos nesse processo e os seus vínculos.  
  
**Atalho**: Turnos  
  
**Tabela:**SR6 - Turnos de Trabalho  
  
**Campos:**R6\_HRNORMA - Hrs. Normais  
R6\_HRDESC - Hrs. Descanso  
  
**Vínculos:**Em **Atualizações > Cadastros Gerais > Turnos de Trabalho**. Fazer a inclusão de um turno.   
  
Em **Atualizações > Laudos > Laudos**. - Incluir um laudo tendo o campo Tipo Laudo **(TO0\_TIPREL)** como **2=PCMSO**.  Na aba de Conteúdo Laudo, adicionar o atalho "**TURNOS**".  
  
Exemplo de cadastro: Como incluir um atalho **Turnos** em um Laudo do tipo PCMSO.  
  
![TXSlRfzw20.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360100735053)

**Saiba Mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Consulte artigos PCMSO](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010945214-MDT-PCMSO)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
