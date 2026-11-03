---
article_id: 360028344732
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 69f867d1d9de87ee38a6f407666d43e066ed9e015d9564f5aae74cc867efa273
fetched_at: '2026-06-28T22:42:06.721412+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Tratamento do
  Controle de Crédito de PIS e COFINS na Apuração e geração dos Registros 1100 e 1500
  no Arquivo do EFD Contribuições
type: support-article
updated_at: '2022-08-31T12:37:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028344732-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Tratamento-do-Controle-de-Cr%C3%A9dito-de-PIS-e-COFINS-na-Apura%C3%A7%C3%A3o-e-gera%C3%A7%C3%A3o-dos-Registros-1100-e-1500-no-Arquivo-do-EFD-Contribui%C3%A7%C3%B5es
---

**Dúvida**Como gerar o saldo Credor do PIS e COFINS do período anterior na **Apuração** e gerar os **Registros 1100** e **1500** no **Arquivo do EFD Contribuições**.  
  
**Ambiente**Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**Tratamento dos **Créditos na Apuração:**1º O sistema realiza a tratativa de forma automática, havendo saldo credor de **PIS** e **COFINS** no período anterior, ao processar a **Apuração do PIS e COFINS** (**FISA001**), o sistema carrega os valores para o próximo período.  
Verifique o último mês em que ocorreu o processo corretamente e realize o **processamento da Apuração** de **PIS** e **COFINS** desde este período até o período atual.  
  
Segue exemplo:   
  
Processada a **Apuração** do período de Junho, porém, o sistema não carregou o **saldo credor** do período anterior (Maio). Neste, caso, sugerimos que seja reprocessado o período de Maio até o período atual.

2º Nos casos em que é necessário inserir no Protheus, o **saldo credor de PIS e COFINS** de período anterior, e assim demonstrar no próximo período, realize a inclusão manual do saldo credor pelas rotinas de **Controle de Saldo de Crédito de PIS e COFINS** na **FISA001**.  
  
![](https://totvssuporte.zendesk.com/attachments/token/mY9748JpHLyMh8BxwAN6aVKXQ/?name=inline-1336693805.png)

Atenção: O campo **Reserva Cred** (**CCW\_RESCRE**) deve estar como **2-Não** caso queira utilizar o crédito no próximo período.

![](https://totvssuporte.zendesk.com/attachments/token/ZaF6lATUmRHaUBnsMGSLMTB0W/?name=inline-376299107.png)

3º Quando o **credito** **é maior que o valor da contribuição no período**, o sistema efetua **o abatimento  com o credito anterior informando o mesmo valor da contribuição**:  
  
Segue exemplo:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7598033082391/mceclip6.png)

4º  Os **créditos do período atual e anterior** podem ser **utilizados para abater o valor da contribuição**, entretanto se o credito anterior for suficiente para os abatimentos  de **PIS** e **COFINS**, o sistema não utilizará o **credito atual** e o mesmo **será levado para o próximo período** na linha **(SALDO DE CREDITO A TRANSPORTAR PARA PROXIMO PERIODO)**, no arquivo o credito transportado é levado para próximo período no **campo 18 dos Registros 1100 e 1500.**Segue exemplo:

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7598735212695/mceclip7.png)

**Importante: Para saber a origem do valor do crédito na Apuração, dê um duplo clique em cima do valor da linha de SALDO DE CRÉDITO A TRANSPORTAR PARA PRÓXIMO PERÍODO.**

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7598974137239/mceclip8.png)

5º Quando o valor da **contribuição é maior que os créditos seja anteriores ou atuais**, o sistema gera o **valor a recolher na linha VALOR DA CONTRIBUIÇAO NÃO CUMULATIVA A RECOLHER**. Os valores a recolher geram os **títulos a pagar a Tabela SE2,** é necessário o preenchimento da **aba Apuração em  INFORMAÇÕES DE RECOLHIMENTO DOS TRIBUTOS.**Neste caso, como a **Apuração** ficará com **saldo devedor de PIS e COFINS**, os **Registros 1100 e 1500 não serão gerados.**Segue exemplo:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7597471738135/mceclip3.png)

6º O **valor do Credito** **pode ser preenchido manualmente na opção Controle de saldo de Credito PIS/COFINS**, para utilizar em um determinado período, **sempre deve ser  incluído em um período anterior para utilizar no período posterior**.  
  
Segue exemplo:  
  
**Credito lançado no mês Junho**

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7597518033815/mceclip4.png)

Após, **a geração da apuração do mês 07, o credito é utilizado corretamente**:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7597993019287/mceclip5.png)

​
