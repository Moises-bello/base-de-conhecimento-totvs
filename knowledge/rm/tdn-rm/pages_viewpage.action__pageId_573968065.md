---
content_hash: 7fd4172f694523fc7affd0f7ea3e602de0acdfb29f30accd482afe6d160a5ba1
fetched_at: '2026-06-29T00:10:52.993248+00:00'
page_id: '573968065'
product: rm
source: tdn-rm
title: Processos Farmacêuticos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=573968065
version: 28
---

1. **Visão Geral**
2. **Dispensar Pacote**
3. **Criar Devolução**
4. **Receber Devolução**
5. **Devolução Iniciada - Desdobramentos**
6. **Concorrência de Acessos**
7. **Impressão do Pacote**
8. **Excluir Requisição (Pacote com Devolução Iniciada)**

falsepaineltrueVisão Geral

## **01. VISÃO GERAL**

Os “Processos Farmacêuticos” possuem fluxos distintos na Enfermagem e na Farmácia.

Segue abaixo os 2 menus onde trataremos estes processos:

### 1 Cuidados com o Paciente > Processos Farmacêuticos

Duas ações podem ser executadas pela Enfermagem, através dos botões abaixo:

### 2 Farmácia > Processos Farmacêuticos

Três ações podem ser executadas pela Farmácia, através dos botões apresentados abaixo:

O painel apresenta um filtro para o usuário acompanhar por status:   

Caso o usuário sinta necessidade, há um temporizador para que a tela seja atualizada a cada intervalo escolhido:

Dispensar pacote

## **02. DISPENSAR PACOTE**

A tela de dispensar pacote só pode ser acessada caso a requisição não esteja sendo usada por outro usuário, e também, caso o status seja "Processado". Como é mostrado abaixo:

Ao clicar no botão dispensar pacote a seguinte tela é apresentada:

Também pode ser acessada através de: Processos->Entregar pacote.

Comportamento do parâmetro **Utiliza fluxo de recebimento da enfermagem** da Unidade de Atendimento:

* Caso esteja **habilitado** o status do pacote será **Entregue** para Farmácia e **Agurdando recebimento** para a Enfermagem.
* Caso esteja **desabilitado** o status do pacote será **Entregue** para Farmácia e **Recebido** para a Enfermagem.

Ações:

1. Há possibilidade de bipar pacote, ou então abrirão os pacotes que foram selecionados na tela anterior.
2. Pode bipar o crachá do responsável pela retirada do pacote. Deverá ter permissão para retirada. Pode-se permitir de acordo com perfis, quais usuários poderão ser responsáveis por retirada de pacotes.
3. Para dispensar pacote basta clicar no botão "Dispensar pacote"
4. Para cancelar a ação basta clicar em "Cancelar"

Criar devolução

## **03. CRIAR DEVOLUÇÃO**

Na tela de Farmácia > Processos Farmacêuticos existe um botão chamado **Criar devolução**, essa tela serve para que Farmácia a realize a devolução de medicamentos e materiais.

Existe uma permissão que define quais usuários devem ter o acesso a essa funcionalidade.  
Vá até **Serviços Globais > Segurança > Acesso > Perfis,**após isso, vá até **Acesso a Menus.**

Exitem duas formas de incluir itens na devolução:

Devolução via código do pacote

Após informar código do pacote todos os itens serão adicionados.

Somente os pacotes com o status de Processado e Entregue podem ser devolvidos, além disso, os itens utilizados em uma devolução não poderão ser utilizados em outra.

Não será possível adicionar mais de um pacote em uma mesma devolução.

Caso o pacote selecionado não possa ser utilizado, as mensagens de alerta aparecerão abaixo do campo onde é informado o código.

Devolução via nome do paciente

Nesta opção devem ser informados o paciente (deve possuir um atendimento parcial em aberto), o produto, o lote (caso necessário) e a quatidade.

Será possível também informar o código de barras do produto.

Após clicar no botão **Devolver** e este produto estiver habilitado para devolução, o item será adicionado.

Os próximos são preencher o motivo, a data/hora, o responsável pela devolução que deverá ter a respectiva permissão.

Sugestão da Data da Devolução

A Data/Hora da devolução será sugerida automaticamente da seguinte maneira:

* Atendimento Externo: preenchida com a Data de Entrada do atendimento do paciente.
* Atendimento Interno: preenchida com a Data Início da Parcial, solicitada na seleção do paciente. Caso esta parcial não tenha Data Final , então o sistema irá preencher com a data do dia atual.

Quando uma requisição estiver vinculada a mais de uma parcial, a devolução por pacote contemplará apenas uma dessas parciais. A devolução dos demais itens deverá, obrigatoriamente, ser realizada pelo processo de **Devolução via nome do paciente**.

