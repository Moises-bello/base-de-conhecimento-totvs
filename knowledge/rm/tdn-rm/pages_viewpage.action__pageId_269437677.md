---
content_hash: a8b44f4b117409ce8b91cc23fd05d1bf4c824a95c173339ced4c1c47b690eff9
fetched_at: '2026-06-29T00:08:22.707370+00:00'
page_id: '269437677'
product: rm
source: tdn-rm
title: Aumentar o Timeout da execução das sentenças SQL
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269437677
version: 28
---

# Índice

---

.\*ndice:

# Objetivo

---

     O objetivo deste documento é mostrar como é feita a configuração para aumentar o Timeout da execução das sentenças SQL.

# Como Configurar

---

    Para aumentar o Timeout da execução das sentenças SQL, siga as orientações abaixo:

    Abra os seguintes arquivos (Localizado em C:\totvs\CorporeRM\RM.Net):

* **RM.Host.Service.exe.config**
* ****RM.Host.exe.config****
* ******RM.Host.JobRunner.exe.config******

    Caso a versão seja inferior a 11.XX o diretório será "c:/corporerm/rm.net"

    Em seguida adicione nos arquivos acima, no bloco de comandos **<appsettings>** a seguinte Tag:

* **<add key="DBSCommandTimeout" value="600" />**

1535392872605\_2008715145

| **RM.Host.Service.exe.config** | **RM.Host.exe.config** | **RM.Host.JobRunner.exe.config** |
| --- | --- | --- |

    Após adicionado a Tag nos arquivos de Host, siga os seguintes passos:

false.

**Processo de Configuração:**

1º Passo:

     Acessar no Windows Explorer da máquina, a pasta “C:\totvs\CorporeRM\RM.Net”.

|  |
| --- |

2º Passo:

    Dentro da pasta "RM.Net", abra o arquivo “RM.Host.ServiceManager.exe'. O botão “Desinstalar” deverá estar habilitado, e o label (texto em negrito) com status igual a “Iniciado”.

|  |
| --- |

3º Passo:

    Clique no botão “desinstalar” até o label (texto em negrito) ficar com seu status de “Serviço não existe”.

|  |
| --- |

4º Passo:

    Acesse novamente a pasta "RM.Net" e pesquise pelo arquivo “\_Broker.dat”, em seguida selecione e delete o mesmo.

|  |
| --- |

5º Passo:

    abra novamente o arquivo “RM.Host.ServiceManager.exe”, em seguida clique no botão “Instalar” até o label (texto em negrito) atingir o status “Iniciado”. 

|  |  |
| --- | --- |

Observação:

**DBSCommandTimeout**

Descrição: Define o tempo máximo que uma Consulta SQL pode levar antes de retornar erro de timeout, em segundos.

Exemplo: <add key="DBSCommandTimeout" value="600" />

Default: 120

**Importante:** O valor 600 (utilizado nos exemplos) pode ser aumentado. Pode-se realizar o teste inicialmente com esse valor, caso o problema persista, aumente gradativamente e refaça o teste.

A tag recebe qualquer valor, o número é convertido de segundos em minutos. Por exemplo, o valor 600 segundos é igual a 10 minutos. Esse valor fica a critério do cliente. Caso o valor configurado for muito alto, a mensagem de timeout não será apresentada.

falsefalse

**Produto:** Framework

false

**Versão:** 11.XX; 12.01.XX

false

**Processo:** Aumento do Timeout da execução das sentenças SQL

falsefalse

**Status:** Finalizado

false

**Data:** 21/12/2016

false

**Autores:**
