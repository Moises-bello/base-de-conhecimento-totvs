---
content_hash: 7372f56c35112a4db6a9a3019a941bc10d34ffaac6051142562ada5bcd580b5a
fetched_at: '2026-06-29T00:06:03.620523+00:00'
page_id: '200901574'
product: rm
source: tdn-rm
title: ER_Ajuste_de_dados_do_Workflow
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_Ajuste_de_dados_do_Workflow
version: 47
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## 

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Pessoas | **Módulo** | RHU |
| **Segmento Executor** | CONSTRUÇÃO E PROJETOS | | |
| **Projeto1** | RHU - DESENVOLVIMENTO RHU007 | **IRM1** | PCREQ-6304 |
| **Requisito1** | PCREQ-6308 | **Subtarefa1** | PDR\_RHU\_RHU007-2 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.9 | **Réplica** |  |
| **País** | (x) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** |  | | |

## Objetivo

Este documento descreve um conjunto de recursos que serão adicionados ao **TOTVS Gestão de Pessoas**, com o objetivo de permitir a um usuário, com a devida autorização de acesso, ajustar informações em requisições que já estejam no fluxo ou aprovadas.

Essa implementação se faz necessária devido às seguintes demandas:

* **Alteração do responsável pela aprovação** da requisição, considerando que ele pode vir a se desligar da empresa, mudar de seção ou simplesmente deixar de ser o responsável pela aprovação da requisição por qualquer outro motivo.
* Em requisições de **Aumento de Quadro, Substituição e Transferência** já aprovadas, mas ainda não concluídas**,** a **alteração da Seção** informada na requisição, considerando que pode ocorrer acordo de troca de vagas entre diferentes seções dentro de uma mesma filial.
* Em requisições de **Aumento de Quadro** e **Substituição** já aprovadas, mas ainda não concluídas, a alteração da **Função e/ou Salário e/ou Tabela Salarial** informados na requisição, considerando que um Gestor, por qualquer razão superveniente à aprovação da requisição decida pela modificação destas informações.

Também será modificado o cadastro de **Perfil de Vagas**, para possibilitar a **associação de uma requisição mesmo que a Função informada na requisição seja distinta daquela informada no Perfil de Vaga**, visando atender os casos em que o recurso humano a ser contratado, que trata a requisição, pode atender à vaga em aberto mesmo que a Função para qual foi contratado não seja exatamente aquela definida no processo de seleção.

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Alterar Aprovador Atual | Criação | * RH > Gestão de Pessoas > Planejamento e Captação > Requisições > Aumento de Quadro > Processos > Alterar Aprovador Atual * RH > Gestão de Pessoas > Planejamento e Captação > Requisições > Substituição > Processos > Alterar Aprovador Atual * RH > Gestão de Pessoas > Desenvolvimento > Requisições > Treinamento > Processos > Alterar Aprovador Atual * RH > Gestão de Pessoas > Desenvolvimento > Requisições > Abertura de Turmas > Processos > Alterar Aprovador Atual * RH > Gestão de Pessoas > Valorização > Requisições > Alteração de Dados Funcionais > Processos > Alterar Aprovador Atual * RH > Gestão de Pessoas > Valorização > Requisições > Transferência > Processos > Alterar Aprovador Atual * RH > Gestão de Pessoas > Valorização > Requisições > Transferência com Alteração de Dados Funcionais > Processos > Alterar Aprovador Atual * RH > Gestão de Pessoas > Valorização > Requisições > Transferência em Lote > Processos > Alterar Aprovador Atual * RH > Gestão de Pessoas > Gestão Organizacional > Requisições > Requisição Geral > Processos > Alterar Aprovador Atual * RH > Gestão de Pessoas > Gestão Organizacional > Requisições > Requisição de Desligamento > Processos > Alterar Aprovador Atual | Descrito abaixo no item 1. |
| Alterar Seção | Criação | * RH > Gestão de Pessoas > Planejamento e Captação > Requisições > Aumento de Quadro > Processos > Alterar dados da Requisição * RH > Gestão de Pessoas > Planejamento e Captação > Requisições > Substituição > Processos > Alterar dados da Requisição * RH > Gestão de Pessoas > Valorização > Requisições > Transferência > Processos > Alterar dados da Requisição | Descrito abaixo no item 1. |
| Requisições da Vaga | Alteração | RH > Gestão de Pessoas > Planejamento e Captação > Painel de Seleção > Vagas da Seleção > Anexos > Requisições do Perfil de Vaga > Requisições da Vaga > Campo Código da Requisição | Permitir listar requisições cuja a Função seja diferente daquela informada no cadastro do Perfil de Vaga |

