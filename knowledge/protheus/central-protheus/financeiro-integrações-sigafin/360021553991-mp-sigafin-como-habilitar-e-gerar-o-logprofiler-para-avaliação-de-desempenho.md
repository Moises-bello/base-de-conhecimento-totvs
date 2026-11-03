---
article_id: 360021553991
category: Financeiro - Integrações (SIGAFIN)
content_hash: 3ec69e1e5e08cd3fff5bb9f63656eaf18b702c2b387cd887b7dca1935a8e370a
fetched_at: '2026-06-28T22:38:18.527446+00:00'
product: protheus
section_id: 1500001539241
source: central-protheus
title: MP - SIGAFIN - Como habilitar e gerar o LogProfiler para avaliação de desempenho.
type: support-article
updated_at: '2021-04-28T15:14:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021553991-MP-SIGAFIN-Como-habilitar-e-gerar-o-LogProfiler-para-avalia%C3%A7%C3%A3o-de-desempenho
---

**Dúvida**Como habilitar e gerar o LogProfiler para avaliação de desempenho?  
   
 **Ambiente**Protheus – Financeiro – A partir da versão 11.80  
   
**Solução**

1. Inicie abrindo o arquivo de configuração de seus servidores, mais conhecido como appserver.

![](http://tdn.totvs.com/download/attachments/243638663/image2016-7-8%2015%3A42%3A23.png?version=1&modificationDate=1468003387000&api=v2)

Veja acima que o arquivo de configuração esta nomeado como **"appserver.ini"**

2. Para ativar o LogProfiler é necessário adicionar a clausula "LogProfiler=1" no ambiente que deseja monitorar.

**![(aviso)](http://tdn.totvs.com/s/pt_BR/7201/3d89a43db3618502ceb73a83aa0af888aa0a285a/_/images/icons/emoticons/warning.png) Importante**: Quando habilitamos o LogProfiler ocorre uma pequena queda de performance no ambiente (environment), por isso recomendamos que habilite o logprofiler em um "Aplication Server (Appserver)" exclusivo para o teste (separado dos demais serviços utilizados em seu ambiente de produção).

Exemplo para habilitar o LogProfiler

[SEU AMBIENTE]  
SourcePath=C:\P12.1.17\Protheus\_data\apo  
RootPath=C:\P12.1.17\Protheus\_data\  
StartPath=\system\  
RpoDb=top  
RpoLanguage=portuguese  
RpoVersion=120  
LocalFiles=ctree  
localdbextension=.dtc  
PictFormat=DEFAULT  
DateFormat=DEFAULT  
PanelServer=localhost  
PanelPort=1231  
HelpServer=localhost:8079  
**LOGPROFILER=1 -> Este conteúdo que habilita o log no ambiente**

[Drivers]  
Active=TCP

[TCP]  
TYPE=TCPIP  
Port=1236

[General]  
InstallPath=C:\P1217  
**CONSOLELOG=1 -> Deve-se habilitar o consolelog para que o trace seja gerado nos arquivos console.log e/ou console.bak**

Importante: quando habilitamos o CONSOLELOG=1 os arquivos console.log e console.bak serão gravados dentro da pasta \System, porem existe a clausula "ConsoleFile" onde o administrador do sistema pode alterar o local de gravação do arquivo e seu nome físico, por este motivo devemos prestar atenção a esta configuração.

```
          Veja o exemplo:
```

[General]  
InstallPath=C:\P1217  
CONSOLELOG=1  
ConsoleFile=c:\Sistema\P1217\Logs\Server\_01.log    (Quando utilizamos está opção o administrador do sistema pode alterar o nome do arquivo - Ponto de Atenção)

3. Antes de executar a rotina que será monitorada, é necessário limpar os arquivos de console.log e console.bak.

Observação: Não é possível limpar os arquivos se o serviço do appserver.exe estiver ativo, por isso, derrube o serviço e limpe os arquivos. (Antes de derrubar verifique se existem usuários conectados no sistema).

4. Após os passos 1,2 e 3 execute a rotina a ser monitorada.

    4.1. Abra o SmartClient

    ![](http://tdn.totvs.com/download/attachments/243638663/image2016-7-8%2016%3A10%3A19.png?version=1&modificationDate=1468005063000&api=v2)

    4.2. Execute a rotina desejada.

    4.3. Após finalizar o processamento da rotina, feche o Smartclient.

    Este passo é importante, pois o Log será gerado somente quando fechar a rotina e o      smartclient.

5. **Avalie nos arquivos console.log e console.bak** se o logprofiler foi executado e gerado com sucesso antes de encaminhar o arquivo para análise da equipe de Suporte Técnico. Abaixo segue um exemplo com a estrutura do profiler gerado.

Abaixo veja como identificar se o LogProfiler foi gerado corretamente dentro dos arquivos de console.  
![](http://tdn.totvs.com/download/attachments/243638663/image2016-7-11%2010%3A0%3A18.png?version=1&modificationDate=1468242065000&api=v2)

Abaixo veja como identificar a rotina que foi monitorada pelo LogProfiler.  
![](http://tdn.totvs.com/download/attachments/243638663/image2016-7-8%2017%3A22%3A17.png?version=1&modificationDate=1468009381000&api=v2)
