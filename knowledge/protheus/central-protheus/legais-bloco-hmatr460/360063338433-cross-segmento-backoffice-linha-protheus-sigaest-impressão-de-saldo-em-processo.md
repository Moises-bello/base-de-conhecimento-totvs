---
article_id: 360063338433
category: LEGAIS - BLOCO H/MATR460
content_hash: 9abb881e672eb16850f39daf47e28c568ec0ae0f16d89aec12405d3a1e484cd0
fetched_at: '2026-06-28T22:42:15.074257+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Impressão de saldo
  "Em Processo" indevida. O que fazer?
type: support-article
updated_at: '2021-06-11T20:51:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063338433-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Impress%C3%A3o-de-saldo-Em-Processo-indevida-O-que-fazer
---

**Dúvida**

Ao emitir o MATR460 (Inventário Modelo 7), ocorre que em alguns produtos aparecem na seção de "Saldo em Processo" e não deveriam aparecer. Como identificar para resolver este problema?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - A partir da versão 12.1.17

**Solução**

O Saldo em Processo nada mais é do que um saldo de um produto que está sendo processado para seu consumo gerar um Produto Acabado. Normalmente OPs cujas Matérias Primas ainda estão em processo de consumo para geração do Produto Acabado. Neste artigo daremos algumas dicas de análise quando ocorre de o P7 imprimir um saldo "Em Processo" que a empresa não entende que seria Em Processo.

**Não trabalho com Saldo em Processo nem mesmo Ordem de Produção, porém mesmo assim gera Saldo em Processo.**

Neste cenário, recomendamos que avalie:

- Para este produto, a existência na tabela SD3, registros com D3\_OP preenchido. Caso sim, este produto foi requisitado para uma Ordem de Produção. Avalie a possibilidade de estorno desta requisição;

- Avaliar o produto no relatório MATR989 - Produto em Processo. Se imprimir neste relatório é porque de fato existe um processo envolvendo o produto;

- Avaliar a Data e Armazéns envolvidos no comparativo com o MATR989;

- Avalie se o produto tem saldo no armazém de Apropriação Indireta (MV\_LOCPROC). Quando há saldo e trabalha com o parâmetro MV\_M46PRC ([maiores detalhes deste e outros parâmetros do P7, **clique aqui**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001351901-MP-SIGAEST-Par%C3%A2metros-SX6-relacionados-ao-relat%C3%B3rio-MATR460-Registro-de-Invent%C3%A1rio-Modelo-7)), é impresso no P7 o saldo deste produto como "Em Processo", **mas o saldo deste armazém não é impresso no relatório Em Processo - MATR989**;

- Avalie se o ambiente e o relatório MATR460 está atualizado. Caso necessário, aplicar o Acumulado de Estoque/Custos:

***Pacotes acumulados Estoque/Custos:***

12.1.27- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/960571) **|** 12.1.25- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/826640) **|** 12.1.23- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/748747)

OBS: Aplicar sempre primeiramente em ambiente de homologação.

**Saiba mais:**

*[MP - SIGAEST - P7 - Montagem da seção "Saldo em Processo"](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061473074)*

[*Clique aqui e veja mais artigos sobre o Relatório MATR460(P7) no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000219382-LEGAIS-BLOCO-H-MATR460-P7-)