# 1. Assistentes para ajuste de dados de requisição

Serão desenvolvidos dois assistentes, destinados a permitir a alteração, respectivamente, das seguintes informações de acordo com os seguintes tipos de requisição listados na tabela abaixo:

* **Assistente 1: Alterar Aprovador Atual**
  + **Permitirá alterar o Aprovador**
* **Assistente 2: Alterar dados da Requisição**
  + **Permitirá alterar Seção**
  + ****Permitirá alterar**Função**
  + ****Permitirá alterar**Salário**

| Tipo de Requisição | Alterar Aprovador | Alterar Seção | Alterar Função e/ou Salário |
| --- | --- | --- | --- |
| Aumento de Quadro | X | X | X |
| Abertura de Turmas | X |  |  |
| Alteração de Dados Funcionais | X |  |  |
| Desligamento | X |  |  |
| Geral | X |  |  |
| Substituição | X | X | X |
| Transferência | X | X |  |
| Transferência com Alteração de Dados Funcionais | X |  |  |
| Transferência em Lote | X |  |  |
| Treinamento | X |  |  |

## Estes assistentes poderão ser acessados à partir do menu **Processos** nas seguintes telas.1.1. Menus

### 1.1.1. Alterar Aprovador Atual

* RH > Gestão de Pessoas > Planejamento e Captação > Requisições > Aumento de Quadro > Processos > Alterar Aprovador Atual
* RH > Gestão de Pessoas > Planejamento e Captação > Requisições > Substituição > Processos > Alterar Aprovador Atual
* RH > Gestão de Pessoas > Desenvolvimento > Requisições > Treinamento > Processos > Alterar Aprovador Atual
* RH > Gestão de Pessoas > Desenvolvimento > Requisições > Abertura de Turmas > Processos > Alterar Aprovador Atual
* RH > Gestão de Pessoas > Valorização > Requisições > Alteração de Dados Funcionais > Processos > Alterar Aprovador Atual
* RH > Gestão de Pessoas > Valorização > Requisições > Transferência > Processos > Alterar Aprovador Atual
* RH > Gestão de Pessoas > Valorização > Requisições > Transferência com Alteração de Dados Funcionais > Processos > Alterar Aprovador Atual
* RH > Gestão de Pessoas > Valorização > Requisições > Transferência em Lote > Processos > Alterar Aprovador Atual
* RH > Gestão de Pessoas > Gestão Organizacional > Requisições > Requisição Geral > Processos > Alterar Aprovador Atual
* RH > Gestão de Pessoas > Gestão Organizacional > Requisições > Requisição de Desligamento > Processos > Alterar Aprovador Atual

### 1.1.2. Alterar dados da Requisição

* RH > Gestão de Pessoas > Planejamento e Captação > Requisições > Aumento de Quadro > Processos > Alterar dados da Requisição
* RH > Gestão de Pessoas > Planejamento e Captação > Requisições > Substituição > Processos > Alterar dados da Requisição
* RH > Gestão de Pessoas > Valorização > Requisições > Transferência > Processos > Alterar dados da Requisição

## 1.2. Controles de Acesso

Serão disponibilizados os seguintes controles de segurança para **Permissão de Acesso** aos assistentes:

### 1.2.1. Aprovador Atual

* Serviços Globais > Segurança > Perfis > Acesso a Menus > Gestão de Pessoas > [01] Planejamento e Captação > [01.04] Requisições > [01.04.01] Requisições > [01.04.01.01] Aumento de Quadro > Alterar Aprovador Atual

* Serviços Globais > Segurança > Perfis > Acesso a Menus > Gestão de Pessoas > [01] Planejamento e Captação > [01.04] Requisições > [01.04.01] Requisições > [01.04.01.03] Substituição > Alterar Aprovador Atual

* Serviços Globais > Segurança > Perfis > Acesso a Menus > Gestão de Pessoas > [03] Desenvolvimento > [03.02] Requisições > [03.02.01.01] Requisição de Treinamento > Alterar Aprovador Atual

