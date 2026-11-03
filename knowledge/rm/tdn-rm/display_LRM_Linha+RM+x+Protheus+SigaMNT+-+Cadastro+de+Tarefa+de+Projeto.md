---
content_hash: 8c2efc97aee0bbcec9771448fdb7c95a1d8d2acfc911eabcd82a9307180c92f5
fetched_at: '2026-06-29T00:09:35.364121+00:00'
page_id: '425459327'
product: rm
source: tdn-rm
title: Linha RM x Protheus SigaMNT - Cadastro de Tarefa de Projeto
type: documentation
url: https://tdn.totvs.com/display/LRM/Linha+RM+x+Protheus+SigaMNT+-+Cadastro+de+Tarefa+de+Projeto
version: 3
---

**Linha** **RM x Protheus SigaMNT - Cadastro de Tarefa de Projeto**

---

As inclusões, alterações e exclusões de Tarefa são feitos através do Linha RM, que identifica o evento em sua entidade e envia uma mensagem ao Protheus SigaMNT. Através da sincronia de dados, o Protheus pode utlizar as tarefas enviadas em seus processos de Manutenção de Ativos.   
    
 ***Nota:*** *Para o cadastro de Tarefa é necessária a seleção de um projeto e a criação de uma obra, já que o sistema efetua o cálculo automático dos níveis quando eles são inseridos na planilha de atividades.*

Os dados sincronizados pela mensagem única são :

* Código da Tarefa
* Custo Parcial
* Custo Unitário
* Descrição
* Nome
* Tipo Tarefa
* Valor parcial
* Valor Unitário

**Observações:**

1. O campo "Código da Tarefa" no Protheus deve ser alterado para o tamanho de 60 caracteres, para manter compatibilidade com o RM.
2. O Nível (Obra , Etapa e Tarefa) é atribuido ao cadastro de acordo com a máscara fornecida. Para que a máscara do sistema identifique a tarefa é necessário o preenchimento dos campos :

* Cód. Unid
* Quantidade
* Valor Cotado  
    

  ---

Para mais detalhes sobre o cadastro , acese o Boletim Técnico.

**Recursos Adicionais**

TDN - Boletim Técnico : [Tarefa](http://tdn.totvs.com/download/attachments/76251248/CONNECTOR_BT_CADASTRAR+TAREFA+DE+PROJETO_BR_CON000158.pdf?version=1&modificationDate=1380044705000)
