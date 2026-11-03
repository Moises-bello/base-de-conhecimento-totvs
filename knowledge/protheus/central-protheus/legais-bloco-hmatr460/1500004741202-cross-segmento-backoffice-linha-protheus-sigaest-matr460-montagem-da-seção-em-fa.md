---
article_id: 1500004741202
category: LEGAIS - BLOCO H/MATR460
content_hash: fa9589852fd8894940d3e1871ca9dd22070c3bad73d5c0c46062a94d86e6b238
fetched_at: '2026-06-28T22:42:15.133575+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR460 - Montagem
  da seção "Em Fabricação/Em Elaboração"
type: support-article
updated_at: '2026-01-02T18:24:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004741202-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR460-Montagem-da-se%C3%A7%C3%A3o-Em-Fabrica%C3%A7%C3%A3o-Em-Elabora%C3%A7%C3%A3o
---

A seção "Em Fabricação/Em Elaboração" no relatório P7 considera Ordens de Produção com movimentações de requisição/devolução, excluindo as sem movimentação. Esse saldo refere-se a produtos acabados em processo produtivo, diferente do saldo "Em Processo". Ao selecionar ambos os saldos, o sistema prioriza o saldo "Em Fabricação". O saldo é calculado pela quantidade original da Ordem menos perdas apontadas, mais requisições.

**Dúvida**  
Como é montada a seção de saldo "Em Fabricação/Em Elaboração" no relatório P7?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

**O que é o saldo Em Fabricação?**

Conforme o entendimento da legislação, os saldos em Elaboração/Fabricação referem-se aos produtos acabados que ainda estão em processo produtivo, porém ainda não finalizados. Ou seja, diferentemente do saldo "Em Processo" ([**clique aqui para conhecer mais sobre ele**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061473074)), aqui temos um viés de produto final, normalmente do tipo PA.

**Como ele é tratado no relatório P7?**

* Serão consideradas nesta seção, somente Ordens de Produção **que possuam movimentações de requisição/devolução**. Ordens de Produções que estiverem abertas, **porém sem nenhuma movimentação não serão consideradas**.
* Quando o relatório for configurado para apresentar o Saldo em Elaboração/Fabricação, as movimentações de requisição/devolução que forem consideradas para a composição deste saldo são as mesmas da seção de **Saldo em Processo**. Desta forma, gerar o relatório com as opções de saldo em processo e saldo em fabricação acarretaria em duplicidade de valores.  
  **Dessa forma, caso as opções Saldo em processo e Saldo em Elaboração/Fabricação forem selecionadas para impressão, o sistema vai priorizar o saldo em** **Saldo em Elaboração/Fabricação.**

**Exemplo de utilização**

* Considerando uma estrutura conforme abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006184662)

* Abertura de uma Ordem de Produção de quantidade 5:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006305481)

* Requisição da quantidade empenhada de quantidade 5:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006305521)

* Apontamento de Perda de quantidade 1:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006305561)

* Realizado a geração do Relatório de Inventário Mod 7

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006184782)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006184802)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006184822)

Observação: Note que a coluna QUANTIDADE é o resultado da Quantidade Original da Ordem de Produção – Quantidade de Perdas Apontadas + Quantidade de Requisições para a OP.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre o relatório MATR460 (P7)*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538741-LEGAIS-BLOCO-H-MATR460)
