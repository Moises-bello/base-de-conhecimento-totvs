---
content_hash: b6536b8abbceb122802af1a1cf6a70a7298f23bc0841c9c8584414d545ece4ef
fetched_at: '2026-06-29T00:09:19.349140+00:00'
page_id: '421388844'
product: rm
source: tdn-rm
title: FIN - Controle gerencial
type: documentation
url: https://tdn.totvs.com/display/LRM/FIN+-+Controle+gerencial
version: 3
---

**Definições de orçamento**

Controle orçamentário

* Não utilizar

Sistema não fará controle orçamentário.

* Utilizar nova versão

Sistema fará controle orçamentário utilizando o orçamento antigo.

Descrição do tipo de orçamento

Define nome dado aos campos do orçamento.

* Orçado
* Real
* Opcional 1
* Opcional 2

Usa tabela de grupo orçamentário

Define obrigatoriedade do grupo orçamentário.

**Integração Financeira**

Integrado ao controle orçamentário

Sistema fará controle orçamentário utilizando a nova versão integrada com o TOTVS Gestão de Estoque, Compras e Faturamento.

Data default orçamento no lançamento financeiro

Define qual data será utilizada para afetar o orçamento no lançamento financeiro.

Ação sobre orçamento ao exceder orçamento

* Barra

Ao inserir um lançamento ou extrato que exceda o valor do orçamento, o sistema não permitirá a inclusão do mesmo.

* Avisa

Ao inserir um lançamento ou extrato que exceda o valor do orçamento, o sistema avisará sobre o excedente e permitirá a inclusão do mesmo.

* Bloqueia

Ao inserir um lançamento ou extrato que exceda o valor do orçamento, o sistema deixará o mesmo bloqueado até que o usuário faça uma realocação.

**Observação*:***

Ao marcar o parâmetro 'Bloqueia' será habilitado em Controle Gerencial | Controle Orçamentário os processos de realocação de lançamentos e extratos.

**Centro de custo**

Máscara do centro de custo

Define a máscara do centro de custo.

Exibir centro de custo que não permitem lançamentos

Exibe centros de custo que não permite lançamentos na lista de seleção.

Usa código reduzido

Permite utilizar um código reduzido para o centro de custo.

**Tabelas opcionais**

Usar tabelas opcionais

Define as características gerais das tabelas opcionais e sua obrigatoriedade nos lançamentos e extratos.

Visualizar tabela opcional que  não permita lançamento

Os itens das tabelas opcionais que não permitam lançamentos serão listados na pesquisa.

**Orçamento**

Usa orçamento

Define se será utilizado o orçamento financeiro.

Atualiza valor do orçamento automaticamente

Define que valor realizado do orçamento será atualizado automaticamente através dos lançamentos financeiros.

Usa orçamento hierárquico

Define que o orçamento atualizará os níveis ascendentes automaticamente.

Considera rateio por centro de custo/departamento

Define que o orçamento será atualizado pelo rateio por centro de custo ou departamento.

Atualiza lançamento apenas em orçamento de mesma natureza (pagar/receber)

Define que apenas os lançamentos de mesma natureza (a pagar ou receber) serão atualizados.

Modo de atualização

Define quando a atualização do orçamento ocorrerá (baixa ou inclusão).

Ação nos orçamentos excedidos

Define o procedimento do sistema quando o orçamento exceder (conferir, avisar, barrar ou liberar com senha).

Níveis do orçamento

Número de níveis

Define o número de níveis do orçamento (um ou dois).

* Tabela do nível 1

Define a tabela que será utilizada no primeiro nível (departamento ou centro de custo).

* Tabela do nível 2

  Define a tabela que será utilizada no segundo nível (nenhuma, seção, portador, centro de despesa, natureza de gasto ou contratos vendor).
