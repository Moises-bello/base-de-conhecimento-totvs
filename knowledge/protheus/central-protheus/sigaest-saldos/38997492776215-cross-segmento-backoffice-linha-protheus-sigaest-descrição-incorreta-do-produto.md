---
article_id: 38997492776215
category: SIGAEST - SALDOS
content_hash: 80a0deb99cd54b86eb3f5bcec17261859a94424fda57ab8457f312783ec04f31
fetched_at: '2026-06-28T22:39:14.819715+00:00'
product: protheus
section_id: 1500001538801
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Descrição incorreta
  do produto na tela de Consulta F4 de Saldos em Estoque
type: support-article
updated_at: '2026-03-23T20:23:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38997492776215-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Descri%C3%A7%C3%A3o-incorreta-do-produto-na-tela-de-Consulta-F4-de-Saldos-em-Estoque
---

Foi corrigido o problema em que, ao consultar o Saldo em Estoque pela tecla F4, aparecia a descrição de outro produto no TOTVS Backoffice (Linha Protheus). A solução está na atualização do pacote de manutenção DMANMAT01-47775 para as versões 12.1.2310, 12.1.2410 e 12.1.2510, com links para download e teste em ambiente de homologação antes da produção.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38997492769047) Tempo aproximado para leitura: **00:02:15 min**  
  
**Ocorrência**

Na consulta F4 de saldos em estoque, a descrição do produto está incorreta/divergente do cadastro (SB1). O sistema apresenta descrição diferente do código informado.

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**

Foi identificado e corrigido na ISSUE  de manutenção [DMANMAT01-47775](https://tdn.totvs.com/x/VOZ_Pg). Para solucionar essa ocorrência, realize os seguintes passos: aplicar am base de homologação o pacote abaixo para o respectivo release de seu ambiente e testar antes de sua Base de produção.

***12.1.2310:***[***https://r.totvs.io/p/1241812***](https://r.totvs.io/p/1241812)***;***

***12.1.2410:***[***https://r.totvs.io/p/1241813***](https://r.totvs.io/p/1241813)***;***

***12.1.2510:***[***https://r.totvs.io/p/1241814***](https://r.totvs.io/p/1241814)***;***

***Saiba Mais:***

[Clique aqui e veja mais artigos sobre SALDOS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538801-SIGAEST-SALDOS)

[Backoffice (Linha Protheus) - SIGAEST - Como descobrir a origem dos saldos na consulta com comando [F4] no Produto?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020380572-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-descobrir-a-origem-dos-saldos-na-consulta-com-comando-F4-no-Produto)
