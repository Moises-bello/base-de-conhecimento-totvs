---
content_hash: 6aa9a7cf9c27619327a6c73f47e7996d495b0d6ac97970a8e89e9849f577b5d6
fetched_at: '2026-06-29T00:09:15.264889+00:00'
page_id: '421385328'
product: rm
source: tdn-rm
title: Insumos Copia de Itens
type: documentation
url: https://tdn.totvs.com/display/LRM/Insumos+Copia+de+Itens
version: 2
---

---

Esta opção possibilita a cópia de insumos do projeto escolhido para o projeto aberto, podendo copiar do próprio projeto aberto.

Dados do Projeto de Origem: Coligada: Coligada do projeto de origem da cópia. Projeto: Projeto de origem da cópia.

Insumos: Escolha um ou mais insumos que deseja copiar.

**Observação:**  
 Os filtros criados na visão de insumos serão visualizados na cópia de itens e vice-versa.

Informe como será a cópia de preços marcando a opção desejada: "Copiar Todos os Preços", "Copiar Apenas Preço Ativo" ou "Nenhum". Essa opção inclui, também, a cópia dos campos livres e o campo "Descrição Completa".

Os relacionamentos dos insumos com os produtos do Suprimentos/Faturamento só serão importados se ambos estiverem integrados, ou seja, no menu Opções | Parâmetros | RM Solum deve estar informado se a integração está ativa e o tipo de movimento que será gerado.

Entre coligadas a copia de insumos com os produtos do Suprimentos/Faturamento será copiada desde que à coligada origem e à coligada destino estejam parametrizadas para trabalhar com produto global. Parâmetro este, definido no TOTVS Gestão de Estoques, Compras e Faturamento.

O código do insumo será importado de acordo com a máscara do projeto destino. Você pode definir se o preenchimento de lacunas eventuais no código será preenchida com zeros à esquerda ou à direita do código do insumo importado.

**Exemplo:**  
 Se a máscara de insumos do projeto destino for ###### e o insumo a ser importado for 00001, ao solicitar o preenchimento da lacuna no código à esquerda, o insumo será importado com o código 000001 e à direita será 000010.

Se a máscara de insumos do projeto destino for L##### e o insumo a ser importado for A0001, ao solicitar o preenchimento da lacuna no código à direito, o insumo será A00010 e à esquerda será 0A0001 mas, como os dois primeiros caracteres desse código não se aplica à máscara, será solicitado o caractere (nesse caso, somente letras) que substituirá o primeiro e, logo em seguida, o caractere (nesse caso, somente números) que substituirá o segundo.

**Observações:**  
 Na pasta Defaults, a faixa de códigos de insumos obedecerá a máscara de insumos definida no menu Opções | Parâmetros | RM Solum | Projetos | Pasta Exibição do Projeto Destino.Quando um caractere do código a ser importado não estiver de acordo com a máscara será solicitado um código correspondente para a posição em que ele se encontra.

Caso a máscara seja definida com caracteres numéricos e o código a ser importado seja um caractere alfa será solicitado o código correspondente, ou seja, se a máscara é numérica e o código a ser importado é A00001, ao informar como código correspondente ao A o número 9, todos os insumos que possuam esse caractere nessa posição, terão o A substituído por 9. O contrário também pode ocorrer. A máscara pode ser definida com caracteres alfa e o código a ser importado ser um caractere numérico. Na cópia de Insumos, pode-se solicitar a localização do item por código ou descrição.

Na cópia de Insumos, pode-se alterar a ordenação dos registros. Para isso basta clicar no título da coluna. Na cópia de Insumos, caso o registro já exista, pode-se selecionar a opção "Sobrepor" ou "Ignorar". A opção "Sobrepor" irá atualizar o registro e a opção "Ignorar" manterá o registro existente. Na cópia de Insumos é necessário definir como será o preenchimento de lacunas no código de insumos (com zeros à direita ou à esquerda).
