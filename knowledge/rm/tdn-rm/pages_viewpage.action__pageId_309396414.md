---
content_hash: 430ea14e5e138fd7c80882829041bbc152c0d71f9a236e0404f9121cfc63dba4
fetched_at: '2026-06-29T00:08:44.589687+00:00'
page_id: '309396414'
product: rm
source: tdn-rm
title: Gestão de Compras no TOP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=309396414
version: 116
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Suprimentos |
| **Segmento Executor** | Construção & Projetos | | |
| **País** | Brasil | | |
| **Outros** | *Implementação somente para clientes com backoffice Protheus* | | |

   

### Objetivo

Essa implementação tem como objetivo possibilitar aos clientes que possuem o TOP - TOTVS Obras e Projetos integrado ao backoffice Protheus, realizar as Solicitações de Compras e as Cotações de preços diretamente no TOP e através de somente uma negociação de compra junto aos fornecedores ser possível gerar as Ordens de Compra separadamente por local de estoque (centro de custo) no Protheus.

Além disso, os clientes Protheus também passam a poder realizar Solicitações de Cotação, o que não é possível caso a Cotação de Preços seja realizada no Protheus.

## Definição da Regra de Negócio

Após essa implementação, a partir dos Pedidos de Material o TOP irá gerar na aba "Gestão de Compras" as Solicitações de Compra ou  Solicitações de Cotação, conforme definido pelo usuário.

Para esses movimentos será gerada no TOP a Cotação de Preços que é originária do RM Nucleus e, conforme a parametrização do módulo de Cotação, serão geradas as Ordens de Compra no backoffice Protheus.

## 1. Parâmetros:

O cliente irá definir, para cada coligada ou um vez para coligada global, se irá utilizar essa implementação ou se continuará utilizando o modelo padrão (movimentos e cotação apenas no Protheus).

Assim, para que determinada coligada passe a utilizar a rotina de Gestão de Compras no TOP, o usuário deverá incluir o parâmetro de Integração (TOPUSAGESTAOCOMPRA) do tipo ***Lógico*** e deverá selecioná-lo.

Somente com esse campo marcado, o TOP irá habilitar a aba "Gestão de Compras", bem como os parâmetros necessários para definição dessa em "Ambiente | Parâmetros | Construção e Projetos".

Estes parâmetros deverão ser definidos para cada coligada em que o usuário optar por utilizar a Gestão de Compras no TOP. Conforme o padrão dos parâmetros RM, o usuário poderá definir a parametrização em uma coligada, exportar o arquivo XML da mesma e importá-lo nas demais coligadas. 

Estarão visíveis no TOP apenas os seguintes parâmetros do Nucleus:

* 04.06 - Gestão de Compras;
  + 04.06.01 - Solicitação de Compra;
  + 04.06.02 - Cotação (todos os parâmetros).

### 1.1. Solicitação de Compras:

Nos parâmetros da Solicitação de Compra será permitido ao usuário criar os tipos de movimento que serão criados no RM quando da geração de um pedido de material ou de material extra no TOP.

Assim, ao parametrizar o tipo de movimento de Solicitação de Compra ficarão **visíveis** todas as etapas dos parâmetros de um tipo de movimento exceto:

* Mov - Tab - Classificação (Etapa 7 - Movimento - Tabelas de Classificação);
* Mov - Tab - Funcionário (Etapa 8 - Movimento - Tabelas - Funcionários);
* Mov - Tab - Opcional (Etapa 10 - Movimento - Tabelas - Opcionais);
* Mov - Tab - Representantes (Etapa 11 - Movimento - Tabelas - Representantes);
* Mov - Valores Financeiros (Etapa 15 - Movimento - Valores Financeiros);
* Item - Lote/Grade/Num. (Etapa 29 - Item - Lote / Grade Numerada / Número de Série);
* Item - Tab - Classificação (Etapa 30 - Item - Tabelas - Classificação);
* Item - Tab - Opcional (Etapa 32 - Item - Tabelas - Opcionais);
* Item - Tab - Representantes (Etapa 33 - Item - Tabelas - Representantes);
* Item - Tab - Comprador (Etapa 34 - Item - Tabelas - Comprador);
* Todas as Etapas de Estoque:
  + Estoque - Estoque 1/3 (Etapa 40 - Estoque - Estoque);
  + Estoque - Estoque 2/3 (Etapa 41 - Estoque - Estoque);
  + Estoque - Estoque 3/3 (Etapa 42 - Estoque - Estoque);
  + Estoque - Custo (Etapa 43 - Estoque - Custo);
  + Estoque - Separação (Etapa 44 - Estoque - Separação);
  + Estoque - Ressuprimento (Etapa 44 - Estoque - Ressuprimento);
