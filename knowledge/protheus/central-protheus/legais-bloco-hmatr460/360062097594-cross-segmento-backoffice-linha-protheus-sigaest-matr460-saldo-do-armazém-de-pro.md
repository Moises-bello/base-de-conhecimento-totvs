---
article_id: 360062097594
category: LEGAIS - BLOCO H/MATR460
content_hash: bababbf5a2615398b6a3a459401dd3bb85bcdcc9882f204aa8be1dfb8b094854
fetched_at: '2026-06-28T22:42:15.160680+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR460 - Saldo do
  Armazém de Processo não está saindo no relatório P7
type: support-article
updated_at: '2026-03-16T11:42:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062097594-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR460-Saldo-do-Armaz%C3%A9m-de-Processo-n%C3%A3o-est%C3%A1-saindo-no-relat%C3%B3rio-P7
---

**Dúvida**  
Ao emitir o Relatório de Inventário Modelo 7 (P7), os produtos que estão no Armazém de Processo não estão sendo impressos no P7. Como ajustar para que seja impresso?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Uma premissa importante do relatório P7 com relação ao Armazém de Processo (MV\_LOCPROC), é que nele na impressão do relatório, trarão apenas os saldos de produtos com Apropriação Indireta (B1\_APROPRI = INDIRETO). Se o produto for de Apropriação Direto, o seu saldo realmente não será apresentado no relatório.

**Caso tenha saldo no Armazém de Processo (MV\_LOCPROC) com produtos com Apropriação Direta (B1\_APROPRI = DIRETO)**

Neste cenário, a recomendação é que seja feita uma transferência do Armazém de Processo para outro Armazém, ou poderá utilizar o parâmetro "**MV\_M460PRC**" (para mais detalhes [clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001351901-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Par%C3%A2metros-SX6-relacionados-ao-relat%C3%B3rio-MATR460-Registro-de-Invent%C3%A1rio-Modelo-7)).

**Existe algum Ponto de Entrada/Personalização que permita o Armazém de Processo ser impresso no P7?**

Não existe nenhuma outra forma do sistema considerar esse armazém.

Exemplos com MV\_LOCPROC = 99:

Temos o Produto PA63. Ele possui Saldo de 10 no Armazém 99

**P7 com PA63 com B1\_APROPRI = I:**

*Pagina 1:*

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003639642)

*Página 2:*

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102520714)

**P7 com PA63 com B1\_APROPRI = D**

*Pagina 1:*

**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102520914)**

*Página 2:*

**![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003639822)**

Observação: Mesmo com B1\_APROPRI = I, o P7 imprime o saldo do produto dentro da seção "Em Processo", ele não imprime como "Estoque Próprio" pois o MV\_LOCPROC têm como conceito ser um Armazém de Processo.

**Saiba mais:**

[*MP - SIGAEST - P7 - Montagem da seção "Saldo em Processo"*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061473074)

[*MP - SIGAEST - P7 - Saldo "Em Processo" incorreto. O que fazer?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002907841)

[*MP - SIGAEST - P7 - Impressão de saldo "Em Processo" indevida. O que fazer?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063338433)

[*Clique aqui e veja mais artigos sobre o Relatório P7 (MATR460)*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000219382-LEGAIS-BLOCO-H-MATR460-P7-)
