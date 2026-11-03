---
article_id: 360034991133
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: 83f12997bbb6437ac26c06437647480aa246664f9e6f4e622fe22d79c945e3a4
fetched_at: '2026-06-28T22:39:49.882651+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus  - SIGAEIC - Preenchimento
  da natureza financeira ao incluir despesa no desembaraço
type: support-article
updated_at: '2021-09-24T13:23:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034991133-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Preenchimento-da-natureza-financeira-ao-incluir-despesa-no-desembara%C3%A7o
---

**Dúvida**O campo natureza (**E2\_NATUREZ**) é preenchido automaticamente ao realizar a inclusão de despesa no Desembaraço (EICDI502), onde verifica tal informação para preenchimento?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões  
  
**Solução**

 A configuração da natureza é realizada na rotina de Desembaraço (EICDI502), para o preenchimento automático do campo E2\_NATUREZ ao incluir uma despesa.  
1 - Acesse pelo módulo 17- *Easy Import,* em Atualizações\Desembaraço\Manutenção e selecione F11 .

2 - Nos Parâmetros informe a Natureza do Título e selecione OK.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044701274/mceclip2.png)

**Observação**Caso a natureza do título esteja informada no **cadastro do fornecedor** campo Natureza (**A2\_NATUREZ**), essa será gravada no campo **E2\_NATUREZ** . Não tendo a natureza informada no cadastro do fornecedor campo **A2\_NATUREZ**, será verificado a natureza informada no **F11** do **desembaraço**, para a geração do título. Sem o preenchimento da natureza em nenhum cadastro não será possível gravação do título no SIGAFIN, pois o campo **E2\_NATUREZ** é obrigatório.
