---
article_id: 360059768633
category: MDT - Laudos
content_hash: df3b31fe12aefa71ff6490cd673b9a870273eb4c1ad54c4d687e75fefb46c0bb
fetched_at: '2026-06-28T22:44:26.359918+00:00'
product: protheus
section_id: 360012070273
source: central-protheus
title: RH - Linha Protheus - MDT - Na elaboração de um Laudo para o tipo PCMSO (MDTA210)
  como incluir o atalho Local
type: support-article
updated_at: '2025-03-03T12:29:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059768633-RH-Linha-Protheus-MDT-Na-elabora%C3%A7%C3%A3o-de-um-Laudo-para-o-tipo-PCMSO-MDTA210-como-incluir-o-atalho-Local
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19673348292375)** Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Quais os vínculos tabelas e campos utilizados para o **Atalho Local** na elaboração de um Laudo para o tipo PCMSO?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Os Atalhos são consultas prontas no sistema para geração de laudos, e são gerados de acordo com o Tipo Laudo **(TO0\_TIPREL)**.   
Abaixo segue informações sobre os atalhos que podem ser utilizados na definição de um Laudo do **Tipo PCMSO**, as rotinas e campos envolvidos nesse processo e os seus vínculos.  
 **Atalho**: Local  
  
**Tabela**:   
TNE - Ambiente Físico de Risco  
  
**Campos**:   
TNE\_NOME - Nome Ambiente  
TNE\_MEMODS - Descrição  
  
**Vínculos**:  
Em **Atualizações > Laudos > Laudos**.  Incluir um laudo tendo o campo **Tipo Laudo(TO0\_TIPREL)** como **2=PCMSO**.  Na aba de Conteúdo Laudo, adicionar o atalho "**LOCAL**".  
  
Em **Atualizações > Laudos > Laudos x Locais**. Relacionar um local ao laudo.  
  
Exemplo de cadastro: Como incluir um atalho **LOCAL** em um Laudo do tipo **PCMSO**.  
  
![fpYVLGPjFx.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360100721293)  
  
**Saiba Mais**  
[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos Laudos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012070273-MDT-Laudos)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
