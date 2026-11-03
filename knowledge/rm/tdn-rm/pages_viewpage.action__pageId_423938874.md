---
content_hash: 358a5b216f3f3e635b0753b8764fb035307bcb10434c88150ea89c785e0e0061
fetched_at: '2026-06-29T00:09:29.311943+00:00'
page_id: '423938874'
product: rm
source: tdn-rm
title: Realocação Orçamentária de Movimentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938874
version: 5
---

**Descrição do Processo**

Ao gerar um movimento que afete o orçamento e não possui verba suficiente para o valor solicitado e que esteja configurado para bloquear ao exceder o orçamento (Ambiente – Parâmetros – Gestão de Estoque, Compras e Faturamento – Editar tipo de movimento – Orçamento – Ação ao exceder o orçamento), ao salvá-lo, o movimento ficará com o status bloqueado. Este movimento não poderá ser recebido gerando outro movimento, ficará aguardando até que seja liberado pelo assistente de realocação orçamentária.  
Na realocação orçamentária será apresentada uma grid com todos os movimentos bloqueados.  
Para desbloquear um movimento, deve selecioná-lo na lista, processos, Realocação Orçamentária de Movimentos.  
Após selecionar os centros de custos que deseja desbloquear, e clicar no botão avançar, é apresentada uma tela com as opções de realocação (Centro de Custo – Período – Natureza Orçamentária – Grupo Orçamentário \*) respeitando as regras definidas no perfil do usuário.

**Níveis de realocação para usuários:**

1. Realoca entre Naturezas do Centro de Custo.
2. Realoca entre Naturezas e Centros de Custo que está Associado ao usuário.
3. Realoca entre Naturezas e Centros de Custo que está Associado ao usuário, com Valores dos Períodos Anteriores.
4. Realoca entre Naturezas e Centros de Custo que está Associado ao usuário, com Valores de todos os Períodos.

Para liberar o orçamento excedente, o usuário pode retirar valores de outros centros de custo orçados até atingir o valor necessário.  
Após fazer a transferência dos valores necessários para desbloquear o movimento, e clicar no botão avançar, o sistema atualiza os valores recebidos e cedidos dos orçamentos selecionados e libera o movimento para que esse possa ser recebido.  
*Observações:*

* Após ter feito a realocação e ter salvo o movimento, caso tenha que alterar algum campo do movimento, o sistema irá desfazer a realocação orçamentária.

A Realocação Orçamentária só será permitida se o orçamento origem e o destino possuírem a mesma estrutura de Orçamento, ou seja, movimentos que afetam Orçamento de Despesa retornará Naturezas de Orçamento do tipo **Despesa** ou **Ambos**.  
Centro de Custo | Natureza Orçamentária/Financeira | Grupo Orçamentário (Opcional) \* ou Centro de Custo | Natureza Orçamentária/Financeira  
***Importante!***Para orçamentos do tipo Receita não existe o recurso de realocação.

**Integração com o TOTVS Construção e Projetos**

* Disponível a partir da versão 12.1.31.

---
