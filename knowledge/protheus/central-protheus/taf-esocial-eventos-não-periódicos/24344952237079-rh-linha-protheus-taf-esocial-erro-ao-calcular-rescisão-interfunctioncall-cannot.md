---
article_id: 24344952237079
category: TAF - eSocial - Eventos Não Periódicos
content_hash: 6a8c7d980dab6b872d7f85c7c8c62d54123dad44b321e4a977e69d71a913f5ca
fetched_at: '2026-06-28T22:45:18.113708+00:00'
product: protheus
section_id: 1500001548002
source: central-protheus
title: 'RH - Linha Protheus - TAF - eSocial - Erro ao calcular rescisão - InterFunctionCall:
  cannot find function TPCONCOM in AppMap on X3CBOX(AP5TRANSLATE.PRW)'
type: support-article
updated_at: '2026-06-24T21:26:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24344952237079-RH-Linha-Protheus-TAF-eSocial-Erro-ao-calcular-rescis%C3%A3o-InterFunctionCall-cannot-find-function-TPCONCOM-in-AppMap-on-X3CBOX-AP5TRANSLATE-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24344952197655) Tempo aproximado para leitura: **HH:MM:SS min**  
  
**Ocorrência**  
Ao calcular rescisão no módulo do SIGAGPE o erro abaixo é apresentado:

THREAD ERROR ([2816]) 21/06/2024 09:35:46  
InterFunctionCall: cannot find function TPCONCOM in AppMap on X3CBOX(AP5TRANSLATE.PRW) 17/05/2024 16:58:37 line : 410  
  
  
**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Todas as versões

**Solução**  
Para correção será necessário aplicar a expedição contínua completa do TAF (RPO + Dicionário + UPDDISTR).

12.1.2210: <https://suporte.totvs.com/portal/p/10098/download#detail/1084563>

12.1.2310: <https://suporte.totvs.com/portal/p/10098/download#detail/1126399>

12.1.2410: <https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1174332>

12.1.2510: <https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1228187>

Como aplicar expedição contínua:

[RH - Linha Protheus - TAF - ATUALIZAÇÃO - Como atualizar o TAF E-social (Expedição Contínua)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18972648169239-RH-Linha-Protheus-TAF-ATUALIZA%C3%87%C3%83O-Como-atualizar-o-TAF-E-social-Expedi%C3%A7%C3%A3o-Cont%C3%ADnua?source=search)

Para verificar se o pacote foi aplicado corretamente deverá acessar a tela de diagnóstico do TAF e comparar a data do dicionário e repositório de fontes, ambos precisam constar com a data do pacote.

[RH - Linha Protheus - TAF - eSocial - Rotinas Comuns - Como acessar a tela de diagnóstico no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17988545143063-RH-Linha-Protheus-TAF-eSocial-Rotinas-Comuns-Como-acessar-a-tela-de-diagn%C3%B3stico-no-TAF?source=search)
