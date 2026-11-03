---
article_id: 41122317845655
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 8dad602d7a69b4ee9bca99e5832e81dba758f9a880d235209ae674e5cc595622
fetched_at: '2026-06-28T22:37:21.529418+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como incluir Cronograma
  com parcelas de valores diferentes em si
type: support-article
updated_at: '2026-06-10T18:10:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41122317845655-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-incluir-Cronograma-com-parcelas-de-valores-diferentes-em-si
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41122301533847) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**

Como incluir Cronograma com parcelas de valores diferentes em si

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Solução**

Na inclusão de um contrato no Gestão de Contratos, no padrão da opção de inclusão de Cronograma Financeiro, as parcelas são geradas com valores iguais, dividindo igualmente o valor da planilha pelo número de parcelas informadas no parâmetro *"Quantidade de Parcelas" (CN300CRG06)* da opção de geração do cronograma.  
Uma possibilidade de inclusão do contrato com parcelas diferentes, que pode ser utilizado é:

ser gerado o cronograma com o número de parcelas desejadas, e após gerado com valores iguais, o valores de cada parcela ser alterado conforme a necessidade no campo Vl.Prev.Parc. (***CNF\_VLPREV***).

Importante que ao alterar os valores das parcelas, o montante do cronograma deve estar igual ao Valor Total / Montante da Planilha.  
E quando o Contrato se tornar Vigente os títulos provisórios serão gerados conforme as parcelas do Cronograma Financeiro cadastradas.

***Obs. 1:***

O campo ***CNF\_VLPREV***, deve estar com a configurações de Propriedade = Alterar.

Abaixo imagem das configurações padrões do campo:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41122301534615)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41122301535895)

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41122301536791)

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41122317824791)

Exemplo da Inclusão do Cronograma na Inclusão de um Contrato:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41122317825943)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41122301542551)

Cronograma Gerado com Parcelas iguais:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41122317830167)

Possibilidade de Alteração do campo "***CNF\_VLPREV***" após geração das parcelas:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41122317830807)

Cronograma com valores das parcelas alterados e mantendo os Montantes de Valor da Planilha e do Cronograma iguais, onde pode ser confirmado a inclusão do contrato:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41122317831703)

***Obs. 2:***

Na realização de uma Revisão de Aditivo por exemplo, os valores deste campo ***CNF\_VLPREV*** do valor das parcelas do cronograma podem também ser alteradas conforme a necessidade, sendo que da mesma forma, deve-se manter o montante do cronograma adequado de acordo com o montante/valor total da planilha

***Obs. 3:***

Esta possibilidade de alteração manual do campo ***CNF\_VLPREV*** de Valor Previsto do Cronograma Financeiro, é possível apenas caso o contrato não possua Cronograma Físico, ou seja, tenha sido incluido com a configuração no Tipo de Contrato/Tipo de Planilha com **"Cron. Físico = Não".**

Caso necessário, para maiores dúvidas da melhor forma de configuração do contrato conforme o processo utilizado na empresa, orientamos a verificação junto a um analista especialista em loco para a analise do processo e utilização da melhor configuração do módulo conforme a necessidade.

***Saiba Mais:***

[MP - SIGAGCT - Ponto de Entrada Padrão MVC para a rotina de Manutenção de Contratos CNTA300](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021875031-MP-SIGAGCT-Ponto-de-Entrada-Padr%C3%A3o-MVC-para-a-rotina-de-Manuten%C3%A7%C3%A3o-de-Contratos-CNTA300-?source=search)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
