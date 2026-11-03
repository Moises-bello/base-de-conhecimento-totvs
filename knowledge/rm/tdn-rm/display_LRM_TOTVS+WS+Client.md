---
content_hash: 52c56b0f3e50b7461fa54d50de3f43f932f3a7c5810284d4804adb68aa8d62fe
fetched_at: '2026-06-29T00:05:57.601650+00:00'
page_id: '172300232'
product: rm
source: tdn-rm
title: TOTVS WS Client
type: documentation
url: https://tdn.totvs.com/display/LRM/TOTVS+WS+Client
version: 34
---

BLOCK

# **Objetivo**

---

O **"TOTVS WS Client"** tem como objetivo auxiliar a utilização e/ou testar a execução dos Web Service's disponíveis no RM.

# **Como Configurar**

---

        Para que o TOTVS WS Client consiga acessar os WebServices do RM, é necessário que os mesmos estejam ativos e que o **DefaultDB** esteja configurado. Para saber como configurar o **DefaultDB** acesse o link: **<http://tdn.totvs.com/x/sQSqC>**

      Para uso do sistema **"TOTVS WS Client"** é necessário copiar os arquivos: **"TotvsWSClient.exe"** e **"TotvsWSClient.exe.config"**para a pasta RM.Net do seu ambiente configurado.

      Em seguida, basta editar o arquivo **"**TotvsWSClient.exe.config**"** alterando as Tag's **"Host", "Port"**e**"WS-Server"** para as configurações do ambiente desejado.Conforme exemplo abaixo:

| TotvsWSClient.exe.config |
| --- |
| xmlEclipse             ]]> |

# **Como Funciona**

---

Existem vários métodos que podem ser utilizados no TOTVS WS Client, como exemplos abaixo:

**Tela da consulta dos dados da visão (READVIEW):**

Equivale ao abrir uma visão padrão RM (de um DataServer) que retorna um conjunto de dados, conforme filtros informados nos parâmetros.

**XML da consulta dos dados das visões (READVIEW):**

Equivale a abrir uma visão padrão RM (de um DataServer) que retorna um conjunto de registros (XML), conforme filtros informados nos parâmetros.

**Tela de consulta dos Dados (READRECORD):**

Faz a leitura do DataServer (regra de negócio RM) e retorna os dados de um registro específico.

**XML da consulta dos dados da edição  (READRECORD):**

Faz a leitura do DataServer (regra de negócio RM) e retorna o (XML) de um registro específico. Este XML pode ser utilizado para incluir ou editar um registro através do método SaveRecord do web service wsDataServer. 

**Funcionalidade Excluir e Excluir Por Chave (DELETERECORD e DELETERECORDBYKEY):**

**1)** O botão **Excluir** utiliza o método **DELETERECORD**, onde é necessário um **Dataset** para fazer a **Leitura do Registro** e depois **sua exclusão (WsDataClient).**

**2)** O botão **Excluir por Chave** utiliza a **chave primária da tabela do registro** para fazer a **exclusão,** sem a necessidade expressa de um **ReadRecord** anterior ****(WsDataClient).****

**Tela de consulta dos processos executados:**

Retorna os dados de todas as execuções de um processo selecionado.

**Tela de visualização dos dados do processo:**

Exibe os parâmetros de execução do processo selecionado anteriormente.

**Tela de consulta do XML dos parâmetros do processo:**

 Fornece o XML de parâmetros necessários para acionar um processo através do WebService wsProcess.

**Tela de consulta da sentença SQL:**

Retorna os dados de uma determinada consulta SQL, através dos parâmetros informados.

**XML da consulta da sentença SQL:**

Exibe o resultado de uma consulta em formato XML.

 

|  |  |
| --- | --- |
| **Produto** | Framework |
| **Versão** | 11.82.XX e 12.01.XX |
| **Processo** | Processos |
| **Subprocesso** | Web Services |

|  |  |
| --- | --- |
| Status do Documento: | Finalizado |
| Data: | 09/07/2015 |
| Versão: | 0.1 |
| Versão Anterior: | 0.1 |
| Autores: |  |
|  |  |

---

Para maiores informações:

****[@FRAMEWORK](http://fluig.totvs.com/portal/p/10097/subject/rframework)****

**Canais de Atendimento**

**Chamado:** Através do Portal TOTVS - [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2-2-3-9-5 (Framework) ou 2-2-3-9-4 (BI)
