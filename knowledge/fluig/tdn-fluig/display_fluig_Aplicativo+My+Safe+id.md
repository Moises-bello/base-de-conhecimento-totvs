---
content_hash: bd07833e7953027f4bf7eb94e7db2836e06f354fd431d010a9cc8cc1e290f777
fetched_at: '2026-06-28T21:35:25.763044+00:00'
page_id: '309405201'
product: fluig
source: tdn-fluig
title: Aplicativo My Safe id
type: documentation
url: https://tdn.totvs.com/display/fluig/Aplicativo+My+Safe+id
version: 78
---

true.\*ndicenone

# Objetivo

O objetivo deste guia é orientar os usuários sobre a utilização do aplicativo **My Safe id** para proteção de suas contas em serviços *online* através da autenticação multifator.

# Autenticação Multifator + My Safe id

A autenticação multifator oferece uma camada adicional de segurança para serviços e aplicações *web* através de um token (chave eletrônica) gerado no aplicativo My Safe id. Este token deve ser informado na página de login do serviço para liberar o acesso à conta.

Assumindo que apenas o usuário tem acesso ao aparelho - e portanto ao token - agentes maliciosos serão barrados, mesmo que possuam o login e a senha, pois não dispõe do código gerado pelo My Safe id. Além disso, para impedir a reutilização de um token, o código é substituído automaticamente a cada 30 segundos.

# Como obter o aplicativo My Safe id?

