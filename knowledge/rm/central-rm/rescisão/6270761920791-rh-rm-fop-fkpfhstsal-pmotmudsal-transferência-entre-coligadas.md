---
article_id: 6270761920791
category: Rescisão
content_hash: 1c356fb9ee31e9d838015be7b651829c83d8f6e14bb18c64ce0b1f6d25677e1e
fetched_at: '2026-06-28T22:46:54.343537+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: RH - RM - FOP - "FKPFHSTSAL_PMOTMUDSAL" transferência entre coligadas
type: support-article
updated_at: '2024-09-16T18:31:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6270761920791-RH-RM-FOP-FKPFHSTSAL-PMOTMUDSAL-transfer%C3%AAncia-entre-coligadas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:45 min****Ocorrência**Ao tentar realizar uma transferência entre coligadas o sistema apresenta a seguinte mensagem de erro: **"Funcionário XXXXXXX: Houve um erro de incompatibilidade de informações entre as coligadas, não foi encontrado o código na coligada destino. The INSERT statement conflicted with the FOREIGN KEY constraint** **"FKPFHSTSAL\_PMOTMUDSAL". The conflict occurred in database "CorporeRMV12", table "dbo.PMOTMUDSAL".**  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Essa mensagem é gerada pois o sistema encontrou incompatibilidade de registros na tabela de **FKPFHSTSAL\_PMOTMUDSAL - Motivo da mudança (alteração salarial).**![](https://centraldeatendimento.totvs.com/hc/pt-br/article_attachments/13742647421975/52bd3eb23b9bda9a1c475e8d6bd649655ed434925317499761c7e2f4d97af6c1.png)  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. **Acesse Administração de Pessoal | Cadastros Globais | Tabelas Dinâmicas   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13741447863575)**2. Realizar a copia entre coligadas:  
  
[RH - RM - FOP - Cópia de registros entre coligadas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021778232-RH-RM-FOP-C%C3%B3pia-de-registros-entre-coligadas)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13742128960791)  
  
3. Feito isso, faça todo o processo de transferência entre coligadas e a mensagem de erro não será mais apresentada.  
  
**Saiba mais**[RH - RM - FOP - Transferência entre filiais ou coligadas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020186252-RH-RM-FOP-Transfer%C3%AAncia-entre-filiais-ou-coligadas)
