---
content_hash: 5a47582efc7cfa8425d7c3b9e11bd3120274e1d78a0325325d906226ba8d238c
fetched_at: '2026-06-29T00:10:48.353373+00:00'
page_id: '561643159'
product: rm
source: tdn-rm
title: Integração RM x SmartLink Data Sharing 1.0
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=561643159
version: 48
---

# **01. VISÃO GERAL**

Neste documento é descrito o processo de configuração da integração do RM com os TOTVS Apps (Carol).

# **02. CONFIGURAÇÃO PASSO A PASSO**

É possível acessar a tela da integração através do menu **Ativação Totvs App**, no módulo de **Integração**:

Após isso, devem ser inseridos o **RAC Client Id** e o **RAC Client Secret**, do ambiente já provisionado.

Nesta tela, basta selecionar os aplicativos a serem integrados, e clicar em **Executar**.

# **03. COMO FUNCIONA**

Através da ferramenta de Conceito o **RM** envia para a **Carol**(Inteligência artificial da TOTVS) informações chaves baseadas nas configurações dos **conceitos de cada integração**.

Após a ativação da integração o processo **ConTotvsAppActivatorProcess** que **configura** a integração será disparado.

Após a execução do processo que configura a integração será iniciado o processo que **Executa**a integração **ConTotvsAppExecutorProcess.**

Atenção

Pelo fato da integração ser executada através de **processos**, os processos  **ConTotvsAppActivatorProcess** e**ConTotvsAppExecutorProcess NÃO**podem ser manipulados pelo usuário. 

Os menus **Iniciar / Parar / Desabilitar / Reiniciar**da visão de gerenciamento de Job's foram desativados. 

Os **WebServices** que **Executam / Agendam** processos também foram bloqueados.

A atividade **ExecutarProcesso**da Fórmula Visual também foi bloqueada para não permitir a execução dos processos citados.

O processo será **recorrente** de acordo com a configuração de periodicidade utilizada no arquivo totvsAppConfig.json.

Atenção

Para entender como funciona o serviço de Monitoramento da saúde do processo acesse : <https://tdn.totvs.com/x/27EMIg>

# **04. VISUALIZAÇÃO DE LOG**

Na tabela GTOTVSAPPLOG é armazenado o log detalhado de cada execução dos conceitos e envios cadastrados na tabela GTOTVSAPPCONCEITOHST.

Informações relevantes sobre a tabela GTOTVSAPPLOG:

Na coluna Tipo, deve ser considerado:  
0 - Mensagem de Sucesso  
1 - Mensagem de Alerta  
2 - Mensagem de Erro

Caso ocorram erros, as colunas Mensagem e Descrição podem ser consultadas para obter mais detalhes.

Exemplo de mensagens de erro:  
Mensagem: Erro ao enviar dados para serviço de api!| {"code":404,"message":"HTTP 404 Not Found"}  
Mensagem: Pacote '1' de '1' enviado com erro!|Erro ao enviar dados para serviço de api!| {"code":405,"message":"HTTP 405 Method Not Allowed"}

Para analisar os registros da tabela de log, é importante filtrar a busca pela chave GTOTVSAPPLOG.IDTOTVSAPPCONCEITOHST, relacionada a coluna GTOTVSAPPCONCEITOHST.ID

# **05. HABILITAR TLS**

**Em alguns casos é necessário ajustar o TLS do servidor.**

Para ajustar basta criar um arquivo com a extensão .Reg e escrever o comando abaixo. Após criar o arquivo basta executar.

Importante que todos os servidores que processam Jobs estejam com essa configuração.

Atenção

**Antes de Executar é importante fazer o backup das todas as chaves descritas no bloco de código.**

# **06. MECANISMO DE EXECUÇÃO DA INTERGRAÇÃO COM O TLC**

Importante

A partir da versão 12.1.2406 a API e visualização dos dados das metricas foi decontinuado.  
  
Desta forma o processo ConTotvsAppExecutorTLCProcess irá apresentar seguinte mensagem no Job "Não foi possível criar a classe de processo. O job será encerrado.", o mesmo irá descontinuar o envio.

      O campo "**IDJOB**" já existente na tabela "**GTOTVSAPP**" é responsável em fazer a subida dos dados para Carol (busca do RM e envia para Carol).

      Com a nova implantação do TLC, após realizar a ativação do TotvsApp, será criado um novo IDJOB na tabela "**GTOTVSAPP**", mas que estará disponível no novo campo "**JOIBIDTLC**". Ele é o responsável por enviar mensagens localizadas na tabela "**G****TOTVSLINKMESSAGE**" para o TotvsLinkClient. 

      A cada exportação realizada com sucesso, o dado das métricas será localizado na tabela "**GTOTVSLINKMESSAGE**", após o envio das métricas serem realizados com sucesso, os dados serão enviados para a tabela "**GTOTVSLINKMESSAGEEXEC**" e excluído na tabela "**GTOTVSLINKMESSAGE"**. 

Importante

Os dois Jobs criados "**IDJOB**" e "**JOIBIDTLC**" não poderão ser desabilitados na tela "**Gerenciamento de Jobs**" localizado no RM.exe, visto que são Jobs de integração. Os mesmo somente serão desabilitados pelo processo de "Desativação da integração".

      Na tabela "**GJOBXEXECUCAO**", deve existir dois Jobs recorrentes (de acordo com a configuração de periodicidade utilizada), referentes aos Ids criados no campos "**JOBID**" e "**JOIBIDTLC**" da tabela "**GTOTVSAPP**".

      E ao realizar a desativação do processo, o Jobs devem ser desabilitados (status = 8).

 

      As métricas, estão sendo enviadas para o Grafana (Uma aplicação web de análise, onde são fornecidos tabelas, gráficos, etc). 

      A execução do "**JOBIDTLC**", fará uma leitura na tabela "**GTOTVSLINKMESSAGE**" e realizará o envio das métrica para o Grafana.   
      Segue abaixo o exemplo da visualização das métricas dentro da aplicação:
