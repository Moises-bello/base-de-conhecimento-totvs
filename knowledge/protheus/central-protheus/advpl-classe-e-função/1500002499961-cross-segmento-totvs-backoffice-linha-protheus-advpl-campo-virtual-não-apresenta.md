---
article_id: 1500002499961
category: ADVPL - Classe e Função
content_hash: 78638f35799f914eda0b37b3a7b8fd25bdad29c376a930723c9adb388a209f36
fetched_at: '2026-06-28T22:40:14.512967+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Campo virtual não
  apresenta na consulta por coluna utilizando função posicione
type: support-article
updated_at: '2022-01-03T22:06:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002499961-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Campo-virtual-n%C3%A3o-apresenta-na-consulta-por-coluna-utilizando-fun%C3%A7%C3%A3o-posicione
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min****Dúvida**Por que o campo virtual não apresenta na consulta por coluna utilizando a função posicione ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL– A partir da versão 12.1.17  
  
**Solução**Para apresentar o campo na consulta por coluna as considerações na chamada da função **Posicione()** devem ser observadas conforme abaixo:  
1° - Os parâmetros informados na função **Posicione()** não pode conter nenhuma informação direta ou chumbada exemplo: '01', apenas o nome dos campos exemplo: **B1\_COD**.

2° - Deve conter todos os campos referente ao índice selecionado na função **Posicione****()**.

3° - Ao utilizar a função **xFilial()** a mesma deve possuir somente o primeiro parâmetro.

A adição da coluna na pesquisa do *browser*, para ser utilizada, deve-se adequar o uso do **Posicione()** às condições conforme a documentação.  
  
**Saiba mais**  
[Posicione](https://tdn.totvs.com/display/public/PROT/Posicione+com+Campo+Virtual)
