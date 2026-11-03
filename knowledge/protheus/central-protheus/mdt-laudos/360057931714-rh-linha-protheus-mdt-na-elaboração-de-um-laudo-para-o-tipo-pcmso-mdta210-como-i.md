---
article_id: 360057931714
category: MDT - Laudos
content_hash: 6fc8cd65f97263ac1f1fdac95866e6ddf1b747d7fcf3e26f7ec0fc208626d1e2
fetched_at: '2026-06-28T22:44:26.391690+00:00'
product: protheus
section_id: 360012070273
source: central-protheus
title: RH - Linha Protheus - MDT - Na elaboração de um Laudo para o tipo PCMSO (MDTA210)
  como incluir o atalho Sesmt
type: support-article
updated_at: '2023-12-11T11:15:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057931714-RH-Linha-Protheus-MDT-Na-elabora%C3%A7%C3%A3o-de-um-Laudo-para-o-tipo-PCMSO-MDTA210-como-incluir-o-atalho-Sesmt
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19674056476567)** Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Quais os vínculos tabelas e campos utilizados para o **Atalho Sesmt** na elaboração de um Laudo para o tipo PCMSO?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Os Atalhos são consultas prontas no sistema para geração de laudos, e são gerados de acordo com o Tipo Laudo **(TO0\_TIPREL)**.Abaixo segue informações sobre os atalhos que podem ser utilizados na definição de um Laudo do Tipo PCMSO, as rotinas e campos envolvidos nesse processo e os seus vínculos.  
 **Atalho:** Sesmt  
  
**Tabela:**  
TMK - Usuários de Medicina e Segurança  
  
**Campo:**  
TMK\_INDFUN - Função  
  
**Vínculos:**Em **Atualizações > Semst > Sesmt/Usuar.aten**. Preenhcer o campo Compõe SESMT **(TMK\_SESMT)** como "**1=Sim**".   
  
Em **Atualizações > Laudos > Laudos**. Incluir um laudo tendo o campo Tipo Laudo **(TO0\_TIPREL)** como **2=PCMSO**. Na aba de Conteúdo Laudo, adicionar o atalho "**SESMT**".  
  
Exemplo de cadastro: Como incluir um atalho **Sesmt** em um Laudo do tipo PCMSO.  
  
![cbG8XiVanC.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360100730293)  
  
**Saiba Mais**  
[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos Laudos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012070273-MDT-Laudos)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
