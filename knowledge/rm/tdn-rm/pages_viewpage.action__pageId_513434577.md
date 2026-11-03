---
content_hash: 687958b79a774b73b4690eccc5f175570d41f608b18f5bc967000987c9c15bf2
fetched_at: '2026-06-29T00:10:26.235578+00:00'
page_id: '513434577'
product: rm
source: tdn-rm
title: TOTVS Gestão Hospitalar > Atendimento > Painel de Atendimentos Eletivos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=513434577
version: 21
---

## **ÍNDICE**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Telas do painel de atendimento eletivo**
4. **Tela de cadastro da unidade de atendimento**
5. **Fila de Exames**

sumarioVisão Geral

## **01. VISÃO GERAL**

Nessa opção é possível verificar todos os atendimentos classificados como Eletivos, utilizando filtros. É possível também acessar o Prontuário dos pacientes.

## **02. EXEMPLO DE UTILIZAÇÃO**

* **Aba atendimento > Pronto atendimento > Painel de Atendimento Eletivo**

Telas do painel de atendimento eletivo 

## **03. TELA DO PAINEL DE ATENDIMENTO ELETIVO**

* **Ao abrir a nova tela, selecione a unidade de atendimento**
* **Selecione o médico caso queira a informação completa**

* **Selecione a opção OK**

**Aba Registro de Atendimentos.**

A tela exibe os pacientes de acordo com a ordem e prioridade das senhas emitidas no totem.  
Para realizar uma chamada automática, utilize o botão **Chamar**, que selecionará a próxima senha da fila seguindo os critérios de prioridade.  
É possível também chamar um paciente fora da sequência: basta clicar duas vezes no registro desejado na listagem (grid). Lembre-se que esta ação depende de uma configuração específica nas **Configurações Globais** do sistema.

**Status das senhas**

* **Chamando:** o paciente foi chamado mas ainda não se apresentou para o atendimento.
* **Inicio do Registro de Atendimento:** o paciente está junto com o atendente para geração do Registro do atendimento.
* **Paciente gerou senha de Atendimento:** o paciente gerou a senha e está na fila, aguardando ser chamado.

**Alteração de prioridade.**

Ao clicar com botão direito do mouse sobre a senha desejada é possivel em todas as abas alterar a prioridade da senha ou remover a prioridade da senha.

Tela de cadastro da unidade de atendimento

## **04. TELA DE CADASTRO DA UNIDADE DE ATENDIMENTO**

Todos os parâmetros relacionados à Painéis foram removidos das abas de **Identificação e Outros Dados** e passados para uma aba especifica chamadas **Painéis**.

É importante, caso exista alguma documentação relacionada ao Cadastro da Unidade de Atendimento, fazer a alteração das imagens com a localização desses parâmetros.

Ficou assim

Aba Painéis:

Na imagem acima temos marcado quais são os parâmetros importantes para que a Fila de Exames funcione corretamente.

**Utiliza senha de atendimento** (para que seja possível retirar a senha no totem).

**Utiliza o Painel de Atendimentos Eletivos** (pois a fila de exames é apenas para agendamentos).

**Realiza Chamada de senha no registro de atendimento** (pois é necessário registrar o atendimento e selecionar quais os agendamentos de exames que serão utilizados).

**Utiliza Fila de Exames** Marca que a unidade de atendimento utiliza fila de exames, é obrigatório que a UNIDADE EXECUTORA DE EXAME (configurada no cadastro do exame) também possua esse parâmetro marcado para que o exame seja inserido na fila de exame e a senha seja chamada no Painel de Senhas.

Fila de ExamesFila de Exames

## **05. FILA DE EXAMES**

Fila de ExamesConfiguração

No cadastro da Unidade de atendimento, na aba Paineis existe o parametro **Utiliza Fila de Exames** que marca que a unidade de atendimento utiliza fila de exames, é obrigatório que a UNIDADE EXECUTORA DE EXAME (configurada no cadastro do exame) também possua esse parâmetro marcado para que o exame seja inserido na fila de exame e a senha seja chamada no Painel de Senhas.

Para os exames de imagem, é necessário que a flag **"Utiliza Laudo Pré-Impresso"** esteja **habilitada**. Essa configuração fica em: **Cadastros > Unidade de Diagnóstico > Exames e Serviços,** Aba **Configurações do Exame.**

É obrigatório que exista um agendamento de exames (imagem e/ou laboratorial) na UNIDADE de atendimento em que será realizado o registro do atendimento (Retirada de Senha do Totem).

Todo agendamento deve contar um SALA selecionada. É OBRIGATORIO configurar dentro da agenda em **OPÇÕES > Períodos > Dia > *Horários*** do período e escolher qual a SALA que será utilizada para esta agenda no dia. Desta forma está SALA será o LOCAL (Guiche) chamado no PAINEL de senhas para realização do exame.

