---
article_id: 38053881811735
category: Folha Mensal
content_hash: 0e8d77e09647f637a317f7fb31d201ee4e976d320a156d96efc757e76ce606b1
fetched_at: '2026-06-28T22:46:57.971056+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Crédito do Trabalhador - Importar arquivo de competência futura
type: support-article
updated_at: '2026-02-02T12:16:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38053881811735-RH-RM-FOP-Cr%C3%A9dito-do-Trabalhador-Importar-arquivo-de-compet%C3%AAncia-futura
---

![relogio_tempo_leitura_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38053866049431) Tempo aproximado para leitura: 00:10:00 min  
  
**Ocorrência**  
Foi importado o arquivo da competência seguinte e o desconto não está acontecendo. O campo Competência Atual do empréstimo é diferente da competência da folha e por isto o desconto não ocorre.   
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir dos patches:   
  
12.1.2406.287

12.1.2410.258

12.1.2502.160

12.1.2506.105 e superiores  
  
**Causa**  
Foi criado o campo de Competência Atual conforme documentação abaixo.

* [RH - RM - FOP - Crédito do Trabalhador - Campo Competência Atual](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37541406086295-RH-RM-FOP-Cr%C3%A9dito-do-Trabalhador-Campo-Compet%C3%AAncia-Atual)

Como consequência, se a competência da folha for diferente da competência atual do empréstimo, o desconto do Crédito na folha não vai ocorrer.   
  
Com a importação do arquivo da próxima competência, o sistema passa a atualizar automaticamente o campo **Valor da Parcela**, bem como o campo **Competência Atual**. Essa melhoria corrige fragilidades existentes no processo anteriormente adotado.

No modelo anterior, poderiam ocorrer inconsistências, uma vez que o valor da parcela não é controlado pela empresa. De um mês para outro, esse valor pode sofrer variações em função de amortizações, incidência de juros ou outros ajustes contratuais. Como consequência, o desconto realizado na competência corrente poderia ocorrer de forma equivocada, utilizando valores que não correspondiam àquele período.  
Com a implementação do campo **Competência Atual**, o desconto somente será efetuado quando a **Competência do Crédito** e a **Competência da Folha** forem exatamente iguais. Esse controle impede divergências de valores e garante que o desconto seja aplicado apenas no mês correto, promovendo maior aderência entre os dados importados e a folha de pagamento processada.  
  
  
**Provisionamento de Férias**: No que se refere ao provisionamento de férias, o próprio **Manual do Crédito do Trabalhador** estabelece que, caso o arquivo da competência seguinte ainda não esteja disponível, é permitido realizar o provisionamento com base no valor da parcela da competência anterior.  
Como exemplo, considerando que o sistema esteja na competência **01/2026**, mesmo que as férias do colaborador tenham início na competência **02/2026**, o provisionamento poderá ser realizado normalmente. Nesse cenário, o cálculo será efetuado com base no valor da parcela referente à competência **01/2026**, evitando a interrupção do processo por indisponibilidade do arquivo do mês seguinte.  
  
  
Importante: Tanto a equipe de suporte quanto a equipe de produto não recomendam a importação do arquivo do Crédito do Trabalhador antes do fechamento da folha da competência corrente. Essa prática pode ocasionar dois tipos de problemas:

* A não realização do desconto, caso a **Competência Atual** não corresponda à competência da folha; ou
* A aplicação de descontos com valores de parcelas referentes a outros meses, gerando inconsistências nos cálculos.

Observação:  
Por se tratar de um provisionamento, eventuais diferenças de valor — decorrentes do uso da parcela do mês anterior — não geram prejuízo ao colaborador. O valor provisionado é posteriormente devolvido ao funcionário, com o objetivo de recompor e aumentar o valor líquido a receber. Dessa forma, o procedimento minimiza riscos operacionais e evita conflitos de informação entre os valores provisionados e os efetivamente descontados.  
  
**Saiba mais:**  
[RH - RM - FOP - Crédito do Trabalhador - Campo Competência Atual](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37541406086295-RH-RM-FOP-Cr%C3%A9dito-do-Trabalhador-Campo-Compet%C3%AAncia-Atual)

[RH - RM - FOP - Crédito do Trabalhador - Provisionamento de Férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32319832741527-RH-RM-FOP-Cr%C3%A9dito-do-Trabalhador-Provisionamento-de-F%C3%A9rias)