* Serviços Globais > Segurança > Perfis > Acesso a Menus > Gestão de Pessoas > [03] Desenvolvimento > [03.02] Requisições > [03.02.01.03] Requisição de Abertura de Turmas > Alterar Aprovador Atual

* Serviços Globais > Segurança > Perfis > Acesso a Menus > Gestão de Pessoas > [04] Valorização > [04.02] Requisições > [04.02.01.01] Alteração de Dados Funcionais > Alterar Aprovador Atual

* Serviços Globais > Segurança > Perfis > Acesso a Menus > Gestão de Pessoas > [04] Valorização > [04.02] Requisições > [04.02.01.03] Transferência > Alterar Aprovador Atual

* Serviços Globais > Segurança > Perfis > Acesso a Menus > Gestão de Pessoas > [04] Valorização > [04.02] Requisições > [04.02.01.05] Transferência com Alteração de Dados Funcionais > Alterar Aprovador Atual

* Serviços Globais > Segurança > Perfis > Acesso a Menus > Gestão de Pessoas > [04] Valorização > [04.02] Requisições > [04.02.01.07] Transferência em Lote > Alterar Aprovador Atual

* Serviços Globais > Segurança > Perfis > Acesso a Menus > Gestão de Pessoas > [05] Gestão Organizacional > [05.01] Requisições > [05.01.01] Requisições > [05.01.01.01] Requisição Geral > Alterar Aprovador Atual

* Serviços Globais > Segurança > Perfis > Acesso a Menus > Gestão de Pessoas > [05] Gestão Organizacional > [05.01] Requisições > [05.01.01] Requisições > [05.01.01.03] Requisição de Desligamento > Alterar Aprovador Atual

### 1.2.2. Alterar dados da Requisição

* Serviços Globais > Segurança > Perfis > Acesso a Menus > Gestão de Pessoas > [01] Planejamento e Captação > [01.04] Requisições > [01.04.01] Requisições > [01.04.01.01] Aumento de Quadro > Alterar dados da Requisição

* Serviços Globais > Segurança > Perfis > Acesso a Menus > Gestão de Pessoas > [01] Planejamento e Captação > [01.04] Requisições > [01.04.01] Requisições > [01.04.01.03] Substituição > Alterar dados da Requisição

* Serviços Globais > Segurança > Perfis > Acesso a Menus > Gestão de Pessoas > [04] Valorização > [04.02] Requisições > [04.02.01.03] Transferência > Alterar dados da Requisição

## 1.3. Pré-condição

Para executar qualquer um dos dois assistentes, **apenas 1 (uma)** requisição deverá ser selecionada na visão.

## 1.4. Assistente - Alterar Aprovador Atual

### 1.4.1. Pré-condição de execução do processo

Ao iniciar o processo, a aplicação irá validar o **Status** da requisição selecionada.

A execução do assistente somente ocorrerá se a requisição selecionada estiver no fluxo de atendimento (**CODATENDIMENTO IS NOT NULL**) e o status **Em Andamento**.

O não atendimento dessa condição ensejará a exibição de uma mensagem ao usuário e o processo não será executado.

**Mensagem de validação**: "Não é possível alterar o Aprovador Atual da requisição selecionada porque ela ainda não está no fluxo de atendimento. Para colocá-la no fluxo utilize a opção Processos > Inserir no Fluxo".

## 1.4.2. Etapas do Assistente

* **Etapa 1 (Boas vindas)**
  + **Título**: Bem-vindo ao Assistente de Alteração de Aprovador Atual da Requisição.
  + **Subtítulo**: Este processo tem a finalidade de alterar o responsável pela aprovação da requisição.
* **Etapa 2 (Alteração de Aprovador Atual)**
  + **Protótipo**

* + **Aprovador Atual**: Valor padrão é a Chapa e Nome do Aprovador Atual. (Origem de dados é a mesma da visão da requisição)

