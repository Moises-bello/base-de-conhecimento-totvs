---
article_id: 4409840603159
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: e445d0a9fa9fa045b15fb4a6c5ce93aeb5aa0c0d67eab32f5b69268658ed9efc
fetched_at: '2026-06-28T22:39:50.036630+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Configuração da
  TES no processo de importação
type: support-article
updated_at: '2021-10-01T19:59:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409840603159-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Configura%C3%A7%C3%A3o-da-TES-no-processo-de-importa%C3%A7%C3%A3o
---

**Dúvida**Na integração do SIGAEIC com o SIGACOM, qual seria a configuração da TES para classificar a nota fiscal de importação?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  –*Easy Import Control*– Todas versões  
  
**Solução**Quando integrado com o módulo de compras, através do parâmetro **MV\_EASY**, será gerada a pré-nota via rotina automática. Esta nota fiscal deve ser classificada no módulo de compras, utilizando uma TES que não altera (calcula) os impostos apurados pelo módulo de importação e informados na integração. Na rotina de cadastro de Tes (**MATA080**) ao incluir o TES além de não recalcular os impostos, é imprescindível que o campo “Agrega Valor”  (**F4\_AGREG**) ,na aba “Impostos” do cadastro da TES, seja preenchido com o conteúdo **B (ICMS + MER )**.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409863014807/mceclip0.png)   
Com esta informação, ao classificar o documento de entrada, os valores do ICMS e da mercadoria   
serão agregados ao total do documento não calculando nenhum imposto, mantendo os cálculos realizados pelo SIGAEIC.  
  
**Saiba mais**  
[Campo Agrega Valor - F4\_AGREG](https://tdn.totvs.com/display/public/PROT/Campo+Agrega+Valor++F4_AGREG+--+11263)
