---
article_id: 360026454974
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: c7c83b86eeff121f90f6ab6a4e534151ae31a7c5fa40931a95220649056f76a2
fetched_at: '2026-06-28T22:42:44.679779+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Objetivo do parâmetro MV_SEMAFGE
type: support-article
updated_at: '2024-03-14T17:58:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026454974-Manufatura-Linha-Protheus-SIGAPCP-Objetivo-do-par%C3%A2metro-MV-SEMAFGE
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura**: 00:00:45 min**  
**Dúvida**Qual o objetivo do parâmetro **MV\_SEMAFGE - Utiliza semáforo na geração de empenhos no MATA650 S-Sim/N-Não**?  
  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Em algumas empresas, mais de um usuário pode abrir **OP's - Ordens de Produções** e essas aberturas eventualmente ocorrem de maneira simultânea. Para garantir a integridade dos **Empenhos**, **OPI's - Ordens de Produção Intermediárias** e **SC's - Solicitações de Compras** que são gravados, evitando situações como empenhos duplicado, foi desenvolvido o parâmetro **MV\_SEMAFGE**.Habilitando o parâmetro, o Sistema controlará a integridade dos dados, garantindo que somente um usuário de cada vez executará o processo de registro de **Empenhos**, geração de **OPI's** e **SC's**.
