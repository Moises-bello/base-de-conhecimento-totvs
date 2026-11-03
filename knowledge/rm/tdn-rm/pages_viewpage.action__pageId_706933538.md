---
content_hash: b068b03335356ffae7c98b4f8028eb9ad2c1f87df0fbae0d28f96b0ecac1179e
fetched_at: '2026-06-29T00:11:23.091041+00:00'
page_id: '706933538'
product: rm
source: tdn-rm
title: Criar Planilha de Atividades a partir de Serviços
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=706933538
version: 8
---

---

Com o objetivo de facilitar a criação da [Planilha das Atividades](https://tdn.totvs.com.br/pages/viewpage.action?pageId=421385087) que serão executadas no Projeto, foi desenvolvida a possibilidade de criá-la a partir do orçamento da [Planilha de Serviço](https://tdn.totvs.com.br/pages/viewpage.action?pageId=421385525).

Para a geração da Planilha de Atividades é imprescindível que o projeto utilize Planilha de Serviço, e para isso o [Parâmetros de Projeto (F6)](https://tdn.totvs.com/pages/releaseview.action?pageId=421385183) **"Utiliza Planilha de Serviço"** deve estar habilitado.

O processo encontra-se no menu**Orçamento | Planilha | Planilha de Serviços (ou atalho F11) | Processos | Criar Planilha de Atividades a partir de Serviços**:

Na tela inicial do Wizard serão apresentados, no canto superior direito, os botões que direcionam o usuário para a documentação do processo e para o vídeo tutorial, que poderão auxiliar em caso de dúvidas:

Na sequência, é possível visualizar as informações dos [Parâmetros de Projeto](https://tdn.totvs.com/pages/releaseview.action?pageId=421385183) que já são aplicados na associação entre as planilhas de serviço e atividades, que são:

* **Tipo de vínculo entre Serviço e Atividade:** Qual a grandeza será utilizada, Percentual ou Quantidade;
* **Recursos iguais entre Tarefas Vinculadas:**Para que os Recursos da Planilha de Serviços e Planilha de Atividades estejam idênticos quando é realizado o vinculo. Uma vez habilitado o Parâmetro **Recursos iguais entre Tarefas Vinculadas,**o sistema iguala e bloqueia a edição de Recursos da Planilha de Atividades, caso o parâmetro esteja desabilitado o sistema permitirá ainda na tela do processo fazer alterações no Recurso da Planilha de Atividades;
* **Permitir editar a quantidade na associação de Serviços à Atividade:**Para editar a quantidade na associação de Serviços a Atividades. Caso o parâmetro **Permitir editar a quantidade na associação de Serviços à Atividade**esteja habilitado, o sistema permitirá a edição da quantidade associada entre as Planilhas durante a execução do processo, permitindo assim, associar a quantidade a mais de uma tarefa; caso o mesmo esteja desabilitado, o sistema irá vincular a quantidade total do Serviço à tarefa e não será possível editar;
* **Onde será permitido alterar o recurso:** em qual planilha a edição do recurso estará liberada;

Caso seja necessário conferir ou alterar algum desses parâmetros, basta clicar no link em azul e a tela será carregada:

Ainda na tela inicial do Wizard será possível escolher:

* **Vincular Serviço na Atividade:** Caso queira criar a Planilha de Atividades vinculada ou não aos seus respectivos Serviços;

Todos estes parâmetros irão definir o comportamento durante a execução do processo. assim ao clicar em avançar, serão apresentados todos os serviços do projeto do lado esquerdo:

A partir da planilha de serviços, o usuário tem as seguintes possibilidades, através dos 3 botões azuis existentes no centro da tela: **Criar Obra/Etapa** , **Criar ou Associar** e **Desmembramento de Tarefas**:

* **Criar Obra/Etapa:** Esse botão permite criar Obras ou Etapas, existentes ou não na planilha de Serviços, para a Planilha de Atividades. Selecionando uma Obra/Serviço do lado esquerdo e clicando nesse botão,  serão copiados para o lado direito. Apenas Obras/Etapas. Caso não selecione, será dada a oportunidade de cadastrar, uma Obra/Etapa inexistente na planilha de atividades:

A Obra/Etapa poderá ser visualizada na tela do lado direito, que traz uma Pré-visualização da Planilha de Atividades que será criada após a execução do Processo:

* **Criar ou Associar:** este botão permite criar tanto obra/etapa quanto atividades a partir de um registro existente na planilha de serviços. Ao selecionar os registros e clicar neste botão, os mesmos serão replicados com mesmo código, caso não existam ainda na planilha de atividades. Caso existam, o código será gerado na sequência da hierarquia informada. Os serviços terão seu saldo total ou parcial associados às respectivas atividades criadas.

No exemplo abaixo, todos os serviços foram selecionados na planilha de serviços e ao clicar em Criar ou Associar, automaticamente todas as Obras/Etapas são copiadas. Para as tarefas, é apresentada a tela de confirmação:

Essa tela traz o saldo em quantidade do serviço que está disponível para associação e oferece ao usuário a possibilidade de alterar a quantidade que será associada à atividade criada (dependendo do parâmetro do projeto):

O primeiro checkbox serve para sinalizar caso o usuário queira Utilizar toda grandeza disponível, assim o campo será bloqueado com a grandeza total.

O segundo, é um facilitador para quando o usuário desejar usar o saldo disponível ou a mesma quantidade informada para todas as tarefas assinaladas na sequência, caso contrário, a mesma tela se repetirá para cada serviço:

Ao clicar em criar atividades, o usuário poderá conferir como ficará a planilha de atividades ou alterá-la, antes de concluir o processo:

Quantidade Associada

O somatório das quantidades associadas de um Serviço em N Atividades, não pode ser superior a quantidade total do Serviço. Caso o usuário queria, ele poderá a qualquer momento alterar a quantidade da Atividade, alterando consequentemente a quantidade associada. Vale destacar que ao alterar a quantidade de uma atividade deverá recalcular o percentual do PERT.

Caso tente associar uma quantidade maior que a capacidade do Serviço o sistema irá validar:

Para associar um serviço que possui saldo, a uma ou mais atividades existentes, basta selecionar o serviço e as devidas atividades do lado direto:

E clicar no botão Associar Serviço, uma nova tarefa terá sido associada a atividade, bastando expandir a visão dos serviços associados:

Ao excluir um serviço associado na tela de pré-visualização da planilha de atividades, o vínculo existente entre o serviço e atividades será desfeito:

E o saldo retornará para o serviço em questão, como é possível ver comparando a coluna Saldo (Qtd.) das duas telas, acima e abaixo:

Da mesma forma é possível excluir uma ou mais atividades antes da execução do processo:

* **Desmembramento de tarefas:** Através desse botão é possível desmembrar um serviço em mais de uma atividade, por Local de serviço da unidade informada. Basta informar o percentual de distribuição para cada local e a quantidade ou % que será desmembrado Há ainda a possibilidade de durante o processo, informar dados para o PERT e agregar Unidade e Local de serviço no Nome/Descrição da Tarefa :

Ao clicar em Ok o desmembramento pode ser conferido na Pré-Visualização:

Ao finalizar a criação da planilha de atividades na tela de Pré-Visualização, basta clicar em Avançar, e será exibido um resumo das atividades que serão criadas e seus vínculos:

E ao concluir o processo, é possível visualizar todas as tarefas criadas na planilha de atividades:

E conferir seus respectivos vínculos:

---
