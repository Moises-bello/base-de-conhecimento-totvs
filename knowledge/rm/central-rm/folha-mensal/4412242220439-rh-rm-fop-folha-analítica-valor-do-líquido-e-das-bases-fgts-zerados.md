---
article_id: 4412242220439
category: Folha Mensal
content_hash: 92505d70be9bfd6facda8e11412b918432c72b6f51563a1b843a9101cfd32885
fetched_at: '2026-06-28T22:46:59.356296+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Folha Analítica: valor do líquido e das bases FGTS zerados'
type: support-article
updated_at: '2024-10-18T15:19:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412242220439-RH-RM-FOP-Folha-Anal%C3%ADtica-valor-do-l%C3%ADquido-e-das-bases-FGTS-zerados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao gerar folha analítica o sistema não retorna o valor da BASE FGTS SEFIP e o liquido do funcionário.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412242296983/mceclip0.png)  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Esse incidente ocorre devido a uma inconsistência na versão do sistema.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Acesse: **Gestão | RM Reports**, realize a exclusão de todos os relatórios da folha analítica importados. Segue abaixo documentação para lhe auxiliar no processo.  
  
[RH - RM - FOP - RM Reports: Exclusão de Relatórios](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411688075799-RH-RM-FOP-RM-Reports-Exclus%C3%A3o-de-Relat%C3%B3rios?source=search)  
  
2. Logo, importe o **relatório FOPREL0009** novamente. Segue abaixo documentação para lhe auxiliar no processo.  
  
[RH - RM - FOP - RM Reports: Importação de Relatórios](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007544951-RH-RM-FOP-RM-Reports-Importa%C3%A7%C3%A3o-de-Relat%C3%B3rios?source=search)  
  
3. Após realizar os passos 1 e 2 gere a folha analítica novamente.  
  
**Importante**Caso mesmo com o processo de exclusão e importação persista a inconsistência na folha analítica, por gentileza, crie um novo perfil de parâmetro da folha analítica.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405815554199/mceclip1.png)
