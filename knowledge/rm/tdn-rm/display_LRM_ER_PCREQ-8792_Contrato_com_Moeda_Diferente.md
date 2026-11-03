---
content_hash: 6be48c9f590a22a3f6831bfb3505903839447d55ae39f9634e6877aa6e5403bc
fetched_at: '2026-06-29T00:06:24.096711+00:00'
page_id: '224111787'
product: rm
source: tdn-rm
title: ER_PCREQ-8792_Contrato_com_Moeda_Diferente
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-8792_Contrato_com_Moeda_Diferente
version: 59
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Contratos |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | R\_C&P\_TOP010 | **IRM1** | PCREQ-8788 |
| **Requisito1** | PCREQ-8792 | **Subtarefa1** | PDR\_CP\_TOP010-34 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.10 | **Réplica** | Não |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | Pré-Requisitos para melhor entendimento da especificação:  <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.Contrato.aspx> | | |
| **Integração** | TOP x Protheus (Mensagem Única e Stored Procedure) | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Com o objetivo de atender principalmente ao Mercado Internacional (MI), será implementado no TOTVS Obras e Projetos (TOP), no modulo de contratos, o conceito de Moeda do Contrato, que possibilita que um determinado contrato possa trabalhar com valores que serão cotados de forma diferente em relação ao utilizado no projeto, isto é, a moeda do contrato será prioritária em relação à moeda do projeto.

## Definição da Regra de Negócio

A contratação de bens e serviços no Mercado Internacional geram pagamentos e/ou recebimentos em moedas estrangeiras. Dessa forma, é necessário que o módulo de contratos do TOP se adeque à essa necessidade, possibilitando assim, que todos os valores que de alguma forma estão relacionados a um contrato, possam ser tratados considerando a moeda na qual o contrato foi definido, diferente da moeda na qual o projeto foi orçado e planejado. Considerando toda essa premissa, vários pontos no TOP, principalmente no módulo de contratos, deverão ser modificados e essas alterações serão detalhadas a seguir.

**1. Parâmetro para definição de utilização de Moeda no Contrato**

* Deverá ser criado um novo parâmetro de projeto "**Utilizar moeda no contrato**", para que possa ser definido se será permitido, no cadastro de contratos, a informação da moeda do contrato. Este parâmetro estará presente na aba **Geral**nos parâmetros de contrato (Protótipo 01);
* Também deverá ser criado um parâmetro de projeto, que estará habilitado se o parâmetro acima estiver marcado, que define qual será a data de conversão utilizada para a busca da cotação, quando houver necessidade, "**Data Base de Conversão da Moeda**" (Protótipo 01);
* Caso exista algum contrato que já possui alguma moeda definida, esse parâmetro não poderá ser desmarcado e um alerta deverá ser exibido na tela de parâmetros do projeto (Protótipo 02).

**2. Cadastro de Contratos**

* No cadastro de contratos, na tela de edição, deverá ser possível informar a moeda que será adotada no contrato (Protótipo 03);
* Esse novo campo, "**Moeda**", estará disponível para todos os tipos de contratos;
* Essa moeda poderá ser diferente da moeda do projeto;
* Contratos que já possuem tarefas ou insumos associadas não poderão ter a moeda do contrato alterada;

**3. Associação de Itens ao Contrato**

