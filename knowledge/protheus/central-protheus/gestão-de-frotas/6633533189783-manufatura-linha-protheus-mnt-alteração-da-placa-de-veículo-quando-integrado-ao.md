---
article_id: 6633533189783
category: Gestão de Frotas
content_hash: 5eabfd3f30ac61a06aabd0790ad9d64035bec2cfc51c3251ac0b2e713a2f14d3
fetched_at: '2026-06-28T22:42:39.282781+00:00'
product: protheus
section_id: 360012117873
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Alteração da placa de veículo quando integrado
  ao SIGATMS
type: support-article
updated_at: '2022-06-08T20:45:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6633533189783-Manufatura-Linha-Protheus-MNT-Altera%C3%A7%C3%A3o-da-placa-de-ve%C3%ADculo-quando-integrado-ao-SIGATMS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:45 min****Dúvida**Como alterar o campo **Placa** de um **Veículo** no módulo **SIGAGFR - Gestão de Frotas** quando existe integração com o módulo **SIGATMS - Gestão de Transportes**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Gestão de Frotas - Versão 12  
  
**Solução**Quando o veículo está cadastrado no **MNTA084** com o campo Categoria - T9\_CATBEM igual a 2 - Frota integrada ao TMS, para alterar a **Placa** do mesmo, realize os seguintes passos:

1. Altere primeiramente no módulo do **SIGATMS** em **Atualizações\Transporte\Veículos - OMSA060**
2. Em seguida, altere no módulo **SIGAGFR** em **Atualizações\Cadastros\Veículos - MNTA084**

**Importante**  
O parâmetro que indica a integração entre os módulos é **MV\_NGMNTMS - Integração do Manutenção de Ativos - MNT com Gestão de Transporte - TMS**.
