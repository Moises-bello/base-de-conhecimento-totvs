---
content_hash: ff6fbc3b5d7c230ae4a776af4a393106749c741b48a4c541dcbdc180a07e075c
fetched_at: '2026-06-29T00:06:06.243262+00:00'
page_id: '201729394'
product: rm
source: tdn-rm
title: DT_Controle_de_Retencoes_Contratuais
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Controle_de_Retencoes_Contratuais
version: 3
---

# CONTROLE DE RETENÇÕES CONTRATUAIS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento |
| **Requisito (ISSUE):** | PCREQ-5372 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | Oracle/SQL |
| **Tabelas utilizadas:** | TMOV – Movimentos  TITMMOV – Itens de Movimento  TTMVEXT – Tipos de Movimento  TMOVRELAC – Relacionamento entre Movimentos  TVINCULOMOV – Movimentos Vinculados   TVINCMOVRELAC – Vínculo de Movimentos de Nota Fiscal e Adiantamentos |
| **Sistema(s) operacional(is):** | Windows 7 SP1 ou superiores. |
| **Versões/Release:** | 12.1.7 |

## Descrição

 Permitir que o usuário utilize o Controle de Retenções Contratuais.

**Desenvolvimento/Procedimento**

A Retenção Técnica  serve para garantir a correta execução do serviço contratado. Trata-se de um percentual  a ser descontado do valor medido liberado periodicamente, mas que ao final do contrato ou de um período de prestação de serviço será liberado (pago ou recebido).

 O TOTVS Obras e Projetos ao enviar um movimento para o TOTVS Gestão de Estoque, Compras e Faturamento, deverá informar o valor da retenção em campo específico do item de movimento, separado das demais deduções.

 A retenção técnica sofre incidência de impostos e não desconta do valor total do movimento (NF compra ou venda), e será descontando apenas do valor financeiro. Tais características podem ser tratadas no TOTVS Gestão de Estoque, Compras e Faturamento através dos recursos já existentes, pois é permitido ao usuário determinar a composição do valor do Movimento, do Valor Financeiro e da base de cálculo de impostos através de fórmulas.

O Controle de Retenções terá na gestão de Materiais, basicamente três tipos de movimentos, sendo:

 

 

O movimento de medição é recebido / faturado para o de nota fiscal. O faturamento pode ser agrupado ou individual.

 

O movimento de Retenção a Pagar / a Receber será vinculado ao movimento de nota fiscal.

  

