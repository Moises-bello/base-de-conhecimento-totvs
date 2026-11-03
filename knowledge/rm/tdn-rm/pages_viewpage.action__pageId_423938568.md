---
content_hash: 17f63f33683f038082ad2d504e31c9049c0f6a91678891be234059497d70612c
fetched_at: '2026-06-29T00:09:27.914512+00:00'
page_id: '423938568'
product: rm
source: tdn-rm
title: Versão 11.40.0 (TOTVS Manutenção)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938568
version: 3
---

**Migração do processo de apropriação Direta de Produtos** O processo de apropriação direta de produtos foi migrado para a plataforma .NET. Este processo consiste em mensurar, movimentar o estoque e apurar o custo dos materiais/produtos utilizados pelos objetos de manutenção no dia a dia de um setor de manutenção. Nesta versão o processo de apropriação direta foi transformado em um processo e o mesmo é acessado através do menu Operações | Apropriação direta de produtos, clicando no processo "Assistente de apropriação direta de produtos".

**Apropriação Direta Sem Indicador de Uso** Na apropriação direta de produto será possível realizar apropriações para objetos que não fazem controle de indicadores de uso.  
    
**Gerar movimento para indicadores de uso.** Foi criado o processo de geração de movimento para indicadores de uso dos objetos de manutenção que estão alocados em um projeto cadastrado no TOTVS Gestão de Projetos. Através dessa funcionalidade é possível cobrar a locação de acordo com os indicadores de uso lançados para o objeto durante o período em que o mesmo esteve alocado.  
    
**Mostrar Último Indicador de Uso** Na apropriação direta de produto será mostrado o último indicador de uso do objeto de manutenção pai e do objeto filho.

**Outras atualizações:**

* Atualização no cadastro de mão de obra. Ao cadastrar uma mão de obra será listadas todas as pessoas que estão  vinculadas a funcionários ativos;
* É possível parametrizar no tipo de movimento de requisição de material o tipo de frete CIF ou FOB que será usado no momento da geração do movimento;
* Na geração de ordem de serviço via agendamento o preenchimento do campo "Funcionário Responsável" irá buscar o funcionário default na respectiva ordem: objeto de manutenção ou tipo de movimento ou usuário logado no sistema;
* Os campos de "Tabelas Opcionais" poderão ser parametrizados no tipo de movimento para que apareçam como obrigatórios no movimento e no item da ordem de serviço;
* Realizada melhoria na geração de Ordem de Serviço de Plano de Manutenção pelo Cronograma de Manutenções. Ao editar uma Ordem de Serviço será permitido alterar a data de geração do plano de manutenção na pasta Plano Realizados;
* Realizada melhoria no cadastro de solução do atendimento. Ao inserir uma solução no atendimento será gravado o nome do funcionário associado ao usuário logado no sistema;
* Será possível expandir produtos compostos.

**Novidades Backoffice**Possibilidade de utilizar desconto para o item da OS e para a OS.Nessa versão foi implementado a possibilidade de se trabalhar com desconto para o item da OS e para a OS.  Ao abrir uma OS o usuário informa o percentual ou o valor do desconto que será concedido na OS e o sistema realiza o calculo do valor bruto em cima do desconto dado.

**Meio de pagamento na ordem de serviço.** Nesta nova versão será possível trabalhar com meio de pagamento na ordem de serviço. Sendo assim o usuário poderá informar na Ordem de Serviço de qual forma será o pagamento. Ex: Dinheiro, cheque avista, ou cheque para 30,60 e 90 dias etc.

**Utilização do valor da mão-de-obra alocada na OS com base em seu custo/hora.** Nesta versão será possível calcular o valor do item da ordem de serviço com base no custo/hora da mão de obra alocada na OS. Através de um parâmetro o usuário terá a possibilidade de cadastrar  ou importar de uma planilha o custo de uma determinada mão de obra. Assim, ao alocar essa mão de obra em um determinado serviço existirá um processo que recalculará a OS com base no custo cadastrado para a mão de obra.

**Ordem de Serviço** Como novidade futura o Cadastro da Ordem de Serviço será migrado para a plataforma .NET. A nova interface de cadastro da Ordem de serviço será a mesma interface do movimento .NET do TOTVS Gestão de Estoque, Compras e Faturamento, com isso o usuário do RM Officina terá a possibilidade de utilizar as mesmas funcionalidades e recursos já disponibilizados pelo TOTVS Gestão de Estoque, Compras e Faturamento, através do movimento .NET. Ao incluir ou editar uma Ordem de Serviço, será aberta a tela do movimento .NET e dentro dessa tela haverá uma aba de nome "Ordem de Serviço" onde conterá os dados da Ordem de Serviço aberta. Os Itens da Ordem não serão cadastrados de dentro da tela de ordem de serviço como era feita até a versão 10.80.0 do RM Officina. Na versão 11.20.0, para cadastrar um item, o usuário devera acessar a aba "Itens" que também se encontra na tela do movimento .NET.

**Cópia da Ordem de Serviço** Na versão 11.20.0 será implementado a funcionalidade de cópia de Ordem de Serviço. Com isso o usuário poderá fazer a cópia de uma Ordem de Serviço já existente inclusive copiando para a nova OS os itens contidos na OS de origem. Fórmulas de Consistência Com a migração da ordem de serviço para a plataforma .NET, agora é possível utilizar formulas de consistência para consistir a geração do movimento. As fórmulas podem ser usadas tanto para a consistência da geração da ordem quanto para o item da ordem.

**Vincular e desvincular indicador de uso na Ordem de Serviço** Na versão 11.0.0 foi implementado a funcionalidade de vincular e desvincular um indicador de uso à Ordem de Serviço. Essa funcionalidade esta disponível na aba indicador de uso da edição da ordem de serviço e permite que o usuário selecione o indicador de uso que quer vincular ou desvincular a ordem de serviço.

**T****ela de acessórios da ordem de serviço foi migrada para a plataforma .NET** Nesta versão a tela de acessórios da Ordem de Serviço foi migrada para a plataforma.NET..

**Alterar OS cancelada e Preço de tabela** Na versão 11.20.0 não será mais possível editar uma OS que se encontra com Status "Cancelado" e também aumentar ou diminuir o preço do item da ordem de serviço. Os parâmetros "Permite Alterar OS Cancelada" e "Preço de Tabela" foram retirados do sistema para os clientes que utilizarem o novo modelo de Backoffice.

**Produto substituto/Similar** Na versão 11.20.0 os clientes que migrarem para o novo modelo terão acesso à funcionalidade de alterar o produto da OS por um produto substituto ou similar. Haverá um botão na interface de Ordem de Serviço onde o usuário fará a troca dos produtos no momento de incluir, editar ou faturar uma Ordem de Serviço.

**Acessórios da Ordem de Serviço** Na versão 11.20.0 a tela de acessórios da ordem de serviço acessada de dentro da visão e da edição da ordem será migrada para a plataforma. NET.

**Vincular e desvincular indicador de uso na Ordem de Serviço** Na versão 11.20.0 foi implementado a funcionalidade de vincular e desvincular um indicador de uso à Ordem de Serviço. Essa funcionalidade esta disponível na aba indicador de uso da edição da ordem de serviço e permite que o usuário selecione o indicador de uso que quer vincular ou desvincular a ordem de serviço.

**Cadastro de Problemas da Ordem de serviço migrado para plataforma .NET.** Na versão 11.0.0 o cadastro de Problemas da Ordem de Serviço foi migrado para a plataforma.NET.
