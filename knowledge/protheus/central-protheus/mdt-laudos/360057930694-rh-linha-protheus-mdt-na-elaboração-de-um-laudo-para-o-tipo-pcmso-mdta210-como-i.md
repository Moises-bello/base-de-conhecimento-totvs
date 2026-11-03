---
article_id: 360057930694
category: MDT - Laudos
content_hash: 3610c2ca39ffecc3254ab8f6e69a49c7d59e3f7d7784e576a75e6dec4891c0a2
fetched_at: '2026-06-28T22:44:26.343995+00:00'
product: protheus
section_id: 360012070273
source: central-protheus
title: RH - Linha Protheus - MDT - Na elaboração de um Laudo para o tipo PCMSO (MDTA210)
  como incluir o atalho Equipamento
type: support-article
updated_at: '2025-03-03T12:29:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057930694-RH-Linha-Protheus-MDT-Na-elabora%C3%A7%C3%A3o-de-um-Laudo-para-o-tipo-PCMSO-MDTA210-como-incluir-o-atalho-Equipamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19643199759255)** Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Quais os vínculos tabelas e campos utilizados para o **Atalho Equipamento** na elaboração de um Laudo para o tipo PCMSO?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Os Atalhos são consultas prontas no sistema para geração de laudos, e são gerados de acordo com o Tipo Laudo **(TO0\_TIPREL)**. Abaixo segue informações sobre os atalhos que podem ser utilizados na definição de um Laudo do Tipo PCMSO, as rotinas e campos envolvidos nesse processo e os seus vínculos.  
  
**Atalho:** Equipamento  
  
**Tabela:**TM7 - Equipamento Avaliação  
  
**Campos:**  
TM7\_NOEQTO - Descrição  
TM7\_NOMFAB - Fabricante   
TM7\_DTCALI - Calibração   
TM7\_DTAFER - Aferição  
  
**Vínculos:**  
Em **Atualizações > Cadastros Básicos > Eqptos Avaliação**. Incluir um equipamento. Em **Atualizações > Ppra > Riscos**. Incluir um risco.   
  
Em **Atualizações > Laudos > Laudos**. Incluir um laudo tendo o campo Tipo Laudo **(TO0\_TIPREL)** como **1=SESMT**. Na aba de Conteúdo Laudo, adicionar o atalho "**EQUIPAMENTO**".   
  
Em **Atualizações > Laudos > Laudos x Equipamento** relacionar o equipamento ao laudo. Em **Atualizações > Laudo > Laudos x Riscos**. Relacionar o risco utilizado ao laudo.   
  
Exemplo de cadastro: Como incluir um atalho **Equipamentos** em um Laudo do tipo PCMSO.  
  
![axRtcrljGp.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360100729813)  
 **Saiba Mais**  
[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos Laudos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012070273-MDT-Laudos)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
