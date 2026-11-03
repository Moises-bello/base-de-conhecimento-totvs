---
article_id: 360060205974
category: LEGAIS - BLOCO H/MATR460
content_hash: f60afbadf48b98d586565b5fa3be463358a8875dd70a83e228073dd24c5c2acf
fetched_at: '2026-06-28T22:42:15.170202+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR460 está trazendo
  quantidade negativa no Estoque para alguns produtos
type: support-article
updated_at: '2022-06-09T23:11:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060205974-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR460-est%C3%A1-trazendo-quantidade-negativa-no-Estoque-para-alguns-produtos
---

**Dúvida**

Ao emitir o MATR460 (P7) percebi que tem produto(s) com saldo negativo. O que fazer para resolver/ajustar?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - A partir da versão 12.1.17

**Solução**

Para solucionar este problema, siga os passos abaixo

**1° Passo - Avalie se o seu ambiente está atualizado**

Este problema pode estar relacionado com o ambiente estar atualizado ou não. Então, certifique-se de que os Acumulados de Estoque e Livros Fiscais estão atualizados:

***Pacotes acumulados Estoque/Custos:***

12.1.27- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/960571) **|** 12.1.25- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/826640) **|** 12.1.23- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/748747)

***Pacotes acumulados Livros Fiscais:***

12.1.27- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/956585) **|**12.1.25- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/805589) **|**12.1.23- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/770598)

**2° Passo - Emitir o relatório com a pergunta "Considerar Produto com Sld. Negativo?" = Não**

Com esta pergunta, e caso realmente seu saldo no Kardex do mês tenha finalizado este produto com saldo negativo, caso não queira que o saldo seja levado ao P7 basta parametrizar a pergunta "Considerar Produto com Sld. Negativo" = Não

**3° Passo - Caso o saldo esteja negativo de forma incorreta:**

Emitir o relatório MATR900 do mês em questão que originou o saldo negativo filtrando o produto.

**4° Passo - Caso o Kardex deste produto informe que saldo não terminou sendo negativo**

Confira se o MATR460 com está com a pergunta "Considerar Produto com Sld Negativo?" = Sim. Se mesmo com essa condição estiver imprimindo o saldo negativo somente no P7, confira o campo "Data Fechamento" e parametrize conforme a data do último fechamento.

Assim, a régua de comparação passará a ser também com a SB9 (B9\_QINI). Então, deve-se validar, na data do fechamento (B9\_DATA) qual a quantidade (B9\_QINI) e comparar com o Kardex (MATR900) filtrando o último dia sendo a data do fechamento e checar se baterá.

Se mesmo assim houver divergências, validar qual dos relatórios/tabelas apresenta o saldo correto e acionar ao time de Suporte Técnico para melhor avaliação.

**Saiba mais:**

*[MP - SIGAEST - Dicas de Análise dos Saldos no Relatório MATR460 (P7)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061829673-MP-SIGAEST-Dicas-de-An%C3%A1lise-dos-Saldos-no-Relat%C3%B3rio-MATR460-P7-)*

*[Clique aqui e veja mais artigos sobre Bloco H e MATR460 no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000219382-LEGAIS-BLOCO-H-MATR460-P7-)*
