---
content_hash: 09af8d282ac3ed6f333a0e7577e7a00915844d7ac704501c078037b4a00a5b33
fetched_at: '2026-06-29T00:06:06.506385+00:00'
page_id: '201731452'
product: rm
source: tdn-rm
title: ER_controle_de_retencoes_e_deducoes_contratuais
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_controle_de_retencoes_e_deducoes_contratuais
version: 4
---

## Objetivo

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Relatórios |
| **Segmento Executor** | Construção & Projetos | | |
| **Projeto1** | R\_C&P\_TOP007 | **IRM1** | PCREQ-5371 |
| **Requisito1** | PCREQ-5372 | **Subtarefa1** | PDR\_CP\_TOP007-1543 |
| **Chamado2** | Não se aplica | | |
| **Release de Entrega Planejada** | 12.1.7 | **Réplica** | Não |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Definir alterações no modelo atual de retenções e deduções que são enviados pelo módulo de contratos do TOTVS Obras e Projetos para o Backoffice.

## Definição da Regra de Negócio

* **Cenário Atual**

Será necessário realizar algumas adaptações no processo existente para atender a demanda do mercado.  

Atualmente o TOP permite que sejam informados valores de retenções e deduções para a liberação de medições. Este processo ocorre na liberação de períodos de contratos. Ao gerar um movimento para Suprimentos/Faturamento estes valores de deduções e retenções são levados em consideração sendo abatidos do valor medido e enviado um valor liquido (valor medido – (deduções + retenções)) segundo formula padrão de contrato “A” (protótipo 01).

O valor da medição feita no período do contrato, é enviada para o BackOffice de acordo com a formula inserida no cadastro do contrato, e por padrão a formula utilizada é “A – Valor Default” (soma todas as deduções e retenções e subtrai do valor medido).

Este procedimento dificulta a tratativa de tais valores uma vez que o valor tanto de retenção quanto de deduções, podem ter contabilizações em contas distintas, bem como impacto distinto no valor financeiro e em base de cálculo tributário.

 A incidência dos valores de deduções e retenções sobre o valor do Movimento (NF), valor financeiro, contabilização e base de cálculo fiscal/tributária deve ser definido no BackOffice portanto tais tratativas não devem ser contempladas no TOP. Para que o BackOffice possa determinar o comportamento de cada um dos elementos, é necessário que tais valores (deduções e retenções) sejam enviados separadamente.

 De forma geral, a mudança será no tratamento do valor total medido do contrato, enviando o valor total para o BackOffice (sem subtrair deduções e retenções), separando cada um dos valores redutores (dedução e do valor de retenção).

* **Cenário Proposto**

A seguir seguem requisitos de negócios analisados.

**1.** **Parametrização**

1.1.  No TOP

Atualmente no TOP nas telas de referencia a retenção e dedução está sendo utilizado o termo “retenção”. Para abranger o conceito, será alterado para o termo **retenção/dedução**, pois trata-se de itens que podem reduzir o valor enviado e/ou tratado no BackOffice. Desta forma entende-se como redutores os itens (valores) de adiantamento, dedução e retenção (Protótipo 08 e Protótipo 09).

Deverá ser criado nos Parâmetros de Projeto no tópico de contratos o parâmetro “Discriminar valores de retenção e dedução” (Protótipo 02). Este parâmetro será responsável por determinar se o TOP irá trabalhar utilizando o controle de Retenção/Dedução proposto nesta especificação (parâmetro marcado) ou se irá trabalhar da forma atual onde os valores de retenção e dedução não são enviados separados, mas serão tratados via fórmula de contrato (Subtraindo Dedução e Retenção).

**2.** **Contrato**

2.1.  No TOP

Por padrão novos contratos possuem associação automática a fórmula A – Valor default (C-G), que aplica o valor medido e subtrai as deduções e retenções na liberação do período. Mas quando o usuário define nos parâmetros de projeto que vai utilizar “Discriminar valores de retenção e dedução” a fórmula default para novos contratos passa a ser a fórmula C – Valor com reajuste (Protótipo 01). Porém esse parâmetro pode ser marcado em qualquer momento, sendo assim, o usuário pode marca-lo quando já possuir na base contratos ativos com fórmulas já cadastradas, e por este motivo o campo fórmula na aba de contratos, ficará habilitado para edição quando o usuário marcar a opção “Discriminar valores de retenção e dedução”, deixando flexível para o usuário modificar a fórmula ou continuar utilizando a fórmula anterior cadastrada.

É importante lembrar que a fórmula define como será a tratativa do valor medido enviado para o Nucleus, assim o usuário precisa definir uma fórmula que não tenha o abatimento dos redutores, pois caso contrário, pode ocasionar em problemas no processo.

