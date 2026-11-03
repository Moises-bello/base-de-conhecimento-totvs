---
content_hash: c096538e85ce05395850b2083e47205b21bbf52ee06f20a1b6351f53d0cdac55
fetched_at: '2026-06-29T00:09:47.959667+00:00'
page_id: '435105110'
product: rm
source: tdn-rm
title: Portal do Cliente - PDC - Login - (Incorporadora)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105110
version: 8
---

**Login**

---

**Descrição**  
   
Esta funcionalidade possibilita a Incorporadora realizar a autenticação de usuário do portal. Essa autenticação poderá ser feita pela página nativa do portal ou por uma página personalizada da Incorporadora.

---

O portal tem a possibilidade da Incorporadora escolher duas formas distintas de Login dos compradores: Login TOTVS (Padrão) ou Login Externo (Customizado).

* **Login TOTVS**

O Login padrão da Totvs é uma forma padronizada de Login, e para funcionar corretamente é necessário configurar o parâmetro Global (na aba ambiente-> parâmetros) da nova MDI, e incluindo a url base na aba FrameHTML.    
Após a configuração dos parâmetros globais o comprador terá a possibilidade de acessar o Portal através da url: http:// servidor-domínio/web/app/Imb/PortalCliente/#/.  Ao acessar está url o comprador irá visualizar a página de login como demonstrado na imagem abaixo:

Importante!

A partir da versão 12.1.27, atendendo a nova legislação de uso de dados, o sistema passará a exibir os Termos de Aceite para a utilização do Portal do Cliente, quando o cliente fizer seu primeiro login no portal.  
O login só será possível se o usuário marcar a opção: "Confirmo que li e concordo com os termos e condições de uso" e após isso clicar em aceitar.

O Termo de Aceite, para que seja apresentado, deverá ser parametrizado primeiramente nos parâmetros do TOTVS Incorporação localizado em: **Portal do Cliente > Termo de Aceite > Relatório para exibição do Termo de Aceite.**O relatório poderá ser qualquer relatório definido pelo cliente, que atenda os requisitos da **LGPD**.

O sistema também possuirá um campo para versionamento do Termo de Aceite, localizado em **Portal do Cliente > Termo de Aceite > Versão**. A versão do termo deverá ser sempre incremental, preenchida por um número inteiro e não será possível incluir uma versão anterior a já cadastrada.

Quando se altera o relatório e/ou a versão do termo, o sistema obrigará a exibição do mesmo para o cliente ao realizar o login e só permitirá este login após uma nova confirmação de leitura dos termos.

Para cada confirmação do usuário o sistema gravará na tabela **XAUTORIZACAOLPD** toda a informação do relatório, bem como versionamento, usuário e outros dados.

* **Login Externo (Customizado)**

O portal possui uma segunda forma de autenticação para o comprador,  que pode ser customizada pela Incorporadora. O acesso dos compradores pelo login externo deverá ser feito pela página criada pela Incorporadora, imobiliária ou outros, utilizando um serviço REST da TOTVS que autentica o comprador no servidor RM. veja abaixo um exemplo de como criar e configurar o ambiente e chamando o serviço RM.   
**1º Passo:** É necessário parametrizar a url base do FrameHTML:  Acesse nova MDI, na aba Ambiente  selecione parâmetro global e configure a url base , na aba FrameHTML.  
   
**2º Passo:** Através de um HTML criado pela Incorporadora que precisar ter os campos de usuário e senha do comprador.  
   
**3º Passo:** Configurar a chamada ao serviço TOTVS para realização do login.  
   
**4º Passo:** Se o Portal e o site externo estiverem em domínio diferentes existe a segurança de CORS que impedirá o acesso ao serviço. Assim torna-se necessário alterar o Arquivo de Configuração (web.config) do portal, permitindo o acesso externo de determinado domínio.

Esta tela também apresenta uma funcionalidade para .

Importante!

A duração padrão do **token de acesso** é de 5 minutos e pode ser alterado através da tag **JWTTokenExpireMinutes**, que pode ser inserida nos arquivos RM.Host.exe.config e RM.Host.Service.exe.config.

A duração deste token pode ser configurada entre 1 e 43200 minutos (30 dias).

Já o **refresh token** tem a duração padrão de 16 horas e este tempo de expiração pode ser alterado através da tag **JWTRefreshTokenExpireMinutes.** Este tempo pode ser configurado entre 1 e 129600 minutos (90 dias).

Reforçamos que os valores abaixo estão em minutos:

*<add key="JWTTokenExpireMinutes" value="9999" />*  
*<add key="JWTRefreshTokenExpireMinutes" value="9999" />*

Após realizar os ajustes nos arquivos *config*, reinicie os serviços de Host e valide o tempo configurado:

---

Criação de Usuários
