---
content_hash: c30500f5513a485e5ed27d1a74d241cb5f5b33c9a43134a7c7cf404a55011d58
fetched_at: '2026-06-29T00:05:55.908102+00:00'
page_id: '146969238'
product: rm
source: tdn-rm
title: Identity - Linha RM
type: documentation
url: https://tdn.totvs.com/display/LRM/Identity+-+Linha+RM
version: 10
---

# Objetivo

O objetivo deste documento é especificar como configurar o fluig Identity para linha RM.

# Requisitos mínimos

Para utilizar Integração SAML certifique-se que:

1. A versão do RM é igual ou superior a 11.82.34.0.
2. Disponibilidade da porta 8051. Maiores informações: [Configurando HTTPPort](http://tdn.totvs.com/x/phKqC)

# Configurando IdentityProvide

Importante

Se tiver dúvidas sobre essa documentação, entre em contato com a equipe de suporte da linha RM.

Para conexão do RM com o fluig Identity, torna-se necessário, configurar o IdentityProvider. Para esta configuração, necessitamos do arquivo **IdentityProvider**.

Este arquivo é obtido diretamente no fluig Identity. Nas configurações do aplicativo clique sobre a opção "**Baixar Metadados do IDP**". Será gerado um arquivo em XML.

Acesse o sistema RM e em qualquer segmento acesse as guias/menus "**Ambiente | Parâmetros | Parâmetros | Globais**". Na guia "**Integração fluig**". Clique sobre as reticências da configuração "**Identity Provider | Metadata Identity Provider – RM.exe , Portal :**"

Faça upload dos arquivos XML referentes ao produto (RM.exe e Portal).

Escolha o tipo de integração e salve as configurações.

# Assista ao vídeo: Como ativar a integração SAML

Erros Associados

**"Erro: Certificado do IdentityProvider inválido! Configure o IdentityProvider no RM para estabelecer a comunicação entre eles. Esta configuração é realizada em parâmetros globais."**

**Solução:**

√  Acesse o sistema RM com um usuário com status de supervisor. Selecione “**Ambiente | Parâmetros | Parâmetros | Globais**”. Na guia “**Integração fluig**” associe o arquivo XML as configurações de Identity Provider.

---

**"Erro: Integração SAML está inativa! Configure o “Tipo de Integração” no RM. Esta configuração é realizada em parâmetros globais."**

**Solução:**

√  Acesse o sistema RM com um usuário com status de supervisor. Selecione “**Ambiente | Parâmetros | Parâmetros | Globais**”. Na guia "**Integração fluig**” escolha em “**Tipo de Integração**” a ser utilizado.

 

---

**“Erro: Alias do banco de dados não encontrado!”**

**Solução:**

√  Acesse o diretório “**C:\totvs\CorporeRM\RM.Net**”, da máquina/servidor onde está executando o serviço de host. Edite o arquivo “**RM.Host.Service.exe.config**” e inclua a tag “**<add key="DefaultDB" value="CorporeRM" />**”. O valor desta tag deverá ser o mesmo nome atribuído ao seu alias. No nosso exemplo: **CorporeRM**. 

**Obs.: Para que esta alteração tenha resultado, torna-se necessário reiniciar o serviço do RM Host. Sendo assim, pedimos que esta ação seja programada para realização.**

---

**“Erro: Existe mais de um usuário associado ao mesmo e-mail, e não será possível efetuar o login integrado.”**

**Solução:**

√  Acesse o RM utilizando um usuário com status de supervisor. Selecione o segmento “**Serviços Globais**”. Clique sobre a guia “**Segurança | Acesso | Usuários**”. Pesquise entre os usuários cadastrados, usuários que contenham o **mesmo e-mail utilizado no login fluig.** Corrija o cadastro dos usuários com seus reais e-mails.

---

**“Erro: Não existe usuário associado ao e-mail, e não será possível efetuar o login integrado.”**

**Solução:**

√  Acesse o RM utilizando um usuário com status de supervisor. Selecione o segmento “**Serviços Globais**”. Clique sobre a guia “**Segurança | Acesso | Usuários**”. Selecione o usuário que será associado ao fluig. Edite o usuário e no campo **e-mail** informe o e-mail no login do fluig.

---

---
