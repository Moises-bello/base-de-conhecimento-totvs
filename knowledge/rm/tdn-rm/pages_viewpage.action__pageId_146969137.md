---
content_hash: 84cdfc81ac34d6e309b6ae9de4f0f958e08e4aa4d64f917a13c71646f0909427
fetched_at: '2026-06-29T00:05:55.900592+00:00'
page_id: '146969137'
product: rm
source: tdn-rm
title: Configuração IdentityProvider - Manual
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=146969137
version: 3
---

# **Configurando IdentityProvider**

Para conexão do RM com o Fluig Identity, torna-se necessário, configurar o IdentityProvider. Para esta configuração, necessitamos do arquivo **IdentityProvider**.

Este arquivo é obtido diretamente no Fluig Identity. Nas configurações do aplicativo clique sobre a opção "**Baixar Metadados do IDP**". Será gerado um arquivo em XML.

 

Acesse o sistema RM e em qualquer segmento acesse as guias/menus "**Ambiente | Parâmetros | Parâmetros | Globais**". Na guia "**Integração Fluig**". Clique sobre as reticências da configuração "**Identity Provider | Metadata Identity Provider – RM.exe , Portal :**"

Faça upload dos arquivos XML referentes ao produto (RM.exe ou Portal).

Escolha o tipo de integração e salve as configurações.

Erros Associados

**"Erro: Certificado do IdentityProvider inválido! Configure o IdentityProvider no RM para estabelecer a comunicação entre eles. Esta configuração é realizada em parâmetros globais."**

**Solução:**

√  Acesse o sistema RM com um usuário com status de supervisor. Selecione “**Ambiente | Parâmetros | Parâmetros | Globais**”. Na guia “**Integração Fluig**” associe o arquivo XML as configurações de Identity Provider.

---

**"Erro: Integração SAML está inativa! Configure o “Tipo de Integração” no RM. Esta configuração é realizada em parâmetros globais."**

**Solução:**

√  Acesse o sistema RM com um usuário com status de supervisor. Selecione “**Ambiente | Parâmetros | Parâmetros | Globais**”. Na guia "**Integração Fluig**” escolha em “**Tipo de Integração**” a ser utilizado.

 

---

**“Erro: Alias do banco de dados não encontrado!”**

**Solução:**

√  Acesse o diretório “**C:\totvs\CorporeRM\RM.Net**”, da máquina/servidor onde está executando o serviço de host. Edite o arquivo “**RM.Host.Service.exe.config**” e inclua a tag “**<add key="DefaultDB" value="CorporeRM" />**”. O valor desta tag deverá ser o mesmo nome atribuído ao seu alias. No nosso exemplo: **CorporeRM**. 

**Obs.: Para que esta alteração tenha resultado, torna-se necessário reiniciar o serviço do RM Host. Sendo assim, pedimos que esta ação seja programada para realização.**

---

**“Erro: Existe mais de um usuário associado ao mesmo e-mail, e não será possível efetuar o login integrado.”**

**Solução:**

√  Acesse o RM utilizando um usuário com status de supervisor. Selecione o segmento “**Serviços Globais**”. Clique sobre a guia “**Segurança | Acesso | Usuários**”. Pesquise entre os usuários cadastrados, usuários que contenham o **mesmo e-mail utilizado no login Fluig.** Corrija o cadastro dos usuários com seus reais e-mails.

---

**“Erro: Não existe usuário associado ao e-mail, e não será possível efetuar o login integrado.”**

**Solução:**

√  Acesse o RM utilizando um usuário com status de supervisor. Selecione o segmento “**Serviços Globais**”. Clique sobre a guia “**Segurança | Acesso | Usuários**”. Selecione o usuário que será associado ao Fluig. Edite o usuário e no campo **e-mail** informe o e-mail no login do Fluig.

---

---