* Na associação de itens (tarefas) ao contrato poderão ser associadas qualquer tarefa da EAP (Estrutura Analítica de Projeto), porém, essa associação será realizada considerando a moeda do contrato. As opções de associação "**Valor Unitário (com BDI)**", "**Custo Unitário**" e "**Nenhum**", estarão desabilitadas quando o projeto utilizar moeda no contrato e a mesma for diferente da moeda do projeto, e a terceira opção estará marcada, pois o **Valor Contratado** deverá ser informado manualmente já na moeda do contrato;
* A descrição das colunas "**Valor Unitário**", "**Custo Unitário**", "**Custo Parcial**" e "**Valor Parcial**" deverão ser alteradas para que apresentem a moeda do projeto e a coluna "**Valor Unitário Contratado**" a moeda utilizada no contrato (Protótipo 04);
* Esse processo deverá continuar a considerar o parâmetro "**Permitir contratação de serviços com valor superior ao orçado (Contratos a Pagar)**", porém, deverá ser considerada uma margem de erro pois será necessário realizar uma conversão de valores para que a validação esteja correta, e nesse caso, pode acontecer de essa mesma conversão não atingir exatamente o valor orçado. Essa conversão citada deverá utilizar o parâmetro **Data Base de Conversão da Moeda** como referência, e deverão ser realizadas duas tentativas de conversão, sendo a primeira, onde a cotação existente tem a moeda do contrato referenciada pela moeda do projeto, como por exemplo U$ 1,00 = R$ 4,00, então o valor associado será convertido. Na segunda maneira, a cotação existente tem a moeda do projeto referenciando a moeda do contrato, assim como, R$ 1,00 = U$ 0,25 convertendo então o valor da tarefa para realizar a validação. A margem de erro deverá considerar o valor convertido somado em mais uma unidade da cotação utilizada, como por exemplo:

                                               

Outro exemplo:

**Moeda do Projeto:** Real (R$), **Moeda do Contrato:** Dólar (U$)  
**Valor Unitário:** R$ 1.000,00, **Valor Contratado:** U$ 256,00  
**Cotação 1:** 1 U$ = 3,90 R$, **Cotação 2:** 1 R$ = 0,25 U$  
**Validação da primeira conversão:** (1.000,00 + 3,90(cotação 1)) maior ou igual a (256,00 X 3,90)  
**Validação da segunda conversão:** (1.000,00 X 3,90) + 0,25(cotação 2) maior ou igual a 256,00                                                              

**3.1. Detalhamento de Itens Contratados**

* + A descrição das colunas "**Valor Unitário Orçado**" e "**Custo Unitário Orçado**" deverão, também, ser alteradas para que apresentem a moeda do projeto e a coluna "**Valor Unitário Contratado**" a moeda utilizada no contrato (Protótipo 04).

**4. Liberação de Período**

* No processo de liberação de períodos, os valores utilizados serão oriundos da medição, seguindo as regras de parametrização de projeto, formulas de contrato, dedução e retenção;
* Deverá ser enviada a moeda do contrato quando liberado para o financeiro;
* Em relação ao reajuste, ao calcular o fator que deverá ser utilizado, a moeda do contrato deverá ser considerada para a aplicação e não a do projeto no caso de ambas serem diferentes;
* Na inclusão de produtos faturados deverá ser realizado um filtro, onde somente os movimentos que possuem a moeda do contrato poderão ter os produtos deduzidos, quando o projeto utilizar moeda no contrato e a moeda for diferente da moeda do projeto. Esse mesmo comportamento deverá ocorrer para o anexo de "**Produtos Faturados no Contrato**";
* Nas descrições dos campos de valores, deverá conter a moeda do contrato (Protótipo 05).

IMPORTANTE

Disponível somente na Integração TOP x Protheus (Mensagem Única).

**5. Gerar integração com Suprimentos/Faturamento**

* No processo de geração de movimento para o suprimentos/faturamento, os valores também são oriundos da medição, não tendo necessidade de conversões;
* A moeda do contrato deverá ser enviada, juntamente com todos os parâmetros e valores que atualmente são enviados para a geração do movimento.

**6. Liberação de Retenção**

* Deverá ser enviada a moeda do contrato quando a retenção for liberada.

IMPORTANTE

Disponível somente na Integração TOP x Protheus (Mensagem Única).

**7. Adiantamento de Contratos**

* A moeda do contrato deverá ser enviada, juntamente com todos os parâmetros e valores que atualmente são enviados na liberação do adiantamento;
* A descrição das colunas de valores deverão ser alteradas para que apresentem a moeda utilizada no contrato.

