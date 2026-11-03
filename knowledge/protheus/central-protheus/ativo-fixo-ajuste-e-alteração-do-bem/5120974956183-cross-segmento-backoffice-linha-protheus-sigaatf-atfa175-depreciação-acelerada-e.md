---
article_id: 5120974956183
category: Ativo Fixo - Ajuste e Alteração do Bem
content_hash: 5af428cecadfce2ea3a6b986676f1fcd222d51bcd1aa2bb373f09a6f9bcebbb7
fetched_at: '2026-06-28T22:41:58.823344+00:00'
product: protheus
section_id: 1500001546862
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA175 - Depreciação
  acelerada em lote, conceito e funcionalidade.
type: support-article
updated_at: '2023-11-16T16:31:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5120974956183-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA175-Deprecia%C3%A7%C3%A3o-acelerada-em-lote-conceito-e-funcionalidade
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **HH:03:SS min****Dúvida**Conceito e funcionalidade da rotina depreciação acelerada em lote (ATFA175)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Protheus - Ativo fixo - Todas as versões  
  
**Solução**

A rotina de depreciação em lote, tem como objetivo acelerar mensalmente a depreciação de um bem, que terá seu turno de uso, em mais período, ate o final da sua vida útil.

Para processar a depreciação acelerada em lote (ATFA175) é necessário ter um bem cadastrado com o tipo 01 (N3\_TIPO= FISCAL) e a data base tem que ser posterior ao ultimo calculo de depreciação (MV\_ULTDEPR).

ATFA175 irá gerar o tipo 07 (N3\_TIPO), nesse momento não será gerado movimentação na SN4.

O sistema passará a depreciar mensalmente através da rotina de "Depreciação mensal" (ATFA050) tanto o tipo 01 quanto o tipo 07 do bem. Quando a soma da depreciação acumulada (N3\_VRDACM1) do tipo 01 e tipo 07 for igual ao valor de aquisição (N3\_VORIG1) o sistema para de depreciar os dois tipos de ativo e preenche o campo N3\_FIMDEPR com a data do último cálculo.

Exemplo de um bem com valor de aquisição de R$1.000,00 + taxa de 70% ao ano.

Na SN3:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5120730013591/mceclip2.png)

Na SN4

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5120570662807/mceclip1.png)

Relatório de movimentos (ATFA150):

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5120170449303/mceclip0.png)

Importante!

A rotina de descalculo (ATFA070) não estorna a depreciação acelerada da SN3, nem apaga os registros da SN4 ( N4\_TIPO= 07  + N4\_OCORR=10). Por ser uma rotina irreversível, faça um backup das tabelas antes de executar o processo.
