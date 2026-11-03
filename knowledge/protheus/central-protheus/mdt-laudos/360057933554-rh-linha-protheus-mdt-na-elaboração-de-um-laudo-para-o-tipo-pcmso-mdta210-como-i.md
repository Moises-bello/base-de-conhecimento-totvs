---
article_id: 360057933554
category: MDT - Laudos
content_hash: 1232eaed68ca5a7a71a91fa579ecd651bf261f3a2234e20981931069dcbd4060
fetched_at: '2026-06-28T22:44:26.378393+00:00'
product: protheus
section_id: 360012070273
source: central-protheus
title: RH - Linha Protheus - MDT - Na elaboração de um Laudo para o tipo PCMSO (MDTA210)
  como incluir o atalho Quadro dos Funcionários
type: support-article
updated_at: '2023-12-11T11:13:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057933554-RH-Linha-Protheus-MDT-Na-elabora%C3%A7%C3%A3o-de-um-Laudo-para-o-tipo-PCMSO-MDTA210-como-incluir-o-atalho-Quadro-dos-Funcion%C3%A1rios
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19673888603415)** Tempo aproximado para leitura:**00:02:00 min  
  
Dúvida**Quais os vínculos tabelas e campos utilizados para o **Atalho Quadro Funcionários** na elaboração de um Laudo para o tipo PCMSO?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Os Atalhos são consultas prontas no sistema para geração de laudos, e são gerados de acordo com o Tipo Laudo **(TO0\_TIPREL)**.   
Abaixo segue informações sobre os atalhos que podem ser utilizados na definição de um Laudo do Tipo PCMSO, as rotinas e campos envolvidos nesse processo e os seus vínculos.  
  
**Atalho**: Quadro Funcionários  
  
**Tabela:**SRA - Funcionários  
  
**Campos:**RA\_MAT - Matricula   
RA\_NOME - Nome   
  
**Vínculos:**  
Em **Atualizações > Ppra > Riscos**. Incluir um risco utilizando as informações anteriormente cadastradas e preencher o campo Mapa Risco (**TN0\_MAPRIS**) como "**2=SESMT**".  
  
Em **Atualizações > Laudos > Laudos**. Incluir um laudo tendo o campo Tipo Laudo (**TO0\_TIPREL**) como **2=PCMSO**. Na aba de Conteúdo Laudo, adicionar o atalho "**QUADRO FUNCIONÁRIOS**".  
  
Exemplo de cadastro: Como incluir um atalho **Quadro Funcionários** em um Laudo do tipo PCMSO.  
  
![EWYDbHSve2.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360098485014)

**Saiba Mais**  
[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos Laudos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012070273-MDT-Laudos)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
