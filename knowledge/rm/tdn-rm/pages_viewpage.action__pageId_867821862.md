---
content_hash: 7e8045c4661b228a1fca164ae370bf16980ca32efc57002b3e51daa354e6e2c7
fetched_at: '2026-06-29T00:11:56.657711+00:00'
page_id: '867821862'
product: rm
source: tdn-rm
title: Modelo integração Azure via aplicativo SAML - Portal de Medição de Contratos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=867821862
version: 5
---

Iremos apresentar um modelo de como realizar a integração com Azure para autenticação no Portal de Medição de Contrato Fornecedor, para isso, siga os passos a seguir:

**Importante**: Por favor, esteja ciente de que este documento contém um modelo de integração com o Azure como exemplo. A TOTVS não oferece manutenção nem assume qualquer responsabilidade em relação ao serviço Azure. O modelo fornecido aqui é apenas para fins ilustrativos e de referência. É importante que você consulte os termos de serviço e as políticas de suporte do Azure antes de aplicar tal solução.

1 - No RM, acessar o cadastro de 'Aplicativos SAML' no módulo de Globais:

e criar um novo registro apenas com Nome do provider e URL de retorno preenchidos conforme imagem abaixo:

Url de Retorno: Deve ser preenchida com a URL de login do Portal de Medição de Contrato, tipicamente seria:

<http://localhost:8051/portal-contrato-fornecedor/login>

Substituindo localhost e 8051 pelo servidor e porta adequados respectivamente.

Por fim, o registro deve ser salvo para que o ID seja gerado, ele será usado posteriormente, nesse caso, conforme imagem logo acima o ID é 1.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

2 - Logar no portal Azure e acessar Aplicativos Empresariais:

Link para login no azure:

[https://azure.microsoft.com](https://azure.microsoft.com/)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

3 - Criar um novo aplicativo:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

4 - Selecionar a opção Crie seu próprio aplicativo:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

5 - Informe um nome que seja conveniente e acione o botão 'Criar'.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

6 - Criada a aplicação, acione a opção 'Configurar logon único' em 'Getting Started' conforme imagem abaixo:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

7 - Na pagina seguinte, é necessário selecionar o método de autenticação, escolha SAML conforme imagem abaixo:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

8 - Agora estamos na pagina principal de configuração do aplicativo recém criado, nela algumas configurações devem ser realizadas. Acione a opção 'Editar' de 'Configuração Básica de SAML ' para o próximo passo:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

8.1 - Configuração Básica de SAML:

Identificador: Identificador do aplicativo no Azure AD, ele deve ser único entre os outros aplicativos criados.

URL de resposta: No caso da integração com RM essa URL deve ser:

<http://localhost:8051/RMCloudPass/SSOSaml2?ProviderId=3>

Onde localhost deve ser substituído pelo servidor, 8051 pela porta e o 1 de ProviderId=1 deve ser substituído pelo ID do cadastro de Aplicativo SAML criado no RM no passo 1

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

8.2 - Atributos e Declarações

Nessa tela vamos configurar o que fará a integração identificar qual usuário RM estará ligado ao usuário autenticado do Azure, e para isso selecione o 'Identificador Exclusivo do Usuário (ID do Nome)':

Após clicar como indicado pela seta na imagem acima, a seguinte tela será exibida, onde o 'Atributo de origem' deve ser alterado para 'user.mail':

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

9 - Agora precisamos conceder permissão ao aplicativo criado a todos os usuários que irão acessar o Portal de Medição usando tal integração, vale lembrar que o e-mail de cada um desses usuários, deve ter um cadastro de usuário no RM com o mesmo e-mail, o que garante que ao autenticar, o usuário do Azure terá os mesmo privilégios no Portal de Medição que esse usuário RM. Para conceder tal permissão, clique em 'Adicionar um usuário ou grupo', selecione o usuário e adicione a atribuição:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

10 - Em seguida, precisamos parar o serviço de host e acrescentar a seguinte TAG no arquivo de config:

<add key="SamlProviderIdPortalMedicao" value="1" />

Onde seu valor deve ser o ID do cadastro de aplicativo SAML que criamos no passo 1, nesse caso ele será 1, em seguida iniciar novamente o serviço de host.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

11 - Então, vamos preencher o campo Metadados do cadastro do aplicativo SAML, para isso, vamos baixar o arquivo 'XML de Metadados de Federação', clicando em baixar, como mostra a imagem abaixo:

Abra o arquivo baixado em um bowser, procure pela TAG <X509Certificate></X509Certificate> e copie todo o seu conteúdo, conforme imagem abaixo:  
  
Obs: Não recomendamos o uso de editores de texto, pois dependendo de suas configurações, podem haver quebra de linha na TAG que pode influenciar no resultado

Cole o conteúdo copiado no campo Metadados do cadastro de aplicativo SAML criado no passo 1 conforme imagem abaixo e salve:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

12 - Agora, o aplicativo criado estará disponível para login externo, mas para completar nosso cadastro de aplicativo SAML no RM, precisamos da URL, e para consegui-la, deve-se acessar o seguinte link:

<https://myapplications.microsoft.com/>

Nele, seu aplicativo será exibido, e seu link de login deverá ser copiado da seguinte forma:

Finalmente, o link copiado deve ser colado no cadastro de aplicativo SAML no RM conforme demonstrado na imagem a seguir:

Agora, no próximo acesso ao Portal da Obra, a página convencional de login será substituída pela seguinte:

Ao clicar no botão 'Portal de Medição do Fornecedor', caso o usuário já esteja autenticado no Azure, o login será feito automaticamente e o Portal da Obra será aberto com o usuário do RM que tiver o mesmo e-mail autenticado no browser, caso não esteja autenticado, ao clicar no botão, ele será direcionado para pagina de login do Azure e após a autenticação ser concluída, o Portal de Medição será aberto da mesma forma.

Atenção:

Devido a cache e alguns outros fatores, no primeiro acesso ao portal, pode ser que a página de login antiga seja exibida por alguns segundos antes de mostrar a tela acima.

No exemplo, usamos o seguinte usuário do Azure:

Então ele foi autenticado com os privilégios do atendente Ana do RM de mesmo e-mail:
