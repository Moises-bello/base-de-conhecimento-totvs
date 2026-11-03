---
content_hash: 7c08c44b518464eed4605896046416c220934f8ca9224e92a24d653e5e61e86c
fetched_at: '2026-06-29T00:11:12.486741+00:00'
page_id: '653572529'
product: rm
source: tdn-rm
title: Ativação da Hierarquia Por Posição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=653572529
version: 19
---

**Disponível a partir da versão 12.1.34**

**Ao ativar a Hierarquia por Posição o cadastro de chefes e supervisores não será mais utilizado no ERP RM para os seguintes cadastros/processos:**

**Importante: Os cadastros se encontram atualizados também no app MeuRH.**

* Requisições (Caso o parâmetro Hierarquia Requisições estiver ativado)
* Aprovações de Ponto
* Aprovar Batidas
* Aprovar Batidas em Grupo
* Aprovar Abonos
* Saldo do Banco de Horas
* Grupo de descanso
* Gestão por Escala
* Batidas Aprovadas
* Gestão de Férias
* Avisos Calculados
* Definição de substitutos
* Listagem dos Subordinados
* Avaliações de Desempenho
* Visualização de subordinados

**Parametrização necessária para utilização:**

Acessar o parametrizador do Gestão de Pessoas (Configurações > Parametrizador > Gerenciamento de Hierarquia).

Se o campo **Habilita funcionalidades de****Hierarquia** **não estiver** marcado, significa que as funcionalidades da gestão de **Hierarquia por Posição** não ficarão visíveis no Totvs Gestão de Pessoas.

**Observação**: Após ativar a Hierarquia por Posição, caso o menu não esteja disponível, será necessário liberar o acesso ao Menu através das Permissões de acesso do TOTVS Gestão de Pessoas.

Se este campo **estiver** marcado, as funcionalidades da gestão de Hierarquia por Posição ficarão visíveis no Totvs Gestão de Pessoas e o ERP passará a utilizar a Gestão por Hierarquia não utilizando o cadastro de Chefes e Supervisores.

**Importante**

* Mesmo com este campo marcado o usuário deve ter permissão de acesso às funcionalidades da gestão de Hierarquia por Posição.

false🚀 Novidade: Sequencial Global de ID de Posição (Hierarquia)

A partir da **Versão 12.1.2510**, o sistema passa a oferecer a opção **"Utiliza Sequencial Global"** no parametrizador, dentro da configuração de *Hierarquia.*

### 💡 O que muda?

Ao **marcar** este novo parâmetro, todas as coligadas que utilizam a Hierarquia por Posição passarão a compartilhar um **ID de Posição único (sequencial global)**.

Isso garante que o próximo ID de Posição criado será sempre o maior ID já registrado no **contexto de todas as coligadas**.

### 📋 Exemplo Prático

Considere o cenário antes da criação de uma nova posição:

| **Coligada** | **Maior ID de Posição Criada** |
| --- | --- |
| **01** | 59 |
| **06** | 35 |
| **07** | 115 |

**Resultado com o parâmetro "Utiliza Sequencial Global" MARCADO:**

* Ao criar uma nova Posição em **qualquer uma das coligadas** (01, 06 ou 07), essa nova Posição receberá o **ID 116** (que é o maior ID global + 1).

Ao utilizar a **Hierarquia e Posição**, para a visualização de funcionários subordinados de outra coligada (em caso de funcionários que são chefes em outras coligadas que não sejam sua lotação atual) através da Gestão do Time (MeuRH) ou Subordinados (Portal RM) o parâmetro abaixo deverá ser marcado através do parametrizador do RM LABORE.

**Parâmetros referentes à Funcionário**

Através desta área o usuário irá configurar como será a atualização das informações da posição que são exibidas no cadastro de funcionário.

As opções disponíveis são:

**Permite informar dados somente na Posição**

Se esta opção estiver marcada significa que os campos abaixo ficarão habilitados no cadastro de Posição e ficarão desabilitados no cadastro de Funcionário:

* Seção
* Função
* Nível salarial
* Faixa salarial
* Sindicato
* Salário mensal
* Carga horária mensal
* Horário
* Letra

Ao salvar as informações acima no cadastro de posição as mesmas serão replicadas no cadastro do funcionário alocado na posição.

**Permite informar dados somente no Cadastro de Funcionário**

Se esta opção estiver marcada significa que os campos abaixo ficarão desabilitados no cadastro de Posição e poderão ser manipuladas no cadastro do funcionário.

* Seção
* Função
* Nível salarial
* Faixa salarial
* Sindicato
* Salário mensal
* Carga horária mensal
* Horário
* Letra

Com esta opção habilitada, ao manipular os campos a cima no cadastro do funcionário, as mesmas informações serão replicadas para o cadastro da posição do funcionário em questão.

**Permite informar dados no Cadastro de Funcionário e na Posição**

Se esta opção estiver marcada significa que os campos abaixo ficarão habilitados para manipulação no cadastro de Posição e no cadastro de Funcionário:

* Seção
* Função
* Nível salarial
* Faixa salarial
* Sindicato
* Salário mensal
* Carga horária mensal
* Horário
* Letra

Ao salvar as informações acima no cadastro de funcionário as mesmas serão atualizadas no cadastro da posição que o funcionário está alocado.

Ao salvar as informações acima no cadastro da posição as mesmas serão atualizadas no cadastro do funcionário alocado na posição.

**Calendário utilizado no cálculo do ponto**

Através desta área o usuário irá configurar se no cálculo do ponto o calendário será o informado no cadastro de Seção ou no cadastro da Hierarquia.

**Calendário da seção**

Se esta opção estiver marcada significa que o cálculo do ponto irá utilizar o calendário de feriados configurado na seção do funcionário. Esse é o cálculo padrão do Totvs Automação de Ponto.

**Calendário da hierarquia**

Se esta opção estiver marcada significa que o cálculo do ponto irá utilizar o calendário de feriados configurado na hierarquia de lotação definida na posição do funcionário.

**Habilita uso da hierarquia nas requisições**

Este campo ficará habilitado quando o campo “Habilita funcionalidades de Hierarquia” estiver marcado e o sistema não possuir requisições “Em Andamento” ou “Suspensas”.

Essa regra irá garantir que a virada da requisição para hierarquia acontecerá quando não existir requisições para serem concluídas.

Da mesma forma que o sistema só permitirá que este campo seja desmarcado se não existir requisições “Em Andamento” ou “Suspensas” usando a estrutura hierárquica.

Marcando o parâmetro **Habilitada uso da Hierarquia nas Requisições**deverá ser definido se o repasse das requisições respeitará o fluxo definido pelo Agilis (Integração com o Agilis) ou o definido de acordo com a hierarquia (dentro dos tipos de requisição).

**IMPORTANTE !**

Após ativação da Hierarquia por Posição, caso o menu não seja habilitado, basta liberar acesso aos menus através dos Perfis de Acesso.

Maiores informações sobre o fluxo de repasse das requisições estão disponíveis na página .

**Links Importantes e Complementares:**
