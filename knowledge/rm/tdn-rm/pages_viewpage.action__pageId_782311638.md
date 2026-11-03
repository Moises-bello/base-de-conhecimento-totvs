---
content_hash: b3fd089d8a3060eee93d284d5586e65482f18c55896af2aca9f734130b2c9309
fetched_at: '2026-06-29T00:11:38.242044+00:00'
page_id: '782311638'
product: rm
source: tdn-rm
title: Requisição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=782311638
version: 72
---

RequisiçãoVisaoGeralVisão Geral

## **01. VISÃO GERAL**

A movimentação de estoque do tipo requisição foi criada para atender clientes que não possuem prescrição ou que necessitam realizar algum lançamento na conta. Esse processo irá dispensar e lançar itens na conta do paciente, desde que estejam devidamente configurados.

O usuário pode acessar o processo através do menu Farmácia > Controle de estoque > Movimentação de estoque.

Apenas usuários com permissão poderão atender movimentações do tipo requisição, a permissão é configurada através das permissões de perfil, padrão do RM:

Criação da movimentação de estoque

## **02. MOVIMENTAÇÃO DE ESTOQUE**

Na tela de movimentação de estoque ao selecionar o tipo de movimento "Requisição para o paciente", a tela irá exibir os seguintes controles, vide imagem abaixo:

**Paciente:** Nesse campo o usuário deve selecionar o botão que fica ao lado e escolher para qual atendimento/paciente deseja realizar a requisição.  
**Local de Estoque Origem e Centro de custo:** Ambos os campos serão preenchidos automaticamente após o usuário selecionar o atendimento/paciente.  
**Local de Uso:** Local onde será utilizado os itens que foram requisitados.

OBS: Ao selecionar a parcial do paciente por padrão o campo data será preenchido com a data de abertura da conta do paciente, no caso de pacientes externo.

Após salvar uma requisição será aberta em uma nova aba para o usuário inserir os itens da requisição, vide imagem abaixo:

Itens da movimentação

## **03. ITENS DA MOVIMENTAÇÃO**

Nessa tela serão selecionados e exibidos todos os itens da requisição, a tela está divida em cabeçalho, seleção de itens e itens selecionados.

### **03.01 Cabeçalho**

No cabeçalho são exibidas as informações do paciente e atendimento:  
Nome, data de nascimento, idade, sexo, unidade de atendimento, convênio, número de atendimento, leito, prontuário, número da requisição e status da requisição.

### **03. 02 Seleção de itens**

Na parte de seleção dos itens o usuário terá duas possibilidades, são elas:

1. 1. Busca pelo código de barras, nela o usuário deve selecionar a quantidade digitar/bipar o código de barras do produto e clicar no "enter" para adicionar o item a requisição. Importante informar que neste caso utilizaremos sempre a unidade de controle de estoque do produto escolhido.
   2. Busca pelo nome/código do produto, nela o usuário deve selecionar o nome ou código do produto, selecionar a unidade de medida e a unidade de controle. No caso de produtos controlados por lote, o usuário após seleciona-lo obrigatoriamente deve informar o lote clicando no botão "...", que fica ao lado campo lote. Será aberto uma janela com a lista de lotes disponíveis, após selecionar o lote as demais informações serão preenchidas.

**03.03 Itens selecionados**

Na parte de itens selecionados são exibidos os itens adicionados a requisição independente de seu status, também são exibidos os botões com as ações que podem ser aplicadas ao item desde que seu status permita.

Na grid são exibidas as informações de status, descrição do item, quantidade ( em relação a unidade de estoque ), unidade de estoque, lote, número de série, validade do lote, fabricante e observação.

Adicionar item

## **04. ADICIONAR ITEM**

Existem duas opções para adicionar um item à requisição, são elas:

**Código de barras:** Digitar o código de barras, informar a quantidade e pressionar Enter para adicionar, conforme imagem abaixo.

**Pesquisa do produto:** Digitar o nome do produto, preencher as demais informações e, após completar, clicar no botão 'Adicionar Item'.

Versão 

Nas versões 2406 e superiores será permitido adicionar itens utilizando a unidade de prescrição.

### **04.01 Item composto**

Quando selecionado ou bipado um item que é composto será exibida uma tela onde o usuário poderá selecionar quais os itens do composto que deseja adicionar na requisição.

