---
article_id: 360059777753
category: MDT - Laudos
content_hash: 273c106b50f7d19c7996da5603496d59f64f92423ffa2a0bd74c778134f7a6df
fetched_at: '2026-06-28T22:44:26.382714+00:00'
product: protheus
section_id: 360012070273
source: central-protheus
title: RH - Linha Protheus - MDT - Na elaboração de um Laudo para o tipo PCMSO (MDTA210)
  como incluir o atalho Requisitos
type: support-article
updated_at: '2023-12-11T11:14:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059777753-RH-Linha-Protheus-MDT-Na-elabora%C3%A7%C3%A3o-de-um-Laudo-para-o-tipo-PCMSO-MDTA210-como-incluir-o-atalho-Requisitos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19673952955671)** Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Quais os vínculos tabelas e campos utilizados para o Atalho Requisitos na elaboração de um Laudo para o tipo PCMSO?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Os Atalhos são consultas prontas no sistema para geração de laudos, e são gerados de acordo com o Tipo Laudo **(TO0\_TIPREL)**.   
Abaixo segue informações sobre os atalhos que podem ser utilizados na definição de um Laudo do Tipo PCMSO, as rotinas e campos envolvidos nesse processo e os seus vínculos.  
  
**Atalho**: Requisitos  
  
**Tabela:**TA0 - Requisitos Legais e Outros  
  
**Campos:**TA0\_CODLEG - Requisito   
TA0\_EMENTA - Tema da Lei   
TA0\_TIPO - Tipo   
TA0\_ORIGEM - Origem   
TA0\_CODRES - Resolução   
TA0\_NUMRES - Nº Resolução  
TA0\_OREMIS - Órgão Emis.   
TA0\_DTEMIS - Data Emissão  
TA0\_SITE - Site   
TA0\_DTVIGE - Vig. Inic.   
TA0\_DTVENCI - Vig. Fim   
TA0\_EST - Estado   
TA0\_DTVCTO - Dias Venc.   
TCM\_RESPON - Responsáveis  
TCL\_DESPLA - Plano de Ações do Requisito  
  
**Vínculos:**  
Em **Atualizações > Requisitos > Requisitos**. Incluir um requisito.   
  
Em **Atualizações > Laudos > Laudos**. Incluir um laudo tendo o campo Tipo Laudo **(TO0\_TIPREL)** como **2=PCMSO**. -Na aba de Conteúdo Laudo, adicionar o atalho "**REQUISITOS**".  
  
Em **Atualizações > Laudos > Laudos x Requis.** Relacionar o requisito ao laudo.  
  
![BKLXTYVxra.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360100736253)  
 **Saiba Mais**  
[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos Laudos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012070273-MDT-Laudos)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
