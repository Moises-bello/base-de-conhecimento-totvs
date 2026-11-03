---
content_hash: a9dd41f68ecd04cf910456da6a9773d05265d9d8a39721f30abe6177e3574244
fetched_at: '2026-06-29T00:11:27.689856+00:00'
page_id: '729219562'
product: rm
source: tdn-rm
title: Importar Planilha Executiva do Excel
type: documentation
url: https://tdn.totvs.com/display/LRM/Importar+Planilha+Executiva+do+Excel
version: 15
---

Para facilitar a criação da Planilha Executiva, foi disponibilizado um processo de importação de dados, o que possibilita importar todos os itens e vínculos da planilha executiva, através de uma planilha do Excel. O processo fica disponível na tela inicial, ao acessarmos a planilha executiva pela primeira vez em um projeto:

E na visão da planilha, quando já existem itens cadastrados:

Ao clicar em "Importar Excel", será apresentada a tela do processo de importação, que será detalhada posteriormente, primeiro destacamos um modelo de planilha do excel usada nesse processo:

Com base nessa planilha, voltamos para a tela do processo de Importar Excel e seu correto preenchimento:

Na parte superior da tela, será necessário informar a localização do arquivo, a linha inicial da planilha para importação (campo numérico), e a coluna do código do item. Essas colunas serão sempre obrigatórias, principalmente o código do item, pois toda importação e seus vínculos, serão feitos tendo essa coluna como referência:

Na parte inferior da tela, são apresentadas as 3 abas do cadastro de itens da Planilha Executiva: Dados do Item, Vínculos e Planejamento/Avanço Físico; permitindo que sejam importados, além dos campos obrigatórios, os vínculos e os dados do planejamento/avanço físico.

Para realizar a importação de cada uma dessas abas é necessário marcar o checkbox "**Incluir/Atualizar Dados do Item**" em cada aba que desejar realizar a importação de dados.

No exemplo abaixo, apenas os Dados do Item serão importados, pois apenas essa aba teve o checkbox marcado:

O botão **Importar** ficará habilitado assim que informados os campos da parte superior da tela e habilitar também o checkbox de incluir/atualizar de alguma das suas três abas.

Após preenchidas as informações necessárias, basta clicar em Importar e os registros serão inseridos/atualizados na planilha executiva, caso tudo tenha corrido conforme o esperado, uma nova aba será aberta ao final da importação, contendo o log do processo:

Caso a importação tenha ocorrido com erros, estes também serão listados nessa mesma aba.

**Observação:** Em uma estrutura com múltiplos níveis, na importação, será considerado de ultimo nível o item final da estrutura da planilha, não o item final da estrutura da mascara, todos os itens superiores, serão importados com os campos 'Quantidade', 'Unidade' e 'Valor Unitário' como nulos, e o item de último nível seguirá as informações da documentação de parâmetros da planilha executiva, para mais detalhes vide link abaixo:

Na importação de Vínculos

Os vínculos criados através da importação só poderão ser excluídos de forma manual no sistema. Caso uma tarefa tenha sido vinculada por engano, será possível importar o vínculo correto, porém é necessário fazer a exclusão pelo sistema do vínculo feito por engano.
