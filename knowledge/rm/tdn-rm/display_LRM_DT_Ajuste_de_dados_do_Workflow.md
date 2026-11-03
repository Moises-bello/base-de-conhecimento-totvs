---
content_hash: 49fbd6addb69d1e68afc24e601097b60c57a64d8410fe139c356562eb5c61486
fetched_at: '2026-06-29T00:06:23.468254+00:00'
page_id: '224103082'
product: rm
source: tdn-rm
title: DT_Ajuste_de_dados_do_Workflow
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Ajuste_de_dados_do_Workflow
version: 2
---

# AJUSTE DE DADOS DO WORKFLOW

## Características do Requisito

  

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão de Pessoas* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Serviços Globais* | *Requisições* | |
| **Versões/Release:** | *12.1.9* |

## Descrição

Este documento descreve um conjunto de recursos do TOTVS Gestão de Pessoas que permite ao usuário ajustar informações em requisições que já estejam no fluxo ou aprovadas.

***Implementações:***

**Alteração do responsável pela aprovação** da requisição serve para o caso de alguém se desligar da empresa, mudar de seção ou simplesmente deixar de ser o responsável pela aprovação da requisição por qualquer outro motivo.  
Em requisições de **Aumento de Quadro, Substituição e Transferência** já aprovadas, mas ainda não concluídas**,**a**alteração da Seção** informada na requisição, serve para o caso de ocorrer acordo de troca de vagas entre diferentes seções dentro de uma mesma filial.  
Em requisições de **Aumento de Quadro** e **Substituição** já aprovadas mas ainda não concluídas, a alteração da **Função e/ou Salário e/ou Tabela Salarial** informados na requisição, serve para que um Gestor por qualquer razão superveniente à aprovação da requisição decida pela modificação destas informações.

O cadastro de **Perfil de Vagas** possibilita a **associação de uma requisição mesmo que a Função informada na requisição seja distinta daquela informada no Perfil de Vaga.** Essa funcionalidade visa atender os casos em que o recurso humano a ser contratado, possa atender à vaga em aberto mesmo que a Função para qual foi contratado não seja exatamente aquela definida no processo de seleção. 

***Caminhos:***

* RH / Gestão de Pessoas / Planejamento e Captação / Requisições / Aumento de Quadro / Processos / Alterar Aprovador Atual
* RH / Gestão de Pessoas / Planejamento e Captação / Requisições / Substituição / Processos / Alterar Aprovador Atual
* RH / Gestão de Pessoas / Desenvolvimento / Requisições / Treinamento / Processos / Alterar Aprovador Atual
* RH / Gestão de Pessoas / Desenvolvimento / Requisições / Abertura de Turmas / Processos / Alterar Aprovador Atual
* RH/ Gestão de Pessoas / Valorização / Requisições / Alteração de Dados Funcionais / Processos / AlterarAprovador Atual
* RH / Gestão de Pessoas / Valorização / Requisições / Transferência / Processos / Alterar Aprovador Atual
* RH / Gestão de Pessoas / Valorização / Requisições / Transferência com Alteração de Dados Funcionai / Processos / Alterar Aprovador Atual
* RH / Gestão de Pessoas / Valorização / Requisições / Transferência em Lote / Processos / Alterar Aprovador Atual
* RH / Gestão de Pessoas / Gestão Organizacional / Requisições / Requisição Geral / Processos / AlterarAprovador Atual
* RH / Gestão de Pessoas / Gestão Organizacional / Requisições / Requisição de Desligamento / Processos / Alterar Aprovador Atual
* RH / Gestão de Pessoas / Planejamento e Captação / Requisições / Aumento de Quadro / Processos / Alterar dados da Requisição
* RH / Gestão de Pessoas / Planejamento e Captação / Requisições / Substituição / Processos / Alterar dados da Requisição
* RH / Gestão de Pessoas / Valorização / Requisições / Transferência / Processos / Alterar dados da Requisição
* RH / Gestão de Pessoas / Planejamento e Captação / Painel de Seleção / Vagas da Seleção / Anexos / Requisições do Perfil de Vaga / Requisições da Vaga / Campo Código da Requisição

## Procedimento para Utilização

## Assistentes para ajuste de dados de requisição

Alterar Aprovador Atual: Permite alterar o aprovador  
Alterar Dados da Requisição: Permite alterar seção, função e salário.

