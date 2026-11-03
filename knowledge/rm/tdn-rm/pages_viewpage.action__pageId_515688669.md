---
content_hash: 933abdfa34020a1ed78aa035b6450553d60c341cded6bc8f8cc86507e491aee9
fetched_at: '2026-06-29T00:10:26.952314+00:00'
page_id: '515688669'
product: rm
source: tdn-rm
title: Parâmetros de Lançamento Folha de Pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=515688669
version: 8
---

**Consiste Verbas Selecionadas x Calculadas**

Com este parâmetro marcado, o processo 'Lançar para Folha de Pagamento', no Modulo Automação de Ponto, irá retornar um log, com os eventos que não foram selecionados, mas foram calculados no movimento do ponto do funcionário. Este log irá descriminar por funcionário os eventos calculados no ponto e que não foram enviados para a 'Consulta Movimento da Integração' do Modulo Folha de Pagamento.

**Consiste Funcionários Elegíveis para o Lançamento para Folha de Pagamento**

Com este parâmetro marcado, o processo 'Lançar para Folha de Pagamento', no Modulo Automação de Ponto, irá retornar um log, com os funcionários que foram selecionados e são elegíveis para bater o ponto e que não tem as verbas calculadas no Movimento de Ponto.

**Bloqueia recálculo após lançamento de eventos para a folha de pagamento**

Este parâmetro criado em 'Ambiente| Parâmetros| Automação de Ponto| Iniciais | Lançamento para Folha de Pagamento', tem como objetivo bloquear o recálculo do funcionário, após o processo de lançamento de eventos para a folha de pagamento for executado em Automação de Ponto Movimento| Calculo| Lançar para Folha de Pagamento.

*Exemplo:*

Com o parâmetro marcado:

Calculo realizado para o funcionário.

Lançamento para a Folha de Pagamento realizado.

Após realizar o recalculo para o funcionário é apresentada a mensagem de bloqueio.

**Obs:** O lançamento para Folha de Pagamento não será bloqueado, apenas o recálculo realizado em Movimento| Calculo| Calcular.

**Obs:** Os módulos devem estar na mesma competência.

**Consiste funcionários com os eventos lançados para o envelope de pagamento da folha no desbloqueio de recálculo**

Este parâmetro criado em 'Ambiente| Parâmetros| Automação de Ponto| Iniciais| Lançamento para Folha de Pagamento', tem como objetivo alertar o usuário ao tentar desbloquear o recálculo, indicando que o lançamento de eventos já foram lançados para o envelope do funcionário na Folha de Pagamento.

Mais informações Sobre os Parâmetros acima: [Segurança do Processo de Cálculo da Folha](https://tdn.totvs.com/pages/viewpage.action?pageId=515688642)
