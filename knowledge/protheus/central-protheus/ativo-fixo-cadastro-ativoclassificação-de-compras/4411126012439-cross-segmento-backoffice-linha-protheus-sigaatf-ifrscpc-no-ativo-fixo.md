---
article_id: 4411126012439
category: Ativo Fixo - Cadastro Ativo/Classificação de Compras
content_hash: 00ee6119672e48d3e0e00cdebff2037af0b2a5a3aa5050a479329f44e0dd54f9
fetched_at: '2026-06-28T22:41:48.437042+00:00'
product: protheus
section_id: 1500001547662
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - IFRS/CPC no Ativo fixo
type: support-article
updated_at: '2021-10-29T18:00:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411126012439-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-IFRS-CPC-no-Ativo-fixo
---

**Dúvida**CPCs no ativo fixo: CPC 01, CPC 04, CPC 08, CPC 15, CPC 17, CPC 20, CPC 25, CPC 27, CPC 28 e ICPC 01  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - Ativo Fixo - Todas as versões  
  
**Solução**

No módulo do ativo fixo sempre iremos tratar as CPC´s com um tipo gerencial de ativo (N3\_TIPO) diferente do tipo 01. Isso porque o tipo fiscal = 01 não será alterado devido ao vinculo com a Nota fiscal, CIAP e PIS/COFINS, sendo assim, toda questão de redução ou aumento de Ativo Imobilizado provenientes a aplicação de algum CPC, será tratado via lançamento padrão conforme determinação do contador.

