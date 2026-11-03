---
content_hash: 229030b57d2e199f8576b4b8d7e927adbf654ef739e7086cd44ff5aafb46b643
fetched_at: '2026-06-29T00:09:28.646645+00:00'
page_id: '423938736'
product: rm
source: tdn-rm
title: Separação de Pedidos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938736
version: 3
---

O movimento que utilizará esta funcionalidade deverá ser previamente parametrizado e executado da seguinte maneira:  
 Menu Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento, acessando a parametrização do Tipo de Movimento desejado  | etapa Estoque - Separação:

* **Usa Separação**: Marcando este parâmetro para movimentos do tipo compra e venda, o módulo de separação estará habilitado (Visão do movimento – Processos – Iniciar Separação). Este recurso é uma forma de distribuição de mercadoria entre cliente/fornecedor. O item de movimento poderá ser identificado pelo código do produto ou código EAN ou código auxiliar ou código reduzido ou número do fabricante.

* **Código do Lote**: No mesmo código informando na separação pode estar o código que identifica o produto e o código que identifica o lote (número do lote). Assim pode ser separada a quantidade de um lote específico do item de movimento.

Exemplo:

O código do produto é 0000001 e para o item de movimento com este produto foram informados três lotes, o 01, 02 e 03.   
Se eu informar na tela de separação o valor 000000102 para o código de separação significa que quero separar o lote 02 do item com produto 0000001.   
Para isso o parâmetro "Posição Inicial do Código do lote" deverá ser 8, pois o número do lote começa na posição 8 do valor informado (os 7 primeiros caracteres é do código do produto);   
e o parâmetro "Tamanho do código do lote" deverá estar com 2, pois o número do lote tem dois caracteres.   
O número do lote somente poderá ficar no final do código informado na separação.   
Se o código do produto é 0000001 e o número do lote 02 o valor informado poderá ser somente 000000102, outra combinação (como o número do lote no início ou no meio do código) não é permitida.

* **Código da Grade**: No mesmo código informando na separação pode estar o código que identifica o produto e o código que identifica a Grade Numerada (número da grade ). Assim pode ser separada a quantidade de um determinado produto com a Grade específica do item de movimento.

Exemplo:

O código do produto Sapato é 0000001 e para o item de movimento com este produto foram informados uma Grade Numerada, cujo o código é P38, P39 e P40.  
Se informar na tela de separação o valor 0000001P40 para o código de separação significa que quero separar o sapato de cor preta número 40 do item com produto 0000001.   
Para isso o parâmetro "Posição Inicial do Código da Grade" deverá ser 8, pois o numero da Grade começa na posição 8 do valor informado (os 7 primeiros caracteres é do código do produto); e o parâmetro "Tamanho do código da grade" deverá estar com 3, pois o número da grade tem três caracteres.   
O número do grade somente poderá ficar no final do código informado na separação.   
Se o código do produto é 0000001 e o número da grade P40 o valor informado poderá ser somente 00000010P40, outra combinação (como o número da grade no início ou no meio do código) não é permitida.

**Processo de Separação**

Para separar os itens de um movimento, deve-se selecionar o movimento desejado, ir ao menu 'Processos' e colocar o movimento no status 'Em Separação' ou iniciando a separação, clicando em Iniciar Separação.  
Na visão de Separação de Pedidos, após digitar a quantidade e o código do produto, o usuário deverá separar item a item, até finalizar a separação.   
Caso não sejam separados todos os itens de compra ou venda, o processo deverá ser finalizado clicando-se no botão 'Finalizar C/ Divergência'.   
Assim o movimento faturado poderá ser faturado parcialmente. Se necessário, o movimento com Status 'Separado' ou 'Em Separação' poderá voltar ao status anterior clicando em 'Voltar ao Status de Separação Anterior' no menu Processos.

**Desfazer separação**: Desfaz qualquer alteração no processo de separação e retorna para a visão do movimento.

**Finalizar**: Finaliza o processo de separação quando a quantidade separada for igual à quantidade original do movimento.

**Separar Parcialmente**: O usuário poderá realizar o processo de separação gradativamente.

**Finalizar C/ Divergência**: Conclui o processo de separação quando os itens estiverem com a quantidade inferior à quantidade original do movimento.

***Observações***:

* Este movimento não deverá aceitar ser parametrizado com separação de lote e utilizar grade simultaneamente, pois o sistema não trabalha com separação de movimentos que contenham itens de grade.
* Na parametrização do tipo de movimento que irá utilizar o processo de Separação não é permitido configurar itens repetidos.
* É possível permitir/proibir acesso aos usuários para "Colocar Movimentos em Separação' e "Iniciar Separação', através do cadastro de perfil (Cadastros/Segurança/Perfis/Pasta Acesso a Menus).
* A quantidade deverá ser informada antes do código do produto.
* É possível selecionar mais de um movimento e colocá-los em separação, mas não inicia-los. Basta selecionar os movimentos desejados, clicar no menu Movimentos/Colocar Movimento em Separação.
* Ao realizar movimentações de entrada, o sistema permite que sejam separadas quantidades maiores que a quantidade original do item.
* Para movimentações de saída, o sistema não permitirá que sejam separadas quantidades maiores que a original.
