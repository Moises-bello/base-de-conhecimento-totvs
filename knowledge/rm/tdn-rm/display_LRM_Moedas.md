---
content_hash: 1ba9c46924e9b8aef3cbfe9a08ac51b9343a59f9442d44197cd4320a7f53dad1
fetched_at: '2026-06-29T00:10:53.834326+00:00'
page_id: '588681922'
product: rm
source: tdn-rm
title: Moedas
type: documentation
url: https://tdn.totvs.com/display/LRM/Moedas
version: 12
---

Nesta etapa são disponibilizados os parâmetros que denotam as moedas utilizadas pelo sistema. Temos a moeda corrente/funcional e as moedas alternativas/paralelas.

**Moeda corrente**

Se trata da moeda oficial / funcional considerada para todo o módulo contábil.

Todos os valores monetários apresentados nos registros, relatórios, etc - quando não houver um indicativo especifico de multimoeda (nestes casos os valores nas demais moedas são apresentados em outros funcionalidades como anexos, colunas/campos complementares, etc) - são expressos em tal unidade.

A definição da moeda corrente é realizada através da seleção de um dos registros do cadastro de moedas e índices (módulo Financeiro) que esteja com o atributo "Tipo" sendo do tipo moeda, isto é, para seleção da moeda corrente, somente serão exibidos registros que sejam do tipo "Moeda".

**Moedas utilizadas nos processos contábeis multimoedas**

Neste parâmetro, que se encontra na forma de um cadastro, é possível informar as diferentes moedas que se deseja que o sistema calcule os valores (de acordo com cotações, índices, multiplicadores, etc), os mantenha gravados e os apresente em visão, edição, anexo, relatório, etc,.

Não será permitido inserir a moeda que foi definida como moeda corrente.

Não são todas as funcionalidades e/ou recursos onde serão apresentados os valores nas multimoedas aqui cadastrados. Inicialmente teremos estes valores nos lançamentos contábeis (e seus rateios), no processo de equivalência patrimonial e alguns relatórios: Balancete, Balanço, Demonstrações Contábeis.
