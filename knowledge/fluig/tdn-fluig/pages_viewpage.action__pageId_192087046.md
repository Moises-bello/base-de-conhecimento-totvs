---
content_hash: 7739c9a7c818ebed5627617d3dc4a6b0dd5daa529417d0ba860ee5119925d20f
fetched_at: '2026-06-28T21:35:19.116893+00:00'
page_id: '192087046'
product: fluig
source: tdn-fluig
title: Usuário Google Analytics
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=192087046
version: 33
---

Atenção

O Google desativará o Universal Analytics em **01 de Julho de 2023** e será substituído pelo Google Analytics 4.

Essa desativação fará com que os dados da sua empresa no TOTVS Fluig Plataforma deixem de ser coletados e para que você consiga continuar medindo os acessos ao Fluig utilizando o Google Analytics 4, é necessário que uma nova propriedade do Google Analytics 4 seja criada e configurada no TOTVS Fluig Plataforma.

Recomendamos que a nova propriedade seja configurada antes do prazo da desativação conforme os passos descritos nesta documentação.

Ressaltamos que: para que a configuração funcione de modo esperado a plataforma Fluig precisa estar na release **[1.8.0-040423](https://tdn.totvs.com/x/3QR2KQ)** ou **superiores**.

# Índice

4true.\*ndicenone

# Objetivo

O objetivo desta documentação é demonstrar os passos iniciais para configuração da integração do TOTVS Fluig Plataforma com o Google Analytics. O Google Analytics é uma ferramenta gratuita de monitoramento de servidor, que disponibiliza informações precisas de uso por requisição, entre outros dados. Com ele é possível saber quem está utilizando o servidor no momento, praticamente em tempo real, dependendo das condições da conexão.

# Inscrever-se no Google Analytics

Para inscrever-se no Google Analytics, é necessário criar ou possuir uma [Conta do Google](https://accounts.google.com/SignUp?hl=pt-BR) (esta mesma conta é usada para acessar serviços do Google como o Gmail, YouTube, Play Store, etc.). Uma vez criada a conta, é possível seguir os passos abaixo.

As telas abaixo podem apresentar diferenças em relação ao que está demonstrado, devido a eventuais atualizações da Google.

falsecriar\_usuario\_gatruePasso 1

* Acessar <https://analytics.google.com/>.
* Prosseguir com o **Login no Google Analytics** e autenticar-se com a conta do Google .

Passo 2

* Após efetuar o login, será apresentada a página abaixo.
* Acionar **Começar a usar**.

Passo 3

* Será apresentada a seção de **Configuração da conta**.
* Nesse momento, deve-se configurar o nome da conta do usuário, um identificador único para a conta no Google Analytics.
* Nesta mesma página também é possível informar se deseja que setores do Google acessem as informações da conta criada no Google Analytics de alguma forma.

Lembre-se que, mesmo que as informações sejam desmarcadas, alguns produtos Google ainda podem verificar informações de sua conta Google Analytics, a menos que sejam manualmente desativados pela opção "Vinculação de Produto".

* Acionar **Próxima** para continuar a configuração.

Passo 4

* Será apresentada a seção de **Configuração da propriedade**.
* Nesse momento, deve-se configurar o nome da propriedade, um facilitador para identificar o endereço sendo monitorado.
* Clique em **Próxima** para continuar a configuração.

Passo 5

* Será apresentada a seção **Sobre sua empresa**.
* Nesse momento, deve-se configurar os dados conforme o tamanho da empresa e objetivos.
* Acionar **Criar**para concluir a configuração.

Passo 6

* Será apresentado o contrato de Termos de serviço.
* Acionar **Aceito** para prosseguir.

Passo 7

* Após aceitar os Termos de Serviço, uma nova tela aparecerá. Clique em **Web**.

* Em seguida, preencha a URL do site e o Nome do Fluxo e clique em **Criar Fluxo**.

Passo 8

* Copie o **ID da Métrica** apresentado na tela de Detalhes do Fluxo e em seguida clique em **Gerenciar as tags do site conectadas**.

* Cole o ID copiado e digite um apelido na tela que surge. Em seguida, clique em **Conectar**.

# Informar o usuário do Google Analytics no TOTVS Fluig Plataforma

Com o ID de acompanhamento em mãos, acessar o Fluig Plataforma com um usuário administrador da empresa.

falsepainel\_controletruePasso 1

* Acessar o **Painel de controle** → agrupador **Parâmetros técnicos** → **Usuário Google Analytics**.

Passo 2

* Informar o ID de acompanhamento no campo **Token**.
* Acionar **Salvar**.A integração estará ativa e o Fluig passará a informar o Google Analytics de suas requisições HTTP, permitindo o monitoramento do servidor e o acesso a algumas informações privilegiadas, como acessos e requisições, em tempo hábil.

Para desabilitar o envio de informações futuramente, basta assinalar a opção **Desabilitar o Google Analytics** e acionar **Salvar**.