Os itens que não são controlados por lote já serão exibidos na de incluídos.

Será possível incluir itens controlado por lote sem informar o lote do produto.

Após incluir os itens que deseja o usuário deve clicar no botão adicionar

Após clicar no botão adicionar todos os itens incluídos serão adicionados a requisição, vide imagem abaixo:

#### **Para confirmar a adição dos itens na requisição é necessário clicar no botão salvar.**

### **04.02 Item associado**

Quando selecionado ou bipado um item que possui associados todos os associado serão adicionado na requisição.

Selecionado o item Polpa de Fruta

Após clicar no botão adicionar item, os associados agulha e algodão serão adicionados, vide imagem abaixo:

ObservaçõesAlterar lote

## **05. ALTERAR LOTE**

Para alterar o lote de um determinado o usuário deve realizar os seguintes passos:

Marcar na grid o item que deseja alterar o lote e clicar no botão alterar lote.

Após clicar no botão alterar lote será exibido uma tela com a lista de lotes disponível para esse produto, vide imagem abaixo.

Para selecionar o lote que deseja o usuário bastar selecionar a linha do lote e clicar no botão "OK".

Após clicar no botão "OK", podemos notar que na grid dos itens solicitados foi alterado o lote e a sua validade, para confirmar a alteração do lote o usuário deve clicar no botão "Salvar" da tela.

Observações

* Só será permitido o alterar lote de itens que são controlados por lote
* Só será permitido o alterar lote de itens com o status pendente não confirmado
* Só será permitido o alterar lote de apenas um item por vez
* Não será permitido alterar o lote de produtos confirmados
* A alteração de lote só será salvar após clicar no botão salvar da tela
* Lotes vencidos serão mostrados na tela, porém destacados em vermelho para atenção do usuário.
* Somente para item configurado como Baixa Estoque = Sim,  a grid “Seleção de Lote” somente irá listar os lotes que tenham saldo no estoque.

Excluir

## **06. EXCLUIR**

Para excluir um determinado item o usuário deve realizar os seguintes passos:

Marcar na grid um ou mais item que deseja excluir e clicar no botão excluir, vide imagem abaixo.

Após clicar no botão excluir será exibido uma mensagem de confirmação para o usuário.

Caso clique em NÃO, irá retornar para a tela principal.

Caso clique em SIM, os itens serão removido da tela, vide imagem abaixo:

Para confirmar a exclusão dos itens o usuário deve clicar no botão "Salvar" da tela.

Observações

* Só será permitido excluir itens com o status pendente.
* O usuário poderá excluir um ou mais itens.
* NÃO será permitido excluir item(ns) oriundos de uma solicitação de exame.
* A exclusão só será confirmada após clicar no botão salvar da tela.
* Após confirmar exclusão caso só tenha item processado a requisição será modificada para processada.
Confirmar

## **07. CONFIRMAR**

Para confirmar um determinado item o usuário deve realizar os seguintes passos:

Caso o usuário não marque itens selecionados na grid, todos os itens serão enviados para confirmação, caso deseje o usuário pode selecionar quais os itens desejam confirmar, vide imagem abaixo:

Após clicar no botão confirmar todos os itens selecionado serão confirmados e será exibido uma mensagem informando ao usuário sobre a confirmação.

No grid dos itens selecionado o status do item mudará para confirmado, vide imagem abaixo:

Caso no momento de confirmar um item exista algum item que não foi salvo, seja um item que foi adicionado ou que teve o seu lote alterado, será exibida uma mensagem para o usuário que existem itens pendente de salvar, vide imagem abaixo:

Caso clique em "Sim" todos os itens serão salvos, caso clique em "Não" irá retornar para a tela, em ambas as situações os itens não serão confirmados, sendo necessário clicar no botão confirmar logo após salvar os itens.

Observações

* Só será permitido confirmar item que possui saldo suficiente.
* No caso de itens controlados por lote, só será possível confirmar item com lote definido, lotes com validade e saldo.
* Só será permitido confirmar itens com o status pendentes.
* Para itens CME só será permitido confirmar caso não tenha atingido o limite de uso.

## **07.1 CONFIRMAR POR LEITOR DE CÓDIGO DE BARRAS**

Também é possível confirmar os itens por leitor de código de barras através de um processo:

É necessário que todos os itens sejam salvos antes da confirmação.

