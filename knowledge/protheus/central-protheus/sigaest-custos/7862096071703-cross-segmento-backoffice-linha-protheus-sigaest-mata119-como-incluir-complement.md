---
article_id: 7862096071703
category: SIGAEST - CUSTOS
content_hash: 049611129fd2b532c2db69873a1331785653c8f1299f25b25e9772383a0aadc3
fetched_at: '2026-06-28T22:39:02.045076+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA119 - Como incluir
  complemento de Despesa de Importação e agregar a despesa no Custo?
type: support-article
updated_at: '2025-07-23T11:50:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7862096071703-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA119-Como-incluir-complemento-de-Despesa-de-Importa%C3%A7%C3%A3o-e-agregar-a-despesa-no-Custo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33656789553431) Tempo aproximado para leitura: **00:03:30 min****

**Dúvida**  
Como agregar ***o Custo da Despesa de Importação*** ao meu produto amarrada a um Documento de Entrada (MATA103)?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

A despesa de importação é um processo muito comum em documentos dado entrada como importação, abordaremos, em passo a passo, como fazer este valor agregar ao Custo do Produto.

**Vídeo explicativo do processo de Despesa de Importação no Custo do produto:**

****How To | SIGAEST - Complemento de despesa de Importação no Custo #TOTVS Backoffice (linha Protheus)****

|  |
| --- |
| **Informação importante:****Para que o valor de despesa de importação seja agregado ao custo, no momento da execução da rotina MATA119,** ***deve utilizar TES que Atualiza Estoque (F4\_ESTOQUE=S)*** |

1- Acesse a rotina MATA119

* SIGAEST> Atualizações > Movimentações > Fiscais > Despesas de importação.

Preencha os campos para inclusão da despesa desejada.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7865424769047)

2-  Preencha os dados da despesa a ser agregado.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7865544864151)

3- Selecione o documento, e clique em "Gera Despesas".

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7865639917591)

4- Confirme os dados do documento que ira gerar a despesa, ao documento selecionado, depois clique em salvar, será gerado um novo numero de documento.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7865679499031)

5- Poderá validar no relatório MATR900 o documento incluído com sucesso para custo no produto.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7865930186519)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Agregando o Custo ao Conhecimento de Frete*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053013934-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Agregando-o-Custo-ao-Conhecimento-de-Frete-)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Refaz Custo de Entrada (MATA190) - Conceito e Exemplos*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051999634-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Refaz-Custo-de-Entrada-MATA190-Conceito-e-Exemplos)
