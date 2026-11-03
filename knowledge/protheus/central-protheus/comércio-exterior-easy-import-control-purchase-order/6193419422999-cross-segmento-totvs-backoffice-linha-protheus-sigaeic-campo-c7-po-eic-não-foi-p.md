---
article_id: 6193419422999
category: Comércio Exterior - Easy Import Control - Purchase - Order
content_hash: 4baade292d6d5f0bd6e5bed28cbfb1baeb0312911a2b2fabc74aae58be5fa1fe
fetched_at: '2026-06-28T22:39:41.079819+00:00'
product: protheus
section_id: 1500001538481
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Campo C7_PO_EIC
  não foi preenchido após a gravação da PO e integração com o SIGACOM
type: support-article
updated_at: '2024-11-21T10:57:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6193419422999-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Campo-C7-PO-EIC-n%C3%A3o-foi-preenchido-ap%C3%B3s-a-grava%C3%A7%C3%A3o-da-PO-e-integra%C3%A7%C3%A3o-com-o-SIGACOM
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **02:00 min****Dúvida**Após a gravação da **PO** e integração do **SIGAEIC** com o **SIGACOM** o campo "**C7\_PO\_EIC**" não foi preenchido dentro da Tabela "**SC7**". Como corrigir?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – a partir da versão 12.1.27  
  
**Solução**Para correção deste incidente em ambientes onde o fonte **MATA120A** possuir data inferior a **23/11/2021**, é necessário efetuar a atualização dos módulos **SIGACOM** e **SIGAEIC**, aplicando o pacote acumulado de expedição continua de ambos os módulos. Estes estão disponíveis no portal do cliente na área de download.

**Recomendação**Recomendamos que mantenha o parâmetro **MV\_EXECCOM** ligado em seu ambiente para que as validações do **SIGACOM** sejam respeitadas durante a integração.

**Observação**Caso não possua o parâmetro **"MV\_EXECCOM"** em sua base, deverá proceder com atualização do  dicionário diferencial através da execução do **UPDDISTR**(Release incremental) disponível na Expedição Contínua do módulo **SIGACOM**.  
  
  
**Saiba mais:**[Pacote Acumulado SIGACOM](https://tdn.totvs.com/pages/releaseview.action?pageId=522011099)  
[Pacote Acumulado SIGAEIC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047332793-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Pacote-Acumulado-Comex)  
[Central de atualizações](https://tdn.totvs.com/pages/viewpage.action?pageId=531011130)  
[UPDDISTR](https://tdn.totvs.com/display/public/framework/Upgrade+de+Release+do+Protheus+12)  
[Release incremental do Protheus 12](https://tdn.totvs.com/display/public/framework/Release+incremental+do+Protheus+12)
