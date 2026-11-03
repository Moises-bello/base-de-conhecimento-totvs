---
content_hash: 315aa5741eb4508fa32c38e91aa916d17ae58577f959047bfacb8307474d9f98
fetched_at: '2026-06-29T00:08:40.670556+00:00'
page_id: '286490894'
product: rm
source: tdn-rm
title: Artigo 58-A paragrafo 5 Regime de Tempo Parcial - Acerto do banco de horas
type: documentation
url: https://tdn.totvs.com/display/LRM/Artigo+58-A+paragrafo+5+Regime+de+Tempo+Parcial+-+Acerto+do+banco+de+horas
version: 7
---

# Remuneração

|  |  |
| --- | --- |
| **Produto:** | RM Chronus |
| **Versões:** |  |
| **Ocorrência:** | **Artigo 58-Aº-A § 5º**  "Art. 58-A. § 5º As horas suplementares da jornada de trabalho normal poderão ser compensadas diretamente até a semana imediatamente posterior à da sua execução, devendo ser feita a sua quitação na folha de pagamento do mês subsequente, caso não sejam compensadas." |
| **Ambiente:** | Horas Extras |
| **Passo a passo:** | Para atender Artigo 58-Aº Paragrafo 5º será  necessário que o processo seja executado depois do fechamento do ponto do período, pois como será necessário efetuar a compensação duas vezes, o espelho fica bloqueado para alterações.  Segue passo a passo de como parametrizar o RM Chronus, referente compensação semanal.    1º ) Foi realizado a parametrização no sindicato na etapa Banco de horas como Diário, e informado as ocorrências configuradas para irem para o banco ( Compensar ), através  Configurações>Selecionar o funcionário>Processos>Parametrizar Sindicato> Etapa Banco de Horas:            2º ) Foi realizado a importação das batidas através do módulo>Entrada de Dados>Importar>para o funcionário de forma que ele teve as seguintes ocorrências em cada semana:  1º semana: 10 horas extras  2º semana: 03 horas de atraso  3º semana: 05 horas de atraso  4º semana: 07 horas extras    O período do ponto utilizado como exemplo é de 01/04/2017 a 30/04/2017.    \*\*\*\* Obs: Para que o sistema faça o que está descrito no Artigo 58-A $5 é necessário que o processo seja executado depois do fechamento do ponto do período, pois como será necessário efetuar a compensação duas vezes, o espelho fica bloqueado para alterações.    Foi executado o processo de compensação e lançamento do banco de horas do dia 01/04/2017 a 15/04/2017, através do menu>Banco de Horas>Compensação e/ou Lançamento do Banco de Horas.    Segue exemplo da configuração:  1ª tela:  Período compreendendo as duas primeiras semanas ( no exemplo citado: 01/04/2017 a 15/04/2017 ).  Banco de horas diário  Tipo de compensação: Compensação e lançamento do banco de horas      2ª tela:  Parametrização padrão ( caso necessário, aplicar alterações específicas).      3ª tela:  Parametrização padrão ( caso necessário, aplicar alterações específicas).      4ª tela:  Tipo de lançamento: Período  Forma de lançamento: Somente acima do número de horas  Opções para lançamento: Número de horas  Início do lançamento: Início da faixa  Considera total de horas: Marcar somente a opção Extras e número de horas igual a 000:00      3º ) Após conclusão do processo, serão lançadas as horas extras excedentes à compensação das duas semanas iniciais para o movimento.      4º ) Para realizar a segunda semana,  basta seguir os mesmos passos, realizado na primeira semana. Período a apurar 16/04/2017 a 30/04/2017, onde serão somados os valores ao evento de extra no movimento anterior.      5º ) Após toda a parametrização e compensação das horas,  foi feito o lançamento dessas horas para a folha de pagamento, pelo menu Movimento > Lançar para Folha de Pagamento.          6º ) Após todo o processo os eventos são lançados para o módulo da Folha de pagamento > Folha Mensal > Consulta movimentação da integração      7º ) Ao lançar a folha de pagamento pelo menu Folha mensal > Lançamentos > Grupos de eventos, o evento é incluído no envelope de pagamento do funcionário. |
| **Observações:** |  |
