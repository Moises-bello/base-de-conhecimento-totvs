---
content_hash: f57dc257e92ab3e77645dbd56d060a77447e72932aadce41ad5a4c4a62fc4a28
fetched_at: '2026-06-29T00:11:18.208365+00:00'
page_id: '684024014'
product: rm
source: tdn-rm
title: Gerenciador de Movimento - Manutenção
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=684024014
version: 34
---

Nesta visão será apresentada o cadastro da Movimentação de Eventos dos Funcionários. Os eventos processados pelo usuário serão armazendos na Tabela PFENTMOV antes de serem enviados para o evenlope quando a base estiver parametrizada para utilizar o Gerenciador de Movimento.

Através deste módulo será possível visualizar todos os lançamentos realizados através do Grupo de Eventos, Lançamento de Férias, Importação e Entrada de Dados, assim como será possível incluir, excluir e alterar qualquer evento.

O lançamento de 'Grupos de Eventos' ou qualquer outro lançamento (entrada de dados, importação de movimento, etc) não irá fazer cálculo dos eventos, ou seja, caso o evento lançado tenha fórmula, código de cálculo, etc., o evento será apresentado com valor zero. sendo que, ao processar o processo de Lançamento do Gerenciadro de Movimento o Cálculo será acionado para calcular o valor destes eventos, e caso exista o mesmo evento mais de uma vez, os valores serão somados e lançados para o envelope de pagamento.

false

Somente os eventos de Vale Transporte, Código de Cálculo 32 - 'Total entregue em vale Transporte' e 104 - 'Total calculado para compra de Vale Transporte' terão seus valores calculados no momento do lançamento do Grupo de Eventos.

Quando o período estiver bloqueado, o sistema não permitirar nenhuma alteração, inclusão ou exclusão neste Cadastro.

Os eventos digitados nos módulos abaixo serão gravados na Movimentação de Eventos dos Funcionários, no campo ORIGEMMOV (Origem do Movimento):

|  |  |
| --- | --- |
| **Módulo** | **Código da Origem do Movimento** |
| Entrada de Dados | 1 |
| Entrada de Dados por Centro de Custo | 2 |
| Importação do Movimento | 3 |
| Importação do Movimento por Centro de Custo | 4 |
| Lançamento Eventos Programados | 5 |
| Lançamento de Grupos de Eventos | 6 |
| Manutenção do Gerenciador de Movimento | 7 |
| RM Chronus | 8 |
| Lançamento de Férias | 9 |
| Entrada de Dados Por Tomador | 10 |
| Rescisão | 11 |
| Movimento de Ensino | 12 |
| Transferência | 13 |
| Finaliza Férias | 14 |

**Processo de lançamentos**

**Grupo de Eventos**

Sempre que o grupo de eventos for lançado, o sistema irá validar se o usuário está lançado o mesmo grupo de eventos. Para isto serão validados os campos: NROPERIODO, MESCOMP, ANOCOMP, ORIGEMMOV e CODGRPLANC.

Casos os campos acima sejam os mesmos, o sistema irá fazer a seguinte validação:

* se para aquela chapa já existir o evento que esta sendo lançado, o sistema irá substituir os campos VALOR/HORA/REF deste evento;
* se para aquela chapa ainda não existir o evento que esta sendo lançado, o sistema irá inserir o evento;
* se para aquela chapa existir um evento, e este evento não esta sendo lançado, o sistema irá excluir este evento e apresentar uma mensagem de aviso no log;
* se no grupo de eventos foi selecionada uma chapa que não esta no grupo já lançado, o sistema irá inserir a chapa;
* se no grupo de eventos não foi selecionada uma chapa que esta no grupo já lançado, o sistema não faz nada. Caso o usuário queira excluir esta chapa deverá excluí-la através do módulo ‘Cancelamento do Gerenciador de Movimento’

*Considerações*

Não exisitirar mais as ações: Adicionar, Ignorar, Rermover e Substituir. O campo fircará desabilitado no cadastro de eventos do Grupo de Eventos

Sempre que for o mesmo grupo de eventos, o sistema irá substituir, caso contrário, o sistema irá adicionar o registro na Manutenção de Eventos dos Funcionários, mesmo que o evento já exista para o funcionário

Para alertar o usuário que algum processo do grupo de eventos (Vale Transporte, Eventos Programados, Códigos Fixos, Salário Composto e Insuficiência de Saldo) está sendo lançado mais de uma vez para o funcionário, independente de ser o mesmo grupo ou não, no momento do lançamento do Grupo de Eventos será validado se o NROPERIODO, MESCOMP, ANOCOMP e ORIGEMGRP são os mesmos, caso seja, irá apresentar uma mensagem de aviso no log.

As integrações com outros aplicativos não ficará disponível quando utilizar Gerenciador de Movimento, isso porque os aplicativos enviarão diretamente para a tabela PFENTMOV invés de enviar para a tabela PFMOVTEMP.

false

* O Lançamento de Grupo de Eventos irá preencher a data de pagamento conforme configurado nos parâmetros Globais ou Locais.
* A insuficiência de saldo somente funcionará corretamente se no evento exisitir 'Evento de insuficiência de saldos' informado.

**Entrada de Dados / Entrada de Dados por Centro de Custo / Entrada de Dados Por Tomador**

Sempre que incluir eventos através destes módulos, o sistema irá adicionar um registro na Movimentação de Eventos dos Funcionários.

Caso o evento que está sendo lançado já existir na Movimentação,  o mesmo será inserido mais de uma vez. O sistema nunca irá substituí-lo.

