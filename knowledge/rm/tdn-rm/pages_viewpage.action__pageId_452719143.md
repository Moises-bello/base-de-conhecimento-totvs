---
content_hash: 41dbc135e5cacce85a237af77dffed2269c52bd3eff15649d5c626ad5f720720
fetched_at: '2026-06-29T00:10:03.718640+00:00'
page_id: '452719143'
product: rm
source: tdn-rm
title: Liberar Período
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719143
version: 6
---

A liberação mensal é feita após o processamento do mês. É sugerido que seja feito backup do banco de dados antes de liberar o mês.

Após a confirmação do processo, o Sistema irá atualizar informações dos funcionários que serão utilizadas no próximo período a ser considerado pelo Sistema, inclusive o histórico do saldo do banco de horas.

Após a liberação, o Sistema irá requisitar as informações referentes ao período de processamento.

Ao executar a liberação mensal, o sistema pode efetuar a transferência dos dados mais antigos para tabelas de arquivo morto.

O objetivo desta transferência é a diminuição da quantidade de registros de tabelas com consequente ganho de performance.

Para realizar a transferência para o arquivo morto, é necessário selecionar o parâmetro na tela de liberação de período. Com o parâmetro marcado, o sistema irá considerar o valor que está preenchido no parametrizador e irá manter a quantidade de meses informada. Ao final desse documento, se encontra a documentação relacionada aos parâmetros mencionados.

É importante ressaltar que o processo considera tanto períodos em produção, quanto períodos parcialmente transferidos ao ser executado com a flag selecionada. Em casos que existem muitos períodos a serem transferidos, podem ocorrer impactos na performance do processo.

**Observação**

Sistema já trás as informações preenchidas. Estas poderão ser alteradas ou não pelo usuário.

**Atenção**

Recomendamos efetuar a compensação do banco de horas por período após fechar o ponto do funcionário e antes da liberação mensal mesmo para os funcionários que não iremos lançar eventos de extras, atrasos ou faltas para o movimento.

A compensação deve ser feita para que seja efetuada a atualização do saldo do banco de horas por período.

Utilizando a compensação podemos observar que em períodos anteriores ao atual não podemos ter armazenado no banco de horas eventos de horas extras junto com eventos de faltas ou atrasos.

Períodos  
HelpWiki - RH - Automação de Ponto

[DT\_Transferência de Período com mais de 6 meses](https://tdn.totvs.com/pages/viewpage.action?pageId=372548518)

[Definir Período Ativo](https://tdn.totvs.com/pages/viewpage.action?pageId=452719112)
