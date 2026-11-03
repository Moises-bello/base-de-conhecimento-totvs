---
article_id: 10792187679511
category: Comércio Exterior - Easy Export Control - Tabelas
content_hash: a16a3275565a0fc1e5b2978aed72b8545a21dca8a99fd068fc35777801490a67
fetched_at: '2026-06-28T22:37:01.398027+00:00'
product: protheus
section_id: 1500001549222
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC -  Como corrigir
  a mensagem, Registro Inválido A cotação da moeda informada não foi alterada ao integrar
  cotação de moedas do Logix?
type: support-article
updated_at: '2022-12-08T12:53:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10792187679511-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Como-corrigir-a-mensagem-Registro-Inv%C3%A1lido-A-cota%C3%A7%C3%A3o-da-moeda-informada-n%C3%A3o-foi-alterada-ao-integrar-cota%C3%A7%C3%A3o-de-moedas-do-Logix
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida** Como corrigir a mensagem, Registro Inválido, A cotação da moeda informada não foi alterada ao integrar cotação de moedas do Logix (CURRENCYQUOTATION)?  
  
**Ambiente** Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões.  
  
**Solução**Para que a mensagem não seja apresentada, não deve ser enviada na integração cotação de moedas com valor 0,00, conforme exemplo abaixo, deve ser enviada na integração a cotação somente dos dias que há cadastro da cotação.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10792118879127)

**Saiba mais:**[Integração do Easy Export Control via Mensagem Única (SIGAEEC)](https://tdn.totvs.com/pages/releaseview.action?pageId=562473799) [Integração Backoffice Logix Trade Easy Exportação](https://tdn.totvs.com/pages/releaseview.action?pageId=201750338)
