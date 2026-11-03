---
content_hash: 5ef9744dfd15f6ea34d78c684bc63f15b213c570bee365a56aefd49ab2ecfa98
fetched_at: '2026-06-29T00:10:26.218005+00:00'
page_id: '513433869'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-5719 DT Agrupamento de lançamento de outras filiais no mesmo
  boleto e Agrupamento automático de lançamento ao gerar parcelas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=513433869
version: 25
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | TOTVS Gestão Educacional |
| Função: | Geração de lançamento |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : |  |

## **02. SITUAÇÃO/REQUISITO**

O TOTVS Gestão Educacional não permite que lançamentos de Filiais diferentes seja agrupado no mesmo boleto.

## **03. SOLUÇÃO**

Realizamos uma melhoria no módulo TOTVS Gestão Educacional para que seja possível realizar o agrupamento de lançamentos de Filiais distintas no mesmo boleto considerando algumas regras que iremos detalhar.

**Parametrização**

Disponibilizamos o parâmetro “Agrupar no mesmo boleto lançamentos de outras Filiais”.

Ao marcar o parâmetro será informado que o comportamento será igual para todas as Filiais da coligada do contexto

Este parâmetro possui dois direcionamentos:

**1º** Se a geração de lançamento estiver sendo executada pela visão de parcela será respeitada a opção definida no parâmetro citado acima.

**2º** Se a geração de lançamento estiver sendo executada pelo processo em lote será considerada a opção “Agrupar no mesmo boleto lançamentos de outras Filiais”.

* É importante destacar que ao acessar essa tela o sistema irá definir a opção **“Agrupar no mesmo boleto lançamentos de outras Filiais”** conforme o que foi definido nos parâmetros de sistema, porém no processo o usuário tem o poder de decisão sobre o comportamento do parâmetro.
* O agrupamento de lançamento de outras filiais será aplicado somente para a forma de agrupamento por “**Aluno**” ou “**Responsável financeiro**”

**Regras**

Durante a execução da geração de lançamento o TOTVS Educacional realizará uma análise nos lançamentos de **todas as outras Filiais da coligada do contexto**, identificando se existem parcelas que poderão ter os lançamentos agrupados ao mesmo boleto do lançamento correspondente ao contexto corrente de processamento.

Por exemplo:

- Temos cadastrado para a coligada 1 a Filial 1, 2, 3 e 4 para o nível de ensino básico.

- Vamos gerar os lançamentos da coligada 1 e Filial 3,

Durante o processamento o sistema irá analisar nas parcelas da Filial 1, 2 e 4 se existem parcelas que podem ser agrupadas ao boleto da Filial 3 (que está sendo processada), se sim, estes lançamentos também serão gerados e agrupado ao boleto.

Características para um lançamento ser agrupado:

* As parcelas devem ter o mesmo responsável financeiro
* As parcelas devem ter a mesma data de vencimento
* As parcelas não podem ser do tipo extra
* No cadastro da conta caixa a filial não pode ser informada
* As parcelas precisam ter o mesmo convênio
* No Educacional para todas as filiais que deseja agrupar os parâmetros de regra de geração de vencimento devem ser iguais. Ex: Regra de data de vencimento, baixa automática, agrupamento
* Se o lançamento já estiver gerado, o status tem que ser igual a “Aberto”, e o boleto não pode esta remetido ao banco.
* Se o lançamento já estiver gerado, não será permitido realizar o agrupamento quando pelo menos um deles estiver em processo de cobrança terceirizada nas **versões 12.1.2302 e superiores**

Estas são regras do Educacional, porém ainda serão consideradas também as regras do TOTVS Gestão Financeira que podem ser consultadas em [FIN - Boleto](https://tdn.totvs.com/display/LRM/FIN+-+Boleto).

Para que seja realizado agrupamento em lançamentos já gerado é necessário que o parâmetro em destaque esteja marcado.

* Parcelas que possuem lançamentos de bolsa de crédito não serão regeradas, neste caso é necessário que o usuário cancele os lançamentos.
* Ao processar a regeração de lançamentos de parcelas de outras filiais caso as parcelas seja aptas a serem agrupadas o parâmetro **Cancelar a remessa automaticamente ao regerar lançamento com status registrado ou remetido** não será aplicado, somente será aplicado a regeração nas parcelas do contexto corrente.   
  Para mais informações sobre a regra do parâmetro, [clique aqui.](http://tdn.totvs.com)

Por exemplo:

- Temos cadastrado para a Coligada 1 a Filial 1 e 2 para o nível de ensino básico.

- Na Filial 1, temos duas parcelas com lançamentos de status registrado e outra remetida

- Vamos gerar os lançamentos da coligada 1 e Filial 2

- Durante o processamento o sistema analisa as parcelas da Filial 1, mas não irá considerar as parcelas remetidas e registradas ao banco para agrupamento ao boleto.

Também foi criado o parâmetro “Identificação automática das parcelas que podem ser agrupadas no mesmo boleto independente do filtro selecionado no processo geração de lançamento”

Ao marcar esta opção, durante o processo de geração de lançamento o sistema irá verifica para cada parcela processada, se na mesma filial, existe outra parcela que pode ser agrupada levando em consideração as regras de agrupamento, tais como:

* Mesma filial (se a opção "Agrupar no mesmo boleto lançamentos de outras filiais" desmacado)
* As parcelas devem ter o mesmo responsável financeiro e RA (irá depender da opção de agrupamento escolhida)
* As parcelas devem ter a mesma data de vencimento
* As parcelas não podem ser do tipo extra
* Para os casos de regeração, o boleto tem que estar em aberto e não remetido ao banco

Ressaltamos que este comportamento em versões anteriores já é aplicado pelo processo de geração de lançamento, porem o agrupamento é aplicado somente entre as parcelas que estão sendo processadas, ou seja, as parcelas selecionadas conforme o filtro do processo.

Marcado este novo parâmetro o agrupamento vai ocorrer mesmo que a parcela não esteja carregada em função do filtro do processo.

div.theme-default .ia-splitter #main {
margin-left: 0px;
}
.ia-fixed-sidebar, .ia-splitter-left {
display: none;
}
#main {
padding-left: 10px;
padding-right: 10px;
overflow-x: hidden;
}
.aui-header-primary .aui-nav, .aui-page-panel {
margin-left: 0px !important;
}
.aui-header-primary .aui-nav {
margin-left: 0px !important;
}
]]>
