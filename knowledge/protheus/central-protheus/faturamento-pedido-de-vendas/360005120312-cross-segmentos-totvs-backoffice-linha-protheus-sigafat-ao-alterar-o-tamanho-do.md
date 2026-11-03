---
article_id: 360005120312
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 5a05acab6e11d3db8600d09c21293ca423586b52a3911dff0fadc0c0e5677a10
fetched_at: '2026-06-28T22:38:38.343088+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: ' Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ao alterar
  o tamanho do campo C6_PEDCLI no configurador, o pedido de vendas não aceita a quantidade
  de caracteres configurada'
type: support-article
updated_at: '2023-01-18T14:23:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005120312--Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ao-alterar-o-tamanho-do-campo-C6-PEDCLI-no-configurador-o-pedido-de-vendas-n%C3%A3o-aceita-a-quantidade-de-caracteres-configurada
---

**Dúvida**

Ao alterar o tamanho do campo **C6\_PEDCLI** no configurador, o pedido de vendas não aceita a quantidade de caracteres configurada, como fazer o campo aceitar?  
  
**Ambiente**

 Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento) - A partir da versão 11.80

**Solução**Por não existir padrão para o número de dígitos do código do pedido, algumas empresas tem necessidade de alteração da quantidade de caracteres do campo **C6\_PEDCLI** (Ped Cliente).

 Porém alterando o mesmo via configurador, que no padrão possui Tamanho = 9, o pedido de vendas não aceita a alteração configurada.

O problema ocorre porque para que o mesmo consiga informar a quantidade correta no campo, deve-se configurar igualmente o campo CK\_PEDCLI, assim:

* **C6\_PEDCLI** == **CK\_PEDCLI** (igual o tamanho do campo **C6\_PEDCLI)**

Os dois são campos correspondentes.
