---
article_id: 360018735711
category: Folha Mensal
content_hash: 3b52026aec8d6c029024d4a4dc4c11cb779933184d6e828c4bff4947a221ca0f
fetched_at: '2026-06-28T22:47:00.194776+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Erro CHAPAANTERIORTRANSF  e/ou COLIGADAANTERIORTRANSF
type: support-article
updated_at: '2025-03-07T14:37:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018735711-RH-RM-FOP-Erro-CHAPAANTERIORTRANSF-e-ou-COLIGADAANTERIORTRANSF
---

**Ocorrência**Ao realizar a abertura de qualquer log de cálculo o sistema apresenta a mensagem: **Ocorreu um erro ao efetuar a leitura do registro:****Invalid column name 'CHAPAANTERIORTRANSF'.**O erro também é recorrente ao realizar o processo de transferência de funcionários entre filiais, a mensagem seguinte é apresentada:  
**Funcionário X: Houve erros na execução da transferência.**  
**Invalid column name "COLIGADAANTERIORTRANSF".**  
**Invalid column name "CHAPAANTERIORTRANSF".**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Esses erros ocorrem devido a não existência ou erro nas colunas **COLIGADAANTERIORTRANSF** e **CHAPAANTERIORTRANSF**.  
  
**Solução**Para correção deste erro das colunas **CHAPAANTERIORTRANSF e CHAPAANTERIORTRANSF,** é necessário executar o script abaixo. Existem casos que o Script já está como executado na base, nessa situação é **necessário executar novamente**. Para executar o script novamente é necessário remover o script.  
  
Segue orientação em vídeo para realizar o procedimento de remoção do script, link para execução do script e link para download do script.  
  
[Remoção do SCRIPT](http://suporte.totvs.com/totvs-tdi-files-maps/mapeamentos/portal-anexos/anexos/zendesk/20181030/TTVFLGP1J003-1540922133245-367854.zip)  
[Execução do SCRIPT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007059632-RM-BD-Passos-RM-Executor-de-Scripts-)  
[Download do SCRIPT](http://suporte.totvs.com/totvs-tdi-files-maps/mapeamentos/portal-anexos/anexos/zendesk/20181026/TTVFLGP1J002-1540553416446-542068.zip)
