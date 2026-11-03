---
article_id: 360000664407
category: Movimento
content_hash: 1c787573fde5deec111df3a630949369b56f65e665b79b996e85f47147de9fb1
fetched_at: '2026-06-28T22:46:36.104783+00:00'
product: rm
section_id: 1500000861602
source: central-rm
title: RH - RM - PTO - Lançar eventos para a Folha de Pagamento
type: support-article
updated_at: '2025-10-15T16:29:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000664407-RH-RM-PTO-Lan%C3%A7ar-eventos-para-a-Folha-de-Pagamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15816576994839) Tempo aproximado para leitura: 00:01:00 min  
  
Dúvida**Como lançar eventos para a folha de pagamento?  
  
**Ambiente**RH - RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 11.80

**Solução**Para enviar os eventos calculados no **TOTVS Automação de Ponto** para o módulo de **Folha de Pagamento**, siga os passos abaixo:

1. Acesse no módulo de **Automação de Ponto,**o menu **Configurações | Parametrizador** ao abrir o assistente clique em avançar e selecione o processo**08.02 - Sindicato** e edite o sindicato desejado.![](https://centraldeatendimento.totvs.com/hc/article_attachments/15816576998807)
2. Ao abrir o novo assistente, avance até a etapa **18 - Eventos** e realize a inserção do evento cadastrado com o evento desejado do **Labore,** ou edite os eventos já cadastrados**.**  
   ![2018-09-14_12_19_10-Assistente_de_Implanta__o_de_Processos__Processo__08.02_-_Parametros_Sindicato__.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15816576999575)
3. Ao abrir o novo assistente, avance até a etapa **18 - Eventos** e realize a inserção do [evento cadastrado no módulo de Automação de Ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025095672-TOTVS-RH-Linha-RM-PTO-Como-cadastrar-eventos) com o evento desejado do **Labore** (RM Folha de Pagamento), ou edite os eventos já cadastrados**.**![2018-03-09_10_40_43-.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360001055868)
4. Caso tenha sido necessário realizar alguma alteração nos eventos, realize o recalculo do ponto do funcionário.
5. Os eventos serão lançados para a aba **Movimento**, localizada dentro do espelho do funcionário.  
   ![2018-03-09_11_31_40-Espelho_do_Funcion_rio_00003_-_MARIA_CONCEICAO_DE_ASSIS.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360001066847)
6. Para lançar este evento, acesse o menu **Movimento | Lançar para Folha de Pagamento**.    
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/13658519055127)
7. Informe a parametrização desejada e selecione os eventos a serem lançados.    
   ![2018-03-09_11_34_13-Lan_amento_de_Eventos_para_o_RM_Labore.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360001066827)
8. Confira o lançamento através do módulo da **Folha de Pagamento**, em **Folha Mensal | Consulta |Consulta Movimento de Integração**.  
   ![2018-03-09_10_55_23-TOTVS_S_rie_T_Servi_os__RM__Alias__CorporeRM___1-TOTVS_SA.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360001055888)  
   ![2018-03-09_11_34_44-TOTVS_S_rie_T_Servi_os__RM__Alias__CorporeRM___1-TOTVS_SA.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360001066807)

**Saiba Mais**Para mais informações sobre os parâmetros da tela **Lançar para Folha de Pagamento**, acesse o documento [Lança Eventos para Folha de Pagamento](https://tdn.totvs.com/pages/viewpage.action?pageId=452719144).

[RH - RM - PTO - Cadastrar eventos no Sindicato do funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043969074)  
[RH - RM - PTO - Cadastrar eventos para cálculo do ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025095672)
