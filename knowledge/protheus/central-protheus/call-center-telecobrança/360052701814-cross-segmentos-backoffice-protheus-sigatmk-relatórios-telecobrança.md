---
article_id: 360052701814
category: Call Center - Telecobrança
content_hash: dcc181be5a2b7d556397cad7f1d634d96beb4f79825553a2f7f4fadcb4e9877d
fetched_at: '2026-06-28T22:41:28.557616+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGATMK -  Relatórios Telecobrança
type: support-article
updated_at: '2024-04-25T12:54:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052701814-Cross-Segmentos-Backoffice-Protheus-SIGATMK-Relat%C3%B3rios-Telecobran%C3%A7a
---

**Dúvida**

Quais filtros e informações são impressas nos relatórios do **telecobrança** no módulo Call Center?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGATMK - A partir da release 12

**Solução**

Filtros e informações que são impressa relatórios do telecobrança:

**TMKR037 - Situação de Clientes**

Este relatório relaciona os títulos em cobrança, apresentado informações tais como: código/razão social do cliente, contato, número do atendimento, data do atendimento, data/hora de retorno do atendimento e dados dos títulos (prefixo, número, parcela, tipo, natureza, vencimento, valor, acréscimo, decréscimo, número do banco, valor/percentual dos juros e etc). Nos parâmetros é possível filtrar cliente, loja, status do título (pago, negociado, cartório ou todos, tipo ligação(ativo, receptivo ou ambos) e ocorrência.

**TMKR038 - Atendimentos Telecobrança**

Este relatório relaciona os atendimentos com títulos em cobrança, apresentado informações tais como: data, número atendimento, tipo ligação(receptivo ou ativo), código/razão social do cliente, operador, ocorrência e dados dos títulos (prefixo, número, parcela, tipo, natureza, vencimento, valor, acréscimo, decréscimo, número do banco, valor/percentual dos juros e etc). Nos parâmetros é possível filtrar número do atendimento, cliente, loja, operador, data, tipo da ligação(receptivo, ativo e ambos) e ocorrência.

**TMKR040 - Cobrança por Grupo**

Este relatório apresenta apuração das cobranças realizada por grupo de operadores, gerando informações tais como: saldo inicial (total dos títulos vencidos a serem cobrados), enviado (somatório dos títulos de todos os clientes que pertencem a carteira de cobrança do operador), recuperado (valor recebido das cobranças efetuadas), não realizados (atendimentos de telecobrança que não foram realizados, quando o operador não conseguiu efetuar o contato com o cliente), cancelado (notas fiscais canceladas), saldo final ("saldo inicial" menos "enviado" mais "não realizado" igual saldo atual em aberto) e participação (percentual de participação do grupo em relação ao total da cobrança menos cobrado vezes recebido). Nos parâmetros é possível filtrar por data, grupo atendimento, filial, tipo grupo(interno ou externo). 

**TMKR041 - Pendências de Agenda**

Este relatório relaciona os atendimentos telecobranças pendentes que estão na carteira do operador, apresentado informações tais como: código e nome do operador, razão social do cliente, CPF/CNPJ do cliente, total da dívida, data de envio (data de cobrança), data/hora de retorno da ligação pendente, o nome completo do cliente, o número do atendimento, a data do atendimento, a operação (ativa ou receptiva), o total por filial, o total por operador, o total geral. Nos parâmetros é possível filtrar por filial, grupo de atendimento, operador e tipo de grupo(interno ou externo). 

**TMKR042 - Ocorrências**

Este relatório relaciona os atendimentos das telecobranças agrupados por ordem de ocorrências, apresentado informações tais como: operador, data/hora da ocorrência, CPF/CNPJ do cliente, telefone, razão social do cliente, valor da cobrança, total por operador, total por ocorrência e etc. Nos parâmetros é possível por operador, data, tipo (ativo, receptivo ou ambos) e ocorrência.

**TMKR043 - Cenários de Cobrança**

Este relatório demonstra a visão do cenário de cobrança de um cliente, onde relaciona o grupo de atendimento e as regras de cobranças, apresentado informações tais como: código/descrição do grupo de atendimento, regra de seleção, a regra de negociação, tipo de grupo de atendimento (interno ou externo), o prefixo/natureza/situação/portador dos títulos a serem cobrados, a permissão para alteração do crédito do cliente, prazo máximo para reagendar o atendimento de telecobrança, prazo máximo para prorrogação dos vencimentos dos títulos, percentual máximo de desconto nominal, percentual máximo de desconto no juros, percentual máximo de acréscimo, percentual máximo de decréscimo, os operadores do grupo de atendimento, tipo do operador (operador ou supervisor) e etc. Nos parâmetros é possível filtrar por grupo de atendimento.

**FINR750 - Eficiência de Cobrança**

Este relatório apresenta somatório dos títulos por dia, gerando informações tais como: valor dos títulos, valores recebidos sem atraso, valores sem atraso acréscimo, valores sem atraso total recebido, valores com atraso, valores com atraso acréscimo, valores recebidos com atraso total recebido e etc. Nos parâmetros é possível filtrar prefixo, natureza, seleciona tipo(opção para selecionar os tipo de títulos antes de gerar) e compõe saldo retroativo (sim ou não).

**TMKR045 -  Posição Geral**

Este relatório apresenta consulta geral das cobranças, gerando informações tais como: total de títulos por regra de seleção, total de clientes por regra de seleção, total de valores por regra de seleção. Não há parâmetros para realizar filtros, as informações são geradas com base dos atendimentos feito até o momento e data da ultima geração de seleção de títulos.

**Saiba mais: [relatórios no módulo Call Center](https://tdn.totvs.com/x/oQxWIQ)**
