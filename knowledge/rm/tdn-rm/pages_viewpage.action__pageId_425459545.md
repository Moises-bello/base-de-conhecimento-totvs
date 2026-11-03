---
content_hash: 567408012e022addfc18d44e1b134f68188a421b45c4e502f49571762ea1446f
fetched_at: '2026-06-29T00:09:36.960864+00:00'
page_id: '425459545'
product: rm
source: tdn-rm
title: Linha RM x Protheus SigaMNT - Processo Solicitações de Armazém
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459545
version: 3
---

**Linha RM x Protheus SigaMNT - Processo Solicitações de Armazém**   
A Solicitação de Armazém é um processo responsávelo por controlar a reserva de materiais, que poderão ser utilizados em uma Ordem de Serviço para a manutenção de Bens das empresas. Ao gerar uma solicitação de Armazém é feita uma verificação do saldo em estoque dos Insumos a utlizar, e possuindo a quantidade informada, é feita uma reserva dos mesmos para possivel utilização futura dentro do Processo de Gerar Ordem de Serviço.  
A Solicitação de Armazém é um processo que ocorre automaticamente, assim que uma Ordem de Serviço no Protheus SigaMNT tem o seu Status alterado para "Liberado".

**Pré-condições :**

**1:** Ter cadastrado os Tipos de Movimento :

* Ordem de Manutenção
* Baixa de Estoque
* Acréscimo em estoque
* Solicitação de Compra
* Solicitação de Armazém

**2:** Incluir uma Ordem de Serviço com Insumos Previstos com o Status **"Liberado".**

**3:** Configurar o Parametro MV\_ESTNEG.

* N- Não permite Estoque Negativo

**4:** Configurar o Parâmetro MV\_NGGERSA. Este parâmetro controla se será gerada ou não Solicitações de Armazém.

* S– Gera Solicitação de Armazém independente do saldo em estoque.

**Visualizar Solicitação de Armazém**

**Passo 1:** Acessar: RM / Backoffice / Gestão de Estoque, Compras e Faturamento / Estoque / Requisição de Materiais.

**Passo 2:** Informar o código do Tipo de Movimento criado para a Solicitação de Armazém, Filial e clicar em Ok.

**Passo 3:** O Movimento de solicitação de Armazém é exibido com o seu valor zerado(0).

**Passo 4:** Selecione o movimento criado com o status "Pendente" e clique em Editar

**Passo 5:** O sistema exibe os dados do movimento. Acesse a aba Itens para visualizar os Insumos Previstos informados na O.S para cada uma das Solicitações de Armazém criados. A solicitação de Armazém também é criada com o valor 0.

**Observações :**

**1-** Se a Solicitação de Armazém for faturada no Backoffice RM, não deve ser permitido ao Protheus SigaMNT Alterar os Insumos Previstos. O Faturamento da Solicitação de Armazém obedecerá o tipo de movimento que o usuário informará ao iniciar o processo de Faturamento.
