---
content_hash: c3ff9477d443bba63c4a07696eecca5b17084b45e8eb31fd58214758e34c7b36
fetched_at: '2026-06-29T00:09:15.271831+00:00'
page_id: '421385330'
product: rm
source: tdn-rm
title: Obras Copia de Itens
type: documentation
url: https://tdn.totvs.com/display/LRM/Obras+Copia+de+Itens
version: 2
---

---

Esta opção possibilita a cópia de obras do projeto escolhido para o projeto aberto, podendo copiar do próprio projeto aberto.

Dados do Projeto de Origem:

Coligada: Coligada do projeto de origem da cópia.

Projeto: Projeto de origem da cópia.

Os projetos com a opção "Projeto Modelo" marcados em sua edição, ficarão disponíveis para cópia de itens, independentemente se o usuário possui acesso ao projeto ou não.

Obras: Escolha a obra que deseja copiar. Pode-se alterar o código da nova obra preenchendo o campo "Novo Código da Obra". Essa opção inclui, também, a cópia dos campos livres. Ao marcar o campo "Copiar Cronograma Previsto" será copiado também os dados do cronograma previsto daquela obra. A copia será realizada respeitando período e não de acordo com a data definida no projeto. Para efetuar a cópia de múltiplas obras, utilize a combinação de teclas CTRL + Clique. Essa cópia não permite a definição do código da obra, ou seja, a obra será copiada com o mesmo código.

Copia Preços: Quando a cópia de obras é feita sem a prévia cópia de composições, insumos e seus preços, as composições e os insumos utilizados nas obras importadas, são importados automaticamente.Informe como será a cópia de preços marcando a opção desejada: "Copiar Todos os Preços", "Copiar Apenas Preço Ativo" ou "Nenhum".

Copia de Pert  
 Ao copiar a obra para um projeto, o Pert da obra é copiado para reutilização.Foi criado um parâmetro para o usuário escolher se deseja copiar as ligações da tarefas.Caso o usuário escolha ,será feita uma copia fiel do Pert utilizado anteriormente.

**Observações:**

Na cópia de Obras pode-se solicitar a localização do item por código ou descrição. Na cópia de Obras pode-se alterar a ordenação dos registros. Para isso basta clicar no título da coluna. Na cópia de Obras, indiretamente são feitas as importações dos recursos (composições e seus insumos) que estão associados a eles e dos seus grupos de custo. Portanto, para esses, a opção "Ignorar" e "Sobrepor" é válida para o recurso que estiver associado e não para a Obra.

Na cópia de Obras é necessário definir como será o preenchimento de lacunas no código de insumos (com zeros à direita ou à esquerda).

Se já existir alguma tarefa cadastrada, a máscara de tarefas não será copiada.

Os centros de custo e departamento das tarefas serão copiados entre coligadas, somente se o centro de custo e departamento do projeto origem for igual ao centro de custo e departamento do projeto destino. Para copiar o Departamento, é necessário informar no projeto destino a filial na edição do projeto.

A opção "Sobrepor" do grupo "Item Existente", não funciona na cópia de Obras. A copia de tarefas sucessoras ocorrerá somente na copia da obra.Caso ocorra copia de uma obra A e esta tem referencia a uma obra B e não esta sendo copiada a obra B a referencia da obra B presente na obra A não é copiada.

**Exemplo:**

Considere o serviço 001.01.02 que tem a composição 000001 associada, que por sua vez, é composta dos insumos E00001, F00001, M00001 e V00001. O serviço é copiado. Caso a composição e os insumos existam e a opção "Sobrepor" esteja marcada, serão copiados os insumos e a composição sobre os que existiam. Caso a opção "Ignorar" esteja marcada, somente o serviço será copiado.
