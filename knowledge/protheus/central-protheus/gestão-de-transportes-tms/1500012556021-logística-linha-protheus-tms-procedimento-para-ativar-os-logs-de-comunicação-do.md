---
article_id: 1500012556021
category: Gestão de Transportes (TMS)
content_hash: ab0127bb36654d442bc0ac8ca9772021ac2494f11bb523f8dbc327b4f7b2b061
fetched_at: '2026-06-28T22:45:32.455828+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Procedimento para ativar os logs de comunicação
  do TSS
type: support-article
updated_at: '2021-06-02T17:13:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012556021-Log%C3%ADstica-Linha-Protheus-TMS-Procedimento-para-ativar-os-logs-de-comunica%C3%A7%C3%A3o-do-TSS
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:02:10 min**  
**Dúvida**Como ativar os logs de comunicação do **ERP - Enterprise Resource Planning** com o **TSS - *TOTVS Service SOA***, e do **TSS** com as **URLs** externas?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as Versões  
  
**Solução****1.** No arquivo de configuração **appserver.ini** que existe dentro do diretório**\bin\appserver** da instalação do **TSS**, habilite/crie as chaves conforme os exemplos abaixo:

![tss2.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019578122/tss2.jpg)

**SPED\_SAVEWSDL:**Habilita a gravação dos **XMLs** de comunicação do **TSS** com os ***Web Services*** Externos. Os arquivos gerados são gravados na pasta **System** do **TSS.**  
Esta chave deve ser habilitada apenas em casos que sejam realmente necessários, pois pode causar certa lentidão na comunicação.  
  
**XMLSAVEALL**: Chave que permite a gravação de todos os **XMLs** de comunicação entre o **TSS** e as aplicações dos clientes do ***Web Services*** do **TSS**. Os arquivos gerados são gravados na pasta **WSLOGXML**do **TSS****.**Esta chave deve ser habilitada somente para ajudar na análise de inconsistências, pois gera um grande número de arquivos **XML**.  
  
**2.** Para que as chaves comecem a funcionar, após configurar e salvar o **appserver.ini**, é necessário reiniciar o **TSS**;  
**Dica:** Antes de realizar a simulação, apague todos os arquivos de extensão **\*.*xml*** das pastas **WSLOGXML** e **SYSTEM**, para que fiquem apenas os registros gerados durante a simulação;  
  
**3.** Realize a simulação do incidente em questão e ao término da simulação, envie os seguintes arquivos para análise da situação:  
- Os arquivos com a extensão **\_in** e **\_out** gerados na pasta **WSLOGXML,**localizada no diretório raiz do **TSS**;  
- Os arquivos com a extensão **\_rcv** e **\_snd** gerados na pasta **SYSTEM**, também localizada no diretório de instalação do **TSS**.  
  
**4.** Ao final da gravação, para desabilitar, altere para **0 - zero** os valores das chaves acima informadas e reinicie o **TSS** novamente;  
  
**Importante**  
**Os parâmetros para geração dos logs só devem estar ativos durante a simulação**. Após a simulação, altere novamente o arquivo **appserver.ini**, desabilitando os parâmetros **XMLSAVEALL** e **SPED\_SAVEWSDL** e reinicie o serviço do **TSS**, assim a aplicação não irá gerar logs desnecessários.
