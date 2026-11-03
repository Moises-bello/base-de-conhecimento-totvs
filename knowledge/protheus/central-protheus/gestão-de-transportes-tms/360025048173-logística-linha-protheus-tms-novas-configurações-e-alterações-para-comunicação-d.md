---
article_id: 360025048173
category: Gestão de Transportes (TMS)
content_hash: 9a1bc78945b360f537026155c2c43d79d0f7d7c14121dd2192d80cfd5c444a65
fetched_at: '2026-06-28T22:45:29.479248+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Novas configurações e alterações para comunicação
  da integração com a Pamcard
type: support-article
updated_at: '2021-12-21T16:53:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025048173-Log%C3%ADstica-Linha-Protheus-TMS-Novas-configura%C3%A7%C3%B5es-e-altera%C3%A7%C3%B5es-para-comunica%C3%A7%C3%A3o-da-integra%C3%A7%C3%A3o-com-a-Pamcard
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:30 min****Dúvida**Quais foram as novas alterações feitas para atender as **mudanças de comunicação na integração com a operadora de frota Pamcard**?  
  
**Ambiente**

TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS)  - Todas as versões  
  
**Solução**

1. Permitir a seleção de um arquivo **.pfx** no **Cadastro de Operadoras** e fazer com que este arquivo seja quebrado em arquivos **.pem.**  
   1.1 - Para esse processo deve ser usado a **URL**:   [https://www.roadcard.com.br/ sistemapamcard/services/WSTran sacional](https://www.roadcard.com.br/sistemapamcard/services/WSTransacional)
2. Permitir que os arquivos **.crt** continuem sendo utilizados na integração.
3. Definição de qual o método de integração a partir do **Cadastro do Certificado**.
4. Integração entre **SIGATMS - Gestão de Transportes x Pamcard**, das seguintes funcionalidades:
   1. Cálculo do valor do pedágio.
   2. Inclusão de **Contrato** na **Pamcard**.
   3. Geração de **CIOT - Código Identificador de Operação de Transporte**.
   4. Apontamento de **Saída** da viagem - Liberação da parcela de **Adiantamento**.
   5. Pagamento de **Saldo** e **Liberação do Contrato de Carreteiro** - Criação da parcela do saldo do frete.
   6. Geração do **CIOT** por período.
   7. Encerramento do **CIOT**.
5. Utilização do parâmetro **MV\_TMSXML**, para gravar as mensagens integradas entre o **SIGATMS** e o **Pamcard**, pelos arquivos **XML**.

Saiba Mais  
Mais informações poderão ser acessadas no*link's*:   
[DT Pamcard - Alteração no Modelo de Comunicação - ICP Brasil](http://tdn.totvs.com/pages/viewpage.action?pageId=349187659)  
[DT Troca do Certificado na Integração Entre SIGATMS x Pamcard](http://tdn.totvs.com/pages/viewpage.action?pageId=385848487)  
[DT Pamcard - Cancelamento de Cartão](http://tdn.totvs.com/pages/viewpage.action?pageId=390407676)[DT Pamcard - CIOT Por Período](http://tdn.totvs.com/pages/viewpage.action?pageId=307835680)[DT Pamcard - Mais de um Cartão na Viagem](http://tdn.totvs.com/pages/viewpage.action?pageId=359470260)
