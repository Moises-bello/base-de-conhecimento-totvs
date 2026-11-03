---
content_hash: f6f578525cfa6ead462776c61496cf1c04e9209a9abfd550d0886c028a504f6c
fetched_at: '2026-06-29T00:10:07.828375+00:00'
page_id: '452719446'
product: rm
source: tdn-rm
title: Cancelamento de movimento - FOP
type: documentation
url: https://tdn.totvs.com/display/LRM/Cancelamento+de+movimento+-+FOP
version: 17
---

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Tela Cancelamento de Movimento**
   1. **Principais Campos e Parâmetros**
5. **Tabelas utilizadas**

## **01. VERSÕES**

false

**Atualização com Fracionamento de Jobs a partir dos patches:**

* 12.1.2306.180
* 12.1.2310.114
* 12.1.2402 e Superiores

## **02. VISÃO GERAL**

A movimentação do funcionário deve ser lançada  mensalmente no envelope de pagamento e neste caso deve existir a possibilidade de cancelar um ou vários eventos lançados, ou toda a movimentação do último período ou de todos os períodos de um mês.

Dica

Esse módulo pode ser executado com fracionamento de Jobs, veja mais informações em [Segurança de Jobs Fracionáveis](https://tdn.totvs.com/pages/viewpage.action?pageId=547231277).

Quando utilizar "Incrementa Códigos Fixos" fique atento para as seguintes informações:  
**Atenção:**

1. O sistema verificará quantas vezes o evento de Código Fixo aparece na movimentação, quando o usuário seleciona todos os períodos para cancelamento e incrementará o nº de vezes em que ele foi lançado em todos os períodos. Em caso de cancelamento somente do período atual, o sistema incrementará uma única vez.
2. Quando os campos "Incrementa códigos fixos" e "Grava movimento cancelado" estão marcados e o usuário deseja importar esta movimentação novamente, o sistema não deduzirá automaticamente o campo "Nº de vezes" dos códigos fixos (c/nº de vezes diferente de 999). Portanto, o acerto do nº de vezes do Código Fixo deverá ser feito manualmente pelo usuário.

Quando utilizar "Cancela Movimentação por Centro de Custo" fique atento para as seguintes informações:  
**Atenção:**

1. O campo "Cancela Movimentação por Centro de Custo" e "Todos os Centros de Custos" cancelam todos os centros de custo, inclusive os editados manualmente dentro da ficha financeira.
2. O campo "Cancela Movimentação por Centro de Custo" somente cancela um centro de custo, quando editado manualmente, ficando inconsistente com o envelope de pagamento, já que existem centros de custos que não foram cancelados na ficha financeira, e o evento no envelope existe apenas com os centros de custos restantes, isto é, que ainda não foram cancelados. Se não estiver editado, o cancelamento por apenas um centro de custo cancelará todos os centros de custos existentes.

Quando o parâmetro “Usa folha agrária” em Parametrizador / Folha Agrária estiver marcado será habilitado os seguintes parâmetros:

* Atualiza cadastro de convênios
* Atualiza movimento da produção agrária
* Atualiza cadastro de comissões

 Quando a opção "Retificação folha/rescisão" for habilitada o cancelamento irá ocorrer em apenas um Job,

Utilizar "Grava Movimento Cancelado" para que a movimentação cancelada seja preservada em arquivo.    
**Atenção:** No caso dos dados serem cancelados e salvos em arquivo texto, os dados poderão ser novamente reintregados à base, via importação de movimento.

## **03.** **EXEMPLO DE UTILIZAÇÃO**

**Nesse item será demonstrado alguns exemplos para o módulo de cancelamento.**

11Parâmetro 'Habilita controle de rescisão não calculada' 

No processo de cancelamento de movimento, que quando marcado, irá cancelar a movimentação do demitido no mês, sem alterar sua situação e retornando a informação de rescisão calculada para falso (PFUNC>RESCISAOCALCULADA =0). 

**Atenção**

O Parâmetro 'Habilita controle de rescisão não calculada' só ficará habilitado para uso caso o parâmetro 'Cancela movimento de demitido no mês' estiver marcado. Este controle não será feito em caso de rescisão calculada no próximo mês.

Quando existir algum evento de valor forçado e o campo 'Cancela eventos alterados manualmente' estiver desmarcado, caso o parâmetro 'Habilita controle de rescisão não calculada' estiver marcado não irá cancelar os eventos de valores forçados, porém irá mudar a informação de rescisão calculada para falso.

2Parâmetro Marcado

Processo de Cancelamento marcando o controle:

Movimentação excluída:

O campo RESCISAOCALCULADA = 0

3Parâmetro Desmarcado

Processo de Cancelamento sem marcar o controle:

Movimentação excluída:

O campo RESCISAOCALCULADA = 1

21Cancelamento sem fracionamento de Jobs

Na base exemplo fictícia foi executado o cancelamento sem parametrizar o fracionamento de jobs e abaixo demonstramos como seria o resumo da execução:

2Cancelamento com fracionamento de Jobs

Na base exemplo fictícia foi executado o cancelamento com parametrizar o fracionamento de jobs e abaixo demonstramos como seria o resumo da execução:

## **04.** **TELA Cancelamento de Movimento**

**Principais Campos e Parâmetros**

| Campo | Descrição |
| --- | --- |
| Quebra de Seção | Selecionar a quebra |
| Seleção de funcionários | Selecionar um filtro de funcionários |
| Período mês atual   Período próximo mês | No momento da seleção do período haverá a possibilidade de selecionar:  Cancela movimentação do período atual ou   Cancela todos os períodos  Sendo que selecionando a primeira opção serão cancelados todos os eventos de um determinado período. E nesse caso também será disponibilizada a pasta "Eventos a Cancelar" para selecionar um evento ou mais para serem cancelados. |
| Retificação folha/rescisão | Para cancelar o período que foi lançada a retificação de desligamento ou folha de pagamento deve ser marcado o parâmetro Retificação folha/rescisão e informar a competência e o período que se quer cancelar. Atenção:   Não será possível o recálculo da retificação, caso seja necessário deve cancelar através do cancelamento de folha e depois lançar novamente.  O cancelamento da retificação da folha só é possível caso seja cancelado o período atual onde foram lançados os valores dos líquidos da retificação.  Cancela todos os eventos, não há possibilidade de selecionar eventos. |
| Cancela eventos alterados manualmente | Marcar  para realizar o cancelamento dos eventos alterados manualmente dentro do envelope somente quando está selecionado o cancelamento de determinado período.   Se selecionar o período “Todos” o evento será cancelado independentemente do parâmetro marcado ou não. |
| Cancela verbas com insuficiência de saldo | Marcar para realizar o cancelamento dos eventos com insuficiência de saldo para os funcionários que utilizam o campo "Controle de Saldo de Verbas" no cadastro de funcionários. |
| Cancela movimento de demitido no mês | Marcar para cancelar a movimentação da ficha financeira do demitido no mês, sem cancelar os dados de rescisão. |
| Habilita controle de rescisão não calculada | Marcar para alterar a informação do campo rescisão calculada (PFUNC.RESCISAOCALCULADA)  para falso.  Atenção: O campo 'Habilita controle de rescisão não calculada' só ficará habilitado para uso caso parâmetro 'Cancela movimento de demitidos no mês' estiver marcado |
| Cancela movimento de férias | Marcar para cancelar a movimentação da ficha financeira das férias, sem cancelar os dados cadastrados.   Atenção: Nesse caso deve lançar novamente as férias para que os valores voltem ao envelope ou então excluir o cadastro das férias para não ter inconsistência na base de dados. |
| Cancela eventos de origem do Gerenciador de Movimento | Quando o parâmetro ‘Utiliza Gerenciador de Movimento’ estiver marcado no parametrizador em Folha Normal / Cálculo 2/2, então esse parâmetro ‘Cancela eventos de origem do Gerenciador de Movimento’ será habilitado e servirá para cancelar os eventos de origem do gerenciador de movimentos. |
| Cancela movimentação por centro de custo | Marcar  para cancelar a movimentação por centro de custo que possua o campo EDITADO = 1. Não utilizando, somente a movimentação por centro de custo com o campo EDITADO = 0 será cancelada. |
| Incrementa códigos fixos | Quando há o lançamento de um código fixo cadastrado no funcionário o número de vezes para lançamento é decrementado conforme parametrização.  Utilizar "Incrementa Códigos Fixos", para incrementar o número de vezes do Código Fixo do funcionário quando se realiza o cancelamento, sendo que, somente será incrementado o número de vezes quando este for diferente de 999. |
| Atualiza cadastro de empréstimos | Quando há o lançamento de empréstimo cadastrado no funcionário, esse cadastro é alterado para constar o pagamento. Ao utilizar esse parâmetro o cadastro do empréstimo retorna ao valor anterior ao lançamento. |
| Atualiza cadastro de convênios | Deverá retirar o mês, ano de pagamento de movimentação de convênios em que o evento da ficha financeira excluída pertença à despesa dentro da competência do evento excluído. |
| Atualiza movimento da produção agrária | Deverá retirar o mês, ano, período de competência de lançamento da produção do funcionário em que o evento da ficha financeira excluído pertence à produção dentro da competência do evento excluído. |
| Atualiza cadastro de comissões | Deverá retirar o mês, ano de pagamento das comissões de funcionários em que o evento da ficha financeira excluída pertença à comissão dentro da competência do evento excluído. |

**Tela de Parâmetros de Cancelamento de Movimento Informados:**

## **05.** **TABELAS UTILIZADAS**

* PFPERFF
* PFFINANC
* PFMOVCC
* PVERBAS
* PFUNC
* PFCODFIX
* PFEMPRT
* PPRODUCAOAGRARIA
