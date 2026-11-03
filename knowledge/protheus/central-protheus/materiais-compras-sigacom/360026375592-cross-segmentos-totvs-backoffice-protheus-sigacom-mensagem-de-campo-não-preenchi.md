---
article_id: 360026375592
category: Materiais - Compras (SIGACOM)
content_hash: 5c35837ef23263fd0bb82e682372e6fc275e6d728bc43e7e6af593b1c99a8981
fetched_at: '2026-06-28T22:41:09.038761+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Mensagem de Campo Não
  Preenchido no Lançamento de Documento de Entrada x Ativo Fixo
type: support-article
updated_at: '2022-05-12T21:28:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026375592-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Mensagem-de-Campo-N%C3%A3o-Preenchido-no-Lan%C3%A7amento-de-Documento-de-Entrada-x-Ativo-Fixo
---

**Ocorrência**

Mensagem de Campo Não Preenchido no Lançamento de Documento de Entrada x Ativo Fixo

**Ambiente**Protheus – Compras  A partir da versão 12  
  
**Causa**

Ao incluir documento de entrada com TES que movimenta ativo fixo, o sistema exibe mensagem dizendo: "O campo C Custo Bem (N3\_CUSTBEM) não foi preenchido."

OBS: A mensagem acima é apenas um exemplo, mas sistema poderá apresentar ocorrência nas tabelas SN1 / SN3.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025905631/mceclip0.png)

Esse incidente ocorre, pois campos estão Marcados como obrigatório via configurador do sistema, na versão P11 do sistema, não havia este tipo de validação, e por consequência não apresentada help/mensagem ao incluir NF com integração com Ativo Fixo.

Ao entrar com NF pela rotina de Documento de Entrada, o que irá validar se terá integração com o módulo de Ativo é a configuração do TES que está utilizando para o Produto em questão, ou seja, se o campo (F4\_ATUATF=S - Atualiza Ativo Fixo.

**Solução**Na integração com o módulo de Ativo Fixo, o módulo de Compras não possui as informações para preenchimento de todos os campos do Ativo. Quando um dos campos que não são preenchidos pelo Compras for obrigatório, será exibida a mensagem de alerta.  
  
Na versão 11, não existia esta validação, causando inconsistência no Ativo Fixo, pois vários campos obrigatórios ficavam em branco. Por este motivo, sugerimos desmarcar a obrigatoriedade do campo N3\_XXXX no dicionário de dados para correta integração.

**Saiba mais:**

[Integração Documento de Entrada x Ativo Fixo](http://tdn.totvs.com/pages/releaseview.action?pageId=334335454)
