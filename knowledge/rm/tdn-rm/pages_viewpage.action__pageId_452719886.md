---
content_hash: a452fa32033bb3d5d455d4f41846d19bf743810a695d7384a794c89919d0d2d4
fetched_at: '2026-06-29T00:10:10.591508+00:00'
page_id: '452719886'
product: rm
source: tdn-rm
title: Agrupamento Salarial (RM Classis Net)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719886
version: 3
---

Nesta pasta está relacionado todo o movimento do RM Classis para os funcionários, e no RM Labore será associado um evento a este movimento para lançamento de salário composto. O salário composto de cada um destes funcionários importados do RM Classis deverá ser alterado através de Gestão Educacional | Reprogramação Salarial.   
   
**Dicas**  
Para facilitar a visualização, o usuário poderá arrastar qualquer uma das colunas ou mais de uma coluna para o espaço acima onde está escrito "Para agrupar, arraste para esta área o título da coluna desejada".  
A mensagem "Favor verificar professores com eventos não informados." será apresentada sempre que não houver evento informado para algum professor no agrupamento para salário composto, sendo que deve ser informado para a correta reprogramação salarial do funcionário.

**Atenção 1**  
Para Reprogramação salarial detalhada por centro de custo, você lança eventos através do menu Gestão Educacional | Lançamento de Eventos por Centro de Custo, caso contrário, você lança o evento através de Movimentação | Folha de pagamento | Lançamentos automáticos | Grupos de eventos.

**Atenção 2**  
Para faltas e atrasos, você deve lançar o evento através do Agrupamento de Salário Composto e lançá-los em Movimentação | Folha de pagamento | Lançamentos automáticos | Grupos de eventos. Não se esqueça, caso haja alteração salarial do funcionário (professor) é necessário Reprogramar o salário, veja em Gestão Educacional | Reprogramação Salarial.

**Centro de Custo**  
A coluna de Centro de Custo é informada de acordo com o parâmetro marcado no RM Classis nos dois contextos: Ensino básico e Ensino superior, sendo da seguinte forma:  
Centro de Custo com origem 'Da turma' ou Centro de custo com origem da 'Da matriz aplicada a Turma' .

**Valor Hora**  
A coluna de Valor Hora é informada de acordo com o parâmetro: "Utilizar valor da hora/aula" marcado no RM Classis nos dois contextos: Ensino básico e Ensino superior, sendo da seguinte forma:  
Valor Hora com origem do 'De acordo com a titulação e função do professor' ou Valor Hora com origem do 'Do cadastro de professor da turma/disciplina'

**Evento de Salário / Evento de Falta / Evento de Atraso**  
O(s) evento(s) informado(s) neste menu deverá(ão) ser do tipo hora, para que ao executar o menu Gestão Educacional | Lançamento de Eventos por Centro de Custo o sistema processe o salário corretamente.

**Lançar Eventos**  
Será lançado o evento escolhido pelo usuário nos campos marcados. É possível setar todo um agrupamento para que este evento seja lançado de uma única vez, para isto o usuário deve clicar no agrupamento desejado, ou marcar cada funcionário individualmente.

**Exemplo**  
Para lançar para o agrupamento período letivo, arraste o nome da coluna para o espaço "Arraste aqui o cabeçalho de uma coluna para agrupar", clique no período letivo desejado, escolha o evento e lance este evento para todos os funcionários que estão selecionados. Para lançar para funcionários que lecionam a matéria geografia dentro do agrupamento período letivo, arraste o nome da coluna período letivo para o espaço " Arraste aqui o cabeçalho de uma coluna para agrupar ", clique usando o "shift" marcando todos os funcionários que lecionam geografia, escolha o evento e lance este evento para todos os funcionários que estão selecionados.

**Observação:**

Quando é efetuado o lançamento do evento, ele é lançado para turma/disciplina. O professor recebe o evento lançado por estar vinculado à turma/disciplina. No caso,  
se lançarmos o evento para uma determinada turma/disciplina será lançado para todos professores vinculados à ela, mesmo que não possua aulas semanais na turma/disciplina.

**Atualizar visão**  
Ao lançar um evento para o movimento será perguntado se o usuário deseja atualizar a visão ou não. Caso o usuário clicar em "Sim" não será necessário utilizar este botão, mas caso o usuário faça vários lançamentos de eventos distintos e desejar atualizar visão somente uma vez poderá clicar em "Não" toda vez que apresentar a mensagem e pedir uma única atualização utilizando este botão.

**Configurar Colunas**  
Através desta função o usuário poderá configurar as colunas dos lançamentos dos eventos. Este recurso é de grande utilidade, uma vez que, a visualização das tabelas são otimizadas e ainda poderão ser organizadas tanto na caixa de configuração como na própria grade do menu.
