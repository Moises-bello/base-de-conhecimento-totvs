---
article_id: 10573836744087
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 00df1a111c6c227ecde689d85f505570a5a29d7a01d20773693ed3b5f6a04c97
fetched_at: '2026-06-28T22:42:43.354783+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Gerar transferências previstas no MRP
  memoria
type: support-article
updated_at: '2022-11-29T19:47:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10573836744087-Manufatura-Linha-Protheus-SIGAPCP-Gerar-transfer%C3%AAncias-previstas-no-MRP-memoria
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:00:55 min  
  
Dúvida**É possível gerar transferências entre filias previstas no **PCPA712 - MRP Memória**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
Não é possível, a transferência entre filiais não possui um *status* de firme ou previsto como as **OPs - Ordens de Produção** e **SCs - Solicitações de Compra.**Independente de como selecionar para gerar os documentos, as transferências vão ser geradas, e o usuário vai precisar efetivar essas transferências através da rotina **MATA311 - Solicitação de Transferências**.  
Caso execute o **MRP** novamente, com o parâmetro para **excluir documentos previstos** marcado, as transferências que foram geradas pelo **MRP** e que não foram efetivadas vão ser eliminadas.  
  
**Importante**No **PCPA712**, o parâmetro **MV\_MRPGETR** não será mais utilizado, pois as transferências serão sempre geradas no **MRP Memória**.
