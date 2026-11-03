---
content_hash: 61fc2727b975279e50c318d43c034ede1088ca2e95e840dd78f38b1cc514848d
fetched_at: '2026-06-29T00:05:47.709814+00:00'
page_id: '1015124104'
product: rm
source: tdn-rm
title: Facilitador RM
type: documentation
url: https://tdn.totvs.com/display/LRM/Facilitador+RM
version: 79
---

## O que é?

O Facilitador RM é uma ferramenta desenvolvida para nos auxiliar na criação de atividades  de automações de testes vocacionados. Baseado na comunicação com estruturas nativas das soluções do TOTVS linha RM, essa ferramenta permite que durante o processo de geração dos testes, você crie atividades de automações para processos ou manipulação de registros, de forma simples e através de uma interface guiada (Wizard), sem precisar lidar com códigos complexos, ferramentas de terceiros ou configurações técnicas avançadas.

## Para que serve?

O Facilitador RM tem como objetivos:

* **Criação de Atividades de Testes que permitem Incluir/Editar ou Excluir registros dos principais cadastros da linha RM**, simplificando a validação de toda a estrutura de dados do sistema.
* **Criação de Atividades de Testes que Executam Processos** a partir de uma execução realizada previamente.

## Links Úteis

1. Documentação da Atividade Soap:
2. Documentação de Serviços para preparação do ambiente de testes de WebServices:

Este recurso possui restrição de versão e está disponível para ser executado exclusivamente em ambientes que utilizam o RM **na versão 12.1.2506 ou superior**.

## Como Utilizar

Como cadastrar

## Facilitadores RM

Cadastros Incluir/Editar 

Este módulo é focado na manipulação de registros do TOTVS RM por meio dos seus DataServers.

> O **DataServer** é um componente-chave da arquitetura do RM, responsável por acessar e manipular dados diretamente nos objetos de negócio do sistema. Ele funciona como um serviço que expõe operações de **consulta, inclusão, alteração e exclusão** de dados dos módulos e telas do RM.

Navegação para o Cadastro

1. No menu lateral, acesse: **Facilitadores** → **Incluir/Editar**
2. Clique no card **Incluir/Editar**.

1. Automação de Testes

Configure a infraestrutura de referência:

* **Ambientes:** Selecione o ambiente RM para buscar os dados de configuração.

* **Servidor (Obrigatório):** Escolha o servidor para a leitura técnica do sistema.

2. RM (Conexão)

Estabeleça a comunicação com o **Host do RM**:

Informe o endereço do **Host**.  (Ex: `http://localhost:8051`).

* A porta padrão é a **8051**. No entanto, essa configuração pode variar de acordo com o ambiente ou alguma necessidade específica.  
  Caso seja necessário, o usuário possui **liberdade para alterar a URL (Endereço e porta)**.

Usuário e Senha**:** Insira suas credenciais de acesso ao RM.

* Utilize o botão **TESTAR CONEXÃO** para validar os dados antes de prosseguir.

3. Contexto RM

Informe o contexto a ser utilizado para o DataServer.

Selecione o contexto adequado (como CodColigada, CodSistema, entre outros) no qual a automação será aplicada. Isso garante que os dados buscados pertençam à unidade de negócio correta.

> Dentro do ecossistema TOTVS RM, o **Contexto** funciona como o "endereço" da sua operação. Ele avisa ao sistema em qual **Coligada (Empresa)** e em qual **Sistema (Módulo)** a ação deve acontecer.

Alguns DataServers do RM exigem um contexto específico para sua carga ou operação (Ex: CodColigada = 1).

4. DataServer RM

Nesta etapa, definimos **qual cadastro** será manipulado.

1. O campo **Módulo** agrupa as funcionalidades por área de negócio. Ao selecionar um item da lista, o sistema carrega os objetos de integração específicos daquele produto.

3. Clique em **Selecionar** para buscar o DataServer desejado (Ex:EstConsultaSaldoData).

4**.** Filtros de Pesquisa**:** Utilize o botão **+ ADICIONAR FILTRO** para buscar registros específicos no RM.

