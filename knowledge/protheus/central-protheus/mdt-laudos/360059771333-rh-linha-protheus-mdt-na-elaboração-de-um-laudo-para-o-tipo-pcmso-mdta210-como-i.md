---
article_id: 360059771333
category: MDT - Laudos
content_hash: d1c39fdde08ceb737ec3f986f30c471d5157e84eba16ed0e33e9b9234fa43792
fetched_at: '2026-06-28T22:44:26.351989+00:00'
product: protheus
section_id: 360012070273
source: central-protheus
title: RH - Linha Protheus - MDT - Na elaboração de um Laudo para o tipo PCMSO (MDTA210)
  como incluir o atalho Funcionário x Função
type: support-article
updated_at: '2025-03-03T12:29:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059771333-RH-Linha-Protheus-MDT-Na-elabora%C3%A7%C3%A3o-de-um-Laudo-para-o-tipo-PCMSO-MDTA210-como-incluir-o-atalho-Funcion%C3%A1rio-x-Fun%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19645552250647)** Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Quais os vínculos tabelas e campos utilizados para o **Atalho Funcionário x Função** na elaboração de um Laudo para o tipo PCMSO?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Os Atalhos são consultas prontas no sistema para geração de laudos, e são gerados de acordo com o Tipo Laudo **(TO0\_TIPREL).**   
Abaixo segue informações sobre os atalhos que podem ser utilizados na definição de um Laudo do Tipo PCMSO, as rotinas e campos envolvidos nesse processo e os seus vínculos.  
 **Atalho**: Funcionário x Funções  
  
**Tabela:**  
SRJ - Funções  
  
**Campo:**RJ\_FUNCAO - Função  
  
**Vínculos:**Em **Atualizações > Ppra > Riscos**. Incluir um risco.   
  
Em **Atualizações > Laudos > Laudos.** Incluir um laudo tendo o campo Tipo Laudo **(TO0\_TIPREL)** como **2=PCMSO**. -Na aba de **Conteúdo Laudo**, adicionar o atalho "**FUNCIONARIOS X FUNCAO**".   
  
Em **Atualizações > Laudos > Laudos x Riscos**. Relacionar o risco ao laudo.  
  
Exemplo de cadastro: Como incluir um atalho **Funcionário x Função** em um Laudo do tipo PCMSO.  
  
![KogQlQQG0O.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360098472654)  
  
**Saiba Mais**  
[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos Laudos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012070273-MDT-Laudos)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
