---
content_hash: 25a0d06a4a802575363ec2a5d16feb53072d907deec1c8b24dccf896dfe55353
fetched_at: '2026-06-29T00:11:54.088970+00:00'
page_id: '853285767'
product: rm
source: tdn-rm
title: Registro de atendimento simplificado
type: documentation
url: https://tdn.totvs.com/display/LRM/Registro+de+atendimento+simplificado
version: 97
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Pré-Requisitos**
   1. **Parâmetros**
   2. **Permissões**
   3. **Premissas**
3. **Totem de Atendimento**
   1. **Totem de Atendimento**
4. **Fila de Atendimento**
   1. **Visão Geral**
   2. **Guichê**
   3. **Filtro de Unidade de Atendimento**
   4. **Chamar Paciente**
   5. **Iniciar atendimento**
   6. **Cancelamentos**
      1. **Cancelar chamada**
      2. **Cancelar senha**
   7. **Filtro Especialidade**
5. **Registro Simplificado**
   1. **Paciente**
      1. **Identificação**
      2. **Documentos**
      3. **Endereço**
      4. **Responsável financeiro**
   2. **Procedimentos**      i. **Procedimentos** ii**. Guias**
   3. **Responsável Paciente**
   4. **Documentos**
   5. **Pendências**
   6. **Pagamento**
   7. **Conclusão**

Registro de atendimento simplificado1Visão Geral

## **01. VISÃO GERAL**

Registro de atendimento simplificado

2Pré-Requisitos

## **02. PRÉ-REQUISITOS**

Parâmetros e permissõesParâmetros

## **a. PARÂMETROS**

  

Para utilizar o Registro de atendimento simplificado e a Fila de Atendimento é necessário indicar no cadastro do totem gerador de senhas que ele utilizará Registro de Atendimento Simplificado. Para isso acesse: Cadastros > Registro e Controle > Outros cadastros > Totem.

Marque o parâmetro **Usa Registro Atendimento Simplificado**.

No cadastro da Unidade de Atendimento atribuída ao Totem é necessário que alguns parâmetros estejam marcados para emissão de senha.

Marque o parâmetro **Utiliza senha de atendimento, Utiliza o Painel de Atendimentos Eletivos e Realiza chamada de senha no registro de atendimento**.  
**Não** pode estar definido como **Atendimento Automático**, as opções devem estar desmarcadas.

Permissões

## **b. PERMISSÕES**

Serviços Globais > Segurança > Acesso > Perfis > Acesso a Menus

Premissas

## **c. PREMISSAS**

Os dados da aba **Informções ANS - TISS**, podem ser preenchidos manualmente ao editar ou automáticamente, para isso é necessário configurar os **Valores Padrão para Atendimento TISS**, para saber mais consulte

3Totem de Atendimento

## **03. TOTEM ATENDIMENTO**

InformaçõesTotem de Atendimento

## **a. Totem de Atendimento**

Com o TOTEM devidamente configurado, o usuário deverá abrir a tela "TOTEM de Atendimento" através do Menu: **Atendimento → Totem de Atendimento**

O fluxo do painel foi alterado parcialmente no final do processo. Ao selecionar a especialidade, o usuário será solicitado que informe o seu CPF, após informar, o usuário será direcionado para uma nova tela solicitando a confirmação do CPF, caso o CPF esteja correto, o usuário irá clicar no botão do CPF, caso contrário o usuário terá a opção de cancelar para que seja possível realizar a correção do mesmo.

Após confirmação do CPF o sistema tentará buscar o paciente na base de dados, caso o paciente ja tenha cadastro, o sistema segue o fluxo normal, caso não seja identificado, internamente será cadastrado um paciente PADRÃO apenas com o CPF informado e com o nome "Paciente Sem Checkin".

4Fila de atendimento

## **04. FILA DE ATENDIMENTO**

InformaçõesVisão Geral

## **a. Visão Geral**

A fila de atendimento irá mostrar ao usuários as senhas que foram retiradas (ontem e hoje), sua prioridade, informações do paciente e horários. O usuário poderá visualizar uma lista dos clientes que pegaram senha no totem para posteriormente realizar o cadastro de maneira organizada e eficiente. Através do filtro Unidade de Atendimento é possível filtrar a lista de senha pela unidade de atendimento em que ela foi retirada. Além disso, pode-se definir o guichê em que o usuário se encontra para realizar chamadas de senha no painel de chamadas.

**Senha:** Número da senha retirada no Totem.

**Prioridade:** Indica a prioridade do atendimento (**N**-Normal, **P**-Prioritário ou **P80**-Prioritário acima de 80 anos).

