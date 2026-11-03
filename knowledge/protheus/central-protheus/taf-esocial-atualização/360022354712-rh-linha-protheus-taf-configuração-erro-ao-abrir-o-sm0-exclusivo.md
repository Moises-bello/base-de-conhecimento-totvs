---
article_id: 360022354712
category: TAF - eSocial - Atualização
content_hash: 9c5c67887554f8e217ba0fc3ac91b54f38b318e7c9841db1a67b10d21c4f1c57
fetched_at: '2026-06-28T22:45:13.381809+00:00'
product: protheus
section_id: 1500001547902
source: central-protheus
title: RH - Linha Protheus - TAF - Configuração - Erro ao abrir o SM0 exclusivo
type: support-article
updated_at: '2026-06-24T21:50:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022354712-RH-Linha-Protheus-TAF-Configura%C3%A7%C3%A3o-Erro-ao-abrir-o-SM0-exclusivo
---

**Ocorrência**Ao executar a atualização do TAF através da UPDDISTR ou ao cadastrar uma nova empresa no TAF, deparar-se com o problema que resulta em um erro ao abrir SM0 exclusivo.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Automação Fiscal - À partir da release 12.1.33  
  
**Causa**Este incidente ocorre quando algum serviço da aplicação está consumindo o cadastro de empresas (SM0):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019542991)  
  
**Solução**

1. **Parar o Serviço TAF-WS no TAF Segregado:** No ambiente de TAF segregado, é comum deparar-se com essa situação devido à ativação do serviço TAF-WS. Para solucionar esse problema, é necessário interromper o serviço. Siga as instruções abaixo para encerrar a aplicação:  
     
   [RH - Linha Protheus - TAF - SERVIÇOS - Como parar o serviço TAF-WS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036631673-RH-Linha-Protheus-TAF-SERVI%C3%87OS-Como-parar-o-servi%C3%A7o-TAF-WS)
2. **Identificar e Reiniciar o Serviço Responsável pelo Consumo do Cadastro de Empresas:** Em outra situação, será imprescindível reiniciar ou parar o serviço que está consumindo o cadastro de empresas. Isso ajudará a liberar o SM0 e solucionar o erro.
3. **Gerenciar Schedules no appserver.ini do Protheus:** Verifique a existência de Schedules configurados no arquivo appserver.ini do Protheus. Se houver Schedules configurados, siga as etapas abaixo:

   * Comente as chaves de configuração no arquivo appserver.ini.
   * Após executar o UPDDISTR, descomente as chaves de configuração para reativar o Schedule.

**Dica Adicional: Identificar o Serviço Consumindo o Cadastro de Empresas:** Para determinar qual serviço está consumindo o cadastro de empresas, siga o procedimento abaixo:

* Acesse o diretório $\system, onde "$" representa o diretório de instalação do sistema.
* Tente renomear o arquivo "sigamat.emp".
* O sistema operacional impedirá a ação e exibirá uma mensagem indicando o serviço que está bloqueando a renomeação do arquivo.

Com essas soluções e dicas, você poderá resolver o erro ao abrir SM0 exclusivo ao atualizar o TAF ou cadastrar empresas no TAF. Certifique-se de seguir as instruções com precisão para alcançar uma resolução bem-sucedida.