* Orçamento (Etapa 46 - Orçamento);
* Vinculações (Etapa 48 - Vinculações);
* Contabilidade (Etapa 51 - Contabilidade);
* Contratos (Etapa 52 - Contratos);
* Todas as Etapas Fin (Financeiro):
  + Fin - Condições de Pagamento (Etapa 53 - Financeiro - Condições de Pagamento);
  + Fin - Faturamento 1/6 (Etapa 54 - Financeiro - Faturamento);
  + Fin - Faturamento 2/6 (Etapa 55 - Financeiro - Faturamento);
  + Fin - Faturamento 3/6 (Etapa 56 - Financeiro - Faturamento);
  + Fin - Faturamento 4/6 (Etapa 57 - Financeiro - Faturamento);
  + Fin - Faturamento 5/6 (Etapa 58 - Financeiro - Faturamento);
  + Fin - Faturamento 6/6 (Etapa 59 - Financeiro - Faturamento);
* Todas as Etapas Fis (Fiscal):
  + Fis - Natureza (Etapa 60 - Fiscal - Natureza);
  + Fis - Dados (Etapa 61 - Fiscal - Dados);
  + Fis - Escrituração 1/2 (Etapa 62 - Fiscal - Escrituração 1/2);
  + Fis - Escrituração 2/2 (Etapa 63 - Fiscal - Escrituração 2/2);
  + Fis - Tributação - Item (Etapa 64 - Fiscal - Tributação - Item);
  + Fis - Tributação - Movimento (Etapa 65 - Fiscal - Tributação - Movimento);
  + Fis - NF-e (Etapa 66 - Fiscal - Nota Fiscal Eletrônica);
  + Fis - Conhecimento de T (Etapa 68 - Fiscal - Conhecimento de Transporte);
* Manutenção (Etapa 67 - Manutenção);
* Patrimônio (Etapa 69 - Patrimônio);
* Produção (Etapa 70 - Produção);
* Recursos Humanos (Etapa 72 - Recursos Humanos);
* Biblioteca (Etapa 75 - Biblioteca);
* Totvs Colaboração (Etapa 76 - Totvs Colaboração);
* Integração Paradigma (Etapa 77 - Integração Paradigma).

Na etapa Compra/Venda - Outros (Etapa 50 - Compra / Venda - Outros Dados) o campo Tipo do Movimento de Compra (TITMTMV.TIPOMOVCOMPRAS) deverá estar desabilitado e automaticamente preenchido com Solicitação de Compras.

O processo de Cópia de Tipo de Movimento estará disponível.

### 1.2. Cotação:

As seguintes abas/campos não deverão estar **visíveis**, conforme descrito abaixo:

* Na aba "Definições Gerais 2/5" não estarão visíveis os campos:  
  + Permite alterar tipo de movimento ao gerar Ordem de Compra;
  + Usar marca de produto na Cotação.
* Na aba "Movimentos 1/2" não estará visível o campo:  
  + Gera movimento por departamento.
* A aba "Movimentos 2/2" não estará visível;
* Na aba "E-mail" não estarão visíveis os campos:
  + Texto do corpo do email para Ordem de Compra.

## 2. Cadastros:

No TOP em "Cad. Gerais | Tabelas Auxiliares" deverá estar disponível o cadastro de Transportadoras do RM Nucleus.

## 3. Gestão de Compras:

Será criada no TOTVS Obras e Projetos a aba Gestão de Compras, que conterá os seguintes ícones (processos) do Nucleus:

* Solicitação de Compra;
* Cotação.

### 3.1. Solicitação de Compras:

Permitirá os procedimentos normais de uma Solicitação de Compras do TOTVS Gestão de Estoque, Compras e Faturamento.

Na tela das Solicitações de Compras, não devem  estar visíveis os seguintes Anexos :

* Log de Comparação de Impostos do Totvs Colaboração;
* NFS-e (Notas Fiscais Eletrônicas Municipais.

A Solicitação de Compra somente poderá ser faturada/recebida para o tipo de movimento configurado na integração com o Protheus. 

### 3.2. Cotação:

Seguirá todos os procedimentos normais do TOTVS Gestão de Estoque, Compras e Faturamento, conforme parametrização efetuada.

### 3.3. Ordens de Compra:

Para as Ordens de Compra, no TOP não será permitido editar e nem realizar nenhum processo, ou seja, as Ordens de Compra poderão apenas ser visualizadas através do rastreamento de movimentos da tela da Solicitação de Compra.

Não será permitido inserir item  em uma Ordem de Compra já existente.

Para excluir o movimento de Ordem de Compras e o pedido no Protheus, será necessário primeiramente realizar o **cancelamento deste movimento no RM** e em seguida **excluí-lo para que o processo seja executado por completo.**

Após concluir a exclusão por completa o pedido de compra será excluído no Protheus através da mensagem com a Transação**ORDER** e Evento **DELETE.**

A Solicitação de Compras (movimento inicial) terá seu status retornado para **PENDENTE** e poderá ser ajustada.  
Caso deseje cancelar/excluir também a SC, será necessário que sejá feita a exclusão do movimento através do pedido de material no TCOP.

**Importante:**

No TCOP - TOTVS Construção Obras e Projetos em **Cad. Gerais - Tabelas Auxiliares** deverá estar disponível o cadastro de **Transportadoras do RM Nucleus.**

Maiores detalhes sobre esse processo estão na seguinte FAQ:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/17916805761431>

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