**Status:**Status da senha (Aguardando, Chamando e Em Atendimento), senhas inativas não aparecerão na fila de atendimentos.

**Nome:**Nome do paciente, caso tenha sido informado o CPF e tenha gerado o pré-registro de atendimento no momento de retirada da senha.

**Unidade:**Unidade de atendimento onde retirou a senha.

**Tempo de espera:**Tempo de espera contato a partir da retirada da senha no totem.

**Especialidade do agendamento**: Indica qual a especialidade do agendamento. Pacientes sem agendamento terão a especialidade escolhida ao retirar a senha.

**Agendamento:** Caso existam agendamentos do paciente para o dia, irá aparecer o primeiro horário encontrado.

**Ações:** Ações que o usuário pode realizar (Chamar paciente, Iniciar atendimento, Cancelar chamada e Cancelar senha).

Guichê

## **b. GUICHÊ**

O campo guichê permite que o usuário visualize e/ou edite o nome do guichê que irá ser chamado no painel de chamadas ao realizar a ação **c.** **Chamar paciente**.

Para atualizar o nome basta alterá-lo no campo de texto e clicar no botão **Atualizar Guichê**.

Filtro Unidade de Atendimento

## **c. FILTRO UNIDADE DE ATENDIMENTO**

Através do filtro Unidade de Atendimento é possível filtrar a lista de senha pela unidade de atendimento em que ela foi retirada. 

Observação

Apenas serão exibidas as senhas que foram retiradas em um TOTEM configurado para usar atendimento simplificado.

Chamar paciente

## **d. CHAMAR PACIENTE**

Chama a senha escolhida no Painel de Chamadas, informando o nome do Guichê.

A ação de chamar paciente ficará disponível apenas quando o status da senha esteja **Aguardando**.

Iniciar Atendimento

## **e. INICIAR ATENDIMENTO**

Após chamar o paciente será possível iniciar atendimento. 

A ação de iniciar atendimento ficará disponível apenas quando o status da senha esteja **Chamando**.

Ao clicar em "Iniciar Atendimento":

* Se o paciente possuir **mais de um agendamento** para a mesma data, o sistema exibirá a tela de seleção:

            Selecione o agendamento desejado para vinculá-lo ao atendimento. Caso nenhum agendamento seja selecionado o botão "Aplicar" ficará desabilitado.

* Após a seleção, o sistema avançará para a tela de **Convênio do Atendimento**.

**Preenchimento de Dados do Convênio:**

Os campos serão preenchidos automaticamente com as informações vindas do agendamento (vinculado anteriormente). O usuário tem a oportunidade de conferir, complementar ou corrigir os dados, sendo que qualquer alteração será replicada na ficha do agendamento para manter a integridade das informações.

Para um paciente Sem Checkin os campos aparecerão em branco.

**É obrigatório escolher o convênio.**

Após informar os dados de convênio, caso exista agendamento serão atualizados (convênio, plano, subplano nº da Carteirinha, Validade da carteirinha) os que foram selecionados anteriormente, o atendimento será criado com base no agendamento do paciente, realizando os lançamentos dos procedimentos que foram devidamente agendados, a partir da atividade selecionada e o código do procedimento definido nela.

A especialidade do atendimento criado será a mesma do agendamento, caso este exista. Se não houver agendamento, será atribuída a especialidade da senha retirada pelo paciente.

Importante

**O convênio SUS não é permitido no Registro de Atendimento Simplificado**, caso a senha tenha agendamento atrelado com o convênio SUS, o usuário será alertado e o convênio será desselecionado. A opção de convênio SUS não aparece para ser escolhida, independente de estar cadastrada.

Para registrar atendimentos que contenham consulta, é necessário realizar um agendamento antes de iniciar o atendimento para que as regras de cadastro de consulta sejam aplicadas.

Cancelamentos

## **f. CANCELAMENTOS**

## 

CancelamentosCancelar chamada

## **i.** **CANCELAR CHAMADA**

Interrompe a chamada da senha, retornando ela para o status de Aguardando.

Cancelar senha

## **ii.** **CANCELAR SENHA**

Inativa a senha escolhida, removendo ela da fila de atendimento.

Filtro Especialidade

## **g. FILTRO ESPECIALIDADE**

Através do filtro Especialidade é possível filtrar a lista de senhas pela **especialidade do agendamento**. Pacientes sem agendamento terão a especialidade escolhida ao retirar a senha.

Observação

