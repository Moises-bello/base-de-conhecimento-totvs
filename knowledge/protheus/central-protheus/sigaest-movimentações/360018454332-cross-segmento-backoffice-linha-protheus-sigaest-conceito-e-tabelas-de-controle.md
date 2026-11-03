---
article_id: 360018454332
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 8df645081d3d0799c5b75b4579adbc291ce39cb9721d68007a73015fd8be7032
fetched_at: '2026-06-28T22:38:53.974130+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Conceito e tabelas
  de controle de Lote e Endereço no Protheus
type: support-article
updated_at: '2025-06-06T12:07:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018454332-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-e-tabelas-de-controle-de-Lote-e-Endere%C3%A7o-no-Protheus
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19464665209495) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida:**

No que consiste o controle de **Rastreabilidade por Lote** e **Localização por Endereço** e quais as tabelas envolvidas nestes processos no Protheus?

**Ambiente:**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução:**

***Sugestão*:** Assista também o ***WEBINAR*** que apresentamos sobre o **conceito de Lote e Endereço**:

 - O Lote consiste na possibilidade de rastreio de um produto ou grupo de produtos de ponta a ponta, ou seja, desde o seu saldo inicial, suas entradas, saídas e por fim, o seu saldo final. Desta forma ganha-se em controle eficiente dos produtos pertencentes ao lote.

 - No Protheus todo produto que habilitado o controle de Rastro, também vai controlar a Data de Validade do Lote.

 - Já o Endereçamento visa um controle de saldo dos produtos por localizações específicas, desta forma o usuário consegue endereçar produtos para determinados locais e ter um controle de todo do ciclo de estoque dos produtos endereçados.

 - O controle de Rastreabilidade (Lote) e de Localização Física (Endereçamento) são independentes entre si, ou seja, podem ser utilizados em conjunto ou não. Quando ambos são ativados existe uma correlação entre os mesmos.

Abaixo temos uma tabela que descreve de maneira ilustrativa a diferença a nível de tabelas entre Saldo Físico, Saldo por Rastreabilidade e Saldo por Endereço:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101357433)

Tipos de Saldos:

* **Saldo Físico**

O controle para este tipo de saldo, controla a quantidade física disponível no armazém. Seu saldo é alimentado pelos Documentos de Entrada/Saída e pelos Movimentos Internos.

**Tabelas envolvidas:**

* SB9 – Saldos Iniciais
* SB2 – Saldos Físico e Financeiro
* SD1 – Itens da NF de Entrada
* SD2 – Itens da NF de Saída
* SD3 – Movimentos Internos
* SD4 - Bloqueios/Empenhos

* **Saldo por Rastreabilidade**

Utiliza-se o controle para este tipo de saldo (Lote/SubLote) para controlar a rastreabilidade e a data de validade de seus produtos dentro do armazém. Para ativar o Controle de Saldos por rastreabilidade, configure o parâmetro ***MV\_RASTRO*** com o conteúdo igual a **S** pelo Configurador e após esse procedimento, pela rotina Cadastro de Produtos (MATA010) altere o campo Rastro (B1\_RASTRO) para o conteúdo Lote ou SubLote. Ao habilitar o Rastro para os produtos, é necessário também controlar data de validade Lote a Lote.

**Tabelas (e campos) envolvidos:**

* SBJ – Saldos Iniciais por Lote
* SB8 – Saldos por Lote
* SD5 – Requisições por Lote
* SDD - Lotes Vencidos ou Bloqueados
* B8\_EMPENHO - Quantidade empenhada do Lote

* **Saldo por Endereço**

O controle para este tipo de saldo é utilizado quando o cliente quer controlar a Localização Física de seus produtos dentro do armazém. Para ativar o Controle de Saldos por Endereço, configure o parâmetro *MV\_LOCALIZ* com o conteúdo igual a S pelo Configurador. Na sequência pela rotina Cadastro de Produtos (MATA010) altere o campo Contr.Ender (B1\_LOCALIZ) com o conteúdo igual a Sim.

**Tabelas (e campos) envolvidos:**

* SBK – Saldos Iniciais por Endereço
* SBF – Saldos por Endereço
* SDB – Movimentos de Distribuição
* SDA - Saldo a Endereçar
* SBE - Cadastro de Endereços
* SDC - Reserva de endereços no faturamento

**Observação:**

Caso tenha divergências entre as tabelas de saldos de rastro e endereço utilizar o relatório [MATR282.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018463012-MP-SIGAEST-MATR282-Parametriza%C3%A7%C3%A3o-para-identificar-diverg%C3%AAncia-de-saldos-entre-tabelas-SB2-X-SB8-X-SBF)

**Saiba mais:**

*[Documentação completa sobre controle de Rastreabilidade de Produtos no Estoque](https://tdn.totvs.com/pages/releaseview.action?pageId=367232994)*

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
