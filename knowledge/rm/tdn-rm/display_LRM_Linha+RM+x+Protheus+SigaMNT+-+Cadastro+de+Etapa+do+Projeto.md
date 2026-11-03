---
content_hash: 7f60d2a6865abf0ad0f071e2fc2af819fda161f18b4e2e2c4b5f552674f98783
fetched_at: '2026-06-29T00:09:35.427643+00:00'
page_id: '425459352'
product: rm
source: tdn-rm
title: Linha RM x Protheus SigaMNT - Cadastro de Etapa do Projeto
type: documentation
url: https://tdn.totvs.com/display/LRM/Linha+RM+x+Protheus+SigaMNT+-+Cadastro+de+Etapa+do+Projeto
version: 2
---

**Linha** **RM x Protheus SigaMNT - Cadastro de Etapa do Projeto**

---

As inclusões, alterações e exclusões de Etapas são feitas através do Linha RM, que identifica o evento em sua entidade e envia uma mensagem ao Protheus SigaMNT. Através da sincronia de dados o Protheus pode utlizar as etapas enviadas, em seus processos de Manutenção de Ativos. Para o cadastro de Obra , é necessária a seleção de um projeto.  
    
 A integração Linha RM x Protheus SigaMNT não permite que seja excluida uma obra sem antes a exclusão de outras **etapas** ou **tarefas** vinculadas a ela. Através do sistema RM é permitido cadastrar ou excluir diversos registros simultaneamente, que são enviados ao sistema Protheus somente após os registros serem salvos.   
    
 **Nota:** Para cadastrar uma etapa é necessário antes ter um projeto e uma obra.  
 Os dados sincronizados pela mensagem única são :

* Código da Tarefa
* Custo Parcial
* Custo Unitário
* Descrição
* Nome
* Quantidade
* Valor parcial
* Valor Unitário

**Observações :**

1. O campo "Código da Etapa" no Protheus deve ser alterado para o tamanho de 60 caracteres, para manter compatibilidade com o RM.

---

**Recursos Adicionais**

Para mais detalhes sobre o cadastro , acese o Boletim Técnico.

TDN - Boletim Técnico : [Etapa](http://tdn.totvs.com/download/attachments/76251248/CONNECTOR_BT_CADASTRAR+ETAPA+DE+PROJETO_BR_CON000158.pdf?version=1&modificationDate=1380044684000)
