---
content_hash: 8228233e3d8f7ec68e1c9d181578c61e2b57f46248619334636bb1bc5e7969ad
fetched_at: '2026-06-29T00:11:10.011964+00:00'
page_id: '641154708'
product: rm
source: tdn-rm
title: Protocolos Oncológicos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=641154708
version: 68
---

### Lançamento de medicamento

ProtocolosOncologicosVisão geral

## **01. VISÃO GERAL**

A tela pode ser acessada através de Cadastros > Prescrição Médica > >Oncologia > Protocolos Oncológicos.

Ao acessar a opção Protocolos Oncológicos a seguinte tela é apresentada com os dados dos protocolos oncológicos:

**Filtros:** Nessa tela é possível executar a busca por nome de protocolo, Tipo de protocolo, Finalidade do protocolo e Situação do protocolo. Os protocolos podem estar classificados em três situações: Incompleto (quando ele está sendo criado/editado), Ativado (quando finalizado e disponível para prescrição) e Desativado (quando não está disponível para uso).

Ao clicar em "Novo protocolo" é exibida tela para o cadastro de protocolos:

## **02. REGRAS PARA EDIÇÃO**

Para editar os protocolos cadastrados basta clicar duas vezes sobre o registro, ou então, clicar no botão de edição na barra de ferramentas.

Somente será possível editar protocolos com a situação **Incompleto** ou **Desativado**. Para editar um protocolo com a situação **Ativado**, será necessário desativá-lo previamente.

Ao tentar editar um protocolo com a situação **Ativado** será exibida a mensagem abaixo:

## **03. PRÉ-REQUISITOS**

Antes de realizar o cadastro do protocolo oncológico, é essencial configurar o parâmetro que define a unidade de medida correspondente ao Miligrama. Essa configuração é indispensável e será utilizada durante o cadastro dos itens da quimioterapia. Sem ela, não será possível vincular medicamentos ao protocolo. Para configurar, siga os passos abaixo:

Acessar: Menu > Ambiente > Parâmetros > Gestão Hospitalar

Clicar a opção Integração e avançar, conforme imagem abaixo:

Acessar a opção "Configurações gerais 2/5" e configurar o campo Miligrama, vide imagem abaixo:

Cadastrar protocolo

## **01. Cadastrar protocolo**

Para cadastrar um novo protocolo o usuário tem duas opções, clicar no botão de "Novo" padrão da tela ou clicar no botão "Novo protocolo" que fica acima da grid dos protocolos, vide destaques abaixo:

Após clicar em uma dessas opções será aberto a tela para o cadastro do novo protocolo.

Na aba "Identificação" o usuário deverá informar obrigatoriamente as informações de: Nome ou sigla do protocolo a ser cadastrado, Finalidade e Referência bibliográfica.

O ID do protocolo será gerado automaticamente pela aplicação assim que o usuário salvar as informações - o usuário não pode alterar esta informação.

O Tipo de tratamento nesse momento será apenas de quimioterapia, logo não será permitido alteração nesse campo e todos os protocolos oncológicos criados pertencerão a este tipo.

Os campos de log, criado em, criado por, modificado em e modificado por, serão gerados automaticamente pela aplicação, e não podem ser alterados pelo usuário.

## **01.01 Finalizar protocolo**

No momento em que o usuário está salvando o protocolo oncológico, existe a possibilidade de finalizar o protocolo.

Caso o usuário já tenha inserido as fases da quimioterapia, logo após salvar o protocolo será exibida uma mensagem perguntando ao usuário se deseja finalizar o protocolo.

Caso o usuário opte por finalizar o protocolo, clicando no "sim", após a finalização todas as informações serão salvas e o protocolo ficará com o status de ativado.

Caso o usuário opte por não finalizar o protocolo, clicando no "não", o protocolo ficará com o status de incompleto.

A mensagem perguntando se o usuário deseja finalizar o protocolo só será exibida caso já tenha cadastrado fases para o protocolo.Ativar protocolo

## **01. Ativar protocolo**

Para ativar um determinado cadastro, devemos selecionar a(s) linha(s) desejadas, e após, clicar no botão **Ativar protocolo** ou então no processo de mesmo nome.

Para ativar um protocolo deve ser selecionado pelo menos uma linha com a situação **Incompleto** ou **Desativado**.

Desativar protocolo

## **01. Desativar protocolo**

Para desativar um determinado cadastro, devemos selecionar a(s) linha(s) desejadas, e após, clicar no botão **Desativar protocolo** ou então no processo de mesmo nome.

Para desativar um protocolo deve ser selecionado pelo menos uma linha com a situação **Incompleto** ou **Ativado**.