**3.** **Retenção**

A Retenção Técnica serve para garantir a correta execução do serviço contratado. Se trata de um percentual a ser descontado do valor medido liberado periodicamente, mas que ao final do contrato ou de um período de prestação de serviço será liberado (pago ou recebido). Portanto seu controle passa por dois momentos já tratados pelo TOP, “liberação de Medição” e “liberação de Retenção”.

 3.1.  Processo 1 - Liberação da Medição

Onde o valor da retenção técnica pode ou não ser abatido do valor a ser enviado para o BackOffice. Se o valor enviado ao BackOffice será liquido ou bruto deve ser determinado pelas “fórmulas” do contrato (Protótipo 01).

3.1.1.         No TOP

3.1.1.1.    Alteração de tela

Não haverá Alteração de na tela de Liberação de Período, as deduções e retenções serão informadas nos devidos campos já disponibilizados. (Protótipo 03)

A tela de liberação de retenção teve algumas alterações, pois é necessário informar ao usuário quais produtos do rateio na liberação do período foram utilizados. Assim quando o usuário solicitar a liberação da retenção, será mostrado no campo “Produto(s) Relacionado(s)”, os produtos que estiveram na liberação do respectivo período. (Protótipo 06)

 3.1.1.2.    Valor Bruto (Cheio)

O valor Bruto será determinado pelo item “C – Valor com reajuste” do cadastro de fórmula (cadastro do Contrato aba Fórmulas). Para contratos ativos com formulas diferentes, será possível a modificação da formula pois o campo estará habilitado para edição.

 3.1.1.3.    Envio para o Nucleus

O envio do movimento com o valor da medição pode ter influencias de rateio de produto. Os rateios podem ser cadastrados na associação de tarefas ao contrato ou na medição por tarefa ou na tela de medição informando o produto padrão. Quando o usuário decide utilizar o rateio ele tem a seguintes opções:

* Rateio Padrão: É necessário que o usuário informe por tarefa quais produtos e qual o percentual aplicável na respectiva tarefa, é importante lembrar que o percentual de rateio para as tarefas precisam fechar na totalidade em 100%, senão o TOP não deixará que a liberação seja feita.
* Rateio especifico por medição: Na medição de tarefa o usuário poderá informar o rateio especifico da tarefa naquele período. É importante lembrar que o percentual de rateio para as tarefas precisam fechar na totalidade em 100%, senão o TOP não deixará que a liberação seja feita.
* Produto padrão: Na liberação o usuário poderá informar o produto padrão da liberação, assim o TOP irá enviar o valor da medição associado em 100% no produto informado.

No processo de envio para o Nucleus o TOP irá somar todas as medições de tarefas, e no processo de liberação o usuário pode informar quais serão os valores de retenção e dedução (Protótipo 03) que serão redutores da liberação. Ao informar todos os dados necessários, o processo do TOP irá enviar o valor total da medição (separando produto e percentual de rateio) e separar as deduções e as retenções enviando para o Nucleus.

Quando o usuário informa a retenção na liberação é criado um registro do mesmo período no anexo de retenção do TOP. Esse processo de retenção pode ser liberado depois que o movimento gerado pelo Nucleus esteja com status de “Faturado/Recebido”. Quando o movimento de liberação é Faturado, e o usuário decide liberar a retenção na visão de retenção irá exibir os produtos que serão rateados na Liberação (Protótipo 06).

 3.1.2.         No Suprimento/Faturamento

Na geração do Movimento deve ser enviado o valor da retenção no item do movimento, separado das demais deduções, o usuário pode visualizar o valor retido editando o item de movimento, como demostrado na Protótipo 04, este campo não poderá ser editado. A retenção técnica sofre incidência de impostos e não desconta do valor total do movimento (NF compra ou venda), e será descontando apenas do valor financeiro. Tais características podem ser tratadas no Suprimento/Faturamento através dos recursos já existentes, pois é permitido ao usuário determinar a composição do valor do Movimento, do Valor Financeiro e da base de cálculo de impostos tudo através de fórmulas.

 3.2.  Processo 2 - Liberação da Retenção

Depois que os serviços são prestados e aferida a qualidade dos mesmos, há liberação da retenção que deve gerar um movimento.

**Importante:**

**O processo de liberação de retenção deverá ser modificado da seguinte forma:**

**Se o parâmetro “Discriminar valores de retenção e dedução” estiver marcado, os produtos que deverão ser considerados na geração do movimento são os mesmos utilizados no movimento que foi gerado a liberar a medição do período e essa informação deverá ser exibida ao usuário na tela do processo e não o produto default (Protótipo 06).**

