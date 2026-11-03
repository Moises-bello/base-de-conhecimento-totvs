---
article_id: 360021954272
category: Financeiro - Integrações (SIGAFIN)
content_hash: fdb2a80424132528a06b1211edb4f91f9fabfedcd37c477c65aca9b9cbb1a717
fetched_at: '2026-06-28T22:38:18.533585+00:00'
product: protheus
section_id: 1500001539241
source: central-protheus
title: MP- SIGAFIN - Integração Centro de custo x Reserve
type: support-article
updated_at: '2022-03-23T02:41:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021954272-MP-SIGAFIN-Integra%C3%A7%C3%A3o-Centro-de-custo-x-Reserve
---

**Dúvida**Como integrar um Centro de custo do Protheus com o Reserve?  
   
 **Ambiente**Microsiga Protheus – Financeiro – A partir da versão 12.  
   
**Solução**Para que haja a integração de um centro de custo com o Reserve, é necessário que os seguintes campos estejam preenchidos:

| CTT |
| --- |
| CTT\_CODIGO |
| CTT\_DESC01 |
| CTT\_CLASSE |
| CTT\_BLOQ |
| CTT\_INTRES |

**Importante**  
- A integração será feita apenas para os registros que tiverem o campo CTT\_INTRES = SIM.   
- O campo CTT\_RESERV indica o status da inegração, onde  
1= Pendente de inclusão;  
2= Pendente alteração;  
3= Pendente exclusão;  
4= Sincronizado.