**Importação de Movimento / Importação de Movimento por centro de Custo**

Sempre que um lote for importado o sistema irá adicionar os dados na Movimentação de Eventos dos Funcionários, independente se o lote já foi importado.

No arquivo de importação o campo ‘Dados alterados manualmente’ será ignorado. Independente se tiver ‘S’ ou ‘N’, o sistema irá enviar para o Gerenciador de Movimento, e no lançamento da Movimentação de Eventos para o envelope o valor será recalculado. Desta forma, quando o campo ‘Dados alterados manualmente’ estiver ‘S’ não irá preencher o campo PFFINANC.ALTERADOMANUAL ou o campo PFMOVCC.EDITADO com 1(um).

O campo data de pagamento da movimentação de eventos será preenchida com a data informada no arquivo ou com a data informada na tela da importação.

**Férias**

O cálculo das férias continua sendo gravado no recibo de férias, a única alteração é no lançamento das férias, os eventos são lançadas para á Movimentação de eventos dos Funcionários com o campo origem do Movimento 'Lançamento de Férias'

**Rescisão individual e Rescisão Coletiva**

Ao calcular a rescisão, o sistema enviará os eventos da Manutenção de Eventos do Funcionário que não foram lançados no período da rescisão direto para o Envelope de Pagamento (PFFINANC ou PFMOVCC), sem precisar executar o processo 'Lançamento' do Modulo Gerenciador de Movimento. Para isto, o parâmetro 'Lançar a movimentação do Gerenciador de Movimento' sempre retornarar marcado:

false

Os eventos calculados e lançados na rescisão, seja os automaticos ou os selecionados pelo usuário (Código Fixos, Eventos Programados, Vale Transporte, Salário Composto, Emprestimo) estarão apenas no Envelope de Pagamento (PFFINANC) com o campo Origem do Movimento (ORIGEMMOV) = 0. Os eventos existentes na Manutenção de Eventos do Funcionário que não são de rescisão, exemplo, um evento que a origem =1 - Entrada de Dados, o mesmo será lançado no Envelope de pagamento com o ID da origem = 11 (Entrada de Dados Pela Rescisão)

*Considerações*

O envelope de pagamento para demitido terá o mesmo comportamento para o não demitido, ou seja, não poderá incluir, alterar ou excluir evento.

Não será permitido incluir, excluir ou alterar eventos no cadastro de Manutenção de Eventos do Funcionário. Quando for necessário incluir eventos sem cancelar a rescisão, o mesmo deverá ser feito através do grupo de eventos, selecionando a opção 'Lançar eventos para Funcionários demitidos no mês' e na selação de funcionário, a situação D:

O eventos do Grupo de eventos serão enviados diretamente para a Manutenção de Eventos do Funcionário e não será incluído no envelope automaticamente, sendo necessário executar o processo de Lançamento do Gerenciador, marcando a opção 'Lança Movimento Demitido mês'.

Quando executar o processo de Lançamento de Grupo de Eventos no cenário acima (após a rescisão), os eventos de Rescisão serão incluídos na Manutenção de Eventos do Funcionário com a origem do Movimento = 11 (Entrada de Dados Pela Rescisão), independente se a rescisão já foi calculada ou não.

Quando a rescisão for cancelada, o sistema excluirar os eventos de Origem de Movimento = 11 (Entrada de Dados Pela Rescisão) da Movimentação de Eventos do Funcionário e todos os eventos do Envelope de Pagamento independente da Origem do Movimento.

Quando existir férias pendentes de Lançamento/Finalização e ao acessar o cadastro de rescisão o usuário optar por calcular/Lançar/Finalizar as férias pendentes, os eventos de férias irão para a Movimentação de Eventos do Funcionário com a origem do Movimento = 9 (Lançamento de Férias). Quando as férias forem lançadas junto com a rescisão (mesmo período), os eventos de Férias irão para o Envelope de Pagamento (PFFINANC) com o campo Origem do Movimento = 11 (Entrada de Dados Pela Rescisão)

**Transferência**

Quando houver transferência para mesma coligada ou para uma coligada que esteja configurada para utilizar o Gerenciador de Movimento, o sistema irá Lançar os eventos para o Envelope de Pagamento da chapa atual com o codigo de origem do movimento = 11 e, caso o usuário maque o parâmetro 'Transfere movimentação do mês atual', irá transferir a ficha financeira para chapa ativa.

Quando na coligada de origem estiver configurada para utilizar o Gerenciador de Movimento e na Coligada de destino **não** estiver configurada para utilizar o Gerenciador de Movimento e, existir movimento no mês da Transferência na Movimentação de Eventos do Funcionário, o sistema irá emitir a mensagem de erro abaixo e a transferência não será concluída.

**13º Salário e Diferenças (Férias, Salário, 13º Salário e Rescisão Complementar**

Estes processos não irão enviar os eventos para a Movimentação de Eventos do Funcionário. Os eventos serão enviados diretamente para o envelope de pagamento com o ID da Origem do Movimento = 0.

Qualquer inclusão de evento para este processo deverá ser feito através da Movimentação de Eventos do Funcionário.

Qualquer alteração no valor do evento deverá ser realizada através do Envelope de Pagamento, através a opção 'Forçar Valor'.

Qualquer exclusão será através do cancelamento de movimento.

**Lançamento do Movimento de Ensino (Utilizando a Importação e RM Classis)**

Este processo irá enviar os eventos para a Movimentação de Eventos do Funcionário com o ID da origem do Evento = 12 (Movimento de Ensino).
