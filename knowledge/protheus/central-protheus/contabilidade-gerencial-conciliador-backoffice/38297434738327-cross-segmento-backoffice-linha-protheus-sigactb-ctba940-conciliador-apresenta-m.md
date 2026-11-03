---
article_id: 38297434738327
category: Contabilidade Gerencial - Conciliador BackOffice
content_hash: 87e3d295831400f55d4b17c8b9643e94116350d80e18276809fe33f142d91663
fetched_at: '2026-06-28T22:40:30.937263+00:00'
product: protheus
section_id: 31314114896791
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA940 - Conciliador
  apresenta menssagem "Internal Server Erro"
type: support-article
updated_at: '2026-02-10T16:58:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38297434738327-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA940-Conciliador-apresenta-menssagem-Internal-Server-Erro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38297434726551) Tempo aproximado para leitura: **00:10 min**

**Dúvida**  
O conciliador Backoffice (rotina CTBA940) exibe a mensagem de "Internal Server Error" durante o processamento ou abertura. Quais procedimentos devem ser realizados para identificar a causa?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Contabilidade Gerencial - 12.1.2210

**Solução**  
O erro "Internal Server Error" é um retorno genérico do protocolo HTTP indicando que o servidor (*AppServer*/*REST*) encontrou uma condição inesperada. Para identificar a causa raiz, é necessário habilitar chaves de rastreio detalhadas e coletar os logs de comunicação entre o Protheus, o DBAccess e o serviço REST.

* Para ambientes em **Cloud Totvs:**  
    
  A coleta deve seguir os procedimentos específicos de download de logs via portal T-Cloud, conforme processo da documentação: [CLOUD - MP - Download de logs TCLOUD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408646347671-CLOUD-MP-Download-de-logs-TCLOUD)
* Para ambientes on-premise:  
  1. Interrompa temporariamente os serviços: **dbaccess** e **appserver**;
  2. Antes de reiniciar os serviços, acesse as pastas de instalação e **renomeie** os arquivos de log atuais para que um novo log limpo seja gerado:  
     + \dbaccess\dbaccess.log
     + \dbaccess\dbconsole.log
     + \appserver\console.log
  3. No arquivo **appserver.ini**, adicione as seguintes chaves para validação dos logs:  
     + Na seção **[Ambiente]** (ex: [P12]), insira:  
         
       FWTRACELOG=1  
       LogHttpFuncs=1
     + Na seção **[GENERAL]**, insira:  
         
       consolelog=1  
       tlpp\_rest\_log=1   
       rest\_log\_level=6  
       rest\_log\_StringSize=0
  4. Inicie os serviços novamente;
  5. Reproduza o erro na rotina **CTBA940** para que o sistema registre os detalhes nos novos arquivos;
  6. Após a reprodução, colete os seguintes arquivos atualizados para análise técnica:  
     + \dbaccess\dbaccess.log
     + \dbaccess\dbconsole.log
     + \appserver\console.log
     + Arquivos com a nomenclatura appserver\_[data\_hora].log ou appsrvlinux\_[data\_hora].log (gerados automaticamente no diretório do AppServer).

**Saiba Mais:**

[Ambientes Cloud (T-Cloud)](https://tdn.totvs.com/pages/viewpage.action?pageId=706922008)

[LogHttpFuncs - TOTVSTEC](https://tdn.totvs.com/display/tec/LogHttpFuncs)

[Como Ativar a função FWLogMsg.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041301114-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-Ativar-a-fun%C3%A7%C3%A3o-FWLogMsg-?source=search)

[TLPP REST LOG](https://tdn.totvs.com/display/tec/tlpp_rest_log)
