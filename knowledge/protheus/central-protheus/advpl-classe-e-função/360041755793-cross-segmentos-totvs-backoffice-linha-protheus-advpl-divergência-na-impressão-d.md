---
article_id: 360041755793
category: ADVPL - Classe e Função
content_hash: 9f162109bac96da15f4a764b922e1b1408af4317c194cfa843220983ac091993
fetched_at: '2026-06-28T22:40:18.289146+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Divergência na
  impressão do QRCODE
type: support-article
updated_at: '2022-01-06T18:51:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041755793-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Diverg%C3%AAncia-na-impress%C3%A3o-do-QRCODE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Ocorrência**Ao utilizar a classe **FWQRCode**() ou método **QrCode(FwMsPrinter)** no **Smartclient x86** na 12.1.25, a imagem gerada está incorreta.

**Smartclient x86**

![Screenshot_15.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054990894/Screenshot_15.png)

**Smartclient x64**

![Screenshot_16.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055862273/Screenshot_16.png)  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.125  
  
**Causa**Esse incidente ocorre, pois existia uma limitação de  tamanho para geração do **QRCODE** nas versões anteriores. O binário mais recente contempla também a versão mais recente do **printer.exe,** onde foi implementado uma melhoria em relação ao **QRCODE**.

**Observação**Nas versões anteriores , não era possível a criação livre do **QRCODE**, onde existia um tamanho minimo aceitável para geração. Porém foi sugerido por alguns clientes a melhoria dessa funcionalidade, onde fosse possível o cliente criar o **QRCODE** conforme a sua necessidade, ou seja, de forma livre(sem limitação). Essa melhoria foi disponibilizado para as releases mais atuais na versão 1.7.2 do **printer.exe**(*executável responsável pelas impressões*).  
 **Importante:**Essa melhoria visa atender uma demanda solicitada por diversos clientes, porém informamos que é de inteira responsabilidade do desenvolvedor a leitura do **QRCODE**, pois ao gerar uma imagem muito pequena, a mesma pode ficar corrompida e acaba comprometendo a sua leitura

**Solução**Para corrigir esse problema, baixe a versão igual ou superior a 1.7.2 do **Printer.exe** no portal de download TOTVS e redefina o tamanho da imagem gerada dentro de suas customizações.  
  
**Saiba mais**  
[**Implementação - Redimensionamento de QRCode e Datamatrix para dimensões inferiores ao natural.**](https://tdn.totvs.com/pages/viewpage.action?pageId=519198145)