5. Clique em **BUSCAR REGISTROS** para visualizar os **50 últimos registros cadastrados no RM**.  
    Após a exibição dos dados, será permitido **selecionar apenas um registro** para prosseguir para a **próxima etapa da tela**

1. Caso não saiba o nome técnico, identifique o DataServer diretamente no cadastro do RM pressionando a combinação de teclas **CTRL + ALT + F9** diretamente na tela de edição do sistema.
2. Crie bons filtros para identificar com precisão o seu registro base para a criação da sua atividade de testes SOAP.
5. Revisão do XML

Nesta etapa, o sistema **gera automaticamente o XML** que será utilizado na criação da sua atividade SOAP de automação.

Você pode alterar o XML conforme a sua necessidade, mas mantenha os seguintes cuidados:

* **Estrutura das Tags:** Não remova ou altere o formato das tags para não invalidar a comunicação com o RM.
* **Para Inclusão/edição:** Altere o XML conforme a sua necessidade, sempre mantendo o cuidado quanto a estrutura do mesmo.

Novas chaves primárias significam a criação de um teste de **Inclusão** (novo registro). Manter as chaves originais e alterar apenas os outros campos significa a **Edição** de um registro existente.

Se clicar em **ANTERIOR**, qualquer edição manual feita no XML será perdida., caso clique em **CANCELAR,** não acontecerá nada.6. Criação de Atividade

Nesta etapa, você irá configurar as informações finais necessárias para que a atividade seja criada dentro do sistema. Essas informações definem como a automação será identificada, descrita e executada quando for utilizada em um fluxo. Dependendo do tipo de atividade que você estiver criando, esses dados serão utilizados pelo sistema para estruturar e realizar corretamente a execução durante os testes ou processos automatizados.

Grupo

Seleciona o grupo ao qual a atividade pertencerá.