**Medição a Pagar (1.1) ou Medição a Receber (2.1**

* Esses tipos de movimentos podem ser gerados através da integração com o TOP (envio para Materiais) ou incluídos diretamente na gestão de Materiais;
* O preço unitário do item será o valor do serviço medido, ou seja, valor cheio, sem qualquer redução.
* Ele será parametrizado para utilizar Retenção Técnica por item de movimento, que poderá ser registrado em % , Valor ou Ambos (mesmo tratamento do campo de desconto). Quando informado em %, o sistema irá calcular o valor aplicando o % informado sobre o Preço Unitário do respectivo item de movimento.
* Se o tipo de movimento estiver parametrizado para integração com o TOP, o valor do serviço e o valor da Retenção Técnica serão carregados através da integração e não poderão ser editados no módulo de Materiais.
* Somente tipos de movimentos não integrados com o TOP poderão editar esses campos no módulo de Materiais.

 

**NF Entrada – Serviço PJ (1.2) ou NF Saída Prestação Serviços (2.2)**

* Esses tipos de movimentos serão gerados através do recebimento ou faturamento dos movimentos de Medição (processo nativo do Materiais);
* Além dos parâmetros de utilização  da Retenção citados acima, terão também a parametrização quanto a Vinculações / Classificação de Vinculação = Retenção.  Este tipo de movimento que irá alimentar o controle de vinculações entre movimentos da gestão de Materiais.
* O campo Valor do Movimento  da tabela Movimentos Vinculados será carregado com a soma dos valores de Retenção Técnica  do item de movimento (procedimento diferente do controle de adiantamento).
* Este movimento, além da integração com o TOP terá também integração: Fiscal, Financeira e Contábil. Para facilitar a utilização do valor da Retenção Técnica nos processos de integração, será criada uma função de fórmula para retornar a soma do valor de Retenção Técnica de todos os itens do movimento.

 

**Retenção a Pagar (1.2.) ou Retenção a Receber (2.2)**

* Esses tipos de movimentos podem ser gerados através da integração com o TOP (processo de Liberação de Retenção) ou incluídos diretamente na gestão de Materiais;
* Terá a parametrização quanto a Vinculações / Tipo de Vinculação = Controlar Retenção;
* O vínculo atualizado na tabela Vínculo de Movimentos de NF e Adiantamentos deverá ser com o movimento de nota fiscal (1.2 ou 2.2), que foi gerado através do faturamento do movimento de medição.

  **Observação:** Atenção para os movimentos gerados através da integração com o TOP, pois o mesmo deve verificar a rastreabilidade entre movimentos para passar o movimento corretamente. Deve-se passar como movimentos origem, o movimento da cadeia de recebimento/faturamento que tenha parametrizado  campo: Vinculações / Classificação de Vinculação = Retenção.
* O preço unitário do item será o valor da retenção. Em movimentos integrados com o TOP, esse campo será carregado através da integração e não poderá ser editado na gestão de Materiais.

 

 **Observação:** O movimento de NF a ser vinculado aos itens de movimento de retenção deve ter as informações referente a estado e município preenchidas para que a liberação da retenção será realizada

A solução da Retenção dentro do TOTVS Gestão de Estoque, Compras e Faturamento funcionará independentemente da integração com o TOTVS Obras e Projetos, ou seja, se os tipos de movimento forem parametrizados corretamente, a retenção poderá ser utilizada mesmo se o cliente não tiver o TOTVS Obras e Projetos.

 Serão criados na tabela do item de movimento os campos Valor de Retenção e Percentual de Retenção para tratar o valor da retenção ou o percentual da retenção.

Para que a solução da Retenção seja utilizada pelo TOTVS Obras e Projetos será necessário que o tipo de movimento esteja com a seguinte parametrização:

 No módulo **Gestão de Estoque, Compras e Faturamento**, acessar o menu **Ambiente >> Parâmetros >> Gestão de Estoque, Compras e Faturamento**

1. Parâmetro **Informa Projeto/Tarefa** diferente de **Não Informa**: **Parâmetros de Projeto**

 

2.  Parâmetro **Usa Retenção** também precisa estar marcado assim como o **Tipo de Retenção** (**Valor, Percentual ou Ambos**) deve ser selecionado:  **Etapa Item – Valores Financeiros 2/2**.

 

 

3.  A função de fórmula **TVIM** permitirá que se some todas as retenções dos itens a partir do movimento, para que sejam feitos os cálculos necessários.

 

Para definir a Fórmula acessar o  módulo **Serviços Globais\Administração\Fórmulas**, selecionar o contexto de sistema: Gestão de Estoque, Compras e Faturamento e incluir um novo registro

 

 

 Nos parâmetros de tipo de movimento **Etapa Fin-Faturamento 3/6** campo **Fórmula do Valor a Ratear** informar a fórmula cadastrada. 

 

 

Se o tipo de movimento estiver integrado com o TOTVS Obras e Projetos, os campos da Retenção permanecerão desabilitados, não permitindo sua edição a partir do TOTVS Gestão de Estoque, Compras e Faturamento. Caso o tipo de movimento não esteja integrado, esses campos poderão ser editados.

 

 

A vinculação do movimento de retenção com o movimento de liberação da retenção funcionará da seguinte forma: A vinculação poderá acontecer entre movimentos do tipo Pedido (1.1.xx ou 2.1.xx) e Nota Fiscal (1.2.xx ou 2.2.xx). Os movimentos de retenção gerados pelo TOTVS Obras e Projetos são do tipo 1.1.xx, com isso a solução deverá trabalhar com três diferentes tipos de movimento.

 

O primeiro (1.1.xx) deverá ser parametrizado para integração com o TOTVS Obras e Projetos e para utilizar Retenção. O segundo (1.2.yy) corresponderá ao faturamento do primeiro (1.1.xx) e deverá ser parametrizado para integração com o TOTVS Obras e Projetos, Usar Retenção, e ter **"Classificação de Vinculação = Retenção" e "Tipo de Vinculação = Vazio"** (**Etapa Vinculações do parametrizador**).

 

O terceiro será outro 1.2.zz, enviado pelo TOTVS Obras e Projetos e deverá estar parametrizado para integração com o TOTVS Obras e Projetos, Usar Retenção, e ter **"Classificação de Vinculação = Sem Classificação" e "Tipo de Vinculação = Controlar Retenção"**.

 

 

  **Informações Adicionais**

O movimento 1.X.zz (Retenção a pagar) e 2.X.zz(Retenção a receber), não necessariamente precisa ser de Nota Fiscal, os mesmo podem ser de outro tipo, como Ordem de compra/Ordem de venda.
