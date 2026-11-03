---
content_hash: a5688e624e302e8e6f67f4e35b2100e28530889a4ce0624c06d7c5856aaf7450
fetched_at: '2026-06-29T00:05:58.241917+00:00'
page_id: '185744077'
product: rm
source: tdn-rm
title: API
type: documentation
url: https://tdn.totvs.com/display/LRM/API
version: 15
---

# Pré-requisitos

---

2
complete
Linha RM atualizada até a versão 12.1.5

3
complete
Contas de Comunicação devidamente cadastradas e funcionando

# Objetivos

---

Permitir que os módulos utilizem o recurso de envio de informações pelas Redes Sociais.

# Classes

---

A equipe de Framework disponibilizou algumas classes que podem ser utilizadas para utilização desse recurso:

## RMSMessageSender

Todo o envio de mensagens é gerenciado por esta classe. O método Send é o responsável por fazer o envio da mensagem.

| Parametro | Tipo | Descrição |
| --- | --- | --- |
| serviceType | RMSCommunicationServiceType | Enumerado que determina o tipo de publicação |
| providerName | String | Nome do provedor de acesso às redes sociais (Fonte de Comunicação) |
| sender | RMSCommunicationEntity | Entidade/Conta de Comunicação remetente |
| recipient | RMSCommunicationEntity | Entidade/Conta de Comunicação destinatária |
| subject | String | Assunto da mensagem |
| message | String | Texto da mensagem |

## RMSCommunicationEntity

Quando é cadastrada uma Conta de Comunicação, uma RMSCommunicationEntity é criada e salva junto à conta de comunicação no campo PARAMETROS da tabela GCONTACOMUNICACAO.

Nessa entidade, são armazenados os dados necessários ao acesso das APIs das Redes Sociais. Por isso, é necessário utilizá-la ao enviar uma mensagem.

## Recuperando o ProviderName

Quando é cadastrada uma conta de comunicação, uma fonte de dados deve ser informada. Essa fonte de dados é que determina o provedor de acesso às redes sociais. Para recuperar o nome do provedor você deve recuperar o campo CLASSEFONTE da tabela GFONTECOMUNICACAO associado à conta de comunicação que deseja utilizar e invocar o método GetProviderName da classe RMSCommunicationUtils.

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
