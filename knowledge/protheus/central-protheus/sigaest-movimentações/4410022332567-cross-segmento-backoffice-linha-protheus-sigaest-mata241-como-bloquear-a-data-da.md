---
article_id: 4410022332567
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 0c6bf4d2453df703b1a145d9c301ad615759ada1de9800d5c16a33b1f77a80c9
fetched_at: '2026-06-28T22:38:56.927504+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA241 - Como bloquear
  a data (DA241DATA) na rotina de Movimentos Internos?
type: support-article
updated_at: '2021-10-04T18:46:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410022332567-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA241-Como-bloquear-a-data-DA241DATA-na-rotina-de-Movimentos-Internos
---

**Dúvida**Como deixar o campo DA241DATA bloqueado para alteração na rotina MATA241?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Para a rotina MATA241, existe uma tratativa que alimenta a variável DA241DATA com as validações do campo D3\_EMISSAO. Basta alterar este campo para ser apenas Visual, a rotina não irá mais permitir a alteração da data.

1° Via Configurador (SIGACFG), acesse ao caminho: Base de Dados -> Dicionário -> Base de Dados:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410022535575/mceclip0.png)

2° - Clique em "Dicionário de Dados", localize a tabela SD3 e clique para Editar:

![mceclip1.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4410022674839/mceclip1.gif)

3° - Altere o campo "Propriedade" para a opção "Visualizar":

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410022271255/mceclip0.png)

Com isso, veja que o campo não permitirá mais alteração:

![](https://totvssuporte.zendesk.com/attachments/token/PpHKgnN0uqUmljAahbye9hs4m/?name=inline329601390.png)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações de Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