Tipo de tratamento quimioterapia

## **01. Cadastro das fases de quimioterapia**

Quando o tipo de tratamento cadastrado for quimioterapia será criada um aba com o mesmo nome exibindo as informações das fases cadastradas e seus desdobramentos.

A aba irá exibir um resumo das fases cadastradas com as informações de nome, quantidade de ciclos, duração dos ciclos e intervalo entre ciclos. Conforme manuseio padrão do RM o usuário poderá inserir, editar ou excluir as fases associadas ao protocolo em questão.

Para cadastrar um novo ciclo é necessário que antes seja cadastrado uma fase, do contrário a seguinte mensagem será exibida:

Observe que as opções relacionadas ao Ciclo, ficarão desabilitadas até que seja adicionado ao menos um ciclo:

## **01.01****Ciclos X Dias**

Dentro da fase de quimioterapia é possível realizar a inclusão dos ciclos.

Cada ciclo poderá ter prescrições diferentes por dia de tratamento. Cada dia terá medicamentos associados.

Para facilitar o lançamento de dias iguais é possível utilizar a função de copiar dia, deste modo não é necessário refazer todo o lançamento dos itens.

### 01.01.01 Cópia de ciclos

Para facilitar o cadastro, existe um processo com o objetivo de criar cópias dos ciclos previamente cadastrados.

Basta selecionar o ciclo, e no botão **Processos** clicar em **Copiar ciclo**:

Após, selecionar o quantidade de cópias desejadas e clicar em **Copiar**:

Os novos ciclos serão adicionados a listagem:

### 01.01.02 Exclusão de ciclos

Ao selecionar um ou vários ciclos o usuário poderá excluir o ciclo e todos os demais cadastros associados ao registro selecionado de uma só vez, medicamentos, diluentes e materiais e os materiais do ciclo. Ao clicar no botão para excluir será apresentada uma mensagem para que o usuário possa confirmar a exclusão.

### 01.01.03 Exclusão de dias

Ao acessar um determinado dia o usuário poderá excluir todo o dia e os demais cadastros associados ao registro selecionado de uma só vez, medicamentos, diluentes e materiais. Ao clicar no botão para excluir será apresentada uma mensagem para que o usuário possa confirmar a exclusão.

## **01.02****Prescrição de medicamento**

Dentro do cadastro dos dias da fase de quimioterapia serão incluídos os medicamentos na ordem em que serão preparados/administrados.

### 01.02.01 Lançamento de medicamento

Ao clicar em "Novo" ou clicar 2x no registro desejado é aberta uma tela com as abas Medicamento, Diluentes e Materiais.

**Medicamento**

Destinada para adição/edição dos medicamentos. O usuário deverá informar os dados conforme a necessidade do protocolo. As informações de Ciclo, Dia e Ordem, nesse ponto, são apenas informativas não podendo ser alteradas. O usuário somente poderá selecionar a unidade de medida caso o parâmetro de cálculo da dose seja fixo, do contrário deverá selecionar a forma pela qual o medicamento será calculado de acordo com o cadastro do medicamento de escolha.

**Categorias Disponíveis para Lançamento de Medicamentos**

As seguintes categorias estão disponíveis para serem utilizadas no lançamento de medicamentos, especialmente no contexto de tratamentos oncológicos:

* Quimioterapia
* Pré-Quimioterapia
* Pós-Quimioterapia
* Hormonioterapia
* Anticorpo Monoclonal

Essas classificações auxiliam no controle, organização e rastreamento dos medicamentos utilizados nos diferentes estágios ou tipos de tratamento.

Antes de realizar o cadastro do medicamento, é essencial configurar o parâmetro que define a unidade de medida correspondente ao Miligrama. Para configurar acessar: Parâmetros Gerais > Integrações > Configurações gerais 2/5

A ordem dos medicamentos poderá ser realizada na grid dos medicamentos após a seleção no checkbox e movimentação através dos botões direcionais, conforme destaque da imagem:

#### Diluentes

Na aba de diluentes do cadastro de medicamento da prescrição, podemos adicionar qual o tipo de diluição, o componente que será utilizado, a quantidade (em ml) do componente utilizado e caso tenha mais de uma ação de diluição o usuário poderá definir a ordem de ações.

Na aba de diluentes será exibido todas as ações definidas para o determinado medicamento, vide imagem abaixo:

Clicando no botão de novo será exibida a tela para o usuário cadastra os componentes e ação que será utilizada no medicamento.

**Ordem**: Será preenchido automaticamente de acordo com as ações que foram cadastradas anteriormente, esse campo não permite alteração.

