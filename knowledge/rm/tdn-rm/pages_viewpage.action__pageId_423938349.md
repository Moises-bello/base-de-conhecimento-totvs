---
content_hash: fc2d212df390fd2742b54fa92ea05a1676af23ad909359118b77120ceaaf5156
fetched_at: '2026-06-29T00:09:26.647355+00:00'
page_id: '423938349'
product: rm
source: tdn-rm
title: Contabilização da Aquisição de Patrimônio 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938349
version: 2
---

Responsável pela contabilização dos patrimônios durante a sua aquisição, este processo cria lançamentos contábeis de acordo com a parametrização definida no(s) evento(s) contábil(eis) de forma que, posteriormente, sejam enviados para o sistema contábil.

A contabilização de aquisição de patrimônio(s) não será realizada nas seguintes situações:

* Patrimônios pertencentes a grupos de patrimônio que possuem cenários sem evento(s) contábil (eis) associado(s);
* Utilizar evento contábil que possui  diferenças entre débitos e créditos. Está situação é definida nos itens do evento;
* Em patrimônios considerados títulos;
* Em patrimônios inativos;
* Alterar, diretamente na tela do processo de contabilização, a data do lançamento de forma que fique diferente à da aquisição do patrimônio;
* Alterar, diretamente na tela do processo de contabilização, o valor do lançamento de forma que fique diferente ao da aquisição do patrimônio;
* Patrimônio(s) já contabilizado(s) anteriormente;
* Patrimônio(s) definido(s) para não ser (em) contabilizado(s). Nesta situação o status da opção "Contabilizar Aquisição" deverá estar como "Não contabilizar".

**Passos para realização da contabilização da aquisição**

Antes de contabilizar a aquisição de patrimônio(s) deve-se verificar a existência de evento contábil, devidamente parametrizado. Este evento deverá ser classificado em "Classificação de Evento Contábil" como de aquisição. Após a classificação do evento deve-se associá-lo ao grupo de patrimônio, grupo este que será, posteriormente, associado ao patrimônio durante sua inclusão.

**Observação**

Os lançamentos contábeis serão criados respeitando as informações definidas no evento contábil associado ao cenário informado no grupo de patrimônio. Desta forma é fundamental que todos os passos citados até o momento sejam respeitados a fim de que a contabilização seja realizada corretamente.

Durante a inclusão do patrimônio caso deseje não contabilizar a aquisição do mesmo deve-se desmarcar a opção "Contabilizar aquisição". Uma vez cadastrado o patrimônio com esta opção desmarcada o sistema não permitirá que, posteriormente, seja realizado o processo de contabilização de aquisição.

Ao marcar a opção "Contabilizar aquisição" durante a inclusão do patrimônio será exibido uma mensagem onde se poderá escolher em contabilizar durante o cadastro do mesmo ou deixar a contabilização pendente.

Na tela de contabilização de aquisição será exibido o código e descrição do patrimônio (não pode ser alterado), a descrição do lançamento contábil, o número do documento, o código do histórico (histórico do lançamento) e seu complemento.

Por default, a descrição do lançamento e o número do documento serão preenchidos, respectivamente, pelo código do patrimônio e o seu número de documento ficando estes campos livres para serem alterados.

Após o preenchimento dos campos citados anteriormente será exibido detalhes dos lançamentos contábeis. Este passo é extremamente importante, pois pode-se verificar se todos os dados da contabilização (tais como contas contábeis, valores e distribuição gerencial) estão de acordo com o evento contábil.

Caso deseje refazer a contabilização antes de finalizar o processo, definindo outros dados para os lançamentos, deve-se informar outro evento contábil (na tela de edição da contabilização) e clicar na opção "Refaz Contabilização". Neste momento o lançamento existente será excluído e será criado um novo lançamento de acordo com o novo evento contábil informado.

**Observação**

Como medida de segurança exigida pelo sistema não será permitido que o valor e a data do lançamento sejam alterados. Estando todos os dados corretos o processo deverá ser executado sendo que, ao seu final será exibido um log contendo todas as informações referentes a execução da contabilização da aquisição. 

**Visualizar contabilização da aquisição**

Ao realizar a contabilização da aquisição do patrimônio com sucesso o status do campo "Contabilizar Aquisição" será alterado para "Contabilizado". Os lançamentos contábeis poderão ser visualizados a partir da opção "Visualizar contabilização da aquisição" editando o cenário existente em "Cenários para cálculos" na visão de patrimônios.

**Desfazer a contabilização de aquisição**

Caso seja necessário realizar a exclusão da contabilização de aquisição do patrimônio deve-se selecionar o(s) patrimônio(s) contabilizados e escolher a opção "Desfazer contabilização de aquisição" em Processos.

Como fazer

* Desfazer contabilização de aquisição
Veja também

* Cadastro - Patrimônio
