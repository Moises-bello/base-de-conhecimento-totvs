---
content_hash: cfe981e954238c74117efcf8f7ba531a3d2146a686bab4680aa3a7cad63484fc
fetched_at: '2026-06-29T00:05:56.342023+00:00'
page_id: '149881510'
product: rm
source: tdn-rm
title: Utilizando a atividade "Executar serviço do TOTVS API Service"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=149881510
version: 11
---

# Índice

---

.\*ndice

# Objetivo

---

Este documento tem por objetivo especificar a atividade “**Executar serviço do TOTVS API Service**” disponível na Fórmula Visual (antiga atividade "Executar Mashup").

# Especificação

---

A atividade “Executar serviço do TOTVS API Service” é uma atividade que permite utilizar um serviço disponibilizado pelo **TAS**. No exemplo que será utilizado abaixo, iremos utilizar o serviço de Envio de SMS.

          Para começarmos a utilizar a atividade, temos que conhecer os parâmetros que ela recebe:

| **N°** | **Nome do Parâmetro** | **Descrição do Parâmetro** | **Obrigatoriedade** |
| --- | --- | --- | --- |
| 1 | Usuário | Usuário de Login utilizado no TAS | **OBRIGATÓRIO** |
| 2 | Senha | Senha do usuário do TAS | **OBRIGATÓRIO** |
| 3 | Tipo de Serviço | Tipo do Serviço   * SOACustomService * SOADbService * SOAMashupStudioService * SOAMetadataService | **OBRIGATÓRIO** |
| 4 | Nome do Serviço | Nome do serviço | **OBRIGATÓRIO** |

          Neste exemplo, iremos utilizar o serviço *SOASMSService* do *SOACustomService*.

          Após preencher as informações, os "Parâmetros do serviço do TAS" necessários para execução serão solicitados, assim como as propriedades de "Resultados do serviço do TAS" serão exibidas:

| **N°** | **Nome do Parâmetro** | **Descrição do Parâmetro** | **Obrigatoriedade** |
| --- | --- | --- | --- |
| 1 | Identificação do Remetente | Número do Telefone identificador do envio (DDD + Telefone). Ex: 31999991234 | **OBRIGATÓRIO** |
| 2 | Mensagem | Mensagem a ser enviada (160 caracteres) | **OBRIGATÓRIO** |
| 3 | Provedor de SMS | Fornecedor provedor de SMS que será utilizadoTipo do Serviço   * takenet * infobip | **OBRIGATÓRIO** |
| 4 | Senha do serviço de SMS | Senha cadastrada junto ao fornecedor do serviço | **OBRIGATÓRIO** |
| 5 | Telefone de destino | Número do Telefone destino do envio (DDD + Telefone). Ex: 31999991234 | **OBRIGATÓRIO** |
| 6 | Usuário do serviço de SMS | Usuário cadastrado junto do fornecedor do serviço | **OBRIGATÓRIO** |

          Após preencher os parâmetros, salve e execute a Fórmula Visual.

falsefalse

**Produto:** Framework

false

**Versão:** A partir da 12.1.19

false

**Processo:** Utilizando atividade "Executar serviço do TOTVS API Service" via Fórmula Visual

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
