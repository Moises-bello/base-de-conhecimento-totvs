---
content_hash: 5d16008e2de37aaab9348e9460b44e43bec8ff7a1b7348a56be562117d36ea72
fetched_at: '2026-06-29T00:10:19.435308+00:00'
page_id: '4813669'
product: rm
source: tdn-rm
title: Transferência Direta de Mercadorias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4813669
version: 6
---

BLOCK

Transferência Direta de Mercadorias

FAQ: **Transferência Direta de Mercadorias**

Avaliação

* ***Como Fazer***

Como parametrizar o sistema para fazer transferência direta de movimentos?

* ***Definição do Processo***

As movimentações de transferências de mercadorias são realizadas no estoque do estabelecimento do remetente para o estoque de outro estabelecimento pertencente ao mesmo titular, ou seja, a transferência de mercadorias ocorre entre filiais e locais de estoque da própria empresa.

Tem por finalidade fazer transferência de mercadorias entre filial x local de estoque de forma on-line, ou seja, a quantidade que sair da filial de origem vai entrar automaticamente na filial de destino.

Solução

* ***Parametrizações Necessárias - Totvs Gestão de Estoque, Compras e Faturamento***

Acessar **| Cadastro | Fórmula | Incluir |** e cadastrar fórmula que será utilizada para gravação do custo a ser apresentado no valor financeiro na transferência.

Exemplo:

(KQT\*KPU)

Acessar | **Opções | Parâmetros | RMNucleus |** e selecionar processo onde o tipo de movimento a ser utilizado para este fim foi configurado. A seguir editar tipo de movimento 3.1.XX a ser parametrizado para este fim e informar:

**Etapa Mov – Emitente / Destinatário**

- Emitente: Empresa

- Edição da Filial de Emissão: informar “Edita” para permitir que o usuário preencha os dados da filial, ou “Mostra” se quiser deixar um default preenchido

- Edição do Local de Emissão: informar “Edita” para permitir que o usuário preencha os dados da filial, ou “Mostra” se quiser deixar um default preenchido

- Destinatário: Empresa

- Edição do Local de Destino: informar “Edita” para permitir que o usuário preencha os dados da filial, ou “Mostra” se quiser deixar um default preenchido

**Etapa Mov – Datas**

- Data do Movimento Default: informar qual será a data considerada para afetar estoque e apresentação dos dados da ficha física financeira.

Exemplo:

Se for informado “Data Emissão” significa que as movimentações vão afetar estoque de acordo com a data de emissão apresentada na inclusão do movimento.

**Etapa Item – Preço**

- Edição do Preço: Mostra

- Buscar preço em: **Custo Médio** para considerar o “Custo Médio por Local” ou **Custo Médio Filial** para considerar o “Custo Médio por Filial”. Esta informação será considerada para composição do custo entre as filiais x local de estoque.

Importante:

O campo “Edição do Preço” é parametrizado como “mostra” para evitar que o preço unitário seja alterado manualmente pelo usuário, visto que, será apresentado “custo médio” default.

**Etapa Estoque**

- Efeito sobre os saldos Físico | Saldo Atual: Diminui

- Saldo Financeiro | Efeito sobre o saldo atual: Diminui

- Utilizar Fórmula de Valor Financeiro na Transferência: averiguar a funcionalidade do parâmetro e habilitar de acordo com a necessidade da empresa.

\*\*O exemplo está considerando o saldo 2 para efeito de transferência\*\*

Importante:

- O parâmetro **| Utilizar Fórmula de Valor Financeiro na Transferência |** tem a seguinte funcionalidade:

Parâmetro habilitado: o sistema vai calcular o valor financeiro da entrada da transferência através da fórmula indicada na pasta **| Estoque | Fórmula Valor Financeiro |**

Parâmetro desabilitado: o valor financeiro da entrada da transferência será buscado no valor financeiro do movimento.

- Como se trata de uma movimentação de transferência o custo deve ser o mesmo entre as filias x locais de estoque envolvidos. Diante disto, este exemplo vai considerar o parâmetro **| Utilizar fórmula de valor financeiro na transferência |** habilitado.

**Etapa Fis- Dados**

- Tipo: Saída

**Etapa Fis- Escrituração 1/2**

- Gerar Escrituração: Habilitar

- Tipo de Documento Escrituração: informar o tipo de documento que deve ser apresentado no Totvs Gestão Fiscal

**Etapa Fis- Escrituração 2/2**

- Tipo do Lançamento Fiscal da Transferência: Ambos

* ***Parametrizações Necessárias - Totvs Gestão Fiscal***

Acessar **| Utilitários | Selecionar Filial |** e escolher a filial onde a movimentação será inclusa.

Acessar **| Cadastro | Natureza de Operação | Cadastro de Natureza de Operação |** onde deverá incluir duas naturezas compatíveis com os dados da movimentação de transferência.

