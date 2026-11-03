---
article_id: 1500001868261
category: SIGAEST - LEGAIS
content_hash: aacb558c7a983633c454cd9543e449316a67d4ae77661b3dfd0a28ff749617be
fetched_at: '2026-06-28T22:38:51.932697+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: MP - SIGAEST - FCI - Protheus está pré-apurando importações antigas. O que
  fazer?
type: support-article
updated_at: '2021-04-28T15:12:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001868261-MP-SIGAEST-FCI-Protheus-est%C3%A1-pr%C3%A9-apurando-importa%C3%A7%C3%B5es-antigas-O-que-fazer
---

**Dúvida**Ao gerar a Pré-Apuração do FCI (FISA061) percebo que na SA8 está trazendo importações antigas que até mesmo já efetuei consumo ou venda. O que fazer para resolver este problema?  
  
**Ambiente**Microsiga Protheus - Estoque - A partir da versão 12.1.25  
  
**Solução**

A pré-apuração do FCI ocorre quando há importação de produto (quando D1\_CLASFIS inicia-se com 1, 2, 3 ou 8) populando a tabela **SA8** a partir do 2° mês após a importação do mesmo caso o seu saldo ainda não tenha sido consumido. 

Porém nos deparamos com alguns casos em que a empresa teve uma compra importada do Produto porém, por algum motivo não tem feito importações por um período, mas ao gerar a SA8 continua gerando a pré-apuração do último mês em que importou.

**Por qual motivo o *Protheus* continua considerando uma importação "antiga" na Pré-Apuração do FCI?**

Tendo como premissa bases legais cujas referências serão disponibilizadas ao final do artigo, quando ocorre um cenário em que um produto não é importado há um certo período ou mesmo deixou de ser importado, **mas que já tenha tido alguma ocorrência de importação**, **ele continuará pré-apurando o FCI com base na informação do último período em que tenha ocorrido a importação**. Ou seja, se o nosso produto MP25 teve importação em 04/2017 e desde então as demais entradas foram feitas nacionalmente, mesmo assim ao gerar a pré-apuração será considerado o último periodo em que teve a importação, ou seja, 04/2017.

Abaixo o trecho extraído do site do Portal da Fazenda de SP (link: <https://portal.fazenda.sp.gov.br/servicos/fci/Paginas/perguntas-frequentes.aspx> -> Parcela Importada)

*"Na hipótese de não ter ocorrido operação de importação ou aquisição no mercado interno de produto com conteúdo de importação no penúltimo período de apuração, para informação do Valor da parcela importada do exterior deverá ser considerado o último período anterior em que tenha ocorrido a operação.*

*​Referências:*

*- Resolução do Senado Federal n.º 13/2012;*

*- Convênio ICMS n.º 38/2013;*

*- Portaria CAT n.º 64/2013."*

**O que fazer caso meu produto deixou de ser importado e agora é adquirido nacionalmente?**

Uma alternativa é trabalhar com dois códigos de produto, sendo um deles com B1\_ORIGEM nacional e outro com B1\_ORIGEM estrangeira. Desta forma conseguirá ter um controle maior principalmente no cenário de um produto que pode ser importado ou adquirido nacionalmente.

**Saiba mais:**

*[MP - SIGAEST - FCI (Ficha de Conteúdo de Importação) - Método 3 - Conceito e Informações](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004679892)*

*[Portal da Fazenda - FAQ FCI](https://portal.fazenda.sp.gov.br/servicos/fci/Paginas/perguntas-frequentes.aspx)*

*[Clique aqui e veja mais artigos sobre Legais/Fiscais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033001-SIGAEST-LEGAIS)*
