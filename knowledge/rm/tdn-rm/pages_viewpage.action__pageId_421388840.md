---
content_hash: 730b3954c440c15ee21abd34e3a53f0a395fadf24836566e5e5cf5d40fb892e4
fetched_at: '2026-06-29T00:09:19.329106+00:00'
page_id: '421388840'
product: rm
source: tdn-rm
title: FIN - Controle bancário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388840
version: 9
---

**Tabelas opcionais**

Usar tabelas opcionais

Define as características gerais das tabelas opcionais e sua obrigatoriedade nos lançamentos e extratos.

Visualizar tabela opcional que  não permita lançamento

Os itens das tabelas opcionais que não permitam lançamentos serão listados na pesquisa.

**Centro de custo**

Máscara do centro de custo

Define a máscara do centro de custo.

Exibir centros de custo que não permitem lançamentos

Exibe centros de custo que não permite lançamentos na lista de seleção.

Usa código reduzido

Permite utilizar um código reduzido para o centro de custo.

**Opções gerais**

N° de casas decimais

Define o número de casas decimais utilizadas nos processos financeiros.

**Extrato de caixa**

Centro de custo obrigatório

Define a obrigatoriedade de centro de custo em extrato de caixa.

Compensar saque/depósito de transferência separadamente

Define que extratos de saques e depósitos gerados através de transferências bancárias serão compensados separadamente.

Gerar CPMF automaticamente

Define que ao incluir um extrato de caixa manual ou gerar extratos de caixa por outros módulos do sistema, o sistema irá calcular e gerar um extrato de caixa do tipo "Saque CPMF " automaticamente.

Número do documento

* Tamanho

Define o tamanho do número do documento de extrato de caixa.

* Preencher com zeros a esquerda

Define o preenchimento com zeros a esquerda até completar o tamanho do número do documento.

* Copiar ref. Para o número do documento

Define que a referência será copiada para o número do documento nos extratos manuais (depósito manual, saque manual, saque CPMF e transferência).

Fechamento do extrato

Define a data que restringirá a inclusão de extrato. Isso inclui cheques e baixas.

Período inclusão do extrato

Define o período para inclusão de extrato.

Permitir data de emissão posterior à data de compensação no extrato

Define que será permitido incluir extrato com data de emissão posterior à data de compensação no extrato.

**Contab. financeiro**

Tabela default para evento

Define qual será a tabela default de evento: Nenhuma, Seção, Portador, Centro de despesa, Natureza de gasto, Contratos vendor ou Tipo documento.

Tabela opcional de vendor

Define qual será  tabela default de vendor: Nenhuma, Seção, Portador, Centro de despesa, Natureza de gasto ou Contratos vendor.

Copia número contábil sem alfanumérico

Define que o número contábil será copiado considerando apenas os números e desconsiderando as letras.

**Contab. extrato**

Default contábil no extrato

Define o default contábil no extrato de caixa (não contábil, contábil, à contabilizar).

Usar contabilização de mútuo

Define se utilizará os recursos de contabilização de mútuo.

Inverte o default contábil de mútuo para o Extrato de Saque

Determina se a contabilização de mútuo será gerada com as naturezas contábeis invertidas no extrato de saque.

Data default do extrato

* Contabilização

Define data default de contabilização do extrato (sistema, vencimento, emissão ou compensação).

* Estorno

Define data default de estorno (sistema ou contab. extrato).

Evento contábil CPMF

Define evento contábil para CPMF.

Campos do extrato de que afetam a contabilização

Determina os campos que, quando alterados, demandam regeração da contabilização

**Calendário oficial**

Calendário oficial

Define o calendário que será utilizado no sistema. Estes calendários são cadastrados no menu Cadastros | Calendário. O calendário escolhido será utilizado nos lançamentos e nas fórmulas para cálculo de dias úteis.

Considerar sábado como dia útil

Define que o sábado será considerado como dia útil nos processos de manipulação de datas. Este parâmetro não será considerado nas aplicações financeiras, pois não há indexador para sábados.

**Aplicação financeira**

Coligada isenta de cobrança de impostos para aplicação financeira

Define se a coligada será isenta de impostos para aplicação financeira.

Contabiliza provisões

Contabiliza as provisões de IRRF e IOF da aplicação financeira.

Tipo do feriado

Nas datas em que houver feriados deste tipo, a aplicação financeira irá desconsiderar a cotação do dia.

**Conta Caixa**

Permite global

Define se será utilizada a coligada global (coligada = 0) no cadastro de conta Caixa e Conta Corrente. Para uso de Conta Caixa global no sistema, além de definir que ela seja global em seu cadastro, é preciso que esse parâmetro seja marcado. Assim ,as contas caixa globais serão apresentadas em todas as coligadas cadastradas no sistema.

**Gestão de Caixa**

Natureza orçamentária/financeira

Ao efetivar a movimentação registrada na simulação do Gestão de Caixa, o sistema criará extratos correspondentes às transferências. Informe neste campo a natureza orçamentária financeira que será utilizada como default nesses extratos.
