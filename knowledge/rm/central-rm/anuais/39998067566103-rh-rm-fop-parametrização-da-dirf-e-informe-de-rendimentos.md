---
article_id: 39998067566103
category: Anuais
content_hash: 10176d43afe96a64d4d501a6a20c5ba5a2ac7dffb31ae7f1cbc65aaa495a8c33
fetched_at: '2026-06-28T22:46:50.956787+00:00'
product: rm
section_id: 1500000861142
source: central-rm
title: RH - RM - FOP - Parametrização da DIRF e Informe de Rendimentos
type: support-article
updated_at: '2026-04-30T13:05:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39998067566103-RH-RM-FOP-Parametriza%C3%A7%C3%A3o-da-DIRF-e-Informe-de-Rendimentos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39998067549719) Tempo aproximado para leitura: **00:03:50 min**  
  
**Dúvida**  
No módulo **Folha de Pagamento,** como realizar a parametrização dos eventos, seleção de funcionários e regras de retenção para a geração da **DIRF e Informe de Rendimentos**?  
  
**Ambiente**  
RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões.  
  
**Solução**  
Para configurar corretamente os parâmetros da coligada e garantir a emissão adequada da **DIRF** e do **Informe de Rendimentos**, siga as orientações abaixo:  
  
 1. Na geração da DIRF, parametrize a primeira tela conforme desejado e clique em **Avançar** .  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39998067551383)  
  
2. Selecione a coligada desejada e clique no ícone de adicionar parâmetros da coligada  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39998043874583)  
   
3. Em **Eventos** , configure as regras de restituição e afastamento.   
  
No campo **Evento de Restituição de IRRF,** informe apenas eventos que não possuam o código de cálculo (CC) 122, pois eventos com CC 122 são deduzidos automaticamente e sua inclusão neste campo pode causar duplicidade no abatimento.   
  
No campo **13º Pago pela Previdência sobre Lic. Maternidade** , preencha apenas para casos históricos específicos, como afastamentos entre 1999 e 2003 ou para categorias como Doméstica e Contribuinte Individual.   
  
Para os demais casos, mantenha o campo em branco.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39998067552407)  
   
4. Na aba **Parâmetros Específicos /\*Opções de Seleção / Selecionar funcionários ou autônomos** defina conforme a obrigatoriedade.  
  
A opção **Apenas com IRRF** seleciona apenas funcionários com retenção de imposto.

A opção **Com IRRF ou Limites RFB** considera os limites estabelecidos pela IN RFB 1.216/2011, sendo assalariados com rendimentos iguais ou superiores a R$ 28.559,70 ou não assalariados com rendimentos superiores a R$ 6.000,00.  
  
A opção **Todos** considera todos os funcionários com rendimentos tributáveis, isentos, descontos de saúde ou casos de moléstia grave, habilitando também o campo **Usa filtro de seleção ao gerar DIRF em arquivo** para refinamento manual.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39998067554583)  
   
5. Configure as opções de controle de cadastro e movimentação. Para:  
  
**Transferidos:** utilize a opção **Considera movimentação de períodos anterior para transferidos** para unificar os dados do ano-calendário.

**Dependentes:** utilize a opção **Desconsidera número de dependentes no mês da rescisão por transferência** para evitar deduções em duplicidade entre coligadas de origem e destino.

**CPF:** Utilize a opção **Selecionar apenas funcionários com CPF preenchido** para evitar inconsistências no validador da Receita Federal.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39998043877655)  
   
6. Para configurar a geração do informe de rendimentos, acesse a aba **Informe de Rendimentos** , localizada ao lado de **Parâmetros Específicos** .  
  
Em **Opções de Geração** , selecione a opção **Lançar valores para o gerador de relatórios**.   
  
Caso o parâmetro **Apenas lançar valores para o Gerador de Relatórios** esteja desmarcado, o informe de rendimentos também será gerado ao final do processo.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39998043879063)  
  
7. Após essas configurações, prossiga para as demais abas dos parâmetros da coligada conforme a necessidade.  
  
Saiba mais:  
[Parametrização do menu de emissão da rotina DIRF / Informe de Rendimentos](https://tdn.totvs.com/pages/releaseview.action?pageId=208347682#Mapeamento-2-2)
