---
article_id: 7216517178391
category: Meu RH - Login
content_hash: ee702f23f1d4930d3be6c917d0bbca853f7c2d3b07fa8c6fdc0633888e087edf
fetched_at: '2026-06-28T22:47:27.273714+00:00'
product: rm
section_id: 37725850167319
source: central-rm
title: RH - RM - Meu RH - Como integrar e autenticar o Meu RH com o TOTVS Identity
type: support-article
updated_at: '2026-01-16T15:26:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7216517178391-RH-RM-Meu-RH-Como-integrar-e-autenticar-o-Meu-RH-com-o-TOTVS-Identity
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24075221896855) Tempo aproximado para leitura: **00:14:41 min**  
  
**Dúvida**  
Como integrar e autenticar o Meu RH com o TOTVS Identity?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) – Meu RH – A partir da release 12.1.34  
  
**Solução**  
Além da autenticação padrão utilizando o usuário do ERP, também é possível configurar o Meu RH para autenticar com o provedor de identidade TOTVS Identity. Para isso, siga os passos abaixo:

1. Dentro da aplicação do TOTVS Identity, selecione a opção Aplicativos e clique no botão "Novo aplicativo" e selecione a opção "Padrão":

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7215189817879)

1.1 Na aba **"Visão geral"** estão as informações gerais sobre o aplicativo:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7215489259543)

* **Nome da Aplicação**: Nome do aplicativo que será exibido na tela de autenticação do TOTVS Identity
* **Descrição:** Breve descrição do aplicativo
* **Categoria:** Tipo de aplicativo
* **Navegável:** Indica se o aplicativo estará visível no Launchpad
* **Trocar Logo:** Imagem que será exibida na tela de autenticação do TOTVS Identity
* **Habilitar Segurança OAuth 2.0:** Deixar desmarcado

Após preencher todas as informações da aba, clicar em **"Salvar"**

1.2 Na aba **"Entrar"** estão as informações de configuração do aplicativo:

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7215790778135)

* **Modo de Login:** SAML
* **Tipo Inic SSO:** IDP\_INITIATED
* **ID da Entidade Específica do Domínio:** Deixar desmarcado
* **URL Completa:** Deixar desmarcado
* **Domínio:** Deixar em branco
* **Formato do Name ID:** Endereço de Email
* **Assinatura do Response:** Deixar marcado
* **Resposta Criptografia:** Deixar desmarcado
* **Assinatura do Assertion:** Deixar marcado

1.3 Ainda na aba **"Entrar"**:

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7215851236247)

* **URL do Consumidor de Asserções:** o formato da URL deve ser escrita da seguinte maneira → **http(s)://****IP da máquina onde exista serviço de host configurada****:****Porta WebApi configurada no serviço****/RMCloudPass/SSOSaml2?ProviderId=****Número do Id do provider cadastrado no ERP**
* **Destinatário:**o formato da URL deve ser escrita da seguinte maneira → **http(s)://****IP da máquina onde exista serviço de host configurada****:****Porta WebApi configurada no serviço****/RMCloudPass/SSOSaml2?ProviderId=****Número do Id do provider cadastrado no ERP**
  + **OBS: O número que deve ser passado no parâmetro ProviderId é o mesmo Id cadastrado para o provider dentro do ERP. Exemplo de**
  + **URL:** [**http://192.168.1.10:8051/RMCloudPass/SSOSaml2?ProviderId=3**](http://192.168.1.140:8051/RMCloudPass/SSOSaml2?ProviderId=12)
* **Público:**TOTVS
* **Nome do Emissor SP:**TOTVS
* **Mapeamento ID de Usuário:**E-mail do Usuário
* **Usar URL de Acesso Direto ao Aplicativo:**Deixar marcado
* **Autenticação Externa:**Deixar desmarcado
* **Sincronizar login SAML com e-mail do AD:**Deixar desmarcado

Após preencher todas as informações da aba, clicar em **"Salvar"**

1.4 Na aba **"Provisionar"** estão as informações de provisionamento do aplicativo:

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7215934611095)

* **Habilitar Provisionamento:** Deixar desmarcado

Após preencher todas as informações da aba, clicar em **"Salvar"**

**2 - Configurando o ERP**

Além da criação do aplicativo dentro do TOTVS Identity, também é necessário parametrizar algumas informações dentro do ERP.

2.1 Permissionamento:

Para habilitar o menu de configuração de aplicativos SAML dentro do ERP, é necessário primeiro habilitar as seguintes permissões de menu do módulo de **Serviços Globais**:

