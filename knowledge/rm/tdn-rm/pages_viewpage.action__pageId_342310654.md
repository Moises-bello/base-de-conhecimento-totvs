---
content_hash: 29959d812d0d9cb0f9c6765678291b10e717b7da24d32a25257b164ed4e45f7a
fetched_at: '2026-06-29T00:08:53.091791+00:00'
page_id: '342310654'
product: rm
source: tdn-rm
title: DT - Liberação de Competência Multi-Coligadas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=342310654
version: 4
---

# Liberação de Competência Multi-Coligadas

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Folha de Pagamento |
| **Módulo:** | Folha Mensal |
| **Função:** | Liberação de Competência Multi-Coligadas |
| **Situação/Requisito:** | Liberação de Competência Multi-Coligadas |
| **Solução/Implementação:** | O processo de liberação de competência foi alterado para permitir a execução do processo em múltiplas coligadas simultaneamente. |

**Funcionamento do Novo Processo:**

Acesse o menu de Liberação de Competência.

Os parâmetros de liberação continuam presentes, com a adição de um campo para informar um caminho local, caso deseje salvar os logs da execução para análise:

Em seguida selecione para quais coligadas deseja efetuar a liberação de competência. Apenas serão exibidas as coligadas que estiverem na mesma competência da coligada atual do contexto.

É possível também alterar certos parâmetros específicos para cada coligada:

Antes de executar o processo, é necessário efetuar a validação das coligadas selecionadas. Ao clicar sobre o botão de "Validar Coligadas", o processo será efetuado para cada uma, e o status e log serão informados na grid.

Ao final da validação é exibida uma mensagem informando o local onde foram salvos os logs da validação:

A validação pode retornar 3 status: Sucesso, Aviso ou Erro.

O processo, por padrão, será executado apenas para coligadas com sucesso na validação. Caso haja coligadas com aviso, serão apresentados dois checkboxes para o usuário:

* Li e estou ciente dos avisos que foram dados para as coligadas abaixo (ou seja, leu e está ciente das mensagens de validação presentes nos logs)
* Desejo liberar a competência das coligadas que tiveram avisos (ou seja, deseja executar o processo de liberação também para as coligadas com aviso)

Ao avançar, o usuário será lembrado novamente de quais coligadas serão processadas:

Caso todas as coligadas possuam erros, o processo não poderá avançar:

Ao final da execução, os logs de cada coligada serão salvos na pasta informada na tela de parâmetros, ou na pasta de logs do sistema, caso seu caminho esteja informado no LOGPATH do host.

**VALIDAÇÃO DA LIBERAÇÃO DE COMPETÊNCIA**

O processo de validação da liberação de competência funciona de maneira semelhante.

Na primeira tela de parâmetros é apresentado apenas o campo para informar o caminho do diretório onde serão salvos os logs:

Além disso, durante a validação não são exibidos os checkboxes e o processo permite continuar mesmo com erros, e todos os logs são exibidos ao final, bem como armazenados seguindo as mesmas regras acima.
