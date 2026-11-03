---
article_id: 38160392369175
category: Financeiro - Smart View
content_hash: f06696ea66b1f24a88050c5f97c821dd4ae28a3d3db12f3c1dc2e154d1b8a3d0
fetched_at: '2026-06-28T22:37:44.863339+00:00'
product: protheus
section_id: 32632656432151
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFIN - Como analisar e coletar logs
  de erros no Smart View
type: support-article
updated_at: '2026-02-05T13:48:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38160392369175-Cross-Segmentos-Backoffice-Protheus-SIGAFIN-Como-analisar-e-coletar-logs-de-erros-no-Smart-View
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38160417247255) Tempo aproximado para leitura: **00:10:00 min**  
  
**Dúvida**  
Qual o procedimento para diagnosticar as ocorrências de erro apresentadas na tela ao gerar relatórios Smart View no módulo Financeiro?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFIN - Todas as versões  
  
**Solução**  
Quando um relatório do Smart View apresentar erro em tela ou qualquer comportamento inconsistente durante sua execução, é indispensável realizar a coleta dos logs do ambiente. Essa ação é necessária para permitir uma análise detalhada e a correta identificação da causa do problema, considerando o uso de informações e chaves relevantes que auxiliam no diagnóstico.

**Importante:** As validações dos relatórios Smart View utilizam linguagens avançadas. Por esse motivo, é essencial garantir que todo o ambiente esteja devidamente atualizado antes de iniciar a coleta dos logs.

[- Pacote de acumulados BackOffice - Conforme Release](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/Backoffice)

[- LIB Atual - Onca](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/LIB%20Onca)

[- Appserver](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/APPSERVER)

[- DBACCESS](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/DBACCESS)

[- WebApp | Smartclient](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/WEBAPP)

[- WebAgent](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/WEBAGENT)

**Orientamos que todos os procedimentos sejam realizados primeiro em ambiente de homologação atualizado.**

---

##### 

**Configuração de chaves para coleta do console.log:**

Antes da reprodução do erro, se faz necessário a inclusão das chaves no Appserver do ambiente REST usado para configurar o Smart View. A ativação dessas chaves é crucial para mapear a origem e o fluxo do erro, fornecendo detalhes técnicos essenciais para a análise do suporte:

* Aplicar a chave FWTRACELOG=1 na seção [ENVIRONMENT] (ambiente em que o Smart View é executado) no appserver.ini;
* Aplicar as chaves ConsoleLog=1, ConsoleMaxSize=999999999, LogHttpFuncs=1 e rest\_log\_level=1 na seção [GENERAL] no appserver.ini;

**Procedimentos para coleta de logs:**

* Renomeie os arquivos, console.log e console.bak (presentes na pasta do APPSERVER ou onde foi definido para gravação do log);
* Reinicie o serviço do APPSERVER;
* Reproduza o erro novamente (Utilizando o relatório que apresenta a falha);
* Envie ao suporte o console.log gerado junto ao log do Smart View (Necessário acessar o diagnóstico do Smart View e validar qual o caminho apontado, conforme print abaixo):

  O caminho deve ser executado no navegador onde o Smart View foi instalado.

  Caminho para acesso: <http://localhost:7019/diagnostic>

  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38186279126679)
* Valide o Token via SIGACFG (SIGACFG > Ambiente > Cadastros > Configuração TReports/Smart View (Opção: Token, no módulo Configurador);
* Ao abrir o ticket, informe ao suporte se o erro ocorre em todos os relatórios (outros módulos) ou apenas em um específico;
* Valide se o seu agent do Smartv View está atualizado e envie um print

![agent.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38160417249687)

##### **Onde localizo meus logs para coleta e envio?**

Os logs ficam nas pastas internas de seu ambiente. É necessário solicitar à sua equipe de TI a coleta dos logs, caso não tenha acesso

##### **Meu ambiente é TCLOUD, como coletar os logs?**

Em casos de ambientes Cloud, a limpeza do console.log acaba não sendo muito viável de início, pois é necessário abrir uma solicitação para o time **CLOUD** realizar essa ação caso não tenha acesso ao servidor.

No entanto, pode realizar a coleta dos logs no portal, ou via **SFTP**. Isso também é um processo que pode ser efetuado por seu **time de T.I.**, ou por usuários comuns, caso possua acesso ao portal do ambiente Cloud.

[***CLOUD - MP - Download de logs (TCLOUD)***](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408646347671-CLOUD-MP-Download-de-logs-TCLOUD)
