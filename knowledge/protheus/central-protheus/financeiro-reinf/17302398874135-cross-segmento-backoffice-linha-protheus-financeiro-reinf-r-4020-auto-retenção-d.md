---
article_id: 17302398874135
category: Financeiro - Reinf
content_hash: ccf35e742bdafd99939b1f36f00d18fdd4cce6062bb0ae12175d502ac21966f6
fetched_at: '2026-06-28T22:37:51.672687+00:00'
product: protheus
section_id: 17886892336407
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - Financeiro REINF - R- 4020, Auto
  retenção do IR e natureza de rendimento 12001
type: support-article
updated_at: '2026-03-25T12:55:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17302398874135-Cross-Segmento-Backoffice-Linha-Protheus-Financeiro-REINF-R-4020-Auto-reten%C3%A7%C3%A3o-do-IR-e-natureza-de-rendimento-12001
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17302421358615) Tempo aproximado para leitura: **05:00 min**  
  
**Dúvida**

O prestador de serviço que realiza a auto retenção do Imposto de Renda, deve realizar o envio do Registro R-4080 da EFD-Reinf, informando no campo "ideRend" o código da natureza de rendimento de acordo com o grupo 20 da tabela 1 que descreve os serviços prestados bem como os códigos de natureza de rendimentos no qual houve a auto retenção.

![](https://tdn.totvs.com.br/download/attachments/754225677/image2023-4-17_18-18-6.png?version=1&modificationDate=1681766286853&api=v2)

![](https://tdn.totvs.com.br/download/attachments/754225677/image2023-4-17_18-27-35.png?version=1&modificationDate=1681766855897&api=v2)

Já o tomador de serviço, contratante do serviço, deve enviar as informações no EFD-Reinf no registro R-4020, utilizando um dos códigos de natureza de rendimento, do grupo 20 da Tabela 01.

Devido a obrigatoriedade de prestação de informação de rendimentos sem retenção de imposto de renda, deve ser informado pelo tomador no registro R-4020, apenas o campo “valor bruto” do serviço, devendo ser deixado em branco o "campo vlrIR" relacionado ao valor do Imposto de Renda Retido na Fonte.

Como enviar os rendimentos sem retenção de tributos?

**Ambiente**  
Cross Segmento - TOTVS Backoffice Linha Protheus - Financeiro- Todas as versões

**Solução**

Temos casos previstos na legislação em que há a obrigatoriedade da prestação de informação de rendimentos sem **retenção de imposto de renda** na **EFD-REINF bloco 40**. Deve ser enviada a informação do valor do pagamento e sua respectiva classificação de **Natureza de Rendimento**.

Por exemplo, caso haja pagamento de **lucros e dividendos**, o contribuinte deverá informar a **natureza de** **rendimento** “**12001**” no **título a pagar** ou **documento de entrada**.

Como o fato gerador para esses casos é o pagamento, o **título a pagar** deve estar baixado e a data de envio para o **TAF** será a **data da baixa** (será gerado os dados no **layout T158** do **TAF**).

**Legislação:** [EFD-Reinf - R-4080 - Auto Retenção](https://tdn.totvs.com.br/pages/releaseview.action?pageId=754225677)
