---
content_hash: 81cdd8c133afa26dcf788e88047e6c7b03629917a187ece916f0de5799eb6047
fetched_at: '2026-06-29T00:12:09.502161+00:00'
page_id: '946431925'
product: rm
source: tdn-rm
title: Como criar uma conta One Drive for Business com o FileRepo
type: documentation
url: https://tdn.totvs.com/display/LRM/Como+criar+uma+conta+One+Drive+for+Business+com+o+FileRepo
version: 30
---

#### **Pré-requistos**

1. Uma conta de administrador no Microsoft 365/Azure AD.
2. Acesso ao portal do Azure ([portal.azure.com](https://www.google.com/search?q=portal.azure.com)).
3. Familiaridade básica com os conceitos de OAuth 2.0 e Azure AD.

   Observação

   A integração One Drive for Business, não funciona com:  
   - SharePoint ou One Drive Personal

   O tipo da licença deve ser OneDrive for Business para Armazenamento pessoal corporativo, Licença Microsoft 365 com SPO

#### **Passo 1: Criando um Aplicativo**

1. Acesse <https://portal.azure.com/>
2. Na pesquisa de Serviços, Recursos e Documentos, informe: Registros de aplicativo.

   Demonstração
3. Clique em + Novo registro.  
   Informe o nome do Aplicativo e selecione o tipo de conta, opção é a padrão.

   Demonstração
4. Clique no botão Registrar.

#### **Passo 2: Configurando o Aplicativo**

Visão geralvisaogeral

Demonstração

1. Anote os identificadores:  
   ID do aplicativo (cliente)  
   ID do diretório (locatário)
2. Clique no link ao lado direito de URIs de Redirecionamento.

   Demonstração
3. Clique no botão + Adicionar uma plataforma.  
   Será exibido um menu lateral a direita.
4. Selecione Aplicativos móveis e de área de trabalho.

   Demonstração
5. Informar <http://localhost> no campo URIs de redirecionamento personalizados.

   Demonstração
6. Clicar no botão Configurar.

#### **Passo 3: Gerando as Credenciais**

1. Volte para a  do Aplicativo.
2. Clique no link a direita de Credenciais de cliente.

   Demonstração
3. Clique em + Novo segredo do cliente.
4. Informe uma descrição e o tempo de expiração.  
   Obs: Após este tempo a integração será interrompida pelo serviço do One Drive.

   Demonstração
5. Clicar no botão adicionar.
6. Anotar o Valor do Segredo e o ID Secreto. credenciais

   Demonstração

#### **Passo 4: Configurando as Permissões**

1. Volte para a  do Aplicativo.
2. Clique em Permissões de Api, no menu.

   Demonstração
3. Clique em + Adicionar uma permissão.
4. Selecione o quadro Microsoft Graph e Permissões de aplicativo.
5. Busque pela palavra "files".
6. Selecione e marque a caixa: Files.Read.All e Files.ReadWrite.All
7. Clique no botão Adicionar permissões.  
   Será apresentada na tela de Permissões de APIs o nome das permissões selecionadas

   Demonstração
8. Clicar em Conceder consentimento do administrador para MSFT.

   Demonstração

   Note que o Status mudou para um ícone verde!

#### **Passo 5: Montar o Json**

1. Será necessário montar um arquivo no formato Json, com codificação UTF-8, para habilitar a integração.
2. Abaixo o formato e quais os dados devem ser usados neste arquivo:

   jsArquivo Json

   TenantId e AppId são encontrados na tela .  
   ClientSecret, são encontrados na tela .
3. Salve o arquivo em uma pasta.
4. Na tela de cadastro Selecione este arquivo para concluir a integração.  
   Mais detalhes em:

Informação sobre o One Drive

1. **A onde ficam os arquivos**Os arquivos enviados são armazenados na conta do usuário dentro do OneDrive for Business, dependendo do tipo de conta utilizada.   
   Eles podem ser acessados através da interface web do OneDrive ou via API do Microsoft Graph.  
   Os arquivos são organizados dentro da pasta raiz (/drive/root) ou em diretórios específicos definidos pelo usuário.
2. **Como funciona a segurança**  
   A segurança é garantida por algumas camadas de proteção, como:  
   Autenticação e Autorização, o acesso à API é feita via OAuth 2.0, onde o aplicativo precisa obter um token de acesso para interagir com os arquivos do usuário.  
   Controle de Permissões, o usuário pode definir permissões específicas para cada arquivo ou pasta, permitindo acesso apenas a determinados usuários ou grupos.  
   Criptografia, todos os arquivos armazenados no OneDrive são protegidos por criptografia em repouso e criptografia em trânsito.

Mais informações em: <https://learn.microsoft.com/pt-br/onedrive/>
