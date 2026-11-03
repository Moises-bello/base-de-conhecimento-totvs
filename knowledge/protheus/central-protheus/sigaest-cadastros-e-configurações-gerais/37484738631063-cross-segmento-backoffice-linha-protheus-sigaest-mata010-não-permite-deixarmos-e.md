---
article_id: 37484738631063
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 42251914c4816b6807d026975e1cbd4fc4656266ec4d696d42eefad2618f65ba
fetched_at: '2026-06-28T22:39:09.513894+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA010 - não permite
  deixarmos em branco os campos de B1_TIPCONV e B1_CONV?
type: support-article
updated_at: '2026-01-06T20:22:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37484738631063-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA010-n%C3%A3o-permite-deixarmos-em-branco-os-campos-de-B1-TIPCONV-e-B1-CONV
---

Durante a cópia de um produto no TOTVS Protheus, não é possível desconsiderar por padrão os campos B1\_TIPCONV e B1\_CONV, pois o método copia exatamente o produto, exceto campos de controle do sistema. Porém, o cliente pode usar o ponto de entrada MTA010NC para definir logicamente quais campos não devem ser copiados, embora alguns ainda sejam tratados pelo inicializador do dicionário.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37484717340055) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Durante a copia de um produto, eu gostaria de desconsiderar que venha os campos B1\_TIPCONV e B1\_CONV, é possivel?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
De forma padrão não.

O método de cópia consiste em efetuar uma cópia exata do produto, não copiando campos que são pertinentes ao controle do sistema, como por exemplo, o código do produto.

Esta funcionalidade é um recurso do modelo MVC em que o produto informa quais os campos que não devem ser copiados na funcionalidade MVC do framework.

Para estes casos específicos, o cliente pode utilizar o ponto de entrada [MTA010NC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003591241-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA010-Quais-s%C3%A3o-os-Pontos-de-Entrada-da-rotina-de-Cadastro-de-Produtos)**onde informa quais campos não devem ser copiados, e através de um tratamento logico pode indicar se o campo deve ser copiado ou não, porem alguns campos ainda serão tratados pelo inicializador do dicionário.**

**Saiba mais:**

[*Clique aqui para mais informações sobre a MATA010*](https://tdn.totvs.com/display/public/PROT/Produtos+-+MATA010#ProdutosMATA010-PastaCadastrais)

[*Clique aqui e veja mais artigos sobre Cadastros e Configurações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Configuração de envio Messenger para ID de eventos do Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003963562-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Configura%C3%A7%C3%A3o-de-envio-Messenger-para-ID-de-eventos-do-Estoque)
