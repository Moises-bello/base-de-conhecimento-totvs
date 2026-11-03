---
content_hash: 401041bc1c32bf06caeb303c587ded93b4a137929af8b68685b88a8fd562f31f
fetched_at: '2026-06-29T00:09:52.191494+00:00'
page_id: '438273534'
product: rm
source: tdn-rm
title: Associação Lançamentos de Saída
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=438273534
version: 13
---

## **Conteúdo**



## **01. Sobre1**

Por meio deste processo é possível associar um lançamento de entrada ao lançamento de saída correspondente a fim de gerenciar a substituição tributária.

O processo está disponível em: Menu Obrigações Principais \ Mais \ Associação Lançamentos de Saída.

Possui somente uma etapa, em que é necessário o preenchimento da informação do código do motivo do ressarcimento.

Além disso, pode-se selecionar um filtro de lançamento a fim de definir para quais lançamentos de saída o processo será aplicado.

Para cada um dos itens associados aos lançamentos fiscais selecionados pelo usuário, o sistema deverá buscar a última entrada que possua ICMS ST informado, desconsiderando as entradas de devolução.

Se a quantidade de itens na última entrada for inferior à quantidade que está no lançamento fiscal de saída, o sistema deve procurar a penúltima entrada e assim sucessivamente, até que toda a quantidade que esteja saindo esteja "coberta".

Para os registros processados corretamente o registro do processo informará qual item de saída foi vinculado a qual item de entrada e em que quantidade.  
Conforme a figura seguinte:

Vão ser consideradas devoluções de venda, desde que tenha ocorrido a associação inversa manual, para contar como saldo de itens disponíveis para futuras associações.

A associação inversa consiste em referenciar no Lançamento de Entrada o Lançamento de Saída, exemplo:

## **02. Advertências:****2**

1 - Ao processar itens já associados, o registro do processo apresentará a seguinte informação:

"O item 1 do lançamento fiscal de saída 58826 não foi processado por já estar associado a um item".

2  - Caso haja uma maior quantidade de itens de saída do que de entradas com ST registradas, o sistema apresentará o seguinte comportamento:

"O produto Produto NF-e do lançamento 58831 e número do item 1 não foi associado por falta de quantidade".

3 - Caso a CFOP de saída seja do tipo Devolução, o sistema apresentará o seguinte comportamento:

"Lançamentos de saída de devolução não podem ser associados automaticamente."

## **03. Agendamento do Processo****3**

Em um ambiente configurado com arquitetura 3 camadas (<http://tdn.totvs.com/pages/releaseview.action?pageId=63277426>), é possível agendar este processo para execução.  
Neste, a última tela do wizard permitirá configurar o agendamento:

**04. Considerações Finais****4**

* Se um lançamento tiver vários itens, caso um item esteja associado e os demais não, o sistema tentará associar os demais itens ainda não associados.
* A associação é feita no formato UEPS - último que entra/primeiro que sai, validando se a quantidade total de produtos da nota já foi associada anteriormente, busca outra mais antiga que ainda não tenha sido associada.
* Somente serão associados lançamentos de até 60 meses, 5 (cinco) anos, a partir da data atual.
* Somente serão associados os itens dos lançamentos fiscais com o valor do ICMS ST maior do que zero.
* Lançamentos de entrada que possui como origem transferência de produtos, também será considerado no **processo de associação de lançamentos** e no filtro de **referência** do item para vinculação de forma manual conforme imagem abaixo:

  Imagem
