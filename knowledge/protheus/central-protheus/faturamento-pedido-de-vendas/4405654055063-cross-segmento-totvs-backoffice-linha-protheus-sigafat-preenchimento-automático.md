---
article_id: 4405654055063
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 60e9026417bb88565ee29aaa89a3fc8888d2abba466579651a73d1b2ee501823
fetched_at: '2026-06-28T22:38:38.650014+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT -Preenchimento
  automático do campo c5_indpres  e preenchimento da tag indpres
type: support-article
updated_at: '2021-08-13T18:34:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405654055063-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Preenchimento-autom%C3%A1tico-do-campo-c5-indpres-e-preenchimento-da-tag-indpres
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00min** **Dúvida**

Qual é o parâmetro para o preenchimento automático do campo c5\_indpres do pedido de venda (**mata410**)? Como preencher a tag indpres preenchida quando utiliza nota fiscal manual (mata920)?  
  
**Ambiente**   
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Solução**

Não tem parâmetro para efetuar o preenchimento automático do campo **c5\_indpres**, este é um campo de preenchimento manual. O que pode ser efetuado é a configuração do inicializador padrão do campo com a opção desejada entre aspas (**" "**), tendo em vista que o campo é do tipo caracter, é necessário tratar o conteúdo desta forma para não gerar erro de **argument error**:

Exemplo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405653786775/mceclip0.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405658031639/mceclip2.png)

**Importante**: Toda alteração de campo deve ser efetuado via configurador, dicionário de dados, na tabela correspondente, neste caso em específico, na SC5, altere o campo desejado, salve as alterações do campo, salve as alterações da tabela e atualize o dicionário de dados. Posteriormente, reinicie o smartclient para que as configurações efetuadas passe a vigorar na rotina.

Outra informação é que o campo **c5\_indpres** preenche a **tag indpres** do XML para levar a informação de indicador de presença ao Danfe, não há campo correspondente na SF2, desta forma, o XML sempre buscará a informação diretamente do cabeçalho do pedido de vendas (SC5).

Caso seja utilizado a rotina de **Nota fiscal Manual (MATA920**) e necessite de gerar esta tag, não será possível, por que a rotina trabalha apenas com as tabelas referentes a nota fiscal , SD2 e SF2, tendo em vista que não há um campo de indicador de presença correspondente ao c5\_indpres na SF2, a tag não será preenchida.

**Saiba mais sobre** **c5\_indpres**:

**[MP - FAT - Pedido de Venda - Código do Intermediador (Validações e Emissão da NF)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005084801-MP-FAT-Pedido-de-Venda-C%C3%B3digo-do-Intermediador-Valida%C3%A7%C3%B5es-e-Emiss%C3%A3o-da-NF-)**

**[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Como aglutinar pedidos iguais de um mesmo cliente para gerar uma única nota de saída](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115013019207-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-aglutinar-pedidos-iguais-de-um-mesmo-cliente-para-gerar-uma-%C3%BAnica-nota-de-sa%C3%ADda)**

**[Cross-Segmentos-Backoffice-Protheus-Doc-Eletrônicos-029-Falha-de-schema-na-Tag-indpres](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402760998935--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-029-Falha-de-schema-na-Tag-indpres)**
