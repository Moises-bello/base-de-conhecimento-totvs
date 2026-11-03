---
content_hash: 1705d6c5947e95bb56a7b9fe841d051960bd45fb6b62df59b3ddc9afcab6ac3a
fetched_at: '2026-06-29T00:11:04.275063+00:00'
page_id: '625937600'
product: rm
source: tdn-rm
title: Portal de Imóveis - Backend - Globais - Situação da Unidade
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=625937600
version: 4
---

#FF9000Introdução

O cadastro de situação da unidade determina qual o status a unidade terá com o avançar das negociações no Portal de Imóveis. Este cadastro já vem previamente construído e pode ser modificado pelo cliente.

Existe uma linha tênue que separa o status de uma unidade e uma proposta de venda. Temos que ter em mente que são duas situações distintas e que em algum momento elas podem se fundir possuindo o mesmo nome, exemplo:

| Ação | Situação da unidade | Situação da proposta |
| --- | --- | --- |
| Reservar uma unidade | Reservada | nenhuma |
| Fazer uma proposta para uma unidade | Em Proposta | Aprovada ou Reprovada |
| Avançar a proposta para contrato em assinatura | Em assinatura | Em assinatura |

No cadastro de situações de unidades definidos a correlação das situações do Portal de Imóveis com as situações existentes no TOTVS. Através da situação da unidade podemos ter o Portal de Imóveis sempre atualizando a situação da unidade no TOTVS de acordo com o que for feito no portal.

Importante: A Partir da versão 12.1.33, o Portal de Imóveis permitirá a exclusão das situações de unidades que não estão em uso do sistema, ou seja, que ainda não possuem registro na tabela de unidade.#FF9000Procedimentos para utilização

Ao abrir a tela de cadastro ou edição de uma situação de unidade teremos os seguintes campos para informar:

* Titulo - Nome da situação
* Atualizar situação no Backofice - se marcado muda a situação da unidade no RM de acordo com a situação determinada no próximo campo
* Situação no Backoffice - Mostra um combobox com todas as situações existentes no cadastro de situações de unidades do TOTVS RM. Se for marcado o campo anterior, deve-se selecionar a situação desejada no RM.
* Cor de fundo e das letras - utilizado para customizar as cores de cada situação criada.
* Permite propostas - se marcado, as unidades nesta situação poderão ter propostas de venda.
* Mostrar Preços - se marcado, as unidades nesta situação terão seus preços de tabela visíveis.
* Permite Reservas - quando marcado, uma unidade nesta situação permite que seja feita reservas para ela
* Permite enviar venda para backoffice -
* Visível na tabela de preços - se marcado as unidades que estirem nesta situação serão visíveis na tabela de preços.
* Contabilizar no totalizador de unidades disponíveis - Quando esta opção está marcada, definirá que a situação da unidade irá ser mostrada na soma de unidades disponíveis de um empreendimento.

Uma possibilidade interessante é o agrupamento de situações do RM em uma situação no Portal de Imóveis. Esta possibilidade é útil quando desejamos, por exemplo que as unidades com as situações de permuta, reserva técnica, vendidas e bloqueadas juridicamente, todas apareçam no portal como VENDIDAS. Para isto basta na parte inferior da tela selecionar todas as unidades no TOTVS que irão compor a unidade do Portal de Imóveis.
