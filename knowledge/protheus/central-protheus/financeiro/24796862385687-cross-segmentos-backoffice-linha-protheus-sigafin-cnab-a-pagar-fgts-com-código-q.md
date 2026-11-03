---
article_id: 24796862385687
category: Financeiro
content_hash: 80c1beda99942e176ddf1703b79139fad2e4135bf970e81f01a81fdaf96430fd
fetched_at: '2026-06-28T22:38:01.236241+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CNAB a Pagar - FGTS
  com Código QrCode - PIX
type: support-article
updated_at: '2024-07-10T20:57:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24796862385687-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CNAB-a-Pagar-FGTS-com-C%C3%B3digo-QrCode-PIX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24796862363927) Tempo aproximado para leitura: **02:00 min** **Dúvida**Qual o procedimento para lançar esta Guia FGTS com modalidade Pix Qrcode?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - Todas as versões  
  
**Solução**Caso o cliente queira enviar o título do **FGTS Digital** para o banco via **CNAB** o próprio cliente terá que realizar a configuração no layout conforme o banco que utiliza.  
  
Lembrando que quando o cliente não possui os módulos de folha, a geração deste título é manual. Quando há o módulo de folha, o título é gerado automaticamente, porém sem o código de barras e sem a chave pix. Segue documentação completa. https://tdn.totvs.com/pages/viewpage.action?pageId=569478747   
  
As rotinas **FINA240** e **FINA241** foram adequadas para atender a demanda. No mais, somente deve estar atualizado junto ao portal, e realizar o processo via **PIX**.   
  
A configuração e implantação do **CNAB PIX**, possuem particularidades de acordo com seu Banco e Contrato.   
  
Para o banco ITAU no contas a pagar, a **TOTVS** disponibiliza um layout via **CNAB CLOUD** que poderá utilizar como exemplo Geração de layout via **CNAB Cloud**: <https://www.youtube.com/watch?v=vW-DHUHom4o&t=10s>

Documentação **CNAB CLOUD**: [CNAB Cloud](https://tdn.totvs.com/display/public/PROT/CNAB+Cloud+-+Financeiro)

**Saiba Mais**

[PIX](https://tdn.totvs.com/pages/releaseview.action?pageId=569478747)
