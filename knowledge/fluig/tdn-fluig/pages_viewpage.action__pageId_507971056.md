---
content_hash: d781188682666082f57b6b4e0887da519b18bde35cb83cc19e88146ce06d0412
fetched_at: '2026-06-28T21:35:27.249140+00:00'
page_id: '507971056'
product: fluig
source: tdn-fluig
title: Como alterar a porta de acesso à plataforma em HTTP e HTTPS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=507971056
version: 9
---

Fique atento!

Esta página foi revisada para considerar as configurações do TOTVS Fluig **a partir** da atualização **1.6**.

4.\*ndice

# Objetivo

---

Este guia visa mostrar o procedimento para alterar a porta de acesso à plataforma em HTTP e HTTPS. Se desejar trocar o conjunto de portas padrão, acesse .

oculto

A informação dessa página foi replicada para o artigo: <https://centraldeatendimento.fluig.com/hc/pt-br/articles/360027791251>

Se fizer qualquer alteração aqui, é importante lembrar de atualizar esse artigo!

# Alterando a porta de acesso

---

Para alterar a porta de acesso da URL da plataforma, verifique os passos conforme a configuração do seu ambiente: HTTP, HTTPS ou integrado ao TOTVS Identity.

## Alterar porta com protocolo HTTP

---

Siga os passos abaixo:

0.5falsesamplesfadetrue1Passo 1

* Logar com o usuário **wcmadmin** e acessar **Painel de Controle →** **WCM** **→** **Configurações do Sistema**.

2Passo 2

* Em **Configuração do Sistema** **→ Aba Portal,** no campo **URL do Portal,** altere para a nova porta.

* Ao finalizar a alteração clique em **Salvar.**

3Passo 3

* Pare os serviços do Fluig em sua ordem correta (fluig, fluig\_Indexer e fluig\_RealTime).

4Passo 4

* **A partir da atualização 2.0**:  
  Acesse [diretório\_instalação]/appserver/standalone/configuration e edite o arquivo **standalone.xml**.

* **Para atualizações 1.6 até 1.8.2**:  
  Acesse [diretório\_instalação]/appserver/domain/configuration e edite o arquivo **domain.xml**.
5Passo 5

* No arquivo editado (standalone.xml ou domain.xml, de acordo com a atualização do Fluig que você utiliza), localize o trecho abaixo e altere para a mesma porta informada no passo 2.

xml]]>6Passo 6

* Localize o trecho abaixo. A variável deve conter o IP interno do servidor do Fluig com a porta interna. Altere para a **mesma porta** informada no **passo 2**.

xml]]>7Passo 7

* Localize o trecho abaixo e verifique se o endereço IP configurado na variável FLUIG\_URL consta na variável NETWORK\_IP\_ADDRESSES. Inclua-o se necessário.

xml]]>

* Ao finalizar **salve** o arquivo.

8Passo 8

Pronto! Agora é só iniciar os serviços do Fluig na ordem correta (fluig\_RealTime, fluig\_Indexer e fluig), e então acessá-lo pela nova porta.

## Alterar porta com protocolo HTTPS

---

Siga os passos abaixo:

Para saber mais informações sobre configuração HTTPS, acesse .

0.5falsesamples1fadetrue1Passo 1

* Logar com o usuário **wcmadmin** e acessar **Painel de Controle →** **WCM** **→** **Configurações do Sistema**.

2Passo 2

* Em **Configuração do Sistema** **→ Aba Portal,** no campo **URL do Portal,** altere para a nova URL.É importante mencionar que as portas padrões deste protocolo são a **443** e **8443** sendo que, a porta 8443 vem por *default* na instalação da plataforma. Se desejar alterar para a porta **443**, informe a URL conforme o exemplo: **https://<HOST>/portal**, sem informar a porta.

* Ao finalizar a alteração clique em **Salvar.**

3Passo 3

* Pare os serviços do Fluig em sua ordem correta (fluig, fluig\_Indexer e fluig\_RealTime).

4Passo 4

* **A partir da atualização 2.0**:  
  Acesse [diretório\_instalação]/appserver/standalone/configuration e edite o arquivo **standalone.xml**.

* **Para atualizações 1.6 até 1.8.2**:  
  Acesse [diretório\_instalação]/appserver/domain/configuration e edite o arquivo **domain.xml**.

5Passo 5

* No arquivo editado (standalone.xml ou domain.xml, de acordo com a atualização do Fluig que você utiliza), localize o trecho abaixo e altere para a porta **443**.

xml]]>

* Ao finalizar salve o arquivo.

6Passo 6

**Pronto!** **Agora é só iniciar os serviços do Fluig e acessá-lo pela nova URL**.

* Inicie os serviços do **Fluig** na ordem recomendada: **fluig\_RealTime, fluig\_Indexer e fluig**.

Identity

## Alterar porta com TOTVS Identity integrado

---

Caso seu ambiente tenha integração com o **TOTVS Identity** é necessário seguir os procedimentos abaixo:

0.5falseidentityfadetrue1Passo 1

* Acessar o contexto criado no Identity, por exemplo, https://[suaempresa].fluigidentity.com, com as credenciais do administrador.

* Acionar o menu **Aplicativos**.

* Acionar **Fluig** na lista de aplicativos. É possível localizá-lo utilizando o campo Pesquisar no canto superior esquerdo.

* Selecionar a aba **Entrar**.

* Acionar **Editar** localizado no canto superior direito.

2Passo 2

* Informar o novo endereço de acesso à plataforma no campo **Domínio**.

* Ao final da URL de acesso deve ser sempre incluído o caminho **/portal/idp.**

Exemplos:

http://meufluig.com:8080/portal/idp (Protocolo HTTP)

https://meufluig.com:8443/portal/idp (Protocolo HTTPS com a porta *default*)

https://meufluig.com/portal/idp (Protocolo HTTPS com a porta for 443)

* Acionar **Salvar** no final da página.

Clique no link e acesse a documentação completa referente a .

3Passo 3

A partir de agora, a configuração será realizada na plataforma.

* Acessar a plataforma com o usuário '**wcmadmin**'.

* Acessar o **Painel de Controle** → **WCM** → **Empresas**.

* Assinalar a empresa desejada e acionar **Editar**.

4Passo 4

* Acessar a aba **Autenticação**.

* Para garantir que os dados informados serão atualizados no Identity, acionar **Ações**→ **Testar conexão**.

* Se a mensagem "Conexão com o servidor do Identity realizada com sucesso" for apresentada, a configuração está correta e pode ser concluída.

* Acionar **Salvar**.

$("b:contains('oculto')").parent().parent().hide();
]]>