- Uma Natureza Fiscal de Entrada Transferência de dentro ou fora do Estado (de acordo com a necessidade da operação)

- Uma Natureza Fiscal de Saída Transferência para dentro ou fora do Estado (de acordo com a necessidade da operação)

Depois de incluir as naturezas, deve editá-las e acessar a aba **| Outros Dados |** onde deve informar:

- Tipo: Transferência

- Nat.Inversa: Para **natureza de saída** deve informar o código da natureza fiscal de entrada que será relacionada a ela. Se tratando de **natureza de entrada** deve informar o código da natureza fiscal de saída que será relacionada a mesma.

Importante:

- O sistema irá utilizar a Natureza Inversa parametrizada na Natureza de Saída do movimento para geração automática do lançamento fiscal de Entrada na Empresa Destino, sendo necessário que as configurações fiscais das naturezas de Entrada e Saída sejam equivalentes.

- Por se tratar de uma transferência direta será gerado apenas um movimento considerando a saída e entrada do saldo do produto em estoque.

* ***Descrição do Processo***

A movimentação 3.1.XX será inclusa como de costume tendo como particularidades o preenchimento dos campos abaixo:

**Aba Identificação:**

- Local de Estoque: informar o local de estoque de origem da mercadoria

- Cód.Filial de Destino: informar o código da filial de destino da mercadoria

- Local de Destino: informar o local de estoque de destino da mercadoria

- Natureza de Operação: informar o código da natureza de operação compatível com estado da filial de destino

* ***Escrituração do Movimento de Transferência***

A movimentação inclusa no tipo de movimento 3.1.XX vai gerar duas escriturações, uma pertinente saída da mercadoria onde será considerada natureza de operação informada na aba | Identificação | do movimento e outra pertinente entrada da mercadoria em seu destino que vai considerar natureza inversa definida na natureza de saída.

Para isto o usuário deverá incluir 02(dois) lotes de escrituração no Totvs Gestão de Estoque, Compras e Faturamento onde vai informar:

Lote para escriturar movimento 3.1.XX - Saída da mercadoria para transferência

- Tipo de Exportação: Normal

- Tipo de Movimento: Saída

- Filial: informar o código da filial onde foi inclusa movimentação de transferência

- Movimentos: informar o código do tipo de movimento 3.1.XX

- Período: informar a data de lançamento em que a movimentação foi inclusa

Lote para escriturar movimento 3.1.03 - Entrada da mercadoria transferida

- Tipo de Exportação: Normal

- Tipo de Movimento: Entrada

- Filial: informar o código da filial de destino da mercadoria

- Movimentos: informar o código do tipo de movimento 3.1.XX

- Período: informar a data de lançamento em que a movimentação foi inclusa

Importante:

O tipo de movimento 3.1.XX vai obedecer parametrização definida no mesmo para geração dos lançamentos fiscais, ou seja, o mesmo tem que estar parametrizado como | Tipo do Lançamento Fiscal da Transferência: Ambos |.

Depois de feita escrituração dos lançamentos para o Totvs Gestão Fiscal deverá acessar o mesmo e selecionar opção **| Utilitários | Selecionar Filial |** onde deve escolher filial de origem da mercadoria. A seguir acessar **| Lançamentos | Manutenção Lançamentos Saída |** e editar o lançamento fiscal. Na aba identificação do lançamento fiscal serão apresentados dados do destinatário e filial da mercadoria.

[![clip_image002](http://lh3.ggpht.com/_G7KXZLoZDsY/TKot31lhgcI/AAAAAAAABkY/2KmeBLygvlA/clip_image002_thumb%5B1%5D.jpg?imgmax=800 "clip_image002")](http://lh3.ggpht.com/_G7KXZLoZDsY/TKot2-oFMwI/AAAAAAAABkU/EnXI1G8wkhs/s1600-h/clip_image002%5B4%5D.jpg)

Para visualizar os dados do lançamento de entrada da transferência deve acessar **| Utilitários | Selecionar Filial |** e escolher filial de destino da mercadoria, o código em questão pode ser visualizado no lançamento anterior. A seguir acessar **| Lançamentos | Manutenção Lançamentos Entrada |** e editar o lançamento fiscal. Na aba identificação do lançamento serão apresentados dados do emitente e filial de origem do lançamento.

[![clip_image004](http://lh4.ggpht.com/_G7KXZLoZDsY/TKot5WB0OiI/AAAAAAAABkg/uh41yfwom44/clip_image004_thumb%5B1%5D.jpg?imgmax=800 "clip_image004")](http://lh3.ggpht.com/_G7KXZLoZDsY/TKot4mhS5RI/AAAAAAAABkc/j1m1ThCRUg8/s1600-h/clip_image004%5B4%5D.jpg)

Para maiores informações:

**COMUNIDADE **[R@Materiais e Finanças](https://totvs.byyou.com/?space=rmateriais)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015
