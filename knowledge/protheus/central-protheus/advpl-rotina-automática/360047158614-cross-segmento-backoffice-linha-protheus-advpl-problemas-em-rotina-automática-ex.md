---
article_id: 360047158614
category: ADVPL - Rotina Automática
content_hash: 755c55924801d8475e6a20550aa1a0abf7174481ddf4ad6e91856330be8cb343
fetched_at: '2026-06-28T22:40:24.163205+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Problemas em rotina automática
  (EXECAUTO)
type: support-article
updated_at: '2021-12-29T19:04:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047158614-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Problemas-em-rotina-autom%C3%A1tica-EXECAUTO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Boas praticas na utilização de EXECAUTO  
  
**Ambiente**  
Protheus  – ADVPL – A partir da versão 11.80  
  
**Solução**  
Existem rotinas que podem ser executadas de forma automática, elas podem ser utilizadas via JOB**(agendado)** ou algum processo customizado dentro do sistema e Integrações(**WebServices**).

Porém todos esses modos de utilização informados acima, são enquadrados no escopo de customização, onde a responsabilidade do funcionamento é do desenvolvedor que criou a aplicação que utiliza a execauto.

**Mas e se for apresentado um erro no fonte padrão?**  
Para esses casos, o cliente deve fazer prova de conceito(POC), mais conhecido como teste isolado ou pontual. Basicamente, devemos pegar o exemplo documentado da EXECAUTO que estamos utilizando, criar um fonte independente(.prw) e montar a execauto, informando os dados fixos, de preferencia os mesmos dados que foi simulado o erro.  Se ainda sim o erro for apresentado, pedimos que nos abra uma solicitação informando o erro gerado, com a POC e as informações necessárias para reproduzir o problema.

**Exemplo**

```
aadd(aLinha,{"C7_PRODUTO" ,"PRDT0001",Nil})
```

**Mas e se a rotina não estiver documentada?**Caso você deseja usar execauto de uma determinada, e a mesma não esteja documentada, possivelmente essa rotina não está preparada para ser executada de forma automática. Mas você pode nos abrir uma solicitação para validar se a rotina está ou não preparada para esse procedimento.  
  
**Mas e quando a rotina está em MVC ?**Quando uma aplicação é desenvolvida utilizando-se o conceito de **MVC** e suas classes, pode-se fazer  
uso de seu modelo de dados em outras aplicações, similarmente ao que seria uma rotina automática no  
desenvolvimento tradicional. Porém indicamos que sempre utilizem os exemplos documentados, pois se simplesmente tentar fazer o uso do modelo de dados , pode ocorrer da rotina não estar totalmente no padrão **MVC** e acabar causando erros indesejados ou para casos que a rotina esteja totalmente em **MVC**, pode ocorrer de cair em alguma validação no fonte padrão, desconhecida por parte do cliente  e acabar gerando erros. **Mas e a função FWMVCRotAuto?**Realmente essa função foi criada para ser utilizada em rotinas **MVC**, porém desde **2019**, ela passou a ser de **uso interno TOTVS**, por esse motivo os clientes não devem utilizar em suas customizações.  
  
**Boas praticas:**Evite chamar direto a função da rotina padrão, utilize sempre a função **MSExecauto()**

**Exemplo:**

```
//errado  
MATA120(k,v,w,x,y,z)  
  
//correto  
MSExecAuto({|k,v,w,x| MATA120(k,v,w,x)},1,aCabec,aItens,3)  
  
Obs.: Os exemplos documentados deverão ter o modelo correto
```

Se possível, procure informar o valor do campo com o tamanho exato da **SX3,** exemplo**:**Imagine que o campo **XX\_CPO,** tenha tamanho 8 em sua estrutura, se informar o seu valor com apenas 5 caracteres, pode ocorrer falhas em encontrar o registro na base de dados.

**Exemplo:**

```
// pode ocorrer erros   
aadd(aLinha,{"C7_PRODUTO" ,"P0001",Nil})  
  
//indicado  
aadd(aLinha,{"C7_PRODUTO" ,"P0001   ",Nil})// os espaços serão contados como caracter, como esta gravado no banco
```

Evitar o uso dos comandos de transações ***Begin Transaction/**EndTransaction(****Veja em Saiba Mais****),*** *pois as rotinas já tem seus controles e validações internos, onde não a necessidade de realizar uma nova implementação.* ***Quando necessário a utilização dos comandos de transação, os mesmos serão documentados.***

**Saiba Mais:**  
[MP - ADVPL - Qual a finalidade de uma rotina automática](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021028911)[MP - ADVPL - FUNÇÕES, CLASSES E VARIÁVEIS RESTRITAS AO USO INTERNO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016461772)  
**[MP - ADVPL - BEGIN TRANSACTION](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020775851)**
