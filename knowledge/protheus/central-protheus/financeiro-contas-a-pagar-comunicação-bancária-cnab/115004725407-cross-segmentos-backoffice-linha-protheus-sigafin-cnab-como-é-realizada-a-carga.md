---
article_id: 115004725407
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: b4606dcc98d841aa4cb8196cd863e73e05239348cac3ae1f39c80676036aedcc
fetched_at: '2026-06-28T22:37:55.267981+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN  - CNAB - Como é realizada
  a carga de dados das ocorrências CNAB e EXTRATO
type: support-article
updated_at: '2022-06-24T17:03:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115004725407-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CNAB-Como-%C3%A9-realizada-a-carga-de-dados-das-ocorr%C3%AAncias-CNAB-e-EXTRATO
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:05:00min  
  
Dúvida**Como é realizada a carga de dados das ocorrências CNAB e EXTRATO?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - CNAB - Todas as versões

**Solução**A carga de dados é iniciado pelo cadastro de uma subconta na rotina de parâmetros **bancos - FINA130**.

Para que essa carga padrão ocorra é necessário que a rotina parâmetros **BANCOS** - **FINA130** esteja com data de 11/07/2016 ou superior, e não podem existir dados (registros) para o banco nas tabelas **SEJ** e/ou **SEB**. Caso haja dados desse banco nessas tabelas, a carga padrão não é executada, ou seja, são mantidas as configurações já realizadas no Sistema.

Para mais informações, acesse: <http://tdn.totvs.com/display/PROT/FIN0037_CNAB_Carga_de_Dados_Tab_SEB_SEJ>

**Veja mais**

* [Página Centralizadora do CNAB](http://tdn.totvs.com/display/PROT/CNAB)
* [Como Parametrizar o sistema para a geração do CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006611532-MP-SIGAFIN-CNAB-Como-parametrizar-o-sistema-para-gera%C3%A7%C3%A3o-do-CNAB-)
* [Principais mensagens do CNAB](http://tdn.totvs.com.br/pages/viewpage.action?pageId=353280222)
