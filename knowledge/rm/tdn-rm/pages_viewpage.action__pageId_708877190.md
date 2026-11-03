---
content_hash: d434f5f33eda4d84bc2ed25d997635269309822bdae6bf94271bb8ce43fc7433
fetched_at: '2026-06-29T00:11:25.414121+00:00'
page_id: '708877190'
product: rm
source: tdn-rm
title: Transcrição de Prescrição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=708877190
version: 39
---

Transcrição de prescriçaoVisaoGeralVisão Geral

## **01. VISÃO GERAL**

A tela pode ser acessada através de Menu > Farmácia > Controle de Estoque > Movimentação de Estoque

Ao acessar a tela de movimentação de estoque, serão exibidas todas as movimentações, considerando o filtro aplicado.

As requisições do tipo transcrição de prescrição possuem 2 status possíveis, Finalizada ou Rascunho.

Toda a requisição deverá ser finalizada ao fim do cadastro para que possa ser enviada ao painel de dispensação e nesse ponto seu status será alterado.

### **01.1 Status da transcrição**

As transcrições possuem 2 status, Rascunho e Finalizada.

As transcrições em rascunho são todas que ainda não foram finalizadas, ou seja, gerado o aprazamento e enviadas ao Painel de Dispensação. 

As transcrições com o status Finalizada são as já foram gerados os aprazamentos e estão disponíveis para a dispensação no Painel de Dispensação. 

Apenas as transcrições em rascunho podem ser editadas.

Criação da movimentação de estoque

## **02. MOVIMENTAÇÃO DE ESTOQUE**

Na tela de movimentação de estoque ao selecionar o tipo de movimento "Transcrição de prescrição", a tela irá exibir os seguintes controles, vide imagem abaixo:

**Nome:** Nesse campo o usuário deve selecionar o botão que fica ao lado do campo e escolher para qual atendimento/paciente deseja realizar a transcrição.  
**Medico Prescritor:** Nesse campo o usuário deve selecionar qual o médico responsável pela prescrição.  
**Local de Estoque Origem e Centro de custo:** Ambos os campos serão preenchidos automaticamente após o usuário selecionar o atendimento/paciente, não será possível altera-los.

**Obs.:**   
Todos os campos são de preenchimento obrigatório.  
Ao selecionar a parcial do paciente por padrão o campo data será preenchido com a data de abertura da conta do paciente, no caso de pacientes externos.

Após salvar uma transcrição de prescrição será aberta uma nova aba para o usuário inserir os itens da transcrição, conforme imagem abaixo:

Tela transcrição da prescrição

## **03. TELA TRANSCRIÇÃO DA PRESCRIÇÃO**

Na tela de transcrição da prescrição o usuário poderá visualizar todos os itens que foram adicionados.

No cabeçalho serão exibidas as informações básicas para identificar o paciente, médico prescritor e número da transcrição.

No lado esquerdo da tela teremos:

1. Botões de ação para permitir o usuário inserir medicamentos, inalações e soros e componentes.
2. Controle para permitir o usuário anexar a prescrição do médico. Para realizar a transcrição é obrigatório anexar a prescrição original.

Obs.: A função de anexar prescrição possui duas opções: 1- Adicionar uma imagem; 2- Utilizar a webcam do computador para tirar uma foto da prescrição.

No lado direito da tela teremos:

1. Grid onde será exibido todos os itens que foram solicitados pelo usuário.
2. Botão excluir item, onde usuário poderá selecionar um item no grid e removê-lo da transcrição.

### **03.1 Anexo da prescrição**

Para validação do processo o usuário deverá anexar uma foto da prescrição original. Será permitido selecionar um arquivo no computador com a imagem ou capturar através da câmera.

A inclusão do anexo da prescrição é obrigatória, e quando não adicionada será mostrada a seguinte mensagem abaixo do controle de seleção "Necessário anexar prescrição".

