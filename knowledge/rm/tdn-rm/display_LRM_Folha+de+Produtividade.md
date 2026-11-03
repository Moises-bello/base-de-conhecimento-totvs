---
content_hash: 40ba0815d6d824a85c43810b9857ca7a0bc93fc07f2dd147c1e626f64152666a
fetched_at: '2026-06-29T00:09:58.182701+00:00'
page_id: '451267530'
product: rm
source: tdn-rm
title: Folha de Produtividade
type: documentation
url: https://tdn.totvs.com/display/LRM/Folha+de+Produtividade
version: 40
---

---

Com o intuito de melhor distribuição do custo da mão de obra na execução das tarefas existe a Folha de Produtividade, onde o cálculo do valor para cada membro da equipe associada a Folha Tarefa considera a importância (peso) que cada membro tem para a equipe.

Foi criado em Projeto | Construção e Projetos | Gerais, os Campos Unidade de Serviço e Local de Serviço, possibilitando a parametrização do nome.

Exemplo:

A**Unidade de Serviço**, pode ser utilizada para descriminar as Torres de um Prédio.

O **Local de Serviço**, pode ser utilizado para descriminar os andares de um Prédio. Os registros dessa tabela são específicos para cada unidade de serviço, por isso deve ser identificado qual unidade ele pertence, isso porque cada unidade por ter locais distintos (ex: Torre 1 tem 20 andares, e a Torre  2 tem 10 andares).

A funcionalidade está disponível no TOTVS Obras e Projetos, Cad. Gerais, de acordo com o nome parametrizado.

Ao acessar a funcionalidade, é possível incluir uma Unidade de Serviço.

Após cadastrar a Unidade de Serviço, o cadastro de Local de Estoque fica disponível em Anexos.

Através do processo de "**Copiar Local de Serviço"** é possível incluir uma determinada Unidade de Serviço destino os Locais de Serviços desejados. Esse processo encontra-se presente na opção de Processos do cadastro de Unidade de Serviço para sua execução é necessário selecionar algumas informações de origem como a Coligada, o Projeto e a Unidade de Serviço, assim serão exibidos os Locais de Serviços existentes, e ao executar, os mesmos serão incluídos nas Unidades selecionadas na visão principal. Somente serão incluídos os Locais que não tem seu código equivalente à um já existente na Unidade destino.

**Observação:**

Para acessar a funcionalidade, é necessário Permissão de Acesso.

* Os dados de Unidades de Serviço e Locais de Serviço também estão presentes no Backup/Restore de Projetos, nas Revisões de Projeto, tanto simples quanto múltipla;
* Para tarefas que tem associado Unidade ou Local, ao realizar Cópia de Itens, a associação será desfeita, pois o processo não copia Unidade e Local de serviço.

**Unidade e Local de Serviço na Tarefa**

