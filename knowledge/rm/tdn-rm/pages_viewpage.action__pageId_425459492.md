---
content_hash: 0f676da99cca512f8a3cfe7a3e2c4afc0b20168462cf62afadf632516d032ecb
fetched_at: '2026-06-29T00:09:36.284077+00:00'
page_id: '425459492'
product: rm
source: tdn-rm
title: Backoffice RM x Protheus SigaMNT - Processo Incluir de Ordem de Serviço Corretiva
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459492
version: 3
---

**Backoffice RM x Protheus SigaMNT - Processo Incluir de Ordem de Serviço** **Corretiva**

---

As Ordens de Serviço de Manutenção Corretiva são todos aquelas necessárias para o restabelecimento do pleno funcionamento do Ativo da empresa, quando técnicamente possível e recomendável, com reparos dos defeitos constatados. A execução de serviços de manutenção corretiva.  
   
  
   
**Pré-Condições:**

1: Cadastrar manualmente o DE-PARA de Coligada e Filial RM x Empresas e Filiais Protheus

2: Cadastrar os tipos de movimento :

* Acréscimo em estoque
* Apropriação de Custos
* Baixa de Estoque
* Ordem de Manutenção
* Ordem de Manutenção de Terceiros
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

11: Ter vinculado um Ativo a um Bem no Protheus SigaMNT.

**Executando o Processo:**

Passo 1: Acessar: Protheus SigaMNT / Atualizações/ Ordem de Serviço / Corretiva

Passo 2: Clique em Incluir.

Passo 3: Informar o Bem vinculado ao Ativo.

Passo 4: Preencha os campos, informe o Status "Pendente" e se dejejar inclua os Insumos Previstos. A ordem de serviço pode ser incluída com o Status "Liberado".Se a Ordem de Serviço for criada com o Status "Liberado" pule o passo 5.

Passo 5: Alterar o Status da O.S para "Liberada" ao cadastrá-la,ou acessar a funcionalidade Liberar O.S.

Passo 6: O Protheus SigaMNT executa o processo Consulta de Saldos e custos.

Passo 7: Se a Ordem de Serviço possuir insumos previstos, é incluída uma Solicitação de Armazém ou Solicitação de Compra no Backoffice RM(Ver pré-condições 9 e 10)com os seus valores zerados (0) e contemplando apenas os Insumos Previstos.

Passo  8: Acesse: RM / Backoffice / Gestão de Estoque, Compras e Faturamento / Outras Movimentações

Passo  9: Informe o código do Tipo de Movimento criado para Ordem de Manutenção,Filial e clique em Ok.

Passo 10: Selecione o Movimento de Ordem de Manutenção e clique em Editar. O movimento é criado no Backoffice RM com o status "Em Separação" e exibido sem produtos, mesmo se ela possuir insumos previstos.

Passo 11: Acesse no Protheus SigaMNT a funcionalidade Retorno de O.S para a inclusão de Insumos Realizados e Finalização de Ordem de Serviço .

Passo 12: Execute :

* Finalizar Ordem de Serviço e Converter Insumos Previstos em Insumos Realizados
* Inserir Insumos Realizados

Passo 13: O Protheus SigaMNT executa o processo Consultar Saldos e Custos.

Passo 14: O Protheus envia uma mensagem ao Backoffice RM, que inclui um Movimento de Baixa de Estoque ou informa que o saldo em estoque dos insumos é insuficiente. Se o saldo for insuficiente, é necessário faturar o movimento de Solicitação de Armazém/Compra para um movimento de  Acréscimo em Estoque .

Passo 15: Finalizar a Ordem de Serviço(Se Insumos Previstos foram convertidos em Realizados,o Protheus SigaMNT já disparou o processo de Finalização de Ordem de Serviço)

Passo 16: O Protheus SigaMNT envia uma mensagem ao Backoffice RM vinculando os insumos realizados e calculando o valor da Ordem de Serviço. O status é alterado para "Pendente".

Passo 17: Faturar Movimento de Ordem de Manutenção no Backoffice RM.
