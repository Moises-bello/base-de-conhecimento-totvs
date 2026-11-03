---
article_id: 360059772353
category: MDT - Laudos
content_hash: ffaa808b9105e2ac121ea7f636359e1101442acf46843b4be462097e9ef96b3c
fetched_at: '2026-06-28T22:44:26.335095+00:00'
product: protheus
section_id: 360012070273
source: central-protheus
title: RH - Linha Protheus - MDT - Na elaboração de um Laudo para o tipo PCMSO (MDTA210)
  como incluir o atalho Controle
type: support-article
updated_at: '2023-12-08T14:25:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059772353-RH-Linha-Protheus-MDT-Na-elabora%C3%A7%C3%A3o-de-um-Laudo-para-o-tipo-PCMSO-MDTA210-como-incluir-o-atalho-Controle
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19642297979415)** Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Quais os vínculos tabelas e campos utilizados para o **Atalho Controle** na elaboração de um Laudo para o tipo PCMSO?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Os Atalhos são consultas prontas no sistema para geração de laudos, e são gerados de acordo com o Tipo Laudo **(TO0\_TIPREL)**.   
Abaixo segue informações sobre os atalhos que podem ser utilizados na definição de um Laudo do Tipo PCMSO, as rotinas e campos envolvidos nesse processo e os seus vínculos.  
**Atalho:** Controle  
  
**Tabelas:**  
TO4 - Medidas de Controle   
TO3 - Laudos x Medidas de Controle   
  
**Campos:**  
TO4\_NOMCTR - Nome   
TO3\_DESCRI - Descrição  
  
**Vínculos:**  
Em **Atualizações > Ppra > Riscos**. Incluir um risco.   
  
Em **Atualizações > Ppra > Medidas Controles**. Incluir uma medida de controle.   
  
Em **Atualizações > Laudos > Laudos**. Incluir um laudo tendo o campo Tipo Laudo **(TO0\_TIPREL)** como **2=PCMSO**. Na aba de Conteúdo Laudo, adicionar o atalho "**CONTROLE**". Em **Atualizações > Laudo > Laudos x Riscos**. Relacionar o risco utilizado ao laudo.   
  
Em **Atualizações > Laudo > Laudos x Controles**. Relacionar a medida de controle ao laudo.  
  
Exemplo de cadastro: Como incluir um atalho **Controle** em um Laudo do tipo PCMSO.  
  
![eWiG4EwNp7.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360100729913)  
 **Saiba Mais**  
[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos Laudos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012070273-MDT-Laudos)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