É importante ressaltar que os exames podem ser executados em unidades distintas à unidade em que o atendimento for registrado, por exemplo, numa Central de Exames, onde o atendimento é realizado nela e direcionado a outra unidade para execução.

Após retirar a senha do totem para a UNIDADE em que foi realizado o agendamento.

O paciente será chamado no painel para registrar o atendimento:

Observa-se que a senha de registro de atendimento é chamada no Painel de Senhas da unidade de atendimento em que a senha foi REGISTRADA.

A tela de agendamento irá abrir para selecionar um OU mais agendamentos de exames para registrar atendimento e assim inserir os exames na fila de exames,

se as unidades executoras cadastradas utilizarem a fila de exames.

**Após registrar o atendimento, os exames constando nos agendamentos aparecerão na Fila de Exames associados à senha que o paciente retirou no Totem.**

Fila de Exames

A Fila de Exames é utilizada para controlar separadamente todos os exames que uma mesma senha irá realizar.

Exames de laboratório são realizados ao mesmo tempo, portanto todos serão agrupados em um único exame “Exames Laboratoriais”, enquanto os exames de

Imagem aparecerão separados e identificados.

Os exames podem aparecer em três status na fila de exame, Aguardando, Em atendimento e Finalizado. Ao marcar e desmarcar o checkbox você filtra quais tipos aparecerão.

Existem dois botões, **Chamar e Finalizar**.

Botões de açãoChamar Senha

O Botão Chamar é utilizado para chamar os pacientes no Painel de Senhas, passando os exames para o status de Chamando.

Obs: Dois clicks na linha do exame que você quer Chamas geram o mesmo comportamento de clicar no botão Chamar.

**Só pode haver um exame de uma mesma senha Chamando ou Em Atendimento.**  
Caso tente chamar um exame enquanto outro esteja já Chamando ou Em atendimento, uma mensagem de erro é mostrada.

Caso tente chamar um exame que já está Em atendimento ou Finalizado, uma mensagem de erro é mostrada.

Ao clicar em Chamar, uma janela aparecerá para o usuário, nela haverá o campo Sala, que estará preenchido automaticamente e bloqueado caso a agenda seja do tipo SALA ou o agendamento já tenha esta informação preenchida. Caso a Sala não esteja preenchida o lookup estará habilitado para escolher a Sala desejada.

Ao clicar em **sim,** confirmando a chamada da senha, a senha aparecerá no Painel de Senhas da Unidade de Atendimento Executora indicado na Fila de Exames, utilizando o nome da Sala presente no agendamento e/ou selecionada na tela anterior mostrada na Fila de Exames como sendo o Guichê / Local de execução.

Obs: A Coluna Exames no painel de senha mostra as senhas que foram chamadas pela Fila de Exames.

Além disso, após clicar **sim**, o modal de Iniciar Exame será apresentado.

Caso o usuário clique **não** o modal será fechado.

Caso o status do exame seja **Chamando**, ao clicar **Chamar** a senha será chamada novamente automaticamente e a tela de Iniciar Exame será apresentada.

Iniciar Exame

Iniciar exame:

É necessário escolher o Executante de Exame que será responsável pela execução do mesmo.

A confirmação deve ser feita apenas após a apresentação do paciente, consequentemente alterando o status do exame para Em Atendimento e o Executante selecionado aparecerá na Fila de Exames associado ao Exame. Após ser atendido o status do agendamento é alterado para **Em Atendimento**.

Definir Prestador como Executante

Para definir os prestadores que serão Executantes de Exame, é necessário ir até o cadastro do Prestador e adicionar o Tipo de Prestador 15 (Executante de Exames).

Somente aparecerão na busca os prestadores que contenham esse tipo adicionado.

FinalizarFinalizar

Após terminar a execução do exame, devemos Finalizar o mesmo.

Apenas é possível Finalizar exames Em Atendimento. Caso tente, a seguinte mensagem aparecerá.

Ao Finalizar um exame Em Atendimento, aparecerá uma confirmação para evitar erros.

Ao Clicar Sim, o status no exame passa a ser Finalizado.

Ao Finalizar **TODOS** os exames associados à senha, todos eles estarão Finalizados e serão removidos da Fila de Exames. O status do agendamento passa a ser **Atendido**.

Observações de cancelamentoObservações

Caso o Registro de Atendimento seja cancelado, todos os exames associados a ele serão removidos da Fila de Exames.

Caso um Pedido de Exame seja cancelado, todos os exames associados a ele serão removidos da Fila de Exames.

Caso um exame de imagem seja cancelado, ele será removido da Fila de Exames. Para remover exames de laboratório, por terem sigo agrupados, é necessário cancelar o Pedido de exame contendo o mesmo.
