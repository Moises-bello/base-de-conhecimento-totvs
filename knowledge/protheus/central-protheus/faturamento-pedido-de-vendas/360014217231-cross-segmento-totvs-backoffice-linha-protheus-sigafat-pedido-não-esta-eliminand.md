---
article_id: 360014217231
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: a4a59f75c9f00f5d0c6a8ec971746d606bbdc6b9ba79575e0fbea3ba7c6751bd
fetched_at: '2026-06-28T22:38:38.601916+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Pedido não esta
  eliminando resíduo, como resolver.
type: support-article
updated_at: '2023-07-12T13:01:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014217231-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Pedido-n%C3%A3o-esta-eliminando-res%C3%ADduo-como-resolver
---

**Ocorrência**

Pedido não esta eliminando resíduo, como resolver?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento - A partir da versão 11.80  
  
**Causa**

Ao acionar a Eliminação de Resíduo **MATA500**, se não é processada a eliminação, indica que algum fator deste Pedido não atende às premissas.  
  
**Solução**

Verifique se:

* O Pedido está em aberto sem liberação (credito/estoque/regra) pendente? Se o Pedido não será entregue por completo recomenda-se excluir o Pedido;
* O pedido esta parcialmente faturado? Se houver dúvida, verifique no campo **D2\_PEDIDO** se é localizado algum registro em Nota já emitida para esse Pedido;
* O Pedido tem relação com operação para Controle de Poder de Terceiro (TES preenchido com **F4\_PODER3** igual a Remessa ou Devolução / Campo **C6\_NFORI** preenchido com uma Nota que controla Poder de Terceiro). É necessário que não;
* O Pedido já foi submetido à Liberação (conteúdo no campo **C6\_QTDEMP**). É necessário que não;
* Os parâmetros de entrada da Rotina estão corretamente preenchidos;
* O campo **C6\_ENTREG** (Data de entrega) do item está preenchido. É necessário que sim.
* Há conteúdo no campo **C5\_ORIGEM**? É necessário que não. Este campo deve estar em branco para que ocorra a eliminação.
* O campo **C6\_BLQ** está com conteúdo igual a **"R"** ou **"S"**? É necessário que não, este campo deve estar com conteúdo **igual a** **"N"** ou **em branco** para que ocorra a eliminação.

**Importante**: em caso onde haja não permissão de usuário para  utilização da rotina de reíduo, conforme a imagem abaixo, valide as seguinte considerações:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408426132887/mceclip0.png)

* **Controle de privilégios de usuários**: se a função estiver não permitida, e o privilégio vinculado ao usuário, o mesmo não poderá acessar a função na rotina em questão, mais detalhes podem ser acessado em **: [Configurar Privilégio para controlar acesso a rotinas](https://tdn.totvs.com/x/1RMtE);**
* Ponto de entrada: verifique se o ponto de entrada **[MT410ACE](https://tdn.totvs.com/x/WoVn)** está habilitado para controle de acesso de usuário, se for o caso desabilite no catálogo de personalizações do configurador, reinicie o smartclient e valide a função de eliminação de resíduo no pedido novamente;

Mais detalhes de eliminação de resíduo, acesse: **[Eliminar Resíduo de Pedido de Vendas](https://tdn.totvs.com/x/t8IGEQ)**
