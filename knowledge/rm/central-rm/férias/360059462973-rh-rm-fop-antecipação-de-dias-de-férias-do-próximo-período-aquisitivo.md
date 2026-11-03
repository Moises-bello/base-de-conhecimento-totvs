---
article_id: 360059462973
category: Férias
content_hash: e1111eebfcc57c49408ea5fa93bb91f80c38edafa28e15f64c13b3d1e2cbf03d
fetched_at: '2026-06-28T22:46:56.437410+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: RH - RM - FOP - Antecipação de dias de férias do próximo período aquisitivo
type: support-article
updated_at: '2025-01-21T17:47:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059462973-RH-RM-FOP-Antecipa%C3%A7%C3%A3o-de-dias-de-f%C3%A9rias-do-pr%C3%B3ximo-per%C3%ADodo-aquisitivo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:04:00 min  
  
Dúvida**Como realizar a antecipação de dias de férias do próximo período aquisitivo para um funcionário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para realizar a antecipação dos dias de férias do próximo período aquisitivo, é necessário verificar primeiramente a parametrização no **Sindicato**, pois isso definirá de forma correta as informações no cadastro do funcionário. Veja o passo a passo a seguir:  
  
1. Acessar o **Sindicato** e verificar se a flag **Permite antecipação de dias de férias do próximo período aquisitivo** está marcada. Se esta flag não estiver marcada, no cadastro de férias do funcionário, não será criada a aba **Antecipação de férias**, onde a informação dos dias de férias antecipados ficará armazenada conforme veremos a seguir.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099998413/mceclip0.png)  
  
Lembre-se de verificar se o **Sindicato** onde está fazendo esta marcação é o mesmo do funcionário que pretende antecipar as férias.  
  
2. Comprovando que realmente o funcionário precisa tirar férias, mas ultrapassará os 30 dias de férias dentro deste período aquisitivo, basta realizar o cadastro das férias normalmente. No exemplo abaixo, o funcionário tem 17,5 dias de saldo de férias, mas serão cadastrados 30 dias.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100125853/mceclip1.png)  
  
3. Ao acessar o cadastro de férias do funcionário, a aba de **Antecipação de férias** já estará disponível devido à flag marcada no **Sindicato**. Ao cadastrar as férias, será demonstrado o saldo negativo em **Férias a marcar** e que será descontado no próximo período aquisitivo.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097858754/mceclip2.png)  
  
4. Ao salvar o cadastro das férias, serão emitidas duas mensagens pelo sistema. A primeira mensagem informa que o saldo dias de férias a ser cadastrado é superior ao saldo que o funcionário tem de direito. Clique em sim.  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100125933/mceclip3.png)  
  
A segunda mensagem informa sobre a quantidade de dias de férias a serem antecipados. Clique em sim.  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097858814/mceclip4.png)  
  
5. Ao finalizar o cadastro de férias e salvar as informações, os dias de antecipação serão demonstrados na aba de antecipação de férias.  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100125993/mceclip5.png)  
 **Importante**- A aba **Antecipação de férias** fica com seus campos desabilitados para edição, uma vez que são alimentados automaticamente pelo sistema;  
- A antecipação de férias do próximo período aquisitivo, conforme demonstrada acima, só é possível quando o funcionário está ultrapassando o gozo de 30 dias de um mesmo período aquisitivo, somando os períodos de gozo dentro deste período aquisitivo. Ou seja, não se enquadra quando o funcionário ainda tem avos de férias o suficiente a serem conquistados neste mesmo período. Caso o usuário marque férias para um funcionário cujo período aquisitivo acabou de se iniciar, por exemplo, o campo **Férias a marcar** também ficará negativo, mas não alimentará o campo **Nro dias antecipados** da aba **Antecipação de férias**, uma vez que o valor negativo das Férias a marcar será abatido a cada avo conquistado.