* + **Novo Aprovador**: Valor padrão em branco.
    - **Lista**: Todos os funcionários da mesma coligada e filial da requisição. (Origem de dados é a mesma da tela de funcionários "RH > Gestão de Pessoas > Acompanhamento > Funcionários")
  + **Responsável pela mudança de Aprovador**: O mesmo lookup utilizado no anexo "Parecer" das requisições, destinado a indicar o responsável pelo parecer.
  + **Motivo**: Valor padrão em branco.
  + **Validação** (Ao clicar em avançar)
    - **Validação 1**: Se o campo Novo Aprovador estiver em branco ou com o mesmo valor do campo Aprovador Atual e/ou o campo Motivo estiver em branco, o sistema não permitirá o avanço da etapa e o usuário será informado por meio da seguinte mensagem de alerta:
      * **Mensagem de Validação**: "Para avançar esta etapa é necessário informar um Novo Aprovador diferente do Aprovador Atual e preencher o motivo desta alteração!".
    - **Validação 2**: Se o Novo Aprovador informado não é um Atendente, o sistema não permitirá o avanço da etapa e o usuário será informado por meio da seguinte mensagem de alerta:
      * **Mensagem de Validação**: "O Novo Aprovador escolhido não é um atendente, então não poderá ser colocado como responsável pela aprovação da requisição. Para torna-lo um atendente, é necessário que seja executado o assistente "RH > Gestão de Pessoas > Configurações > Criar Atendente no RM Agilis".
      * **Nota técnica**: Para identificar se o Novo Aprovador é um Atendente será utilizado na classe **RM.Rhu.Facade.RhuAtendenteAgilis** o método "**public int GetCodAtendenteByChapa(int codColigada, string chapa)**". Se o retorno do método for menor ou igual a zero, o funcionário não é um atendente.
        + **codColigada**: Código da Coligada do usuário que está executando o processo.
        + **chapa**: Chapa do Novo Aprovador selecionado.
* **Etapa 3 (Execução)**
  + **O Aprovador Atual será atualizado**  
    - **Nota técnica**: Para atualização do atendente será utilizado na classe "**RM.Rhu.Facade.RhuAtendimentoAgilis**" o método "**public string RepassarAtendimento(int codColigada, string codUsuarioAtual, int codColAtendimento, int codLocal, int codAtendimento, int codColigadaNovoAtendente, string chapaNovoAtendente, string justificativa)**.
  + **Parecer**: Será criado um parecer, registrando na requisição a mudança do responsável pela aprovação.
  + **Log**
    - **Se** ocorrer um erro desconhecido durante a execução do processo

      * Mensagem de **erro**: "O Aprovador Atual da requisição não foi alterado, porque ocorreu o seguinte erro durante a execução do processo: {0}"
      * {0} = Mensagem de erro.
    - **Senão, Se** ocorrer uma validação que impeça a conclusão do processo

      * Mensagem de **atenção**: "O Aprovador Atual da requisição foi alterado, com as seguinte(s) ressalva(s): {0}".
      * {0} = Mensagem de erro.
    - **Senão**

      * Mensagem de **informação**: "O Aprovador Atual da requisição foi alterado com sucesso!".
      * {0} = Mensagem de erro.

## 1.5. Assistente - Alterar dados da Requisição

### 1.5.1. Pré-condição de execução do processo

Ao iniciar o processo, a aplicação irá validar o **Status** da requisição selecionada.

A execução do assistente somente ocorrerá se a requisição selecionada estiver com o status **Aprovado**.

O não atendimento dessa condição ensejará a exibição de uma mensagem ao usuário e o processo não será executado.

**Mensagem de validação**: "Não é permitido a mudança de Seção para requisições que não estejam aprovadas ou que já estejam concluídas".

### 1.5.2. Etapas do Assistente

* **Etapa 1 (Boas vindas)**
  + **Título**: Bem-vindo ao Assistente de Alteração de dados da Requisição.
  + **Subtítulo**: Este processo tem a finalidade de alterar dados da requisição.
* **Etapa 2 (Alteração de Seção)**
  + **Título**: Seção.
  + **Subtítulo**: Esta etapa lhe permite alterar a Seção informada na requisição. Você pode optar pode optar por manter a Seção informada, deixando o campo em branco e clicando em Avançar.
  + **Protótipo**

* **Filial e Seção**: Correspondem aos dados existentes na tela de cadastro de requisição. Os valores "default" são os mesmos que estiverem preenchidos no grupo "Seção Atual".
* **Etapa 3 (Alteração de Função e/ou Salário e/ou Tabela Salarial)**
  + **Visibilidade**: Esta etapa somente será apresentada se a requisição selecionada for de um dos seguintes tipos: Aumento de Quadro / Substituição.
  + **Título**: Função e Salário
  + **Subtítulo**: Esta etapa lhe permite alterar dos dados relativos à Função e Salário (incluindo os dados da Tabela Salarial)
  + **Protótipo**

