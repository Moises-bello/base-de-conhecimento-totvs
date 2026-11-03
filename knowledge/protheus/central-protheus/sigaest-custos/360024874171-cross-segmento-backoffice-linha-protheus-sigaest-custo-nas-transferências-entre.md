---
article_id: 360024874171
category: SIGAEST - CUSTOS
content_hash: c3596dbc75e412ca4246e5b284a3bc000f42790feab0ab2cdb4d15d882e1c09c
fetched_at: '2026-06-28T22:39:02.401944+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST – Custo nas transferências
  entre filiais
type: support-article
updated_at: '2026-02-13T16:14:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024874171-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Custo-nas-transfer%C3%AAncias-entre-filiais
---

**Dúvida**

Como interpretar o Custo nas operações de transferência entre filiais (MATA310/MATA311)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
  
**Solução**

**Cenário para demonstração dos Custos**

Neste artigo iremos detalhar um cenário em que é realizada uma transferência da filial “D MG 01” para a filial “D MG 02” e posteriormente o produto é transferido da filial “D MG 02” para a filial “D MG 01”.

**IMPORTANTE:** **Para que o custo de transferências entre filiais fique correto, é necessário executar o recálculo do custo médio (MATA330) simultaneamente para todas as filiais que tiveram transferências entre si.**

Partimos da premissa de que a entrada de transferência entre filiais deve ser valorizada conforme a saída da filial origem. Então, a saída da filial “D MG 01” deve ser o mesmo da entrada na filial “D MG 02”.

**Entendendo a ordenação das movimentações no Kardex**

O que geralmente gera dúvida é no caso da ordenação dos movimentos.  Veja no relatório Kardex por Período (MATR900) onde é possível notar que as entradas de transferência da filial D MG 02 ficaram abaixo das saídas de transferência da filial “D MG 01”:

![matr900_D_MG_01.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023240651)

Veja também no relatório que efetuamos uma venda (TES 501) que ficou ordenada corretamente e absorvendo o custo destas transferências entre filiais com o custo de 10,60.

No link abaixo, na aba “Ordenação de Movimentos”, temos a descrição de como deve ser a ordenação de transferências entre filiais.

[MATA330 - Documentação completa do Custo Médio](http://tdn.totvs.com/pages/releaseview.action?pageId=340361781)

Veja que, segundo a documentação, as saídas devem estar ordenadas **acima** das entradas. Porém, veja na imagem abaixo que na filial “D MG 02” isto não ocorre, pois o sistema entende que esta saída tem que ser valorizada absorvendo o custo da entrada da filial “D MG 01”.![matr900_D_MG_02.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023240671)

**Analisando a TRB**

A TRB é a uma tabela temporária que a rotina do Recálculo do Custo Médio (MATA330) gera durante seu processamento. Para mais detalhes de como extrair a TRB, [**clique aqui.**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011904591-MP-SIGAEST-Como-extrair-arquivo-de-trabalho-TRB-ao-executar-o-custo-m%C3%A9dio-MATA330-) Para que a ordenação fique correta é necessário indexar esta tabela através da ferramenta APSDU com o índice abaixo.

**DTOS(TRB\_DTBASE)+TRB\_SEQPRO+TRB\_ORDEM+TRB\_NIVEL+TRB\_NIVSD3+TRB\_CHAVE+TRB\_SEQ**

Abaixo temos o print da TRB onde podemos ver a ordenação dos registros. A ordenação ocorre desta forma pois, se a entrada da filial “D MG 02” for alterada, a saída da transferência para filial “D MG 02” ficaria com o custo diferente da saída da filial “D MG 01” e entrada na filial “D MG 02”.

Veja que existe uma amarração entre os campos TRB\_FILIAL e TRB\_FILTRA, indicando que é uma transferência entre filiais.

![TRB.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023240791)

Abaixo podemos ver a TRB somente da filial “D MG 01”.

![TRB_D_DM_01.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023240811)

E abaixo temos a TRB da filial “D MG 02”.![TRB_D_MG_02.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023240831)

Caso este cenário não atenda a regra de negócio do cliente e seja necessário alterar esta ordenação pode ser utilizado o ponto de entrada [MA330TRB](https://tdn.totvs.com/display/public/mp/Ponto+de+Entrada+MA330TRB).

Sobre o custo de ORIGEM ser diferente para o DESTINO

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como alterar o custo de entrada na transferência entre filiais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4638410759319-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-alterar-o-custo-de-entrada-na-transfer%C3%AAncia-entre-filiais)

**Saiba mais:**

[*Clique aqui e veja mais artigos de Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000049222-SIGAEST-CUSTOS)
