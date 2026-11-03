---
article_id: 360062102774
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: d4998bcb3ca9cf9cb53573c0efabc42af734b7ba89148b09ccfa3778b7626ae2
fetched_at: '2026-06-28T22:42:42.135842+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Consumo de licenças na integração do
  APS x SIGAPCP
type: support-article
updated_at: '2021-06-07T11:12:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062102774-Manufatura-Linha-Protheus-SIGAPCP-Consumo-de-licen%C3%A7as-na-integra%C3%A7%C3%A3o-do-APS-x-SIGAPCP
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:01:10 min**  
**Dúvida**Como configurar o ambiente para não consumir licenças na utilização do **WebService** de integração entre os produtos?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Para que não haja consumo de licenças na integração do **APS** - **Planejamento Avançado da Produção** x **SIGAPCP - Planejamento e Controle da Produção**, será necessário fazer uma alteração no appserver.ini onde está configurado o **WebService**.  
A chave **PREPAREIN - Informações para preparação do ambiente**, que instancia o grupo de empresa e filial que fica permanentemente ativos deve ser substituída pela **PCPPREPAREIN,** configurando para abrir o ambiente somente ao executar a integração indicando o grupo de empresa e filial que devem ser utilizados na integração.  
  
**Exemplo**Supondo que o grupo de empresa seja 99 e a filial seja 01, e a configuração abaixo para o *webservice*:

```
[servidor:<porta>/<instancia>]  
ENABLE=1  
PATH=<root_patch>  
ENVIRONMENT=<ambiente>  
INSTANCENAME=<instancia>  
RESPONSEJOB=<secao_job>  
DEFAULTPAGE=<pagina_default>  
  
[<secao_job>]  
TYPE=<type>  
ENVIRONMENT=<ambiente>  
INSTANCES=<número mínimo,número máximo de instâncias>  
SIGAWEB=<sigaweb>  
INSTANCENAME=<instacia>  
ONSTART=<onstart>  
ONCONNECT=<connect>  
PREPAREIN=99,01  
  
A chave PREPAREIN descrita acima deve ser substituída pela PCPPREPAREIN conforme abaixo  
[servidor:<porta>/<instancia>]  
ENABLE=1  
PATH=<root_patch>  
ENVIRONMENT=<ambiente>  
INSTANCENAME=<instancia>  
RESPONSEJOB=<secao_job>  
DEFAULTPAGE=<pagina_default>  
  
[<secao_job>]  
TYPE=<type>  
ENVIRONMENT=<ambiente>  
INSTANCES=<número mínimo,número máximo de instâncias>  
SIGAWEB=<sigaweb>  
INSTANCENAME=<instacia>  
ONSTART=<onstart>  
ONCONNECT=<connect>  
PCPPREPAREIN=99,01
```
