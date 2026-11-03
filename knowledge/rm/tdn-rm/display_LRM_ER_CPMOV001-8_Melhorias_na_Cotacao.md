---
content_hash: 67cffb7815690b69cbcf156440012a749e260f8dc782d0731e28e0eae5b45b2b
fetched_at: '2026-06-29T00:08:09.295592+00:00'
page_id: '239032713'
product: rm
source: tdn-rm
title: ER_CPMOV001-8_Melhorias_na_Cotacao
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_CPMOV001-8_Melhorias_na_Cotacao
version: 138
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Segmento Executor** |  | | |
| **Projeto1** | R\_CP\_MOV 2016/2017 | **IRM1** | CPMOV001-4 |
| **Requisito1** | CPMOV001-8 | **Subtarefa1** | Não se aplica |
| **Chamado2** | Não se aplica | | |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | Não se aplica | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). ,

## Objetivo

Revitalização do módulo de compras baseado nos levantamentos feitos através do projeto de UX, visando melhorar a usabilidade e experiência do usuário. 

## Definição da Regra de Negócio

Neste release, elencamos os seguintes itens para a segunda fase do processo de revitalização do módulo de compras.

# Criar um Status de produto indisponível para que o fornecedor sinalize que não tem determinado produto para fornecimento

A informação dos produtos indisponíveis para orçamento deve ser registrado no item para que os produtos ainda não cotados sejam confundidos com os produtos indisponíveis pelo fornecedor da cotação. Para isso serão necessários as seguintes alterações na cotação.

* + ## Criar o o status 'Indisponível' no Item de Orçamento

Será criado o novo status **'Indisponível'** na tela de edição de Itens de Orçamento que terá o mesmo que comportamento que o de **Produto Não Fornecido**, Não sendo considerado no calculo do quadro comparativo, e sendo apresentado apenas como **Indisponível.**

 - Quando o produto tiver seu status alterado para **Indisponível**o valor cotado será zerado assim como  é feito para com o status **Não Cotado**. 

 - O campo status só pode ser alterado durante a edição de um orçamento. Durante a negociação, este não poderá editado, e caso tenha a necessidade de alterar o status para **Indisponível** deverá editar o mesmo como **Orçamento** ao invés de **Negociação**

* + ## Incluir o Campo na Grid\Tela de Item de Orçamento Web.

Será criado um campo do tipo checkbox para marcar o produto **Indisponível** durante a inclusão de Orçamento via Web.

 - Durante a importação dos orçamentos para o sistema o campo será verificado para ser importado e caso o fornecedor tenha marcado o produto como **Indisponível**, este será importado com status **Indisponível**.

* + ## Incluir o Campo na planilha de Orçamento Excel.

Na exportação da planilha de Orçamento para Excel será criado o campo '**Indisponível**' do tipo lista suspensa com as opções SIM / NÃO para marcar o produto **Indisponível**durante o preenchimento da planilha de orçamento

 - Durante a importação dos orçamentos para o sistema, este campo será convertido para o status correspondente: Cotado (Indisponível = NÃO), Indisponível (Indisponível = SIM) ou não cotado quando o campo Indisponível = NÃO e o valor cotado não estiver preenchido.

* + ## Tratar o Campo no Quadro Comparativo.

Ao acessar **Gestão de Estoque, Compras e Faturamento | Compras | Cotação**, ao abrir uma cotação e **Calcular o quadro comparativo**, os itens que possuírem status do item igual a**Indisponível** no momento do registro de orçamento e/ou negociação, serão apresentados com a informação: **Indisponível**.

* + ## Tratar o Campo no Relatório de Quadro Comparativo Simples e Relatório de Quadro Comparativo Detalhado.

Os Produtos com **status Indisponível** serão apresentados nos relatórios de **Cotação Simples** e **Cotação Detalhada** da mesma forma que são apresentados os produtos **Não Cotados** por exemplo.

* + ## Tratar o Campo no Relatório de Quadro Comparativo em Excel.

Ao acessar **Gestão de Estoque, Compras e Faturamento | Compras | Cotação**, ao abrir uma cotação e **Calcular o quadro comparativo**, a opção **Gerar Dados do QCP para Planilha** ficará habilitada, nesta é necessário informar um arquivo com planilha modelo. O modelo padrão encontra-se em: ObjetosGerenciais\Planilha, sendo dois modelos disponíveis: Completo e Simplificado.

O modelo completo terá a informação do **Status do Item**, que ficará localizado a frente do **Status de Qualificação do Produto**, conforme imagem abaixo.

