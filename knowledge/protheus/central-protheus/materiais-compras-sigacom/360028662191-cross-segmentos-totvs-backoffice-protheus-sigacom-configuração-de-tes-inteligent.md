---
article_id: 360028662191
category: Materiais - Compras (SIGACOM)
content_hash: 4abe1e40170ac3a03aef4022d19e9d3b2167776cb51a51c485802ac86d2b2922
fetched_at: '2026-06-28T22:41:16.140077+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Configuração de TES
  Inteligente para utilização no TOTVS Colaboração
type: support-article
updated_at: '2024-08-01T17:33:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028662191-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Configura%C3%A7%C3%A3o-de-TES-Inteligente-para-utiliza%C3%A7%C3%A3o-no-TOTVS-Colabora%C3%A7%C3%A3o
---

**Dúvida**Existe configuração de TES Inteligente para utilização no TOTVS Colaboração  
  
**Ambiente**Protheus – Totvs Colaboração – A partir da versão 12  
  
**Solução**

A TES inteligente pode ser utilizada somente quando o documento for diferente de CTO

C: por ser complemento de preço ou quantidade;  
T: é complemento de transporte;  
O: a equipe de produto informou que é antigo (por favor, desconsiderar)

**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4474978872983)**

**Acesse o módulo do Compras -> Atualizações -> Cadastros  -> Entrada/saída inteligente:**

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4474849529879)**

Realizar o cadastro de sua TES inteligente preenchendo o tipo de operação:

**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4474981816983)**

Poderá realizar a amarração da TES:

**![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4474982660887)**

**OBS:** Poderá utilizar a rotina de cadastro de TES Inteligente + Relação de tipo de Operação x CFOP para amarrar a TES ao cadastro a partir do momento que gerar o documento, antes de gerar o documento a TES não será preenchida. Para isso a TES não deverá gerar duplicata, caso gere será necessário a utilização do ponto de entrada COLF1D1 para informar a condição de pagamento.

Documentação: [TC02012 - COLF1D1 - Ponto que permite adicionar campos customizados na geração do documento](https://tdn.totvs.com/pages/viewpage.action?pageId=233760370)

**Acesse o módulo do Compras -> Miscelanea -> TOTVS Colaboração -> Relação Tp Vs Cfop (MATA002):**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4474752720279)**

Neste processo poderá amarrar seu tipo de operação da TES Inteligente ao CFOP desejado:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4475005080343)

Caso a rotina MATA002 não conste no seu menu, segue abaixo exemplo padrão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25341835943319)

***Saiba Mais :***

[TC02002 - COMCOLF4 - Novo código da TES na geração do documento via monitor do Totvs Colaboração / Importador XML](https://tdn.totvs.com/x/QwUOAw)

[TC07010 - Totvs Colaboração - Regras TES / Condição de pagamento](https://tdn.totvs.com/x/lumVI)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Importador XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026658994-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML)

[CENTRALIZADORA COMPRAS](https://tdn.totvs.com/x/rivQHw)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
