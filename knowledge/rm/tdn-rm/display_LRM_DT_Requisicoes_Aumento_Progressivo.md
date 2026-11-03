---
content_hash: a11bcd024d9a84fe514683bab3fab905ea3a443506967cf3c3fd5b381af724ef
fetched_at: '2026-06-29T00:06:14.319198+00:00'
page_id: '210043540'
product: rm
source: tdn-rm
title: DT_Requisicoes_Aumento_Progressivo
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Requisicoes_Aumento_Progressivo
version: 2
---

# REQUISIÇÕES AUMENTO PROGRESSIVO

## Características do Requisito

  

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Gestão de Pessoas** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Valorização/Requisições* | *Requisições de aumento progressivo* | |
| **Versões/Release:** | *12.1.6* |

## Descrição

Nessa versão está disponível a funcionalidade Aumento Progressivo para as requisições **Alteração de dados Funcionais** e **Transferência com Alteração de Dados Funcionais**

## Procedimento para Utilização

**Parametrização de Tipos de Requisição (“Alteração de dados funcionais” e “Transferência com alteração de dados funcionais”)**  
A parametrização das requisições **“Alteração de dados funcionais”** e **“Transferência com Alteração de dados Funcionais”** consiste em definir as regras que serão validadas ao incluir um Aumento progressivo.  
Em **RH | Gestão de Pessoas | Configurações | Tipos de Requisição,** selecione uma das requisições e acesse **Anexo | Parametrização.**

Ao abrir a tela, inclua uma parametrização para o tipo de requisição selecionado e preencha os campos necessários.

O campo **“Permitir Progressão”** quando marcado possibilita o usuário incluir progressões e também interfere no momento de incluir uma requisição, pois caso o solicitante informe o percentual máximo acima do valor que foi parametrizado, o sistema ira exibir uma mensagem de alerta perguntando ao solicitante se ele deseja que o sistema crie progressões obedecendo a parametrização.

**“Percentual máximo de aumento sobre o salário”**, **“Tempo mínimo de casa”**, **“Prazo mínimo entre aumentos”** e **“Fórmula Customizada”**, são campos que precisam ter os seus valores definidos e poderão ter um dos quatro comportamentos (Ações sobre a regra) abaixo:

* **Não Validar:** a regra não será validada.

* **Validar com mensagem de alerta:** a regra será validada seguida de uma mensagem de alerta.

* **Validar com bloqueio:** a regra será validada mas boqueia o solicitante de continuar com o processo.

**Exemplo:** O campo **“percentual máximo de aumento sobre o salário”** foi parametrizado para 50% e sua ação sobre a regra é **“Validar com mensagem de alerta”**, se no momento de incluir a progressão o solicitante informar um percentual superior ao valor definido na parametrização, o sistema irá exibir a seguinte mensagem de alerta:

Já os campos abaixo iram agir da seguinte forma:

* **Registro “padrão” para todas as filiais?**

Quando marcado será gerado um registro com as regras parametrizadas para todas as filiais.

* **Registro “padrão” para todos os motivos?**

Quando marcado será gerado um registro com as regras parametrizadas para todos os motivos da coligada.  
Quando desmarcados, o ícone de inclusão ficará visível para que informe as filiais e os motivos de sua preferência.

**Obs.** A parametrização definida valerá apenas para as filiais que foram incluídas, portanto, não será possível incluir um registro com as mesmas parametrizações. Caso queira uma parametrização diferente para outras coligadas, será necessário incluir um novo registro, essa informação vale tanto para as filiais quanto para os motivos.

**Alteração nas visões das requisições dos tipos: (“Alteração de dados funcionais” e “Transferência com alteração de dados funcionais”)**  
Em **RH | Gestão de Pessoas | Valorização | Requisições | Alteração de dados Funcionais** foram feitas alterações na visão das requisições dos tipos **“Alteração de dados funcionais”** e **“Transferência com alteração de dados funcionais”**, com o objetivo de deixar o usuário livre para a configuração da tela de visão e destacar os campos que não estão dentro da regra desejada. A visão das requisições contém os seguintes campos:

• Filial

• Tempo de casa

• Função de Origem

• Tempo na função atual

• Faixa salarial de Origem Salário atual  

• Função proposta,                              

 • Faixa salarial proposta

• Salário proposto Percentual de reajuste

• Data da última alteração salarial

• Motivo desta alteração

• Previsão

**Alterações Winforms / Webforms para registro de Alteração de Dados Funcionais Progressivo e Transferência de Dados Funcionais Progressivo.**

As funcionalidades **“Alteração de dados funcionais progressivo”** e a **“Transferência com alteração de dados funcionais progressivo”** foram criadas para possibilitar a inclusão/alteração de progressões, respeitando as parametrizações feitas em tipos de requisições. Iremos utilizar como exemplo o anexo **“Transferência com Alteração de Dados Funcionais Progressivo”**Acesse **Efetivações | Efetivar Transferência com Alteração de Dados Funcionais | Anexos | Transferência com Alteração de Dados Funcionais Progressivo.**

