---
content_hash: 099ffbef697563c7f55d614932686f74dfa5bf0dafecf9ff7c5d47419b3297a9
fetched_at: '2026-06-29T00:12:02.626045+00:00'
page_id: '901964447'
product: rm
source: tdn-rm
title: 1- Configuração do login unificado dos portais.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=901964447
version: 16
---

O login unificado dos portais, fazem o uso de API para buscar e armazenar informações, o controle destas APIs é feito pelo host. Para que os portal funcione corretamente, é necessário expor as APIs para web, desta maneira, é necessário o uso do módulo URL Rewrite do IIS para que este módulo filtre as solicitações e encaminhe para o host as solicitações que sejam para a API.

1- Configuração do ARR e URL Rewrite

A configuração do portal, segue a regra de configuração dos demais portais,  onde é necessário instalar o **URL Rewrite** e **ARR (Application Request Routing)** no IIS.

ARR (Application Request Routing)

A instalação deve ser realizada no servidor do portal desejado.

**Link para download do ARR**:  <https://www.microsoft.com/en-us/download/details.aspx?id=47333> 

Apenas uma vez para cada IIS

**A instalação deve ser realizada apenas uma vez para cada IIS.**

Habilitar o proxy

Após finalizar a instalação **ARR (Application Request Routing),** deverá ser **habilitado** a propriedade **"Enable proxy"**

URL Rewrite

A instalação deve ser realizada no servidor do portal desejado.

**Link para download do URL Rewrite**: <https://www.iis.net/downloads/microsoft/url-rewrite>

Após a Instalação, será criado um ícone: “URL *Rewrite*” no IIS.

**1-** Após a instalação da regra do *Rewrite*, clicar em: 'Abrir recursos'

**2-** Será listado duas regras, sendo: 

     1º regra, acesso à *api* do portal;

     2º regra, acesso à *api* de integração com o SAML\* 

> \* ver mais informação configuração aqui.

2- Configurar aquivo de config do Host do RM

Após configurar o servidor conforme o item: Configuração, é necessário configurar o arquivo de configuração do Host do RM. Para isso, acesse o arquivo **RM.Host.Service.exe.config** que está disponível no caminho padrão do instalador do RM.exe.

Inserir as chaves as chaves abaixo:

      <add key="ApiPort" value=**"porta\_definida\_no\_rewrite (IIS)"** />  
      <add key="DefaultDB" value=**"informe\_aqui\_o\_nome\_do\_alias"** />

3- Configurar protocolo SAML

A Linguagem de Marcação para Asserção de Segurança (SAML) é um padrão amplamente utilizado para garantir que aplicativos e serviços externos possam verificar a identidade de um usuário de maneira confiável, assegurando que ele realmente seja quem afirma ser. Por meio desse protocolo, é possível implementar a tecnologia de login único (SSO), que permite que o usuário se autentique uma única vez e, a partir dessa autenticação, tenha acesso a diversos aplicativos e sistemas sem precisar se reautenticar em cada um deles. Isso simplifica a experiência do usuário, melhora a segurança e reduz a sobrecarga administrativa relacionada ao gerenciamento de senhas. Para realizar a configuração, é necessário realizar algumas configurações, sendo:

Configuração SAML - Portal Azure

Para realizar a configuração de integração com SAML. **Saiba mais em**

Cadastro do "Aplicativo Externo" - RM.exe

Para realizar a configuração do **"Aplicativos SAML"** em "**Gestão Educacional | Educacional | Gestão | Comunicação | Aplicativos SAML"**

* Nome do provider: nome para identificar o provider, esse nome que será exibido no botão que será utilizado para logar pelo portal
* URL de retorno: url utilizada para redirecionar o usuário após a autenticação no provider, essa url deve ser preenchida com o seguinte valor: **[url\_do\_portal]**[/FrameHTML/web/app/edu/loginportais/#/loginsso](http://localhost/FrameHTML/web/app/edu/loginportais/#/loginsso), onde o valor **[url\_do\_portal]** deve ser substituído pela url do portal.
* URL de login do provider; url utilizada para realizar a autenticação do usuário no provider, essa url é fornecida pelo provider. No portal azure a mesma se encontra dentro da configuração do aplicativo em propriedades no campo **URL de acesso do usuário**

* Metadados: campo que contém algumas informações de segurança do provider como por exemplo uma chave de segurança para autenticar, o metadado é fornecido pelo provider. Para recuperar essa informação no portal azure deve ir em Logon único, Certificados SAML (passo 3) e clicar no baixar xml de metados de federação. Após baixar, abrir o xml baixado e ir no campo X509Certificate e copiar o seu conteúdo

* Url de logout do provider: url utilizada para realizar o logout no provider ao clicar no sair dos portais, caso essa url não seja preenchida, ao clicar no sair nos portais o usuário **continuará logado no provider** apesar de deslogar nos portais. Essa url é fornecida pelo provider. Para o provider azure preencher com o seguinte valor: [https://login.microsoftonline.com/**[tenantID]**/oauth2/v2.0/logout](https://login.microsoftonline.com/[tenantID]/oauth2/v2.0/logout), onde o valor [tenantID] deve ser substituido pelo id do tenant que foi gerado no provider.  No portal azure a mesma se encontra dentro da configuração do aplicativo em propriedades no campo **ID do Aplicativo**

Após realizar a configuração acima, ao acessar o login unificado dos portais, será apresentado o botão **"Acessar com o Provider Azure"**

ATENÇÃO

Para os exemplos de configuração citados acima foi utilizado o portal azure como provider, mas qualquer outro provedor pode ser utilizado como google, amazon entre outros. Para cada um deles o local aonde as informações necessárias citadas acima para configurar o protocolo SAML se encontraram em locais diferentes.

Vínculo do usuário

Acessar o cadastro do usuário, seja: aluno, professor, responsável (financeiro/acadêmico) e/ou agente de atendimento,  e informar o email parametrizado no Azure Microsoft.

Atenção

Para que o processo funcione corretamente só pode existir **um** usuário com o e-mail vinculado ao mesmo, caso exista mais de um usuário com o mesmo e-mail, o processo não irá funcionar.
