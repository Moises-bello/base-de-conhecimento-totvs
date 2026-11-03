---
content_hash: 2882005f163a6b3d378f78c82f54762d85bd4202d4c4c541b3f6ee03317a6876
fetched_at: '2026-06-29T00:09:16.940195+00:00'
page_id: '421388529'
product: rm
source: tdn-rm
title: Preencher Intervalo de Cotações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388529
version: 3
---

Utilizando o processo "Preencher Intervalo de Cotações" você pode incluir várias cotações para uma moeda ou índice no mesmo momento, ou seja, não será necessário incluir uma a uma. O processo de preenchimento de intervalo de cotações é realizado através da janela de visão do cadastro de moedas e índices.

Este processo só pode ser realizado para uma moeda ou índice de cada vez. Marque o registro, abra o processo e informe:

Data Inicial e Data Final

Você pode incluir cotação para uma única data ou para um determinado período.

Exemplo

Cotação para uma única data

* Marcado o índice Poupança
* Data Inicial = 01/05/2007
* Data Final = 01/05/2007
* Fator = 1,10
* Fator Fixo
* Criar datas no intervalo caso não existam

No cadastro de "Cotações" é incluída uma cotação para o índice Poupança na data "01/05/2007" com o valor de "1,10".

Cotação para um período

* Marcado o índice Poupança
* Data Inicial = 01/05/2007
* Data Final = 18/05/2007
* Fator = 1,10
* Fator Fixo
* Criar datas no intervalo caso não existam

No cadastro de "Cotações" são incluídas várias cotações para o índice Poupança da data "01/05/2007" até a data "18/05/2007" com o valor "fixo" de "1,10".

Valor da Cotação

O valor da cotação é informado através da informação "Fator". Você pode determinar que o fator seja "Fixo" ou "Reajustar fator da data anterior em % (percentual)".

Fator Fixo

O valor informado no campo "Fator" será incluído no campo "Valor" da "Identificação" da cotação.  
 Utilizando esta opção para a inclusão de cotações para um período, todas as cotações terão o mesmo valor.

Exemplo

Cotação para um período

* Marcado o índice Poupança
* Data Inicial = 01/05/2007
* Data Final = 18/05/2007
* Fator = 1,10
* Fator Fixo
* Criar datas no intervalo caso não existam

No cadastro de "Cotações" são incluídas cotações para o índice Poupança da data "01/05/2007" até a data "18/05/2007" com o valor único de "1,10" para todas as cotações.

Sobrescrever datas do intervalo

Com esta opção marcada os valores existentes no período informado serão substituídos pelo novo valor.

**Observação**

Se não existirem cotações no período informado, o sistema incluirá automaticamente.

Considerar somente dias úteis

Com esta opção marcada o sistema verifica o calendário utilizado no parâmetro "Calendário Oficial" (Assistente de Implantação de Processos | etapa Calendário Oficial) e só inclui registros de cotações em datas que sejam dias úteis.

Reajustar fator da data anterior em % (percentual)

O valor informado no campo "Fator" irá reajustar em % (percentual) o valor da última cotação incluída para este índice ou moeda e incluirá o resultado do cálculo na próxima cotação.

Exemplo

Cotação para uma única data

Marcado o índice Poupança A última cotação incluída para este índice é no valor de "1,30" na data "01/05/2007"

* Data Inicial = 02/05/2007
* Data Final = 02/05/2007
* Fator = 10 Reajustar fator da data anterior em % (percentual)
* Criar datas no intervalo caso não existam

No cadastro de "Cotações" é incluída uma cotação para o índice Poupança na data "02/05/2007" com o valor de "1,43". (1,30 + 10% = 1,43)

Cotação para um período

Marcado o índice Poupança A última cotação incluída para este índice é no valor de "1,30" na data "01/05/2007"

* Data Inicial = 02/05/2007
* Data Final = 04/05/2007
* Fator = 10 Reajustar fator da data anterior em % (percentual)
* Criar datas no intervalo caso não existam

No cadastro de "Cotações" são incluídas cotações para o índice Poupança nas datas "02/05/2007", "03/05/2007" e "04/05/2007" com os valores de "1,43", "1,573" e "1,7303".

* (1,30 + 10% = 1,43)
* (1,43 + 10% = 1,573)
* (1,573 + 10% = 1,7303)
