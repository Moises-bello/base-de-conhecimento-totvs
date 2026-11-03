---
content_hash: 92029b669a791e58d714bc6e51b60f8bb0188273765bb61e9f6bead5ee37cfc0
fetched_at: '2026-06-29T00:09:08.437480+00:00'
page_id: '389546331'
product: rm
source: tdn-rm
title: Aplicativos Externos
type: documentation
url: https://tdn.totvs.com/display/LRM/Aplicativos+Externos
version: 19
---

Índice:

---

.\*ndice:

# Objetivo

---

       Neste documento será exibido o passo a passo para cadastrar no RM um novo aplicativo externo.

       Um aplicativo externo deve ser cadastrado no RM para permitir a comunicação do sistema com aplicativos terceiros, que não são da TOTVS. Por exemplo, a partir da versão 12.1.22 do RM, será possível utilizar aplicativos externos, tais como o Google, Facebook ou APIs terceiras para realizar login na MDI.

# Criando um novo Aplicativo

---

       Para cadastrar um novo aplicativo no RM, basta acessar o menu **Serviços Globais > Gestão > Aplicativos Externos.**É importante que o aplicativo no provedor já tenha sido criado - ver mais sobre como criar aplicativo no , ou .

       Ao incluir um novo aplicativo, deve-se informar os campos obrigatórios, que estão em negito.

Caso o aplicativo seja o Facebook, é necessário preencher somente os campos de chave;

       Quando o provedor do aplicativo for o Google, deve-se preencher os campos: Chave Pública, Chave Primária e Url de Retorno (Endereço Recomendado: <https://www.google.com.br/>) e URL de Descoberta (<https://accounts.google.com/.well-known/openid-configuration>) utilizada pelo Portal do Aluno.

       Se o provedor do aplicativo for WSO2, deve-se preencher todos os campos da tela, inclusive a URL de Descoberta ([https://<domínio do WSO2>/oauth2/oidcdiscovery/.well-known/openid-configuration)](https://bh-teste-ws16:9443/oauth2/oidcdiscovery/.well-known/openid-configuration) utilizada pelo Portal do Aluno.

       Se o provedor do aplicativo for Custom, deve-se preencher todos os campos da tela, em exceção o "Escopo Padrão" que não é obrigatório, mas pode ser necessário dependendo o provedor escolhido.

       O Escopo Padrão determina as informações que você obtêm do aplicativo utilizado (ex: LinkedIn) sobre o usuário durante o processo de autorização.

       Além das chaves, a URL de autorização, de recuperação do token de acesso e de recuperação de informações da conta de usuário devem ser obtidas diretamente no provedor de origem do aplicativo.

       A Url de Retorno (Url de callback) é utilizado somente para no login Winforms (MDI), no portal Corpore.NET e Portal do Aluno é utilizada a própria Url de login. É possível utilizar o link do portal ([http://Servidor:Porta/Corpore.Net/Login.aspx](https://totvs.caram.com.br/CorporeRM/Login.aspx)), o próprio site do cliente, um link disponibilizado pelo provedor do aplicativo ou um link disponibilizado no RM.Host ([http://Servidor:PortaHttp/RMRestCallback/oauth/callback](http://localhost:8051/RMRestCallback/oauth/callback));

       O "Campo de Correspondência do Provedor" é a informação enviada pelo provedor de autenticação (como UserId, Email e UserPrincipalName) que ajuda a identificar o usuário no sistema. Esse campo será utilizado para localizar o registro correspondente do usuário no RM. Já o "Campo de Correspondência do RM" é as informação disponibilizada pelo próprio RM que deve corresponder aos dados fornecidos pelo provedor para garantir a identificação correta do usuário. Entre essas opções, encontram-se o CodUsuario, Email e CodExterno. Resumidamente, o campo de correspondência do provedor representa a informação fornecida pelo provedor de autenticação, que deverá coincidir com o campo de correspondência no RM, possibilitando a identificação e o acesso seguro do usuário no sistema.

       A URL do Emissor do Token de Acesso (Issuer) identifica o provedor de identidade (IDP) responsável pela autenticação dos usuários e pela emissão dos tokens que permitem o acesso seguro aos recursos da aplicação. Esse campo é essencial para validar a autenticidade dos tokens gerados, assegurando que sejam emitidos pelo provedor correto. Por exemplo, uma URL de Issuer pode ser <https://provider.com/>. O preenchimento do Issuer é necessário caso o aplicativo utilize OAuth2 com OpenID Connect (OIDC) e seja acessado por meio do portal Meu RH.

       O campo User Principal Name (UPN) é usado para identificar o usuário autenticado no sistema, sendo normalmente representado pelo endereço de e-mail ou outro identificador único. A URL de recuperação do UPN permite que o sistema obtenha essas informações do usuário após o login, por meio do token de acesso. Com o UPN, o sistema identifica quem está acessando e associa esse identificador a um perfil ou conta já existente, facilitando o processo de autenticação e autorização. Por exemplo, em uma integração com Auth0, a URL para recuperar o UPN seria: https://{seuAuth0Domain}/userinfo.

       Apenas se o campo Ativo estiver marcado será possível utilizar este aplicativo externo para fazer login nos sistemas.

       A imagem anexada no cadastro do aplicativo pode ser usada como ícone ou como botão na tela principal de login. A recomendação de tamanho das imagens é de:

* Ícone: 16 x 16 (Medida em pixels)
* Botão: 75 x 24 (Medida em pixels)

       Após cadastrar o aplicativo, é possível customizar o botão que aparecerá na tela de login. Veja o tópico abaixo: Customização do Aplicativo Externo.

**Observação:** Não é permitido cadastrar mais de um aplicativo do provedor Facebook, Google ou WSO2.

# Customização do Aplicativo Externo

---

       É possível customizar algumas cores do botão do aplicativo externo, desde que possuam Provedor do tipo 'Custom' ou 'WSO2'. Para visualizar essas propriedades, basta acessar o menu **Anexos > Customização do Aplicativo Externo.**

       Podem ser customizadas a cor de fundo, do texto e da borda. Caso exista alguma imagem cadastrada no aplicativo externo, ela será usada como ícone no botão.

Ver exemplo

Configuração:

Tela de Login:

       Para que essa imagem apareça como botão, basta marcar a opção Usar imagem cadastrada como background. Com essa configuração não é possível editar as cores ou texto do botão.

Ver exemplo

Configuração:

Tela de Login:

**Observação:** Pode-se cadastrar apenas uma customização por aplicativo.

# Visualização de correspondência entre usuários

---

       É possível visualizar pelo sistema quais são os usuários do RM que possuem vínculo criado com algum aplicativo externo. Basta acessar a tela **Aplicativos Externos > Anexos > Correspondência entre usuários**. Essa funcionalidade está disponível a partir da versão 12.1.22.

       Usuários que tem permissão a tela de Aplicativos externos conseguem excluir o(s) match(es) através deste anexo. Caso a exclusão seja feita, quando o usuário que teve seu match excluído logar novamente pelo aplicativo do provider, a associação será criada automaticamente, de forma transparente. Veja no documento   as regras de Vínculo com o usuário da Linha RM.

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.22

false

**Processo:** Aplicativos Externos

falsefalse

**Status:** Em andamento

false

**Data:**

false

**Autores:**

.
