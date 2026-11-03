---
content_hash: 2d1dc1d59e12760a57b882864681197e853e4a221bdd018a19bd849d0da577fe
fetched_at: '2026-06-29T00:11:18.218587+00:00'
page_id: '684025471'
product: rm
source: tdn-rm
title: Gerenciador de Movimento - Cancelamento
type: documentation
url: https://tdn.totvs.com/display/LRM/Gerenciador+de+Movimento+-+Cancelamento
version: 5
---

Este módulo permite cancelar eventos gravados na Movimentação de Eventos dos Funcionários, onde é selecionado um ou mais processos. Quando é utilizado algum filtro de seleção de funcionários (Chapa, seção, situação, origem evento, etc), é cancelado somente para esse grupo informado na seleção, permancendo os demais registros que não fazem parte deste agrupador mas que fazem parte do processo.

*Exemplo*

Temos o processo ID = 36 com lançamentos para as chapas 00003 e 00009:

Fazendo o Cancelamento e selecionando o processo de ID = 36 e na seleção de Funcionários foi innformado somente a chapa 00003:

Após executar o processo, os eventos da Chapa 00003 não está mais na consulta da Movimentação, porém a chapa 00009 continua com os registros cadastrados, sem nenhuma alteração:

Os eventos são inseridos no Histórico de Alterações:

false

O Campo Mootivo do Cancelamento não é de preenchimento obrigatório.

Para processar o cancelamento é obrigatório selecionar pelo menos um ID Processo.

É possível fazer o cancelamento de movimento do próximo mês.

false

Mesmo que já tenha sido executado o Laçamento dos Eventos da Movimentação de Eventos dos Funcionários para o Envelope de Pagamento, ao executar esse processo, os registros serão excluídos da Movimentação (PFENTMOV) sem fazer nenhuma bloqueio. Os eventos permanerão no Envelope de Pagamento e neste caso, será necessário executar o processo de cancelamento de movimento, marcando a opção 'Cancela evento de origem do Gerenciador de movimentos'.
