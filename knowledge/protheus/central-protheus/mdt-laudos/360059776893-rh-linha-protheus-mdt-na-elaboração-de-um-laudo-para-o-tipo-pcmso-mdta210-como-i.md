---
article_id: 360059776893
category: MDT - Laudos
content_hash: d116be2566329dbfb19c92c360e50331521e18dfa45d3ac4265d954a67d290d2
fetched_at: '2026-06-28T22:44:26.330629+00:00'
product: protheus
section_id: 360012070273
source: central-protheus
title: RH - Linha Protheus - MDT - Na elaboração de um Laudo para o tipo PCMSO (MDTA210)
  como incluir o atalho Anexo B
type: support-article
updated_at: '2023-12-07T13:45:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059776893-RH-Linha-Protheus-MDT-Na-elabora%C3%A7%C3%A3o-de-um-Laudo-para-o-tipo-PCMSO-MDTA210-como-incluir-o-atalho-Anexo-B
---

**![time.png](https://centraldeatendimento.totvs.com/guide-media/01GVK0XPESEK73YY0FKEGBFP3Z)** Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Quais os vínculos tabelas e campos utilizados para o **Atalho Anexo B** na elaboração de um Laudo para o tipo PCMSO?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Os Atalhos são consultas prontas no sistema para geração de laudos, e são gerados de acordo com o Tipo Laudo **(TO0\_TIPREL)**.   
Abaixo segue informações sobre os atalhos que podem ser utilizados na definição de um Laudo do Tipo PCMSO, as rotinas e campos envolvidos nesse processo e os seus vínculos.  
  
**Atalho**: Anexo B  
  
**Tabelas:**TO1 - Laudos x Riscos   
SRJ - Funções   
TMA - Agente   
TN2 - Exames por Risco   
SRA - FuncionariosTN0 - Risco   
  
**Campos:**RJ\_DESC - Descrição   
TMA\_GRISCO - Grupo   
TMA\_NOMAGE - Nome Agente   
TN2\_FAIXA - Faixa   
TO1\_RECOME - Recomendação  
RA\_CC - Centro Custo  
TN0\_CODFUN - Função  
  
**Vínculos:**  
Em **Atualizações > Ppra > Agentes**. Incluir um agente.   
  
Em **Atualizações > Ppra > Riscos**. Incluir um risco utilizando as informações anteriormente cadastradas e preencher o campo Mapa Risco **(TN0\_MAPRIS)** como "**2=SESMT**".  
  
Em **Atualizações > Pcmso > Exames Por Risco**. Relacionar um exame ao risco.   
  
Em **Atualizações > Laudos > Laudos**. Incluir um laudo tendo o campo Tipo Laudo (**TO0\_TIPREL**) como **2=PCMSO**. Na aba de Conteúdo Laudo, adicionar o atalho "**ANEXO B**".   
  
Em **Atualizações > Laudos > Laudos x Riscos**. Relacionar o risco ao laudo.  
  
Exemplo de cadastro: Como incluir um atalho **Anexo B** em um Laudo do tipo PCMSO.  
  
![o1G0xQVia7.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360098486934)  
 **Saiba Mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos Laudos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012070273-MDT-Laudos)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
