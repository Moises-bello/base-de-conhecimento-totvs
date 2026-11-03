---
article_id: 23158905977239
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 54fe62cde76dd95ba88ea1a5a63770e6d7e63fc568888eb4c311709458771d27
fetched_at: '2026-06-28T22:42:42.355506+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Exemplo de Configurador de Produto
type: support-article
updated_at: '2024-04-30T20:32:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23158905977239-Manufatura-Linha-Protheus-SIGAPCP-Exemplo-de-Configurador-de-Produto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23158961686679) Tempo aproximado para leitura: **00:07:00 min****Dúvida**Como realizar o cadastro para utilizar o **Configurador de Produtos**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**O objetivo de utilizar o conceito de **Configurador de Produtos** é padronizar o cadastro de produtos e estruturas para facilitar a localização dos cadastros.

Vamos utilizar como exemplo, uma empresa que fabrica calça *jeans*.

No **MATA093 - Configurador de Produtos**, realizamos o cadastro conforme a imagem abaixo:

![1.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/23165650765207)

Para cada uma das características deve ser especificado as opções que existem. Neste exemplo, as modelagens que podem existir, tipo do jeans e tamanho, ou seja, o que for pertinente àquele produto.  
A definição das opções de cada característica é feita por meio da rotina **MATA099 - Conjuntos**. As opções de uma característica podem ser definidas de maneira:   
**Manual** - para a característica descrever todas as opções que existem;  
**Conjunto** -  quando já tem uma tabela de opções e preciso informar com qual dessas tabelas essa característica está vinculada. Exemplo: em uma tabela de modelagem, dizer que a característica 0001 deve permitir as modelagens cadastradas nessa tabela de modelagens;  
**Intervalo** - se uma característica tiver um valor numérico, informar qual o valor mínimo e máximo e qual o intervalo. Exemplo, para a característica do tipo tamanho, informar o tamanho mínimo de 34, o máximo de 48 com um intervalo de 2. Isso quer dizer que haverá a calça jeans dos tamanhos, 34, 36, 38, 40, 41 assim por diante, até o 48;  
**Cópia** - copia as opções que já foram configuradas para outro produto ou outra característica para o produto atual.

Então, voltando ao exemplo, para definir uma característica como **Manual**, seguiria os passos abaixo, para a modelagem, no **MATA098 - Codificação**:

![2.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/23165650780311)

![3.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/23165650797335)

Observe que o número de caracteres do campo **Cod Caracter.** é limitado. Esta limitação é de acordo com o tamanho da característica definido no **MATA093**.

![4.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/23165650804759)

Neste caso o tamanho do código das opções para Modelagem não pode exceder 2 caracteres.  
Para opções do tipo **conjunto**, deve-se cadastrar o conjunto no **MATA099**:

![5.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/23165704227351)

E no **MATA093** vincular o conjunto com a característica:

![6.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/23165704234647)

![7.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/23165650831639)

Para característica do tipo **Intervalo**, é especificado o valor mínimo, máximo e o intervalo entre eles, isto é, o incremento:

![8.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/23165650841239)

![9.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/23165650852119)

Neste exemplo, colocamos o valor **De** igual à 34 e o valor **Até** igual à 48. Isto significa que podem ser gerados produtos com tamanho 34, 36, 38, 40, 42, 44, 46 e 48, pulando a numeração de 2 em 2, conforme conteúdo do campo **Passo**.  
Definida a família, as características e as opções de cada característica, devem ser especificados os campos padrões do cadastro do produto.   
Este processo é realizado por meio da rotina **MATA093**, em **Outras Ações->Dados Padrões.**   
Nessa tela são determinados a descrição do produto, o tipo, unidade e armazém padrão, além dos componentes.

![10.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/23165650859671)

**Descrição do produto -** será parte da descrição, quando o produto for criado na tabela **SB1 - Produtos**, a descrição final será composta por essa informação com as demais informações das características selecionadas na composição do produto. Exemplo: Calça Jeans Skinny Destroied 38, onde Calça Jeans é a descrição padrão, Skinny a modelagem, Destroied o tipo de jeans e 38 o tamanho.  
Os componentes que podem ser incluídos nesta tela são aqueles usados em todos os códigos a serem gerados a partir do configurador. Outros exemplos: zíper e botão.![19.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/23166467110679)

No *Menu* **Outras Ações->Descrição** da rotina **MATA093**, pode-se mudar o formato do código do produto a ser gerado, lembrando que todas as variáveis devem estar contempladas. Para que seja possível utilizar esta opção do Menu, o campo **Cod. Padrão** deve ter o conteúdo **Não.**

![11.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/23165650869527)

Em **Outras Ações->Descrição**, no grid abaixo é possível determinar o conteúdo de outros campos do cadastro do produto, atribuindo valor ou chamando uma função de usuário.

![12.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/23165704283543)

Em **Outras Ações->Especificação** podem ser definidas regras de combinação, como por exemplo: a calça super skinny somente será feita até o tamanho 40, então o processo não irá gerar código 2641020142, que corresponderia a calça super skinny, tipo de jeans claro, tamanho 42.

![13.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/23165704292631)

Já no grid abaixo, pode-se informar componentes adicionais que são usados na fabricação de uma característica específica, exemplo a caça de jeans intermediário terá um botão adicional:

![14.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/23165704300311)

Em **Outras Ações->Simulação**, é possível simular o processo de geração de um código de produto. Neste processo, a rotina apresenta a mesma tela que é apresentada em diversos processos do Protheus quando digitado o código da família.

![15.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/23165704310551)

Se nessa tela colocarmos as opções Modelagem 02 - Super Skinny,  Tipo de Jeans  01 - Claro e Tamanho 44:

![16.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/23166467130263)

Será apresenta a mensagem abaixo:

![17.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/23166453786519)

Isso porque essa combinação não é permitida, conforme regra de configuração especificada em **Outras Ações->Especificação.** Quando uma configuração é possível, o Sistema apresenta a tela abaixo, apresentando os dados da configuração e os componentes que serão empenhados:

![18.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/23166453798679)

![20.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/23166467176215)

Em **Outras Ações->Gera Autom**, o Sistema realiza todas as combinações de opções entre as características e apresenta na tela os códigos possíveis:

![21.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/23166733038743)

E marcando os códigos desejados, eles serão incluídos na tabela SB1, desde que, o campo **Disp. p/ Uso** esteja como **Sim**:

![23.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/23166733045911)

![22.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/23166733051671)

![24.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/23166796171927)
