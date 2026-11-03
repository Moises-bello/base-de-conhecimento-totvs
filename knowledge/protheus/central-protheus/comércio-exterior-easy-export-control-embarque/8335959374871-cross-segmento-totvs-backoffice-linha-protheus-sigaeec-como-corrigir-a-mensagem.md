---
article_id: 8335959374871
category: Comércio Exterior - Easy Export Control - Embarque
content_hash: 17b54abd95ccda061cdca5fdd1c89bde0571af729e71b80c85a1ebbe5009923b
fetched_at: '2026-06-28T22:36:56.546935+00:00'
product: protheus
section_id: 1500001549322
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Como corrigir
  a mensagem: AVG0000637 ''Quantidade informada não é multipla pela quantidade na
  embalagem?'
type: support-article
updated_at: '2022-08-22T11:46:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8335959374871-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Como-corrigir-a-mensagem-AVG0000637-Quantidade-informada-n%C3%A3o-%C3%A9-multipla-pela-quantidade-na-embalagem
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como corrigir a mensagem: AVG0000637 'Quantidade informada não é multipla pela quantidade na embalagem?

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8335953815063/mceclip0.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Easy Export Control –  Todas versões.  
  
**Solução**

Deve ser verificado o cadastro da embalagem vinculada ao produto. O cálculo é feito sobre a quantidade do item embarque / pela quantidade na embalagem   
  
Exemplo: EE8\_QTDEM1 := M->EE8\_SLDINI/M->EE8\_QE  Quantidade de embalagem.  
  
[Embalagens - EECAT170](https://tdn.totvs.com/display/public/PROT/Embalagens+-+EECAT170#eecat170Embalagens-eecat170EmbalagensIncluir)  
  
[MTRADE-682 DT Calculo do peso bruto na Nota Fiscal de Saída com lote](https://tdn.totvs.com/pages/releaseview.action?pageId=274855235)
