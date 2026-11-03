---
article_id: 360016789291
category: SIGAEST - CUSTOS
content_hash: f07c7ce4186ac0b57a8de21d6454d9788e59ce04c0f0b99cd4e4c907c3c2241e
fetched_at: '2026-06-28T22:39:00.331558+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Data width error -  Estouro
  de campo de Valor em outras moedas
type: support-article
updated_at: '2025-03-12T12:25:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016789291-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Data-width-error-Estouro-de-campo-de-Valor-em-outras-moedas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30374385690519)** Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Ao executar uma rotina ou relatório é apresentado o error.log - Data Width Error em campo campo de valor em outra moeda. O que fazer? Como limpar os saldos nos campos de moedas que não utilizo.

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

**Procedimento para Validação e Limpeza de Dados em Outras Moedas**

**1. Introdução** O parâmetro `MV_MOEDACM` é utilizado em cenários onde há estouro de campo para moedas diferentes da Moeda 1 ou quando se deseja desativar o cálculo de valores em determinadas moedas nos processamentos para ganho de performance.

Caso existam valores registrados em outras moedas, o correto é efetuar o ajuste de custo nas moedas:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Acerto de Custo dos Produtos em Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057292614-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Acerto-de-Custo-dos-Produtos-em-Estoque)

Mas caso não queira efetivar, devido a não usar a moeda, mas ocorrer um estouro de campo, por conta de alguma digitação da moeda de forma indevida, **nesse caso é necessária a limpeza manual desses campos diretamente na base de dados por meio da ferramenta APSDU**. Ressalta-se que não há rotinas automáticas para a remoção de valores de custos em qualquer moeda.

**2. Procedimento de Limpeza de Dados**

**2.1. Execução da Limpeza**

* A limpeza dos campos das moedas adicionais (Moeda 2, Moeda 3, Moeda 4 e Moeda 5) deve ser realizada diretamente no banco de dados via APSDU.
* Após a remoção dos valores, o parâmetro `MV_MOEDACM` deve ser atualizado para um valor nulo (removendo o padrão "2,3,4,5").
* O sistema não deve conter informações de taxas para essas moedas no momento da abertura.
* Movimentos também não devem ser informados com valores nessas moedas.
* Caso existam registros nos campos mencionados, eles serão validados pelas rotinas do sistema e carregados em outras tabelas.

**2.2. Considerações sobre a Moeda 3**

* A Moeda 3 é utilizada pelo módulo de Ativo Fixo. É necessário cuidado ao manipular seus dados para evitar impactos indevidos.

**3. Validação e Ajuste de Campos**

Para garantir a integridade dos dados, devem ser verificadas as colunas a seguir. Se os valores estiverem muito altos, excedendo o tamanho suportado pela picture, eles deverão ser ajustados. Caso a empresa não utilize custos em outras moedas, os campos deverão ser preenchidos com zero.

**3.1. Campos a serem zerados**

***Tabela SM2***

* M2\_MOEDA2, M2\_MOEDA3, M2\_MOEDA4, M2\_MOEDA5
* M2\_TXMOED2, M2\_TXMOED3, M2\_TXMOED4, M2\_TXMOED5

***Tabela SB9***

* B9\_VINI2, B9\_VINI3, B9\_VINI4, B9\_VINI5

***Tabela SB2***

* B2\_VFIM2, B2\_VFIM3, B2\_VFIM4, B2\_VFIM5
* B2\_VATU2, B2\_VATU3, B2\_VATU4, B2\_VATU5
* B2\_CM2, B2\_CM3, B2\_CM4, B2\_CM5

***Tabela SD2***

* D2\_CUSTO2, D2\_CUSTO3, D2\_CUSTO4, D2\_CUSTO5

***Tabela SD3***

* D3\_CUSTO2, D3\_CUSTO3, D3\_CUSTO4, D3\_CUSTO5

***Tabela SD1***

* D1\_CUSTO2, D1\_CUSTO3, D1\_CUSTO4, D1\_CUSTO5

***Tabela SB6***

* B6\_CUSTO2, B6\_CUSTO3, B6\_CUSTO4, B6\_CUSTO5

***Tabela SC2***

* C2\_VATU2, C2\_VATU3, C2\_VATU4, C2\_VATU5
* C2\_VINI2, C2\_VINI3, C2\_VINI4, C2\_VINI5
* C2\_VFIM2, C2\_VFIM3, C2\_VFIM4, C2\_VFIM5
* C2\_APRATU2, C2\_APRATU3, C2\_APRATU4, C2\_APRATU5
* C2\_APRINI2, C2\_APRINI3, C2\_APRINI4, C2\_APRINI5
* C2\_APRFIM2, C2\_APRFIM3, C2\_APRFIM4, C2\_APRFIM5

***Tabela SBD***

* BD\_CUSINI2, BD\_CUSINI3, BD\_CUSINI4, BD\_CUSINI5
* BD\_CUSFIN2, BD\_CUSFIN3, BD\_CUSFIN4, BD\_CUSFIN5

***Tabela SD8***

* D8\_CUSTO2, D8\_CUSTO3, D8\_CUSTO4, D8\_CUSTO5

**4. Considerações Finais**

* A manipulação de dados deve ser realizada inicialmente em um ambiente de testes.
* Recomenda-se fortemente que um **analista in loco** execute a validação dos dados utilizando a ferramenta APSDU.
* A execução do procedimento deve ser acompanhada por um analista credenciado pela TOTVS, garantindo a integridade dos dados e evitando impactos indesejados no sistema.

Esse procedimento garante que os custos em moedas adicionais sejam tratados corretamente, prevenindo erros de estouro de campo nas mesmas.

**Saiba mais;**

*[MP - SIGAEST - Data Width error - Field: B2\_VATU1 / B2\_VATU2 / B2\_VATU3 / B2\_VATU4 / B2\_VATU5. Como resolver?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003491921-MP-SIGAEST-Data-Width-error-Field-B2-VATU1-B2-VATU2-B2-VATU3-B2-VATU4-B2-VATU5-Como-resolver-)*

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
