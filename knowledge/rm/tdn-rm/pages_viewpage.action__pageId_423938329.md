---
content_hash: b022381cba7f7b643a7ff4164c7202eb3b481a7816ef77f063f4ab0882442668
fetched_at: '2026-06-29T00:09:26.599862+00:00'
page_id: '423938329'
product: rm
source: tdn-rm
title: Contabilização da Transferência de Controle
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938329
version: 4
---

Responsável pela contabilização de Transferência de Controle realizada nos patrimônios, este processo cria lançamentos contábeis de acordo com a parametrização definida no(s) evento(s) contábil (eis)  de forma que, posteriormente, sejam enviados para o sistema contábil. A contabilização de Transferência de Controle em patrimônios não será realizada nas seguintes situações:

* Patrimônios pertencentes a grupos de patrimônio que possuem cenários sem evento(s) contábil (eis) associado(s);
* Utilizar evento contábil que possui diferenças entre débitos e créditos. Está situação é definida nos itens do evento;
* Em patrimônios considerados títulos;
* Em patrimônios inativos;
* Alterar, diretamente na tela do processo de contabilização, a data do lançamento de forma que fique diferente à da Transferência de Controle;
* Alterar, diretamente na tela do processo de contabilização, o valor do lançamento de forma que fique diferente ao da ocorrência de Transferência de Controle;
* Transferência(s) já contabilizada(s) anteriormente.

**Passos para realização da contabilização da Transferência de Controle**

Antes de contabilizar a Transferência de Controle em patrimônio(s) deve-se verificar a existência de evento contábil, devidamente parametrizado. Este evento deverá ser classificado em  como de Transferência de Controle. Após a classificação do evento deve-se associá-lo ao grupo de patrimônio, grupo este que será, posteriormente, associado ao patrimônio durante sua inclusão.

**Observação**

Os lançamentos contábeis serão criados respeitando as informações definidas no evento contábil associado ao cenário informado no grupo de patrimônio. Desta forma é fundamental que todos os passos citados até o momento sejam respeitados a fim de que a contabilização seja realizada corretamente.

Se o parâmetro "Contabilizar Transferência de Controle" estiver marcado nos parâmetros de Integração Contábil do sistema será exibido no processo de Transferência de Controle um CheckBox para que o marque caso deseje que essa operação seja contabilizada. A contabilização não ocorre automaticamente se o parâmetro estiver marcado. Ele somente habilita essa possibilidade.

A contabilização da transferência deverá ser definida durante o processo de Transferência de Controle. Para isto deve-se marcar a opção "Contabilizar Transferência". Lembre-se que a contabilização não será realizada neste momento. Somente a Transferência de Controle do patrimônio será executada.

Durante o processo de Transferência de Controle do patrimônio caso deseje não realizar a contabilização do mesmo deve-se desmarcar a opção "Contabilizar Transferência". Uma vez executado o processo com esta opção desmarcada o sistema não permitirá que, posteriormente, seja realizada a contabilização desta transferência.

Ao executar a Transferência Monetária, com a opção "Contabilizar Transferência" marcada, a ocorrência ficará com o status da contabilização como "Pendente". Desta forma a contabilização poderá ser executada a partir da tela de Consulta de Transferência de Controle realizadas no menu Operações Patrimoniais.

Na tela de contabilização de Transferência de Controle, exibida após selecionar a transferência (na tela de consulta de Transferência de Controle), ao acessar Processos/Contabilização da Transferência de Controle serão exibidas informações sobre o(s) patrimônio(s) que foi transferido tais como o código, a descrição, as filiais, centros de custo e departamentos de origem e destino. Na próxima tela tem-se a descrição do lançamento contábil, o número do documento, o código do histórico (histórico do lançamento) e seu complemento. Por default, a descrição do lançamento e o número do documento serão preenchidos, respectivamente, pelo código do patrimônio e o seu número de documento ficando estes campos livres para serem alterados.

Após o preenchimento dos campos citados anteriormente será exibido detalhes dos lançamentos contábeis. Este passo é extremamente importante, pois pode-se verificar se todos os dados da contabilização (tais como contas contábeis, valores e distribuição gerencial) estão de acordo com o evento contábil.

**Observação**

Caso no evento contábil esteja definido que a "Origem da Conta" buscará o default em "Conta do Processo de Contabilização", antes de visualizar os lançamentos contábeis será exibida uma tela onde devem ser informadas as contas contábeis de acordo com cada item existente no evento.

**Exemplo**

Se no evento existem dois itens, um a débito que aplica o item na Depreciação Acumulada (Patrimônio de Origem) e outra a crédito que aplica o item na Depreciação Acumulada (Patrimônio de Destino) e ambos com a opção "Buscar default em" "Conta do Processo de Contabilização", na tela de contabilização da Transferência de Controle será exibida uma tela onde deverão ser informadas as contas contábeis (a débito e a crédito) referentes a cada item.

Caso deseje refazer a contabilização antes de finalizar o processo, definindo outros dados para os lançamentos, deve-se informar outro evento contábil (na tela de edição da contabilização) e clicar na opção "Refaz Contabilização". Neste momento o lançamento existente será excluído e será criado um novo lançamento de acordo com o novo evento contábil informado.

**Observação**

Como medida de segurança exigida pelo sistema não será permitido que o valor e a data do lançamento sejam alterados. Estando todos os dados corretos o processo deverá ser executado sendo que, ao seu final será exibido um log contendo todas as informações referentes a execução da contabilização da Transferência de Controle.

**Visualizar contabilização da Transferência de Controle**

Os lançamentos contábeis poderão ser visualizados a partir da opção "Visualizar Contabilizações" no menu Contabilização/Contabilização Patrimonial.

**Desfazer contabilização da Transferência de Controle**

Caso seja necessário realizar a exclusão da contabilização da Transferência de Controle dos patrimônios deve-se selecionar o histórico da transferência (na tela de Consulta de Transferência de Controle) e escolher a opção "Desfazer Contabilização" em Processos.

Como fazer

* Desfazer Contabilização
Veja também

* Consulta de Transferência de Controle
