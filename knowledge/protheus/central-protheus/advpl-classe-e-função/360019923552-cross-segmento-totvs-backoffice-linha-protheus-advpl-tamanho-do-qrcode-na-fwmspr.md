---
article_id: 360019923552
category: ADVPL - Classe e Função
content_hash: efaaa2a76e0e560c6a8028ea48ff8b221fca683f6beb4a6a10e2290d15388574
fetched_at: '2026-06-28T22:40:18.066779+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Tamanho do QRcode
  na FWMSPRINTER
type: support-article
updated_at: '2022-09-29T14:39:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019923552-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Tamanho-do-QRcode-na-FWMSPRINTER
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:02:00 min****Dúvida**Usando a classe FWMSPrinter com QrCode, dependendo do tamanho da string o espaço utilizado pelo "desenho" aumenta. Eu terei um espaço pré-determinado, como ajustar para respeitar este espaço?

Segue o comando:   
oPrint:QrCode(0150,0005,"Teste de codificacao QR Code", 100)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**O método QRcode conforme o conteúdo do Texto ele redimensiona o tamanho consequentemente mesmo definindo o parâmetro que trata o tamanho.  
Para definir um tamanho fixo sugiro que utilize a classe **[FwQrCode](http://tdn.totvs.com/display/PROT/FwQrCode)**