Apenas serão exibidas as senhas que foram retiradas em um TOTEM configurado para usar atendimento simplificado.

5Registro Simplificado

## **05.** **REGISTRO SIMPLIFICADO**

Ao clicar no botão Iniciar atendimento será iniciado o registro simplificado.   
Caso a senha do paciente escolhido ainda seja válida, as informações aparecerão no topo da tela.

StepperPaciente

## **a. PACIENTE**

As informações do paciente serão carregadas e os campos ficarão disponíveis para edição caso os campos obrigatórios (CPF, Nome do paciente, Nome da mãe e Data de nascimento) estejam preenchidos.  
Ao mudar de campo o sistema irá atualizar automaticamente o cadastro do paciente (autosave).

Informações do PacienteIdentificação

## **i. IDENTIFICAÇÃO**

O prontuário ficará desabilitado para edição enquanto o atendimento não for iniciado / carregado.   
Após iniciar o atendimento, o campo permanecerá **desabilitado** (proibido editar) seguindo os parâmetros: **Controlado pelo Sistema** marcado ou **Igual ao Código do paciente** marcado ou **Utilizado no Pronto Atendimento** desmarcado.  
O Atendmiento é criado após a confirmação de dados do paciente e clicar em "Procedimentos". O controle volta a ficar completamente habilitado após o carregamento indicado no topo da tela.

O número do Prontuário também poderá ser gerado automaticamente baseado nos parâmetros da imagem acima.

ParâmetrosCarregar documentoCarregar documento

O botão **Carregar documento** permite ao usuário enviar fotos de documentos para extrair com o uso de IA informações como CPF, Nome, Nome da mãe, Sexo e data de nascimento de documentos como Identidade ou CNH.

O DTA suporta o carregamento dos seguintes formatos de arquivo: PDF, PNG, JPEG, JPG e WEBP.

Importante

Este recurso está disponível a partir da versão **12.1.2510.100** e em todas as versões superiores.

CPF

Caso o usuário tente alterar o CPF para outro valor, este será validado.

* Se for inválido:

* Se encontrar pacientes cadastrados com o CPF informado:  
    
    
    
  Se o usuário clicar em Cancelar, o modal é fechado e o valor anterior ao novo CPF será restaurado.  
  Ao escolher uma das opções o usuário habilita o botão Selecionar:  
    
    
    
  Caso o usuário clique em Selecionar, um modal de confirmação aparecerá explicando que as informações preenchidas até então serão trocadas pelas informações encontradas no cadastro do paciente selecionado.  
    
    
    
  Após confirmar ocorrerá o recarregamento da tela com as novas informações do paciente.
Documentos

## **ii. DOCUMENTOS**

Endereço

## **iii. ENDEREÇO**

Procedimentos

## **b. Procedimentos**

ProcedimentosProcedimentos

## **i. Procedimentos**

Nesta etapa serão exibidos todos os procedimentos do atendimento, agrupado pelo médico solicitante.

Os Cards agrupados exibem as informações:

* Convênio
* Procedimento / Descrição do procedimento
* Quantidade
* Número da Guia do Prestador

**Ações**

É possível, Editar, Cancelar e Incluir novos procedimentos.

**Incluir Procedimentos**

Ao clicar no botão Incluir procedimentos é aberta a tela para entrada dos dados.

Importante

Atualmente é possível incluir Exames, Taxa/Serviços e Consultas(Honorários).

Para registrar atendimentos que contenham consulta, é necessário realizar um agendamento antes de iniciar o atendimento para que as regras de cadastro de consulta sejam aplicadas.

A lista de procedimentos é carregada de acordo com o contrato vinculado ao convênio selecionado e ao tipo de procedimento que o usuário deseja incluir.

Caso o paciente queira incluir algum procedimento em um outro convênio diferente do informado no inicio do atendimento ou do agendamento, nesta tela é possível fazer essa inserção através do botão "+ Adicionar Carteira".

É possível já neste momento informar os dados de autorização caso necessário.

Os campos Número da Guia Operadora e Número da Guia Prestador, respeitam os parâmetros para habilitar ou desabilitar a edição. Essa configuração é realizada no contrato do convênio.

**Obs.** Os parâmetros "Número e data da GUIA / NOTA / COMPROVANTE sempre obrigatórios" e "Número da AUTORIZAÇÃO / SENHA e procedimentos autorizados sermpre obrigatórios", devem permanecer desabilitados no uso do atendimento simplificado.

Observação

Para que as informações de autorização estejam disponíveis para edição, é necessário que o parâmetro "***Incluir na Guia de autorização os exames solicitados para paciente externo e execução externa***"

