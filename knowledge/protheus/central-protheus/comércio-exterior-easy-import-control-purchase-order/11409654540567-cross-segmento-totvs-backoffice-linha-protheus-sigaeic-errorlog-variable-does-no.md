---
article_id: 11409654540567
category: Comércio Exterior - Easy Import Control - Purchase - Order
content_hash: 301451fe60f3c9dbc097917fa12f778b334136fa37b7ba3e4b7d3ca304fcdf7b
fetched_at: '2026-06-28T22:39:41.153309+00:00'
product: protheus
section_id: 1500001538481
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Error.log variable
  does not exist N on GRAVASC7A(MATA120A.PRW)
type: support-article
updated_at: '2023-01-04T12:42:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11409654540567-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Error-log-variable-does-not-exist-N-on-GRAVASC7A-MATA120A-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **02:00 min** **Dúvida**Ao incluir uma nova *Purchase Order*, a rotina está retornando o seguinte Error.log: **"variable does not exist N on GRAVASC7A(MATA120A.PRW)"**

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – a partir da versão 12.1.27

**Solução**

Para correção deste incidente em ambientes onde o fonte **MATA120A** possui data inferior a 23/11/2021, é necessário efetuar a atualização dos módulos **SIGACOM** e **SIGAEIC**, aplicando pacote acumulado de expedição continua de ambos os módulo, estes estão disponíveis no portal do cliente na área de download.

**Recomendação**Recomendamos manter o parâmetro **MV\_EXECCOM** ligado em seu ambiente para que as validações do **SIGACOM** sejam respeitadas durante a integração.

**Observação**Caso não possua o parâmetro **"MV\_EXECCOM"** em sua base, deverá proceder com atualização do  dicionário diferencial através da execução do **UPDDISTR** (Release incremental) disponível na Expedição Contínua do módulo **SIGACOM**.

**Saiba mais:**[Pacote Acumulado SIGACOM](https://tdn.totvs.com/pages/releaseview.action?pageId=522011099)  
[Pacote Acumulado SIGAEIC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047332793-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Pacote-Acumulado-Comex)  
[Central de atualizações](https://tdn.totvs.com/pages/viewpage.action?pageId=531011130%20%20)  
[UPDDISTR](https://tdn.totvs.com/display/public/framework/Upgrade+de+Release+do+Protheus+12)  
[Release incremental do Protheus 12](https://tdn.totvs.com/display/public/framework/Release+incremental+do+Protheus+12)
