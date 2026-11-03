---
content_hash: fa52592e2415708d024aab23205499277f8cc51aa6a4226b5216533798b33ab7
fetched_at: '2026-06-29T00:09:14.098957+00:00'
page_id: '421385122'
product: rm
source: tdn-rm
title: Anexo de Itens da Folha Tarefa
type: documentation
url: https://tdn.totvs.com/display/LRM/Anexo+de+Itens+da+Folha+Tarefa
version: 21
---

---

Os itens de uma Folha Tarefa são as tarefas que foram planejadas para serem executadas nas frentes de obra em dado intervalo de tempo.

É o progresso destas tarefas que deve ser obtido nos apontamentos de Avanço Físico realizados no App Minha Obra.

O anexo Itens da Folha Tarefa contém as tarefas da Planilha de Atividades ou Planilha Executiva (conforme parâmetro **Planilha para Apontamentos )** e nele pode-se visualizar, incluír ,alterar e excluir itens.

As Tarefas que são exibidas são aquelas que ainda possuem saldo para serem associadas.

Dados dos itens da folha tarefa: ( as informações serão exibidas conforme a planilha definida para apontamento no parâmetro Planilha para Apontamentos em [Mobilidade (F6)](https://tdn.totvs.com/pages/viewpage.action?pageId=421385196) )

**Código da tarefa:** Código da tarefa da Planilha de Atividades ou do item da Planilha Executiva

**Nome da tarefa:** Nome da tarefa da Planilha de Atividades ou do item da Planilha Executiva

**Descrição da Tarefa:** Descrição da tarefa da Planilha de Atividades ou do item da Planilha Executiva

**Quantidade da tarefa:** Quantidade total da tarefa ou item

**Quantidade Programada:** Quantidade programada da tarefa ou do item.

A quantidade programada e quantidade planejada, é calculada da seguinte forma:

(qtdeTarefa - (qtdeTarefa \* percConcluidoTarefa / 100) - qtdePlanejada) \* diasIntersecaoTarefaFolha / diasRestantesTarefa)

Onde:

**QtdeTarefa:** É a quantidade total da tarefa (Planejada na Planilha de atividades o Planilha Executiva).

**PercConcluidoTarefa:**  É o percentual já concluído da tarefa.

**QtdePlanejada:** É a quantidade planejada dessa tarefa em qualquer outra folha ativa.

**DiasIntersecaoTarefaFolha:** São os dias da tarefa na folha.

**DiasRestantesTarefa:** São os dias uteis restantes na folha, lembrando que a definição de dias uteis pode ser parametrizada.

**Código da unidade:** Código da unidade da tarefa

**Data inicial:** Data de início da tarefa

**Data final:** Data fim da tarefa

**Status do apontamento:** Status do apontamento

**Criado por:** Usuário que incluiu o item a folha tarefa

**Data Criação:** Data da criação do item

**Modificado por:** Usuário que alterou o item na folha tarefa

**Modificado em :** Data da modificação

**Saldo a executar:** Saldo de quantidade da tarefa/item  disponível para ainda ser  associado a novas folhas tarefa (saldo = qtde da Tarefa - qtde concluída - qtde planejado na folha)

**Número do contrato:** Contrato que a tarefa esteja associado ou vinculado

**Valor da tarefa:** Valor total da tarefa

**Valor disponível de M.O:**

**Valor Mão de Obra:**

**Valor alocado:**

**Fator de Produtividade:**

* As tarefas de uma Folha Tarefa são as atividades que foram planejadas para serem executadas nas frentes de obra em dado intervalo de tempo. É do progresso destas tarefas que deve ser obtido os apontamentos através do uso de coletores móveis pelos responsáveis por tais funções;
* A inserção das tarefas da Folha Tarefa se baseará, única e exclusivamente, na planilha de atividades do TOP. Este anexo contém as tarefas da planilha de atividades e ainda possui campos adicionais;
* Para seleção das tarefas para a Folha Tarefa o sistema disponibiliza algumas formas de fazê-lo:
  + Cadastro padrão inserindo uma tarefa por vez;
  + Processo que permitirá selecionar várias tarefas ao mesmo tempo e inseri-las;
  + “Drag-and-Drop”, o usuário deverá abrir a planilha de atividades e o anexo de itens da Folha tarefa lado a lado, arrastando e soltando as tarefas para o anexo de itens.
* Em qualquer situação de apresentação das tarefas da planilha de atividades, para seleção/inserção como tarefa da Folha, as tarefas da planilha de atividades são filtradas de acordo com as datas de início e fim da Folha previamente cadastrada;
* Este filtro deve ser aplicado nos campos início e fim programado das tarefas da planilha de atividades e serão exibidas (da Planilha de Atividades, Seleção múltipla, cadastro padrão) somente as tarefas que façam interseção com o período informado.

A partir do APP Minha Obra é possível criar/alterar medições de itens de contrato através dos apontamentos de Avanço Físico dos itens da Folha Tarefa, sendo via coletor ou apontamento manual. Para que essa incidência ocorra, é necessário vincular o contrato desejado ao item associado à folha tarefa, porém é necessário considerar algumas premissas:

* A tarefa deve ser definida antes do contrato;
* As datas início e fim do contrato devem fazer interseção com as datas início e fim da folha tarefa;
* A tarefa selecionada deve estar associada ao contrato;
* Ao salvar a associação do contrato ao item, caso o parâmetro de medição acima de 100% estiver diferente de SEMPRE PERMITIR, será verificado se a quantidade planejada do item da folha é maior que a quantidade do saldo do item no contrato, o que não deve ser permitido.