| Tipo de Requisição | Alterar Aprovador | Alterar Seção | Alterar Função e/ou Salário |
| --- | --- | --- | --- |
| Abertura de Turmas | X |  |  |
| Alteração de Dados Funcionais | X |  |  |
| Aumento de Quadro | X | X | X |
| Desligamento | X |  |  |
| Geral | X |  |  |
| Substituição | X | X | X |
| Transferência | X | X |  |
| Transferência com Alteração de Dados Funcionais | X |  |  |
| Transferência em Lote | X |  |  |
| Treinamento | X |  |  |

Para executar qualquer um dos dois assistentes, **apenas 1 (uma)** requisição deverá ser selecionada na visão.

Ao iniciar o processo de alterar o aprovador atual, a aplicação irá validar o **Status** da requisição selecionada.  
A execução do assistente ocorre somente se a requisição selecionada estiver no fluxo de atendimento e o status **Em Andamento**.  
O não atendimento dessa condição irá exibir uma mensagem ao usuário e o processo não será executado.

**Mensagem de validação**: "Não é possível alterar o Aprovador Atual da requisição selecionada porque ela ainda não está no fluxo de atendimento. Para colocá-la no fluxo utilize a opção Processos / Inserir no Fluxo".

Para novo aprovador: Todos os funcionários da mesma coligada e filial da requisição. (Origem de dados é a mesma da tela de funcionários em RH / Gestão de Pessoas / Acompanhamento / Funcionários).

Se o campo Novo Aprovador estiver em branco ou com o mesmo valor do campo Aprovador Atual e/ou o campo Motivo estiver em branco, o sistema não permitirá o avanço da etapa e o usuário será informado por meio de uma mensagem de alerta.  
Se o Novo Aprovador informado não é um Atendente, o sistema não permitirá o avanço da etapa e o usuário será informado por meio de uma mensagem de alerta. Para torna-lo um atendente, é necessário que seja executado o assistente em RH / Gestão de Pessoas / Configurações / Criar Atendente no RM Agilis.

Quando o Aprovador Atual for atualizado, será criado um parecer registrando na requisição a mudança do responsável pela aprovação.

Se ocorrer um erro desconhecido durante a execução do processo irá aparecer uma mensagem informando o motivo.  
Se ocorrer uma validação que impeça a conclusão do processo, o sistema mostrará uma mensagem informando.

Ao iniciar o processo de Alterar dados da Requisição, a aplicação irá validar o status.  
A execução do assiste ocorre somente se a requisição selecionada estiver com o status APROVADO.  
O não atendimento dessa condição ira exibir uma mensagem ao usuário e o processo não será executado.

**Mensagem de validação**: "Não é permitido a mudança de Seção para requisições que não estejam aprovadas"

A etapa de assistente permite alterar a Seção informada na requisição. O usuário pode optar por manter a Seção informada, deixando o campo em branco e clicando em Avançar.

**Filial e Seção**: Correspondem aos dados existentes na tela de cadastro de requisição. Os valores "default" são os mesmos que estiverem preenchidos no grupo "Seção Atual".

A etapa de alteração de função e/ou salário e/ou tabela salarial só será apresentada se a requisição selecionada for de Aumento de Quadro / Substituição.  
Esta etapa permite o usuário alterar os dados relativos à Função e Salário (incluindo os dados da Tabela Salarial).

Para habilitar os campos relacionados com Tabela Salarial (Nível e Faixa), o sistema tem que estar parametrizado para utilizar Tabela Salarial (RH / Gestão de Pessoas / Configurações / Parametrizador / 07.00 Configurações / 07.00.00 Gerais / 07.00.00.01 / Validações / Remuneração / Considerar os salários das tabelas salariais).

Os campos do grupo "Proposta de Alteração" não podem conter os mesmos valores dos campos do grupo "Dados atuais do funcionário". Caso isso ocorra, o usuário será impedido de avançar a etapa e será exibido a mensagem ''A proposta de alteração de Função e/ou Salário não pode conter os mesmos valores que estão atualmente atribuídos ao funcionário!".

Na etapa de Parecer, o usuário deve informar quem foi o responsável pela autorização de alteração dos dados da requisição.

Caso ocorra um erro desconhecido durante a execução do processo, irá aparecer uma mensagem de erro informando o motivo.  
Se ocorrer uma validação que impeça a conclusão do processo, irá aparecer uma mensagem de atenção informando as ressalvas.

**Informações Complementares: Toda regra do processo de aprovação e conclusão da requisição deve ser mantida, incluindo aquelas relacionadas a controle de lotação, que no caso de modificação de Seção surtirá efeitos na nova Seção informada.**
