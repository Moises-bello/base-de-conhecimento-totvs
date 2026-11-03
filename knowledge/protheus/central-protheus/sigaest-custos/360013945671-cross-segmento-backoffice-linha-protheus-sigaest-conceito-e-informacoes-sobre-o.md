---
article_id: 360013945671
category: SIGAEST - CUSTOS
content_hash: af3e4fced0b763bb97eb426c54ed77e1790cd5b4147f216825924532384b7e3f
fetched_at: '2026-06-28T22:39:00.313857+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Conceito e informacoes
  sobre o calculo de custo medio
type: support-article
updated_at: '2026-04-13T16:33:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013945671-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-e-informacoes-sobre-o-calculo-de-custo-medio
---

O Recálculo do Custo Médio no Protheus reprocessa movimentos de estoque na sequência correta, atualizando custos e saldos para conferência e contabilização. A rotina ordena entradas antes de saídas, considerando o tipo e nível dos movimentos, garantindo precisão no controle de custos dos produtos.

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28807337709335)** Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**

O que é e como entender o Recálculo do Custo Médio, qual o conceito de custo?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

**Afinal, o que é Custo?**

De acordo com o Dicionário da **APICS (American Production and Inventory Control Society)**, Custos são "dispêndios (consumo/despesas) que são absorvidos ao valor do produto e incorporados no valor dos estoques de produtos acabados." Sendo assim, no Protheus o usuário através do módulo Estoque/Custos consegue efetuar o controle de saldos e custos dos seus produtos em diversas situações do seu negócio, tais como: entrada de produtos, movimentos internos, produções, saída de produtos do estoque, etc.

**Qual o objetivo do Recálculo do Custo Médio?**

A Rotina de Recalculo do Custo Médio tem como objetivo básico reprocessar os movimentos na sequencia considerada correta e gravar os custos no arquivo de Saldos em estoque (SB2) bem como nos arquivos de movimentos, fornecendo desta forma as informações necessárias para conferencia e contabilização de custos.

O grande desafio do processamento do Recálculo do Custo Médio é ordenar os movimentos de forma que sejam satisfeitas as condições exigidas por cada processo no arquivo de trabalho utilizado durante o processamento.

![cm1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39711412747159)

**A rotina de recalculo do custo médio não coloca simplesmente entradas antes de saídas**, verifica também o nível e o tipo dos movimentos efetuados para sequenciar o processamento corretamente. A ideia principal é identificar através da característica do movimento qual a sequência mais adequada.

**Qual a importância da Ordenação dos Movimentos durante o Recálculo do Custo Médio?**

A função primordial da rotina de Recálculo do Custo Médio é reordenar as movimentações de forma que todas as notas de entradas sejam processadas antes das movimentações internas e notas de saídas em um mesmo período.

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como é feita a ordenação dos movimentos após recálculo do custo médio?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17221653862551-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-%C3%A9-feita-a-ordena%C3%A7%C3%A3o-dos-movimentos-ap%C3%B3s-rec%C3%A1lculo-do-custo-m%C3%A9dio)

**Como fazer uma gestão de custos correta para minha empresa?**

[Gestão de Custos: Para que serve, quais as vantagens e dicas](https://www.totvs.com/blog/gestao-industrial/gestao-de-custos/)

**Saiba mais:**

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Perguntas do Recálculo do Custo Médio*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024805291)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR900 - Interpretando o Custo no Kardex antes e depois do Recálculo do Custo Médio*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005781102)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Como extrair o arquivo TRB após executar o custo medio?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011904591-MP-SIGAEST-Como-extrair-arquivo-de-trabalho-TRB-ao-executar-o-Rec%C3%A1lculo-do-Custo-M%C3%A9dio-MATA330-)

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)
