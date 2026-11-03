---
content_hash: 096267fecdb05042eddbd5deef8b814f1c8b5a2c5a196f8d0dbc7260aa2e303c
fetched_at: '2026-06-29T00:08:48.826088+00:00'
page_id: '327335110'
product: rm
source: tdn-rm
title: 1808923 MATFATCMPCRM01-2059 DT Envio/Consulta de evento GTV(Guia de Transporte
  de Valores)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=327335110
version: 10
---

## Envio de Evento GTV (Guia de Transporte de Valores)

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | **RM** |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **Totvs Gestão de Estoque, Compras*.e Faturamento* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *CT-e OS* | *ENVIO/CONSULTA DE EVENTO GTV(GUIA DE TRANSPORTE DE VALORES)* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **CT-e OS** | **CONHECIMENTO DE TRANSPORTE ELETRÔNICO - OUTROS SERVIÇOS** | |  |  | |
| **Cadastros Iniciais:** | *Cadastro das Guias de Transporte e suas Especies* |
| **Parâmetro(s):** | *Fis Conhecimento de Transporte - Tipo CT-e OS - Transporte de Valores* |
| **Ponto de Entrada:** | *-* |
| **Tickets relacionados** | *-* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | - |
| **País(es):** | **Brasil** |
| **Banco(s) de Dados:** | **SQL Server / Oracle** |
| **Tabelas Utilizadas:** | *TGTV e TGTVESPECIE* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Implementação do evento de Envio de GTV.  De acordo com o Manual de Orientações ao Contribuinte Versão 3.00 do Conhecimento de Transporte Eletrônico, após o envio do CT-e OS de Transporte de Valores, é necessário fazer o envio de pelo menos um evento de GTV (Guia de Transporte de Valores) referente ao CT-e OS enviado. 

## Documentação Adicional

Informações adicionais sobre o funcionamento do CT-e OS podem ser encontrados no Manual do CT-e que pode ser adquirido em <http://www.cte.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=bx74pJ8hXaM=>

Segurança

Para Incluir uma nova guia, Alterar, Excluir, Enviar Evento ou Consultar Evento, é necessário permitir acesso

 

## Definição da Regra de Negócio

Visão de Conhecimento de Transportes Eletrônicos - Outros Serviços

Observação: Necessário executar o script responsável por criar as tabelas TGTV e TGTVESPECIE

1. Anexo: Cadastro de GTV.

Implementado um novo anexo da visão de Conhecimento de Transportes Eletrônicos - Outros Serviços chamado "Cadastro de GTV". Antes de realizar o envio do evento é necessário realizar o cadastro da GTV bem como suas Espécies.

Nesse anexo o usuário fará o cadastro das GTVs associadas ao CT-e OS selecionado. O usuário deve ter a possibilidade de incluir, editar e excluir GTVs. Para cada GTV cadastrada deverá ser exibido um registro no anexo. Esse anexo deverá apresentar duas abas, sendo a primeira aba chamada "Identificação". A segunda aba, chamada "Espécies".

Tela de Cadastro de GTV:

Tela de Cadastro da Espécie:

2 - Processos: Envio e Consulta.

O Status inicial da GTV será sempre 'A Enviar', ou seja, após cadastro, o mesmo estará pronto para o envio.

Para realizar o envio, basta selecionar o GTV (pode-se selecionar mais de um GTV), acessar o menu de Processos e clicar em 'Enviar Evento GTV'.

Obs.: Esta consistência pode ser lançada durante o processo de envio, antes da comunicação com o TSS.

Feito isso, o GTV terá seu status alterado para 'Enviado'.

Podem ser cadastrados inúmeros GTVs mas, para realizar novos envios, todos os registros que possuam o status 'Enviado' devem ser consultados, para que seu status seja atualizado. Caso contrário, uma mensagem de consistência será exibida.

Então, a partir de um GTV que possua o status Enviado, basta selecioná-lo, acessar o menu de processos e clicar em Consultar Evento GTV.

Após a consulta, um dos possíveis status do GTV pode ser Autorizado, caso todas as informações estejam de acordo com a SEFAZ.

Caso contrário, o registro terá seu status alterado para Rejeitado, devendo ser feitas as possíveis correções e realizado o processo de envio novamente.

2.1 - Processos: Múltiplos GTVs

Quando são enviados mais de um GTV ao mesmo tempo, eles passam a ser considerados um lote, e no XML de envio são contempladas todas as suas informações, separadas em grupos. Segue exemplo:

Obs.: Alguns grupos do GTV destacado foram minimizados, para facilitar a visualização.

Ao executar o processo de consulta, será exibida uma mensagem notificando que todos os GTVs que se encontram com o status Enviado serão consultados, e como eles foram enviados em formato de lote, seu status final será correspondente ao status dos GTVs. Uma particularidade à ser observada é que, se um dos registros enviados for rejeitado por algum motivo, o status de todos será alterado para rejeitado, devendo ser ajustadas as possíveis pendências.

**Importante:** No retorno da SEFAZ é informado o motivo da rejeição, porém este motivo não é relacionado ao GTV em questão pois nesse tipo de envio a SEFAZ não consegue controlar individualmente os registros que foram enviados e/ou consultados.

3 - Histórico

O histórico dos processos executados com relação ao GTV são exibidos no anexo de histórico do próprio CT-e OS.

Ao editar o histórico, é exibido um campo confirmando o Tipo do Evento, bem como suas demais informações.