**8. Atualizar Cronograma pelos Lançamentos da Medição**

* No processo de atualizar cronograma pelos lançamentos da medição, deverá ocorrer a conversão de valores no momento em que os valores são lançados no cronograma em caso de a moeda do contrato ser diferente da moeda do projeto. A data de referência para a conversão será a **Data Início do Período**.

**9. Associar Objetos ao Contrato**

* A associação deverá ser realizada considerando a moeda do contrato. As opções de associação "**Valor Unitário**", "**Custo Unitário**" e "**Nenhum**", estarão desabilitadas quando o projeto utilizar moeda no contrato e a mesma for diferente da moeda do projeto, e a terceira opção estará marcada, pois o **Valor Unitário Contratado** deverá ser informado manualmente;
* A descrição das colunas "**Valor Unitário Orçado**" e "**Custo Unitário Orçado**" deverão, também, ser alteradas para que apresentem a moeda do projeto e a coluna "**Valor Unitário Contratado**" a moeda utilizada no contrato (Protótipo 06);
* Na listagem de insumos o Valor Unitário Contratado, deverá exibir 0(zero), para os insumos que ainda não foram associados.

**10. Pedido de Material / Pedido de Material Extra**

* Para os pedidos de material e material extra deverão ser incluída na visão de itens do pedido, uma coluna "**Moeda**" que indique a moeda do contrato para os itens que estão vinculados à um contrato que possui moeda diferente da moeda do projeto (Protótipo 07);
* Não será necessário separar os movimentos gerados no pedido de acordo com a moeda, pois o próprio processo já agrupa os movimentos separadamente em relação ao contrato vinculado.

**11. Cronograma de Desembolso**

* Ao calcular o cronograma de desembolso considerando contratos, deverá acontecer a conversão do **Valor Unitário Contratado** de cada insumo contratado utilizando o parâmetro **Data Base de Conversão da Moeda** como referência e e também do **Valor Previsto** do contrato, porém nessa conversão deverá ser utilizada a **Data Início** do período do contrato.

**12. Saldo para Fluxo de Desembolso**

* No processo de saldo para fluxo de desembolso, ao obter a natureza orçamentária relacionada ao contrato, o valor medido/liberado ou o valor atual de cada item associado deverá ser convertido para a moeda do projeto, considerando a **Data Início** do período do cronograma como referência, e o mesmo deverá acontecer para o valor do contrato e valor previsto que também são utilizados para o cálculo do fluxo de desembolso.

**13. Insumo Derivado: Derivação de Contratos**

* Para insumo derivado do tipo **receita**, existe a possibilidade de vincular um contrato de serviço de qualquer projeto na regra de derivação. Existem três funções de fórmulas que complementam essa derivação de contratos que deverão ter o retorno dos valores, previsto, medido e liberado, convertidos de acordo com a moeda do contrato em relação à moeda do projeto do insumo. A data base para a conversão deverá ser a **data de início do período** do contrato:
  + VLRPDOCNTPLAN(TIPOBUSCA): Resgata o **valor previsto** do contrato para o período de cronograma;
  + VLRPDOCNTMED(TIPOBUSCA): Resgata o **valor medido** do contrato para o período de cronograma;
  + VLRPDOCNTREAL(TIPOBUSCA): Resgata o **valor liberado** do contrato para o período de cronograma.  
      
    Para um melhor entendimento dessa funcionalidade: <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.InsumoReceita.aspx>

**14. Contratos de Licitação**

* Não será possível criar contratos de licitação com moeda diferente da moeda do projeto pois no processo de **Gerar Contrato** não será possível informar a moeda do contrato.

**15. Relatórios**

* Alguns relatórios deverão ser modificados para que apresentem a moeda do contrato ao lado dos valores que são exibidos, e são eles:
  + **Medição Completa**: Medição Completa e Medição Completa com Detalhamento de Retenção;
  + **Genéricos**: Contratos por Projeto, Itens do Contrato, Relação de Contratos por Projeto, Itens Medidos, Pagamento de Medição, Resumo de Medições do Projeto por Contrato e Evolução Financeira.

