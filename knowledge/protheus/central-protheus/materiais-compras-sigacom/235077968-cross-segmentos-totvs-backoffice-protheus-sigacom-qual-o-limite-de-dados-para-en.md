---
article_id: 235077968
category: Materiais - Compras (SIGACOM)
content_hash: d86f26ecad6e0186e326e47c009ec03ee2c51f434f160ec2ebacd8e06dbf9cf9
fetched_at: '2026-06-28T22:41:24.317766+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Qual o limite de dados
  para envio através de um XML pela rotina Pedido de Compras (MATA120) na integração
  Pedido X Neogrid ?
type: support-article
updated_at: '2022-05-18T21:19:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/235077968-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Qual-o-limite-de-dados-para-envio-atrav%C3%A9s-de-um-XML-pela-rotina-Pedido-de-Compras-MATA120-na-integra%C3%A7%C3%A3o-Pedido-X-Neogrid
---

**Dúvida**

Qual o limite de dados para envio através de um XML pela rotina Pedido de Compras (MATA120) na integração Pedido X Neogrid ?  
  
**Ambiente**

Protheus – Compras – A partir da 12.1.17  
  
**Solução**

O sistema **Protheus** possui um limite de variável, onde ao montar uma string **XML**, o mesmo não pode ultrapassar 1 MB.

Para maiores detalhes, consulte a pagina: **[Seção [general], chave MaxStringSize](http://tdn.totvs.com/x/oQCeCQ)**

Após a comunicação com o sistema **Neogrid**, o sistema **Protheus** irá gravar uma cópia do **XML** enviado na tabela **CKOCOL** em um campo do tipo **MEMO**, os campos com este tipo possuem um limite de 1.000.000 bytes, conforme página: **[TOPMemoMega](http://tdn.totvs.com/x/j4pc)**

Para evitar que o sistema **Protheus** bloqueie a exportação do pedido de compra, indica-se que haja um limite de itens no pedido de compra de maneira a não ultrapassar a quantidade de bytes descrita acima. Para uma maior segurança, é indicado um máximo de 300 itens por pedido de compra, lembrando que esse valor é indicado para as empresas que utilizam o sistema **Protheus** com o tamanho padrão de seus campos, caso a empresa opte por aumentar qualquer campo que envolva este processo, este numero de itens pode cair, sendo necessário a quebra com menos itens dentro de um mesmo pedido de compra.

Lembramos também que essa dica somente se aplica as empresas que utilizam a integração **Pedido de Compras X Neogrid**.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
