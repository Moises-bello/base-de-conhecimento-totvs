---
article_id: 360057931374
category: MDT - Laudos
content_hash: 8d1715fa19b6b734b584f98cb9bc0a1d7795a99966037f21be0db8af1b91ec27
fetched_at: '2026-06-28T22:44:26.347758+00:00'
product: protheus
section_id: 360012070273
source: central-protheus
title: RH - Linha Protheus - MDT - Na elaboração de um Laudo para o tipo PCMSO (MDTA210)
  como incluir o atalho Exames
type: support-article
updated_at: '2025-03-03T12:29:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057931374-RH-Linha-Protheus-MDT-Na-elabora%C3%A7%C3%A3o-de-um-Laudo-para-o-tipo-PCMSO-MDTA210-como-incluir-o-atalho-Exames
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19643276145943)** Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Quais os vínculos tabelas e campos utilizados para o **Atalho Exames** na elaboração de um Laudo para o tipo PCMSO?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Os Atalhos são consultas prontas no sistema para geração de laudos, e são gerados de acordo com o Tipo Laudo **(TO0\_TIPREL).**Abaixo segue informações sobre os atalhos que podem ser utilizados na definição de um Laudo do Tipo PCMSO, as rotinas e campos envolvidos nesse processo e os seus vínculos.  
  
**Atalho:** Exames  
  
**Tabela:**  
TM4 - Exames   
  
**Campo:**TM4\_NOMEXA - Nome Exame  
  
**Vínculos:**Em **Atualizações > Ppra > Riscos**. Incluir um risco. Em **Atualizações > Pcmso > Exames Por Risco**. Relacionar exames ao risco utilizado.   
  
Em **Atualizações > Laudos > Laudos**. Incluir um laudo tendo o campo Tipo Laudo **(TO0\_TIPREL)** como **2=PCMSO**. Na aba de Conteúdo Laudo, adicionar o atalho "**EXAMES**".   
  
Em **Atualizações > Laudo > Laudos x Riscos**. Relacionar o risco utilizado ao laudo**.**Exemplo de cadastro: Como incluir um atalho **Exames** em um Laudo do tipo PCMSO.  
  
![jpHf5o0zgq.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360100729993)  
  
**Saiba Mais**  
[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos Laudos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012070273-MDT-Laudos)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
