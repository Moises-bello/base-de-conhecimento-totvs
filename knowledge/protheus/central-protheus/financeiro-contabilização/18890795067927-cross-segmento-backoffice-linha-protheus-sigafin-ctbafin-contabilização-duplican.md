---
article_id: 18890795067927
category: Financeiro - Contabilização
content_hash: 186eedf3065bbbebdc68486b85914447f8ce0611911324171904493692632dab
fetched_at: '2026-06-28T22:38:05.266622+00:00'
product: protheus
section_id: 1500001550502
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAFIN - CTBAFIN - Contabilização
  duplicando ou gerando gravação incorreta do campo da tabela Sequência de Baixa (E5_SEQ) '
type: support-article
updated_at: '2023-11-08T12:36:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18890795067927-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-CTBAFIN-Contabiliza%C3%A7%C3%A3o-duplicando-ou-gerando-grava%C3%A7%C3%A3o-incorreta-do-campo-da-tabela-Sequ%C3%AAncia-de-Baixa-E5-SEQ
---

**Ocorrência**  
A contabilização registros sendo duplicados online ou offline

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - CTBAFIN - Todas as versões

**Solução**  
Neste artigo será mencionado alguns cenários para que sejam validados, buscando agilizar a solução do tema.

1) Quando é realizado baixas de um título ou por liquidação, compensação, baixa manual e etc... é gravado o conteúdo do campo E5\_SEQ com o número da sequência da baixa parcial realizada.

**Exemplo:**

Título de valor R$ 1.000,00 do tipo:NF, ao baixar por liquidação, compensação, baixa manual no valor parcial  de R$ 100,00

Será gerado a tabela SE5 (Sequencia de Baixa), o campo terá o conteúdo **E5\_SEQ = 01** com o valor de E5\_VALOR = 100,00

Ao baixar novamente por liquidação, compensação, baixa manual o valor de R$ 200,00

Será gerado a tabela SE5 (Sequencia de Baixa), o campo terá o conteúdo **E5\_SEQ = 02** com o valor de E5\_VALOR = 200,00

E assim por diante.

A geração da duplicidade no momento de uma contabilização pode ocorrer caso a gravação do campo  **E5\_SEQ** não esteja sendo incrementada durante as baixas parciais, e sendo gravado tudo com um único conteúdo em todas as baixas.

**Exemplo:**

Ao baixar parcial com valor parcial  de R$ 100,00

Será gerado a tabela SE5, o campo terá o conteúdo **E5\_SEQ = 01** com o valor de E5\_VALOR = 100,00

Baixa parcial no mesmo título no valor de R$ 200,00

Será gerado SE5, o campo terá o conteúdo **E5\_SEQ = 01** com o valor de E5\_VALOR = 200,00

(Veja que o conteúdo do campo foi gravado errado, onde deveria gravar  **E5\_SEQ = 02** )

Baixa parcial no mesmo título no valor de R$ 300,00

Será gerado SE5, o campo terá o conteúdo **E5\_SEQ = 01** com o valor de E5\_VALOR = 300,00

(Veja que o conteúdo do campo foi gravado errado, onde deveria gravar  E5\_SEQ = 03)

**O que deve ser avaliado:**

- O conteúdo dos campos:

Parcela

Cliente ou Fornecedor

Loja

Grupo de Campo "Sequência de baixa"

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/18892548535959)](https://totvssuporte.zendesk.com/guide-media/01HENHWK766TD2A2G07MB5D1R4)

Pois esses campos são chaves de identificação dos títulos, e não podemos alterá-los sem uma análise de base.

Valide se os campos nas tabelas SE1, SE2, SE5 e FK7 se todos possuem os mesmo tamanhos tanto no banco de dados ou na APSDU

Abra também a tabelas de dicionário chamada SX3, e faça essa mesma validação dos tamanhos de campo

Segue um exemplo de uma inconsistência de base, onde um campo parcela está entre as tabelas  SE1 e a FK7

No dicionário veja que as tabelas estão corretas, ambos com o tamanho 2

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/18892501307287)](https://totvssuporte.zendesk.com/guide-media/01HENHXVZ9MGQD6Z7P8V5XJZBZ)

Mas ao ver o tamanho no banco

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/18892548557079)](https://totvssuporte.zendesk.com/guide-media/01HENHZ7BNJFNZMYHDYGY3QN6S)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/18892548566039)](https://totvssuporte.zendesk.com/guide-media/01HENJ04QYMS8WXKN9THHZ98AX)

Veja que o campo E1\_PARCELA possui 2 caracteres de tamanho

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/18892548569623)](https://totvssuporte.zendesk.com/guide-media/01HENJ0M324RSAMJ6K864B0Z3E)

Já o campo FK7\_PARCEL possuem 1 caracter de tamanho

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/18892501328023)](https://totvssuporte.zendesk.com/guide-media/01HENJ22G6J3NQQPAF5NKZ3F2P)

Esse tipo de cenário poderá gerar várias inconsistências de base como:

- Duplicidade na contabilização

- Gravação da E5\_SEQ com inconsistência

- No momento da inclusão de um título, gerar o registro com duplicidade na FK7, sendo que deve gerar um único registro por título.

Entre outras inconsistências não mapeadas que somente é possível de ser encontrada depurando.

**Seguem alguns artigos que têm relação com o tema abordado.**

[FIXSEQBX - Rdmake para ajuste no conteúdo dos campos \_SEQ](https://tdn.totvs.com.br/pages/releaseview.action?pageId=622668372)

[Alteração do campo parcela - Rdmake FinAjuTam - FINA050 - Desdobramento acima de 35 parcelas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021873891-Cross-Segmento-Backoffice-Linha-Protheus-FINA050-Desdobramento-acima-de-35-parcelas)

[SIGAFIN - FINA330 - HELP:NOTITSEL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012361522-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA330-HELP-NOTITSEL)

[SIGAFIN - FINA340 - HELP: NOTITSEL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021352991-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA340-HELP-NOTITSEL)

[MP - SIGAFIN - Help: TITNAOXADO ao cancelar a baixa do título](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053001473-MP-SIGAFIN-Help-TITNAOXADO-ao-cancelar-a-baixa-do-t%C3%ADtulo)

[TOTVS Diagnóstico de Dicionários](https://tdn.totvs.com.br/pages/releaseview.action?pageId=725728577)
