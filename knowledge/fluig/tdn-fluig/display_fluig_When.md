---
content_hash: 097a454fb19f400525d472b3a60258b11b1893ce747c90c32e3a7c6e823afa91
fetched_at: '2026-06-28T21:35:28.093767+00:00'
page_id: '6066576'
product: fluig
source: tdn-fluig
title: When
type: documentation
url: https://tdn.totvs.com/display/fluig/When
version: 10
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**.

A finalidade desse componente é criar decisões a serem tomadas no fluxograma do Fluig ESB. Verifica o valor identificado pelo componente  e realizar a verificação com base nas propriedades informadas.

Nos casos em que não for encontrado nenhum valor do objeto When, pode ser feito um desvio do fluxo do diagrama a partir do uso de um objeto  conectado ao Identifier, redirecionando a mensagem para uma situação de erro, por exemplo.

| Campo | Descrição |
| --- | --- |
| Name | Inserir uma identificação para a configuração do componente. |
| Identifier | Inserir o valor que deverá ser retornado para o objeto na determinada situação. |
| Operation | Selecionar qual o tipo de operação se deseja fazer com a informação recebida:  * **Equals (=)**: para quando for necessário que o valor contido no XML seja o mesmo informado no campo “Identifier value”; * **Not Equals (!=)**: para quando for necessário que o valor contido no XML seja diferente do valor informado no campo “Identifier value”; * **Less Than (<)**: para quando for necessário que o valor contido no XML seja menor do que o valor informado no campo “Identifier value”; * **Less or Equals than (<=)**: para quando for necessário que o valor contido no XML seja menor ou igual ao valor contido no campo “Identifier value”; * **Greater than (>)**: quando for necessário que o valor contido no XML seja maior do que o valor informado no campo “Identifier value”; * **Greater or Equals than (>=)**: quando for necessário que o valor contido no XML seja maior ou igual ao valor informado no campo “Identifier value”. |
| Data Type | Selecionar qual o tipo de dado se deseja validar.  * **String**: quando o tipo do dado a ser validado for texto; * **Number**: quando o tipo do dado a ser validado for um número; * **Date/Timestamp**: quando o tipo do dado a ser validado é uma data ou data e hora. |
| *Case Insensitive* | Quando selecionado, não valida maiúsculas e minúsculas para o Identifier value. Este campo só será habilitado quando o tipo de dado (Data Type) escolhido for String. |
