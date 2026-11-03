---
article_id: 360037249374
category: Contabilidade Gerencial - Escrituração-Contábil-Lalur
content_hash: 09e0af86f0f1423372e0bce2ca9152e993551a9d5b35a8e4623b0c3e6f43b79c
fetched_at: '2026-06-28T22:40:40.310037+00:00'
product: protheus
section_id: 1500001548842
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - TAF - TAFA436 - Controle de Deduções/Compensação
  parte B do LALUR
type: support-article
updated_at: '2024-11-18T17:31:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037249374-Cross-Segmento-Backoffice-Linha-Protheus-TAF-TAFA436-Controle-de-Dedu%C3%A7%C3%B5es-Compensa%C3%A7%C3%A3o-parte-B-do-LALUR
---

**Dúvida**Controle de Deduções/Compensação parte B do LALUR  
  
**Ambiente**

Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.  
  
**Solução**

Este controle é feito apenas através da rotina Conta da Parte B (TAFA436)

* **CONTROLE NO LALUR**O excesso do incentivo fiscal do PAT não aproveitado em um período poderá ser transferido para dedução do imposto devido nos dois anos-calendário subsequentes aquele em que ocorreram os gastos. As empresas deverão controlar a parcela excedente na parte ”B“ do Lalur.

Exemplo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048790634)

* **LIMITE DA DEDUÇÃO DO IRPJ**  
  A dedução do incentivo do PAT está limitada a 4% do imposto devido em cada período de apuração à alíquota de 15%, ou seja, sem a inclusão do adicional, podendo o eventual excesso ser transferido para dedução nos 2 anos-calendário subsequentes, sempre respeitado esse limite.  
  Observe-se que a dedução do incentivo do PAT, conjuntamente com o incentivo relativo aos Programas de Desenvolvimento Tecnológico Industrial (PDTI) e Programas de Desenvolvimento Tecnológico Agropecuário (PDTA), fica limitada a 4% do IRPJ devido à alíquota de 15%.

**1°** Realize o cadastro da conta da parte B na rotina TAFA436

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049703613)

**2°** No Evento Tributário (rotina TAFA433), o cliente pode escolher entre as seguintes origens: 1 - Conta Contábil, 2 - Lalur - Parte B, ou 3 - Evento Tributário.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25692920482327)  
  
**1 - Conta contábil:** O sistema executará a busca dos saldos na rotina TAFA331 - Lançamento contábil, da conta contábil que foi vinculada ao evento tributário.   
  
**2 - Lalur - Parte B:** Para que a simulação da apuração e a apuração considerem os lançamentos efetuados na parte B, é necessário realizar lançamentos manuais na aba "Lançamentos na Conta da Parte B" na rotina TAFA436 - Conta da Parte B.  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/25692920486551)**  
  
  
**3°** No cadastro do Evento Tributário (rotina TAFA433), informamos a conta da parte B, o percentual de dedução e o código limite para o código.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049710473)

**Saiba Mais**

Calculo PAT na Folha de pagamento (Módulo SIGAGPE ):

[RH - Linha Protheus - GPE - Como preencher e o que significa os campos do parâmetro 45 (versão 11) e S041 (versão 12)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024691512)  
  
Lalur:

[Cross Segmento - Backoffice Linha Protheus - Lalur - Cadastro, apuração e integração com o ecf](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018585831)

[Cadastro de dedução de tributo 15% PAT – Programa de alimentação do Trabalhador.](https://tdn.totvs.com.br/pages/releaseview.action?pageId=874196126)
