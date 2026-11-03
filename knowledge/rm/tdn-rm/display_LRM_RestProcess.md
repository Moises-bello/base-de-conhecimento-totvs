---
content_hash: 7f83a90f93d7953a70969780feb0f03ac4265fc198254502ca732c19104731db
fetched_at: '2026-06-29T00:08:52.682214+00:00'
page_id: '342299224'
product: rm
source: tdn-rm
title: RestProcess
type: documentation
url: https://tdn.totvs.com/display/LRM/RestProcess
version: 107
---

# Índice:

---

.\*ndice:

# Objetivo

---

Apresentar como utilizar o serviço RestProcess.

# Requisitos

---

Versão

 Disponível à partir da versão 12.1.21 da linha RM.

| Linha de Software | Versão | Data de Liberação | Observação |
| --- | --- | --- | --- |
| **RM** | 12.1.21 e/ou posteriores | Junho/2018 | Para os requisitos de software deve-se consultar a [Portabilidade RM](http://tdn.totvs.com/display/LRM/PORTABILIDADE) |

falseAlias Default

```
Acesse a máquina ou servidor que está executando o serviço. 
Vá ao diretório C:\totvs\CorporeRM\RM.Net e edite o arquivo RM.Host.Service.exe.config.
```

```
Inclua a tag <add key="DefaultDB" value="CorporeRM" /> dentro da limitação appSettings.  
O valor a ser atribuído a tag DefaultDB deve ser idêntico ao nome do alias que aponta para a base de dados utilizada. No exemplo que citamos atribuímos o valor "CorporeRM" ao alias e respectivamente ao DefaultDB.
```

```

```

xmlRM.Host.Service.exe.Config















]]>Atenção

Para que estas configurações entrem em vigor será necessário reiniciar o serviço do Host.

# Métodos disponibilizados pelo serviço:

---

| Método | URL | Nome | Descrição |
| --- | --- | --- | --- |
| GET | rest/restprocess/getschema/{processServerName} | GetSchema | Faz a leitura do Processo informado. |
| GET | rest/restprocess/getprocessstatus/{jobId}/{execId} | GetProcessStatus | Monitora o progresso da execução de um processo. |
| POST | rest/restprocess/executeprocess/{processServerName} | ExecuteProcess | Executa o processo informado |
| POST | rest/restprocess/executeprocessasync/{processServerName} | ExecuteProcessAsync | Executa o processo informado de forma assíncrona. |

# Exemplos de Utilização:

---

falseRestProcess»localhost:8051»GetSchema

## Exemplo de Uso

Url: <http://localhost:8051/rest/restprocess/getschema/GlbCopyPermisUsrProc>

Resultado Esperado

js

Exemplo prático no postman

falseRestProcess»localhost:8051»ExecuteProcess

## Exemplo de Uso

Url: <http://localhost:8051/rest/restprocess/executeprocess/GlbCopyPermisUsrProc>

Body:

js

Exemplo prático no Postman

falseRestProcess»localhost:8051»ExecuteProcessAsync

## Exemplo de Uso

Url: [http://localhost:8051/rest/restprocess/executeprocessasync/GlbCopyPermisUsrProc](http://localhost:8051/rest/restprocess/executeprocess/GlbCopyPermisUsrProc)

Body:

js

Exemplo prático no Postman

falseRestProcess»localhost:8051»GetProcessStatus

## Exemplo de Uso

Url: <http://localhost:8051/rest/restprocess/getprocessstatus/103157/1>

js

Exemplo prático postman:

Exemplo prático no Postman

falsePara maiores informações:

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.21 (superiores)

false

**Processo:** Integração

false

**SubProcesso:** RestProcess

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
