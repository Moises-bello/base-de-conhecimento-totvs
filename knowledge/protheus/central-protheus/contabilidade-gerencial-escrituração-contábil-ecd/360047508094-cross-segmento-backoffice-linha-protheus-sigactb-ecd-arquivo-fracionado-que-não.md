---
article_id: 360047508094
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 64925072ede099fec3450f5d2788bff20abab42ac10626d0f49c681122b4ae76
fetched_at: '2026-06-28T22:40:44.361201+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECD – Arquivo Fracionado  que
  NÃO seja  Situação Especial '
type: support-article
updated_at: '2023-06-23T18:39:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047508094-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-Arquivo-Fracionado-que-N%C3%83O-seja-Situa%C3%A7%C3%A3o-Especial
---

**Dúvida**

* Como gerar arquivo fracionado para situações onde a empresa possui DATA DE INICIO em período diferente de 01/01 , **NÃO** sendo por situação Especial

**Ambiente**Protheus – Contabilidade – A partir da versão 11.80.

**Solução**

* Realizar a apuração de resultado (CTBA211) no período  que o arquivo será gerado fracionado
* Possuir o Calendário Contábil com o mesmo período
* Ao gerar a revisão da rotina de escrituração contábil deve ser informada a data

**Passos**

**Exemplo : 27/02/2017 a 31/09/2017**

**Apuração anual**

* Apuração deve ser executada de 27/02/2017 a 31/12/2017

[27/02 a 31/03](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049318233-MP-SIGACTB-ECD-Deve-existir-pelo-menos-um-registro-J100-Balan%C3%A7o-e-um-J150-DRE-para-cada-registro-J005-Demonstra%C3%A7%C3%A3o-Cont%C3%A1bil-informado-?source=search) -período não teve receita e despesa Com isso não temos apuração de resultado  
01/04 a 30/06  
01/07 a 30/09  
01/10 a 31/12

* Através da rotina de dados contábeis auxiliares (CTBA007) o sistema gera a data da apuração (Tabela CW0)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360069645034)

**Apuração Trimestral**

Caso a apuração for trimestral será  necessário realizar apuração do período :

Obs: Período de 27/02 a 31/03 não teve receita e despesa Com isso não temos apuração de resultado

Ex.:

* 01/04 a 30/06
* 01/07 a 30/09
* 01/10 a 31/12

* Através da rotina de dados contábeis auxiliares (CTBA007) o sistema gera a data da apuração (Tabela CW0)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070763673)

* Cadastro do calendário  deve ser criado com o período completo de 01/01 a 31/12
* Foi realizado o cadastro  de 01/01 a 31/12

**Calendário quando for apuração Trimestral**

01/01 a 31/03    
01/04 a 30/06  
01/07 a 30/09  
01/10 a 31/12

**Calendário quando for apuração  Anual**

01/01 a 31/01    
01/02 a 29/02  
01/03 a 31/03  
01/04 a 30/04  
01/06 a 31/06  
01/07 a 30/07  
01/08 a 30/08  
01/09 a 30/09  
01/10 a 30/10  
01/11 a 30/11  
01/12 a 30/12

* Preencher os parâmetros abaixo conforme descreve o manual da receita
* Neste exemplo foi informado "Z- normal" , pois não temos situação especial
* Obs: como será descrito ao final dessa documentação no PGE tem a opção "Z-Normal" , porem ao seguir essa passos o sistema irá gerar com o campo em BRANCO
* [Indicador Situação Especial- Campo IND\_SIT\_ESP](https://tdn.totvs.com/pages/releaseview.action?pageId=547876652) (DSERCTR1-26950)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360069740994)

Caso  informe:

* Opção "Z -Normal" o sistema gera erro de [BALANCETE PARCIAL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016597051-MP-SIGACTB-ECD-POR-QUE-OCORRE-VALIDA%C3%87%C3%83O-HELP-BALANCETE-PARCIAL-?source=search) se o cadastro do calendário não estive correto ,  o registro 0000 no campo 11 é gerado o arquivo em branco.
* Quando o parâmetro  ![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070861473)   for preenchido como "Z -Normal" o  calendário deve ser cadastrado com o período de 01/01 a 31/12
* Quando o parâmetro  ![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070861513) for preenchido como 0,1,2,3,4,5 - o  calendário deve ser cadastrado fracionado com isso deve seguir a documentação[Fracionado COM Situação Especial (Extinção,Fusão,Incorporação,Transformação ...)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015908192-MP-SIGACTB-ECD-Arquivo-Fracionado-COM-Situa%C3%A7%C3%A3o-Especial-Extin%C3%A7%C3%A3o-Fus%C3%A3o-Incorpora%C3%A7%C3%A3o-Transforma%C3%A7%C3%A3o-?source=search)
* Foi informado  o parâmetro
* Indicador Inicio do Período?: Opção "1 -Abertura" **![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070861593)**
* Deve informar  o período completo que a empresa possui movimento na CT2, neste exemplo a empresa possui movimento de **27/02 a 31/12**

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360069651114)**

* Caso tenha realizado apuração trimestral deve informar o parâmetro abaixo
* Como apuração deste cenário é trimestral foi informado o parâmetro abaixo **![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070861713)**

* Aqui deve ser informado de**01/01/2017 a 31/12/2017** - conforme o cadastro do calendário **![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070770413)**Com isso o sistema  gerar o arquivo com o campo  em branco , pois no PGE não existe a opção "Z- Normal" **![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070861853)**

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360069741274)

Veja que para o layout 8 o validador também só tem opção em caso de situação especial , com isso deve gerar esse campo em branco conforme exemplo anterior

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070861933)
