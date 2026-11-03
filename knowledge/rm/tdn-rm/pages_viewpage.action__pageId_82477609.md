---
content_hash: 7f7d116aa17892d42ef5b5ac3aecc01ca15eb7e6b4e498c401b7e286757b2575
fetched_at: '2026-06-29T00:11:48.507179+00:00'
page_id: '82477609'
product: rm
source: tdn-rm
title: Como expor os Web Services do RM através do IIS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=82477609
version: 22
---

AVISO SOBRE TÉRMINO DO SUPORTE

A partir da versão 12.1.2302, o RM não dará mais suporte às integrações que utilizam o TBC (TOTVS Business Connect) via IIS, conforme instruções descritas neste documento.

**O QUE DEVE SER FEITO**  
As integrações existentes deverão ser substituídas pelo TBC via Host.

Mais informações aqui,  ou 

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Conector                       **Versão:***12.0* |
| **Processo** | **:** | Instalação do TBC no IIS |
| **Subprocesso** | **:** |  |
| **Data da publicação** | **:** | 13/01/2015 |

O TOTVS Business Connect (TBC) deve ser instalado para as integrações padrões da TOTVS. As integrações disponíveis atualmente são:

* TOTVS Obras e Projetos x BackOffice Protheus;
* TOTVS Incorporação x BackOffice Protheus;
* SigaLoja x FrontLoja x BackOfficeRM;
* TOTVS Educacional x BackOffice Protheus;
* Protheus SigaMNT x Linha RM;
* TOTVS Educacional x EAD (WebEnsino e AMS).

Para instalar o TBC para o IIS são necessários alguns pré-requisitos, que são:

## **1. Pré-requisitos:**

**Possuir o Internet Information Service (IIS) instalado e devidamente configurado. Alguns sub-componentes do IIS que serão descritos abaixo devem estar configurados/instalados, que são:**

**Windows XP ou superiores: (Acesse PAINEL DE CONTROLE > ADICIONAR OU REMOVER PROGRAMAS (PROGRAMAS E RECURSOS) > ATIVAR OU DESATIVAR RECURSOS DO WINDOWS)**

**Windows Server: (Acessar GERENCIADOR DE SERVIDORES (SERVER MANAGER) > ADICIONAR FUNÇÃO > SERVIDOR DE WEB (WEB SERVER) ):**

 

**As restrições CGI e ISAPI devem estar liberadas para o Asp Net 4.0, conforme prints abaixo:**

## **2. Instalação – WS do TBC**

O pacote de instalação "TOTVS Business Connect – [versão].msi" instala os WebServices do TBC e hospeda estes no IIS. A sua instalação é muito simples e intuitiva, através de um assistente. Veja passo a passo:

**Poderá ser apresentado o seguinte aviso, caso o Sistema Operacional do Computador não seja o recomendado:**

Passo 1 – Ler aviso e clicar em Avançar

Passo 2 – Ler o contrato e se estiver de acordo clicar em Avançar

Passo 3 - Confirmar a instalação, clicando em Instalar

Passo 4 – Instalação concluída  
A instalação padrão incluirá um aplicativo no IIS:

   
Verifique nas configurações básicas do aplicativo se o "Caminho Físico" está apontando para o caminho onde o TBC foi instalado, e qual o Pool de Aplicativos está selecionado:

   
Nas configurações dos Pools, verifique se o Pool de Aplicativos utilizado está como:  
Status = Iniciado  
Versão FrameWork = v4.0  
Modo de Pipeline = Clássico  
Identidade = "ApplicationPoolIdentity"   
   
   
  
   
Caso não esteja, altere em Configurações avançadas.  
  
  
   
   
**No arquivo Web.config existente no <diretório de instalação>\WS\_TBC deve ser alterada as seguintes** **tags:**

Web.config : Informar o hostname ou ip da máquina que contém o serviço do Host do RM;
 : Informar a porta em que o serviço do Host do RM está sendo executado;
 : Informar o Alias, do arquivo Alias.dat, que contém a informação de qual base será utilizada na integração;
 
Alterar a linha abaixo (Para as integrações "SigaLoja x FrontLoja x BackOfficeRM" e "Protheus SigaMNT x Linha RM" Manter como " ")
De:
        
Para:
      
        
]]>

**Observação:**   
**Nos arquivos "<diretório de instalação do RM>\WS\_TBC\Web.Config"  e ""<diretório de instalação do RM>\RM.Net\RM.Host.Service.exe.config", verificar se as linhas relacionadas à informação abaixo, estão idênticas para ambos os arquivos;**

Web.config
]]>

Os WS serão instalados na porta 80 (como é a porta padrão pode ser omitida na url). Mas o administrador do sistema poderá alterar esta e demais configurações, se desejado, editando o arquivo Web.config que se encontra no diretório de instalação RM na pasta WS\_TBC: (verificar as configuração JOSERVER3CAMADAS, DABALIAS, HOST e PORTA de acordo com as configurações do RM.Host.Service.exe.config ou RM.Host.exe.config).

**A partir deste ponto os WebServices do TBC já podem ser acessados, por exemplo através do navegador Internet Explorer:**

## 3. Autenticação

Informações importantes sobre o comportamento do mecanismo de autenticação de usuários quando o TBC é instalado no IIS.

Para o WebMethod: **AutenticaAcesso**

Autentica o acesso do usuário no ambiente RM. O usuário e senha terá que ser passado via SOAP, criando um token para isto.

Especificamente quando o TBC estiver no IIS, o mecanismo de autenticação utilizará o protocolo de autenticação WSS, [mais informações](https://learn.microsoft.com/pt-br/dotnet/framework/wcf/feature-details/security-protocols).

Significa que na requisição do serviço, o usuário e senha devem ser informados no modelo do protocolo WSS, que é diferente do Basic Authentication. (Que é o utilizado quando o TBS é acessado direto do RM.Host)

O usuário e senha devem ser informado no Header da requisição Soap, conforme o exemplo abaixo:

Usuário em texto limpo e a senha em base64:

Soap Request Example

<soap:Envelope xmlns:soap="<http://www.w3.org/2003/05/soap-envelope>" xmlns:br="<http://www.totvs.com.br/br/>">  
   <soap:Header>  
     <wsse:Security soap:mustUnderstand="1" xmlns:soap="<http://schemas.xmlsoap.org/wsdl/soap/>" xmlns:wsse="<http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd>">  
         <wsse:UsernameToken>  
**<wsse:Username>User</wsse:Username>**  
**<wsse:Password>cGFzc3dvcmQ=</wsse:Password>**  
         </wsse:UsernameToken>  
       </wsse:Security>  
     </soap:Header>  
   <soap:Body>  
      <br:AutenticaAcesso/>  
   </soap:Body>  
</soap:Envelope>

## 4. Cache do IIS

Muito importante compreender que o IIS possui seu próprio gerenciamento de Cache e que ele pode interferir nas requisições, respondendo resultados armazenados em seu cache, sem antes requisitar o RM.Host.

Deve ser analisado com um técnico as configurações mais adequadas do IIS, de forma que não afete de forma negativa os serviços TBC.

   
Para maiores informações:  
Icon   
Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/CON3/INT.webservices.aspx)  
   
[  |https://www.byyou.com/static/resources/hotsite/index.html]**COMUNIDADE** [**@TBC e Microsoft Dynamics CRM**](https://totvs.byyou.com/?space=rintegraoecrm)  
 **Canais** **de** **Atendimento:**  
**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  
**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 2 – (CRM), 3 - (Vendas e CRM) e 3 –  (Microsoft CRM).
