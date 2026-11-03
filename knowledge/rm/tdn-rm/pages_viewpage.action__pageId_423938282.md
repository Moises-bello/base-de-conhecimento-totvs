---
content_hash: 23d7435afba0e2650ca795ee015fdccef03c010d4851a5cc1460f999a365879f
fetched_at: '2026-06-29T00:09:26.154777+00:00'
page_id: '423938282'
product: rm
source: tdn-rm
title: Integrar Aquisições Compras
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938282
version: 10
---

Este processo tem como objetivo integrar as compras de imobilizados realizadas pelo sistema de Compras/Estoque (RM Nucleus) com o Sistema de Gestão Patrimonial, cadastrando os patrimônios e preparando os mesmos para cálculos de depreciação, inventário etc.

Após a integração dos bens, o sistema não fará cálculos de depreciação automaticamente. O usuário terá que disparar os cálculos.

a,b,c,d,eaOpções de seleção (Filtros)

Utilize uma ou mais opções de filtro para seleção dos movimentos que deseja integrar com o módulo patrimonial:

* Data - Essa data será utilizada para preenchimento do campo Data de Aquisição do Patrimônio. Como default é apresentado o período patrimonial em aberto.
  + Data de emissão da nota
  + Data de Entrada/saída da nota
* Número do documento
* Filial
* Tipo de Movimento
* Fornecedor

bSeleção de notas

Nesta etapa aparecerão todos os movimentos que atendem aos filtros utilizados na etapa anterior. Inclua aqueles que deseja integrar e clique em Avançar.

cTipos de Campos

Nos campos **Descrição do Patrimônio**, **Considerar no Valor de Aquisição** e **Considerar no Valor Base de Depreciação**, selecione uma das opções da lista para preenchimento dos mesmos no Patrimônio que será criado.

Algumas considerações sobre as opções:

* **Preço unitário:** O **Preço Unitário** do item do movimento será utilizado para preenchimento do campo onde for selecionado. (TITMMOV.PRECOUNITARIO)
* **Valor unitário:**O **Valor Unitário** do item do movimento será utilizado para preenchimento do campo onde for selecionado. (TITMMOV.VALORUNITARIO)
* **Valor Financeiro:** O **Valor Financeiro** do item do movimento será utilizado para preenchimento do campo onde for selecionado. (TITMMOV.VALORFINANCEIRO)
* **Fórmula Valor do Patrimônio:** Os valores calculados à partir das fórmulas definidas nos parâmetros do TOTVS Gestão de Estoque, Compras e Faturamento, calculados durante a inclusão do Movimento, serão utilizados para preenchimento do campo onde for selecionado. (Valor de Aquisição = TITMMOV.VALORBEM; Valor Base de Depreciação = TITMMOV.VALORBASEDEPRECIACAOBEM)

Essas fórmulas devem retornar o valor unitário do bem.

**Incluir patrimônio mantendo as quantidades informadas nos Itens da Nota**

Ativando esta opção ao realizar a integração o sistema manterá os patrimônios agrupados, realizando apenas um único cadastro para o patrimônio no sistema de Gestão Patrimonial com a quantidade exatamente igual à quantidade informada para o item do movimento.

*Exemplo:*

*Uma compra de 10 unidades do item "Cadeira com Encosto":*

* *Ao ser integrada com este parâmetro marcado, será criado apenas **um** Patrimônio contendo 10 unidades da cadeira.*
* *Ao ser integrada com este parâmetro desmarcado, serão criados **dez** Patrimônios, cada um com 1 unidade.*

Não ativando esta opção o sistema criará um Patrimônio para cada unidade do item do movimento.

IMPORTANTE!

Se o item do movimento possui fração (casas decimais), o comportamento do sistema será o seguinte.

*Exemplo:*

*Considere uma compra com os seguintes itens:*

* *1,50 unidades do item "Ferro"*
* *0,37 unidades do item "Aço"*
* *0,74 unidades do item "Alumínio"*

*Ao realizar a integração com essa opção MARCADA, o Sistema de Gestão Patrimonial criará 3 patrimônios com as mesmas quantidades de cada item da nota:*

* *"Ferro"         quantidade = 1,5*
* *"Aço"           quantidade = 0,37*
* *"Alumínio"   quantidade = 0,74*

