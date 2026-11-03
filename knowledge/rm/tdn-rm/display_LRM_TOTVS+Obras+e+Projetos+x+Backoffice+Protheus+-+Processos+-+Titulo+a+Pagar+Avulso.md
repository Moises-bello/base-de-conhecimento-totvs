---
content_hash: 485fb94a302b2088909a6c61710aa8a7125e92f85f728ec7cb03e8d00ba8700a
fetched_at: '2026-06-29T00:09:35.517533+00:00'
page_id: '425459378'
product: rm
source: tdn-rm
title: TOTVS Obras e Projetos x Backoffice Protheus - Processos - Titulo a Pagar Avulso
type: documentation
url: https://tdn.totvs.com/display/LRM/TOTVS+Obras+e+Projetos+x+Backoffice+Protheus+-+Processos+-+Titulo+a+Pagar+Avulso
version: 3
---

**Titulo a Pagar Avulso**

---

A inclusão, alteração e exclusão da despesa avulsa (título a pagar) são realizadas no Protheus. No TOP são gerados os relatórios e o cronograma. É utilizada a tecnologia Stored Procedure para sincronizar os dados entre o TOP e o Protheus.

O lançamento de Títulos a pagar no Protheus, quando relacionados a um projeto/tarefa, irá gerar uma "movimento" de Despesa Avulsa no TOP com apropriação. Neste caso o movimento apropriado é a SA. O Título a Pagar Avulso pode ser alterado no Protheus, ao salvar a alteração o Protheus primeiro exclui o movimento no RM depois inclui os itens/rateio tarefas novamente .  
    
 Para incluir um título a pagar avulso no Protheus, acesse: Protheus | SigaFin | Atualizações | Gerenc. Financeiro | Contas a Pagar  
    
 1. É necessário vincular o projeto e a tarefa ao título que está sendo criado. Clique no ícone Projetos e vincule o projeto e a tarefa.  
    
 2. Preencha o campo Tipo Despesa, e no campo Valor proj. informe um valor menor ou igual ao valor do título, informado no campo Vlr. (Valor) Titulo. Após salvar o título de conta a pagar, a apropriação é realizada e o cronograma é atualizado no item apropriado.  
   
 ***Observações:***

* Devido o Protheus não sincronizar as tarefas que não sofreram alteração, é aconselhável realizar a exclusão do título (todos os rateios por tarefa), e após a inclusão com as alterações desejadas.
* O Lançamento de Títulos a Receber não está contemplado na integração.
