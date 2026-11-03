---
content_hash: 657b99686edeaaa8e10208dd3270bd76627ef925911761766b13b2bae0111f6a
fetched_at: '2026-06-29T00:09:19.197261+00:00'
page_id: '421388819'
product: rm
source: tdn-rm
title: FIN - Débito Direto Autorizado (DDA)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388819
version: 12
---

É um projeto da FEBRABAN - Federação Brasileira de Bancos, que visa facilitar pagamentos por meio da disponibilização de compromissos eletrônicos.

No modelo tradicional, os Bancos cedentes emitem os títulos em papel e enviam-nos aos sacados. Com o DDA, os bancos passarão a gerar os títulos eletronicamente, remetendo-os ao sistema DDA.

Este, que é controlado pela CIP – Câmara Interbancária de Pagamento - armazenará todos os títulos eletrônicos. Os bancos consultarão o DDA e apresentarão a seus clientes (sacados eletrônicos) todos os seus títulos (registrados em qualquer banco).

Dentre os principais benefícios elencados pela FEBRABAN, destacam-se a redução do uso de papel, já que deixa de existir a emissão de títulos físicos, e, ganho de eficiência para o mercado com a simplificação do processo de recebimento e pagamento.

O projeto entra em vigor a partir de 19 de outubro de 2009.

Para mais informações consulte a cartilha DDA disponibilizada pela FEBRABAN:  [www.febraban.org.br](http://www.febraban.org.br)

Considerações sobre o DDA

* O DDA não envolve legislação; trata-se de uma modernização do sistema de pagamento brasileiro.
* O DDA não é obrigatório. As pessoas físicas e/ou jurídicas que aderirem a ele devem se tornar "sacado eletrônico" por meio de seus bancos de relacionamento.
* O DDA abrange apenas cobrança registrada.
* O sacado eletrônico poderá trabalhar com diversos bancos. Neste caso, as informações disponibilizadas serão as mesmas (com o DDA, todos os bancos têm acesso aos títulos registrados em todos os bancos).

O objetivo do módulo de DDA no sistema é o preenchimento das informações de Código de Barras e IPTE dos lançamentos a Pagar de acordo com as informações fornecidas pelo Banco. Após esse preenchimento os lançamentos estão preparados para serem enviados na Remessa de Pagamento Eletrônico.

Esta funcionalidade é realizada da seguinte forma:

**Recebimento do arquivo**

O banco irá disponibilizar diariamente além do arquivo de retorno de pagamento o arquivo de varredura, contendo os títulos que estão disponíveis para pagamento na base de dados do DDA.

Veja Também
