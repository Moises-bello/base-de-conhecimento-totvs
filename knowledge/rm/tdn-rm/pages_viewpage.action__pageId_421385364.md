---
content_hash: 562fa59f887ffb4e28b869d1094a5cf0a02876018c80171c940a36aace301555
fetched_at: '2026-06-29T00:09:15.387305+00:00'
page_id: '421385364'
product: rm
source: tdn-rm
title: Composições Cópia de Itens
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385364
version: 2
---

---

Esta opção possibilita a cópia de composições do projeto escolhido para o projeto aberto, podendo copiar do próprio projeto aberto. Se o projeto corrente for um projeto global, só será possível copiar grupos de custo, insumos ou composições.

**Dados do Projeto de Origem:**  
 Coligada: Coligada do projeto de origem da cópia.  
 Projeto: Projeto de origem da cópia.

**Composições:**  
 Escolha uma ou mais composições que deseja copiar.

**Observação:**  
 Os filtros criados na visão de composições serão visualizados na cópia de itens e vice-versa.

**Copia Preços:**  
 Quando a cópia de composições é feita sem a prévia cópia de insumos e seus preços, os insumos que são recursos das composições importadas, são importados automaticamente.  
 Essa opção permite definir como será a importação de preços.  
 Informe como será a cópia de preços marcando a opção desejada: "Copiar Todos os Preços", "Copiar Apenas Preço Ativo" ou "Nenhum".

**Copiar recursos globais como locais:**  
 Esse campo permite que os recursos globais das composições globais sejam copiados como recursos locais.  
 Esse campo só fica visível quando o projeto origem é projeto global e está sendo copiado para a mesma coligada.

**Aplicação da máscara de destino em projetos com máscaras diferentes:**  
 Levando em consideração as possibilidades para aplicação de máscara para composição entre projetos diferentes serão adotadas as seguintes normas.

1. Projeto Origem sem máscara e Projeto Destino com máscara definida. Caso o tamanho do código adotado pelo conjunto de composições selecionadas não ultrapasse a máscara adotada pelo projeto de destino, todos os itens terão a máscara aplicada pelo projeto destino.
2. Projeto Origem com máscara menor que a máscara do Projeto Destino. Todas as composições terão a máscara do projeto de destino aplicada.
3. Projeto Origem com máscara maior que a máscara do Projeto Destino. A cópia será abortada por não haver possibilidade da máscara do projeto de destino ser aplicada efetivamente.
4. Projeto Origem sem máscara e projeto Destino sem máscara Todos os itens que fazem parte do conjunto de composições selecionadas serão copiados.

**Observações:**  
 Na cópia de Composições é necessário definir como será o preenchimento de lacunas no código de insumos e composições (com zeros à direita ou à esquerda).

Durante o processo de cópia das composições e aplicação da máscara de composições no projeto de origem pode coincidir que o código gerado já esteja presente na tabela de destino, desta forma este item não será copiado por haver um conflito de códigos.

Caso o projeto de destino não possua máscara para composições e utilize para diferenciar os códigos da composição apenas caracteres especiais –Exemplo: "11.70" e "11,70", apenas o primeiro será copiado caso não exista na tabela.

Na cópia de Composições, pode-se solicitar a localização do item por código ou descrição.

Na cópia de Composições pode-se alterar a ordenação dos registros. Para isso basta clicar no título da coluna.

Na cópia de Composições é necessário definir como será o preenchimento de lacunas no código de insumos (com zeros à direita ou à esquerda).

Se já existir alguma tarefa cadastrada, a máscara de tarefas não será copiada.

Através de duplo clique sobre a composição, você pode visualizá-la.

**Atenção:**  
 Na cópia de Composições, caso o registro já exista, pode-se selecionar a opção "Sobrepor" ou "Ignorar". A opção "Sobrepor" irá atualizar o registro e a opção "Ignorar" manterá o registro existente. Atenção ao utilizar a opção "Sobrepor" pois os rercursos existente na composição serão alterados.

**Exemplo:**  
 Projeto A -> Composição A - Recurso de código F00001 - Descrição: Servente Projeto B -> Composição B - Recuros de código F00001 - Descrição: Motorista Realizando copia de composição do projeto B para o A, marcando a opção sobrepor será copiada a Composição A para o projeto B, porém o insumo passará a ser de código F00001 - Descrição: Motorista no projeto B e em todas as composições onde o insumo é utilizado.

Copiar insumos derivados  
 Ao desmarcar o parâmetro "Copiar insumos derivados" os insumos Derivados do projeto de Origem não serão criados ou substituídos no Projeto de Destino, caso um insumo de mesmo código exista no projeto de destino o mesmo será associado a composição.
