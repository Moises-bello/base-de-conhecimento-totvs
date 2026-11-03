---
content_hash: 0f7f74f8f9926474d628e2ea33a45ab81306b65f5dab6db2c200b4f94a785246
fetched_at: '2026-06-29T00:11:45.713061+00:00'
page_id: '821184753'
product: rm
source: tdn-rm
title: TCGI - Comissão - Recálculo de Comissão por Competência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=821184753
version: 21
---

**A partir da versão 12.1.2310.146**

Utilize o processo de **Recálculo de Comissão por Competência** para recalcular a comissão de uma competência já tratada anteriormente, mesmo que ela já tenha sido calculada, paga ou integrada.

Este processo irá atualizar os valores destas comissões em relação ao percentual da comissão que pode ter sido alterado durante o período, seja pelo corretor ter atingido alguma meta posterior ao cálculo das comissões ou, seja por um ajuste necessário. Porém, quando a alteração dos valores de comissão for por meta alcançada por fechamento de competência, então utiliza-se o recurso .

O processo adicionará a diferença a maior a ser paga em um novo tipo de comissão complementar, caso a comissão original já esteja paga/integrada, ou alterando o valor da comissão original, caso a comissão ainda não esteja integrada. Se a diferença seja a menor, o processo tentará descontar dos itens das comissões que estejam em aberto, mesmo que a comissão toda esteja integrada. Caso não seja possível descontar todo o valor, pois o item da comissão esteja integrada/paga, o sistema colocará o processo como aviso e alertará que não possível descontar todo o valor da diferença. E que para descontar tudo, o cliente precisará desfazer a integração dessas comissões para que seja possível reduzir o valor da diferença.

Para permitir este tipo de recálculo por competência foi criado um parâmetro em Contrato de Vendas => Comissão => Nova Comissão "Permite Recalcular Comissão Integrada Por Competência"

 O que o processo faz :

> * Verifica se o parâmetro "permite recalcular a comissão caso esteja integração ou paga" está marcado;
> * Permite agendar o processo para recalcular a comissão por competência;
> * O processo irá recalcular o valor da comissão da competência, considerando o percentual atual da comissão, que poderá ser diferente do que foi praticado nas vendas já realizadas durante o período.
> * Caso a comissão das vendas anteriores à execução deste processo, não estiver integrada, o valor será recalculado no próprio item da comissão original, seja para valor a maior ou a menor;
> * Caso a comissão das vendas anteriores à execução deste processo já estiver integrada, será gerado um novo item de comissão do tipo comissão complementar, com o valor da diferença encontrada no recálculo. Será criada uma nova parcela com a data de vencimento informada no processo ou com a data de vencimento da primeira parcela das comissões de origem do recálculo;
> * As comissões complementares também são recalculadas no processo do recálculo e se for encontrada diferença, seguirá o mesmo critério do recálculo de comissões, ou seja:
>   + Se a comissão complementar não estiver integrada, seu valor será atualizado;
>   + Se a comissão complementar estiver integrada, será gerada um novo item de comissão do tipo comissão complementar.
> * Para efeitos de relatórios e valores sumarizados da comissão, o sistema irá tratar da mesma forma os valores da comissão e da comissão complementar, sendo que os tipos de comissões meta e prêmio são diferentes.

**O que o processo não irá fazer:**

> * Recálculo automaticamente a cada venda realizada, para **evitar problemas de performance.** O processo precisará ser agendado para que aconteça ou executado sempre que necessário;
> * Caso o recálculo da comissão gere um **valor menor** do que a comissão já integrada, devido ao cancelamento de alguma comissão já calculada, não será realizado o tratamento para a diferença a menor, ou seja, este valor **não será atualizado** e sistema emitirá um Aviso no log deste processo, sugerindo que a integração da comissão seja desfeita para que seja possível reduzir o valor da diferença da comissão;
> * Gerenciar a diferença a menor, pois será de responsabilidade do cliente fazer e controlar a compensação desta diferença;

Atenção

* O processo do recálculo da comissão, já existente na tela da comissão, não irá recalcular as comissões integradas/pagas, pois o processo não recalcula as outras vendas que interfere nessa venda, desta forma, esse processo só irar calcular vendas calculadas ou com erros.
* Uma vez executado o processo de "Recálculo da Comissão por Competência", as alterações realizadas nos valores das comissões não podem ser revertidas pelo sistema. Caso ocorram falha nas fórmulas, ocasionando resultados inesperados, o processo de recálculo deve ser executado novamente para poder corrigir esses valores. Caso haja a necessidade de que a comissão seja toda refeita, será necessário cancelar a comissão e gerar novamente.

### Exemplo de um caso completo de gerar comissão e como realizar o recálculo por competência

Vamos criar uma regra que seja flexível e que seu valor seja recalculado a cada venda nova na competência 08/2023 por ter atingido uma nova faixa de vendas com um novo percentual de comissão.

Fórmula da comissão do Corretor

Modalidade da Comissão

Gerei a primeira comissão da venda 3

Como foi a primeira venda do Corretor, então será uma comissão de 2%

Realizei a integração dessa comissão, pois o corretor tinha que receber imediatamente (exemplo hipotético)

Realizei a segunda venda do mesmo corretor e imobiliária

Essa segunda venda já calculou a comissão desse corretor taxa com 2,5%, pois é a segunda venda do mesmo corretor. Mas a primeira comissão continua com 2% e precisa ser recalculado por competência

Então, como precisava pagar a diferença da primeira venda do corretor, eu pedi para recalcular a comissão de todas as vendas na competência 08/2023 e

lançar a diferença no vencimento de 01/02/2024, pois a venda 1 já está integrada e será lançamento a comissão complementar com a diferença de 0,5%

Veja o detalhe do log

Veja como ficou a comissão da primeira venda: Foi inserido a comissão complementar com a diferença do recálculo, onde a comissão deveria ser de 2,5%,

mas foi calculada inicialmente com 2% e depois foi lançado a diferença de 0,% na comissão complementar, caso já existisse uma comissão complementar em aberto,

o sistema iria somar essa diferença na comissão em aberto da complementar, e caso estivesse já integrada a comissão complementar, o sistema iria criar uma novo

item de comissão complementar com o valor da diferença

Veja a comissão complementar com a diferença de 0,5%

Será realizado a integração das parcelas da comissão complementar da primeira venda

Agora a segunda venda será cancelada, pois a venda caiu por não aprovação do crédito do cliente. Desta forma, primeira venda deverá ser recalculada novamente,

pois a comissão dela foi considerada que tinha duas vendas ativas e agora só tem uma. Ou seja, a comissão que era 2,5% passa para 2%, redução de 0,5%.

A comissão está toda integrada e não vai permitir reduzir o seu valor. Veja como o sistema se comporta.

O log do recalculo foi com aviso

Veja o detalhe do log

Se a parcela da comissão complementar não estivesse integrada, o sistema iria reduzir primeiramente das comissões complementares e depois da comissão, mas desde que estivessem em aberto a comissão.

Ao cancelar a integração de todas as parcelas de um comissão, automaticamente a comissão complementar é excluída, pois ela só existe porque a comissão estava integrada, como não está mais ele será cancelada e deverá recalcular a comissão após esse processo
