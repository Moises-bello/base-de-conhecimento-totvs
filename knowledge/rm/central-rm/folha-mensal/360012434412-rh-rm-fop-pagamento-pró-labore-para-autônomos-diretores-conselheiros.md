---
article_id: 360012434412
category: Folha Mensal
content_hash: 693ff9ea29cd978629dcafd94d136b5a72547035b206967f072a2dcbc1697bd9
fetched_at: '2026-06-28T22:47:00.303233+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Pagamento pró-labore para Autônomos, Diretores, Conselheiros
type: support-article
updated_at: '2024-10-23T21:59:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012434412-RH-RM-FOP-Pagamento-pr%C3%B3-labore-para-Aut%C3%B4nomos-Diretores-Conselheiros
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27286981898391)**Tempo aproximado para leitura: **00:03:45 min****Dúvida**Como realizar o pagamento do pró-labore para Autônomos, Diretores e Conselheiros?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para solucionar, realize a parametrização abaixo e depois faça o lançamento do pró-labore.  
  
1. Acesse: **Administração de Pessoal | Funcionários** e edite o funcionário em questão. Logo, acesse a aba **Registro** e no campo **Tipo do Funcionário** deverá ser **A** - **Autônomo** ou **D** - **Diretor.**![](https://centraldeatendimento.totvs.com/hc/article_attachments/27286981906967)  
  
2. Ainda no cadastro do funcionário, acesse a aba **FGTS / SEFIP** e veja como está parametrizado o campo **Código da Categoria**. Para autônomos deverá ser usado os **códigos 13 ou 14** e para diretores, **5 ou 11**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27286981910039)  
  
3. Nos casos de funcionário Autônomos com categoria **13 ou 14**, é obrigatório a informação do PIS. Nesta mesma aba **FGTS / SEFIP**, informe o PIS no campo **Código Contribuinte Individual**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27286981912471)  
  
4. Verifique se evento de pagamento do pró-labore possui [Código de Cálculo 46 - Honorários](https://tdn.totvs.com/pages/releaseview.action?pageId=452718291).  
O código de calculo 46 não busca o valor do salario no cadastro do colaborador.   
  
**Existem duas opções de lançamento:**

* **Primeira opção:** Informar o evento de pagamento em Código Fixo dentro do cadastro do Colaborador e com o valor ser pago.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5280074731415)

* **Segunda opção:** Cadastrar o Grupo de Eventos destinado ao colaborador e informar o evento ser pago com valor ser lançado.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5280098741911)  
  
5. Para recolhimento do INSS de Diretores, Autônomos, Conselheiros deverá ser parametrizada uma fórmula de cálculo juntamente com o código de cálculo 85. Para mais informações sobre como parametrizar a fórmula para realizar o cálculo, [clique aqui](http://tdn.totvs.com/pages/releaseview.action?pageId=118885145).  
  
6. Depois das informações estarem parametrizadas e corretas lance o grupo de eventos criado para realizar o Pró-Labore.   
  
**Saiba Mais**[RH - RM - FOP - Lançamento dos grupos de eventos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014011632-RH-RM-FOP-Lan%C3%A7amento-do-Grupo-de-Eventos)  
[COMO FAZER - INSS // IRRF AUTÔNOMO](https://tdn.totvs.com/pages/releaseview.action?pageId=494803250)  
[COMO FAZER - INSS AUTÔNOMO](https://tdn.totvs.com/pages/releaseview.action?pageId=118885145)
