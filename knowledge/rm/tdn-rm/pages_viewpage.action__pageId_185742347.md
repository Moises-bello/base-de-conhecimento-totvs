---
content_hash: 603127ac27b42af6a8a4a803c1c9a220bd709d2cfde4be4281bbac7b68ba1e7b
fetched_at: '2026-06-29T00:05:58.183666+00:00'
page_id: '185742347'
product: rm
source: tdn-rm
title: Contas de Comunicação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=185742347
version: 20
---

# Pré-requisitos

---

2
complete
Linha RM atualizada até a versão 12.1.5

# Objetivos

---

Fornecer à área de segmentos uma API para publicação de conteúdo nas redes sociais.

# Redes Sociais

---

As redes sociais utilizadas são: Facebook, Twitter e LinkedIn.

Cada uma delas permite diferentes tipos de publicação de conteúdo:

* FACEBOOK
  + Enviar mensagens no mural do usuário.
  + Enviar mensagens no mural de uma página que o usuário gerencia.

    Atenção

    De acordo com a [documentação do Facebook](https://developers.facebook.com/docs/graph-api/changelog/breaking-changes), a permissão de compartilhamento com contas individuais (publish\_actions) foi descontinuada a partir do dia 01/08/2018.

    "A permissão publish\_actions foi removida. Os aplicativos que foram aprovados para publish\_actions podem continuar usando a permissão até 1º de agosto de 2018."

    **Vamos analisar junto ao Facebook se existe um outro meio de realizar as publicações, o que poderá acarretar em uma reestruturação em nossa integração.**
* TWITTER
  + Enviar mensagens no mural do usuário.
  + Enviar mensagens privadas à pessoas que estão na rede de contatos do usuário.
* LINKEDIN
  + Enviar mensagens no mural do usuário.
  + Enviar mensagens privadas à pessoas que estão na rede de contatos do usuário.
  + Mencionar pessoas em mensagens no mural do usuário.

# Configurando o ambiente para utilização da API

---

Para que seja possível a comunicação do RM com as redes sociais algumas configurações e cadastros devem sem feitos:

1. Criar aplicativos nas Redes Sociais
2. Cadastrar chaves de acesso em Parâmetros Globais
3. Cadastrar as Contas de Comunicação e as credenciais do usuário para acesso.

## Adicionando chaves de acesso nos Parâmetros Globais:

Em Parâmetros Globais, aba Redes Sociais é preciso informar as chaves de acesso para a conexão com o aplicativo de cada rede social. Basta preencher os campos com os valores de cada provedor.

## Configurando Proxy: (Caso a rede possua restrições de acesso à internet):

## Fontes de Comunicação

As fontes de comunicação são previamente cadastradas no sistema e são utilizadas para determinar qual o provedor deverá ser utilizado por uma conta de comunicação.

## Criando uma Conta de Comunicação

Acesse o menu Gestão - Contas - Contas Individuais - Incluir.

Nessa tela deve-se determinar qual a fonte de comunicação será utilizada e para cada uma delas prosseguir com o cadastro. Veja os detalhes em:

* TWITTER
* LINKEDIN

Para maiores informações:

****[@FRAMEWORK](http://fluig.totvs.com/portal/p/10097/subject/rframework)****

**Canais de Atendimento**

**Chamado:** Através do Portal TOTVS - [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2-2-3-9-5 (Framework) ou 2-2-3-9-4 (BI)

## **Vamos remover as opções de integração do ERP com redes sociais devido à baixa utilidade e falhas frequentes. Essa mudança significa que não será mais possível conectar o ERP as redes sociais.**

|  |  |
| --- | --- |
| **Produto** | Framework |
| **Versão** | 12.1.5 |
| **Processo** | Gestão |
| **Subprocesso** | Comunicação |

|  |  |
| --- | --- |
| **Status do documento** | Produção |
| **Data** | 13/03/2015 |
| **Versão** | 1.0 |
| **Versão anterior** | 1.0 |
| **Autores** |  |

| Índice |
| --- |
| truenone |
