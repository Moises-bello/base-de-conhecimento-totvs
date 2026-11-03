---
article_id: 360026677233
category: eSocial - Cadastros
content_hash: b2228f767463b03807deb95a4f6f7dddbaa198e38242bb97fc36d22bf482cd48
fetched_at: '2026-06-28T22:47:14.509192+00:00'
product: rm
section_id: 1500000834341
source: central-rm
title: RH - RM - FOP - eSocial - Histórico de rateio por tomador de serviços
type: support-article
updated_at: '2024-06-14T15:14:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026677233-RH-RM-FOP-eSocial-Hist%C3%B3rico-de-rateio-por-tomador-de-servi%C3%A7os
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:01:00 min****Dúvida**Para que serve o histórico de rateio por tomador?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial  - A partir da versão 12.1.22  
  
**Solução**Para quem utiliza o **tomadores de serviço** no TOTVS Folha de Pagamento, a geração do XML do **S-1200** e **S-2299** é baseado na **distribuição do SEFIP** realizada para cada funcionário. Assim, o sistema irá validar o tomador preenchido no rateio do funcionário e buscará a movimentação deste tomador na [distribuição do SEFIP](https://tdn.totvs.com/display/public/LRM/Distribuir+SEFIP), de acordo com o período de apuração, para popular o XML.

Para que seja possível realizar a correta **geração do S-1200 para meses anteriores** ao da competência atual, foi criado o **histórico de rateio por tomador**. Com ele, o sistema irá armazenar o período em que o funcionário ficou alocado em determinado tomador, sendo possível assim validar a distribuição realizada em competências anteriores ou realizar novas distribuições.  
  
**Importante**  
Ressaltamos que o histórico de rateio **não elimina a necessidade de realizar a distribuição do SEFIP**. Tal procedimento deverá ser executado mensalmente para a movimentação atual ou de acordo com a necessidade para distribuição de meses anteriores.  
  
**Saiba mais**  
Acesse [Rateio por Tomador de Serviço](http://tdn.totvs.com/pages/releaseview.action?pageId=453280016) para validar todos os procedimentos necessários para habilitar o histórico de rateio por tomador, executar o conversor de rateio, entre outras informações relevantes.
