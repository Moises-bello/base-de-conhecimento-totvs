---
article_id: 360059774513
category: MDT - Laudos
content_hash: 439f7afed1a6be06262aa7507842f2882b5ad090e1f0d4e8dc7e97e416f33b08
fetched_at: '2026-06-28T22:44:26.369041+00:00'
product: protheus
section_id: 360012070273
source: central-protheus
title: RH - Linha Protheus - MDT - Na elaboração de um Laudo para o tipo PCMSO (MDTA210)
  como incluir o atalho Programa
type: support-article
updated_at: '2023-12-11T11:13:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059774513-RH-Linha-Protheus-MDT-Na-elabora%C3%A7%C3%A3o-de-um-Laudo-para-o-tipo-PCMSO-MDTA210-como-incluir-o-atalho-Programa
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19673755196055)** Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Quais os vínculos tabelas e campos utilizados para o **Atalho Programa** na elaboração de um Laudo para o tipo PCMSO?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Os Atalhos são consultas prontas no sistema para geração de laudos, e são gerados de acordo com o Tipo Laudo **(TO0\_TIPREL)**.   
Abaixo segue informações sobre os atalhos que podem ser utilizados na definição de um Laudo do Tipo PCMSO, as rotinas e campos envolvidos nesse processo e os seus vínculos.  
**Atalho**: Programa  
  
**Tabela:**TMO - Programas de Saúde  
  
**Campos:**TMO\_NOMPRO - Nome   
TMO\_DESPRO - Descrição   
  
**Vínculos:**  
Em **Atualizações > Pcmso > Exames Progr.saude**. Incluir um programa e adicionar exames.   
  
Em **Atualizações > Ppra > Riscos**. Incluir um risco.   
  
Em **Atualizações > Laudos > Laudos**. Incluir um laudo tendo o campo Tipo Laudo **(TO0\_TIPREL)** como **2=PCMSO**. Na aba de Conteúdo Laudo, adicionar o atalho "**PROGRAMA**".   
  
Em **Atualizações > Laudo > Laudos x Riscos**. Relacionar o risco utilizado ao laudo.   
  
Em **Atualizações > Laudos > Laudos x Prog.****Saúde**. Relacionar o programa ao laudo. um risco ao laudo.  
  
Exemplo de cadastro: Como incluir um atalho **Programa** em um Laudo do tipo PCMSO.  
  
![olD5hFn4oq.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360098484094)  
  
**Saiba Mais**  
[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos Laudos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012070273-MDT-Laudos)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
