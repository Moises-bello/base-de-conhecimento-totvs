---
content_hash: b13e6a9abaa8456e90f8fef94769da42552ac0a0fea35b75ff5a308ed1aff845
fetched_at: '2026-06-29T00:06:06.039717+00:00'
page_id: '201727657'
product: rm
source: tdn-rm
title: Criação DumpFile
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201727657
version: 5
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework               **Versão:**11.8X   12.1X |
| **Processo** | **:** | Criação   automática da queda do serviço do Host. |
| **Subprocesso** | **:** | *Verificação / Configuração   do ambiente N camadas* |
| **Data da   publicação** | **:** | 10/09/2015 |

**Introdução:** Este aplicativo servirá para configurarmos no ambiente a identificação de porque o Serviço do Host (RM.Host.Service.exe) está tendo quedas constantes ou aumento do processamento do Servidor ou Computador local, assim como alto consumo do JobRunner.

Sempre que ocorrer **queda do serviço do Host,** alteração de **aumento do serviço Host** sem nenhum motivo aparente, **serviço de Host em queda ou aumentando processamento**, será válido algumas verificações conforme descritas abaixo:

Para tal, temos dois processos:

**Procedimento 1:**

* Realizar o download dos arquivos de configuração
* Copie o arquivo para uma diretório/disco que tenha espaço suficiente para geração do Dump
* Executar o Instalar.bat para a instalação do aplicativo
* Abra o Gerenciador de Serviços do Windows
* Abra o arquivo “CreateAutomaticHostDump.exe.config” e coloque as informações do seu ambiente: 
  + Application: defina o nome do aplicativo que irá coletar o Dump (RM.Host.Service, RM.Host.JobRunner)
  + MaxGBMemory: define a quantidade de memória máxima para geração do Dump (sugiro 4 GB para seu ambiente)
* Inicialize o serviço “Criador de dump automatico do Host”
* Aguarde até que o serviço atinja a quantidade de memoria definida
* O Arquivo de Dump será gerado no mesmo diretório dos arquivos de Configuração da ferramenta.

**Procedimento 2:**

Outra forma de realizar é acessar o processo através do Gerenciador de Tarefas:

Clicar com o botão direito em cima do **JobRunner**, ir na opção **Criar Arquivo de Despejo**

**Lembre-se:** sempre enviar junto ao chamado também a linha de comando sendo executada no momento (como no print screen)

Para tal, acesse a opção **Exibir - Selecionar Colunas...**

E selecionar a opção **Linha de Comando**
