---
content_hash: 4eff11ca11551e6cdd26be4d8628664f0318240ddbad769cb03f9b4d970a5a9e
fetched_at: '2026-06-29T00:09:31.835194+00:00'
page_id: '425458741'
product: rm
source: tdn-rm
title: Copiar modelo de etapas para outro período letivo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458741
version: 8
---

Este processo pode ser realizado pelo cadastro do [período letivo](http://tdn.totvs.com/x/oPxbGQ) e pela [parametrização por curso](http://tdn.totvs.com/x/x-xbGQ). Ele se destina a copiar um modelo de etapa para outro período letivo. Além das etapas, as avaliações também podem ser copiadas. Serão copiados tais dados do modelo de etapas de origem:

* Tipo da etapa
* Código e descrição da Etapa
* Datas de início e término
* Datas de início e limite de digitação
* Datas de limite de conteúdo previsto
* Datas de limite de conteúdo efetivo
* Grupo de conceitos
* Fórmula de notas
* Pontos distribuídos
* Média
* Notas conceituais
* Exibir no gráfico
* Grupo de Conceitos (Competências/Habilidades)

Após informar o período letivo de destino e se as avaliações serão copiadas, todas as datas poderão ser definidas na segunda etapa do processo. Caso você não informe nenhum registro para essas datas, os modelos cadastrados nos períodos letivos de destino terão as datas em branco, mesmo que as etapas de origem tenham datas cadastradas.

A partir da versão 12.1.32 foi criado o parâmetro "Permitir cadastrar avaliação", na etapa do tipo notas. Caso a etapa já tenha avaliação cadastrada não será possível desabilitar o parâmetro. Ao optar por desmarcar o parâmetro o anexo modelos de avalições por período letivo será desabilitado, não sendo possível a inclusão de avaliações.

Este processo não atualiza as etapas e/ou avaliações, ele apenas efetua a cópia. Caso no destino já exista a mesma etapa e/ou avaliação, o processo não irá atualizar.

Segue exemplo de log da execução de uma cópia da matriz aplicada 5611 para a 5612, onde no destino já existia as mesmas etapas cadastradas.