* 06 - Gestão
  + 06.06 - Comunicação
    - 06.06.08 - Aplicativos SAML
      * 06.06.08.01 - Inserir aplicativo SAML
      * 06.06.08.02 - Remover aplicativo SAML
      * 06.06.08.03 - Editar aplicativo SAML

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7216092076183)

2.2 Criação do aplicativo:

Após dada a permissão necessária, para realizar as parametrizações do aplicativo, acesse o menu **Serviços Globais >> Gestão >> Aplicativos SAML**e selecione para criar um novo registro:

![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7216111333399)

Devem ser preenchidas as seguintes informações:

* **Ativo:**Indica se o provider estará habilitado para ser utilizado, deverá ser marcado.
* **Nome do Provider:**Nome de identificação do provider.
* **Url de Retorno:**Url que será redirecionada após a autenticação dentro do TOTVS Identity. A Url será a de acesso do portal do Meu RH, com o final /#/login
* **RelayState:**Não precisa ser preenchido.
* **Url de login do provider:**Deve ser preenchido com a Url presente no campo "URL de acesso direto" na aba "Entrar" dentro do aplicativo criado no TOTVS Identity
* **Url de logout do provider:** Deve ser preenchido com a Url presente no campo "URL de logout direto" na aba "Entrar" dentro do aplicativo criado no TOTVS Identity
* **Metadados:**Deve ser preenchido com o certificado que está cadastrado para o aplicativo criado no TOTVS Identity. Para realizar o download desse certificado, acessar a aba "Entrar" no aplicativo criado no TOTVS Identity e clicar na opção Baixar metadados do IDP. Como é um arquivo XML, o valor que deve ser inserido está entre as chaves <ds:X509Certificate></ds:X509Certificate>

![mceclip15.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7216208236311)

Após o cadastro, será gerado um Id para o aplicativo que vai ser utilizado nas configurações dos tópicos **1.3** e **3.1**:

![mceclip16.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7216235410583)

2.3 Associando o usuário ao e-mail do TOTVS Identity

Para que o usuário consiga se autenticar no Meu RH através do TOTVS Identity é necessário que ele tenha o mesmo e-mail cadastrado dentro do ERP. Para isso, acesse o menu **Serviços Globais >> Segurança >> Usuários:**

Selecione o usuário e abra para edição. No campo "Email" deve estar cadastrado o e-mail de acesso do TOTVS Identity para aquele usuário:

3 Por fim, é necessário também configurar a parte do Meu RH. **Só é possível utilizar apenas um provider ativo para o Meu RH, ou seja, mesmo que existam mais aplicativos ativos, apenas o especificado no arquivo Web.config será considerado**

3.1 Para habilitar o uso do aplicativo configurado no tópico **2.2** dentro do Meu RH, é necessário adicionar a tag <add key="SamlProviderIdMyHr" value="id" /> no arquivo Web.config da pasta FrameHTML na seção <appSettings>, substituindo o "id" pelo Id cadastrado no aplicativo dentro do ERP. Por exemplo, no tópico anterior cadastramos um aplicativo cujo Id é 3, então a chave ficaria dessa forma <add key="SamlProviderIdMyHr" value="3" />

![mceclip17.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7216410077463)

3.2 Através do portal existem duas formas de acesso, utilizando o LaunchPad do TOTVS Identity ou autenticando pela tela de login do TOTVS Identity que redireciona diretamente para o Portal Meu RH. Através do Launchpad, basta se logar na plataforma do TOTVS Identity, selecionar o menu Launchpad e clicar no ícone do aplicativo criado:

![mceclip18.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7216415097623)

A outra forma é utilizar a própria Url já configurada para o portal Meu RH, onde o usuário será redirecionado para a tela de login com o botão indicando o login via TOTVS Identity:

![mceclip19.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7216434360215)

Após clicar no botão, o usuário será redirecionado para a tela de login do TOTVS Identity, ou caso já esteja logado no TOTVS Identity será redirecionado para a home do Meu RH:

![mceclip20.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7216436772247)

3.2.1 No aplicativo, quando o ambiente estiver configurado com o TOTVS Identity a tela de login irá ser apresentada com o botão de acesso ao TOTVS Identity e ao clicar no botão, o usuário será redirecionado para a tela de autenticação do TOTVS Identity::

![mceclip22.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7216439690135)![mceclip23.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7216441299863)  
  
**Saiba Mais**

[Maiores detalhes, confira clicando aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=651934203)
