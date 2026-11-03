---
article_id: 360005553391
category: Cadastros
content_hash: d8bba72c2022443e6d53536f28ac029d3fcae04a3bc63b993261045ba44f8fc1
fetched_at: '2026-06-28T22:46:28.582615+00:00'
product: rm
section_id: 1500000861582
source: central-rm
title: RH - RM - PTO - Horários por jornada
type: support-article
updated_at: '2026-05-11T20:34:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005553391-RH-RM-PTO-Hor%C3%A1rios-por-jornada
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19409061616279) Tempo aproximado para leitura: 00:01:00 min**  
  
**Dúvida**  
Como cadastrar horários por jornada?  
  
**Ambiente**  
RH - RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 11.80  
  
**Solução**

Para solucionar essa dúvida, abaixo segue vídeo de como criar um horário por jornada:

 

Abaixo segue o  passo a passo do processo:

1. Acesse o módulo de **Automação de Ponto**, guia **Cadastros** e selecione o menu **Horários por Jornada**.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/13769256052503)
2. Clique no botão **Incluir** ao abrir a janela aberta, preencha as informações do **Código** e **Descrição** do horário, e faça a parametrização desejada.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/13769365080343)
3. Após salvar o registro e acesse o menu **Anexos**e selecione o item **Índice da jornada**.  
   ![2018-06-27_11_33_32-TOTVS_S_rie_T_Servi_os__RM__Alias__CorporeRM___1-TOTVS_SA.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360006861851)
4. Para realizar a inserção de índices, selecione o botão **Incluir** e preencha as informações de acordo com a jornada que o funcionário deverá executar.  
   ![2018-06-27_11_33_56-.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360006861831)
5. Para associar o horário criado ao cadastro de funcionário, acesse a visão do cadastro de funcionários (Cadastro | Funcionários), selecione o funcionário desejado, em seguida, clique no botão de Anexos | Horário Planejado | Histórico de Horário da Jornada. No botão incluir, deverá selecionar o horário por jornada criado, assim como uma data de mudança e o índice. Se atente ao comportamento do horário anterior e atual, no caso de horário noturno.

   ![2026-04-28 15_25_18-TOTVS Linha RM - Serviços  Alias_ CorporeRM _ 1-TOTVS SA.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40105633675159)

   ![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/13769365080343)

**Importante**

**Restrições para uso do cálculo por jornada:**

* **Intervalos de tolerância:** As tolerâncias de atrasos e extras são cadastradas dentro do índice da jornada do horário. ***A tolerância do sindicato não é considerada para o cálculo***.
* **Considera feriado de acordo com a 1ª batida do horário:** ***Sempre desmarcado**,* o cálculo por jornada já considera a jornada para os cálculos do feriado.
* **Considera feriado até a saída da jornada:** ***Sempre desmarcado***, o cálculo por jornada já considera a jornada para os cálculos do feriado.
* **Distribui extras em faixas considerando a jornada:** ***Não deve estar marcado,*** o cálculo por jornada já considera as extras de acordo com a jornada.
* **Distribui extras descanso, feriado, compensado considerando jornada de trabalho:** ***Não deve estar marcado,*** o cálculo por jornada já considera as extras de acordo com a jornada.
* **Distribui extras adicional Noturno considerando a jornada de trabalho:** ***Não deve estar marcado,*** o cálculo por jornada já considera as extras de adicional de acordo com a jornada.
* **Considera início da jornada para definir tipo de extra:** ***Não pode estar marcado,*** o cálculo por jornada já considera a jornada para distribuição de extras.
* **Considera extras até o fim da jornada na distribuição de extras:** ***Não pode estar marcado,*** o cálculo por jornada já considera a jornada para distribuição de extras.

**Saiba Mais**  
Para maiores informações sobre o cadastro de horário por jornada, acesse a documentação:

[Horários por jornada](https://tdn.totvs.com/pages/releaseview.action?pageId=452719573)  
[Índices da Jornada](https://tdn.totvs.com/pages/viewpage.action?pageId=452719313)
