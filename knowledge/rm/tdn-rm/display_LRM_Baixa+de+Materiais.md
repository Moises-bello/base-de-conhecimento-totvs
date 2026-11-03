---
content_hash: d85d65e92943fa7bb6ec56f0db35f8167454597d6565670171ad92a0caba3c7c
fetched_at: '2026-06-29T00:09:25.199212+00:00'
page_id: '423938057'
product: rm
source: tdn-rm
title: Baixa de Materiais
type: documentation
url: https://tdn.totvs.com/display/LRM/Baixa+de+Materiais
version: 2
---

A Baixa de Materiais ou Entrada no Estoque Intermediário dependerá do tipo de parametrização, que são 4 opções:

1. Não realizar Consistência
2. Antes de Firmar o Item de Ordem
3. Antes de Iniciar Apontamento do Item da Ordem
4. Antes de dar Entrada de Produção

Para efetuar a parametrização acesse o menu Opções | Parâmetros | Produção, pasta Gerais.  
Caso esteja trabalhando com o parâmetro "Empenha Matéria Prima", antes de efetuar a baixa será necessário realizar o processo de empenho ou, então, informar de qual local de estoque será feito a baixa do item.

1. Se o produto a ser baixado tiver controle de lote e/ou número de série, o sistema irá sugerir a baixa dos materiais na seguinte ordem:
2. Materiais com seus respectivos lotes e números de série apontados. Se esses lotes/séries apontados não forem associados, a baixa não poderá ser realizada.
3. Materiais com seus respectivos lotes e números de série empenhados para o item da ordem de produção.
4. Se não existir apontamento e nem empenho o sistema não irá fazer nenhuma sugestão na baixa.
5. Ao concluir a baixa o sistema debita do local de estoque (Local de Empenho ou Local de Matéria Prima) as quantidades necessárias para a fabricação do produto - acabado ou semiacabado.
6. Na visão de Baixa de Materiais, é possível selecionar e excluir todos os materiais com saldo insuficiente para efetuar a baixa de materiais com saldo. Ao editar um item o sistema exibe uma tela onde é possível aumentar ou diminuir a quantidade de material a ser baixado, de qual lote e os números de série que serão baixados caso o material possua estes controles.
7. Na grid "Locais de Estoque / Lotes Disponíveis" – do lado esquerdo da tela, serão listados os lotes disponíveis (quantidade do saldo físico, número do lote e validade), os locais de estoque de outras filiais, independente do contexto de segurança estendida e, no campo "Qtde a Associar", é possível informar a quantidade de materiais que será baixado. Após informar a "Qtde a Associar" selecione o item para transferí-lo para a grid "Locais de Estoque/Lotes Associados" – ao lado direito da tela.

***Observações***: O sistema sugere associação de lotes mais antigos, de acordo com a data de validade de cada lote ou de seu sequencial (do mais antigo para o mais novo). Para tal, é preciso marcar o parâmetro "Carrega lotes mais antigos na escolha do lote" em parâmetros da Produção | Pasta Gerais.  
É possível realizar baixa parcial de material consumido nas atividades apontadas, em quantidade igual, maior ou menor que o previsto. Basta que seja marcado o parâmetro "Baixa Material Consumido no Apontamento" e que a consistência de baixa de matéria prima seja "Não Realizar Consistência" ou "Antes de dar entrada de produção.

***Atenção!***  Se uma atividade for cancelada após a baixa de materiais ao dar entrada de produção o material da atividade cancelada será devolvido.   
Pasta Números de Série Na pasta números de série existem três grids. A grid superior "Locais de Estoque/Lotes Selecionados" contém os lotes que foram selecionados para a baixa.   
As grids inferiores referem-se aos números de série "Disponíveis" e "Selecionados".   
Caso tenha selecionado para a baixa mais de um lote, para selecionar os números de série referente a este lote, é necessário selecioná-lo primeiro na grid superior para que os números de série do lote selecionado sejam listados na grid inferior "Disponíveis", ao lado esquerdo da tela. Após selecionar os números de série, os mesmos deverão ser transferidos para a grid "Selecionados", ao lado direito da tela, só assim o sistema irá efetuar a baixa sem ocorrência de crítica.   
***Observações***: A pasta números de série ficará visível somente quando o produto for controlado por número de série.   
Pasta Críticas Fornece informações que restringem a baixa de materiais.  
**Exemplo** "Quantidade informada superior à quantidade em estoque."   
Baixa de Materiais Pelo Posto de Trabalho É possível baixar materiais pela visão do cadastro do posto de trabalho. A baixa pelo posto é utilizada quando há necessidade de baixar material onde o consumo foi superior ao calculado ou não está previsto na estrutura. Desmarcando o parâmetro "Filtra Produto pelo Item de Ordem e Posto" os materiais que não fazem parte da estrutura, ou seja, que não são listados como componentes da estrutura, ficarão visíveis para baixa.
