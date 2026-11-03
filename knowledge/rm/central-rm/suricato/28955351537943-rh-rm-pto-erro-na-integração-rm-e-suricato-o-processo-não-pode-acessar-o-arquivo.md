---
article_id: 28955351537943
category: Suricato
content_hash: fb42773e95ff6ad047ec744e328cb46bdb78e76a9c462de5afcd4e30f371643e
fetched_at: '2026-06-28T22:46:26.331310+00:00'
product: rm
section_id: 28312167464215
source: central-rm
title: RH - RM - PTO - Erro na integração RM e Suricato - O processo não pode acessar
  o arquivo 'C:\LogWebServiceIntegracaoTSA\WebServiceIntegracaoTSALog.txt' porque
  ele está sendo usado por outro processo
type: support-article
updated_at: '2025-09-05T20:00:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28955351537943-RH-RM-PTO-Erro-na-integra%C3%A7%C3%A3o-RM-e-Suricato-O-processo-n%C3%A3o-pode-acessar-o-arquivo-C-LogWebServiceIntegracaoTSA-WebServiceIntegracaoTSALog-txt-porque-ele-est%C3%A1-sendo-usado-por-outro-processo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28955351525399) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como corrigir o erro a seguir ao editar um funcionário, realizar a carga inicial para Suricato ou algum outro processo que acione a integração com Suricato?

Houve um erro na execução da Fórmula Visual:  
Erro na execução da Atividade: 'CargaInicial'  
Erro: Erro no Agente de Envio (mensagem assíncrona). O servidor não pôde processar a solicitação. ---> O processo não pode acessar o arquivo 'C:\LogWebServiceIntegracaoTSA\WebServiceIntegracaoTSALog.txt' porque ele está sendo usado por outro processo.

**Ambiente**TOTVS RH - TOTVS RH(Linha RM) - Automação de Ponto - A partir da versão 12.1  
  
**Solução**

Esse erro pode ocorrer quando o arquivo de log está aberto ou de alguma forma travado.

Para solucionar esse erro, realize os seguintes passos:

1. Acesse o servidor onde foi instalado o Webservice RM;

2. Abra a pasta indicada no erro. Essa pasta é onde o log foi criado.

    Pasta padrão:  C:\LogWebServiceIntegracaoTSA\

3. Apague o Log, ou coloque-o em outra pasta, ou altere seu nome.

    Nome padrão: WebServiceIntegracaoTSALog.txt

4. Reinicie o IIS