O aplicativo My Safe id pode ser obtido para iPhone na [App Store](https://itunes.apple.com/br/app/safe-id/id1304505629?mt=8) e para smartphones Android na [Google Play Store](https://play.google.com/store/apps/details?id=com.fluig.mfa).

# Como adicionar uma conta ao My Safe id?

A conta do serviço ou aplicação *web* pode ser adicionada ao My Safe id de duas formas: através do escaneamento de um código (*QR code*) ou informando manualmente a chave de acesso.

Tanto o *QR Code* quanto a chave para inclusão manual são fornecidos pelo serviço/aplicação que será adicionado ao My Safe id. .

falseincluir\_contatrueEscanear código

* Abrir o aplicativo My Safe id no smartphone.

* Acionar o botão  para acessar a tela de inclusão de contas.

É necessário conceder ao My Safe id a permissão de acesso à câmera do aparelho para o escaneamento do código.

* A câmera do aparelho será ativada para escaneamento do *QR* *code*.

* Aponte a câmera para o *QR code* para efetuar a leitura da código.

* Pronto! A conta será adicionada automaticamente à tela inicial do My Safe id e o token já pode ser utilizado para autenticação no serviço.

Incluir manualmente

* Abrir o aplicativo My Safe id no smartphone.

* Acionar o botão  para acessar a tela de inclusão de contas.

* Acionar **OK, Entendi** no canto inferior da tela.

* Acionar **Adicione manualmente** no canto inferior da tela.

* Informar o nome do serviço/aplicação no campo **Título**.

* Informar o nome de usuário ou e-mail de acesso no campo **Conta**.

* Informar a chave de acesso fornecida pelo serviço/aplicação no campo **Chave**.

* Acionar  para salvar as informações.

* Pronto! A conta será adicionada automaticamente à tela inicial do My Safe id e o token já pode ser utilizado para autenticação no serviço.

Sem internet? Sem problemas!

Não é necessária conexão à internet no smartphone para adicionar novas contas ou para consultar os tokens no My Safe id.

## Como editar os dados da conta?

O My Safe id permite a edição do título e do usuário/login associados à conta. Abra o aplicativo e siga os passos abaixo.

falseeditartruePasso 1

* Navegar até a conta que será alterada deslizando a tela para os lados.

Passo 2  

* Acionar  no canto superior direito da tela.

Passo 3

* Informar o novo título e/ou conta.

* Acionar  para salvar as alterações.

## Como remover a conta?

O My Safe id permite remover as contas adicionadas. Abra o aplicativo e siga os passos abaixo.

falseremovertruePasso 1

* Navegar até a conta que será removida deslizando a tela para os lados.

Passo 2  

* Acionar  no canto superior direito.

Passo 3

* Acionar .

* Para confirmar a exclusão, acionar **OK**.

# Como adicionar uma conta do TOTVS Identity ao My Safe id?

O passo a passo a seguir demonstra como habilitar a autenticação multifator em uma conta do TOTVS Identity e adicioná-la ao My Safe id.

DICA!

Lembrando que essa configuração, por padrão, é opcional, mas pode ser configurada como obrigatória pela administração da empresa. Para mais detalhes, consulte a documentação .

falseidentityPasso 1

* A demonstração a seguir será ilustrada a partir do ponto de vista de um Usuário comum do TOTVS Identity, porém o procedimento é o mesmo para contas Administrador.
* Passar o cursor do *mouse* sobre o nome do usuário no canto superior direito da página para exibir o menu da conta.
* Acionar **Segurança**.

Passo 2

* Baixar o aplicativo **My Safe id** a partir da loja de aplicativos correspondente ao sistema operacional do smartphone utilizado pelo usuário (iPhone ou Android).

* Abrir o My Safe id no aparelho.

* Acionar  no app

* Apontar a câmera do dispositivo para o código de barras bidimensional (*QR Code*) fornecido pelo TOTVS Identity.

Passo 3

* Feita a leitura, o My Safe id irá gerar um token de acesso. Cada token possui duração máxima de 30 segundos e será renovado automaticamente.

* Informar o token no campo **000-000**. O token será validado e, se estiver correto, uma mensagem de sucesso será apresentada.

Passo 4

* A partir de agora, após preencher o e-mail e senha ao acessar o TOTVS Identity, o usuário deverá abrir o My Safe id no aparelho e informar o token gerado pelo aplicativo para se autenticar.

# Como adicionar uma conta do Google ao My Safe id? google

O passo a passo a seguir demonstra como habilitar a autenticação multifator em uma conta do Google (Passos 1 a 4) e adicioná-la ao My Safe id (Passos 5 a 10).

falseincluir\_contatruePasso 1

* Acessar a página **Minha Conta** do Google (<https://myaccount.google.com/>).

* Acionar **Login e Segurança** → **Verificação em duas etapas → Primeiros passos**.

Passo 2

* Informar a senha da conta do Google e acionar **Próxima**.

Passo 3

* O Google exige que a conta seja verificada com um número de telefone.

* Informar o número do telefone que deseja utilizar para a autenticação (com DDD) e acionar **Próxima**.

Por padrão, um código de verificação será enviado por mensagem de texto (SMS) para o número informado. Também é possível receber este código através de uma ligação telefônica.

* Preencher o campo com o código recebido e acionar **Próxima**.

Passo 4

* Confirmada a validade do número de telefone informado, acionar **Ativar** para que a conta do Google passe a suportar a autenticação multifator.

Passo 5

* Na página exibida após a ativação, localize a sessão **App Google Autenticador**.

* Acionar **Configurar**.

Passo 6

* Selecionar o tipo do dispositivo onde o My Safe id está instalado (**Android** ou **iPhone**) e acionar **Próxima**.

Passo 7

* Abrir o My Safe id no aparelho smartphone.

* Acionar o botão  no aplicativo para acessar a tela de inclusão de contas.

* Apontar a câmera do smartphone para *QR code* apresentado na tela para efetuar a leitura do código.

* Na página da conta Google, acionar **Próxima**.

Usou QR Code?

Caso a conta tenha sido adicionada utilizando a leitura do QR Code, o próximo passo pode ser desconsiderado. Avançar para o Passo 9.

* Para incluir a chave manualmente, acionar **Não consegue ler o código?**.

Passo 8  

* Abrir o aplicativo My Safe id no smartphone.

* Acionar o botão  no aplicativo para acessar a tela de inclusão de contas.

* Acionar **Adicione manualmente** no canto inferior da tela.

Este passo só deve ser executado por usuários que desejem adicionar a conta do Google ao My Safe id manualmente e **não** pelo escaneamento do *QR code*.

* Informar o nome do serviço/aplicação no campo **Título**, por exemplo, "Google".

* Informar o e-mail do Google no campo **Conta**, por exemplo, "seuemail@gmail.com".

* Informar a chave de acesso fornecida pelo Google no campo **Chave**.

* Acionar  para salvar as informações.

* Na página da conta Google, acionar **Próxima**.

Passo 9

* Na página **Minha Conta**, acionar **Concluído** para finalizar a configuração da verificação em duas etapas através do aplicativo My Safe id.

Passo 10

* A partir de agora, ao acessar a conta do Google será exigida, além do endereço de e-mail e senha, o token gerado pelo My Safe id.
