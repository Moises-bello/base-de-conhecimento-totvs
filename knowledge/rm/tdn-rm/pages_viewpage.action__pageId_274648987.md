---
content_hash: 3e818e8afa086a6ad78dd34bce189ee82ddbdfa3d7ccdf572f6f5cb05068aa12
fetched_at: '2026-06-29T00:08:34.179746+00:00'
page_id: '274648987'
product: rm
source: tdn-rm
title: FOPCALCULO01-317 Novos parâmetros na configuração de chapa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274648987
version: 97
---

# TRANSFERÊNCIA COLETIVA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construções e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Geração de chapa no processo de transferência coletiva através de fórmula |
| **Situação/Requisito:** | Realizar a transferência coletiva de funcionários para uma nova coligada sendo possível informar as chapas da funcionário para a coligada destino através de um cadastro de/para |
| **Solução/Implementação:** | * Implementação de um novo parâmetro para geração de chapa no processo de transferência coletiva através de fórmula.   Foram criados dois novos parâmetros no Configuração de Chapa. Sendo acionado em Folha de pagamento / Configuração de Chapa / Transferência   **Geração de Chapa por Fórmula na Transferência Coletiva:** parâmetro para ativar a geração da chapa do funcionário na coligada destino através da fórmula cadastrada no campo relacionado  Este parâmetro ignorará a geração de chapa, na transferência coletiva, através de cadastro sequencial e levará em consideração o resultado da fórmula.  **Fórmula para Nova Chapa:** informar uma fórmula já cadastrada para realizar a busca da nova chapa (ex. buscar informação de campo complementar, tabela de/para)  Exemplo de Fórmula:  STR (COLIGADACORRENTE,'00')+ STR(CHAPA, '000'), onde a coligada corrente é 1, e a chapa do funcionário corrente é 00001. O resultado da fórmula será 01001.  Se a configuração de chapa possuir mascara com separador, ##.###, a fórmula deverá compor o caractere:  STR (COLIGADACORRENTE,'00')+ '.'+ STR(CHAPA, '000'), onde o retorno será 01.001  Quando o parâmetro de geração de chapa por fórmula estiver marcado será obrigatório informar o campo fórmula (validação através de mensagem para o usuário)   * Alteração do processo de cálculo da transferência para validação do novo parâmetro gerado.   No caso do parâmetro de geração de chapa estar selecionado (coligada origem) e o processo ser uma transferência coletiva a geração da chapa do funcionário para a coligada destino respeitará o resultado da fórmula parametrizada.  Foram realizadas as seguintes validações para a nova chapa gerada:   * + Se a nova chapa encontrada pela fórmula existir na coligada destino, o log exibirá a informação:"A Chapa xxx já existe na coligada destino." e a transferência do funcionário não será efetuada.   + Se não retornar nenhuma chapa pela fórmula, a transferência não será realizada para o funcionário e uma mensagem será informada no log: "Nova Chapa inválida".     Caso o parâmetro "Cadastro Automático de Chapas Sequenciais" estiver selecionado na Coligada Destino e a Nova Chapa gerada for maior que o valor informado no campo CADASTROAUTOMATICOCHAPASSEQUENC da tabela GAUTOINC a nova implementação efetuará o ajuste do valor da tabela GAUTOINC para o correspondente a chapa gerada, não prejudicando o sequenciamento. |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** |  |
| **Requisito:** |  |

divs
