---
content_hash: 61ed02706365c6c6cfce80d8f5fa718b2f09f82468edfbd15778c5828c1c335a
fetched_at: '2026-06-29T00:10:26.949636+00:00'
page_id: '515688642'
product: rm
source: tdn-rm
title: Validações na Integração Folha de Pagamento com Automação de Ponto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=515688642
version: 44
---

## Consistência de Lançamento da Integração - Folha de Pagamento x Automação de Ponto

O Objetivo da consistência do Lançamento de Eventos de Integração é controlar o bloqueio de processos entre os produtos do RH buscando dar maior segurança na Folha de Pagamento, liberando os lançamentos via grupo de eventos somente após ter recebido os eventos (verbas) calculadas pelo Automação de Ponto.

Para prover mais segurança com relação aos eventos Lançados na Folha de Pagamento provenientes do Movimento calculado no modulo Automação de Ponto, o RM está disponibilizando a implementação as validações que serão contempladas através dos parâmetros abaixo:

* **Consiste Verbas Selecionadas x Calculadas**

Com este parâmetro marcado, o processo 'Lançar para Folha de Pagamento', no Modulo Automação de Ponto, irá retornar um log, com os eventos que não foram selecionados, mas foram calculados no movimento do ponto do funcionário. Este log irá descriminar por funcionário os eventos calculados no ponto e que não foram enviados para a 'Consulta Movimento da Integração' do Modulo Folha de Pagamento.

Este parâmetro está disponibilizado em Automação de Ponto | Configurações | Parametrizador | 08.01 - Iniciais | Lançamento Folha de Pagamento:

*Exemplo:*

Movimento calculado para o funcionário:

Selecionado somente o evento de Código 0001:

Quando existir os eventos calculados, mas os mesmos não foram selecionados para serem lançados, irá retornar conforme o log abaixo, detalhando os eventos por chapa:

Observação

Se já existir o evento na Consulta Movimento de integração e o mesmo não for selecionado no processo de Lançamento de eventos para o RM Labore, o sistema irá retornar a mensagem, não fazendo a consistência se o mesmo existe na tabela PFMOVTEMP.

* **Consiste Funcionários Elegíveis para o Lançamento para Folha de Pagamento**

Com este parâmetro marcado, o processo 'Lançar para Folha de Pagamento', no Modulo Automação de Ponto, irá retornar um log, com os funcionários que foram selecionados e são elegíveis para bater o ponto e que não tem as verbas calculadas no Movimento de Ponto.

Funcionário Elegíveis Para o Registrar Ponto

São considerado como funcionário elegíveis para registrar ponto aqueles que tem o campo Tipo de Regime de Jornada no cadastro de Funcionários | Salário/Jornada com a informação "Submetido a Horário de Trabalho (Cap. II da CLT)".

Este parâmetro está disponibilizado em Automação de Ponto | Configurações | Parametrizador | 08.01 - Iniciais | Lançamento Folha de Pagamento:

*Exemplo:*

Funcionário submetido ao horário de trabalho.

O mesmo não possui movimento para ser lançado para ser lançado no ponto:

Selecionando os eventos para serem lançados:

Ao executar o processo de Lançamento de Eventos para o RM Labore, retorna o Log abaixo detalhando por chapa:

Observação

1. Caso o Funcionário não esteja cadastrado no Módulo Automação de Ponto o processo de Lançar Eventos para o RM Labore não retorna o mesmo. Desta forma não é possível fazer a consistência da Elegibilidade.
2. Ainda continua sendo necessário executar o processo 'Utilizar o Cartão de Ponto' para o funcionário ser cadastrado no Automação de Ponto.
3. Mesmo se o usuário deixar de Utilizar o Cartão de ponto, o funcionário continua cadastrado no Modulo Automação de Ponto, sendo possível selecionar o mesmo no processo de Lançar Eventos para o RM Labore e o RM faz a consistência da Elegibilidade do funcionário.
4. Caso algum funcionário tenha o campo Tipo de Regime de Jornada diferente de "Submetido a Horário de Trabalho (Cap. II da CLT)" ou não preenchido, e, o mesmo possui movimento no espelho de Ponto, o sistema não está fazer a consistência da não elegibilidade, Lançando os eventos para a tabela PFMOVTEMP.
Atenção

