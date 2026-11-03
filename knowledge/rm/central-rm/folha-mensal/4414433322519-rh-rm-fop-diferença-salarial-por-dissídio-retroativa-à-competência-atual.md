---
article_id: 4414433322519
category: Folha Mensal
content_hash: b8df562caea6b89af4fd5334392154bb5a4dd8b0433ccff4799e4c742c4e013e
fetched_at: '2026-06-28T22:46:59.308750+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Diferença salarial por dissídio retroativa à competência atual
type: support-article
updated_at: '2026-06-24T18:02:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414433322519-RH-RM-FOP-Diferen%C3%A7a-salarial-por-diss%C3%ADdio-retroativa-%C3%A0-compet%C3%AAncia-atual
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23983235441559) Tempo aproximado para leitura: **00:06:00 min****Dúvida**Como realizar diferença salarial retroativa à competência atual?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**A diferença salarial por dissidio, se deve pelo fato do funcionário receber aumento salarial retroativo a competência atual, onde o sistema irá refazer o calculo das verbas pagas no fato gerador, principalmente o calculo do INSS. É importante ressaltar que, o sistema não realiza antecipação/parcelamento de forma padrão sem utilizar o último salário do histórico salarial, pois para recalcular a diferença salarial, o sistema irá utilizar sempre o último salário lançado no histórico salarial. Se pagar uma porcentagem em uma competência anterior e complementar a outra porcentagem em competência futura, o sistema irá pegar o último salário e recalcular a diferença, descontando o valor antecipado. Porém, validando o último salário. Portanto, essa tratativa é possível apenas através de fórmula.  
  
Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Para calcular diferença salarial por dissidio, deverá criar os eventos abaixo com os seguintes códigos de calculo:  
  
[Código de Cálculo 37](https://tdn.totvs.com/pages/releaseview.action?pageId=452718613)  
[Código de Cálculo 64](https://tdn.totvs.com/pages/releaseview.action?pageId=452718637)  
[Código de Cálculo 65](https://tdn.totvs.com/pages/releaseview.action?pageId=452718611)  
[Código de Cálculo 68](https://tdn.totvs.com/pages/releaseview.action?pageId=452718219)  
[Código de Cálculo 69](https://tdn.totvs.com/pages/releaseview.action?pageId=452719698)  
[Código de Cálculo 114](https://tdn.totvs.com/pages/releaseview.action?pageId=452718664)  
[Código de Cálculo 195](https://tdn.totvs.com/pages/releaseview.action?pageId=452718414)  
  
2. Cadastre no parametrizador o motivo da alteração salarial dissídio. Para isso, acesse: **Configurações | Parametrizador | eSocial.**  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414424551703)  
  
O motivo da informação no parametrizador é para que consiga alterar o salário do colaborador.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414431621399)  
  
Também verificar ainda no **Parametrizador | Funcionários | Restrições cadastrais** se está cadastrado o motivo da alteração salarial por dissídio.  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414409758999)  
  
Essa parametrização é importante para que o processo fique completo.  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414424699287)  
  
3. Após as parametrizações realizadas, deverá alterar o salário do colaborador.   
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414431950743)  
  
No exemplo abaixo, estamos na competência Novembro/2021, iremos aplicar o aumento salarial  retroativo Setembro/2021, através do módulo **Administração de  pessoal | Alterações Cadastrais | Alteração de Salário**, marcando a opção **Dissidio**. A chapa  utilizada no processo é 00007. Informar a data retroativa ao aumento Salarial, é importante para que o sistema reconheça a data no momento de processar o calculo. Muitas vezes alguns informam a data da competência no qual está sendo realizado o Pagamento da diferença  salarial, com esse procedimento o sistema valida a  data e não encontra diferença para ser processada.  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414425177239)  
  
Informar a porcentagem de aumento salarial.  
  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414425195159)  
  
O sistema emite o aviso do valor da alteração salarial.  
  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414425281815)  
  
As informações da alteração salarial como, data de mudança, porcentagem e valor, são demonstradas no histórico salarial e o sistema irá realizar o recálculo baseado na data de mudança.  
  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414425339159)  
  
4. Após a alteração salarial, deverá realizar a diferença salarial através do módulo: **Folha Mensal | Lançamentos |  Diferença salarial.**  
  
![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414425384727)  
  
Marque a opção **Dissidio Sim**. Lembrando que, a competência a ser informada para alteração salarial, deverá ser o mês referente a alteração salarial até a Competência anterior a competência atual, pois para a competência atual, o  sistema  já irá processar a folha com o salario reajustado. Ao marcar a opção **Dissidio Sim**, terá que preencher os dados do dissidio, conforme telas abaixo.  A competência acordada para pagamento, deverá informar a competência no qual está sendo processada a folha atual e não a competência referente ao aumento salarial retroativo.  
  
![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414410546455)  
  
5. O lançamento da diferença salarial, foi processada em um período separado da folha, para melhor conferencia e entendimento do calculo. Segue print do envelope da diferença e os cálculos realizado. Lembrando que estamos calculando a diferença referente as competências Setembro e Outubro/2021.  
  
![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414425911447)  
  
No log de cálculo, o sistema demonstra o calculo da diferença por competência, ou seja, mês a mês, no final totalizando os valores de acordo com a classificação dos eventos, veja que também nos informa  quais os eventos  estão sendo lançados na competência atual para pagamento das verbas.  
  
![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414411211927)  
  
No final do log, o sistema informa quais os eventos que estão sendo lançados na competência atual para pagamento das verbas.  
  
![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414426374423)  
  
Na competência do fato gerador, poderá identificar os valores das diferenças discriminados, através da ficha financeira, na aba **verbas geradas por diferença.**  
![mceclip15.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414426409623)  
  
**Importante**Sempre ocorre muitas dúvidas, quanto ao código de calculo 37. Por qual motivo tem que criar dois eventos com o código de calculo 37, um com incidência e outro sem incidência em INSS. Esse processo, se deve, pelo fato que quando a diferença salarial for por dissidio SIM, o evento com código de calculo  37, não poderá ter incidência em INSS, pois não podemos descontar o INSS  somente da competência  atual, ou seja, somente dos eventos referente a diferença salarial que incide em INSS, onde o sistema terá que verificar as verbas pagas na competência do fato gerador, ou seja, em cada competência no qual está sendo realizada a diferença salarial, somar todos os eventos da época, mais os eventos da diferença salarial, jogar na tabela do INSS, deduzir o valor do INSS que descontou na competência referente a diferença salarial e lançar a diferença do INSS.  
  
A base de INSS  e FGTS será levado para a SEFIP 650 e não na SEFIP 115 / 150 ou 155. O sistema só irá calcular diferença quando o evento tiver código de Calculo, fórmula, tipo hora, tipo referência. Quando o evento for do tipo valor, não será calculado a diferença do mesmo, pois não tem  como o sistema verificar como foi realizado  o calculo, para realizar a diferença.  
  
**Saiba Mais**[Lançamento de Diferença Salarial](https://tdn.totvs.com/pages/releaseview.action?pageId=452718616)  
[SEFIP .Net](https://tdn.totvs.com/display/public/LRM/SEFIP+.Net)  
[Folha Analítica por Dissídio](https://tdn.totvs.com/pages/releaseview.action?pageId=452719951)  
[eSocial - Dissidio Retroativo, como informar?](https://tdn.totvs.com/pages/releaseview.action?pageId=391552023)
