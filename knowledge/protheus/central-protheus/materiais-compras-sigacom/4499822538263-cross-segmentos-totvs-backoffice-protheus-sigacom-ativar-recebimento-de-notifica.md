---
article_id: 4499822538263
category: Materiais - Compras (SIGACOM)
content_hash: 755ec173d6eac5943315f2d32d66db0877ccf848f0f1cfc9485251aa9b044544
fetched_at: '2026-06-28T22:41:14.237460+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Ativar recebimento
  de notificação no celular do  App Meu Protheus
type: support-article
updated_at: '2022-02-25T18:38:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4499822538263-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ativar-recebimento-de-notifica%C3%A7%C3%A3o-no-celular-do-App-Meu-Protheus
---

**Dúvida**Como configurar o recebimento da notificação do aplicativo Meu Protheus no celular?  
  
**Ambiente**Protheus – Compras – A partir da versão 12.1.17

**Solução**

***No Configurador**:* Ter a rotina **Event Viewer** no módulo implantada e funcional.

***Lib**:* A lib com a funcionalidade precisa ser igual ou superior a **20180216.**

## **O cadastro do usuário deverá possuir e-mail configurado:**

## **mceclip0.png**

## **Verificar a permissão de usuário**

1. Acesse o módulo **Configurador (SIGACFG)**
2. Acesse a rotina**Usuário > Senhas > Usuários.**
3. Pesquise pelo usuário que será alterado.
4. Selecione o usuário e clique em alterar.
5. Selecione a aba **Restrições de Acesso > Aba Acessos**.
6. Habilite a permissão **174 - Acesso a inscrição nos Eventos do Event Viewer.**

**![](https://tdn.totvs.com/download/attachments/307838137/GIF%2028-09-2020%2013-17-52.gif?version=1&modificationDate=1601310008753&api=v2 "Linha Microsiga Protheus > Guia de uso - Meu Protheus > GIF 28-09-2020 13-17-52.gif")**

## **Criando o evento**

1. Acesse o módulo**Configurador (SIGACFG)**
2. Acesse a rotina **Ambiente > Cadastro > Tabelas.**
3. Pesquise pela tabela (**E3)**.
4. Clique no botão **Editar**.
5. **Inclua** o novo Evento.

![](https://tdn.totvs.com/download/attachments/307838137/GIF%2001-10-2020%2016-26-59.gif?version=2&modificationDate=1601581519000&api=v2 "Linha Microsiga Protheus > Guia de uso - Meu Protheus > GIF 01-10-2020 16-26-59.gif")

## **Inscrever no Event Viewer**

1. Acesse **Miscelânea****> Inscr. Event Viewer** em qualquer módulo.
2. Clique em **Incluir**.
3. Selecione o canal **002**.
4. Selecione categoria **001**.
5. Selecione o evento desejado, no caso da aprovação do aplicativo utilizar o evento 075 (Documentação: <https://tdn.totvs.com/pages/releaseview.action?pageId=572490417>)
6. Selecione**Sim**no campo **Json.**

**Obs:**

***A configuração do EventViewer deverá ser efetuada logando nas contas de cada usuário, que neste caso deverá estar cadastrado como aprovador para obter acesso ao aplicativo.***

Para informações sobre o **Event** **Viewer**, clique **[aqui](https://tdn.totvs.com/display/public/PROT/Acessando+o+AppLinker).**

![](https://tdn.totvs.com/download/attachments/307838137/GIF%2002-10-2020%2012-32-08.gif?version=1&modificationDate=1601652943373&api=v2 "Linha Microsiga Protheus > Guia de uso - Meu Protheus > GIF 02-10-2020 12-32-08.gif")

Configuração de seu e-mail: <https://tdn.totvs.com/display/public/LRM/Dica+de+Envio+de+E-Mail+utilizando+SMTP+-+Gmail>

Na parte de segurança de seu e-mail, por favor **Ativar** utilização do e-mail em outros aplicativos:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4498836085527/mceclip2.png)

Parâmetros no configurador: <https://tdn.totvs.com/pages/releaseview.action?pageId=271166884>  
MV\_RELSERV =  informe o nome/domínio do servidor de e-mail  
MV\_RELACNT =  informe o nome da conta (e-mail)  
MV\_RELPSW = informe a senha da conta (e-mail)  
MV\_RELAUTH = .T.    
MV\_RELAPSW = informe a senha da conta (e-mail) testa com este parâmetro em branco, e testa com ele com a senha branco)  
MV\_RELSSL = .F.    
MV\_RELTLS = .T.   
MV\_RELAUSR = informe o nome da conta (e-mail)  
MV\_RELFROM =informe o nome da conta (e-mail)

Para a notificação funcionar, é importante que preencha com o *Token*de acesso o parâmetro **MV\_MINGKEY.** O mesmo é enviado junto a sua solicitação de alias do mingle: <https://mingle.totvs.com.br/landpage/>

Passo a passo para preenchimento do parâmetro:

![](https://tdn.totvs.com/download/attachments/307838137/GIF%2029-09-2020%2018-52-36.gif?version=1&modificationDate=1601417831553&api=v2 "Linha Microsiga Protheus > Guia de uso - Meu Protheus > GIF 29-09-2020 18-52-36.gif")

**LEMBRE-SE:** A notificação será recebida quando o aplicativo estiver minimizado/fechado.

***Saiba Mais :***

[Guia de uso - Meu Protheus](https://tdn.totvs.com/display/public/PROT/Guia+de+uso+-+Meu+Protheus#tudo-sobre-funcionalidades-interfaces)

# [Cross Segmento - Totvs Backoffice Protheus - SIGACOM - Como anexar documento no pedido de compras e visualizar no aplicativo Meu Protheus ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412680424727-Cross-Segmento-Totvs-Backoffice-Protheus-SIGACOM-Como-anexar-documento-no-pedido-de-compras-e-visualizar-no-aplicativo-Meu-Protheus-?source=search)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS) 

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
