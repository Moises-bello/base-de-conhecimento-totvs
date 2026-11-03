---
content_hash: 10e9522a46878f290b3d5d498d7cb7476599682398bf5f93b17713b4a4bb01f7
fetched_at: '2026-06-29T00:11:45.124956+00:00'
page_id: '819496990'
product: rm
source: tdn-rm
title: Vencimento de Plano(s) de Manutenção
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=819496990
version: 8
---

O vencimento de Plano de Manutenção é gerado em Atividades/ Vencimento de Plano(s) de Manutenção.

Existem algumas formas de se calcular o vencimento de cada plano.

Para o cálculo é considerado o valor da frequência de uso do respectivo indicador no plano: Valor do Indicador no Plano - (Valor do lançamento corrente baseado na data atual - Valor do último lançamento para o Plano).

* Se o cálculo da frequência de uso do indicador do plano estiver com o valor maior que zero, a partir do cálculo da média diária de indicador é possível prever o vencimento
  + Considere um plano de manutenção do tipo cíclico 1000 para um Objeto de Manutenção com os seguintes indicadores de uso:
    - 30/12/2022 0 km Inicialização do plano com zero km
    - 25/02/2023 10000 km O plano venceu e a próxima execução será com 20000 km
    - 30/03/2023 15000 km O plano ainda não venceu e a próxima execução será com 20000 km
    - 30/04/2023 20000 km O plano venceu e próxima execução será com 30000 km
    - 30/05/2023 25000 km O plano ainda não venceu

Usando como exemplo o ultimo lançamento de 25000 km para demonstrar como é feito o cálculo do vencimento do plano.

1. O Cálculo da média dos indicadores de uso no período 30/12/2023 à 30/05/2023 que será igual a 165,56.

2. Para calcular a data de vencimento do plano faz-se o (Medidor Final) – (Medidor Inicial). No exemplo citado acima a ultima execução do plano foi dia 30/04/2023, então 20000 km será o medidor inicial e o medido final será 25000 km. (25000 – 20000) = 5000 km. Pega 5000 km e divide pela média de indicadores de uso (5000/165,56) = 30,20, isso significa que o vencimento será daqui a 30 dias. Considerando que a data atual do sistema seja 15/06/2023 o vencimento do plano será dia 16/07/2023.

* Se o cálculo da frequência de uso do indicador do plano estiver menor ou igual a zero o cálculo se dá da seguinte forma:
  + Considere um plano de manutenção do tipo cíclico 1000 para um Objeto de Manutenção com os seguintes indicadores de uso:
    - Lançamentos do indicador realizados para o plano de manutenção:
      * 30/12/2022 1000 km na inicialização do plano
      * 25/02/2023 3500 km do último lançamento do plano
    - Lançamentos do indicador realizados de forma geral:
      * 30/03/2023 5000 km
      * 29/04/2023 6500 km
      * 28/05/2023 7000 km
      * 30/06/2023 9500 km do lançamento corrente considerando a data atual

1. Sendo assim, considerando a data corrente de 30/07/2023, a frequência de uso no plano será 1000 - (9500- 3500) = **-5000**

2. O valor do vencimento do plano será o Valor do último lançamento para o Plano + Valor do Indicador do plano = 3500 + 1000 = 4500

3. A data vencimento será a Data da Coleta do primeiro lançamento geral, onde o valor é maior ou igual a 4500, isto é **30/03/2023** representado pelo valor 5000.

**Tabela de cores**

| Cores | Descrição |
| --- | --- |
| Vermelho | O 1**°**identificador ficará com o fundo em vermelho quando o plano de manutenção estiver vencido. |
| Amarelo | A cor amarela indica que o plano está com a data de vencimento para o dia atual em que se encontra |
| Verde | O verde é para representar planos de manutenção que ainda estão dentro da data de validade. |

**Modo de visualização**

No canto superior direito logo em cima dos dias da semana, existe uma opção para qual será a forma de visualização que irá ser representado os planos de manutenções, sendo elas por dia, semana, mês e linha do tempo. Esta tela salva a preferência do usuário, que ao abrir esta tela novamente , irá salvar o modo de configuração estabelecida anteriormente.

Ao clicar em algum dia no calendário ao lado, a visão irá alterar para a opção "Dia" e mostrará a hora específica em que o plano de manutenção irá vencer ou foi vencido.

**Atualizar Vencimentos Plano(s) de Manutenção**

Com possibilidade de acesso através da aba "Processos" ou pelo ícone adjacente, o processo de atualização dos vencimentos dos planos de manutenção revela todos os planos juntamente com suas datas de vencimento atualizadas. A informação mais recente é destacada no canto superior direito em vermelho.

É fundamental garantir que a média do indicador de uso do objeto de manutenção esteja corretamente definida, pois a atualização da data de vencimento do plano de manutenção depende dessa informação.

Para conferir essa configuração, siga os passos abaixo:

1. Acesse o menu: **Manutenção de Equipamentos > Objetos de Manutenção > Objeto de Manutenção**.
2. Selecione o objeto desejado.
3. Vá até a aba **Indicador(es) de Uso**, onde será possível verificar e/ou calcular a média do indicador.
