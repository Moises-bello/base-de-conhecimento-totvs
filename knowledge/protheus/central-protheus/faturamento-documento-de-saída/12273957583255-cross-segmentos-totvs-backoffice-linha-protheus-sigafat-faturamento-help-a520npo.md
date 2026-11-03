---
article_id: 12273957583255
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 7e9393dcbcecc87458575f976832c71528856aa0567307981531ca196d4da9a6
fetched_at: '2026-06-28T22:38:45.393015+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento)
  - Help: A520NPODER ao excluir documento de saída'
type: support-article
updated_at: '2023-11-23T14:02:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12273957583255-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Faturamento-Help-A520NPODER-ao-excluir-documento-de-sa%C3%ADda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19278000849559) Tempo aproximado para leitura: **00:03:30 min**

**Ocorrência**Ao excluir um documento de saída ocorreu o Help A520NPODER, como resolver?

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento) - Todas as versões.

**Causa**Esse incidente ocorre, pois existe um documento de entrada, com uma TES que controla poder de terceiros (**F4\_PODER3 = 'D'**) referenciando o documento de saída a ser excluido, que por sua vez também possui em si uma TES que controla poder de terceiros (**F4\_PODER3 = 'R'**).

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12272627903895)

**Solução:**

**OBSERVAÇÃO:** Clique com o botão direto do mouse e vá em "Abrir imagem em uma nova guia" para ver melhor a imagem (com qualidade e definição).

* **1 - Verificar qual a numeração do documento de saída. (No exemplo: 000685)**

**![1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12273602113047)**

* 2 - Localizar filtrando na tabela SB6, no campo B6\_DOC, a linha com a numeração da nota fiscal de saída. (No exemplo: B6\_DOC == **000685**)

![2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12273624764695)

* 3 - Na linha encontrada, verificar o conteúdo do campo B6\_IDENT

![3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12273659908247)

* 4 - Localizar filtrando na tabela SB6, quais são as outras movimentações, filtrando pelo valor encontrado no campo B6\_IDENT da linha com a numeração da nota fiscal de saída, para todos os registros. (No exemplo: B6\_IDENT == 000688).

![4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12273649560087)

* 5 - Aparecerão as outras movimentações de documentos envolvendo o mesmo saldo em terceiros, nas linhas encontradas além do documento de saída, o campo B6\_PODER3 dessas outras linhas provavelmente estarão com conteúdo com "D" de devolução.

![5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12273663817239)

* 6 - Nas linhas encontradas, observe qual dos conteúdos das linhas do campo B6\_DOC. (No exemplo: B6\_DOC '000002' e '000003').

![NEW.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12273708940055)

* 7 - Filtre na rotina de documentos de entrada (MATA103), o documento e série na tabela SD1, por essas numerações no campo 'D1\_DOC'.

![6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12273712499351)

* 8 - Exclua os documentos de entrada que referenciam a nota fiscal de saída.

![7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12273748140567)

* 9 - Exclua o documento de saída desejado.

Verifique que, ao excluir os documentos de entrada que fazem vinculo com o documento de saída, o saldo voltará ao "Saldo **(B6\_SALDO)"**, permitindo a exclusão pois agora o campo "Quantidade **(B6\_SALDO)"** está igual ao **B6\_QUANT** (não houve subtrações) e não há mais de um registro na tabela SB6 com o mesmo identificador **"**Seq. Indent. **(B6\_IDENT)"**.

![8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12273786496407)
