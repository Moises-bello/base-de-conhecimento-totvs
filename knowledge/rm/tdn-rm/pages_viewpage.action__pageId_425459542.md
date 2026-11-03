---
content_hash: 0f824faa38aa0dccc30a5b177e7086be0ee988597b2f2b44bd733b2300b8d9a2
fetched_at: '2026-06-29T00:09:36.931083+00:00'
page_id: '425459542'
product: rm
source: tdn-rm
title: Backoffice RM x Protheus SigaMNT - Processo de Solicitação de Compra
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459542
version: 2
---

**Backoffice RM x Protheus SigaMNT - Processo de Solicitação de Compra**

---

O Processo de Solicitação de Compras é o processo responsável por efetuar pedido de Insumos  que não possuam estoque e tenham sido inseridos em uma Ordem de Serviço como Insumos previstos. O Processo de solicitação de compra é executado automaticamente quando  uma Ordem de Serviço tem o seu status  alterado para "Liberado", momento esse  em que é executada uma consulta de Saldo em Estoque  de todos os Insumos Previstos, para que futuramente eles possuam um estoque e possam ser sinalizados como Insumos Realizados. Depois de Gerar  a Solicitação de Compra, deve ser criado um Movimento de Solicitação de Compra no Backoffice RM, que fica aguardando  seu faturamento a fim de gerar um Pedido de Compra de Materiais através de seu respectivo movimento. Depois de faturar a compra dos insumos, a quantidade informada na Ordem de Compra é inserida em estoque  possibilitando que a Manutenção de Bens seja efetuada , dando prosseguimento em todo o processo de Ordem de Serviço.  
    
   
    
    
 **Pré-Condições:**

1: Ter cadastrado os Tipos de Movimento :

* Ordem de Manutenção
* Baixa de Estoque
* Acréscimo em estoque
* Solicitação de Compra
* Solicitação de Armazém

2: Incluir uma Ordem de Serviço com Insumos Previstos e com o Status Pendente.

3: Não possuir Saldo em estoque dos Insumos Previstos inseridos na Ordem de Serviço.

4: Configurar o Parametro MV\_ESTNEG.

* N- Não permite Estoque Negativo

5: Configurar o Parâmetro MV\_NGGERSA. Este parâmetro controla  se será gerada ou não Solicitações de Armazém.

* N– Gera Solicitação de compra para quantidade  de insumos superior ao total em estoque.

**Visualizar Solicitação de Compra**

Passo 1: Acesse: RM / Backoffice /Gestão de Estoque, Compras e Faturamento.

Passo 2: Acesse: Acesse:Compras / Solicitação de Compra.

Passo 3: Informe o código do Tipo de Movimento criado para a Solicitação de Compra(1.1.80), o código da Filial e clique em Ok.

Passo 4: Selecione o movimento criado com o status "Pendente" e clique em Editar

Passo 5: O sistema exibe os dados do movimento. Acesse a aba Itens para visualizar os Insumos Previstos informados na O.S para cada uma das Solicitações de Armazém criados. A solicitação de Armazém também é criada com o valor 0.

**Observações :**

Se a Solicitação de Armazém for faturada no Backoffice RM, não deve ser permitido ao Protheus SigaMNT Alterar os Insumos Previstos.

O Faturamento da Solicitação de Armazém obedecerá o tipo de movimento que o usuário informará ao iniciar o processo de Faturamento.
