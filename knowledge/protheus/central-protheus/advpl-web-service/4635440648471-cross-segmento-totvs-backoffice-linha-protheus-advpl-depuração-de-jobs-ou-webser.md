---
article_id: 4635440648471
category: ADVPL - Web Service
content_hash: 83c2f755e477855576b0008243aa44ce8c44f24577df3a20b9b8b486624dae3a
fetched_at: '2026-06-28T22:40:10.245952+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Depuração de Jobs
  ou WebService binário Harpia
type: support-article
updated_at: '2024-11-11T17:20:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4635440648471-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Depura%C3%A7%C3%A3o-de-Jobs-ou-WebService-bin%C3%A1rio-Harpia
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27713384418327) Tempo aproximado para leitura: **05:00:00 min****Dúvida**Como depurar um serviços Jobs/ WebService no binário Harpia?  
  
**Ambiente**Cross Segmento - TOTVS BackOffice (Linha Protheus) – ADVPL – A partir da versão 12.1.33  
  
**Solução**

## Depuração de serviços

A principal característica de um serviço é que a sua execução não está diretamente relacionada a interface com o usuário (*SmartClient*) e normalmente é executado em segundo plano pelo *appServer*.

### Preparação para serviços REST

1. No arquivo de configuração do *appServer* (`ini`) comente a sessão `[OnStart]`.
2. Ainda no arquivo de configuração do *appServer*, vá até a sessão `[General]` e ajuste a chave `BUILDKILLUSERS=1`.
3. Reinicie a execução do *appServer*.
4. Abra o arquivo `.vscode\launch.json`.
5. Localize a definição de executor que será utilizada e adicione a chave `"enableMultiThread": true`.
6. Crie um arquivo-fonte, adicione o código abaixo e vá adequando, se necessário.

```
user function startRest()
  //O nome do job REST e ambiente de execução dele, podem ser obtidos no arquivo
  //de configuração do _appServer_.
  //Detalhes da função em https://tdn.totvs.com/display/tec/StartJob
  startjob("HTTP_START", "p12", .f.) //lwait, sempre dever ser false
  sleep(15000) //aguarda o serviço ser inicializado. Ajuste o tempo se necessário.
  alert(">> Serviço REST inicializado. <<")
return
```

### Preparação para outros serviços

1. No arquivo de configuração do *appServer* (`ini`), na sessão `[OnStart]` deixe ativo somente os serviços necessários na depuração e na chave `RefreshRate` informe o intervalo de `30` segundos.
2. Ainda no arquivo de configuração do *appServer*, na sessão `[General]` ajuste a chave `BUILDKILLUSERS=1`.
3. Reinicie a execução do *appServer*.
4. Abra o arquivo `.vscode\launch.json`.
5. Localize a definição de executor que será utilizada e adicione a chave `"enableMultiThread": true`;

### Execução da Depuração

1. Encerre todos os serviços e conexões.   
   ***Dica**: Para compilar qualquer fonte encerre todos os serviços e conexões existentes.*
2. Coloque um ponto de parada que será executado quando o serviço for requisitado.
3. Iniciar a depuração executando qualquer função do *RPO* para que mantenha uma conexão do depurador com o *appServer*. Se for serviço *REST*, então execute a função `u_startRest` e aguarde a mensagem de serviço inicializado.
4. Acione o serviço por fora do **VS-CODE**, por exemplo, executando o `SmartClient`, uma requisição (http, rest, etc)
5. Quando parar no ponto de parada prossiga com a depuração normalmente.

**Nota:**Todas as dúvidas e erros referente a extensão **TOTVS Developer Studio** for **VSCode**, Compilação, Depuração e/ou configuração devem ser direcionadas ao canal oficial **GitHub**(Repositório TOTVS).  
O artigo abaixo contem vídeo exemplificando a abertura.  
[Cross Segmento - TOTVS Backoffice Linha Protheus - AdvPL - Vscode resolução de problemas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044528493)

**Saiba Mais:**[github.com/totvs/tds-vscode](https://github.com/totvs/tds-vscode/blob/master/docs/debugger.md#depura%C3%A7%C3%A3o-de-servi%C3%A7os-jobs)
