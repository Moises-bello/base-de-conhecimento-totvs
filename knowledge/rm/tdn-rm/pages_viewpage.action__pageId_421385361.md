---
content_hash: e721ddbd9992d68f76000717f3f3ccc4c32e26d9fe161dfc29302cafc084f32f
fetched_at: '2026-06-29T00:09:15.381518+00:00'
page_id: '421385361'
product: rm
source: tdn-rm
title: Cópia de Cronograma
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385361
version: 2
---

---

Copiar Cronograma é um processo que possui como finalidade copiar os cronogramas de uma tarefa para outra(s).

Estes cronogramas são categorizados como "Previsto", "Medido" e "Realizado". O usuário poderá selecionar a quantidade e qualquer categoria que desejar.

Planilha de atividades (ou planilha de serviços)|processos| cópia de cronograma

O processo de cópias de cronogramas o usuário poderá selecionar várias tarefas de destino.

Diante disso, a execução deste processo segue com as seguintes restrições de modo a efetivar a sua operabilidade:

* A tela do processo somente abrirá se houver alguma tarefa selecionada;
* Somente uma tarefa deverá ser utilizada como origem;
* Tarefas receita, marco, valor cotado, inativas, rateadas ou que sejam obra ou etapa não podem ser utilizadas como destino de rateio.
* Ao selecionar obras ou etapas informações que esses tipos de registros exibem são oriundas das subtarefas relacionadas.
* De acordo com os processos "Aplicar curva de distribuição" e "Lançamentos Múltiplos", o processo "Copia de cronograma" não deverá copiar valores para os períodos travados.

Durante a cópia de cronogramas a única grandeza a ser copiada será o percentual, de modo que as quantidades e os valores serão calculados em virtude da quantidade e preço da tarefa de origem. Sendo assim, todos os cronogramas das tarefas de destino assumirão como grandeza de lançamento o campo Percentual. Os registros selecionados no campo de destino correspondem aos registros oriundos da mesma planilha, assim como o registro da tarefa de origem responsável pela cópia dos dados. Deste modo, não será possível copiar informações contidas em um determinado cronograma com planilhas diferentes.