Ao salvar o registro, a devolução ficará com o status de **Devolução iniciada**, aguardando a sua finalização.

Para continuar o processo em um requisição com o status de devolução iniciada, o usuário deve marcar o checkbox e clicar no botão Criar devolução. Após essa ação será aberta a tela de devolução com as informações preenchidas, permitindo ao usuário gerar a devolução de maneira definitiva.

Para finalizar o processo basta acessar o registro salvo anteriormente, selecionar os itens que serão devolvidos e clicar no botão **Gerar devolução.**

Caso haja nenhuma pendência o status passará para o status **Finalizada**, e será possível realizar a impressão de etiquetas e protocolo.

Para visualizar as devoluções Finalizadas e Devolvidas, o usuário deve marcar o checkbox e clicar no botão Criar devolução, será aberta a tela apenas para visualização ou impressão.

Os parâmetros para configurar os relatórios de etiquetas e de protocolo, estão na tela de **Ambiente > Parâmetros > Gestão Hospitalar > Relatórios > Relatórios 3/4**.

Receber devolução

## **04. RECEBER DEVOLUÇÃO DE PACOTE**

Na tela de **Farmácia > Processos farmacêuticos**, o pacote com status devolvido foi proveniente de devolução feita pela enfermagem ou pela farmácia após aceitar a devolução na tela de criar devolução.

A tela de receber devolução só pode ser acessada caso a requisição não esteja sendo usada por outro usuário, e também, caso o status seja "Devolvido". Como é mostrado abaixo:

Ao clicar no botão receber devolução a seguinte tela é apresentada:

Usuário pode selecionar através de checkbox os itens que foram efetivamente devolvidos conferindo fisicamente, ou bipar os itens por código de barras. Quando bipar um item, a linha correspondente ao material e lote bipados seleciona automaticamente o checkbox.

Após bipagem ou conferência manual, o usuário poderá clicar em Aceitar devolução.

Após a conclusão a tela é fechada o status é alterado para finalizado.

Somente após "Aceitar devolução" é que os itens terão o controle de estoque e a elaboração de conta do paciente alterados/devolvidos.

Devolução Iniciada - Desdobramentos

## **03. DEVOLUÇÃO INICIADA - DESDOBRAMENTOS**

Acessar a tela Processos Farmacêuticos da farmácia (**Farmácia> Processos Farmacêuticos**) ou enfermagem (Cuidados com o Paciente > Processos Farmacêuticos). O comportamento será o mesmo para ambas as telas:

Criar uma devolução através do botão "Criar devolução":

Selecionar um pacote com mais de um item e confirmar apenas um deles:

Criar uma nova devolução, selecionar o mesmo pacote da devolução anterior:

Apenas o item não devolvido estará disponível:

Concorrência de Acessos

## **04. CONCORRÊNCIA DE ACESSOS**

Cada requisição só poderá ser acessada por um único usuário, desta forma, existe um controle que bloqueia o acesso à Requisição assim que ela é aberta e libera assim que for fechada.

A mensagem abaixo é exibida quando uma requisição estiver sendo utilizada por outro usuário:

O tempo limite que esse bloqueio permanecerá é de até 5 horas, desta forma ele não será permanente em possíveis falhas na liberação do acesso.

## **Processo Liberar Acesso à Requisição**

Caso ocorra alguma falha na liberação automática da requisição, é possível realizar uma liberação manual:

Impressão do Pacote

## **07. IMPRESSÃO DO PACOTE**

Em **Cuidados com o Paciente > Processos Farmacêuticos** na aba Processos há o botão Imprimir Pacote que imprime o relatório do pacote.

Deve ser selecionado apenas um pacote para realizar a impressão.

Para configurar qual relatório será impresso, vá em **Cadastros > Unidade de Atendimento.**

Selecione a unidade de atendimento e vá em Processos farmacêuticos/Centro cirúrgico.

Em Relatório do Pacote selecione o relatório desejado:

O relatório padrão é o SAUREL0098 - Pacote Farmácia.

Excluir Requisição (Pacote com Devolução Iniciada)

## **08. EXCLUIR REQUISIÇÃO (PACOTE COM DEVOLUÇÃO INICIADA)**

Em Cuidados com o Paciente > Processos Farmacêuticos na aba Processos há o botão Excluir Requisição.  
Disponível também em Farmácia > Processos Farmacêuticos na aba Processos.

Apenas registros com o status "Dispensação Iniciada" podem ser excluídos.  
Deve ser selecionado apenas um pacote para realizar a exclusão.

Executando o processo, a requisição é excluída com sucesso.
