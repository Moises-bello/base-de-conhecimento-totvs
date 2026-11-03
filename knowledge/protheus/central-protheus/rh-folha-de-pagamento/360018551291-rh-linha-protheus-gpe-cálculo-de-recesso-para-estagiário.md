---
article_id: 360018551291
category: RH - Folha de Pagamento
content_hash: e8c1957122bda5a4ff976e9a4f47ab9c613e6a99e9c3db03ecee9c497657449e
fetched_at: '2026-06-28T22:44:11.807098+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE -  Cálculo de Recesso para Estagiário
type: support-article
updated_at: '2026-06-22T18:14:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018551291-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-Recesso-para-Estagi%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26265187120151) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Como calcular o **recesso do estagiário?**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões   
  
**Solução**O cálculo de Recesso para Estagiários, **não é feito pela rotina de Férias**, os dias de recesso são **lançados diretamente na folha.** Para pagamento do recesso corretamente, siga as orientações abaixo.  
  
Verifique a categoria e categoria E-social do funcionário - **GPEA010**: RA\_CATFUNC = **E ou G** e RA\_CATEFD = **901;**  
![](http://tdn.totvs.com/download/attachments/284879923/image2017-7-19%2013%3A51%3A42.png?version=1&modificationDate=1500484103000&api=v2)  
  
No cadastro de Verbas - **GPEA040** - Cadastre uma verba com Id p/ Cálculo **0891 - Recesso Estagiário**. Na aba **incidências** o campo **Ref. Fer** deve ser preenchido com **Não;**

![](http://tdn.totvs.com/download/attachments/284879923/image2017-7-19%2013%3A53%3A26.png?version=1&modificationDate=1500484103000&api=v2)  
  
Em **Atualizações > Def. Cálculos > Tipos de Ausências - GPEA430** - Cadastre um novo tipo de ausência, com tipo **4 - Controle de Dias de Direito** e informe a verba cadastrada de **Id 0891;**

![](http://tdn.totvs.com/download/attachments/284879923/image2017-7-19%2013%3A54%3A30.png?version=1&modificationDate=1500484103000&api=v2)  
  
Em **Atualizações > Lançamentos > Ausências - GPEA240** - Lance a ausência para o funcionário indicado o código cadastrado anteriormente, e informe o início e quantidade de dias do recesso;  
  
![](http://tdn.totvs.com/download/attachments/284879923/image2017-7-19%2013%3A56%3A3.png?version=1&modificationDate=1500484103000&api=v2)  
  
Após isso, calcule a Folha e confira em **Consultas > Cálculos > por Funcionário -** GPEA090, que os dias de recesso estão lançados na folha.  
  
![](http://tdn.totvs.com/download/attachments/284879923/image2017-7-19%2014%3A0%3A28.png?version=1&modificationDate=1500484103000&api=v2)  
  
**Atenção**Conforme Artigo 13 da Lei Nº 11.788 de 25 de setembro de 2008, o recesso será concedido apenas para contratos ou prorrogações assinados a partir de 25 de setembro de 2008 (data da publicação da lei). A Lei assegura ao estagiário, que tem contrato de duração igual ou superior a 1 ano, o período de recesso de 30 dias a ser gozado preferencialmente durante suas férias escolares.

Obs.: os dias de recesso serão concedidos de maneira proporcional, nos casos do estágio ter duração inferior a 1 ano. 

**Importante**O **recesso não tem nenhuma correlação com o benefício de férias,** tampouco altera o vínculo do estagiário com a empresa. Portanto, no cálculo não será aplicado 1/3 sobre o salário e não terá incidência de INSS e FGTS.  
  
Não está previsto em Lei a forma como a bolsa auxílio deverá ser paga, por exemplo, se deve ser antecipada integralmente como as férias.  
  
Visto que o recesso não tem nenhuma correlação com o benefício de férias, nem está descrito na Lei a forma de pagamento, será efetuado pagamento em Folha conforme os dias do período.

**Saiba Mais:**

[RH - Linha Protheus - GPE - Como realizar cadastro de Estagiário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016561192-RH-Linha-Protheus-GPE-Como-realizar-cadastro-de-Estagi%C3%A1rio?source=search)

[RH - Linha Protheus - GPE - Mensagem ao cadastrar estagiário: A Entidade escolhida não possui todos os campos necessários preenchidos, para contemplar o cadastro Informações do Estagiário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403056683287-RH-Linha-Protheus-GPE-Mensagem-ao-cadastrar-estagi%C3%A1rio-A-Entidade-escolhida-n%C3%A3o-possui-todos-os-campos-necess%C3%A1rios-preenchidos-para-contemplar-o-cadastro-Informa%C3%A7%C3%B5es-do-Estagi%C3%A1rio?source=search)

[RH - Linha Protheus - GPE - Alteração no Cadastro de Entidade (Estagiário)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058299813-RH-Linha-Protheus-GPE-Altera%C3%A7%C3%A3o-no-Cadastro-de-Entidade-Estagi%C3%A1rio-?source=search)

[RH - Linha Protheus - GPE - Como alterar a Escola/Entidade de um Estagiário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4424966290711-RH-Linha-Protheus-GPE-Como-alterar-a-Escola-Entidade-de-um-Estagi%C3%A1rio?source=search)

[RH - Linha Protheus - GPE - Calculo para estagiário mensalista](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056843894-RH-Linha-Protheus-GPE-Calculo-para-estagi%C3%A1rio-mensalista?source=search)

[RH - Linha Protheus - GPE - Como renovar contrato de estagiário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052079934-RH-Linha-Protheus-GPE-Como-renovar-contrato-de-estagi%C3%A1rio?source=search)

[RH - Linha Protheus - GPE - eSocial - S-2306 - Como altera data prevista para termino de contrato para estagiário no SIGAGPE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025703533-RH-Linha-Protheus-GPE-eSocial-S-2306-Como-altera-data-prevista-para-termino-de-contrato-para-estagi%C3%A1rio-no-SIGAGPE?source=search)