**Editar:**

Para editar um registro é possível clicando no ícone lápis.

Uma tela similar a tela de incluir procedimento será aberta, porém algumas informações não são possíveis de serem editadas.

No caso de um convênio particular apenas o campo quantidade está disponível para edição, os campos de autorização e solicitante médico não são exibidos.

**Cancelar**

Para cancelar um procedimento, é possível fazer clicando no ícone lixeira (cancelar).

Uma tela de confirmação será exibida conforme abaixo:

Ao confirmar, o item será cancelado e deixará de ser exibido na tela de procedimentos.

**Parametrizações:**

Para conseguir incluir um procedimento do tipo exame, o parâmetro "***Obriga Responsável pelo exame no atendimento externo***" deve esta desmarcado.

Guias

## **ii. Guias**

As guias são exibidas de acordo com os procedimentos incluídos na etapa anterior (i. Procedimentos)  
É possível autorizar todas as guias que estão com status  (A solicitação de autorização segue as regras de [Solicitar Autorização](https://tdn.totvs.com/pages/viewpage.action?pageId=773516749#:~:text=Acessar%3A%20Atendimento%20%3E%20Recep%C3%A7%C3%A3o%20%3E%20Registro,guia%20%3E%20Processos%20%3E%20Solicitar%20Autoriza%C3%A7%C3%A3o.) e [Guias de Autorização](https://tdn.totvs.com/pages/viewpage.action?pageId=520672299))

Dentro de cada card é possível:  
*Solicitar Autorização (somente da guia selecionada seguindo as regras de [Solicitar Autorização](https://tdn.totvs.com/pages/viewpage.action?pageId=773516749#:~:text=Acessar%3A%20Atendimento%20%3E%20Recep%C3%A7%C3%A3o%20%3E%20Registro,guia%20%3E%20Processos%20%3E%20Solicitar%20Autoriza%C3%A7%C3%A3o.)))*  
*Visualizar Histórico*  
*Cancelar Autorização*

**Vizualizar Histórico:** Exibe o histórico de solicitações da guia selecinada caso exista alguma solicitação  
  
  
  
**Cancelar Autorização:** Cancela a solicitação de autorização 

Prestador Faturamento

## **ii****i****. Prestador de faturamento para atendimento de exame**

O atendimento simplificado aplica uma regra automática para determinar quem é o prestador de faturamento para lançamento em conta.

A regra irá tentar lançar o prestador configurado no cadastro da unidade de atendimento de execução do exame, aba exames e campo prestador executante. 

Caso essa informação não esteja configurada o RM irá seguir os critérios abaixo:

Quando informado no agendamento o prestador:

* Será determinado o prestador informado no agendamento

Quando não for informado o prestador no agendamento:

* Será dererminado o prestador configurado no campo prestador principal, aba Identificação do cadastro da unidade de faturamento associada a a unidade de execução do exame.

Prestador responsável pedido de exame

## **i****i****i****i****. Prestador responsável do pedido de exame**

O atendimento simplificado faz de forma automática a associação do prestador informado no agendamento ao pedido de exame como prestador responsável, caso essa informação não seja cadastrada o campo ficará vazio para que seja informado no processo de realização do exame.

Responsável paciente

## **c. Responsável Paciente**

Nesta etapa o responsável pelo paciente é definido, que também será responsável pelo financeiro e autorizações necessárias para o paciente.

É possível incluir, editar ou excluir responsáveis para o paciente.

O tipo do responsável pode ser Próprio Paciente, onde todas as informações do paciente são copiadas.

Os outros tipos habilitam o botão de **Preencher com endereço do paciente,** que copia as informações do endereço do paciente, geralmente utilizada para os tipos pai ou mãe.

Se o parâmetro que define o próprio paciente como responsável também estiver marcado, o mesmo será registrado automaticamente como responsável, a menos que seja menor de idade.   
Nessa caso um alerta é enviado ao usuário:

Documentos

## **d. Documentos**

Nesta etapa é possível anexar qualquer tipo de documento que seja necessário para o atendimento. (opcional)  
*Ex: Guia de convenio, Resultado de exame, imagem ou foto e etc.*

Para incluir documentos basta clicar em incluir.

Será exibido um modal conforme o exemplo abaixo para inclusão de documentos.

> 1 - Nome do Arquivo  
> 2 - Formato - Extensão do arquivo  
> 3 - Selecionar arquivo - Selecionar o arquivo diretamente do computador do usuário
>
> 4 - Escanear - Integração com scanner para digitalização do arquivo  
> 5 - Descrição - detalhe do arquivo  
> 6 - Tipo documento - Tipo de documento associado ao controle de documentos do RM  
> 7 - Enviar - Realizar o upload dos documentos para base de dados.

A rotina permitirá também a digitalização de documentos desejados por meio de um scanner.

**Essa funcionalidade está disponível a partir da versão 12.1.2506.**

Ao clicar no botão será exibido uma notificação de escaneamento

Concluído o escaneamento, o arquivo será exibido e seu formato será definido automaticamente como PDF

Após preencher os campos, enviar e fechar o modal a tela de documentos é atualizada retornando todos os documentos para o atendimento selecionado.  
  
É possível Visualizar, Baixar ou Excluir o documento desejado.

**Visualizar:** Exibe um modal com o documento selecionado.

**Baixar:** Realiza download do documento selecionado

**Excluir:** Exclui o documento selecionado.  
(Necessário configurar permissão para exclusão de documentos nas permissões por perfil.)  
  
  
Apos a exclusão a tela de documentos é atualizada retornando somente os documentos do atendimento selecionado.

Pendências

## **e. Pendências**

Na etapa de pendências é possível criar pendências para armazenar informações importantes que devem ser consideradas no registro de atendimento.   
Deve-se indicar a qual Convênio a pendência será atribuída e qual o tipo de pendência (Cadastradas na tela Cadastros > Faturamento > Outros Cadastros > Pendências). O tipo pode ser impeditivo ou risco gerenciável.

Após salvar, um card será criado contendo as principais informações da pendência, como seu status, convênio e tipo.

Três ações são possíveis para pendências com status PENDENTE:

1. Resolver: Marca a pendência como resolvida, mudando seu status. Pendências resolvidas não podem ser editadas ou canceladas.
2. Editar: Permite ao usuário editar o conteúdo da pendência.
3. Cancelar: exclui uma pendência não resolvida.

Pagamentos

## **f. Pagamento**

Na etapa de pagamento serão apresentados para o usuário os itens de gasto particular ou coparticipação.

PagamentosPagar

## **i. PAGAR**

Itens com Status em Aberto ou Parcialmente Baixado podem ser selecionados para Pagar.  
**É necessário especificar o responsável pelo paciente que irá realizar o pagamento.**

As opções apresentadas são as mesmas cadastradas na etapa de Responsável Paciente.

Itens selecionados para pagar são agrupados dentro de uma Parcial, não podendo serem pagos separadamente.  
Após a criação da parcial, informações sobre o movimento financeiro e seu lançamento serão apresentados para o usuário.

Após clicar em pagar a **Sessão de Caixa 2.0** do Financeiro será aberta para realizar o pagamento.

Na sessão de caixa é possível determinar as formas de pagamento que o cliente deseja e confirmar pagamento:

**Observação:** qualquer problema que ocorrer durante a utilização da sessão de caixa deve ser ajustado dentro de BackOffice > Gestão Financeira > Caixa.

Após o pagamento realizado com sucesso, é importante clicar no botão Atualizar para que os itens de gasto tenham seus status atualizados.

Neste exemplo, teremos o status alterado para Baixado:

Desconto

## **ii. DESCONTO**

É possível aplicar e remover descontos antes do pagamento.  
  
  
Os descontos podem ser aplicados de duas formas.

* Por VALOR :
* Por PORCENTAGEM:

**Importante:** Os descontos não se mantem após atualizar a lista de itens de gasto ou pagar algum dos itens.   
Será necessário reaplicar caso deseje dar desconto em um item que não foi selecionado para pagamento.  
Ao adicionar um desconto sobre o valor de um item, o desconto não é aplicado automaticamente nas parciais.

Conclusão

## **g. Conclusão**

Etapa de conclusão irá retornar os dados do atendimento e paciente para verificação dos dados informados.  
  
Nesta etapa é possível imprimir documentos configurados em Unidade de Atendimento > aba: Relatórios

**Concluir:** O atendimento **eletivo** é atualizado para fila do médico em **Painel de Atendimentos Eletivos**e o status dos agendamentos é atualizado para **Sala de espera**  
                O atendimento **urgente **(paciente sem checkin)**** é atualizado para fila do médico em **Painel de Classificação de Risco**

**IMPORTANTE:** Caso o parâmetro de convênio **"Geração de movimento financeiro/caixa no ato do registro de atendimento"** estiver habilitado no cadastro do convênio, não será possível concluir o atendimento enquanto tiver itens de gasto com status não-baixados na etapa de Pagamento.

Informações do Paciente
