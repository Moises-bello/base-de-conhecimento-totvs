---
article_id: 360059773293
category: MDT - Laudos
content_hash: 0d82102f9ca8897373638130b6260c08ed7ac9a462db219dc5b67f6adf90b722
fetched_at: '2026-06-28T22:44:26.364450+00:00'
product: protheus
section_id: 360012070273
source: central-protheus
title: RH - Linha Protheus - MDT - Na elaboração de um Laudo para o tipo PCMSO (MDTA210)
  como incluir o atalho Plano
type: support-article
updated_at: '2023-12-11T11:13:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059773293-RH-Linha-Protheus-MDT-Na-elabora%C3%A7%C3%A3o-de-um-Laudo-para-o-tipo-PCMSO-MDTA210-como-incluir-o-atalho-Plano
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19673427100567)** Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Quais os vínculos tabelas e campos utilizados para o **Atalho Plano** na elaboração de um Laudo para o tipo PCMSO?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Os Atalhos são consultas prontas no sistema para geração de laudos, e são gerados de acordo com o Tipo Laudo **(TO0\_TIPREL)**.   
Abaixo segue informações sobre os atalhos que podem ser utilizados na definição de um Laudo do Tipo PCMSO, as rotinas e campos envolvidos nesse processo e os seus vínculos.  
**Atalho**: Plano  
  
**Tabelas:**AA - Plano de Ação  
TC9 - Responsáveis pelo Plano de Ação  
  
**Campos:**TAA\_NOME - Nome Plano  
TAA\_OQUE - O que?   
TAA\_ONDE - Onde?   
TAA\_PORQUE - Por que?   
TAA\_COMO - Como?   
TAA\_DTIMPL - Data Impl.   
TAA\_DTINPR - Dt Ini Prev   
TAA\_DTFIPR - Dt Term Prev  
TAA\_DTINRE - Dt. Ini Real  
TAA\_DTFIRE - Dt Term Real  
TC9\_NOMRES - Nome  
  
**Vínculos:**  
Em **Atualizações > Ppra > Riscos**. Incluir um risco utilizando as informações anteriormente cadastradas e preencher o campo Mapa Risco **(TN0\_MAPRIS)** como "**2=SESMT**".   
  
Em **Atualizações > Laudos > Laudos**. Incluir um laudo tendo o campo Tipo Laudo **(TO0\_TIPREL)** como **2=PCMSO**. Na aba de Conteúdo Laudo, adicionar o atalho "**PLANO**".  
  
Em **Atualizações > Ppra > Plano de****Ação**. Incluir um plano. Em **Atualizações > Ppra > Riscos x Plano****Ação**. Relacionar o plano ao risco. **Em Atualizações > Laudo > Laudos x Plano Açao**. Relacionar o plano ao laudo.   
  
Em **Atualizações > Laudo > Laudos x Riscos**. Relacionar o risco utilizado ao laudo. 2. PCMSO.  
  
Exemplo de cadastro: Como incluir um atalho **Plano** em um Laudo do tipo PCMSO.  
  
![IKIfSs4ncP.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360100730553)  
  
**Saiba Mais**  
[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos Laudos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012070273-MDT-Laudos)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
