---
content_hash: d88bb71dd1e5d15d401b66643c1232cf026e45d0a4487fd6933e6062838e0372
fetched_at: '2026-06-29T00:11:07.058169+00:00'
page_id: '638719251'
product: rm
source: tdn-rm
title: DT - Portal RM - Sugestão de Férias - Desconsiderar  dia compensado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=638719251
version: 18
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | Folha de Pagamento |
| Função: | Portal RM - Sugestão de Férias |
| País: | Brasil |
| Ticket: | [#11132523](https://totvssuporte.zendesk.com/agent/tickets/11132523 "View ticket on the Zendesk portal") |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHCALCRM-117](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-117) |

## **02. SITUAÇÃO/REQUISITO**

Ao realizar a marcação de férias para uma Quinta-Feira, utilizando um funcionário que possui o  Sábado compensado, o sistema está disparando a seguinte mensagem: 'Início de férias não pode ser programado para até dois dias antes de feriado ou descanso', impedindo a marcação a mesma através do portal RM. Na MDI a marcação de Férias não impedida, porém retorna a mensagem de forma incompleta.

## **03. SOLUÇÃO**

Para o Portal RM foi criado o parâmetro 'Desconsiderar dia compensado', que quando marcado, irá validar o tipo de Jornada cadastrada para o horário do funcionário e caso a mesma seja compensado, não irá impedir a marcação de férias até dois dias antes deste.

Para MDI foi ajustado a mensagem para 'Início de férias não pode ser programado para até dois duas antes de feriado, descanso ou dia compensado.'

Portal, MDI, Passo 03, Passo 04Portal,MDIyesPortal

No parametrizador, marcar para Ativar alterações da Reforma trabalhista:

No Grupo de Quiosque do portal marcar o Parâmetro destacado abaixo:

Funcionário com Jornada cadastrada onde o Sábado é compensado:

Ao cadastrar férias iniciando dia 09/09/2021 (Quinta-feira), não foi impedido:

noMDI

No parametrizador, marcar para Ativar alterações da Reforma trabalhista:

Funcionário com Jornada cadastrada onde o Sábado é compensado:

Ao marcar as férias dia 09/09/2021 (Quinta-Feira), retorna a mensagem abaixo, informando que as férias pode estar iniciando até 2 dias antes de dia compensado. Mas não impede a marcação de Férias:

## **04. DEMAIS INFORMAÇÕES**

* O Parâmetro 'Desconsiderar dia compensado' só ficará habilitado quando o parâmetro 'Impedir férias em feriados, dias de descanso ou até 2 dias antes destes' estiver marcado.
* Os parâmetros de quiosque do grupo do portal não fazem efeitos na MDI. Desta forma, a MDI só verifica o parâmetro Geral para ativar a reforma trabalhista para retornar a mensagem. Na MDI as férias nunca serão impedidas.
* É necessário que o parâmetro para ativar a reforma esteja marcado para que o portal verifique os parâmetros de Quiosque.

falseImportante

Solução disponível a partir dos patches:

* 12.1.29.306
* 12.1.31.228
* 12.1.32.164

## **05. ASSUNTOS RELACIONADOS**
