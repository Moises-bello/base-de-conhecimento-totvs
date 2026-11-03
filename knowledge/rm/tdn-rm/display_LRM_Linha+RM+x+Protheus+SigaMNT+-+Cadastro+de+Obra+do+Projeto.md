---
content_hash: 522c27b4a99ae7ef53919dec62a551ca8588bbfda6224a2f6f4e59162afa64d1
fetched_at: '2026-06-29T00:09:34.588398+00:00'
page_id: '425459196'
product: rm
source: tdn-rm
title: Linha RM x Protheus SigaMNT - Cadastro de Obra do Projeto
type: documentation
url: https://tdn.totvs.com/display/LRM/Linha+RM+x+Protheus+SigaMNT+-+Cadastro+de+Obra+do+Projeto
version: 2
---

**Linha** **RM x Protheus SigaMNT - Cadastro de Obra do Projeto**

---

As inclusões, alterações e exclusões de Obra são feitos através do Linha RM, que identifica o evento em sua entidade e envia uma mensagem ao Protheus SigaMNT.   
 Através da sincronia de dados o Protheus pode utlizar as etapas enviadas, em seus processos de Manutenção de Ativos. Para o cadastro de Obra, é necessária a seleção de um projeto. A integração Linha RM x Protheus SigaMNT não permite que seja excluida uma obra sem antes a exclusão de outras **etapas** ou **tarefas** vinculadas a ela.

Através do sistema RM é permitido cadastrar ou excluir diversos registros simultaneamente. Qualquer inclusão ,alteração ou exclusão efetuadas no RM são enviadas ao Protheus SigaMNT depois de salvar os registros apenas.

***Nota:*** *Para cadastrar uma obra é necessário antes ter um projeto.* Os dados sincronizados pela mensagem única são: Código da Tarefa Custo Parcial Custo Unitário Descrição Nome Quantidade Valor parcial Valor Unitário

1. O campo Edt/ Tarefa precisa ser configurado e parametrizado no Protheus para receber obras sem apresentar problemas.
2. Os campos abaixo  do Protheus SigaMNT devem ser  parametrizados e inicializados com os valores abaixo:

   |  |  |  |
   | --- | --- | --- |
   | **Tabela** | **Campo** | **Valor** |
   | SA1 | A1\_LOJA | "1" |
   | SA1 | A1\_COD | GETSXENUM("SA1", "A1\_COD") |
   | SA2 | A2\_LOJA | "1" |
   | SA2 | A2\_COD | GETSXENUM("SA2", "A2\_COD") |

   **Observações :**
3. O campo "Código da Obra" no Protheus deve ser alterado para o tamanho de 60 caracteres, para manter compatibilidade com o RM.
4. Para saber mais sobre a configuração do campo Edt/Tarefa,clique aqui
5. Para saber mais sobre a configuração dos campos das tabelas SA1 e SA2,clique aqui

---

**Recursos Adicionais**

TDN - Boletim Técnico : [Obra](http://tdn.totvs.com/download/attachments/76251248/CONNECTOR_BT_CADASTRAR+OBRA+DE+PROJETO_BR_CON000158.pdf?version=1&modificationDate=1380044695000)
