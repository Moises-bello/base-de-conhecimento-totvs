---
article_id: 18504207190039
category: TAF - eSocial - DBAccess
content_hash: ae12952c714eb187731b3480645f702c68e18d8c69df0800df5dfad510fe888f
fetched_at: '2026-06-28T22:45:12.404030+00:00'
product: protheus
section_id: 1500001536981
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - ATUALIZAÇÃO - Como atualizar o DBACCESS
  do TAF?
type: support-article
updated_at: '2024-10-28T14:25:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18504207190039-RH-Linha-Protheus-TAF-eSocial-ATUALIZA%C3%87%C3%83O-Como-atualizar-o-DBACCESS-do-TAF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18504207152023) Tempo aproximado para leitura: 00:05:00 min**

**Dúvida**Automação Fiscal - ATUALIZAÇÃO - Como atualizar o DBACCESS do TAF?   
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Como atualizar o DBACCESS do TAF - Todas as versões.

**Solução em vídeo:**

**Solução (leitura):**

⚠ **Sempre realize um Backup da sua estrutura antes de realizar qualquer ação !** ⚠

Para atualização do DBACCESS do TAF é necessário que você baixe os arquivos correspondentes ao seu Sistema Operacional.

**Versão do DBACCESS:**

|  |  |
| --- | --- |
| **WINDOWS X64** | [clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/1168438) |
| **LINUX X64** | [clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/1168439) |

**OBS: Lembrando que o DBACCESS só é homologado para a versão 64 bits.**

Ao efetuar o download do arquivo correspondente ao seu Sistema Operacional, salve-o em seu local de preferência.

![Baixar DBAccess (1).gif](https://centraldeatendimento.totvs.com/hc/article_attachments/18505135561623)

Salvando o arquivo, agora será necessário parar o serviço do DBACCESS.

Recomendamos que você pare todos os serviços da sua aplicação. Acesse o gerenciador de tarefas clicando com o botão direito em sua barra de tarefas, vá na aba "Serviços", pare primeiro os binários, Brokers ou Slaves e depois o serviço do DBACESS.

![Parar Serviços.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/18560667974935)

OBS: Caso o serviço do REST (TAF-WS) não pare, finalize-o na aba "Processos" encerrando o processo "Application Server". Para certificar que o processo é realmente o serviço do REST (TAF-WS) você pode expandir no canto esquerdo os detalhes do serviço.

![Parar o serviço do REST.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/18560666926615)

Depois de parar os serviços, extraia os arquivos utilizando seu programa de extração de sua preferência e copie os arquivos baixados.

![Extrair e copiar os arquivos.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/18574217775127)

Cole os arquivos copiados na sua estrutura do DBACCESS do TAF localizados na pasta **TafDbAccess64**.

```
Exemplo de caminho: C:/TOTVS/TAF/TafDbAccess64
```

**![copiar e colar os arquivos.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/18574205787543)**

Ao realizar a substituição dos arquivos, agora devemos deixar o arquivo **dbapi.dll** do DBACCESS igual ao nosso binário, brokers ou slaves. Para isso, acesse a pasta **client** do DBAccess, copie o arquivo dbapi.dll e cole em suas pastas dos binários, brokers ou slaves.

```
Exemplo de caminho: C:/TOTVS/TAF/TafDbAccess64/Client
```

![Atualização DBAPI .gif](https://centraldeatendimento.totvs.com/hc/article_attachments/18574281993623)

Pronto, seu DBACCESS está atualizado !

Basta iniciar novamente os serviços na ordem correta (DBACCESS, TAF-APPSERVER e TAF-WS) e acessar a aplicação.