* + O comportamento dos componentes do grupo "Proposta de Alteração" desta etapa, devem seguir àquele existente no grupo de mesmo nome na tela de edição da Requisição de Alteração de Dados Funcionais (RH > Gestão de Pessoas > Valorização > Requisições > Alteração de Dados Funcionais):
    - Listar Nível e Faixa de Tabela Salarial que esteja associada à Função informada no campo Função.
    - Listar somente Faixa do Nível de Tabela Salarial selecionado.
    - Habilitar os campos relacionados com Tabela Salarial (Nível e Faixa), somente se o sistema estiver parametrizado para utilizar Tabela Salarial (RH > Gestão de Pessoas > Configurações > Parametrizador > 07.00 Configurações > 07.00.00 Gerais > 07.00.00.01 > Validações > Remuneração > Considerar os salários das tabelas salariais).
      * Se habilitado o uso de Tabela Salarial, ao selecionar o Nível e Faixa, preencher automaticamente o campo Salário com o valor do item selecionado na tabela.
      * Se habilitado o uso de Tabela Salarial, somente permitir ao usuário modificar o valor selecionado na tabela se o sistema estiver parametrizado para permitir alteração salarial com uso de tabela (RH > Gestão de Pessoas > Configurações > Parametrizador > 07.00 Configurações > 07.00.00 Gerais > 07.00.00.01 Validações > Remuneração > Considerar os salários das tabelas salariais > Permitir alteração manual de salário).
    - Não se aplica a validação de redução salarial (RH > Gestão de Pessoas > Configurações > Parametrizador > 07.00 Configurações > 07.00.02 Requisições > 07.00.02.01 Requisições 2 > Permitir redução salarial para Requisições de Alteração de Dados Funcionais e Transferência com Alteração de Dados Funcionais).
  + **Validação** (ao clicar em Avançar)
    - Os campos do grupo "Proposta de Alteração" não podem conter os mesmos valores dos campos do grupo "Dados atuais do funcionário". Caso isso ocorra, a validação deve impedir o usuário de avançar a etapa e exibir a mensagem:
      * "A proposta de alteração de Função e/ou Salário não pode conter os mesmos valores que estão atualmente atribuídos ao funcionário!".
* **Etapa 4 (Parecer)**
  + **Título**: Parecer
  + **Subtítulo**: Nesta etapa você deve informar quem foi o responsável pela autorização de alteração dos dados da requisição
  + **Protótipo**

* **Responsável pelo ajuste nos dados da Requisição**: O mesmo lookup utilizado no anexo "Parecer" das requisições, destinado a indicar o responsável pelo parecer.
* **Motivo**: Valor padrão em branco.

* **Etapa 5 (Execução)**
  + **Será atualizada a Seção da Requisição.**
  + **Para requisições dos tipos Aumento de Quadro / Substituição, serão atualizadas as informações de Função, Salário e Tabela Salarial da Requisição**
  + **Um registro de Parecer será criado para a Requisição, com os dados do Responsável e Motivo informados**.
* **Log**
  + **Se** ocorrer um erro desconhecido durante a execução do processo

    - Mensagem de **erro**: "Os dados da Requisição não puderam ser alterados, porque ocorreu o seguinte erro durante a execução do processo: {0}"

      * {0} = Mensagem de erro.
  + **Senão, Se** ocorrer uma validação que impeça a conclusão do processo

    - Mensagem de **atenção**: "Os dados da Requisição foram alterados, com as seguinte(s) ressalva(s): {0}".

      * {0} = Mensagem de erro.
      * Exibir o detalhe de informações alteradas, para cada campo.
  + **Senão**

    - Mensagem de **informação**: "Os dados da Requisição foram alterados com sucesso!".

      * {0} = Mensagem de erro.
      * Exibir o detalhe de informações alteradas, para cada campo.

# Informações complementares

Toda regra do processo de aprovação e conclusão da requisição deverá ser mantida, incluindo aquelas relacionadas a controle de lotação, que no caso de modificação de Seção deverá surtir efeitos na nova Seção informada.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
