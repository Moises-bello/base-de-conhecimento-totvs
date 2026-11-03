---
article_id: 10118026726679
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 605ba442683e74d90930e89c54e6b59372592895ab4118ee33757ed82f6ccf29
fetched_at: '2026-06-28T22:42:45.739557+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: 'Manufatura - Linha Protheus - SIGAPCP - Problema: A integração com o MRP este
  desativada por algum período ou não foi concluída'
type: support-article
updated_at: '2024-08-21T03:14:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10118026726679-Manufatura-Linha-Protheus-SIGAPCP-Problema-A-integra%C3%A7%C3%A3o-com-o-MRP-este-desativada-por-algum-per%C3%ADodo-ou-n%C3%A3o-foi-conclu%C3%ADda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:41 min****Ocorrência**Ao abrir a rotina **PCPA712 - MRP****Memória** é apresentada a mensagem: **Problema: A integração com o MRP este desativada por algum período ou não foi concluída. Para garantir a integridade das informações do MRP será necessário executar a sincronização das seguintes entidades:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10118467722007)

**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Causa**Isso ocorre pois a integração do **MRP Memória** foi desativado e posteriormente ativado na rotina **PCPA139 - Parâmetros de integração do MRP**  
**Solução**Para resolver esta situação é necessário realizar a sincronização dos dados através da rotina **PCPA140 - Sincronização**.
