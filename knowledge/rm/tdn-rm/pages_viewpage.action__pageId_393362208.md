---
content_hash: bd80bb86c38ada54f89b4d7e11abbedde780f3fd430265db4a941ea950582079
fetched_at: '2026-06-29T00:09:09.678050+00:00'
page_id: '393362208'
product: rm
source: tdn-rm
title: FISCAL01-923 DT Lançamento Fiscal Saída - Associação de Lançamentos de Saída
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=393362208
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Associação de Lançamentos de Saída |
| **Situação/Requisito:** | Criar no Menu Obrigações Principais\Lançamento de Saída - um processo para associar de forma automática os Itens de Entrada ao Itens de Saída.  Para cada um dos itens associados aos lançamentos fiscais selecionados pelo usuário, o sistema deverá buscar a última entrada que possua ICMS ST informado (desconsiderar entradas de devolução).  Se a quantidade de itens na última entrada for inferior à quantidade que está no lançamento fiscal de saída, o sistema deve procurar a penúltima entrada e assim sucessivamente, até que toda a quantidade que esteja saindo esteja "coberta".  Este processo não será executado para Lançamentos que já tiveram o Item de Referencia incluído;  Após a execução do Processo será gerado um log com o resultado do processo contendo:  1) quais notas de entrada foram associadas a quais notas de saída; 2) os produtos que não foram associado por falta de quantidade, entre o Item de Saída e o Item de Entrada; 3) lançamentos que não foram processados por já terem associação informada; 4) itens não encontrados por não possuírem natureza com "Operação com Ressarcimento de ST na Compra" habilitado. |
| **Solução/Implementação:** | Desenvolvimento do processo descrito a seguir.  O processo está disponível em: Menu Obrigações Principais \ Lançamentos de Saída \ Associação de Lançamentos de Saída.    Possui somente uma etapa, em que é necessário o preenchimento da informação do código do motivo do ressarcimento.  Assim, o processo associará os registros de saída selecionados, que estiverem com a natureza com "Operação com Ressarcimento de ST na Compra" marcados (conforme figura abaixo).  Para cada um dos itens associados aos lançamentos fiscais selecionados pelo usuário, o sistema deverá buscar a última entrada que possua ICMS ST informado, desconsiderando as entradas de devolução.    Se a quantidade de itens na última entrada for inferior à quantidade que está no lançamento fiscal de saída, o sistema deve procurar a penúltima entrada e assim sucessivamente, até que toda a quantidade que esteja saindo esteja "coberta".  Para os registros processados corretamente o registro do processo informará qual item de saída foi vinculado a qual item de entrada e em que quantidade. Conforme a figura seguinte:     Caso para algum registro de saída marcado não possuir a natureza com "Operação com Ressarcimento de ST na Compra" marcado, o registro do processo apresentará o seguinte:    "Não foi encontrado nenhum item de saída para o grupo de lançamento 50478. Verifique se a natureza é de "Operação com Ressarcimento de ST na Compra" na aba "Outros Dados".  No caso de se tentar processar itens já associados, o registro do processo apresentará a seguinte informação:     "O item 1 do lançamento fiscal de saída 58826 não foi processado por já estar associado a um item".  Caso haja uma maior quantidade de itens de saída do que de entradas com ST registradas, o sistema apresentará o seguinte comportamento:     "O produto Produto NF-e do lançamento 58831 e número do item 1 não foi associado por falta de quantidade".  Considerações finais:   * Se um lançamento tiver vários itens, caso um item esteja associado e os demais não, o sistema tentará associar os demais itens ainda não associados. * A associação é feita no formato UEPS - último que entra/primeiro que sai, validando se a quantidade total de produtos da nota já foi associada anteriormente, busca outra mais antiga que ainda não tenha sido associada. |
