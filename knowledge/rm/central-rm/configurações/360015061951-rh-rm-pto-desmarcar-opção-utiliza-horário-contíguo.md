---
article_id: 360015061951
category: Configurações
content_hash: 3061bba3a3811dbd2ccad64d2f0e339d96b6a5d19757a547ab1457073d952184
fetched_at: '2026-06-28T22:46:29.940270+00:00'
product: rm
section_id: 1500000835121
source: central-rm
title: RH - RM - PTO - Desmarcar opção 'Utiliza Horário Contíguo'
type: support-article
updated_at: '2025-02-19T00:39:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015061951-RH-RM-PTO-Desmarcar-op%C3%A7%C3%A3o-Utiliza-Hor%C3%A1rio-Cont%C3%ADguo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16780635488407) Tempo aproximado para leitura: 00:01:00min**

**Dúvida**Como desmarcar a opção **Utiliza Horário Contíguo** no parametrizador do funcionário?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 11.80  
  
**Solução**Para desmarcar a opção **Utiliza Horário Contíguo** no parametrizador do funcionário, siga os passos abaixo:

1. Ao tentar desmarcar a opção quando não estiver no período de transição, será apresentada uma mensagem informando a data que a opção foi marcada, conforme exemplo abaixo.  
     
   ![2018-08-27_11_12_28-RM.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360009987151)
2. Para desmarcar esta opção será necessário definir como ativo o período que compreenda a data que a opção foi marcada. Para isso, acesse a guia **Configurações** e selecione o menu **Períodos**.  
     
   ![2018-08-27_11_12_43-TOTVS_S_rie_T_Servi_os__RM__Alias__CorporeRM___1-TOTVS_SA.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360009987131)
3. Na tela de períodos, selecione o período a ser ativado e selecione o menu **Processos** e a opção **Definir período como ativo**. Note que após o processo, a linha do período selecionado ficará com o ícone de **Ativo**.  
   ![2018-08-27_11_13_05-TOTVS_S_rie_T_Servi_os__RM__Alias__CorporeRM___1-TOTVS_SA.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360009971512)  
   ![2018-08-27_11_13_26-TOTVS_S_rie_T_Servi_os__RM__Alias__CorporeRM___1-TOTVS_SA.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360009971492)
4. Agora será possível desmarcar a opção. Para isso acesse novamente a guia **Configurações** e selecione o menu **Parametrizador**.  
     
   ![2018-08-27_11_11_04-TOTVS_S_rie_T_Servi_os__RM__Alias__CorporeRM___1-TOTVS_SA.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360009987071)
5. Selecione a opção **Funcionário**.  
     
   ![2018-08-27_11_11_26-Assistente_de_Implanta__o_de_Processos__Ponto___Funcion_rio_.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360009987091)
6. Selecione o funcionário desejado e clique no botão **Parametrizar**.  
     
   ![2018-08-27_11_12_10-Assistente_de_Implanta__o_de_Processos__Ponto___Funcion_rio_.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360009987171)
7. Desmarque a opção e avance o processo até concluir.  
     
   ![2018-08-27_11_14_05-Assistente_de_Implanta__o_de_Processos__Processo__08.03_-_Funcion_rio__00003_.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360009987111)
8. E necessário **recalcular** o período de transição e os períodos posteriores para que o cálculo seja atualizado.

**Saiba Mais**  
Para saber mais sobre as funcionalidades desta opção, acesse as documentações:

[Horário Contíguo](https://tdn.totvs.com/pages/viewpage.action?pageId=452719358)  
[RH - RM - PTO - Definir Período anterior como Ativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024507332-TOTVS-RH-Linha-RM-PTO-Definir-Per%C3%ADodo-anterior-como-Ativo)
