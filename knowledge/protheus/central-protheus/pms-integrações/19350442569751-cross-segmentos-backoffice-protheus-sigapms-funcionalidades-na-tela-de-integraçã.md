---
article_id: 19350442569751
category: PMS - Integrações
content_hash: 47a64ba9f6a5006c04daa401fe887cd9d769f516ef491699689eac995c3cc699
fetched_at: '2026-06-28T22:37:16.754365+00:00'
product: protheus
section_id: 1500001550742
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Funcionalidades na tela de
  integração com MS Project
type: support-article
updated_at: '2024-02-26T18:31:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19350442569751-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Funcionalidades-na-tela-de-integra%C3%A7%C3%A3o-com-MS-Project
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19350434206615) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Qual funcionalidade das opções da tela de integração com o Microsoft Project?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAPMS - Todas as versões  
  
**Solução**

**A) Cópia em Arquivo temporário?**

Antes desta implementação, o SIGAPMS criava um arquivo temporário, cópia do MPP selecionado, para realizar a integração. A partir de agora, com esta nova opção, podemos indicar se trabalharemos com um arquivo temporário ou MPP original.

**OBS 1:** Se a opção "Projeto Semelhante" igual a “Sim”, não aconselhamos a utilização de arquivo temporário. Utilizando o arquivo original, podemos garantir que as informações contidas no Project e SIGAPMS estarão compatíveis para futuras integrações.

**B) Habilitar parâmetro MV\_PMSTX30?**

Indica se o sincronismo será apenas para atualizações pontuais no projeto como, por exemplo, descrições e durações. Deste modo o Protheus saberá quais linhas precisará processar no momento da importação, a fim de proporcionar uma melhor performance na rotina, sem a necessidade de reimportar todo o projeto.

**OBS 2:** Para que o Protheus saiba qual Tarefa e/ou EDT deverá ser considerada, deve-se alimentar a coluna Texto30 do MS Project com valor igual a 1, caso contrário a linha do Project será desconsiderada no momento da importação.

**C) Projeto Semelhante?**

Indica se o arquivo “.MPP” seleciona no sincronismo é semelhante ao existente/selecionado no SIGAPMS.

**OBS 3:** Este item deve ser usado somente quando utilizado novo conceito de IDProject/Texto 29, onde o arquivo .mpp e o SIGAPMS estão com os valores já alimentados e relacionados.

**Tela:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19350525928983)**