**Ação:** Nesse campo o usuário deverá definir o que deverá ser realizado com o medicamento, nele temos as opções: **Diluir**, **Reconstituir** ou **Rediluir**.

Os componentes devem ser preenchidos para informar qual o componente será utilizado para realizar a ação que foi definida, nessa seção teremos os campos:

**Volume:** Será definida quantos ml do diluente será utilizado para realizar a ação.

**Componente:** Será definido qual o diluente que será utilizado para realizar a ação, nesse campo serão exibidos os itens configurados como Solução (Soro) ou Componente de solução.

Para realizar essa configuração deverá acessar o produto no anexo "Informações do TOTVS saúde" na aba de Identificação II, segue imagem abaixo:

#### Materiais do medicamento

Na aba de materiais do cadastro de medicamento da prescrição podemos adicionar itens que serão usados exclusivamente para esse medicamento. Como exemplo, a exigência de um filtro de linha para determinado medicamento. 

Para criar um novo registro é necessário clicar no botão "Novo".

Para excluir um registro é necessário selecionar o item na grid e no botão excluir.

Para editar um item editar um registro já lançado basta clicar duas vezes no material desejado.

#### Trocar a ordem de infusão dos medicamentos através da grid de visualização dos itens

A ordem de infusão pode ser revisada e alterada pela grid de visualização dos itens já lançados, o usuário deverá selecionar na grid um medicamento e clicar nas setas disponibilizadas no menu acima da grid para realizar a troca.

## **01.03****Ciclos X Dias X Materiais**

Dentro do ciclo é possível vincular materiais que serão usados em dias específicos ou em todos eles.

### 01.03.01 Cadastro de materiais do ciclo

Pra cadastrar materiais do ciclo é necessário informar o material usado e a quantidade usada para o material.

Se houver necessidade de substituição do material caso o paciente utilize cateter, é possível realizar o cadastro do material conforme destaque abaixo.

O material que será usado pode ser aplicado a todos os dias do ciclo ou de um dia especifico.

Favoritos

## **01. Cadastro e Lançamento de medicamentos e materiais favoritos**

Ao realizar o cadastro de um medicamento, material associado ao medicamento ou ao ciclo, o usuário pode marcá-lo como favorito facilitando seu lançamento em novos cadastros.

## **01.01** **Medicamento Favorito**

O usuário no cadastro do medicamento do protocolo deve marcar o item como favorito.

Após esse cadastro o usuário poderá selecioná-lo na tela de seleção de medicamentos favoritos que pode ser acionada através do ícone de favoritos na aba de lançamento de medicamentos do dia do ciclo da fase de quimioterapia. Apenas os medicamentos favoritos podem se adicionados, os materiais e ações de diluição não são gravadas.

O usuário pode remover o item da lista de favoritos a qualquer instante, a ação pode ser realizada através do cadastro do item desmarcando a opção favoritos ou ao abrir a tela de seleção de favoritos o usuário poderá selecionar os itens que deseja remover e clicar no botão remover favoritos.

## **01.02 Material favorito**

O Usuário no cadastro de materiais que fica dento do produto, tem a possibilidade de marca um desses materiais como favorito.

Após esse cadastro o usuário salvar um material como favorito, poderá selecioná-lo na tela de seleção de materiais favoritos, que deve ser acionada através do ícone de favoritos na aba de materiais que fica na tela de cadastro do produto. Ao cadastrar o material do produto o mesmo pode ser associado a 1 (um) dia ou todos, no caso de selecionar o item favorito essa informação sempre será todos.

O usuário pode remover o item da lista de favoritos a qualquer instante, a ação pode ser realizada através do cadastro do item desmarcando a opção favoritos ou ao abrir a tela de seleção de favoritos o usuário poderá selecionar os itens que deseja remover e clicar no botão remover favoritos.

## **01.03 Material do ciclo favorito**

O usuário no cadastro dos materiais do ciclo do protocolo deve marcar o item como favorito.

Após esse cadastro o usuário poderá selecioná-lo na tela de seleção de materiais do ciclo favoritos que pode ser acionada através do ícone de favoritos na aba de lançamento de materiais do dia do ciclo da fase de quimioterapia. Ao cadastrar o material do ciclo o mesmo pode ser associado a 1 (um) dia ou todos, no caso de selecionar o item favorito essa informação sempre será todos.

O usuário pode remover o item da lista de favoritos a qualquer instante, a ação pode ser realizada através do cadastro do item desmarcando a opção favoritos ou ao abrir a tela de seleção de favoritos o usuário poderá selecionar os itens que deseja remover e clicar no botão remover favoritos.
