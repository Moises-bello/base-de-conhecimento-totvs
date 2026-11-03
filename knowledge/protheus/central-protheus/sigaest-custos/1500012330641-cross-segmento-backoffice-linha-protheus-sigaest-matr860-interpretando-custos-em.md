---
article_id: 1500012330641
category: SIGAEST - CUSTOS
content_hash: 9ddd4e6810415f920dc13b4fd9f8c23ddb75bff0b3eda1c1bd497f439ced3163
fetched_at: '2026-06-28T22:39:00.422927+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR860 - Interpretando
  Custos em Apontamento de Produção (OP)
type: support-article
updated_at: '2026-05-25T16:00:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012330641-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR860-Interpretando-Custos-em-Apontamento-de-Produ%C3%A7%C3%A3o-OP
---

O artigo explica como entender a composição de custos em uma Ordem de Produção no TOTVS Protheus, detalhando o consumo de materiais via estrutura, movimento interno e beneficiamento. Apresenta um exemplo prático com produtos PA105, MP105, MP106 e MP107, mostrando saldos iniciais, requisições e apontamentos, resultando no custo total de R$ 1.436,00 para o produto final. Também destaca parâmetros que influenciam o processo produtivo.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36579449076631) Tempo aproximado para leitura: **00:02:50 min**  
  
**Dúvida**

Como entender a composição de Custos em uma Ordem de Produção para saber se está correta ou não.

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

**Observações:** A partir do release 12.2510 somente é possível utilizando a **CONSULTA SMART VIEW RELAÇÃO POR OP PCPR860 (**[**link**](https://tdn.totvs.com/pages/releaseview.action?pageId=777935258)**)**. No respectivo release relatórios TREPORT serão descontinuados no Protheus.

Nesta documentação abordaremos um cenário prático onde mostraremos como ocorre a apropriação de Custo no apontamento de Produção.

**O que você precisa saber antes da prática:**

Existem 4 (quatro) formas do *Protheus* requisitar um produto para ser consumido em uma OP:

- Via Estrutura (gerando RE1);

- Via Movimento Interno (gerando RE0);

- Via Beneficiamento com OP (gerando RE5).

- Via Movimento Interno **sem agregar custo** (gerando RE9) - Para detalhes desta modalidade, [**clique aqui**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018771732-MP-SIGAEST-Como-N%C3%83O-agregar-custo-da-Mat%C3%A9ria-Prima-MP-em-uma-Produ%C3%A7%C3%A3o-#:~:text=Como%20n%C3%A3o%20agregar%20o%20custo,ordem%20de%20produ%C3%A7%C3%A3o%20(OP)%3F&text=Com%20os%20passos%20abaixo%20conseguiremos,custo%20do%20produto%20na%20OP).)

**Cenário prático:**

Teremos os seguintes produtos:

PA105 - Produto Final (ao qual faremos a abertura da Ordem de Produção);

MP105 - Estará na Estrutura do PA105, sendo 1:1 (1 MP105 é suficiente para montar 1 PA105);  
MP106 - Será requisitado via Movimento Interno contra a OP do PA105;  
MP107 - Será Beneficiamento por OP

OBS: No nosso teste, todos eles ficarão no Armazém 01.

**Custos de cada produto envolvido na Ordem de Produção:**

Saldos Iniciais dos produtos MP105 e MP106. Será feito via MATA220, ou, pelo caminho:

Módulo 04 (Estoque/Custos) ->Atualizações -> Saldos -> Inicial.

**MP105** - Daremos saldo inicial de quantidade **500**, com custo total de **R$ 300,00**, logo nosso Custo Médio Unitário será de **R$ 0,60 (300/500)**.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019670901)

**MP106** - Daremos saldo inicial de **200**, com custo total de **R$ 1.800,00**, logo o nosso Custo Médio Unitário será de **R$ 9,00 (1800/200)**.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019413062)

**MP107** - Entraremos com um Documento de Entrada de quantidade **20**, com custo total de **R$ 500,00**, logo o nosso Custo Médio Unitário será de **R$ 25,00 (500/20)**.

Este será feito mais à frente, no artigo.

**Passo 1 - Realizar a abertura de Ordem de Produção do nosso produto PA105 (OP: Y0188501001)**.

Ela será de quantidade 60.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019677381)