Basta informar o código de barras e a quantidade, vide imagem abaixo:

Após confirmar todos os itens a janela de código de barras é fechada automaticamente. Se não deseja confirmar todos os itens é só fechar a janela de Código de Barras e após isso é atualizado o status dos itens na grid de Itens Selecionados:

Desconfirmar

## **08. DESCONFIRMAR**

Para desconfirmar um determinado item o usuário deve realizar os seguintes passos:

Marcar na grid os itens que deseja desconfirmar e clicar no botão desconfirmar, vide imagem abaixo:

Após clicar no botão desconfirmar será exibida uma mensagem de confirmar.

Caso clique em NÃO, irá retornar para a tela principal.

Caso clique em SIM, os itens selecionados serão desconfirmado.

Ao termino do processo, será exibida uma mensagem informando que os itens foram desconfirmados, na grid podemos notar que os itens voltarão para o status de pendente e no caso de itens controlado por lote, as informações de lote serão removidas.

Caso no momento de desconfirmar exista algum item que não foi salvo, será exibida uma mensagem para o usuário que existem itens pendente de salvar, vide imagem abaixo:

Caso clique em "Sim" todos os itens serão salvos, caso clique em "Não" irá retornar para a tela, em ambas as situações os itens não serão desconfirmados, sendo necessário clicar no botão desconfirmar logo após salvar os itens.

Observações

* Só será permitido desconfirmar item que estão com o status confirmados.
* No caso de itens controlados por lote após desconfirmar todas as informações de lote serão removidas.
Suspender

## **09. SUSPENDER**

Esta funcionalidade permite suspender um ou mais itens de uma requisição, desde que eles tenham sido gerados a partir de uma solicitação de exame.

1. Na tela da requisição, selecione o(s) item(ns) desejado(s) marcando a caixa de seleção ao lado deles.
2. Clique no botão **"Suspender"**.

3. O sistema exibirá uma mensagem de confirmação: *"Deseja suspender o(s) item(ns) selecionado(s)?"*.

* **Se clicar em NÃO:** A ação é cancelada e você retorna para a tela principal sem alterações.
* **Se clicar em SIM:** O sistema processará a suspensão e exibirá a mensagem de sucesso: *"Suspensão realizada com sucesso!"*.

4. Ao retornar para a tela principal, o item passará a ser exibido com o status **Suspenso**.

### Mensagens de Erro Frequentes

Se você tentar suspender um item que foi **adicionado manualmente** ou que não pertença à solicitação de exame original, o sistema bloqueará a ação e exibirá a seguinte mensagem de erro:

Observações

* **Origem permitida:** Só é permitido suspender itens vindos de uma **solicitação de exame**. Itens adicionados manualmente **não** podem ser suspensos.
* **Status necessário:** O item deve estar com o status **Pendente**.
* **Impacto na requisição:** Se todos os itens pendentes da requisição forem suspensos, o status geral da requisição será alterado automaticamente para **Processada**.
Processar

## **10. PROCESSAR**

Para processar uma requisição o usuário deve realizar os seguintes passos:

Marcar na grid um ou mais item que deseja processar e clicar no botão processar, os itens selecionados devem estar confirmado, vide imagem abaixo:

Após o processamento será exibida uma mensagem informativa:

O item será exibido na grid com o status de processado.

Observações

* Só será permitido processar itens confirmados.
* Após processado o item não poderá ser removido.
* Após processado o item não poderá ser desconfirmado.
* Após processado o item não poderá sofrer alteração do lote.
Devolução a Paciente

## **10. DEVOLUÇÃO A PACIENTE**

A devolução a paciente para requisição de paciente originadas na movimentação de estoque deve ser realizada no mesmo processo, pois, não é gerado pacote e logo não pode ser realizada através do painel de processos farmacêuticos.  
O usuário precisa ter a permissão para criar devolução no processo de movimentação de estoque:

O usuário deve informar os dados do atendimento do paciente para iniciar o cadastro da devolução, a requisição associada é opcional para aumentar a integridade limitando apenas a devolver itens da requisição informada.

O usuário deverá informar os itens para devolução e para os itens que possuam controle de lote deverá informar também seus respectivos lotes.

