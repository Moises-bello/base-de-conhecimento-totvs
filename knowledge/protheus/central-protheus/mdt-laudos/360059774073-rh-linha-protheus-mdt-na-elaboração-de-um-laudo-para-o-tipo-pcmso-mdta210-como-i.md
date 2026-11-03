---
article_id: 360059774073
category: MDT - Laudos
content_hash: 9626e0d6bcbb6ff9c30511b193eebe0710ecf5efdaadd0ad067ea271352dc099
fetched_at: '2026-06-28T22:44:26.339770+00:00'
product: protheus
section_id: 360012070273
source: central-protheus
title: RH - Linha Protheus - MDT - Na elaboração de um Laudo para o tipo PCMSO (MDTA210)
  como incluir o atalho Cronograma
type: support-article
updated_at: '2023-12-08T14:25:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059774073-RH-Linha-Protheus-MDT-Na-elabora%C3%A7%C3%A3o-de-um-Laudo-para-o-tipo-PCMSO-MDTA210-como-incluir-o-atalho-Cronograma
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19642522155031)** Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Quais os vínculos tabelas e campos utilizados para o **Atalho Cronograma** na elaboração de um Laudo para o tipo PCMSO?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Os Atalhos são consultas prontas no sistema para geração de laudos, e são gerados de acordo com o Tipo Laudo **(TO0\_TIPREL)**.   
Abaixo segue informações sobre os atalhos que podem ser utilizados na definição de um Laudo do Tipo PCMSO, as rotinas e campos envolvidos nesse processo e os seus vínculos.  
**Atalho**: Cronograma  
  
**Tabela:**TAA - Plano de Ação  
  
**Campos:**TAA\_NOME - Nome Plano   
TAA\_DTINPR - Dt Ini Prev   
TAA\_DTFIRE - Dt Term Real  
  
**Vínculos:**  
Em **Atualizações > Ppra > Riscos**. Incluir um risco utilizando as informações anteriormente cadastradas e preencher o campo Mapa Risco **(TN0\_MAPRIS)** como "**2=SESMT**".   
  
Em **Atualizações > Laudos > Laudos**. Incluir um laudo tendo o campo Tipo Laudo **(TO0\_TIPREL)** como **2=PCMSO**. Na aba de Conteúdo Laudo, adicionar o atalho "**CRONOGRAMA**".   
  
Em **Atualizações > Ppra > Plano de****Ação**. Incluir um plano. Em **Atualizações > Ppra > Riscos x Plano****Ação**. Relacionar o plano ao risco.   
  
Em **Atualizações > Laudo > Laudos x Plano****Ação**. Relacionar o plano ao laudo. Em A**tualizações > Laudo > Laudos x Riscos**. Relacionar o risco utilizado ao laudo.   
  
Exemplo de cadastro: Como incluir um atalho **Cronograma** em um Laudo do tipo PCMSO.  
  
![MXyHbRLnOt.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360100731273)  
 **Saiba Mais**  
[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos Laudos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012070273-MDT-Laudos)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