Através do caminho acima será possível a inclusão das progressões, e essas só serão validadas após salvar a requisição de acordo com a parametrização definida em “Tipos de requisição”, caso não tenha nenhuma parametrização a progressão não passará pelas validações.

Obs.: A inclusão de uma progressão é possível quando a requisição tiver o seu status como **“Pendente”** ou **“Em andamento”** e o parâmetro **“Permitir Progressão”** de **“Tipo de Requisição”** estiver marcado.

Inclua uma progressão, preencha os campos necessários e salve.

As requisições que tiverem progressões não poderão ter os dados alterados, os campos serão somente leitura. A alteração só será possível no anexo **“Alteração de Dados Funcionais Progressivo”** ou excluindo as progressões**.**

**WEBFORMS**

Assim como no WinForms as alterações e criações de telas e funcionalidades serão implementadas na Web(Portal), somente para as requisições do tipo **“Alteração de dados funcionais”** e **“Transferência com Alteração de dados Funcionais”.**

Acesse **Recursos Humanos | Requisições | Transferência com Alteração de Dados Funcionais**

Também é possível incluir no portal o aumento progressivo para a requisição. Para isso acesse **Recursos Humanos | Requisições | Alteração de dados Funcionais** einclua uma nova requisição clicando em **“Nova”.**

Após preencher e incluir os campos necessário da requisição será habilitado o botão **“Aumento Progressivo”.**

A aba **“Aumento Progressivo”** terá uma visão dos dados e também as funcionalidades comuns do sistema como inclusão e exclusão da progressão.

Não será possível informar para determinado funcionário um salário inferior que o da progressão anterior, da mesma maneira a função também não poderá ser igual a de uma progressão anterior.

Além disso, as progressões do portal serão validadas de acordo com a parametrização feita no sistema, portanto, o salário do funcionário pode ser informado a partir do nível, faixa ou diretamente no campo ao salário e percentual.

Acesse **“Aumento Progressivo”** inclua uma progressão e clique em **“Tabela”.** Será exibida a tela com as faixas e níveis existentes, escolha a de sua preferência. Após informar o Nível e a Faixa, os campos **“Salário”** e **“Percentual”** serão preenchidos automaticamente.

A outra maneira de informar o salário é preencher diretamente o campo **“Salário”** ou **“Percentual”,** mas os campos **“Nível”** e **“Faixa”** não serão preenchidos automaticamente.

A requisição que for do tipo **“Alteração de dados funcionais”** ou **“Transferência de Alteração de dados funcionais”** e tiver progressões com o status **“Pendente”** ou **“Em andamento”,** não poderá ser concluída. Não é possível efetivar as progressões dos tipos **“Alteração de dados Funcionais”** quanto **“Transferência com alteração de dados funcionais”,** essa opção está disponível somente no Winforms.

**Efetivação das “Progressões” de requisições dos tipos: (“Alteração de dados funcionais” e “Transferência com alteração de dados funcionais****”)** 

A efetivação das progressões permite efetivar todas as progressões existentes nas requisições **“Alteração de dados funcionais”** e **“Transferência com Alteração de dados funcionais”.**Para efetivar as progressões acesse **Efetivações | Efetivar Alteração de Dados Funcionais / Efetivar Transferência com Alteração de Dados Funcionais.**

Para ter acesso a tela de progressões de determinada requisição vá em **Anexo | Alteração de Dados Funcionais Progressivo.**

A efetivação das progressões deverá ser realizada seguindo a ordem de “data mínima de efetivação”. Não será possível efetivar uma progressão se existir uma outra progressão pendente com a “data mínima de efetivação” menor que à da progressão a ser efetivada.

Caso o usuário tente efetivar uma progressão com a “data mínima de efetivação” maior que as progressões existentes na requisição, o sistema exibira o seguinte erro:

Marque a progressão com a menor “data mínima de efetivação” e acesse **Processos | Efetivar progressão de Alteração de Dados Funcionais.**

Após executar o processo o sistema exibira a tela de “Efetivação da Progressão” para que seja informado (se necessário) a data para efetivação.

O status da requisição foi alterado para **“Efetivado”.**

Depois de efetivar a progressão o sistema irá enviar um e-mail para todos os envolvidos informando que houve alterações na progressão.

Para concluir a requisição é preciso que a mesma não tenha progressões, se tiver efetive-as e automaticamente a requisição será concluída, em seguida será enviado um e-mail para os envolvidos.

Caso a requisição não tiver progressões a efetivação é possível a través do processo “**Concluir Requisição”.**Acesse **Efetivação | Efetivação de Alteração de dados funcionais / Efetivação de Transferência com alteração de dados funcionais | Processos | Concluir Requisição**

Em seguida a requisição terá seu status alterado para **“Concluída”**.
