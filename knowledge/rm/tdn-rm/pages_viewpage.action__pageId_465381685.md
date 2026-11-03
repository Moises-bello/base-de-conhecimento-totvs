---
content_hash: 680a2092d971eaeeffbc5c098f5e3a232f8fb3a3ccb6abdc649053ef7d8a20af
fetched_at: '2026-06-29T00:10:15.870887+00:00'
page_id: '465381685'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-2222 DT - Log detalhado de contabilização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=465381685
version: 31
---

Log com informações de contabilizações realizadas com sucesso ou erros.STATUS

## ****DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | *RM* |
| Segmento: | *TOTVS Gestão Educacional* |
| Módulo: | *TOTVS Educacional* |
| Função: | *Contabilização por competência* |
| Ticket: | *N/A* |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DEDUINTEGRACOES-2222](http://jiraproducao.totvs.com.br/browse/DEDUINTEGRACOES-2222 "Revitalização da Contabilização - Log do processo de contabilização - mais descritivo") |

## **SITUAÇÃO/REQUISITO**

Usuário não possuía uma maneira simples e usual de conferir as contabilizações / estornos feitas. Anteriormente, o usuário deveria conferir o resultado em um log textual de resultado do processamento.  
Ao fechar a tela do processo, caso quisesse verificar o resultado do processamento, o usuário teria que acessar o respectivo JOB via Gerenciador de Jobs e obter as informações de forma textual e não usual.

## **DESCRIÇÃO**

Com o objetivo de se ter um log com o resultado das contabilizações gravado no banco de dados e não somente textual, criamos o log de contabilizações para facilitar para o usuário a conferência das contabilizações por competência realizadas ou estornos não processados.  
O usuário terá de forma clara e objetiva informações como: Contrato contabilizado, Status da contabilização / estorno, Mensagem de erro / advertência, Usuário que processou, Data de processamento, etc...  
Essas informações serão gravadas no banco de dados e poderão ser filtradas conforme necessidade do usuário para fins de informações e/ ou conferência.

## **VISUALIZAÇÃO DO LOG**

Para que o log de contabilizações seja visualizado, o parâmetro de integração do educacional com a contabilidade deverá estar marcado.

O log de contabilizações poderá ser acesso de vários lugares distintos. Segue abaixo uma listagem dos locais pelos quais acessamos a tela de log:

1. **Menu (Log de contabilizações)**: Para acessar um log de contabilizações de mais de um contrato de acordo com o filtro desejado, podemos acessar o log a partir do menu Financeiro / Contábil → Geração → Contabilidade conforme abaixo:
2. **Anexo de contrato**: Para acessar o log de contabilizações de um contrato específico, o mesmo poderá ser acessado através do anexo de contrato.
3. **Log do processo**: Ao final do processamento da contabilização por competência, o log poderá ser acessado através do botão "Visualizar Log Detalhado"
4. **Tela de monitoramento de JOBS (Fracionamento)**: Ao acompanhar a execução de um JOB, o usuário poderá acessar a tela de log de contabilizações a partir do monitoramento da execução do processo.

## **PERMISSÃO NO PERFIL DE USUÁRIO**

A permissão de acesso ao log é a mesma permissão para geração de contabilização.

## **TELA**

Tela principal,Filtro de registros,Valores contabilizados, Visualização de valores contabilizadostelaprincipal,filtro,valorescontabilizados,contabilizacao

Tela principal de visualização do log de contabilizações / estornos com os registros processados com sucesso ou que deram erro ou advertência e os botões de filtro e valores de contabilizações totalizados.

Nessa tela será possível avaliar os contratos contabilizados com sucesso, as contabilizações da provisão e apropriações mensais, com valores de serviço, bolsa e desconto.  

yestelaprincipal

Na coluna memória de cálculo ao passar o mouse sobre a imagem são exibidas informações sobre as provisões de contrato, mostrando os valores do contrato na data em que foi gerada a contabilização.

Quando ocorre um cancelamento ou aumento são exibidos as informações da provisão de contrato de aumento ou cancelamento com o valor do serviço anterior e atual.

Também são exibidas informações sobre as a memória de cálculo da apropriação mensal, detalhando como é o calculo para chegar no valor da apropriação mensal.

Na apropriação de aumento e cancelamento a memória de calculo considera o valor da provisão, subtraindo apropriações de aumento ou cancelamento já realizadas e dividindo pelas competências restantes.

Com o botão direito do mouse, é possível copiar a memória de cálculo para a área de transferência.

Estorno

Contratos que foram estornados com sucesso terão seus Log's de contabilização e partidas contábeis excluídas, o processo de estorno só guardara Log para contratos estornados com advertência e erros.

nofiltro

Barra de ferramentas de filtro de registros

O usuário terá a opção de filtrar os registros de acordo com os cinco grupos abaixo:

* Operação   
  + : Considera ou desconsidera processos contabilizados
  + : Considera ou desconsidera processos estornados
* Status da contabilização / estorno
  + : Considera ou desconsidera contabilizações realizadas com sucesso (sem erros)
  + : Considera ou desconsidera contabilizações/estorno com erros.
  + : Considera ou desconsidera contabilizações/estorno com advertência. (Contabilizações com advertência são contabilizações de contrato serviço, aumento ou cancelamento que não resultaram em lançamentos contábeis. Ex.: Evento contábil configurado para buscar defaults contábeis cuja entidade parametrizada não possui defaults)
* Status do diagnostico
  + : Considera ou desconsidera contratos analisados com sucesso aptos a contabilização (sem erros)
  + : Considera ou desconsidera contratos analisados com advertência que não estão aptos a contabilização.
* Contabilização de contrato ou apropriação mensal
  + : Considera ou desconsidera contabilizações/estorno de contratos
  + : Considera ou desconsidera apropriações mensais
* Origem da contabilização: Considera ou desconsidera contabilizações com origem de serviço, aumento ou cancelamento
  + : Considera ou desconsidera contabilizações com origem serviço, isto é, contabilizações originais calculadas com bases nas parcelas do contrato sem alteração de valores.
  + : Considera ou desconsidera contabilizações com origem aumento, isto é, contabilizações de acréscimos efetuados após contabilização utilizando valores originais de contrato ou apropriação mensal. Ex.: aumento de mensalidade após alguma contabilização já ter sido feita.
  + : Considera ou desconsidera contabilizações com origem cancelamento, isto é, contabilizações de decréscimos efetuados após contabilização utilizando valores originais de contrato ou apropriação mensal. Ex.: redução de mensalidade após alguma contabilização já ter sido feita.
novalorescontabilizados

Valores totais contabilizados de serviços, bolsas e descontos

ATENÇÃO:

Nos valores contabilizados, somente serão considerados os valores de contabilizações realizadas com sucesso (status = Sucesso)

nocontabilizacao

Permite um acesso à contabilização realizada na operação de geração do respectivo registro de log

A edição de um log de sucesso, exibirá a tela de contabilizações do TOTVS Gestão Contábil contendo a contabilização realizada

ATENÇÃO:

Caso o usuário tente editar uma linha de log com status de erro ou advertência, será exibida uma tela informando o usuário de que a contabilização não poderá ser exibida:

## **TABELA NO BANCO DE DADOS**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Nome da coluna | Tipo | Comprimento | Aceita nulos | Descrição |
| CODCOLIGADA | DCODCOLIGADA | 2 | Não | Código da coligada |
| RA | varchar | 20 | Não | Registro Acadêmico |
| CODCONTRATO | varchar | 20 | Não | Código do Contrato |
| IDPERLET | int | 4 | Não | Identificador do Período Letivo |
| MESANO | datetime2 | 8 | Não | Competência contábil |
| TIPOCONTABILIZACAO | varchar | 1 | Não | Tipo de contabilização ('C' - Contrato / 'P' - Parcela) |
| ORIGEM | varchar | 1 | Não | Origem da contabilização ('S' - Serviço / 'A' - Aumento / 'C' - Cancelamento) |
| OPERACAO | varchar | 1 | Não | Operação contábil (C - Contabilização, E - Estorno) |
| DATACONTABIL | datetime2 | 8 | Sim | Data contábil  Para contabilizações de sucesso, será igual à data informada (caso tenha sido informada) ou será igual à data da competência.  Para contabilizações com erro, esse campo será nulo |
| STATUS | int | 4 | Não | Status da contabilização (1 = Sucesso, 2 = Erro, 3 = Advertência, 4 = Analisado com sucesso, 5 = Analisado com advertência) |
| MENSAGEM | MEMO | 16 | Sim | Mensagem após processamento Será nula, caso a contabilização tenha sido realizada com sucesso Caso a contabilização tenha tido erro, conterá a mensagem de erro. |
| IDJOB | int | 4 | Sim | Id. do Job |
| IDCONTRATOCONT | int | 4 | Sim | Identificador da contabilização de contrato |
| IDPARCELACONT | int | 4 | Sim | Identificador da parcela contábil |
| MEMORIADECALCULO | MEMO | 16 | Sim | Memória de cálculo |
| RECCREATEDBY | varchar | 50 | Sim | Usuário criador do registro |
| RECCREATEDON | datetime2 | 8 | Sim | Data de criação do registro |
| RECMODIFIEDBY | varchar | 50 | Sim | Autor da última modificação no registro |
| RECMODIFIEDON | datetime2 | 8 | Sim | Data da última modificação no registro |

## **ASSUNTOS RELACIONADOS**

* + Contabilização / Estorno por competência
  + Fracionamento de jobs (contabilização/estorno)

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
