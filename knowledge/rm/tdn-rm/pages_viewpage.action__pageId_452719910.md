---
content_hash: 072417d2f9582cc9536c2bcdc43f1d52d074edcc0067638d47e1561e88b9709b
fetched_at: '2026-06-29T00:10:10.694594+00:00'
page_id: '452719910'
product: rm
source: tdn-rm
title: Lançamentos Globais - Extra Autorizada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719910
version: 3
---

**Lançamentos Globais - Extra Autorizada**

Utilize esta opção para Aprovar extras executadas ou Autorizar hora extra diária diferente da hora extra determinada na pasta de outros parâmetros no cadastro do funcionário. A Aprovação consiste em aprovar as extras já executadas ou aprovar um valor diferente das extras executadas, já a Autorização consiste em autorizar ou pré-autorizar um valor de horas extras para determinado período antes mesmo da execução destas extras.

Para fazer o lançamento é necessário preencher os campos abaixo:

***Autorizar Extra***

**Nº de Horas**

Informe neste campo o número de horas diárias que deseja Autorizar ou Aprovar para a seleção de funcionários. Este campo só será habilitado se o parâmetro "Considera extra autorizada por intervalo" estiver desmarcado na pasta Iniciais dos parâmetros do Totvs Automação de Ponto.

**Total**

Selecione este parâmetro para cancelar toda extra autorizada, do contrário informe o número de horas. Este campo só será habilitado se o parâmetro "Considera extra autorizada por intervalo" estiver desmarcado na pasta Iniciais dos parâmetros do Totvs Automação de Ponto.

**Início/Fim**

Informe neste campo o intervalo de horas diárias que deseja Autorizar ou Aprovar para a seleção de funcionários. Este campo só será habilitado se o parâmetro "Considera extra autorizada por intervalo" estiver marcado na pasta Iniciais dos parâmetros do Totvs Automação de Ponto.

**Motivo**

Caso queira informar o motivo da autorização da extra, informe neste campo.

**Justificativa**

Informe neste campo uma justificativa para autorização da hora extra que deve ser previamente cadastrada em Tabelas Dinâmicas. O código da tabela dinâmica para o cadastro de justificativa é "AJUSTHEXTR".

**Responsável**

Caso queira informar o responsável para autorização da extra, informe a chapa do responsável ou clique no ícone de seleção para selecionar o responsável.

***Aprovar considerando extras executadas***

Este campo deverá ser habilitado para que sejam selecionados os tipos de extras a serem aprovadas.

**Tipos de Extras**

Selecione o(s) tipo(s) de extras que deseja aprovar ou cancelar. Deverá ser selecionado pelo menos um tipo de extra.

**Formas Lançamento**

**Intervalo considerando extras executadas**

Este parâmetro só será habilitado quando a autorização da hora extra for por intervalo. Ao marcar este parâmetro será necessário informar o período de início e fim (intervalo) de horas extras a serem autorizadas.

**Toda extra executada**

Este parâmetro só será habilitado quando a autorização da hora extra for por intervalo. Ao marcar este parâmetro não será permitido o período de início e fim (intervalo) de horas extras a serem autorizadas, o sistema cancelará toda extra autorizada ou realizará a aprovação de toda extra executada. As formas de lançamento só ficarão habilitadas se o parâmetro "Aprovar considerando extras executadas" estiver marcado.

***Cancelar Extra Autorizada***

Marque esta opção para cancelar a extra autorizada que foi lançada para o funcionário. O cancelamento poderá ser feito por tipo e forma de lançamento, permitindo cancelar toda extra executada ou apenas o intervalo, basta informar em Extra Autorizada o número de horas ou o intervalo das extras que deseja cancelar. Os campos número de horas ou intervalo das extras devem ser preenchidos com exatamente o número ou o intervalo que deseja cancelar.

**Observação:**

A extra autorizada que será cancelada não é a extra que está informada no parametrizar funcionários - etapa Extras. A extra que será cancelada é a extra que é autorizada dia a dia por este módulo ou via espelho do período do funcionário em Anexo | Extras Autorizadas. Para o cancelamento por tipo e forma de lançamento o parâmetro "Aprovar considerando extras executadas" deverá estar marcado.
