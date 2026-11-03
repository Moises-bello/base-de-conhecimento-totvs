---
article_id: 4441032963735
category: Financeiro - Novo Gestor Financeiro
content_hash: f5c99dc43463e625b5e2ab91e8ac4f89fe2addf4b8e63e35b2e6f65a264519f0
fetched_at: '2026-06-28T22:37:41.328125+00:00'
product: protheus
section_id: 33830415324183
source: central-protheus
title: Cross Segmento - Backoffice linha Protheus -  SIGAFIN - FINA710 - Mensagem
  FINA710REST ao acessar o Novo Gestor Financeiro / FINA716 - Ambiente incompatível
  Ocorrência Porta multiprotocolo não está habilitada no ambiente!
type: support-article
updated_at: '2026-03-04T17:15:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4441032963735-Cross-Segmento-Backoffice-linha-Protheus-SIGAFIN-FINA710-Mensagem-FINA710REST-ao-acessar-o-Novo-Gestor-Financeiro-FINA716-Ambiente-incompat%C3%ADvel-Ocorr%C3%AAncia-Porta-multiprotocolo-n%C3%A3o-est%C3%A1-habilitada-no-ambiente
---

**Dúvida**  
Ao acessar a rotina FINA710 - Painel Gestão apresentando “FINA710REST A Configuração da porta multiprotocolo não está habilitada no ambiente. Verifique a configuração para o uso do Novo Gestor Financeiro”.  Ao acessar a rotina FINA716 - Aplicação Empréstimo apresentando a mensagem "HELP - Ambiente incompatível - Ocorrência - Porta multiprotocolo não está habilitada no ambiente!"  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – FINA710 - A partir da versão 12.1.33

Segue exemplo ao acessar a rotina FINA716 - Aplicação Empréstimo

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/17490324691735)**

**Solução:**

Habilitar no appserver.ini a tag **MultiProtocolPort**

**[Drivers]**

**MultiProtocolPort=1**

Segue um exemplo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17490382912919)

**Segue documentação sobre o tema:**

[Novo Gestor Financeiro - (FINA710 - SIGAFIN)](https://tdn.totvs.com/pages/releaseview.action?pageId=611007335)

[Application Server - Porta Multiprotocolo](https://tdn.totvs.com/display/tec/Application+Server+-+Porta+Multiprotocolo)