Todos o processos do Modulo Automação de Ponto (cadastro, cálculo, etc) não são bloqueados e caso o funcionário não seja elegível a fazer o registro do ponto. Também não é verificado tal condição, ficando apenas a verificação no processo de Lançamento de Eventos para a PFMOVTEMP

* **Bloqueia Lançamento de Grupo de Eventos para Funcionário com recálculo desbloqueado no Automação de Ponto**

Com este parâmetro marcado, no processo de Lançamento de Grupo de Eventos, será validado se o Recálculo do Ponto do Funcionário está bloqueado no Modulo Automação de Ponto. Esta verificação é feita quando o funcionário tem eventos na movimentação temporária e é marcado a opção 'Lançar eventos da Integração com outros aplicativos' no Grupo de eventos.

Este parâmetro está disponibilizado em Folha de Pagamento | Configurações | Parametrizador | 06.02 - Integrações | 06.02.08 - Automação de Ponto:

*Exemplo:*

Funcionário com movimento de integração:

Funcionário com o recalculo do espelho do ponto desbloqueado:

Fazendo o lançamento através do Grupo de Eventos, selecionando para lançar os eventos de integração:

Retornou o log, informando que o Lançamento não será efetuado e o motivo, conforme abaixo:

No envelope não foi incluído nenhum evento:

Observações

1. Quando não está marcado para lançar eventos de Integração, mesmo com o recálculo do ponto desbloqueado, será lançado os eventos do grupo de eventos para o funcionários
2. Se o ponto estiver bloqueado e não for informado o tipo de lançamento de Integração com Outros Aplicativos referente ao Automação de Ponto, é feito o lançamento do grupo de eventos. A consistência só é feita considerando ponto desbloqueado.
3. Somente com este parâmetro marcado, caso o funcionário não seja elegível para bater ponto, porém o mesmo possui movimento de integração e o ponto está desbloqueado, o sistema irá fazer o lançamento de todo o movimento.

* **Bloqueia Lançamento de Grupo de Eventos para funcionários submetido a horário de trabalho mas não possui movimentação temporária**

Com este parâmetro marcado, no processo de Lançamento de Grupo de Eventos, será validado se o funcionário é submetido ao horário de trabalho e não possuiu movimentação temporária lançada na PFMOVTEMP. Esta verificação é feita quando o funcionário tem eventos na movimentação temporária e é marcado a opção 'Lançar eventos da Integração com outros aplicativos' no Grupo de eventos.

Este parâmetro está disponibilizado em Folha de Pagamento | Configurações | Parametrizador | 06.02 - Integrações | 06.02.08 - Automação de Ponto:

Exemplo:

Funcionário submetido ao horário de trabalho:

Fazendo o lançamento de Grupo de Eventos, informando para lançar eventos de Integração com outros aplicativos:

Retornou a mensagem abaixo, não lançando nenhum evento para o funcionário:

Observações

1. Quando não está marcado para lançar eventos de Integração com outros aplicativo no processo de Grupo de Eventos, mesmo o funcionário sendo submetido ao horário de trabalho, será lançado os eventos do grupo de eventos para o funcionários.
2. Caso um funcionário não seja submetido ao horário de trabalho e não possuí movimentação temporária, com opção 'Lançar eventos de integração com outros aplicativos' marcada, irá lançar normalmente os eventos do grupo de eventos.
Funcionários não Submetidos ao Horário de Trabalho

Quando o funcionário possuí movimentação temporária e no cadastro de funcionário o mesmo não está com o campo Tipo de Regime de Jornada com a informação "Submetido a Horário de Trabalho (Cap. II da CLT)", o processo retornar a mensagem abaixo:

"**O funcionário xxxx tem movimentação temporária para o mês, porém não é submetido a horário de trabalho. Verifique o cadastro. Seu lançamento não será efetuado.**"
