---
article_id: 1500002839582
category: LEGAIS - BLOCO H/MATR460
content_hash: d8050d81e45544e98e59e77bc33b0fe69177c5d34c40339ca7629d647d5c4ef9
fetched_at: '2026-06-28T22:42:15.093111+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR460 - Como emitir
  o Relatório filtrando por tipos específicos de Produtos?
type: support-article
updated_at: '2021-06-14T12:24:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002839582-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR460-Como-emitir-o-Relat%C3%B3rio-filtrando-por-tipos-espec%C3%ADficos-de-Produtos
---

**Dúvida**

Como emitir o relatório P7 filtrando tipagens específicas de produtos?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - A partir da versão 12.1.23

**Solução**O Parâmetro MV\_BLHDSTP  deixou de ser utilizado. Então uma alternativa para outros tipos de produtos serem considerados na impressão do P7 é através da personalização do relatório do mesmo.

**Exemplo prático:**

No nosso exemplo, **não queremos** que produtos do tipo **MC** sejam considerados na impressão do P7.

No Inventário Mod. 7, clicando em "Personalizar", você consegue fazer o filtro desejado (desconsiderar B1\_TIPO = MC) na impressão. Veja a imagem abaixo de como será feito:

![](https://totvssuporte.zendesk.com/attachments/token/nZ2Co6LDTpQ8YY420IZYnMfAJ/?name=inline565052216.png)

Clicando em Filtro -> Selecione a tabela SB1 -> Campo "Tipo" com a condição **Diferente De** = MC.   
  
Com isso, basta Adicionar, Salvar e dar um OK para tirar o P7 novamente.

**Saiba mais:**

*[MP - SIGAEST - Dicas de Análise dos Saldos no Relatório MATR460 (P7)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061829673-MP-SIGAEST-Dicas-de-An%C3%A1lise-dos-Saldos-no-Relat%C3%B3rio-MATR460-P7-)*

*[MP - SIGAEST - Perguntas do relatório MATR460 (Inventário Modelo 7)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001540542-MP-SIGAEST-Perguntas-do-relat%C3%B3rio-MATR460-Invent%C3%A1rio-Modelo-7-)*

*[Clique aqui e veja mais artigos sobre o Relatório MATR460 (P7)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000219382-LEGAIS-BLOCO-H-MATR460-P7-)*