[CPC 01: Redução ao Valor Recuperável de Ativos (IAS 36)](https://tdn.totvs.com/pages/viewpage.action?pageId=62390816)

O Objetivo desta Norma é estabelecer procedimentos que a entidade deve aplicar para assegurar que seus ativos estejam registrados contabilmente por um valor que não exceda seus valores de recuperação.

[ATFA380 Redução ao Valor Recuperável de Ativos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014264292-Cross-Segmento-Backoffice-Linha-Protheus-ATFA012-ATFA380-Valor-recuper%C3%A1vel)

Utilizando a rotina ATFA380 – Redução ao Valor Recuperável de Ativos, informar os dados dos ajustes que devem ser atualizados, lembrando que o Sistema não efetua o cálculo do valor a ser registrado, somente efetua a atualização da ficha de ativos com as informações disponibilizadas pelo usuário.

A rotina ATFA380 possui a funcionalidade de importar um arquivo .CSV com os dados dos bens a serem atualizados.  O layout arquivo .CSV a ser utilizado deve ser obtido através da opção Exportar dessa mesma rotina.

A contabilização da redução ao valor recuperável, bem como dos demais movimentos gerados no ativo pelo registro tipo 10 ou 12 devem ser gerados com um tipo de saldo contábil diferente do saldo fiscal, pois o teste de impairment possui efeito apenas na contabilidade mercantil.

[CPC 04: Ativo Intangível (IAS 38)](https://tdn.totvs.com/pages/viewpage.action?pageId=62391055)

Para permitir uma melhor classificação do patrimônio no ambiente Ativo Fixo foram criadas as seguintes classificações patrimoniais:

* I - Ativo Intangível
* D - Ativo Diferido

Os bens do intangível devem ter sua respectiva classificação fiscal no tipo 01 (Aquisição / Depreciação Fiscal), acrescidos da classificação contábil do tipo 10 (Depreciação Contábil).

Essa classificação pode ser facilitada através da criação de grupos de ativos com a classificação fiscal e gerencial, na rotina de Grupo de Bens (ATFA271)

A contabilização dos itens de tipo 10 (Depreciação Contábil) deve ser feita em um tipo de saldo contábil adequado ao registro das movimentações da contabilidade mercantil, segregado dos registros da contabilidade fiscal.

Através do relatório Posição Valorizada na Data (ATFR072) pode ser emitida uma posição contábil fiscal ou contábil gerencial das fichas de imobilizado.

[CPC 08: Custo de Transação e Prêmios na Emissão de Títulos e Valores Mobiliários ( IAS 32 )](https://tdn.totvs.com/pages/viewpage.action?pageId=63275292)

Para atender essa norma , o custo de transação poderá ser tratado como uma ficha de um ativo, porém com a nova classificação específica com a identificação “T” chamada de “Custos de Transação”  
Com essa classificação é possível diferenciar essas fichas nos processos de contabilização da constituição, além de utilizar os métodos de depreciação disponíveis no ambiente para realizar a amortização desse custo de transação

A amortização do custo de transação entrará na fórmula para o cálculo do custo de empréstimo, tratada na rotina “Assistente de custo de empréstimo

* Cadastro de Ativos (ATFA012)
* Classificação Patrimonial - T - Custo de Transação

[CPC 15: Valor Justo Societário Positivo/Negativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037857373-MP-SIGAATF-CPC15-VALOR-JUSTO-SOCIETARIO-POSITIVO-NEGATIVO?source=search)

Disponíveis os tipos de ativos para o Ativo Fixo (SIGAATF) no atendimento à CPC 15 item 06 do sumário, em conformidade com a Lei 11.638 de Dezembro 2007, que orienta o cliente sobre a reavaliação ao valor justo positivo e/ou negativo societário

* Cadastro de ativo (ATFA012)
* Tipo de ativo 01 (fiscal) e 10 (ou 12)
* Ajuste Valor Justo (ATFA385)

[CPC](https://tdn.totvs.com/pages/viewpage.action?pageId=63275399) [17: Contratos de Construção (IAS 11)](https://tdn.totvs.com/pages/viewpage.action?pageId=63275399)

[ATFA470 - Margem Gerencial](https://tdn.totvs.com/pages/viewpage.action?pageId=403741176)

O objetivo deste Pronunciamento é estabelecer o tratamento contábil das receitas e despesas associadas a contratos de construção que normalmente se caracterizam por ter suas datas de início e término em períodos contábeis diferentes. O ponto central é o reconhecimento da receita e da correspondente despesa ao longo dos períodos de execução da obra nas demonstrações contábeis das contratadas.

 O cadastro de Margem Gerencial tem como finalidade de prover dois tipos de regras para o cálculo da margem a ser aplicada a um bem gerencial (tipo de ativo 10) ou bem de adiantamento gerencial (tipo de ativo 13).

Esse cadastro pode ser utilizado na rotina de aquisição do ativo, onde o sistema irá incluir automaticamente o tipo de ativo 15 que representa a margem gerencial do ativo.

* Cadastro de Ativos (ATFA012)
* Tipo de Margem Gerencial: 15
* Cadastro de Regras de Margem Gerencial (ATFA470)

[CPC 20: Custos de Empréstimos (IAS 23)](https://tdn.totvs.com/pages/viewpage.action?pageId=63275466)

[ATFA480 - Capitalização de Custo de Empréstimo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411571542551-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA480-Capitaliza%C3%A7%C3%A3o-de-Custo-de-Empr%C3%A9stimo-)

Custos de empréstimos que são diretamente atribuídos à aquisição, à construção ou à produção de ativos qualificáveis para a capitalização formam parte do custo destes ativos. Outros custos de empréstimos são reconhecidos como despesas.

Custos de empréstimos são despesas de juros de todas as formas de empréstimos, inclusive mútuos, e outros custos que a entidade incorre em conexão com o empréstimo de recursos, conforme consta do Pronunciamento Técnico CPC 08 Custos de Transação e Prêmios na Emissão de Títulos e Valores Mobiliários.

Ativo qualificável é aquele que, necessariamente, leva um período de tempo substancial para ficar pronto para uso, ou venda pretendidos.

Para realizar o registro da capitalização do custo de empréstimos foi desenvolvida a rotina**Capitalização de Custo de Empréstimo (ATFA480)**

Esta rotina registra os custos de empréstimos nos ativos em andamento do ambiente. Não é calculado de juros e rendimentos de aplicações e contratos de financiamento.

Disponibilizado no Ativo Fixo o **Tipo de Bem 13 - Adiantamento Gerencial**, que permite registrar e gerenciar o valor do bem em formação. A funcionalidade é semelhante ao Tipo de Bem 10 - Gerencial, sendo utilizado apenas caso a ficha do ativo conste o Tipo de Bem 03 - Adiantamento.

Assim como o tipo de bem 03, o tipo 13 – Adiantamento Gerencial, não sofre depreciação no cálculo mensal e na baixa de ativo.

* Cadastro de Ativos (ATFA012)
* Tipo de Adiantamento Gerencial: 13
* Capitalização de Custo de Empréstimo (ATFA480)
* Demonstrativo Capitalização do Custo de Empréstimo (ATFR471)
* Relatório de Processamento da Capitalização do Custo de Empréstimo (ATFR470)

[CPC 25: Provisões, Passivos Contingentes e Ativos Contingentes (IAS 37)](https://tdn.totvs.com/pages/viewpage.action?pageId=63275481)

O objetivo do Pronunciamento Técnico CPC 25 é o de assegurar que sejam aplicados critérios de reconhecimento e bases de mensuração apropriados a provisões, passivos contingentes e ativos contingentes e que seja divulgada informação suficiente nas notas explicativas, para permitir que os usuários entendam a sua natureza, oportunidade e valor.

Esse Pronunciamento Técnico determina o tratamento contábil e os requisitos de divulgação para todas as provisões, passivos e ativos contingentes, exceto: (a) os que resultem de contratos a executar, exceto quando o contrato for oneroso. Contratos a executar são contratos pelos quais nenhuma parte cumpriu qualquer das suas obrigações ou ambas as partes só tenham parcialmente cumprido as suas obrigações em igual extensão. (b) os cobertos por um outro Pronunciamento Técnico.

 Implementada no cadastro de **Ativos (ATFA012)** a opção para incluir novos bens como  **V-Provisão de Despesa** por meio do campo **Classificac.** (N1\_PATRIM) da tabela **SN1 – Ativo Imobilizado**.

V - Provisão de Despesa

Para o registro e controle da provisão de despesa das manutenções entre outras, é possível incluir uma ficha de imobilizado com a classificação V – Provisão de Despesa. Esse bem pode ser incluído de forma independente ou gerado a partir da rotina de apropriação de provisão.

Bens com a classificação V – Provisão de Despesa não sofrem depreciação.

Também disponibilizada para o módulo **Ativo Fixo** **(SIGAATF)**, a opção de seleção de filtro de classificação patrimonial, que facilita a extração e análise de dados, de acordo com a classificação patrimonial dos bens.

* Cadastro de Ativos (ATFA012)
* Classificação Patrimonial: V - Provisão

[CPC 27: Ativo Imobilizado (IAS 16)](https://tdn.totvs.com/pages/viewpage.action?pageId=63275113)

Estabelece o tratamento contábil para ativos, bem como a divulgação das mutações nesse investimento e das informações que permitam o entendimento e a análise desse grupo de contas. Os principais pontos a serem considerados na contabilização dos ativos imobilizados são o reconhecimento dos ativos, a determinação dos valores contábeis e os valores de depreciação e as perdas por desvalorização a serem reconhecidas em relação a eles.

Ao utilizar o tipo **10 - Depreciação Contábil**podem ser configurados os métodos de depreciação normalmente aceitos para demonstrar adequadamente a utilização dos bens pela empresa.

O tipo 01 – Aquisição / Depreciação Fiscal somente aceita os seguintes métodos de depreciação:

* Depreciação Linear
* Depreciação Linear com Valor Máximo de Depreciação

Cadastro de Ativos(ATFA012) - Tipo de depreciação gerencial: 10

* Tipos de depreciação gerencial (ATFA012/ATFA050)
* Baixa de bens com cálculo de depreciação proporcional (ATFA036)
* Processamento: Redução do valor recuperável de ativos ([ATFA380](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014264292-Cross-Segmento-Backoffice-Linha-Protheus-ATFA012-ATFA380-Valor-recuper%C3%A1vel?source=search))
* Relatório: Posição Valorizada na Data (ATFR072)
* Relatório: Demonstrativo de Ficha de Ativos (ATFR033)

[CPC 28: Propriedade para Investimento (IAS 40)](https://tdn.totvs.com/pages/viewpage.action?pageId=63275140)

O objetivo deste Pronunciamento é o de prescrever o tratamento contábil de propriedades para investimento e respectivos requisitos de divulgação.

Propriedade para investimento é o imóvel (terreno ou edifício – ou parte de um edifício – ou ambos) mantido pelo proprietário (ou arrendatário) para obter rendas ou para valorização do capital ou para ambas, e não para uso na produção ou fornecimento de bens ou serviços, para finalidades administrativas ou para venda no curso ordinário do negócio. **A propriedade para investimento é classificada no Ativo Não Circulante, subgrupo Investimentos.**

 Conforme o CPC 28 – Propriedade para Investimento, os bens do ativo imobilizado que se enquadrarem nesta situação devem ter uma classificação contábil adequada que represente que os mesmos estão disponíveis para venda.

Para esta classificação devem ser utilizados os tipos 01 – Aquisição / Depreciação Fiscal e tipo 10 – Depreciação Contábil, de forma a manter as informação do ativo em conformidade com o Fisco e com a contabilidade mercantil.

Também é recomendável o uso do grupo de bens para permitir a seleção dos bens nesta categoria em relatórios, como o Posição Valorizada na Data (ATFR072)

* Cadastro de Ativos - Tipo de depreciação gerencial: 10
* Cadastro de grupos de bens
* Relatório: Posição Valorizada na Data (ATFR072)

[ICPC 01 - Contratos de Concessão (IFRIC 12)](https://tdn.totvs.com/pages/viewpage.action?pageId=63275802)

[Cadastro de Controle de Provisão (ATFA490)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411489237783-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA490-Controle-de-Provis%C3%A3o-Valor-Presente-AVP-)

Esta Interpretação orienta os concessionários sobre a forma de **contabilização de concessões de serviços públicos a entidades privadas.**

Esta Interpretação é aplicável a concessões de serviços públicos a entidades privadas caso:

(a) o concedente controle ou regulamente quais serviços o concessionário deve prestar com a infraestrutura, a quem os serviços devem ser prestados e o seu preço

(b )o concedente controle por meio de titularidade, usufruto ou de outra forma qualquer participação residual significativa na infraestrutura no final do prazo da concessão.

Foi disponibilizado controles no ambiente Ativo Fixo para o tratamento do seguintes elementos da norma:

* Ativos Tangíveis
* Direitos sobre Ativos Intangíveis
* Provisão para manutenção

Importante:

O controle dos ativos financeiros não estão no escopo presente do processo.

A rotina de controle de provisão tem o objetivo o controle dos projetos de manutenção descritos como obrigação nos contratos de concessão.

A rotina de projetos de imobilizados é uma alternativa de função ao controle de provisões de concessões para os cálculos e controle contábil dos projetos conhecidos como obra futura, que consiste na preparação da rodovia para os requisitos mínimos da concessão, definido nos termos de contrato.

Além disso foram criados dois métodos de depreciação que são utilizados nas empresas concessionárias, principalmente concessão de rodovias:

* Método de depreciação por Curva de Demanda
* Método de depreciação por Índice

Funcionalidades Relacionadas

* + [Cadastro de Controle de Provisão (ATFA490)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411489237783-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA490-Controle-de-Provis%C3%A3o-Valor-Presente-AVP-)
  + Demonstrativo Planejamento Provisão (ATFR490)
  + Calculo Mensal (ATFA050)
  + Método de depreciação por Curva de Demanda
  + Método de depreciação por Índice
  + [Controle de Projeto de Imobilizado (ATFA430)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411566751127-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA430-Projeto-Imobilizado)
  + Demonstrativo Depreciação do Projeto 12 Meses (ATFR431)
  + Demonstrativo Depreciação do Projeto (ATFR432)

**Saiba mais**

[CPC - Impacto da convergência contábil IFRS/CPC nos módulos da Controladoria Protheus](https://tdn.totvs.com/pages/viewpage.action?pageId=6068474)

[Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA012 - Controle do Valor residual no Ativo fixo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411220442775-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA012-Controle-do-Valor-residual-no-Ativo-fixo?source=search)

[Metodos de Calculo de depreciação](http://tdn.totvs.com.br/pages/releaseview.action?pageId=6067612)

[Tipos de ativo N3\_TIPO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035878114-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA012-Tipos-de-ativo-campo-N3-TIPO-)

[Cross Segmento - Backoffice Linha Protheus - SIGAATF - CPC 15 Valor justo societario positivo/negativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037857373-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-CPC-15-Valor-justo-societario-positivo-negativo?source=search)

[Cross Segmento - Backoffice Linha Protheus - SIGAATF- ATFA480 - Capitalização de Custo de Empréstimo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411571542551-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA480-Capitaliza%C3%A7%C3%A3o-de-Custo-de-Empr%C3%A9stimo-?source=search)

[Cross Segmento - Backoffice Linha Protheus - SIGAATF - Tipos de Cálculo de Depreciação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028739011-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-Tipos-de-C%C3%A1lculo-de-Deprecia%C3%A7%C3%A3o?source=search)

[Cross Segmento - Backoffice Linha Protheus - ATFA012 - ATFA380 Valor recuperável](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014264292-Cross-Segmento-Backoffice-Linha-Protheus-ATFA012-ATFA380-Valor-recuper%C3%A1vel?source=search)