A imagem anexada ficará disponível para visualização na aba Transcrição, caso a imagem seja removida ou não tenha sido anexada, a mensagem "Necessário anexar prescrição" será exibida nessa aba também.

### **03.2 Salvar e Finalizar**

Ao finalizar o cadastro da transcrição o usuário poderá salvar ou finalizar.

O botão salvar irá persistir os dados em banco e manter a transcrição com o status rascunho.

O botão finalizar irá salvar os dados em banco e serão gerados os aprazamentos conforme regra padrão de combinação de dose e frequência. Nesse momento não será mais possível editar a transcrição e o processo seguirá no painel de dispensação com o atendimento a requisição.

Medicamento

## **04. MEDICAMENTO**

Para adicionar um medicamento o usuário deve, na tela de transcrição da prescrição, clicar no botão medicamentos. 

Para alterar um item já lançado basta um duplo clique sobre o item no grid de itens selecionados, conforme imagem abaixo:

Após clicar no botão, será exibida a tela abaixo para permitir o usuário inserir o medicamento.

Ao selecionar o medicamento as informações previamente cadastradas e associadas ao medicamento serão carregadas e o usuário deverá selecionar de acordo ao item.  
Os campos quantidade, unidade, via e frequência são obrigatórios a todos o itens. As informação de padrão de diluição são apenas para os itens que possuam em seu cadastro de padrão de prescrição, um padrão de diluição associado, e que pelo menos um dos itens seja diluente, a via de aplicação também deverá ser a mesma cadastrada no padrão.

Verificar o cadastro de unidade de dosagem do produto para a lista de unidades possíveis em Cadastros - Estoque - Produto - Informações TOTVS Saúde - Anexos - Unidade de dosagem.

Verificar o cadastro de Via de aplicação do produto para alista de via em Cadastros - Estoque - Produto - Informações TOTVS Saúde - Anexos - Aplicação associada.

Verificar o cadastro de frequência em Cadastros - Cuidados com o paciente - Prescrição médica - Frequência de administração de medicamentos.

Verificar o cadastro de Padrão de prescrição para o produto e se o mesmo possui um padrões de diluição associado em Cadastros - Cuidados com o paciente - Prescrição médica - Padrões de prescrição

### **04.1 Validações**

No momento de adicionar um novo medicamento as seguintes informações são obrigatórios.

Inalação

## **05. INALAÇÃO**

Para adicionar um item classificado como inalação o usuário deve, na tela de transcrição da prescrição, clicar no botão Inalação. 

Para alterar um item já lançado basta um duplo clique sobre o item no grid de itens selecionados, conforme imagem abaixo:

Após clicar no botão, será exibida a tela abaixo para permitir o usuário inserir a inalação. Ao selecionar a inalação as informações previamente cadastradas e associadas a inalação serão carregadas e o usuário deverá selecionar de acordo ao item.

Os campos apresentação, quantidade, unidade, inalação, via, frequência e através de são de preenchimento obrigatórios.

O campo apresentação será preenchido automaticamente, logo após a seleção da inalação.

Verificar o cadastro de unidade de dosagem do produto para a lista de unidades possíveis em Cadastros - Estoque - Produto - Informações TOTVS Saúde - Anexos - Unidade de dosagem.

Verificar o cadastro de Via de aplicação se está configurado para inalação - Cadastros - Cuidados com o paciente - Prescrição médica - Via de administração de medicamentos.

Verificaro cadastro de frequência em Cadastros - Cuidados com o paciente - Prescrição médica - Frequência de administração de medicamentos.

Verificar o cadastro de Padrão de prescrição para o produto e se o mesmo possui um padrões de diluição associado em Cadastros - Cuidados com o paciente - Prescrição médica - Padrões de prescrição

O Campo inalação tem os valores disponíveis fixo, são eles: Ar Comprimido e Oxigênio

O Campo através de tem os valores disponíveis fixo, são eles: Máscara, Tubo Endotraqueal e Traqueostomia.

### **05.1 Validações**