3.2.1.         No TOP

3.2.1.1.    Parâmetro de Tipo de Movimento

Criar Parâmetro para informar qual o tipo de movimento do Suprimento/Faturamento será gerado a partir da “Liberação de Retenção”, este parâmetro pode estar presente no cadastro do contrato / Aba Default (Protótipo 05). Tal demanda se justifica, pois o tipo de movimento de retenção não é o mesmo tipo de movimento da liberação de uma medição.

3.2.1.2.    Não liberação do Valor Total Retido

Nessa primeira proposta não estará disponível a Liberação de parte de uma retenção. Pode ocorrer em determinado cenário, que parte de um serviço prestado não ter sido satisfatório, acarretando a não liberação da retenção em sua integralidade. Neste caso não será possível a liberação de parte da retenção, apenas o pagamento/recebimento do valor total ou a não liberação do valor total.

3.2.2.         No Suprimento/Faturamento

O movimento de NF a ser vinculado aos itens de movimento de retenção deve ter as informações referente a estado e município preenchidas para que a liberação da retenção será realizada.

3.3.  Solução para o processo de retenção proposta pelo RM Nucleus

**O processo:**

O Controle de Retenções terá na gestão de Materiais, basicamente três tipos de movimentos, sendo:

O movimento de medição é recebido / faturado para o de nota fiscal. O faturamento pode ser agrupado ou individual.

O movimento de Retenção a Pagar / a Receber será vinculado ao movimento de nota fiscal.

**Medição a Pagar (1.1) ou Medição a Receber (2.1)**

* Esses tipos de movimentos podem ser gerados através da integração com o TOP (envio para Materiais) ou incluídos diretamente na gestão de Materiais;
* O preço unitário do item será o valor do serviço medido, ou seja, valor cheio, sem qualquer redução.
* Ele será parametrizado para utilizar Retenção Técnica por item de movimento, que poderá ser registrado em  Valor ou Ambos (mesmo tratamento do campo de desconto).
* Se o tipo de movimento estiver parametrizado para integração com o TOP, o valor do serviço e o valor da Retenção Técnica serão carregados através da integração e não poderão ser editados no módulo de Materiais.
* Somente tipos de movimentos não integrados com o TOP poderão editar esses campos no módulo de Materiais.

**NF Entrada – Serviço PJ (1.2) ou NF Saída Prestação Serviços (2.2)**

* Esses tipos de movimentos serão gerados através do recebimento ou faturamento dos movimentos de Medição (processo nativo do Materiais);
* Além dos parâmetros de utilização  da Retenção citados acima, terão também a parametrização quanto a Vinculações / Classificação de Vinculação = Retenção (novo) (Prototipo 07).  Este tipo de movimento que irá alimentar o controle de vinculações entre movimentos da gestão de Materiais.
* O campo VALORMOVIMENTO  da tabela TVINCULOMOV será carregado com a soma dos valores de Retenção Técnica  do item de movimento (procedimento diferente do controle de adiantamento).
* Este movimento, além da integração com o TOP terá também integração: Fiscal, Financeira e Contábil. Para facilitar a utilização do valor da Retenção Técnica nos processos de integração, será criada uma função de fórmula para retornar a soma do valor de Retenção Técnica de todos os itens do movimento.

**Retenção a Pagar (1.2.) ou Retenção a Receber (2.2)**

* Esses tipos de movimentos podem ser gerados através da integração com o TOP (processo de Liberação de Retenção) ou incluídos diretamente na gestão de Materiais;
* Terá a parametrização quanto a Vinculações / Tipo de Vinculação = Controlar Retenção;
* O vinculo atualizado na tabela TVINCMORELAC deverá ser com o movimento de nota fiscal (1.2 ou 2.2), que foi gerado através do faturamento do movimento de medição.

Obs.: Atenção para os movimentos gerados através da integração com o TOP, pois o mesmo deve verificar a rastreabilidade entre movimentos para passar o movimento corretamente. Deve-se passar como movimentos origem, o movimento da cadeia de recebimento/faturamento que tenha parametrizado  campo: Vinculações / Classificação de Vinculação = Retenção.

* O preço unitário do item será o valor da retenção. Em movimentos integrados com o TOP, esse campo será carregado através da integração e não poderá ser editado na gestão de Materiais.

A solução da Retenção dentro do TOTVS Suprimento e Faturamento funcionará independentemente da integração com o TOP, ou seja, se os tipos de movimento forem parametrizados corretamente, a retenção poderá ser utilizada mesmo se o cliente não tiver o TOP.

