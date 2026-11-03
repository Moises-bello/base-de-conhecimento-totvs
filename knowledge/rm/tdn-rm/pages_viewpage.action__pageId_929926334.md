---
content_hash: 7b08122dc847b82a4d1647e576a3a0a15579cc83de6d9f31f081eb0e8afb5c65
fetched_at: '2026-06-29T00:12:08.207775+00:00'
page_id: '929926334'
product: rm
source: tdn-rm
title: Evento de exclusão S-3500 - Leiaute 1.3 - NT 03/2025
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=929926334
version: 5
---

Evento S-2500 - Leiaute 1.2NovidadesO que está diferente?

* **Alteração na Chave de Exclusão do Evento S-3500**

Antes da criação do campo **{ideSeqTrab}**, a exclusão de um evento S-2500 pelo S-3500 era realizada utilizando como   
identificadores a Coligada **{codColigada}**, Branch **{codBranch}**, Número do Processo **{nrProcTrab}** e o CPF **{cpfTrab}**.

Com a introdução do campo **{ideSeqTrab}**, a chave de exclusão passou a considerar também esse identificador, tornando-se:

Coligada **{codColigada}** + Branch **{codBranch}** + Número do Processo **{nrProcTrab}** + CPF **{cpfTrab}** + Sequência **{ideSeqTrab}**

Para garantir que a exclusão continue funcionando corretamente mesmo quando o campo **{ideSeqTrab}** não estiver preenchido, o sistema atribui o valor -1 a esse campo. Dessa forma, a chave de exclusão é sempre composta corretamente, evitando inconsistências na remoção dos registros.

**Com sequência:**

Neste caso, a chave de exclusão é composta da seguinte forma:

**"{codColigada};;{nrProcTrab};{cpfTrab};1"**  
O número 1 representa o valor atribuído ao campo **"{ideSeqTrab}"** que foi preenchido no momento do cadastro do evento S-2500.

**Sem sequência:**

Quando o campo **"{ideSeqTrab}"** não foi informado, a chave de exclusão é montada assim:

**"{codColigada};;{nrProcTrab};{cpfTrab};-1"**    
 O valor -1 é utilizado para representar a ausência de um identificador sequencial, garantindo que a exclusão seja realizada corretamente.