Caso o item ou lote selecionado não possua requisição processada ou possua uma outra devolução iniciada mesmo sem processar e que a soma de suas quantidades seja igual ao total requisitado na parcial do atendimento será exibida uma mensagem informando que não possui saldo de devolução

Ao final o usuário deverá confirmar os itens e processar a requisição para retirar os itens da conta do paciente e devolver ao estoque atualizando seu saldo.

Observações

* Só será permitido processar itens confirmados.
* Após processado o item não poderá ser removido.
* Após processado o item não poderá ser desconfirmado.
* Após processado o item não poderá sofrer alteração do lote.
Baixa Estoque

Na movimentação de estoque, ao realizar Devolução de Paciente utilizando produto definido como Baixa Estoque = “A Definir”, será aplicado a seguinte validação:

- O campo “Baixa Estoque” será preenchido automaticamente com o mesmo tipo que foi utilizado na requisição origem (quando preenchido o campo Req.Associada). Este tratamento será feito após clicar no botão Salvar.

11SUSParticularidades do SUS

## **11. SUS**

1.O lançamento e estorno de OPME (Órteses, Próteses e Materiais Especiais) na AIH, com base nas movimentações de estoque (saída e devolução), deve ocorrer de forma automática no RM quando houver vínculo com códigos de procedimentos SUS (tabela SIGTAP).

2. Visão Geral da Funcionalidade  
Ao criar e processar requisições de estoque de OPME — tanto de saída quanto de devolução — o sistema realiza automaticamente o lançamento ou estorno dos itens na AIH do paciente, desde que a OPME esteja vinculada a um código de procedimento SUS presente na AIH. Esse comportamento segue a mesma lógica já aplicada na elaboração de contas do paciente.

3. Regras de Funcionamento  
3.1 Requisição de Saída

Ao processar uma requisição de saída de OPME:

O sistema lança automaticamente o procedimento correspondente na AIH.

Cada movimentação de saída gera um novo procedimento na AIH, com a quantidade informada.

3.2 Requisição de Devolução  
a) Devolução Integral

Quando todos os itens de uma OPME são devolvidos:

O sistema remove automaticamente o procedimento correspondente da AIH.

b) Devolução Parcial

Quando apenas parte dos itens é devolvida:

O sistema atualiza o saldo do procedimento na AIH.

Exemplo:

Quantidade solicitada: 3 unidades

Quantidade devolvida: 1 unidade

Resultado na AIH: saldo atualizado para 2 unidades

3.3 Restrições por Status da AIH  
A regra de devolução somente será aplicada se a AIH estiver nos seguintes status:

Pendente

Rejeitada

Em Elaboração

Caso a AIH esteja em um dos status abaixo:

Cancelada

Liberada

Faturada

O sistema irá:

Bloquear a devolução

Exibir uma mensagem de erro e alerta ao usuário no momento do processamento

4. Pré-requisitos para Funcionamento  
Para que o lançamento automático funcione corretamente:

A OPME deve estar vinculada a um código de procedimento SUS (SIGTAP).

O vínculo deve ser realizado através da edição do produto na tabela de preços correspondente.

5. Exemplos Práticos  
5.1 Lançamento Automático na AIH

Foram realizadas:

3 requisições de saída de OPME (processadas)

1 requisição de devolução (pendente)

Resultado:

O sistema gerou automaticamente 3 procedimentos na AIH, correspondentes às saídas realizadas.

O total acumulado foi de 13 itens de OPME na AIH do paciente.

5.2 Processamento de Devolução

Foi realizada a devolução de 11 dos 13 itens.

Resultado após processamento:

Procedimentos sem saldo foram excluídos automaticamente:

2 procedimentos com 5 itens cada foram removidos

Procedimento com saldo remanescente foi atualizado:

Procedimento com 3 itens passou a ter 2 itens

6. Comportamento do Sistema

O sistema realiza automaticamente:

Inclusão de procedimentos na AIH (saída)

Subtração de itens (devolução parcial)

Exclusão de procedimentos (devolução total)

Todas as operações ocorrem sem intervenção manual, desde que os pré-requisitos sejam atendidos.

7. Considerações Finais

A correta parametrização do vínculo entre OPME e código SUS é essencial para o funcionamento da rotina.

O controle automático garante maior consistência entre estoque e faturamento hospitalar.

Recomenda-se validar o status da AIH antes de processar devoluções para evitar bloqueios.