O [grupo](https://tdn.totvs.com/pages/viewpage.action?pageId=680234913#Cria%C3%A7%C3%A3odeumgrupo-1729228565) organiza e controla quem pode visualizar ou utilizar essa atividade.

Versão

Define a versão da atividade que está sendo criada.

* Isso é útil para controle de alterações e evolução de processos.

A versão da atividade é utilizada apenas para fins de organização, controle e evolução das automações no TAT. Ela não possui relação nem impacto técnico com a versão do RM em uso.

*Exemplo utilizando a versão do RM*

*Exemplo utilizando a versão padrão*

Nome da atividade

É o nome que identificará a automação dentro da plataforma.

* Escolha um nome que represente bem o que a atividade faz, facilitando a identificação por você e pela sua equipe.

Descrição da atividade

Campo destinado a explicar, de forma resumida, o propósito da automação.

* Uma boa descrição ajuda a documentar o processo e facilita a manutenção futura.

Timeout (segundos)

Tempo máximo que a execução pode levar antes de ser interrompida automaticamente.

* O valor padrão é 30 segundos, mas você pode aumentar caso o processo do RM costume demorar mais.

Testar execução 

## Testar Execução

O botão **Testar Execução** permite validar a requisição SOAP antes de finalizar a criação da atividade. Durante o teste, o sistema envia a requisição utilizando os dados informados no XML e retorna o resultado da operação, permitindo verificar se:

* Os parâmetros foram preenchidos corretamente
* A estrutura do XML está válida
* A operação SOAP está respondendo conforme esperado

Esta funcionalidade é recomendada para garantir que a atividade será criada com uma requisição funcional e que não ocorrerão falhas durante sua execução no fluxo automatizado.

**Importante:** O tempo de espera da execução reflete o tempo real de processamento do RM. Processos longos podem levar mais tempo para concluir, o que é um comportamento esperado.

Finalização e Ações Pós-CriaçãoCertifique-se de ter realizado o **Testar Execução** antes de chegar a esta tela para garantir que a atividade salva esteja 100% funcional.

Após preencher todos os campos obrigatórios e clicar em **FINALIZAR**, o sistema processará a criação da sua atividade SOAP de Registro RM. Uma mensagem de confirmação será exibida com três opções de direcionamento, permitindo que você escolha o próximo passo no seu fluxo de trabalho.

### Opções de Direcionamento

Ao visualizar a mensagem **"Atividade SOAP Criada com Sucesso!"**, você terá as seguintes alternativas:

* **FECHAR**: Esta opção encerra completamente o assistente (wizard) de configuração. Ao clicar em Fechar, você será redirecionado para a **página inicial do sistema**, finalizando o processo de criação atual sem abrir a atividade.
* **CRIAR NOVA ATIVIDADE**: Ideal para quando há necessidade de cadastrar múltiplos registros ou processos em sequência. Ao selecionar esta opção, o sistema limpa os dados atuais e **reinicia o fluxo do zero**, voltando para o estágio inicial do wizard de Registro RM.
* **ABRIR ATIVIDADE**: Esta opção redireciona você **diretamente para a tela da atividade recém-criada**. É o caminho recomendado caso precise realizar ajustes finos, conferir o XML gerado ou incluir a atividade imediatamente em um cenário de teste.

Cadastros Excluir

Este módulo é focado na remoção de registros do TOTVS RM por meio dos seus DataServers, utilizando a operação de exclusão (Delete) da arquitetura SOAP.

> O DataServer é o motor que garante a integridade dos dados. Ao solicitar uma exclusão, ele valida automaticamente se o registro possui dependências (constraints) em outros módulos, impedindo a remoção de dados que comprometeriam a consistência do sistema.

Nem todos os DataServers da Linha RM estão preparados para a exclusão de dados (diretamente via o próprio DataServer), devido a suas regras de negócio ou por possuir um processo próprio de exclusão de dados. Como em todo o nosso processo de automação, recomendamos que certifique o seu real funcionamento diretamente no RM antes de implementar sua atividade de testes automatizado SOAP aqui no TAT.

Navegação para Excluir Cadastros

 1. Navegue no menu do TOTVS Automação de Testes e clique em: **Facilitadores RM** → **Excluir Cadastros.**

1. Automação de Testes

## Automação de Testes

É a primeira fase do **Assistente de Configuração da Automação de Testes**, responsável por:

* Garantir que todas as etapas seguintes sejam carregadas com base na infraestrutura selecionada

Configure a infraestrutura de referência:

* **Ambientes:** Selecione o ambiente RM para buscar os dados de configuração.

* **Servidor (Obrigatório):** Escolha o servidor para a leitura técnica do sistema.

2. RM (Conexão)

Estabeleça a comunicação com o serviço **RM.Host**:

Informe o endereço (Ex: `http://localhost:8051`).

* Por padrão, a porta mais utilizada é a **8051**. No entanto, essa configuração pode variar de acordo com o ambiente ou alguma necessidade específica.  
  Caso seja necessário, o usuário possui **liberdade para alterar a porta**, desde que o endereço informado seja válido e acessível.

Usuário e Senha**:** Insira suas credenciais de acesso ao RM.

* Utilize o botão **TESTAR CONEXÃO** para validar os dados antes de prosseguir.

3. Contexto RM

Informe o contexto a ser utilizado para o DataServer.

Selecione o contexto adequado (como CodColigada, CodSistema, entre outros) no qual a automação será aplicada. Isso garante que os dados buscados pertençam à unidade de negócio correta.

> Dentro do ecossistema TOTVS RM, o **Contexto** funciona como o "endereço" da sua operação. Ele avisa ao sistema em qual **Coligada (Empresa)** e em qual **Sistema (Módulo)** a ação deve acontecer.

Alguns DataServers do RM exigem um contexto específico para sua carga ou operação (Ex: CodColigada = 1).

4. DataServer RM

Nesta etapa, definimos **qual cadastro** será manipulado.

1. O campo **Módulo** agrupa as funcionalidades por área de negócio. Ao selecionar um item da lista, o sistema carrega os objetos de integração específicos daquele produto.

3. Clique em **Selecionar** para buscar o DataServer desejado (Ex:EstConsultaSaldoData).

4**.** Filtros de Pesquisa**:** Utilize o botão **+ ADICIONAR FILTRO** para buscar registros específicos no RM.

5. Clique em **BUSCAR REGISTROS** para visualizar os **50 últimos registros cadastrados no RM**.  
    Após a exibição dos dados, será permitido **selecionar apenas um registro** para prosseguir para a **próxima etapa da tela**

1. Caso não saiba o nome técnico, identifique o DataServer diretamente no cadastro do RM pressionando a combinação de teclas **CTRL + ALT + F9** diretamente na tela de edição do sistema.
2. Crie bons filtros para identificar com precisão o seu registro base para a criação da sua atividade de testes SOAP.
5. Revisão do XML

Este é o XML completo da requisição SOAP. Para operações de **exclusão**, o envelope é gerado automaticamente pelo sistema e **não requer edição**, sendo disponibilizado **apenas para leitura**.

Nesta etapa, o sistema gera automaticamente o XML que será utilizado na criação da atividade SOAP de automação de testes.

* **Para** **Exclusão:** O XML virá preenchido **somente com as chaves primárias** (PKs) que serão utilizadas para identificar e remover o registro de forma única.

1. O registro selecionado na etapa anterior será a base exclusiva para a criação da atividade de **Exclusão**.
2. Em todos os XMLs gerados, foi removido o envelopamento (Envelope SOAP), que será acrescido automaticamente na criação da atividade de automação.

Se você clicar em **ANTERIOR**, aparecerá uma mensagem de confirmação:

**Deseja realmente voltar? As alterações serão perdidas.**

Isso significa:

* Se você editou o XML manualmente e tentar voltar, o sistema **descarta** qualquer modificação feita na tela.
6. Criação de Atividade

Nesta etapa, você irá configurar as informações finais necessárias para que a atividade seja criada dentro do sistema. Essas informações definem como a automação será identificada, descrita e executada quando for utilizada em um fluxo. Dependendo do tipo de atividade que você estiver criando, esses dados serão utilizados pelo sistema para estruturar e realizar corretamente a execução durante os testes ou processos automatizados.

Grupo

Seleciona o grupo ao qual a atividade pertencerá.

O [grupo](https://tdn.totvs.com/pages/viewpage.action?pageId=680234913#Cria%C3%A7%C3%A3odeumgrupo-1729228565) organiza e controla quem pode visualizar ou utilizar essa atividade.

Versão

Define a versão da atividade que está sendo criada.

* Isso é útil para controle de alterações e evolução de processos.

A versão da atividade é utilizada apenas para fins de organização, controle e evolução das automações no TAT. Ela não possui relação nem impacto técnico com a versão do RM em uso.

*Exemplo utilizando a versão do RM*

*Exemplo utilizando a versão padrão*

Nome da atividade

É o nome que identificará a automação dentro da plataforma.

* Escolha um nome que represente bem o que a atividade faz, facilitando a identificação por você e pela sua equipe.

Descrição da atividade

Campo destinado a explicar, de forma resumida, o propósito da automação.

* Uma boa descrição ajuda a documentar o processo e facilita a manutenção futura.

Timeout (segundos)

Tempo máximo que a execução pode levar antes de ser interrompida automaticamente.

* O valor padrão é 30 segundos, mas você pode aumentar caso o processo do RM costume demorar mais.

Testar execução 

## Testar Execução

O botão **Testar Execução** permite validar a requisição SOAP antes de finalizar a criação da atividade. Durante o teste, o sistema envia a requisição utilizando os dados informados no XML e retorna o resultado da operação, permitindo verificar se:

* Os parâmetros foram preenchidos corretamente
* A estrutura do XML está válida
* A operação SOAP está respondendo conforme esperado

Esta funcionalidade é recomendada para garantir que a atividade será criada com uma requisição funcional e que não ocorrerão falhas durante sua execução no fluxo automatizado.

**Importante:** O tempo de espera da execução reflete o tempo real de processamento do RM. Processos longos podem levar mais tempo para concluir, o que é um comportamento esperado.

Finalização e Ações Pós-CriaçãoCertifique-se de ter realizado o **Testar Execução** antes de chegar a esta tela para garantir que a atividade salva esteja 100% funcional.

Após preencher todos os campos obrigatórios e clicar em **FINALIZAR**, o sistema processará a criação da sua atividade SOAP de Registro RM. Uma mensagem de confirmação será exibida com três opções de direcionamento, permitindo que você escolha o próximo passo no seu fluxo de trabalho.

### Opções de Direcionamento

Ao visualizar a mensagem **"Atividade SOAP Criada com Sucesso!"**, você terá as seguintes alternativas:

* **FECHAR**: Esta opção encerra completamente o assistente (wizard) de configuração. Ao clicar em Fechar, você será redirecionado para a **página inicial do sistema**, finalizando o processo de criação atual sem abrir a atividade.
* **CRIAR NOVA ATIVIDADE**: Ideal para quando há necessidade de cadastrar múltiplos registros ou processos em sequência. Ao selecionar esta opção, o sistema limpa os dados atuais e **reinicia o fluxo do zero**, voltando para o estágio inicial do wizard de Registro RM.
* **ABRIR ATIVIDADE**: Esta opção redireciona você **diretamente para a tela da atividade recém-criada**. É o caminho recomendado caso precise realizar ajustes finos, conferir o XML gerado ou incluir a atividade imediatamente em um cenário de teste.

Processos RM

Este módulo é focado na automação, padronização e execução de tarefas rotineiras, operacionais e estratégicas do TOTVS RM por meio da arquitetura SOAP.

> A funcionalidade de **Processos** permite automatizar etapas de trabalho que normalmente exigiriam intervenção manual, transformando rotinas complexas em execuções disparadas via serviço. Isso garante maior produtividade, padronização das tarefas e assegura que as regras de negócio sejam aplicadas de forma consistente em todo o sistema.

Navegação para Processos 

 1. Navegue no menu do TOTVS Automação de Testes e clique em: **Linha RM** → **Processos**

1. Automação de Testes

## Automação de Testes

É a primeira fase do **Assistente de Configuração da Automação de Testes**, responsável por:

* Garantir que todas as etapas seguintes sejam carregadas com base na infraestrutura selecionada

Configure a infraestrutura de referência:

* **Ambientes:** Selecione o ambiente RM para buscar os dados de configuração.

* **Servidor (Obrigatório):** Escolha o servidor para a leitura técnica do sistema.

2. RM (Conexão)

Estabeleça a comunicação com o serviço **RM.Host**:

Informe o endereço (Ex: `http://localhost:8051`).

* Por padrão, a porta mais utilizada é a **8051**. No entanto, essa configuração pode variar de acordo com o ambiente ou alguma necessidade específica.  
  Caso seja necessário, o usuário possui **liberdade para alterar a porta**, desde que o endereço informado seja válido e acessível.

Usuário e Senha**:** Insira suas credenciais de acesso ao RM.

* Utilize o botão **TESTAR CONEXÃO** para validar os dados antes de prosseguir.

3. Processos RM

## Processos RM

Nesta etapa, o usuário deve selecionar um dos processos do RM executados **hoje**. A escolha do processo permite que a interface guiada (wizard) avance para a etapa de **revisão do XML** gerado.

A tela exibe uma lista com os processos do dia, junto com informações que ajudam na identificação. Para continuar, basta selecionar o processo desejado clicando no ícone à esquerda.

Certifique-se de fornecer os dados de conexão corretos, pois somente os processos executados com essas informações aparecerão na lista.

#### **Informações apresentadas**

* **ID Job** – Identificador único da execução do job no RM.
* **Nome** – Nome do processo registrado no RM.
* **Sistema** – Código do sistema responsável pelo processamento.
* **Status** – Situação final do job (ex.: concluído, com erro, em execução).

1. No RM, execute o processo que deseja automatizar
2. Avalie processos que possam ser reexecutados para a automação - ou garanta que a execução aconteça em uma base onde o mesmo ainda não foi executado.
3. Certifique que o processo executou da forma correta lá no RM antes de ser automatizado aqui no TAT.
4. Exibir informações do XML

## Exibir informações do XML

Nesta etapa, você poderá visualizar todo o conteúdo do XML gerado a partir das informações preenchidas nas etapas anteriores. O objetivo é permitir que você confira se todos os dados estão corretos antes de finalizar o processo.

Aqui você pode analisar o XML completo, verificar se existe alguma inconsistência e garantir que tudo está conforme o esperado. Caso perceba algum erro, você pode voltar para as etapas anteriores, ajustar as informações e retornar para esta tela. Quando estiver tudo certo, basta avançar para concluir o Wizard.

* **Para processos:** o XML aqui virá com uma estrutura que contemple todos os parâmetros utilizados para a execução do processo selecionado.

Se você clicar em **ANTERIOR**, aparecerá uma mensagem de confirmação:

**Deseja realmente voltar? As alterações serão perdidas.**

Isso significa:

* Se você editou o XML manualmente e tentar voltar, o sistema **descarta** qualquer modificação feita na tela.
5. Criação de Atividade

Nesta etapa, você irá configurar as informações finais necessárias para que a atividade seja criada dentro do sistema. Essas informações definem como a automação será identificada, descrita e executada quando for utilizada em um fluxo. Dependendo do tipo de atividade que você estiver criando, esses dados serão utilizados pelo sistema para estruturar e realizar corretamente a execução durante os testes ou processos automatizados.

Grupo

Seleciona o grupo ao qual a atividade pertencerá.

O [grupo](https://tdn.totvs.com/pages/viewpage.action?pageId=680234913#Cria%C3%A7%C3%A3odeumgrupo-1729228565) organiza e controla quem pode visualizar ou utilizar essa atividade.

Versão

Define a versão da atividade que está sendo criada.

* Isso é útil para controle de alterações e evolução de processos.

A versão da atividade é utilizada apenas para fins de organização, controle e evolução das automações no TAT. Ela não possui relação nem impacto técnico com a versão do RM em uso.

*Exemplo utilizando a versão do RM*

*Exemplo utilizando a versão padrão*

Nome da atividade

É o nome que identificará a automação dentro da plataforma.

* Escolha um nome que represente bem o que a atividade faz, facilitando a identificação por você e pela sua equipe.

Descrição da atividade

Campo destinado a explicar, de forma resumida, o propósito da automação.

* Uma boa descrição ajuda a documentar o processo e facilita a manutenção futura.

Timeout (segundos)

Tempo máximo que a execução pode levar antes de ser interrompida automaticamente.

* O valor padrão é 30 segundos, mas você pode aumentar caso o processo do RM costume demorar mais.

Testar execução 

## Testar Execução

O botão **Testar Execução** permite validar a requisição SOAP antes de finalizar a criação da atividade. Durante o teste, o sistema envia a requisição utilizando os dados informados no XML e retorna o resultado da operação, permitindo verificar se:

* Os parâmetros foram preenchidos corretamente
* A estrutura do XML está válida
* A operação SOAP está respondendo conforme esperado

Esta funcionalidade é recomendada para garantir que a atividade será criada com uma requisição funcional e que não ocorrerão falhas durante sua execução no fluxo automatizado.

**Importante:** O tempo de espera da execução reflete o tempo real de processamento do RM. Processos longos podem levar mais tempo para concluir, o que é um comportamento esperado.

Finalização e Ações Pós-CriaçãoCertifique-se de ter realizado o **Testar Execução** antes de chegar a esta tela para garantir que a atividade salva esteja 100% funcional.

Após preencher todos os campos obrigatórios e clicar em **FINALIZAR**, o sistema processará a criação da sua atividade SOAP de Registro RM. Uma mensagem de confirmação será exibida com três opções de direcionamento, permitindo que você escolha o próximo passo no seu fluxo de trabalho.

### Opções de Direcionamento

Ao visualizar a mensagem **"Atividade SOAP Criada com Sucesso!"**, você terá as seguintes alternativas:

* **FECHAR**: Esta opção encerra completamente o assistente (wizard) de configuração. Ao clicar em Fechar, você será redirecionado para a **página inicial do sistema**, finalizando o processo de criação atual sem abrir a atividade.
* **CRIAR NOVA ATIVIDADE**: Ideal para quando há necessidade de cadastrar múltiplos registros ou processos em sequência. Ao selecionar esta opção, o sistema limpa os dados atuais e **reinicia o fluxo do zero**, voltando para o estágio inicial do wizard de Registro RM.
* **ABRIR ATIVIDADE**: Esta opção redireciona você **diretamente para a tela da atividade recém-criada**. É o caminho recomendado caso precise realizar ajustes finos, conferir o XML gerado ou incluir a atividade imediatamente em um cenário de teste.

Exemplo Prático Exemplo Prático – Incluir / Editar Cadastro

## Exemplo Prático – Incluir / Editar Cadastro (RM Imobiliário)

### Cenário

Imagine que o analista de testes precise **validar o cadastro de um novo imóvel** no RM Imobiliário, garantindo que os dados enviados via WebService sejam corretamente persistidos no banco de dados.

O objetivo deste teste é **criar ou alterar um registro de imóvel** utilizando o Facilitador RM, sem a necessidade de desenvolvimento manual de SOAP.

### Fluxo Prático

1. **Acesso ao Facilitador**

   * Menu: **Facilitadores RM → Incluir/Editar**
   * Selecionar o ambiente RM de testes.
2. **Configuração da Infraestrutura**

   * Servidor: `RM-TESTE`
   * Host: `http://localhost:8051`
   * Usuário e senha válidos do RM.
   * Testar conexão com sucesso.
3. **Definição do Contexto**

   * `CodColigada = 1`
   * `CodSistema = I` (Imobiliário)
   > Isso garante que o cadastro será realizado na empresa e módulo corretos.
4. **Seleção do DataServer**

   * DataServer selecionado: **ImoImovelData** (exemplo)
   * Aplicar filtros para localizar um imóvel existente **ou**
   * Utilizar um registro base apenas como modelo.
5. **Geração e Ajuste do XML**

   * O sistema gera automaticamente o XML do imóvel.
   * Para **Inclusão**:

     + Alterar a chave primária (ex.: Código do imóvel).
   * Para **Edição**:

     + Manter a chave primária e alterar apenas campos como:

       - Descrição
       - Situação
       - Valor do imóvel
6. **Teste de Execução**

   * Executar o botão **Testar Execução**
   * Validar retorno de sucesso do SOAP.
7. **Finalização**

   * Nome da atividade:  
     **Cadastro Imóvel – Incluir/Editar**
   * Descrição:  
     Automação para inclusão ou edição de imóveis no RM Imobiliário via DataServer.
   * Finalizar e salvar a atividade.

### Resultado Esperado

* O imóvel é **criado ou atualizado com sucesso** no RM.
* Os dados persistem corretamente no banco.
* A atividade pode ser reutilizada em fluxos automatizados de testes.
Exemplo Prático – Excluir Cadastro

## Exemplo Prático – Excluir Cadastro (RM Imobiliário)

### Cenário

O analista de testes precisa validar se o RM **bloqueia ou permite corretamente a exclusão de um imóvel**, respeitando regras de integridade e dependências.

### Fluxo Prático

1. **Acesso ao Facilitador**

   * Menu: **Facilitadores RM → Excluir Cadastros**
2. **Configuração da Infraestrutura**

   * Ambiente RM configurado.
   * Host RM.Host validado.
   * Conexão testada com sucesso.
3. **Definição do Contexto**

   * `CodColigada = 1`
   * `CodSistema = I`
4. **Seleção do DataServer**

   * DataServer: **ImoImovelData**
   * Aplicar filtros para localizar **exatamente um imóvel**.
5. **Geração Automática do XML**

   * O XML é gerado automaticamente.
   * Contém **somente as chaves primárias** do imóvel.
   * XML disponível apenas para visualização (sem edição).
6. **Teste de Execução**

   * Executar **Testar Execução**
   * Validar retorno:

     + Sucesso → imóvel excluído
     + Erro → dependências existentes (comportamento esperado)
7. **Finalização**

   * Nome da atividade:  
     **Excluir Imóvel RM**
   * Descrição:  
     Automação para exclusão de imóvel via DataServer com validação de integridade.

### Resultado Esperado

* O RM valida automaticamente dependências.
* O registro é excluído apenas se não comprometer a consistência do sistema.
* O teste garante segurança e confiabilidade da exclusão.
Exemplo Prático – Execução de Processos RM

Exemplo Prático – Execução de Processos RM

### Cenário

O analista deseja automatizar a execução de um **processo padrão do RM**, como por exemplo:

> **Atualização de Situação de Imóveis** ou **Reprocessamento de Cálculos Imobiliários**

### Fluxo Prático

1. **Execução Prévia no RM**

   * O processo é executado manualmente no RM.
   * Confirmar que finalizou com **status concluído**.
2. **Acesso ao Facilitador**

   * Menu: **Linha RM → Processos**
3. **Configuração da Infraestrutura**

   * Ambiente, servidor e RM.Host configurados.
   * Conexão validada.
4. **Seleção do Processo**

   * Lista exibe processos executados no dia.
   * Selecionar o processo desejado pelo **ID Job**.
5. **Visualização do XML**

   * XML completo é exibido.
   * Contém todos os parâmetros utilizados na execução real.
6. **Teste de Execução**

   * Validar se o processo pode ser reexecutado corretamente via SOAP.
7. **Finalização**

   * Nome da atividade:  
     **Processo RM – Atualização Imobiliária**
   * Descrição:  
     Automação para execução de processo RM a partir de job previamente executado.

### Resultado Esperado

* O processo é executado automaticamente via TAT.
* Regras de negócio do RM são respeitadas.
* A atividade pode ser reutilizada em cenários de testes regressivos.

---

# Saiba mais

O serviço RM.Host é o responsável por processar as requisições SOAP enviadas pelo TAT. Sem uma conexão estável com ele (geralmente via porta 8051), a ferramenta não consegue realizar a leitura técnica ou a execução dos testes.

Utilize filtros de pesquisa bem definidos ao buscar registros no RM. Isso facilita a identificação do registro base e aumenta a confiabilidade da automação gerada.Valide sempre a requisição antes de finalizar a criação da atividade. O teste prévio ajuda a identificar inconsistências no XML, problemas de autenticação ou falhas de comunicação com o RM.Host.

Para usuários avançados que desejam personalizar o XML, a dica de clicar com o **botão direito** em um campo dentro do RM é essencial. Isso revela o nome físico da coluna na base de dados, permitindo mapear exatamente qual tag do XML corresponde a qual campo da tela.

No módulo de **Processos**, o sistema lista jobs executados no dia. Cada job possui um **ID Job** único, que funciona como uma "caixa preta" contendo todos os parâmetros e XMLs utilizados naquela execução específica, servindo de base perfeita para sua automação.

Defina corretamente o Contexto da operação, garantindo que a automação seja executada na Coligada e no Sistema corretos. Um contexto mal configurado pode resultar em alterações em unidades incorretas ou falhas na execução.

Dentro da tela de edição do cadastro no próprio RM, pressione a combinação de teclas **CTRL + ALT + F9**. O sistema exibirá o nome técnico do DataServer em uso.

# FAQ

**P**: Quando devo criar uma nova versão de uma atividade?

**R:** Sempre que houver alteração no XML, mudança de comportamento do processo ou necessidade de adaptação para outra versão do RM. Isso evita impactos em fluxos já existentes.

**P:** Posso utilizar a mesma atividade em diferentes ambientes RM?

**R:** Sim, desde que o DataServer, o contexto e a versão do RM sejam compatíveis com o ambiente onde a atividade será executada.

**P:** O que acontece se eu selecionar um registro incorreto como base?

**R:** A automação será criada com base nesse registro, o que pode gerar resultados inesperados. Por isso, é recomendado utilizar filtros específicos e validar os dados antes de avançar.

**P:** Posso ajustar o XML manualmente após a atividade criada?

**R:** Sim. A atividade pode ser editada ou versionada posteriormente, permitindo ajustes controlados sem comprometer automações já existentes.