**16. Integração TOP x Protheus (Mensagem Única)**

* Na integração TOP x Protheus, serão necessárias algumas alterações nos seguintes itens:
  + **Pedido de Compra**: A mensagem utilizada para essa integração é a ORDER, sendo que o campo CURRENCYCODE já existe na mensagem, porém, do lado Protheus, será necessário analisar a interpretação desse campo para que possa ser inserido no pedido;
  + **Nota Fiscal de Entrada**: A mensagem utilizada é a INVOICE, e será necessário incluir esse novo campo CURRENCYCODE no qual receberá a moeda do contrato que originou o pedido. Do lado Protheus, será necessário ajustar a interpretação desse novo campo para que possa ser inserido na nota;
  + **Liberação de Adiantamento**: As mensagens utilizadas são ACCOUNTRECEIVABLEDOCUMENT e ACCOUNTPAYABLEDOCUMENT, e também já possuem o campo CURRENCYCODE, sendo necessário mapeá-lo para o campo de moeda do contrato;
  + **Liberação de Retenção**: As mensagens utilizadas são ACCOUNTRECEIVABLEDOCUMENTREPLACE e ACCOUNTPAYABLEDOCUMENTREPLACE, e também já possuem o campo CURRENCYCODE, sendo necessário mapeá-lo para o campo de moeda do contrato.

**17. Integração por Stored Procedure**

* Na integração por stored procedure, será necessário realizar alterações nas integrações que envolvem Contratos e Pedido de Material, para que a moeda do movimento seja mapeada e enviada ao Protheus, assim como:
  + **Pedido de Compra**: Deverá ser incluído o campo C7\_MOEDA;
  + **Solicitação de Compra**: Deverá ser incluído o campo CMOEDA;
  + **Contas a Pagar**: Deverá ser incluído o campo CE2\_MOEDA;
  + **Contas a Receber**: Deverá ser incluído o campo CE1\_MOEDA.

**Importante:**

* **Em relação à integração TOP x Protheus, essa funcionalidade de moeda diferente para contratos estará disponível a partir da versão 12.1.10 do TOP e 12.x do Protheus.**
* ****As conversões citadas anteriormente deverão considerar a cotação existente para uma determinada data como por exemplo a "Data Base para Conversão" existente nos parâmetros do projeto. Um exemplo dessa conversão pode ser visualizada a seguir:****

  | Valor a ser convertido | Moeda do Projeto | Moeda do Contrato | Data Base | Cotação | Valor Convertido |
  | --- | --- | --- | --- | --- | --- |
  | 1.500,00 | R$ | U$ | 01/01/2016 | 1,00 U$ = 3,90 R$ | 384,60 U$ |
* **O processo de Atualizar Consumo pela Apropriação (Timesheet) não será alterado pois para atualizar o consumo a apropriação deverá ter a moeda igual à do contrato, porém essa consistência não será realizada;**
* **Algumas funcionalidades importantes do módulo de contratos, não necessitarão de alterações na regra de negócio, pois, trabalham com os valores já devidamente convertidos em relação à moeda do contrato, porém, nos campos onde são exibidos os valores deverá ser incluído, junto à descrição, o texto com a informação da moeda do contrato, assim como:**
  + **Processo de Medição de Item de Contrato;**
  + **Processo de Realinhar Itens Associados ao Contrato;**
  + **Processo de Reajustar Itens Associados ao Contrato;**
  + **Processo de Lançamento de Reajuste Definitivo;**

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Contratos | [Alteração] | [Controle -> Contrato -> Contratos] | - |

## Protótipo de Tela

**Protótipo 01**

********Protótipo 02********

****Protótipo 03****

******Protótipo 04******

********Protótipo 05********

**********Protótipo 06**********

************Protótipo 07************

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