Ao dar um "Sim" na mensagem abaixo, automaticamente será empenhada uma quantidade de 60 do nosso MP105 (que está na estrutura do PA105).

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019671301)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019418862)

**Observação**: Só será gerado o registro RE0 do produto MP105 no momento do Apontamento de Produção, já que está na estrutura do PA105.

**Passo 2 - Fazer um movimento interno de requisição** **de quantidade 100** **do produto MP106 apontando a OP Y0188501001**. Logo, teoricamente, 100 itens ao custo médio unitário de R$ 9,00 totalizará R$ 900,00:

![Fazendo_Req_contra_a_OP_MP106.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019677821)

Resultado após o Movimento:

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019419682)

**Passo 3 - Entrada de nota do produto MP107,** **de quantidade 20****, apontando a OP Y0188501001**. Como o Custo Médio Unitário é de R$ 25,00, logo, multiplicado à quantidade, o custo total do movimento será R$ 500,00

![Beneficiamento_OP_MP107.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019679221)

Resultado:

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019679541)

**Passo 4 - Com isso, já temos o Empenho do MP105, além das requisições dos MP106 e MP107. Com isso, vamos efetuar o Apontamento de Produção.**

Modulo 04 - Estoque/Custos -> Atualizações -> Movimentações -> Internas -> Produções -> Apontar Produção.

![20210526_113752.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019679861)

Neste momento é gerada a RE1 do MP105:

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019421822)

**Passo 7 - Emissão do relatório "Detalhamento de Ordem de Produção" (MATR860)**. Para facilitar a busca, filtraremos apenas pela OP (Y0188501001):

![newgif.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019421622)

**Passo 7 - Exibição dos resultados**

Perceba que, conforme esperávamos, o cálculo para formar a coluna "Custo" é:

Quantidade (D3\_QUANT) x Custo Medio Unitario (B2\_CM1) = Custo do Movimento (D3\_CUSTO)

O **PA105** **receberá** **o custo** **de R$ 1436,00** pois é a soma dos custos dos MPs consumidos. O valor de **R$ 23,93** é basicamente o resultado de Custo Total / Quantidade produzida, ou seja:

**R$1436,00 / 60**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019476462)

Com isso, nossa produto PA105 assume a quantidade e custo conforme a produção:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019476842)

Esse é apenas um exemplo de como pode funcionar o custo produzido.

Existem 3 parametros que tem influencia direta no processo produtivo, que devem ser avaliados particularmente e testado melhor conjunto para sua necessidade.

Sendo eles: [MV\_PRODPR0](https://tdn.totvs.com/pages/releaseview.action?pageId=6085227), [MV\_SEQ300](https://tdn.totvs.com/x/WrHPN) e [MV\_M330PR1](https://tdn.totvs.com/pages/viewpage.action?pageId=401342835)

**Saiba mais:**

[Influência do parâmetro da correta configuração do parâmetro MV\_M330PR1 na proporcionalização do custo nas Produções](https://tdn.totvs.com/pages/releaseview.action?pageId=401342835)

[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)

[Smart View - Estoque (Consultas)](https://tdn.totvs.com/x/M8LrL)

[SIGAEST - Descontinuidade de Relatórios do Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23374418520087-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Descontinuidade-de-Relat%C3%B3rios-do-Estoque)

[Fontes de Relatórios TREPORT Estoque/Custos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058126794-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Fontes-de-relat%C3%B3rios-Estoque-para-altera%C3%A7%C3%A3o-ou-customiza%C3%A7%C3%A3o-fora-do-padr%C3%A3o)