Nas Planilhas de Atividades e [Serviço](http://tdn.totvs.com/pages/viewpage.action?pageId=421385525) é possível associar a [Unidade e Local de Serviços](http://tdn.totvs.com/pages/viewpage.action?pageId=451251865) em uma determinada tarefa. Na tela de edição da tarefa, na aba "Outros" existe dois lookups, o de Unidade de Serviço e de Local de Serviço, onde para definir o Local é necessário o preenchimento da Unidade.

Através do processo de Atualização Múltipla de Registros também é possível alterar a Unidade e Local de Serviço para várias tarefas ao mesmo tempo, basta selecionar a opção em "Campo" e definir a Unidade e Local.

**Desmembramento de Tarefa**

Existe um processo na Planilha de Atividades onde será permitido o desmembramento de uma tarefa em vários locais de serviço.

Através do processo Desmembrar Tarefas da Planilha de Atividades é possível desmembrar uma atividades ligadas a um locais de serviço e uma [Equipe do Projeto](http://tdn.totvs.com/display/LRM/Equipe+de+Mobilidade).

Após a execução do processo a tarefa selecionada irá se transformar uma etapa e será criada uma nova atividade para a tarefa original e novas atividades para cada Local de Serviço com os campos de Unidade de Serviço, Local de Serviço e Equipe preenchidos.

Exemplo:

Processo executado

* **Itens da Folha Tarefa:**Para esse tipo de folha, a associação de Tarefas à mesma, deve obedecer algumas regras que não são consideradas no tipo de folha tarefa "Padrão":

A quantidade desmembrada será dividida igualmente entre as novas tarefas criadas para cada local de serviço selecionado. Ficando o restante para a tarefa original.

O valor de Mão Obra da Tarefa se refere aos valores dos insumos de Natureza "Mão de Obra", onde esses valores não tem a incidência de Leis Sociais.

Através da opção "Adicionar descrição da Unidade de Serviço e Local de Serviço na descrição da(s) tarefas(s) criada(s)" a descrição das tarefas que serão resultado do desmembramento receberá a concatenação das descrições de Unidade e Local de Serviço. Essa opção somente estará disponível se o parâmetro de projeto "Igualar Descrição/Nome da tarefa a Descrição do recurso que está sendo associado" não estiver marcado.

Caso o processo seja executado novamente para a tarefa original, não será criada uma nova etapa. Neste caso apenas será criado uma nova atividade para cada local de serviços.

Através do desmembramento é possível definir informações para o PERT e cronograma para as tarefas que serão criadas, basta definir a Nova Data Início e a Nova Duração, sendo que essas informações são Data Inicio Programada e Duração da tarefa selecionada, os Dias de Folga e a opção de Sequenciar Datas de Início das Tarefas caso deseje. Ao executar o processo, as tarefas criadas terão suas datas de início programada alteradas, assim como a duração, e no caso de sequenciar as datas das mesmas, serão incluídas as predecessoras em relação à cada tarefa criada, considerando a folga (defasagem).

Se a opção "Criar uma Folha Tarefa de Produtividade para cada Tarefa desmembrada" estiver marcada, serão criadas novas Folhas Tarefas com as respectivas novas tarefas associadas com o valor alocado de acordo com o desmembramento. Para definir o Valor Alocado do item da folha tarefa, existem duas possibilidades, a primeira sem a opção "Recalcular projeto antes de criar as Folhas Tarefas" que calcula a partir do valor unitário da tarefa origem vezes a quantidade da nova tarefa criada, a segunda possibilidade, esta com a opção de recalcular o projeto marcada, busca o valor de mão de obra da tarefa criada, porém é realizado o cálculo do projeto após a criação das tarefas para que o valor possa ser resgatado.

**Observação:** O processo de Desmembramento de Tarefa não está disponível para a Planilha de Serviços.

**Equipes para Folha de Produtividade**

No cadastro de Tarefas na Planilha de Atividades, é possível associar uma Equipe de Mobilidade à uma tarefa, através da edição da própria tarefa ou através da Atualização Múltipla de Registros.

No cadastro do membro dessa equipe de mobilidade, é possível definir o peso de cada funcionário que trabalha na equipe, onde esse valor será, posteriormente, utilizado no cálculo do pagamento da folha para definir o quanto o funcionário vai receber. O utilização do peso é para que ao acrescentar novos funcionários à equipe, o sistema calculará o percentual de cada membro em relação ao total, assim como mostra o exemplo abaixo:

Ex.:

Ao cadastrar um membro na equipe de mobilidade, no qual a mesma será utilizada para alocá-los em um Folha Tarefa de Produtividade, é possível definir se o mesmo estará presente em mais de um equipe, basta marcar a opção "Atua em mais de uma equipe". Com essa opção marcada, será possível permitir que uma membro possa ser incluído em mais de uma equipe, sendo que este mesmo membro somente poderá estar em apenas uma equipe com essa opção desmarcada. Essa característica se faz necessária em casos em que o funcionário precisa atuar em diferentes frentes de trabalho e em diferentes tarefas que necessitam da sua presença.

**Campos Complementares de Folha Tarefa**

Foi criado a opção de Campo Complementar para Folha Tarefa.

Estes campos seguem o padrão para os outros Campos Complementares existentes hoje no sistema.

**Pacote de Serviço**

O cadastro do Pacote de Serviço é realizado no cadastro da Folha Tarefa, onde a mesma pode assumir dois tipos distintos, o tipo **"Padrão"**, que é o tipo já conhecido e utilizado no Minha Obra, e o tipo **"Produtividade"**, que se refere ao pacote de serviços, e faz com que a Folha Tarefa assuma algumas características específicas:

* Ao selecionar o tipo da Folha Tarefa como Produtividade, além da Descrição e Tipo de Apontamento é necessário preencher a equipe do Pacote de Serviço;
* Não é necessário preencher a Periodicidade e Datas de Início e Fim, essas serão preenchidas automaticamente como **Personalizada**, **Data Inicial do Projeto** e **Data Final do Projeto** respectivamente;
* Anexos e Processos que não estão disponíveis para esse tipo de folha:
  + Programado X Alocado;
  + Alocação de Mão de Obra;
  + Equipes Associadas à Folha Tarefa;
  + Recalcular Planejamento das Tarefas;
  + Alocar Mão de Obra na Folha Tarefa.
* **Itens da Folha Tarefa:**Para esse tipo de folha, a associação de Tarefas à mesma, deve obedecer algumas regras que não são consideradas no tipo de folha tarefa "Padrão":

* No lookup da tarefa é possível filtrar por Unidade de Serviço, o Local de Serviço e/ou a Equipe no qual a Tarefa está associada;
* As Tarefas que são exibidas são aquelas que ainda possuem saldo e que ainda não foram iniciadas, e uma tarefa considerada não iniciada deve ter as seguintes características:
  + Não ter sido apropriada;
  + Não ter realizado no cronograma;
  + Não ter medido no cronograma;
  + Não ter apontamento de folha tarefa;
  + Não ter medição de contrato.
* O valor de Mão Obra da Tarefa se refere aos valores dos insumos de Natureza "Mão de Obra", onde esses valores não tem a incidência de Leis Sociais;
* É necessário definir o Valor Alocado para a Tarefa na Folha de Produtividade. Ao defini-lo o saldo disponível de Mão de Obra da tarefa em relação ao seu valor total de Mão de Obra da mesma é recalculado.
* A Quantidade Planejada poderá ser independente do Valor Alocado.
* Para que o Valor Alocado ou a Quantidade Planejada sejam calculados proporcional ao outro, deve-se limpar o campo que o mesmo será automaticamente recalculado.
* Ao salvar o registro o Valor Alocado de todas as tarefas da folha são somados e distribuídos entre os membros da equipe associada à folha tarefa, onde o cálculo considera o peso definido no cadastro do membro, como por exemplo:
  + Total Alocado dos itens da folha = 500,00
  + Membros da equipe:
    - JOSÉ: Peso = 3
    - JOÃO: Peso = 1
    - MARIA: Peso = 1
  + Distribuição dos valores:
    - JOSÉ: 60% x 500,00 = 300,00
    - JOÃO: 20% x 500,00 = 100,00
    - MARIA: 20% x 500,00 = 100,00

* **Validações:**
  + Processo de Drag and Drop não é permitido para esse tipo de folha;
  + O Valor Alocado não pode ser maior que o valor da tarefa ou o saldo;
  + O Valor Alocado não pode ser menor ou igual a zero.
* Se o projeto **utilizar apontamentos com os itens da planilha executiva,** o valor alocado será obtido do valor de mão de obra das tarefas vinculadas a esses itens, considerando o percentual associado, como por exemplo:
  + Planilha Executiva:
  + Item 1 Tarefas vinculadas:
    - Tarefa 1 = Vinculada ao item com 50%, valor de mão de obra 5.000,00.
    - Tarefa 2 = Vinculada ao item com 50%, valor de mão de obra 3.000,00.
  + Ao associar o Item 1 na folha de tarefa, o valor alocado de mão de obra será de 4.000,00, pois apenas 50% de cada tarefa foi vinculado, resultando na soma da metade dos valores.

**Processo de Associar Tarefas (Itens) na Folha Tarefa:**Para esse tipo de folha,  o processo de associar de Tarefas à mesma, deve obedecer as mesmas regras do anexo e que também não são consideradas no tipo de folha tarefa "Padrão":

* Na tela do processo, também é possível definir alguns filtros para a seleção da Tarefa desejada, a Unidade de Serviço, o Local de Serviço e/ou a Equipe no qual a Tarefa está associada;
* As Tarefas que são exibidas são aquelas que ainda possuem saldo e que ainda não foram iniciadas, assim como no anexo;
* O valor de Mão Obra da Tarefa se refere aos valores dos insumos de Natureza "Mão de Obra", onde esses valores não tem a incidência de Leis Sociais;
* Também é necessário definir o Valor Alocado e a Quantidade Planejada para a Tarefa na Folha de Produtividade, basta editar o valor no grid da respectiva coluna;
* Para que o Valor Alocado ou a Quantidade Planejada sejam calculados proporcional ao outro, deve-se limpar o campo que o mesmo será automaticamente recalculado;
* Na página seguinte da tela, são apresentados os membros da equipe da folha com os valores alocados distribuídos entre os membros da equipe associada à folha tarefa, onde o cálculo também considera o peso definido no cadastro do membro;
* Se o projeto utilizar apontamentos com os itens da planilha executiva, o valor alocado será obtido do valor de mão de obra das tarefas vinculadas a esses itens, considerando o percentual vinculado, como por exemplo:  
     Planilha Executiva: **Item 1**

                 Tarefas vinculadas:  
                   **Tarefa 1** = Vinculada ao item com **50%**, valor de mão de obra **5.000,00**.  
                   **Tarefa 2** = Vinculada ao item com **50%**, valor de mão de obra **3.000,00**.           Ao associar o **Item 1** na folha de tarefa, o valor alocado de mão de obra será de **4.000,00**, pois apenas **50%** de cada tarefa foi vinculado, resultando na soma da metade dos valores.

A distribuição dos valores dos membros leva em consideração todas as tarefas associadas à folha, não somente as definidas na tela do processo.

Caso o usuário deseja informar um valor/quantidade maior que o saldo da tarefa será permitido através da permissão Permitir Alocar Grandeza maior que o Saldo da Mão de Obra disponível.

**Membros de Folha Tarefa**

Para que o pagamento dos funcionários de uma Folha de Produtividade possa ser processado, é necessário que os membros estejam associados à Folha Tarefa do tipo Produtividade. Para isso, existe o anexo de "Membros de Folha Tarefa", onde é possível alocar os funcionários à uma determinada folha. A inclusão do membro pode ser realizada através de três formas diferentes:

* Para folhas de tarefa do tipo "**Produtividade**", é possível adicionar membros a qualquer momento, desde que a folha não esteja com status de "**Cancelada**" ou "**Encerrada**".
* Através da inclusão da tela de edição: Necessário informar o Funcionário e a Data de Inclusão sendo que o Peso e Valor são opcionais. O membros sempre será incluído com a situação de Ativado.
* Através do processo de Incluir Membros na Folha Tarefa: Através da seleção da equipe os membros da mesma são exibidos, onde é possível editar o Valor e o Peso, este, vindo do cadastro de membros de equipe. Também é possível informar a data de inclusão e selecionar somente o membros ativos na equipe. Ao executar o processo os membros serão associados à folha tarefa e será registrado no histórico.
* Através da tela de edição da própria folha tarefa, sendo que essa opção somente estará disponível no momento de criar uma nova folha e não na edição da mesma. É possível realizar a inclusão de um funcionário avulso ou de membros de uma determinada equipe.

No anexo de membros de folha tarefa existe o processo de Ativar/Desativar Membros da Folha Tarefa, onde é possível alterar o situação de Ativo do membro. Além da ação, é possível definir a data no qual essa ação será considerada, pois essas informações serão registradas como histórico do membro da folha para que possa ser utilizada no momento de gerar o pagamento para a folha de produtividade. As opções de Ativar e Desativar estarão habilitadas de acordo com as linhas selecionadas na visão de membros da folha tarefa, isto é, se somente ativos estiverem selecionados, apenas a opção de desativar estará disponível, e vice e versa.

Pagamento por Produtividade

---
