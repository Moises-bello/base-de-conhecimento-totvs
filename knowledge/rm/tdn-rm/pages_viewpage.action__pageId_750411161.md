---
content_hash: ae1d45e5934d6b1fa22dd79196fbad66d550fb0ba42a66b1a1775c497e858d58
fetched_at: '2026-06-29T00:11:32.916602+00:00'
page_id: '750411161'
product: rm
source: tdn-rm
title: Relatórios - Controle de Inadimplência - Smart View
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=750411161
version: 15
---

Este relatório apresenta os valores das parcelas em atraso, dos contratos de venda efetivados, em um período pré definido, promovendo aos gestores um **Controle de Inadimplência** sobre estes valores.

Importante!

Para ter acesso a este relatório, é preciso que o Perfil do usuário tenha acesso à opção: *[01.01.01] - Contratos de Venda*, sem necessidade de ter acesso às demais tarefas abaixo desta.

Ao acessar este relatório no Smart View é possível de se aplicar os seguintes *Parâmetros de Visualização*:

* **Código da Coligada:** Neste parâmetro é possível de se filtrar as Coligadas, onde o valor padrão *-1*, processa todas as coligadas e caso o usuário queira filtrar uma ou mais coligadas específicas, pode-se realizar esta ação alterando este valor e/ou acrescentando as demais coligadas, através do botão "+" localizado em frente à descrição do mesmo;
* **Código do Empreendimento:** Neste parâmetro é possível de se filtrar o Código do Empreendimento, onde o valor padrão -1, processa todos os empreendimentos e como ocorre com o parâmetro da entidade acima, caso o usuário tenha necessidade, pode-se filtrar um ou mais empreendimentos específicos através dos botões destinados a este fim;
* **Calcular Valor Líquido:** Este parâmetro define se o sistema irá calcular o Valor Líquido de todas as parcelas dos contratos de venda filtrados nos parâmetros acima. Por questões de performance, o valor padrão deste parâmetro é 0, que não realiza este cálculo, trazendo os valores que estão consolidados na base.

Caso o usuário deseje calcular o valor líquido para a data especificada no parâmetro mais abaixo, é necessário alterar este valor para 1, porém ao realizar esta ação, por questões de performance, recomendamos que os filtros aplicados nos parâmetros acima sejam restritos à uma entidade por vez, já que o sistema irá executar todos os processos necessários para calcular os valores atualizados, como reajuste e as fórmulas de juros e multa; e

* **Data Valor Líquido:** Este parâmetro permite ao usuário especificar uma data base que é utilizada para a atualização do valor líquido. É com base nesta data que o sistema calcula os dias em atraso das parcelas. Por padrão, o sistema apresenta a data corrente e caso o usuário tenha necessidade, é possível de alterá-la.

Importante!

O cálculo do valor liquido deste relatório executa o processo de reajuste em memória e para que este cálculo seja executado com sucesso, é preciso que as cotações das moedas utilizadas nas vendas estejam atualizadas em relação à data solicitada e à defasagem das mesmas nas condições destas vendas.

Após definir estes parâmetros e gerar o relatório, o sistema apresentará as seguintes informações:

* Agrupador **Consolidado**: É um totalizador com um resumo das informações de todas as coligadas e empreendimentos selecionados:
  + **Número de Parcelas em Atraso:** É a proporção total de parcelas em atraso, conforme os parâmetros aplicados;
  + **Valor Total em Atraso:** É a soma dos valores líquidos de todas as parcelas dos contratos de venda, dos empreendimentos filtrados, conforme definido nos parâmetros de visualização deste relatório;
  + **% de Parcelas em Atraso:** É o número de parcelas em atraso, dividido pelo número total de parcelas;
  + **Período Médio de Atraso:** É a soma dos dias em atraso, dividido pelo número de parcelas em atraso;
  + **Valor em Atraso de 1 a 30 dias:** É a soma dos valores das parcelas com atraso entre 1 e 30 dias, contados a partir da data de vencimento delas;
  + **Valor em Atraso de 31 a 60 dias:** É a soma dos valores das parcelas com atraso entre 31 e 60 dias, contados a partir da data de vencimento delas; e
  + **Valor em Atraso com mais de 60 dias:** É a soma dos valores das parcelas com atraso com mas de 60 dias, contados a partir da data de vencimento delas.
* Agrupador de **Empreendimento**: É um sub cabeçalho, para cada empreendimento, no qual são apresentadas exatamente as mesmas colunas citadas acima, porém totalizados por Empreendimento;
* Sub agrupador **Detalhes**: É um frame vinculado ao sub cabeçalho acima, no qual são apresentados os detalhes das parcelas em atraso, pelo cliente do contrato de venda. São apresentadas as seguintes colunas:
  + **Cliente:** É o nome do cliente que é o Comprador Principal no contrato de venda da subunidade detalhada;
  + **Unidade:** É a Unidade/Bloco/Quadra da subunidade do contrato de venda;
  + **Subunidade:** É a Subunidade/Apartamento/Lote da subunidade do contrato de venda;
  + **Nro Parcelas em Atraso:** É a quantidade de parcelas em atraso, do contrato de venda listado;
  + **Valor em Atraso:** É a soma dos valores líquidos de todas as parcelas em atraso deste contrato de venda, conforme definido nos parâmetros de visualização deste relatório;
  + **Dias de Atraso:** É o número de dias de atraso da parcela mais antiga, ou seja, o maior número de dias em atraso, das parcelas deste contrato de venda;
  + **Multa:** É a soma dos valores de multa das parcelas deste contrato de venda, calculados conforme definido nos parâmetros de visualização deste relatório;
  + **Juros de Mora:** É a soma dos valores de juros de mora das parcelas deste contrato de venda, calculados conforme definido nos parâmetros de visualização deste relatório.
  + **Total**, do *Nro de Atraso*, do *Valor em Atraso*, do *Dias de Atraso*, da Multa, do J*uros de Mora*.
