---
content_hash: 66c229be4ee6d983227e578ac1dd7dbf8b4ce2b573d5b32c37e301c9bd6937b2
fetched_at: '2026-06-29T00:06:04.292595+00:00'
page_id: '200908314'
product: rm
source: tdn-rm
title: ER_codigo_automatico_para_composicoes
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_codigo_automatico_para_composicoes
version: 4
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Composição |
| **Segmento Executor** | Construção & Projetos | | |
| **Projeto1** | R\_C&P\_TOP007 | **IRM1** | PCREQ-2580 |
| **Requisito1** | PCREQ-5471 | **Subtarefa1** | PDR\_CP\_TOP007-1135 |
| **Chamado2** | Não se aplica. | | |
| **Release de Entrega Planejada** | 12.1.7 | **Réplica** | Não. |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *Composição - <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.Composicoes.aspx>*  *Máscara - <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.ExibicaoMascaras.aspx>*  *Insumos - <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.Insumos.aspx>* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 Essa nova funcionalidade incluirá ao TOP TOTVS Obras e Projetos a possibilidade de criar composições com Código Automático para as mesmas, sugerindo ao usuário prováveis códigos a medida que o mesmo digita o código.

## Definição da Regra de Negócio

As Composições são um conjunto de insumos e/ou composições auxiliares responsáveis para executar uma determinada tarefa ou serviço. Insumos são elementos básicos de um projeto (matérias-primas, bens intermediários, mão de obra, equipamentos, capital, verbas, entre outros que formarão composições que possuem preços).

O Cadastro de Composição é um dos fundamentais para o TOTVS Obras e Projetos, pois é a partir dessas informações que teremos condições de determinar os custos de um projeto, bem como seu preço de venda. Eles determinarão ainda o planejamento executivo e financeiro do projeto.

Atualmente as composições seguem o padrão da máscara pré-definida nos parâmetrs de projeto, porém, a inserção do código do mesmo seguindo o padrão desta máscara é manual, ou seja, o usuário deve observar o padrão da máscara e propor um novo código no momento da criação do mesmo ou quando um processo correlato que envolva a composição seja executado, lembrando que esse código deve ser único e não poderá existir outros iguais.

### Código automático

Essa funcionalidade poderá ser ativada ou desativada conforme necessidade dos usuários e varia de projeto a projeto. Para essa funcionalidade caso o parâmetro de projeto “Usar auto-incremento”, no mesmo local onde o usuário informa a mascara da composição, definirá se aquele projeto utilizará ou não os Códigos automáticos para Composições.

### Elaboração de um novo código

Para elaborar um novo código o sistema deverá sugerir ao usuário possíveis códigos que se encaixem com os caracteres que o mesmo está digitando, lembrando que, a máscara sempre deverá ser respeitada. Os códigos sugeridos sempre deverão ser auto-incrementados em uma unidade, para que o usuário não tenha problemas ao salvar esse novo código na base de composições.

O código da composição deverá ser sugerido ao usuário automaticamente sem a necessidade de qualquer interação adicional a não ser a digitação do código desejado, a medida que o usuário entra novos caracteres o próximo código de composição que conicida com aquele padrão deverá ser sugerido.

### Regras de Integridade

O Código automático de Composição só será aplicado se o usuário marcar a opção de “Usar auto-incremento” nos parâmetros de projeto. Ainda assim o sistema fará apenas uma sugestão de código, o usuário pode decidir usar ou não aquela sugestão.

Somente mascaras para composições com padrão de pre-fixação ou mascaras contendo somente números serão autoincrementadas, pois mascaras pós-fixadas e mascaras com números intercalados de letras fogem um padrão de autoincremento tradicional. Sendo assim o usuário deverá gerar esses códigos manualmente.

O autoincremente ocorrerá somente a parte numérica da mascara, caso exista pré-fixos com letras esse serão conservados e a parte numérica será incrementada.

 

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Parâmetros de Projeto | Alteração | Projeto -> Construção e Projetos -> Projetos ou a tecla de atalho F6 Exibição -> Máscaras -> Box Composição | - |
| Composições | Alteração | Orçamento -> Composições -> Cadastro ou a tecla de atalho F9 | - |

## Protótipo de Tela

### **Protótipo 01**

### Protótipo 02

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