Para que a solução da Retenção seja utilizada pelo TOP será necessário que o tipo de movimento esteja com as parametrizações demonstradas no Protótipo 07. Com o parâmetro “Informa Projeto/Tarefa” diferente de “Não Informa” (etapa Projetos do parametrizador). O parâmetro “Usa Retenção” também precisa estar marcado assim como o tipo de Retenção (Valor ou Ambos) deve ser selecionado (etapa Item – Valores Financeiros 2/2). A função de fórmula “TVIM” permitirá que se some todas as retenções dos itens a partir do movimento, para que sejam feitos os cálculos necessários. Depois do movimento faturado, e for necessário a liberação da Retenção, o TOP irá realizar a recuperação dos produtos do movimento de Solicitação de compra e o mesmo irá identificar o percentual do valor do item no total do movimento e aplicará a devida retenção em cada produto. Seguindo o Exemplo abaixo:

**Liberação Periodo 001** – Valor R$ 1000

**Retenção de período 001** – Valor R$ 300,00

Tarefas Envolvidas

**01.01.01** – Tarefa A  |  Medição= R$ 300

Produtos Associados –         01.01 Produto A 50%

                                                   01.02 Produto B 50%

**01.01.02** – Tarefa B |  Medição= R$ 300

Produtos Associados –         01.01 Produto A 50%

                                                   01.02 Produto B 50%

**01.01.03** – Tarefa C |  Medição= R$ 400

Produtos Associados –         01.03 Produto C 100%

Solicitação de compra: R$ 1000,00

Rateio no movimento:

Item 1:    01.01 – Produto A | Valor R$ 300,00 – Valor somado da tarefa A e B | Retenção: R$ 90

Item 2:    01.02 – Produto B | Valor R$ 300,00 – Valor somado da tarefa A e B | Retenção: R$ 90

Item 3:    01.03 – Produto C | Valor R$ 400,00 – Valor da tarefa C                        | Retenção: R$ 120

Na Liberação de Retenção: R$ 300,00

Item 1:    01.01 – Produto A | Valor R$ 90,00

Item 2:    01.02 – Produto B | Valor R$ 90,00

Item 3:    01.03 – Produto C | Valor R$ 120,00

Se o tipo de movimento estiver integrado com o TOP, os campos da Retenção permanecerão desabilitados, não permitindo sua edição a partir do RMNucleus. Caso o tipo de movimento não esteja integrado, esses campos poderão ser editados.

A vinculação do movimento de retenção com o movimento de liberação da retenção funcionará da seguinte forma: A vinculação poderá acontecer entre movimentos do tipo Pedido (1.1.xx ou 2.1.xx) e Nota Fiscal (1.2.xx ou 2.2.xx). Os movimentos de retenção gerados pelo TOP são do tipo 1.1.xx, com isso a solução deverá trabalhar com três diferentes tipos de movimento.

O primeiro (1.1.xx) deverá ser parametrizado para integração com o TOP e para utilizar Retenção. O segundo (1.2.yy) corresponderá ao faturamento do primeiro (1.1.xx) e deverá ser parametrizado para integração com o TOP, Usar Retenção, e ter **"Classificação de Vinculação = Retenção" e "Tipo de Vinculação = Vazio"** (etapa Vinculações do parametrizador).

O terceiro será outro 1.1.zz, enviado pelo TOP e deverá estar parametrizado para integração com o TOP, Usar Retenção, e ter **"Classificação de Vinculação = Sem Classificação" e "Tipo de Vinculação = Controlar Retenção"**.

**Obs:** O movimento 1.X.zz (Retenção a pagar) e 2.X.zz(Retenção a receber), não necessariamente precisa ser de Nota Fiscal, os mesmos podem ser de outro tipo, como Ordem de compra/Ordem de venda.

**4.** **Dedução**

Uma dedução de contrato pode ser identificada de N formas através do “detalhamento de itens de retenção”, no entanto podem ser generalizadas em três categorias de deduções:

* Dedução de Adiantamento
* Dedução de Itens de Compra Direta (compra de material)
* Outras Deduções

Para este escopo o campo dedução estará visível apenas na aba Tributos do movimento informado no campo desconto como demostrado no protótipo 10. E não será considerado os três tipos de Categorias de deduções do BackOffice. Tipo de movimento do TOP para deduzir, necessariamente deverá estar parametrizado para usar despesa com valor ou ambos.

 

## Protótipo de Tela

**Protótipo 01**

**Protótipo 02**

**Protótipo 03**

**Protótipo 04**

**Protótipo 05**

**Protótipo 06**

**Protótipo 07**

 

**Protótipo 08**

**Protótipo 09**

**Protótipo 10**

## Fluxo do Processo

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
