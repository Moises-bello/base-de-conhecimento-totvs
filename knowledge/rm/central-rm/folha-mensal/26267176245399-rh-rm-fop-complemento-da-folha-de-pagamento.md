---
article_id: 26267176245399
category: Folha Mensal
content_hash: df351f0c5ccda08145f049c3bb28326259ee04bb8e6dd10588d1d69a1d863b4d
fetched_at: '2026-06-28T22:46:58.144560+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Complemento da Folha de Pagamento
type: support-article
updated_at: '2024-09-11T19:36:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26267176245399-RH-RM-FOP-Complemento-da-Folha-de-Pagamento
---

**Tempo aproximado para leitura: 7min 27sec**Dúvida**Como realizar o complemento da folha de pagamento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento**

**Versão disponível a partir de:**

 - 12.1.2310.245  
 - 12.1.2402.206  
 - 12.1.2406.135  
 - 12.1.2410 e superiores

****Solução****

Nesse processo será feito o  lançamento de Complemento da Folha de Pagamento conforme o artigo nº 27 da Instrução Normativa 2110/2022.

Para utilizar o processo é necessário fazer as seguintes configurações:

* Informar valor no parâmetro geral “Período Complemento Folha ” em “Configurações | Parametrizador | Folha Normal | Geral 2/2” que deve ser maior que 1000 e não pode ser igual a nenhum período do RRA seja Folha/Férias, 13o Salário ou Rescisão.
* Cadastrar em dados do dissídio o tipo de acordo B - Legislação federal, estadual, municipal ou distrital, colocando no campo descrição "§ 3º do art. 27 da IN RFB nº 2.110/22"

Na execução do processo, o usuário deverá: 

* Informar a competência e o período que será complementada
* No lookup “Dados do dissídio/convenção/acordo coletivo” será filtrado para o código do tipo de acordo “B - Legislação federal, estadual, municipal ou distrital” cadastrado no eSocial em Acordo Coletivo/Reajuste por Lei.
* O lançamento do envelope de pagamento será feito na competência atual e no período do campo “Período” no processo de  Complemento Folha de Pagamento. Caso o usuário queira poderá informar um período diferente de 1000 ou necessitar fazer mais de um complemento relacionado ao mesma competência complementada, deverá informar um novo período a ser lançado diferente do existente. Lembrando que este campo dever ser informado a partir de 1000.

Ao executar o processo, os valores serão lançados na Ficha Financeira e também PFVERBASDIS do mês, ano e período informados na competência a ser complementada, para que seja enviado para o eSocial.

**Dica**

Para cancelar o período do complemento da folha de pagamento será necessário selecionar o período do complemento da folha previamente informado nos parâmetros locais e selecionar o mesmo no processo de cancelamento da folha. Ou então cancelar todos os períodos.

**EXEMPLO DE UTILIZAÇÃO:**

* Lançamento do complemento

Lançamento da folha de pagamento em Janeiro:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26284829577879)

* Lançamento da folha de pagamento em Fevereiro:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26284724475543)

Lançamento do complemento da folha de pagamento em Fevereiro referente ao mês de Janeiro:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26284829579159)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26284852470039)

Lançamento da folha de pagamento em Fevereiro:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26284903658263)

**Saiba Mais:**

**[Complemento da Folha de Pagamento](https://tdn.totvs.com/display/public/LRM/Complemento+da+Folha+de+Pagamento)**