No momento de adicionar uma nova inalação as seguintes informações são obrigatórias.

Soros e componentes

## **06. Soros e componentes**

Para adicionar um item classificado como soros e componentes o usuário deve, na tela de transcrição da prescrição, clicar no botão Soros e Componentes. 

Para alterar um item já lançado basta um duplo clique sobre o item no grid de itens selecionados, conforme imagem abaixo:

Após clicar no botão, será exibida a tela abaixo para permitir o usuário inserir soros ou componentes.

Ao selecionar a solução ou o componentes as informações devidamentes cadastradas e associadas ao item serão carregadas e o usuário deverá selecionar de acordo ao item.  
Os campos apresentação, quantidade e unidade são obrigatórios a todos o itens, o usuário deverá selecionar o item as informações e clicar em inserir, apenas ao final deverá informar via e frequência. Nesse momento o RM irá adicionar todos o itens selecionados com essas informações adicionais. Será exibido apenas 1 item ( o primeiro lançado ) na grid principal.

Verificar o cadastro de unidade de dosagem do produto para a lista de unidades possíveis em Cadastros - Estoque - Produto - Informações TOTVS Saúde - Anexos - Unidade de dosagem.

Verificar o cadastro de Via de aplicação se está configurado para soluções - Cadastros - Cuidados com o paciente - Prescrição médica - Via de administração de medicamentos.

Verificaro cadastro de frequência em Cadastros - Cuidados com o paciente - Prescrição médica - Frequência de administração de medicamentos.

Verificar o cadastro de Padrão de prescrição para o produto e se o mesmo possui um padrões de diluição associado em Cadastros - Cuidados com o paciente - Prescrição médica - Padrões de prescrição

### **06.1 Validações**

Ao inserir um item os campos abaixo serão obrigatórios:

Após inserir todos os itens que compoem a solução, e tentar adicionar à requisição será necessário informar os campos abaixo:

### **06.2 Exclusão**

Após a inclusão do soro ou componente, o usuário poderá retirá-lo da lista a qualquer momento antes de sua confirmação. Para tal, basta clicar na grid na célula que possui a imagem de uma lixeira.

Ao clicar será exibida uma mensagem, conforme figura abaixo, confirmando a exclusão do item selecionado.

Alertas

## **07. Alertas**

O processo de transcrição possui alguns alertas clínicos que auxiliam o profissional a promover segurança do paciente.

Os alertas irão exibir mensagens informando especificamente a ocorrência e será necessário selecionar uma justificativa, previamente cadastrada para seguir com a transcrição da prescrição.

As justificativas são cadastradas em Cadastros > Estoque > Cadastros de Estoque > Transcrição da Prescrição - Justificativas de Alertas Clínicos.

A justificativa cadastrada pode ser para um alerta específico ou para todos os alertas, os alertas clínicos que o RM Saúde exibem são interação medicamentosa, duplicidade de princípio ativo e faixa terapêutica, para que sejam validados seus cadastros e configurações devem ter sido realizados.

### **07.1 Interação medicamentosa**

O cadastro de interação medicamentosa deve ser realizado e configurado em Cadastros > Cuidados com o paciente > Prescrição médica > Interações medicamentosas, a regra que será aplicada é para os tipos de interação entre princípio ativo x princípio ativo e com classificaão de risco alto, caso atenda será exibido o alerta:

### **07.2 Duplicidade de princípio ativo**

O cadastro de princípio ativo deve ser realizado e configurado em Cadastros > Cuidados com o paciente > Prescrição médica > Padrões de prescrição, caso a transcrição já possua um medicamento com o mesmo princípio ativo será exibido um alerta:

### **07.3 Faixa terapêutica**

O cadastro de faixa terapêutica deve realizado e configurado em Cadastros > Estoque > Produto > Informações TOTVS saúde > Anexos > Doses máxima e mínima, caso o medicamento prescrito possua uma dosagem fora dos limites configurados será exibido um alerta:
