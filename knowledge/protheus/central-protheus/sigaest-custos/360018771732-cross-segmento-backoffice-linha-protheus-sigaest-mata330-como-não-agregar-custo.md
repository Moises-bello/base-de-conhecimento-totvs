---
article_id: 360018771732
category: SIGAEST - CUSTOS
content_hash: ddd10b5f9cec9f22928dd8f5536389c15faf498114ae920179b6c4c184749622
fetched_at: '2026-06-28T22:39:00.399650+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Como NÃO
  agregar custo da Matéria Prima (MP) em uma Produção?
type: support-article
updated_at: '2025-03-12T12:26:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018771732-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Como-N%C3%83O-agregar-custo-da-Mat%C3%A9ria-Prima-MP-em-uma-Produ%C3%A7%C3%A3o
---

**Dúvida**

Como não agregar o custo da matéria prima (MP) na ordem de produção (OP)?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Videos sobre o assunto com um passo a passo configurando**:**

**How To | SIGAEST - Não agregar custo da MP no movimento PR0 - parte 01/02**

**How To | SIGAEST - Não agregar custo da MP no movimento PR0 - parte 02/02**

Com os passos abaixo conseguiremos fazer com que uma Ordem de Produção ***não agregue o custo da OP***, ou seja sob o produto configurado para esse quesito a ser requisitado.

**Necessario as configurações.**

1. No cadastro do produto (MATA010), **preencher o campo "Custeio OP" (B1\_AGREGCU) = "Permite"** (permite não agregar o custo do produto na OP).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15211492911511)

**Help do pergunte:**

Indica se o produto em questão poderá ser requisitado para uma ordem de produção sem agregar custo a mesma. Esta situação só ocorrerá se o tipo de movimento interno utilizado na operação estiver configurado para não valorizar produtos com essa caracteristica (F5\_AGREGCU = "NAO").

2. No tipo de movimentação de produção (MATA230), **preencher o campo Custeia OP(F5\_AGREGCU) = "Não"**, desta forma o custo da matéria prima será **desconsiderado** na OP.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15211684388887)

**Help do pergunte:**

Indica se o tipo de movimento interno utilizado na operação deve valorizar a ordem de produção relacionada com os produtos que permitem controle de custeio (B1\_AGREGCU = "SIM").

**Exemplo com OP e produto na estrutura:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15211821820183)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15211940553751)

**Exemplo com OP e produto sem estar na estrutura:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15211778896791)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15211985746711)

**Observações**

* Os produtos que estão cadastrados com o campo Custeio OP (B1\_AGREGCU) = "Não permite" continuarão sendo custeados, independente da configuração do Tipo de Movimentação;
* Se os componentes **são requisitados manualmente (MATA241)** durante o processo produtivo, o Tipo de Movimentação de requisição também deverá ser preenchido com o campo Custeia OP(F5\_AGREGCU) = "Não";
* As Requisições/Devoluções geradas terão o [**tipo RE9 e DE9**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007057091-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Quais-os-significados-dos-c%C3%B3digos-dos-tipos-de-Movimentos-Internos-RE-DE) (Movimentos para OP sem agregar custo).
* Produtos de **Apropriação Indireta (B1\_APROPRI=I)** não são permitidos utilizar esse conceito, ao tentar cadastrar ou mesmo alterar apresenta o **HELP M010APR** impedindo o cadastro;

![001 m010apr.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/26889510683415)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR860 - Interpretando Custos em Ordem de Produção (OP)*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012330641-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR860-Interpretando-Custos-em-Ordem-de-Produ%C3%A7%C3%A3o-OP-)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Quais os significados dos códigos dos tipos de Movimentos Internos RE/DE?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007057091-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Quais-os-significados-dos-c%C3%B3digos-dos-tipos-de-Movimentos-Internos-RE-DE-)
