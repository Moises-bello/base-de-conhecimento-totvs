---
content_hash: 99e469fc4da472e6d3d5ca58d63ae2c516ee890340eaa731ff8e91f5319054b4
fetched_at: '2026-06-29T00:08:53.421881+00:00'
page_id: '344475592'
product: rm
source: tdn-rm
title: Integração do RM com ADFS via SAML
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=344475592
version: 89
---

# Índice

---

      .\*ndice:

# Objetivo

---

       Este documento demonstra como integrar o sistema RM com o AD FS como provedor de Identidade.

# Introdução

---

       O ADFS (Active Diretory Federation Services) permite o compartilhamento da informação de identidade em um ampla variedade de aplicativos utilizando o padrão SAML que é suportado na linha RM.

# Configurando o Aplicativo Confiável no ADFS

---

        Abaixo são demonstrados os passos para a criação da entidade confiável para a Linha RM dentro do ADFS.

falseConfigurando o Aplicativo Confiável no ADFS1º Passo:

Ao acessar a configuração do AD FS, selecione "Add Relying Party Trust" para acesso ao assistente de configuração.

2º Passo:

Selecione a opção "Enter data about the relying party manually" para inserir os dados sobre a Linha RM.

Acione o botão "Next".

3º Passo:

Informe um nome para identificar o aplicativo.

4º Passo:

Selecione a opção: "AD FS profile".

5º Passo:

Neste ponto, acione "Next".

6º Passo:

Neste passo, deve-se informar a URL do serviço responsável por processar o SingleSignOn do RM:  
https://<Endereço do Host>/RMCloudPass/SSOSaml2

O AD FS exige que este serviço esteja exposto via SSL. Mais detalhes sobre como configurar o RM Host para expor serviços via SSL em: 

7º Passo:

Selecione a opção: "I do not want to configure multifactor".

8º Passo:

Escolha a opção "Permit all users to access thie relying party".

9º Passo:

Neste ponto, acione "Next".

10º Passo:

Selecione a caixa de seleção para abrir a edição de regras.

# Configurando as Regras de Declaração (RM Portal)

---

falseConfigurando o Aplicativo Confiável no ADFS1º Passo:

Selecione a opção: "Add rule".

2º Passo:

Selecione a opção: "Send LDAP Attributes as Claims".

3º Passo:

Defina um nome para a regra e selecione o mapeamento conforme a imagem abaixo. O mapeamento para o SSO no RM é feito pelo e-mail do usuário.

4º Passo:

Selecione a opção: "Add rule".

5º Passo:

Selecione a opção: "Tranform an Incoming Claim".

6º Passo:

Defina um nome para a regra e selecione os parâmetros conforme a imagem abaixo.

7º Passo:

Para o Portal CorporeRM não é necessário configurar o RelaySate.

Mas, para usar o portal FrameHTML, é necessário configurá-lo, de acordo com a regra abaixo, no seguinte formato:

state|loginPage|returnUrl  
Ex: webapi|[http://localhost:8090/RM/Login/Login.aspx|/web/app/RH/PortalMeuRH/](https://www.google.com/url?q=http://localhost:8090/RM/Login/Login.aspx%7C/web/app/RH/PortalMeuRH/&sa=D&source=hangouts&ust=1598637436249000&usg=AFQjCNEsl44H-Kb_J3WqcRqCAVOufdaIoQ)

**obs1:** state para FrameHTML deve ser exclusivamente webapi.  
**obs2:** até a versão 12.1.29 continua necessário mandar o ExecutablePath na requisição Saml.

# Configurando as Regras de Declaração (MDI - RM.exe)

---

falseConfigurando o Aplicativo Confiável no ADFS1º Passo:

Selecione a opção: "Add rule".

2º Passo:

Selecione a opção: "Send LDAP Attributes as Claims".

3º Passo:

Defina um nome para a regra e selecione o mapeamento conforme a imagem abaixo. O mapeamento para o SSO no RM é feito pelo e-mail do usuário.

4º Passo:

Selecione a opção: "Add rule".

5º Passo:

Selecione a opção: "Tranform an Incoming Claim".

6º Passo:

Defina um nome para a regra e selecione os parâmetros conforme a imagem abaixo.

7º Passo:

Selecione a opção: "Add rule".

8º Passo:

Selecione a opção "Send Claims Using a Custom Rule".

9º Passo:

Defina um nome para a regra e escreva a regra de declaração customizada conforme a imagem abaixo:

c#RelayStatetrue issue(Type = "RelayState", Value = "samlexecutable");]]>10º Passo:

Selecione a opção: "Add rule".

11º Passo:

Selecione a opção "Send Claims Using a Custom Rule".

12º Passo:

Defina um nome para a regra e escreva a regra de declaração customizada conforme a imagem abaixo:

c#RelayStatetrue issue(Type = "ExecutablePath", Value = "C:\totvs\CorporeRM\RM.Net\RM.exe");]]>

# Integração SAML no RM

---

* **Metadado do ADFS**

          Abaixo temos um exemplo do metadados SAML que deve ser importado no RM:

xml1Metadatatrue














]]>

 Repare que as URI's devem estar configuradas de acordo com seu ambiente.

Atenção

* O atributo **entityID** do elemento **EntityDescriptor** deve estar definido com a URL do Portal Corpore.NET.
* A tag **X509Certificate** deve ser preenchida com o certificado em base64 proveninente do arquivo de metadata, disponível em ****https://<Servidor AD FS>/FederationMetadata/2007-06/FederationMetadata.xml****
* Nas URI's de **SingleSignOnService**, o parâmetros **LoginToRp** deve receber o nome da *Relying Party* configurado no Passo 3 do Item "Configurando o aplicativo confiável no AD FS".

* **Importando o metadado do AD FS no RM**

          Após obter o metadados personalizado, ele deve ser importado no RM em: Ambiente → Parâmetros → Parâmetros Globais → Integração SAML

          Caso queira integrar o ADFS com a MDI, via SAML, adicionar o metadado no campo "Metadata Identity Provider - RM.exe"

Caso queira integrar o ADFS com o Portal, via SAML, adicionar o metadado no campo "Metadata Identity Provider - Portal".

Observação

Existe a possibilidade de integrar o ADFS com a MDI e o Portal de forma simultânea, basta adicionar o metadado nos campos "Metadata Identity Provider - RM.exe" e "Metadata Identity Provider - Portal".

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.18 e superiores

false

**Processo:** Integração SAML

falsefalse

**Status:** Finalizado

false

**Data:**
