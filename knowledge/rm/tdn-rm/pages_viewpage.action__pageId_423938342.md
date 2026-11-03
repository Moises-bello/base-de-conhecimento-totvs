---
content_hash: 8cce6568e8d5ebadb5cabc85353cdf4c70be72f7f10390beb5ebc3b849d10588
fetched_at: '2026-06-29T00:09:26.627736+00:00'
page_id: '423938342'
product: rm
source: tdn-rm
title: Contabilização de Ocorrências - Acréscimo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938342
version: 3
---

Responsável pela contabilização dos acréscimos realizados nos patrimônios, este processo cria lançamentos contábeis de acordo com a parametrização definida no(s) evento(s) contábil(eis) de forma que, posteriormente, sejam enviados para o sistema contábil.

A contabilização do acréscimo em patrimônio(s) não será realizada nas seguintes situações:

* Patrimônios pertencentes a grupos de patrimônio que possuem cenários sem evento(s) contábil (eis) associado(s);
* Utilizar evento contábil que possui diferenças entre débitos e créditos. Está situação é definida nos itens do evento;
* Em patrimônios considerados títulos;
* Em patrimônios inativos;
* Alterar, diretamente na tela do processo de contabilização, a data do lançamento de forma que fique diferente à do acréscimo;
* Alterar, diretamente na tela do processo de contabilização, o valor do lançamento de forma que fique diferente ao da ocorrência de acréscimo;
* Ocorrência(s) já contabilizada(s) anteriormente;
* Ocorrência(s) definida(s) para não ser (em) contabilizada(s). Nesta situação o status da opção "Status da contabilização" deverá estar como "Não contabilizar".

**Passos para realização da contabilização da ocorrência de acréscimo**

Antes de contabilizar o acréscimo em patrimônio(s) deve-se verificar a existência de evento contábil, devidamente parametrizado. Este evento deverá ser classificado em "Classificação de Evento Contábil" como de acréscimo. Após a classificação do evento deve-se associá-lo ao grupo de patrimônio, grupo este que será, posteriormente, associado ao patrimônio durante sua inclusão.

**Observação** Os lançamentos contábeis serão criados respeitando as informações definidas no evento contábil associado ao cenário informado no grupo de patrimônio. Desta forma é fundamental que todos os passos citados até o momento sejam respeitados a fim de que a contabilização seja realizada corretamente.

A contabilização da ocorrência deverá ser definida durante o processo de acréscimo. Para isto deve-se marcar a opção "Contabilizar Ocorrência". Lembre-se que a contabilização não será realizada neste momento. Somente o acréscimo no patrimônio será executado.

Durante o processo de acréscimo no patrimônio caso deseje não realizar a contabilização do mesmo deve-se desmarcar a opção "Contabilizar Ocorrência". Uma vez executado o processo com esta opção desmarcada o sistema não permitirá que, posteriormente, seja realizada a contabilização desta ocorrência.

Ao executar o acréscimo, com a opção "Contabilizar Ocorrência" marcada, a ocorrência ficará com o status da contabilização como "Pendente". Desta forma a contabilização poderá ser executada a partir da tela de consulta de ocorrências realizadas em Operações Patrimoniais ou pela visão de ocorrências (em anexo) na tela de patrimônios cadastrados.

Na tela de contabilização de acréscimo será exibido o código e descrição do patrimônio (não pode ser alterado), a descrição do lançamento contábil, o número do documento, o código do histórico (histórico do lançamento) e seu complemento. Por default, a descrição do lançamento e o número do documento serão preenchidos, respectivamente, pelo código do patrimônio e o seu número de documento ficando estes campos livres para serem alterados.

Após o preenchimento dos campos citados anteriormente será exibido detalhes dos lançamentos contábeis. Este passo é extremamente importante, pois pode-se verificar se todos os dados da contabilização (tais como contas contábeis, valores e distribuição gerencial) estão de acordo com o evento contábil. Caso deseje refazer a contabilização antes de finalizar o processo, definindo outros dados para os lançamentos, deve-se informar outro evento contábil (na tela de edição da contabilização) e clicar na opção "Refaz Contabilização". Neste momento o lançamento existente será excluído e será criado um novo lançamento de acordo com o novo evento contábil informado.

**Observação**

Como medida de segurança exigida pelo sistema não será permitido que o valor e a data do lançamento sejam alterados.

Estando todos os dados corretos o processo deverá ser executado sendo que, ao seu final será exibido um log contendo todas as informações referentes a execução da contabilização do acréscimo.

**Visualizar contabilização do Acréscimo**

Ao realizar a contabilização do acréscimo no patrimônio com sucesso o status da contabilização da ocorrência será alterado para "Contabilizado". Os lançamentos contábeis poderão ser visualizados a partir da opção "Visualizar a Contabilização da ocorrência" editando a ocorrência existente em Operações Patrimoniais - Consulta/Cancela ou na visão de ocorrência (em anexos) da tela de patrimônios cadastrados.

**Desfazer a contabilização de ocorrências**

Caso seja necessário realizar a exclusão da contabilização do acréscimo no patrimônio deve-se selecionar a(s) ocorrência(s) contabilizada(s) e escolher a opção "Desfazer Contabilização" em Processos.

Processos

* Desfazer Contabilização
Veja Também

* Consulta de Ocorrências
* Operações Patrimoniais → Acréscimo
* Integrações → Integrar Contabilização
