---
article_id: 21487052449687
category: SIGAEST - CUSTOS
content_hash: 5688735d49a281035662db3a642d100b3ca5d0a2ff84c713e35f7af3be844716
fetched_at: '2026-06-28T22:39:00.644070+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como avaliar os custos
  contabilizados no estoque?
type: support-article
updated_at: '2025-03-12T12:22:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21487052449687-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-avaliar-os-custos-contabilizados-no-estoque
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21487052424471) Tempo aproximado para leitura: **00:07:30 min****Dúvida**Como avaliar os custos contabilizados no estoque? Como saber se os custos estão contabilizados corretamente? Como validar se os custos foram gerados para contabilidade?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
  
**Solução**O Protheus dispões de rotinas para efetuar a contaiblização das movimentações, e assim essas movimentações uma vez custeadas, são levadas para uma validação dos lançamentos utilizados, dentro da contabilidade Gerencial (Modulo 34 SIGACTB).

Normalmente se utilizam de relatorios contabeis, para averiguação dos valores contabilizados em conformidade com as LPs (Lançamentos padronizados) utilizados para determinado tipos de movimentações.

Para saber quais LPs são correspondentes a validação do estoque, em relação ao lote contabil de numero 008840, que são avaliados pelo time de Estoque Custos, consulte o boletim a seguir:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Quais os Códigos dos Lançamentos Padronizados do Estoque?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020801392-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Quais-os-C%C3%B3digos-dos-Lan%C3%A7amentos-Padronizados-do-Estoque)

**Quais tipos de contabilização existentes?**

Existem dois tipos de contabilização> ONLINE e OFFLINE

Valide no boletim, qual é o seu método

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Recalculo do custo Médio On-Line (MATA330) e Saldo Atual para Final (MATA350)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007482371-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Recalculo-do-custo-M%C3%A9dio-On-Line-MATA330-e-Saldo-Atual-para-Final-MATA350)

**Como saber se as movimentações do lote 008840 referente ao Estoque Custos, foram levadas para contabilidade?**

A grande dificuldade de avaliação no sentido de contabilização, é o não entendimento das duas pontas, onde podemos afirmar que:

**1-Primeira ponta:** Estoque > movimentos gerados para contabilidade

**2-Segunda ponta:** Contabil > Extração dos dados gerados pelo estoque

**Mas como saber e identificar movimentos calculados que não foram contabilizados?**

Iremos exemplificar aqui, a utilização do lançamento padrão 666 (Requisição para Estoque), essa mesma avaliação vale para todas as outras LPs pertinentes ao lote 008840.

**1 Passo:** A minha LP esta configurada adequadamente para levar os valor desejado durante a contabilização? É importante avaliar, se sua LP esta devidamente configurada para levar os valores a contabilidade, como no exemplo abaixo da LP 666, onde utilizamos uma regra simples:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21488144056599)

Informa os respectivos valores das moedas para os lançamentos contábeis ou uma expressão ADVPL.

Exemplo.  
SE1->E1\_VALLIQ ou SE2->E2\_VALOR - SE2->E2\_IRRF  
O lançamento contábil só será efetuado se pelo menos um dos valores nas Moedas existentes for diferente de zero.  
Se não for informado nenhum conteúdo para um campo de Valor (com exceção da Moeda 1), o SIGACTB irá automaticamente converter o valor tomando como base o Critério de Conversão e o Cadastro de Moedas. Para maiores detalhes vide “Lançamentos Contábeis”. Se forem utilizadas mais que 5 moedas, haverá a necessidade de criar os campos de valor respectivos no Configurador.

**2-Passo:** A movimentação do meu produto, foi custeada no ESTOQUE para o periodo de apuração ao qual estou contabilizando? Normalmente, utiliza-se do relatorio MATR900 para verificar se a movimentação referente a LP foi ou não custeada no Estoque em decorrencia das movimentações, pois esse é o segund passo mais importante "Validar se o teve custo do movimento no estoque".

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR900 - Como configurar corretamente o relatório Kardex para análise de Custos e Movimentações?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011930291-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR900-Como-configurar-corretamente-o-relat%C3%B3rio-Kardex-para-an%C3%A1lise-de-Custos-e-Movimenta%C3%A7%C3%B5es)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21488156363415)

**Após processamento do recalculo de custo médio e contabilização, como eu sei que o movimento foi levado para a contabilidade?**

Conforme informamos anteriormente, usa-se de relatorios contabeis e kardex, para avaliação das movimentações, mas oque fazer se existir custeio no Kardex, mas na contabilidade identificar que não foi levado os valores?

Para isso, é necessario uma avaliação mais tecnica sistemicamente falando, esse processo a seguir é destinado ao time Tecnico do cliente, que tenha permissionamentos a efetuar consulta de dados.

As informações da **tabela CTK (Arquivo de Contra-Prova)** são geradas a partir da contabilização, **os registros gerados ja são o indicador que ocorreu a contabilização.**  
Então se a movimentação em acordo ao lote utilizado e LP usada, estiverem contidos na CTK isso indica que o ESTOQUE ja fez a cargar para envio dos valores para a CONTABILIDADE.

As contabilizações geradas, geram marcações em flags na origem da contabilização que indica a geração da contabilização.

**Mais sobre a CTK**

<http://tdn.totvs.com/pages/releaseview.action?pageId=6068533>

**E como saber se os dados gerados de fato na CTK foram levados para contabilidade?**

Uma vez os dados das movimentações gravados na CTK, ja indica que foi enviado as informações para a contabilização, onde a decorrencia desses valores serão replicados na tabela **CT2(Lançamentos Contábeis)**, é daqui que o contabil irá pega a maioria das informações para entendimento dos valores contabilizados, outra forma é validar se o movimento interno foi preenchido o campo: Data do Lancto. Contábil (D3\_DTLANC)

**CTK do movimento do KARDEX anterior:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21488593566871)

**CT2 do movimento do KARDEX anterior e em relação a CTK:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21488838073623)

Assim é validado o custo gerado no estoque, e se foi levado para contabilidade.

**Então qual a premissa de validar os custos no estoque para a contabilidade?**

Uma vez os dados das movimentações gravados na CTK, a avaliação dos saldos na contabilidade é de responsabilidade do time Contabil, dessa forma duvidas em relação aos valores contabilizados, podera ser avaliado junto ao time PROTHEUS ATIVO E CONTABIL.

**Saiba mais:**

[SIGAEST - Como Contabilizar as Movimentações Internas do Estoque?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405082704791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-Contabilizar-as-Movimenta%C3%A7%C3%B5es-Internas-do-Estoque)

[Clique aqui e veja mais artigos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