*Com ela DESMARCADA, o Sistema desmembrará os itens e criará 4 patrimônios sempre com quantidade inteira:*

* ***"Ferro"       quantidade = 1***
* ***"Ferro"       quantidade = 1***
* *"Aço"           quantidade = 1*
* *"Alumínio"   quantidade = 1*

**Gerar código do bem e do patrimônio automaticamente**

Marcando esta opção o sistema irá gerar o número do patrimônio e o código do patrimônio automaticamente respeitando sempre o grupo Default cadastrado no Grupo de Patrimônios do patrimônio. O número do patrimônio irá receber o maior valor inteiro da base acrescido de 1, porém se não houver valores inteiros receberá 1. Vale ressaltar que o número do patrimônio é gerado automaticamente considerando os parâmetros de sistema, por exemplo, ele não será 1 se o sistema estiver parametrizado para gerar o número do patrimônio igual ao código do patrimônio.

Se esta opção não for marcada a integração ficará pendente para edição no menu Integrar Aquisição Pendente.

**Considera a falta do Grupo de patrimônios como erro**

Esta opção funciona como uma segurança para você realizar sua integração sem erros. Ao marcá-la o sistema irá conferir se **todos** os produtos da nota fiscal que você está integrando estão com seus grupos de contas cadastrados. Caso algum patrimônio não esteja com o Grupo de patrimônios cadastrado o sistema NÃO integrará nenhum patrimônio desta nota.

Caso você opte por não marcá-la o sistema fará a integração parcial dos patrimônios, ou seja, somente para aqueles que estivem com seu Grupo de patrimônios informado. É um bom recurso quando desmarcada pois facilitará quando existir uma nota fiscal contendo alguns itens para serão imobilizados e outros não.

**Gerar o código do patrimônio a partir do título do patrimônio definido no produto**

Com esta opção o sistema usará o default de Grupo de patrimônios direto dos cadastros de produto no RM Nucleus no lugar do default informado em "Cadastros Grupo de patrimônios Contábeis" do módulo Patrimonial.

Quando a composição do Patrimônio contem, **Produtos** com **Código Grupo/ Titulo Amarrado diferentes** o código do patrimônio será gerado de acordo com o **"Código de Patrimônio"** definido na tela "Composição de Patrimônio /  aba Patrimônio.

**Criar cenários e calcular depreciação durante a inclusão**

Se esta opção for desmarcada a Integração não criará os Cenários e calculará as Depreciações automaticamente ao criar os Patrimônios. Ficará a cargo do usuário realizar estas inclusões em momento posterior. Isto não se aplica caso a integração fique pendente (parâmetro "**Gerar código do bem e do patrimônio automaticamente**" desmarcado). Neste caso, quando Integrar a Aquisição pendente os cenários serão criados por default.

**Construir patrimônios a partir dos itens da nota**

Não será possível marcar essa opção quando for selecionada mais de uma nota fiscal.

Quando a opção "Construir patrimônio a partir dos itens da nota" estiver marcada, as opções "**Incluir patrimônio mantendo as quantidades informadas nos itens da nota**" e "**Considera a falta do grupo de patrimônio como erro**" ficarão desabilitadas, pois estas informações poderão ser preenchida no momento da constituição do novo patrimônio.

Ao acionar a opção "Constituir patrimônio a partir dos itens da nota" será aberta automaticamente a tela de constituição do patrimônio, será possível também acionar essa tela clicando no botão "**Composição de Patrimônios**".

Para saber mais sobre o recurso clique .

Atenção:  
Ao integrar o Sistema de Gestão Patrimonial com o sistema de Compras/Estoque, o sistema estará validando se o patrimônio está com o título inativo, ou seja, se no sistema de Compras estiver utilizando um Grupo de patrimônios que possui um título inativo no Sistema de Gestão Patrimonial, não será possível concluir a integração.

Esta condição é verdadeira desde que a preferência "Não incluir bens em títulos INATIVOS" esteja habilitada.

**Exclusão de Patrimônio originado do Gestão de Compras:**  
Ao realizar exclusão de patrimônio originado do Gestão de Compras, o sistema irá automaticamente excluir todos registros vinculados aquela nota.  
 

Veja Também

* Patrimônios
* Integrar Aquisições Pendentes
