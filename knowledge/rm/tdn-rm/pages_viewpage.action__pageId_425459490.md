---
content_hash: 2a730aa1077fab4cd93e9e98cba1eb980a276030e5eff165f64c4af941cad1d7
fetched_at: '2026-06-29T00:09:36.264618+00:00'
page_id: '425459490'
product: rm
source: tdn-rm
title: Backoffice RM x Protheus SigaMNT - Processo Incluir de Ordem de Serviço Manual
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459490
version: 2
---

**Backoffice RM x Protheus SigaMNT - Processo Incluir de Ordem de Serviço** **Manual**

---

A funcionalidade O.S Manual permite gerar Ordens de Serviço Preventivas para uma manutenção de um Ativo da empresa.

O objetivo da Manutenção Preventiva é que não ocorra uma parada inesperada do equipamento, que muitas vezes vem a acontecer devido ao desgaste de peças e acessórios.

Ao executar uma manutenção preventiva, é possivel garantir uma maior disponibilidade do equipamento para análises e também a comprovação de que o instrumento está funcionando de acordo com as especificações do fabricante.

   
 **Pré-Condições:**

1: Cadastrar manualmente o DE-PARA de Coligada e Filial RM x Empresas e Filiais Protheus

2: Cadastrar os tipos de movimento :

* Acréscimo em estoque
* Apropriação de Custos
* Baixa de Estoque
* Ordem de Manutenção
* Solicitação de Armazém
* Solicitação de Compra

3: Sincronizar os Bens (Ativos Fixos) que sofrerão as manutenções.

4: Sincronizar os Locais de Estoque dos produtos a utilizar como Insumos

5: Sincronizar os Produtos / Serviços  que serão utilizados como Insumos.

6: Sincronizar o  Projeto de manutenção  e suas Tarefas.

7: Sincronizar  as Unidades de Medida.

8: Sincronizar os Centros  de Custos.

9: Configurar o Parametro **MV\_ESTNEG** que controla se a integração permitirá estoque negativo .

10: Configurar o Parâmetro **MV\_NGGERSA**. Este parâmetro controla  se será gerada ou não Solicitações de Armazém.

* N–Gera solicitação de armazém e solicitação de compra para a quantidade de insumo excedida
* S– Gera Solicitação de Armazém

11: Ter vinculado um Ativo a um Bem no Protheus SigaMNT. 12: Ter incluído uma Manutenção para o Bem  no Protheus SigaMNT.

**Executando o Processo:**

Passo 1: Acessar: Protheus SigaMNT / Atualizações/ Ordem de Serviço / Manual

Passo 2: Selecione a manutenção do Bem.

Passo 3: Clique  em Incluir.

Passo 4: Preencha os campos, informe o Status "Pendente" e se dejejar inclua os Insumos Previstos. A ordem de serviço pode ser incluída com o Status "Liberado".Se a Ordem de Serviço for criada com o Status "Liberado" pule o passo 5.

Passo 5: Alterar o Status da O.S para "Liberada" ao cadastrá-la,ou acessar a funcionalidade Liberar O.S.

Passo 6: O Protheus SigaMNT executa o processo Consulta de Saldos e custos.

Passo 7: Se a Ordem de Serviço possuir insumos previstos, é incluída uma Solicitação de Armazém ou Solicitação de Compra no Backoffice RM(Ver pré-condições 9 e 10)com os seus valores zerados (0) e contemplando apenas os Insumos Previstos.

Passo  8: Acesse: RM / Backoffice / Gestão de Estoque, Compras e Faturamento / Outras Movimentações

Passo  9: Informe o código do Tipo de Movimento criado para Ordem de Manutenção,Filial e clique em Ok.

Passo 10: Selecione o Movimento de Ordem de Manutenção e clique em Editar. O movimento é criado no Backoffice RM com o status "Em Separação" e exibido sem produtos, mesmo se ela possuir insumos previstos.

Passo 11: Efetuar o Retorno de O.S para a inclusão de Insumos Realizados e Finalização de Ordem de Serviço .

Passo 12: O Protheus SigaMNT executa o processo Consultar Saldos e Custos.

Passo 13: O Protheus envia uma mensagem ao Backoffice RM, que inclui um Movimento de Baixa de Estoque ou informa que o saldo em estoque dos insumos é insuficiente. Se o saldo for insuficiente, é necessário faturar o movimento de Solicitação de Armazém/Compra para um movimento de  Acréscimo em Estoque .

Passo 14: Finalizar a Ordem de Serviço(Se Insumos Previstos foram convertidos em Realizados,o Protheus SigaMNT já disparou o processo de Finalização de Ordem de Serviço)

Passo 15: O Protheus SigaMNT envia uma mensagem ao Backoffice RM vinculando os insumos realizados e calculando o valor da Ordem de Serviço. O status é alterado para "Pendente".

Passo 16: Faturar Movimento de Ordem de Manutenção no Backoffice RM.
