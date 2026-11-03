---
article_id: 28954495948055
category: Suricato
content_hash: 79cfa112369f95be8cdb1a40c766846f466e99825dd923dfaabd0bcca2cedfd4
fetched_at: '2026-06-28T22:46:26.339189+00:00'
product: rm
section_id: 28312167464215
source: central-rm
title: RH - RM - PTO - Erro na integração RM e Suricato - AliasDBNaoEncontrado
type: support-article
updated_at: '2025-09-05T20:17:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28954495948055-RH-RM-PTO-Erro-na-integra%C3%A7%C3%A3o-RM-e-Suricato-AliasDBNaoEncontrado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28954495905431) Tempo aproximado para leitura: **00:02:00min****Dúvida**Como corrigir o erro a seguir ao editar um funcionário, realizar a carga inicial para Suricato ou algum outro processo que acione a integração com Suricato?

Houve um erro na execução da Fórmula Visual:  
Erro na execução da Atividade: 'CargaInicial'  
Erro: Erro no Agente de Envio (mensagem assíncrona). System.Web.Services.Protocols.SoapException: O servidor não pôde processar a solicitação. ---> System.ApplicationException: Properties.Resources.SLibValidLSAliasDBNaoEncontrado em RM.Pto.Common.PtoUtilsDataBaseServices.GetDbAlias(String alias) em RM.Pto.Common.PtoUtilsDataBaseServices.GetDbServices(String nomeAlias) em RM.Pto.WebService.TSService.get\_DBS() em RM.Pto.WebService.TSService.receiveMessage(String inMsg) --- Fim do rastreamento de pilha de exceções internas ---

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28954495906839)

**Ambiente**TOTVS RH - TOTVS RH(Linha RM) - Automação de Ponto - A partir da versão 12.1  
  
**Solução**  
Para solucionar esse erro, realize os seguintes passos:  
1. Verifique na barra de título do RM qual o nome do Alias que é utilizado;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28954495909399)

2. Acesse o servidor onde foi instalado o Webservice RM;

3. Acesse a pasta do Webservice RM (pasta padrão C:\TSA) e edite o arquivo Alias.dat;

4. Ajuste a tag <Alias></Alias> para que tenha o mesmo nome do Alias verificado na barra de título do RM;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28954525470103)

5. Volte na pasta do Webservice RM e agora edite o arquivo Web.config

6. Localize a tag <add key="Alias" value=""/> e informe no atributo value o nome do Alias verificado na barra de título do RM.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28954495915287)

7. Após os ajustes, reinicie o IIS para aplicar as modificações.

**Saiba mais**

[RH - RM - PTO - Instalação e configuração do Webservice RM para integração com o Suricato](https://centraldeatendimento.totvs.com/hc/pt-br/articles/27720600761367)
