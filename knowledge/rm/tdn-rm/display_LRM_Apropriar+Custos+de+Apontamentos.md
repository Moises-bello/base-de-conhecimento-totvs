---
content_hash: 7f7d379b5bd15f067f4f5c7d9324d1240610659580ecfa45edaa3df59589a066
fetched_at: '2026-06-29T00:09:14.067547+00:00'
page_id: '421385109'
product: rm
source: tdn-rm
title: Apropriar Custos de Apontamentos
type: documentation
url: https://tdn.totvs.com/display/LRM/Apropriar+Custos+de+Apontamentos
version: 7
---

---

Este processo efetua a apropriação de custos para o projeto, dos Ciclos de Transporte que foram obtidos via apontamentos de coletores móveis.  
A apropriação de custos se dá acessando o anexo de "Apontamentos Conciliados" disponível em Controle|Minha Obra|Ciclos de Transporte, selecionando os registros (apontamentos) que se deseja efetuar a apropriação e acionando o processo "Apropriar Custos de Apontamentos".  
O sistema verifica se dentre os registros selecionados existe algum com a situação de "Apropriado" ou "Pendente" e, em caso afirmativo, emite mensagem explicativa, abortando o processo. Em caso negativo, o sistema exibe no primeiro passo do processo a data e hora do último cálculo da curva ABC e a opção para cálculo da curva ABC. Caso a opção de cálculo seja selecionada a curva ABC será recalculada. O processo solicita que seja informado a obra/etapa/tarefa para os apontamentos. No lookup de tarefas somente serão exibidas tarefas que possuam como recurso (direto ou indireto) o insumo relacionado ao Ciclo de Transporte. Além disso, as tarefas exibidas deverão respeitar o parâmetro de projeto "Permite apropriar apenas serviço". Se o parâmetro estiver selecionado, poderão ser selecionadas apenas tarefas de último nível. Caso contrário, etapas e obras também poderão ser escolhidas. Com os dados informados, o sistema efetua os cálculos e faz a apropriação, o status dos registros apropriados são alterados para "Apropriado" e estes apontamentos não poderão mais ser alterados ou apropriados.

**Atenção:**

A apropriação não é um passo obrigatório e pode ser desabilitada via perfil e este deve ser o procedimento adotado caso deseje trabalhar somente com estatísticas (tiradas dos apontamentos dos coletores ou então dos apontamentos conciliados).  
Caso algum apontamento não possa ser apropriado devido a alguma regra interna de apropriação então o sistema não o processará, mas continuará o processamento do próximo registro. Tais apontamentos que apresentaram erro serão listados ao final do processo com suas respectivas mensagens de erro.  
O valor para a apropriação será calculado utilizando a distância do ciclo, preço do insumo, capacidade do bem, conforme previamente parametrizado no cadastro do ciclo.

A seguinte fórmula será utilizada: DISTÂNCIA (QUANTIDADE DO CICLO) \* PREÇO DO INSUMO \* CAPACIDADE DO BEM

A forma de acompanhamento do Ciclo de Transporte pode variar, dependendo da forma como o serviço foi contratado. Sendo que, em alguns casos, a capacidade do bem ou a distância podem não serem consideradas no cálculo do valor a ser apropriado. Esta definição será feita no cadastro do Ciclo. A capacidade do bem/equipamento está no Manutenção de Ativos e, via sincronização, será enviada ao Corpore/Bens. Qualquer alteração necessária na capacidade do bem deve ser feita no Manutenção de Ativos do Protheus e será refletida no Corpore.

Caso não deseje utilizar a capacidade de carga do bem no cálculo da apropriação, deve-se cadastrar o ciclo desconsiderando este campo. A mesma regra é válida para os casos em que não se deseja utilizar a distância no cálculo.

**Apropriando Custos de Apontamentos**

* Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Minha Obra \ Ciclos de Transporte \ Anexo \ Apontamentos Conciliados \ Processos \ Apropriar custos de apontamentos;

A apropriação de custos é realizada sempre com base em uma obra/etapa/tarefa e vale lembrar que os apontamentos de ciclos de transportes coletados e exportados para o ERP/TOP, em primeira instância, não estarão associados a uma destas tarefas.

Este processo contém uma interface do tipo “WIZARD” onde a primeira tela apresentará ao usuário data e hora do último cálculo da curva ABC e a opção para cálculo da curva ABC. Caso a opção de cálculo esteja selecionada a curva ABC será recalculada.

A segunda tela do processo exibe um controle para informar a tarefa na qual será realizada a apropriação dos apontamentos dos ciclos.

São exibidas tarefas que possuem como recurso direto ou indiretamente o insumo informado no cadastro de ciclo de transporte. Além disso, as tarefas exibidas devem respeitar o parâmetro de projeto “Permite apropriar apenas serviço”. Se parâmetro estiver selecionado, serão exibidas apenas selecionar tarefas de último nível. Caso contrário etapas e obras também poderão ser escolhidas. Dessa forma, a primeira tela se faz necessário para garantir que a curva ABC esteja atualizada, já que as tarefas a serem exibidas no segundo passo serão obtidas a partir da curva ABC de insumos.

Após confirmar a execução do processo o sistema efetua a apropriação somente dos apontamentos que ainda não foram apropriados. Apontamentos que tenham sido apropriados não são processados e o sistema os listará com uma mensagem explicativa ao final do processo.

Caso algum apontamento não possa ser apropriado devido a alguma regra interna de apropriação o sistema não o processará, mas continuará o processamento do próximo registro. Estes apontamentos que apresentarem erro serão listados ao final do processo com suas respectivas mensagens de erro.

Considerando que o apontamento é de um ciclo, que o ciclo de transporte possui a distância/quantidade e insumo, que o insumo tem seu valor por sua unidade e está associado a um bem e que o bem tem como um de seus atributos a capacidade.

O atributo “distância” do ciclo de transporte será informado no campo distância no cadastro do Ciclo de Transporte.

A capacidade do bem/equipamento, quando integrado com SIGAMNT do PROTHEUS, está no Manutenção de Ativos e, via sincronização, será enviada ao RM/Bens (no campo complementar **CAPACIDADEPROD,**conforme utilização da capacidade, descrita na aba que detalha o cadastro de Ciclo de transporte). Qualquer alteração necessária na capacidade do bem deve ser feita no Manutenção de Ativos do Protheus e será refletida no RM.

A forma de acompanhamento do Ciclo de Transporte pode variar, dependendo da forma como o serviço foi contratado. Sendo que, em alguns casos, a capacidade do bem ou a distância podem não serem consideradas no cálculo do valor a ser apropriado. Esta definição é feita no cadastro do Ciclo. Desta forma, o cálculo será flexível, parametrizado conforme o tipo de contratação do serviço;

**Importante:**

* + - **Ao se excluir uma apropriação no cadastro de Apropriação de Serviços/Insumos em que está apropriação esteja associada a algum apontamento conciliado, o apontamento conciliado terá seu status modificado de “Apropriado” para “Validado”;**
    - **A data atribuída à apropriação será a data do apontamento de saída (data inicial) do equipamento no ciclo.**

**Observação:**

Os apontamentos conciliados de Ciclos de Transporte aptos a terem seus custos apropriados ao projeto deverão estar com o status "Validado" o que indica que o mesmo já foi conferido e os valores de seus campos estão consistentes para gerarem a apropriação.   
Ao final do processo de apropriação será exibida uma mensagem ao usuário informando o sucesso ou erro na execução.
