---
article_id: 4410337291799
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 93f0668935f4bc0c3ab7a52b216318b826e5b568477d61a2af099f31cc482ead
fetched_at: '2026-06-28T22:37:22.869115+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Help A260VLDDATA ao
  realizar Medição Automática CNTA260
type: support-article
updated_at: '2026-02-10T19:31:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410337291799-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Help-A260VLDDATA-ao-realizar-Medi%C3%A7%C3%A3o-Autom%C3%A1tica-CNTA260
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23911890563863) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**

Ao tentar utilizar a rotina de Medição Automático CNTA260 o seguinte HELP : A260VLDDATA

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23911961173527)

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - A partir da versão 25

**Solução**

Uma possibilidade da ocorrência do Help A260VLDDATA ao realizar uma Medição Automática pela rotina Gerar Medições - CNTA260:

1- É quando os registros das tabelas CPD e CN9 referente ao contrato em questão não estão com o mesmo compartilhamento, ficando desta forma com informações diferentes nos campos ***CPD\_FILIAL*** e ***CN9\_FILIAL*** nos registros referente ao contrato em questão.

Dessa forma primeiramente deve-se verificar se o compartilhamento dessas duas tabelas estão da mesma forma (no padrão do sistema elas são Exclusivas):

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410336794135)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410336876951)

Caso no ambiente as tabelas já estejam com compartilhamento iguais, deve-se analisar os registros referentes ao contrato em questão nas tabelas CPD e CN9 se estão com o mesmo conteúdo quanto a Filial.

Verificar também a opção Outras Ações -> Acesso, na parte inferior da tela se há permissão nas planilhas:

- para filial do contrato

- e para o Usuário que esta realizando a medição automática.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410337420311)

Para necessidade de apoio na manutenção na base de dados orienta-se a verificação junto a um analista especialista em loco.

***Obs1:***

Na medição automática o contrato será sempre medido na Filial em que ele é cadastrado.

***Obs2:***

No caso do help A260VLDDATA, com a informação de "***FWNOWIDTH***" e mencionando um campo com as descrição "Desc. Plan." conforme abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38307386978711)

A mensagem de help ***FWNOWIDTH***está relacionada a tentativa de inserção de uma informação em um campo, sendo que essa informação tem um tamanho maior do que o tamanho do campos comporta.  
E no caso no padrão da tela de Medição de Contrato, o campo padrão que possui e Descrição de "Desc. Plan." é o campo ***CXN\_DESCRI***, de descrição do tipo de planilha na medição.

Assim um ponto que pode ser analisado no ambiente em questão, é se os campos de Descrição de Tipo de Planilha de todas tabelas do contrato estão com o mesmo tamanho conforme o cadastro de tipo de planilha, os quais necessitam estar com o mesmo tamanho (no caso o maior tamanho que estiver nos campos) tanto no dicionário como também no banco de dados, verificando assim os campos: ***CNL\_DESCRI***, ***CNA\_DESCRI*** e ***CXN\_DESCRI***.

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Controle de Acesso ao contrato no Gestão de Contratos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016499391-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Controle-de-Acesso-ao-contrato-no-Gest%C3%A3o-de-Contratos?source=search)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
