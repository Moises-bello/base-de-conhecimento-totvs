---
article_id: 360039146573
category: Comércio Exterior - Easy Export Control - Pedido - Export
content_hash: 02c76325c0b9df9dcdc149ac207a3ecb677fe4346bae49aef56b9f34ee15f0a4
fetched_at: '2026-06-28T22:36:59.042079+00:00'
product: protheus
section_id: 1500001538181
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Peso bruto total
  parâmetro MV_EEC0052
type: support-article
updated_at: '2022-06-29T14:28:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039146573-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Peso-bruto-total-par%C3%A2metro-MV-EEC0052
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Como é calculado o peso bruto total?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões  
  
**Solução**Segue o boletim técnico referente o cálculo do peso bruto: [MTRADE-682 DT Calculo do peso bruto na Nota Fiscal de Saída com lote](http://tdn.totvs.com/pages/releaseview.action?pageId=274855235)  
  
Este é calculado de acordo com a configuração do parâmetro MV\_EEC0052:  
Parâmetro - Tipo Numérico  
MV\_EEC0052 == **1** Peso Bruto = Peso Liq. + Peso da Embalagem  
MV\_EEC0052 == **2** Pesa Bruto = (Peso Liq. \*(Peso Embalagem / Qtd Total)) + Qtd.  
MV\_EEC0052 == **3** Peso Bruto = (Peso Liq. \*(Peso Embalagem / Saldo inicial do embarque))  Qtd.  
  
**Saiba mais**  
[Calculo do peso bruto na Nota Fiscal de Saída com lote](https://tdn.totvs.com/pages/releaseview.action?pageId=274855235)
