---
article_id: 17999573065367
category: TAF - eSocial - Atualização
content_hash: 6a2fdd161ad0cd225110105946f42c85cef2408ed7216a3ef2dcee95b8beff63
fetched_at: '2026-06-28T22:45:13.374341+00:00'
product: protheus
section_id: 1500001547902
source: central-protheus
title: RH - Linha Protheus - TAF- ATUALIZAÇÃO - Como atualizar o Binário do TAF?
type: support-article
updated_at: '2024-05-13T12:46:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17999573065367-RH-Linha-Protheus-TAF-ATUALIZA%C3%87%C3%83O-Como-atualizar-o-Bin%C3%A1rio-do-TAF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17999552065815) Tempo aproximado para leitura: 00:05:00 min**

**Dúvida**Automação Fiscal - ATUALIZAÇÃO - Como atualizar o Binário do TAF?   
  
**Ambiente**  
OTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - ATUALIZAÇÃO - Como atualizar o Binário do TAF?

**Solução em vídeo:**

**Solução (leitura):**

⚠ **Sempre realize um Backup da sua estrutura antes de realizar qualquer ação !** ⚠

Para atualização do Binário do TAF é necessário que você baixe os arquivos correspondentes ao seu Sistema Operacional.

**Versão do Binário:**

|  |  |
| --- | --- |
| **Windows** | [clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1112215) |
| **Linux** | [clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1112216) |

**OBS: Lembrando que os binários são compatíveis da Release 12.1.033 em diante.**

Efetue o download do arquivo correspondente ao seu Sistema Operacional, salve-o e descompacte utilizando um programa de extração de arquivos de sua preferência.

![Baixando e copiando binário.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/18000926464407)

Após a descompactação do arquivo baixado, abra a pasta e copie todo o conteúdo.

![Cópia do arquivo.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/18001422160663)

Antes de realizar a substituição dos arquivos em sua estrutura do TAF, acesse o gerenciador de tarefas e pare os serviços **TAF-APPSERVER** e **TAF-WS (REST).**

**OBS: Caso você seja cliente Protheus e tenha Slaves ou Broker, pare-os para realizar a atualização dos mesmos.**

![Parar serviços.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/18000926478487)

Depois de parar os serviços, cole os arquivos baixados na sua estrutura de binários do TAF localizados na pasta **BIN**.

```
Exemplo de caminho: C:/TOTVS/TAF/bin
```

**OBS: Colar e substituir nas pastas APP e APPSERVER. Caso seja cliente Protheus e tenha SLAVES ou Brokers, colar também nas pastas correspondentes aos serviços criados.**

![Copiar arquivos.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/18007622929687)

Ao realizar a substituição dos arquivos, agora devemos deixar o arquivo **dbapi.dll** do DBACCESS igual ao nosso binário. Para isso, acesse a pasta **client** do DBAccess, copie o arquivo dbapi.dll e cole em seus binários que foram atualizados.

```
Exemplo de caminho: C:/TOTVS/TAF/TafDbAccess64/Client
```

![GIF dbapi.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/18015961628055)

Pronto, seu binário está atualizado !

Basta iniciar novamente os serviços na ordem correta (DBACCESS, TAF-APPSERVER e TAF-WS) e acessar a aplicação.
