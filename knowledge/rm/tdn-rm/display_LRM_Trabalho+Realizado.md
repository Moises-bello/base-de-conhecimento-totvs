---
content_hash: c113db0fb5a8cc77ade32c91cbdbc3c5c7345f0345d1adf0207f3a82ed079843
fetched_at: '2026-06-29T00:11:54.820709+00:00'
page_id: '857928773'
product: rm
source: tdn-rm
title: Trabalho Realizado
type: documentation
url: https://tdn.totvs.com/display/LRM/Trabalho+Realizado
version: 1
---

**Trabalho Realizado no Apontamento**

Ao utilizar o parâmetro para "Trabalho Realizado no Apontamento" e incluir um novo apontamento o sistema considerará somente o último registro anterior **somando** com os novos apontamentos .

**Exemplo:**

Foi realizado 40% da tarefa 001.02.03 conforme imagem abaixo:

A coluna % apontamento mostra o apontamento realizado (avanço da tarefa) a tela esquerda e a direita no anexo Históricos do apontamento vejo todos os apontamentos realizado na tarefa.

Ao realizar mais um apontamento aumentando andamento da tarefa para 10% a mais por exemplo o sistema atualiza a coluna % Apontamento **Somando** o ultimo apontamento realizado aos demais já realizados. (10% mais 40% já apontado).

 totalizando %Apontamento para 50%.

No anexo de Históricos dos apontamento é possível visualizar em detalhes todos os históricos realizado na tarefa.

Na tela de edição do apontamento de avanço físico, é possível realizar correções no percentual ou quantidade apontada, quando um é alterado o outro é calculado automaticamente. Ao salvar, a alteração será acrescentado no histórico respeitando a parametrização "Forma de utilização do apontamento de avanço físico" mencionada acima.

Para clientes que optarem por utilizar a novo cálculo do Avanço ("Trabalho Realizado"), o Totvs Obras e Projetos passa a  aceitar a existência de apontamentos com  percentual (%) ou quantidade negativos.

Isso será possível porque no novo cálculo do Avanço Físico o sistema vai sempre somar os históricos no apontamento e não mais considerar o último histórico.