# Calcular Data de Entrega ao Informar Prazo de Entrega

* ## Prazo de Entrega no Orçamento da Cotação

Atualmente, no orçamento o usuário consegue informar a data de entrega, porém essa data não é gravada na tabela TCORCAMENTO, mas é feito o cálculo da diferença em dias entre a data cotação e a data de entrega informada e o resultado é gravado no campo TCORCAMENTO.VALPRAZOENTREGA.

Será criado um campo na na base de dados, para gravar a informação da data de entrega informada pelo usuário na tela. O campo Prazo de Entrega (dias) será adicionado a tela de Registro de Orçamento, para que o usuário possa escolher qual modelo trabalhar, data de entrega ou prazo de entrega em dias.

Caso o usuário opte por informar a data de entrega do orçamento em vez de o prazo de entrega, o sistema deverá manter o comportamento atual e o prazo de entrega do orçamento deverá exibir a informação "-1" no campo. Caso o usuário opte por informar o prazo de entrega em dias, o sistema fará um calculo da previsão da data que será entregue, mas será considerado o prazo informado.

O prazo de entrega sempre prevalece neste caso, sendo que se o mesmo estiver como valor -1, será considerado a data de entrega informada. Este comportamento já existe no itens de orçamento e foi replicado para o orçamento.

Além disso será criado um botão para que o prazo de entrega e data de entrega do orçamento possa ser replicado para os itens de orçamento.

* ## Geração da Ordem de Compras

Na geração da ordem de compra a partir da cotação, será realizado o tratamento para que, se o tipo de movimento estiver parametrizado para usar prazo de entrega o sistema calculará a data de entrega do movimento a partir da data que estiver informada no parâmetro **“Data Prazo de Entrega”** do tipo de movimento somada ao prazo de entrega do orçamento.

Ex.:

“Data Prazo de Entrega = Data Emissão”: 15/06/16

Prazo Entrega do Orçamento: 5 dias

Data de Entrega Calculada no Movimento: 20/06/16

Na geração da ordem de compra a partir da cotação, se o tipo de movimento está parametrizado para usar data de entrega, o sistema manterá o comportamento atual.

* ## Planilha de Importação e Exportação de Orçamento/Negociação

Esta implementação não afetará a importação de planilhas. Na planilha já existe o campo Prazo de Entrega do orçamento. Caso esse prazo seja alterado na planilha, ao importa-la o prazo informado na planilha é gravado no campo TCORCAMENTO.VALPRAZOENTREGA .

Dessa forma, basta que no campo prazo de entrega do Winforms seja exibido o prazo que está gravado no banco e a data de entrega seja calculada como já é feito hoje.

* ## Orçamento via WEB

Atualmente, no portal o usuário consegue informar a data de entrega do orçamento, porém na importação, essa data é gravada no campo TCORCAMENTO.DATENTREGA, que na tela Winforms corresponde ao campo “Data Recebimento”.

Este comportamento será alterado para que, ao importar os orçamentos da WEB o campo TCORCAMENTO.DATENTREGA será preenchido com a data de importação (data sistema).

Será criado um campo para exibir a data da cotação, que não poderá ser alterado, e um campo para o usuário informar o prazo de entrega do orçamento. Ao informá-lo, a data de entrega será calculada a partir da data da cotação. O prazo de entrega deverá ser gravado no campo TWCORCAMENTO.VALPRAZOENTREGA.

Ex.:

Data Cotação: 10/06/16

Prazo de Entrega do Orçamento no Portal: 5 dias

Data Entrega Calculada no Portal: 15/06/16

**Tabelas Utilizadas**

* TCITMORCAMENTO – Itens de Orçamento
* TWCITMORCAMENTO – Item de Orçamento WEB

## Protótipo de Tela

**Protótipo 01 - Tela de Orçamento / Negociação**

## Dicionário de Dados

**Código do Script:** /\*$Versao=NU.2016.06\_01\*/

 

|  |  |
| --- | --- |
| **Tabela** | TWCITMORCAMENTO |
| **Campo** | INDISPONIVEL |
| **Tipo** | DLOGICONULL |
| **Tamanho** | 2 |
| **Valor Default** | 0 |
| **Mandatório** | Sim (  ) Não (X) |
| **Descrição** | Produto Indisponível |
| **Help de Campo** | Informar se o fornecedor possui o produto para ser cotado. Esse campo poderá ser alterado durante o registro de Orçamento via Web. |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
