---
content_hash: a7f01750bdfb2e6bd582abae10a816d85331eea9d172ac32c1482fed3407a878
fetched_at: '2026-06-28T21:35:19.499543+00:00'
page_id: '208347280'
product: fluig
source: tdn-fluig
title: MOB - Como configurar logo da empresa no My Fluig?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=208347280
version: 9
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**My Fluig

# Dúvida

Como configurar uma imagem de logo da empresa para que seja exibida no aplicativo My Fluig?

# Causa

A imagem atribuída à tela de autenticação, tanto no mobile quanto no navegador, não é a que está configurada no tema.

# Solução

**01.** Autenticar com o usuário *wcmadmin*, e acessar **Painel de Controle** > **WCM** > **Configurações do Sistema** > **Personalização.**

**02.** No ECM, publicar na pasta desejada a imagem de logo. Ir nas propriedades da imagem adicionada e acionar a aba **Segurança** e logo depois acionar a opção **Compartilhar externamente?**Dessa forma a imagem ficará disponível para que seja anexada para ser exibida na autenticação do My Fluig.

**03.** Após isso, vá até a pasta onde a imagem foi publicada e copie o link externo da imagem. Como no exemplo abaixo:

**04.** Agora para cadastrar a imagem para ser exibida no My Fluig acesse a plataforma com o usuário wcmadmin e vá até **Painel de Controle** > **WCM** > **Configurações do Sistema** > **Personalização.**Preencher os campos "URL da imagem de logo (página de login)" e "URL da imagem de logo (página de login mobile)". E acionar **Salvar**.

Após feito esse procedimento a imagem de logo da empresa será exibida no aplicativo My Fluig no momento da autenticação. Além do procedimento que mostramos neste material também é possível incluir qualquer imagem que esteja disponível na web, ou seja, seja uma imagem já publicada para que se possa obter o caminho da mesma e colar nos respectivos campos.
