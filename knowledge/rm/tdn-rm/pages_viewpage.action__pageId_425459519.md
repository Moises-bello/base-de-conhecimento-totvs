---
content_hash: f3f1411b84164fa8a1ed4dd0964c9004fa0588049bcb09c4e4b2677ddea5cdbc
fetched_at: '2026-06-29T00:09:36.776284+00:00'
page_id: '425459519'
product: rm
source: tdn-rm
title: Backoffice RM x Protheus SigaMNT - Reabrir Ordem de Serviço
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459519
version: 2
---

**Backoffice RM x Protheus SigaMNT - Reabrir Ordem de Serviço**

---

Esta função permite reabrir uma O.S. que já havia sido finalizada.  Após a reabertura o usuário poderá informar insumos e etapas para concluir a O.S. e finalizá-la novamente.   
    
   
    
 **Pré-Condições:**  
    
 **1:** Possuir uma Ordem de Serviço com o Status "Finalizada".

**2:** Cadastrar os tipos de movimento :

* Ordem de Manutenção
* Baixa de Estoque
* Acréscimo em estoque
* Solicitação de Compra
* Solicitação de Armazém

**3:** Sincronizar os Bens (Ativos Fixos) que sofrerão as manutenções.

**4:** Sincronizar os Locais de Estoque dos produtos a utilizar como Insumos

**5:** Sincronizar os Produtos / Serviços que serão utilizados como Insumos.

**6:** Sincronizar o Projeto de manutenção e suas Tarefas.

**7:** Sincronizar as Unidades de Medida.

**8:** Sincronizar os Centros de Custos.

**Executando o Processo:**

**Passo 1:** Acesse: Atualizações/Retorno O.S./Reabertura O.S.

**Passo 2:** Informe o número de uma  O.S. finalizada.

**Passo 3:** Confirme a reabertura da O.S.

**Passo 4:** O Protheus SigaMNT  envia uma mensagem ao Backoffice RM e altera o status do Movimento de Ordem de manutenção, que estava com o valor "A Faturar" , para "Em Andamento".

**Passo 5:** Acesse : RM / Backoffice / Gestão de Estoque, Compras e Faturamento.

**Passo 6:** Acesse : RM / Backoffice / Gestão de Estoque, Compras e Faturamento / Outras Movimentações.

**Passo 7:** Informe o código do Tipo de Movimento criado para Ordem de Manutenção e a Filial.

**Passo 8:** Editar o Movimento de Ordem de Manutenção  e verificar que o seu  status  é  "Em Andamento".
