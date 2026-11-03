---
content_hash: 6ac54ca7544e52622ac43f7167859ec73ba9dcba5deb1a210fbfb002f434ae6f
fetched_at: '2026-06-29T00:09:14.986787+00:00'
page_id: '421385327'
product: rm
source: tdn-rm
title: Serviços Copia de Itens
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385327
version: 4
---

---

Esta opção possibilita a cópia de serviços do projeto escolhido para o projeto aberto, podendo copiar do próprio projeto aberto.

Dados do Projeto de Origem: Coligada: Coligada do projeto de origem da cópia. Projeto: Projeto de origem da cópia.

Serviços: Escolha um ou mais serviços que deseja copiar.

**Observação:**  
Os filtros criados na visão de tarefas serão visualizados na cópia de itens e vice-versa.

O projeto destino deve possuir a mesma máscara que o projeto origem. Se a obra não existir no projeto destino, cadastre-a antes da importação ou marque a opção 'Gerar Códigos Superiores'.

Para copiar etapas, marque a opção "Habilitar etapas". Dessa maneira, todas as etapas serão disponibilizadas para cópia. Marcar a etapa não implica na cópia dos serviços de nível inferior (tarefas filhas), portanto, os serviços a serem copiados também deverão ser selecionados. Se desejar marcar outros serviços, além daqueles marcados por essa opção, utilize o Ctrl + Clique.

Para criar, automaticamente, as tarefas superiores (etapas e obras) ao código dos serviços selecionados marque a opção "Gerar Códigos Superiores (tarefa pai) (quando não for encontrado)". Ao marcar o campo "Copiar Cronograma Previsto" será copiado também os dados do cronograma previsto daquele(s) serviço(s). Pode-se copiar este(s) serviço(s) para uma outra obra, preenchendo o campo "Novo Código da Obra".

Se desejar, preencha um valor no campo "Multiplicar Valor Cotado por", e os serviços que tiverem valor cotado terão esse valor multiplicado pelo valor informado.

Na cópia de serviços, se já existir alguma tarefa cadastrada e a máscara do serviço a ser importado for diferente da máscara do projeto destino, os serviços não serão importados. Se a máscara estiver definida mas, não houver serviço cadastrado, a máscara e os serviços serão importados.

Copia Preços: Quando a cópia de serviços é feita sem a prévia cópia de composições, insumos e seus preços, as composições e os insumos utilizados nos serviços importados, são importados automaticamente.Informe como será a cópia de preços marcando a opção desejada: "Copiar Todos os Preços", "Copiar Apenas Preço Ativo" ou "Nenhum".

Os percentuais de associação entre tarefas só serão copiados na cópia detalhada.

**BIM:** Somente serão copiados os dados das associações de tarefas com objetos do modelo BIM associado. A cópia só será realizada se existir no projeto destino a associação do mesmo arquivo do BIM relacionado ao projeto origem, isto é, o arquivo deverá estar compartilhado entre os projetos.

**Observações:**  
Na cópia de Serviços, após a cópia, o sistema continua com a seleção anterior permitindo a cópia para outra obra. Na cópia de Serviços, pode-se solicitar a localização do item por código ou descrição. Na cópia de Serviços, pode-se alterar a ordenação dos registros. Para isso basta clicar no título da coluna. Na cópia de Serviços, indiretamente são feitas as importações dos recursos (composições e seus insumos) que estão associados a eles e dos seus grupos de custo. Portanto, para esses, a opção "Ignorar" e "Sobrepor" é válida para o recurso que estiver associado e não para a Obra. Na cópia de Serviços, caso o registro já exista, pode-se selecionar a opção "Sobrepor" ou "Ignorar". A opção "Sobrepor" irá atualizar o registro e a opção "Ignorar" manterá o registro existente. Na cópia de Serviços é necessário definir como será o preenchimento de lacunas no código de insumos (com zeros à direita ou à esquerda).

Se já existir alguma tarefa cadastrada, a máscara de tarefas não será copiada.

Os centros de custo e departamento das tarefas serão copiados somente se o centro de custo e departamento do projeto origem for igual ao centro de custo e departamento do projeto destino.

**Exemplo:**  
Considere o serviço 001.01.02 que tem a composição 000001 associada, que por sua vez, é composta dos insumos E00001, F00001, M00001 e V00001. O serviço é copiado. Caso a composição e os insumos existam e a opção "Sobrepor" esteja marcada, serão copiados os insumos e a composição sobre os que existiam. Caso a opção "Ignorar" esteja marcada, somente o serviço será copiado.

Considere que o serviço 001.01.03 que tem a composição 000002 associada, que por sua vez, é composta dos insumos F00001 e M00010 já exista no projeto.

Ao selecionar um serviço de mesmo código (001.01.03) para cópia e a opção "Ignorar" esteja marcada, o serviço não será copiado e serão copiados os insumos e a composição caso os mesmos não existam no projeto.
