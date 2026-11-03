---
article_id: 1500009601821
category: SIGAEST - SALDOS
content_hash: 72e43bdd27fd61f451658a0ce5bbb13a9c0206ba080a82d9d36c3160ce342d08
fetched_at: '2026-06-28T22:39:14.838751+00:00'
product: protheus
section_id: 1500001538801
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Dicas de Analise de
  divergência de Saldo Atual/Posição de Saldo em Estoque
type: support-article
updated_at: '2021-07-15T14:45:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009601821-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Dicas-de-Analise-de-diverg%C3%AAncia-de-Saldo-Atual-Posi%C3%A7%C3%A3o-de-Saldo-em-Estoque
---

**Dúvida**

Como investigar se o saldo do meu produto está correto e onde estaria o erro em caso de divergência?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**O Módulo de Estoque/Custos dispõe de várias formas de analisar o saldo físico de estoque, seja por meio de relatórios, consultas e até mesmo por comandos (por exemplo, o botão [F4] em determinadas rotinas).

Nesta documentação vamos abordar sobre dicas de análise da homogeneidade dos saldos de estoque para os produtos.

**Observação importante - Sempre comparar com ao menos 3 fontes de embasamento**

Se o saldo impresso em um relatório levantar estranheza, a recomendação é sempre comparar com outras fontes base. Vamos elencar aqui neste artigo algumas bases interessantes para análise de saldos:

## **Relatório de Posição de Estoque (MATR260)**

**Caminho:****Módulo 04 - Estoque/Custos -> Relatórios -> Saldos -> Em Estoque Analítico**

Este relatório é um dos mais comuns do Modulo de Estoque/Custos, onde permite o usuário avaliar o saldo atual ou com alguma outra régua (de data ou de fechamento). É de **extrema importância** se atentar na parametrização das perguntas para emitir de forma que a análise dos saldos seja coesa e coerente. Recomendamos fortemente que parametrize com a pergunta "Saldo a Considerar" = Movimento e Data Referência = Mesma data utilizada em outras fontes de análises.

Perguntas como***"Saldo a Considerar", "Data Referência", "Armazém De/Até", "Produto de/até"***, devem ser preenchidas com o máximo critério pois a análise pode ser feita de múltiplos ângulos e dimensões, mas para analisar uma divergência todos os relatórios devem ser parametrizados do **mesmo ângulo**.

Veja maiores detalhes sobre este relatório e principalmente o enfoque na importância da pergunta "Saldo do Produto a Considerar" **[clicando aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018559171)**

![20210611_161938.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4402527134871/20210611_161938.gif)

## **Kardex por Período (MATR900)**

**Caminho:****Módulo 04 - Estoque/Custos -> Relatórios -> Análises -> Movimentações -> Kardex -> Por Período**

Este relatório permite uma análise das movimentações, em ordem cronológica de data ou de custos (a depender se já foi executado o Custo Médio, que é sempre recomendável para Empresas de contabilização de custos de forma offline).

Perguntas como***"Armazém", "Período De/Até", "Produto de/até"***, devem ser preenchidas com o máximo critério pois a análise pode ser feita de múltiplos ângulos e dimensões, mas para analisar uma divergência todos os relatórios devem ser parametrizados do **mesmo ângulo**.

![20210611_162414.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4402527162903/20210611_162414.gif)

## 

## **Botão [F4] em Rotinas**

**Um dos caminhos:****Módulo 04 - Estoque/Custos -> Atualizações -> Cadastros -> Produtos**

Muitas rotinas, como Cadastro de Produtos (MATA010), Movimentações Internas (MATA241), e outras, ao chegar na linha do produto ou no campo "quantidade" e apertar o botão [F4] é apresentado os saldos naquele momento, ali considera-se empenhos, reservas, saldo em poder de terceiros, etc. É uma maneira interessante de analisar com rapidez os saldos, mas lembre-se, nunca se deve tomar como base apenas os saldos que estão no botão [F4] pois ele depende de como é composto o seu saldo. Com isso, temos uma documentação para auxilio na interpretação de cada saldo do [F4], veja **[clicando aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020380572-MP-SIGAEST-Consulta-F4-cadastro-de-produtos)**

O comando [F4] serve apenas para comparação de **saldo atual**

![20210611_162705.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4402522576919/20210611_162705.gif)

## **Análise em Base de Dados**

**Caminho:****Módulo 04 - Estoque/Custos -> Consulta -> Cadastros -> Genéricos**

Para usuários com maiores privilégios de acesso à base de dados (normalmente departamento de T.I), existem tabelas que auxiliam na análise dos saldos. Principalmente as tabelas:

SB2 - Saldo Físico e Financeiro, por meio dos campos B2\_QATU (quantidade atual), B2\_VATU1 (valor financeiro atual) e B2\_CM1 (custo médio unitário do produto atual) e

SB9 - Saldos Iniciais, por meio dos campos

* B9\_QINI (Quantidade Inicial (ou final, em caso de existência de virada de saldos));
* B9\_VINI1 (Saldo Financeiro Inicial (ou final, em caso de existência de virada de saldos)) e
* B9\_CM1 (Custo Médio Unitário Inicial (ou final, em caso de existência de virada de saldos)).

Lembrando que, para uma análise de **saldo atual**, recomendamos utilizar de embasamento a tabela SB2. Se a análise for de **saldo no último fechamento** (comparado aos demais relatórios), utilizar a tabela SB9. **Se a análise for em qualquer data que não seja nem a atual nem a de fechamento, não utilizar estas tabelas para comparação.**

Para saber se houve fechamento ou não, basta analisar se o campo B9\_DATA (Data) possui registro com alguma data. Se houver, é porque houve, naquele dia, um Fechamento de Estoque para aquele produto.

Veja maiores detalhes sobre a tabela SB9 **[clicando aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016346632-MP-SIGAEST-Import%C3%A2ncia-da-Tabela-SB9-Saldos-Iniciais-)**

## **20210611_163607.gif**

Estas são apenas algumas das fontes de análises de saldos atual ou posicional. Tendo sempre como base pelo menos 2 a 3 fontes de análises, com certeza será mais prático de se entender se realmente há uma divergência ou se, de repente, precisa fazer apenas algum ajuste fino de parâmetro (SX6) ou parametrização de algum relatório para que o saldo impresso na tela seja conforme a outra fonte de análise inicial.

**Saiba mais:**

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Dicas de Analise de divergência de Saldo Atual/Posição de produtos com controle de Lote e Endereço](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402435493271)*

*[MP - SIGAEST - Importância da Tabela SB9 (Saldos Iniciais)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016346632-MP-SIGAEST-Import%C3%A2ncia-da-Tabela-SB9-Saldos-Iniciais-)*

*[MP - SIGAEST - Consulta com comando [F4] no Produto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020380572-MP-SIGAEST-Consulta-F4-cadastro-de-produtos)*

*[MP - SIGAEST - MATR260 - Saldo do produto a considerar?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018559171)*

*[Clique aqui e veja mais artigos sobre Saldos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538801-SIGAEST-SALDOS)*
