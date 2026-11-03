---
content_hash: 3b3405e185038d7d2091f6611e5a0d1dc69c424f77a5e4a01b30076fe8ad12c2
fetched_at: '2026-06-29T00:05:57.875535+00:00'
page_id: '184781284'
product: rm
source: tdn-rm
title: COMO FAZER - Inclusão de usuário para acesso ao RM Portal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=184781284
version: 12
---

false

**TOTVS Folha de Pagamento**

**Processo:** **Inclusão de usuário para acesso ao RM Portal**

**Versão: 11.8X ou 12.1.X**

1. Dentro do cadastro de funcionários selecione um funcionário que queira adicionar o usuário e vá no botão Processos -> Inclusão de Usuário para Acesso ao RM Portal

Obs. Mesmo que queira incluir para vários funcionários, selecione apenas um nesta tela.

2. Clique em Avançar na primeira tela e na segunda tela selecione a opção "Utiliza Seleção de Funcionários"

Clique para visualizar imagem

3. Clique no botão seleção de funcionários para definir melhor quais funcionários deseja incluir um novo usuário, isto pode ser feito a partir da Situação, Tipo de funcionário recebimento, Filtro ou Fórmula de Seleção. Depois de definir os funcionários clique em "OK" e depois Avançar.

Clique para visualizar imagem

4. Defina o Código de acesso ao banco e Perfil que será utilizado pelo usuário do Portal, as permissões definidas para o perfil serão as permissões que o usuário terá ao acessar o portal. Defina a validade do usuário e avance.

Clique para visualizar imagem

Obs. Deixando o campo Data Final vazio, o sistema irá considerar o usuário como sempre válido.

* O código de acesso ao banco é definido através do aplicativo Serviços Globais -> aba Segurança -> Códigos de Acesso
* O perfil é definido através do aplicativo Serviços Globais -> aba Segurança -> Perfis

5. Na próxima tela, defina o Código do Grupo de acesso ao RM Portal do usuário

Clique para visualizar imagem

**Usuário deve alterar senha no próximo login ->** Ao acessar o portal será solicitado para o usuário que o mesmo altere sua senha

**Utiliza número da coligada e chapa para código de acesso ->** Será criado um usuário conforme exemplo: Chapa 00116 / Coligada 1  
 **Parâmetro marcado:** O usuário criado será 1-00116  
 **Parâmetro desmarcado:** O usuário criado será 00116

**Utiliza CPF para código de acesso ->**Será criado o usuário com o número do CPF. **Observação:** Campo liberado a partir das versões 12.1.33.257, 12.1.34.156 e 12.1.2205.101.

**Definir CPF como senha default ->** Define o CPF cadastrado para o funcionário como a senha de login no portal / com o parâmetro desmarcado, a senha será o último nome do funcionário com letras maiúsculas

**Atualizar permissões para usuário existente ->** o sistema atualiza os dados de Código de acesso ao banco, Perfil, Validade, Código do Grupo, Usuário deve alterar senha no próximo login, Definir CPF como senha default e Núm. de dias para Forçar a Troca de Senha, caso o funcionário já possua um usuário vinculado.

**Importante:** o parâmetro "Atualizar permissões para usuário existente" só funcionará caso o código do usuário definido no processo (**chapa do funcionário**,  **Coligada + chapa do funcionário** (parâmetro "Utiliza número da coligada e chapa para código de acesso" ) ou **CPF** ("Utiliza CPF para código de acesso")) seja igual ao existente no cadastro do funcionário. 

**Exemplo:**

Clique para visualizar imagem

Usuário cadastro no sistema com **Coligada + chapa do funcionário (parâmetro "Utiliza número da coligada e chapa para código de acesso" )**

Para atualizar as permissões do usuário, deverá executar a rotina Inclusão de usuário para acesso ao RM Portal, selecionando o parâmetro **Utiliza número da coligada e chapa para código de acesso** e **Atualizar permissões para usuário existente** conforme abaixo:

6. Agora basta clicar em Executar

**Importante!**

Utilizando esta rotina o usuário do funcionário será o número da sua chapa ou coligada + chapa de acordo com o parâmetro “Utiliza número da coligada e chapa para código de acesso” demonstrado anteriormente.

Para maiores informações, acesse:
