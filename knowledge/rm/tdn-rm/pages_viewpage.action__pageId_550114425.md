---
content_hash: 77a390933dc7e07f092293dbf4ce7906d421ce833c42bafb36094acbafa9876f
fetched_at: '2026-06-29T00:10:43.153424+00:00'
page_id: '550114425'
product: rm
source: tdn-rm
title: Integração Orçamento (Folha de Pagamento) com o Quadro de Lotação (Gestão de
  Pessoas)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=550114425
version: 14
---

## **01. VISÃO GERAL**

A partir do release 12.1.27 foi evoluído o módulo de Orçamento (Folha de Pagamento) contemplando a integração com o Quadro de Lotação (Gestão de Pessoas). Assim ao incluir movimentações de funcionário e vagas nos steps do orçamento, será atualizado o número de limite no Quadro de Lotação do módulo Gestão de Pessoas.

## **02. EXEMPLO DE UTILIZAÇÃO**

Ao admitir 1 (um) funcionário em determinada data do ano corrente, para determinada seção e função, será aumentado uma vaga no campo 'Limite Func' em **vagas | Controle de Lotação** do módulo Gestão de Pessoas. Após atualizar o Quadro de Lotação,  o histórico também será atualizado, considerando as informações cadastradas no orçamento.

Ao demitir 1 (um) funcionário em determinada data do ano corrente, para determinada seção, função,  será diminuído uma vaga no campo 'Limite Func' em **vagas | Controle de Lotação** do módulo Gestão de Pessoas. Após atualizar o Quadro de Lotação,  o histórico também será atualizado, considerando as informações cadastradas no orçamento.

Outras movimentações também aumentarão ou diminuirão o 'Limite Func' em **vagas | Controle de Lotação** do módulo Gestão de Pessoas, como Transferência, mudança de seção, mudança de função (promoção).

**Observação:** Para utilizar este recurso será necessário parametrizar o sistema (Gestão de Pessoas) para utilizar 'Controle de Lotação' por vagas em **Ambiente | Parâmetros | Gestão de Pessoas | Controle de Lotação | Vagas**. Para maiores informações do Quadro de Lotação (Gestão de Pessoas), [clique](https://tdn.totvs.com/pages/viewpage.action?pageId=441821507).

**Restrição:** A atualização do limite de funcionário se aplica somente para este tipo de controle, no caso de controle da lotação por seção ou função não é contemplado nesse escopo.

**Veja a seguir como  parametrizar o Módulo Totvs Foha de Pagamento para utilizar a funcionalidade:**

Em **RH | Folha de Pagamento | Configurações | Parametrizador | Orçamento | Parâmetros Gerais do Orçamento**, marcar '**Atualizar Limite de Funcionários no Quadro de Lotação**':

Em **RH | Folha de Pagamento | Configurações | Parametrizador | Orçamento | Alteração do Quadro de Lotação**, criar/incluir os **steps** (Admissão, Demissão, Transferência, Alteração de Seção e Promoção) e definir o **Motivo** e **Ação:**

**Step Admissão:**

**1- Selecionar o parâmetro desejado;**

**2 - Selecionar o Step desejado;**

**3 - Selecionar o Cod. Motivo;**

**Step Demissão:**

**1- Selecionar o parâmetro desejado;**

**2 - Selecionar o Step desejado;**

**3 - Selecionar o Cod. Motivo;**

**Step Transferência:**

**1- Selecionar o parâmetro desejado;**

**2 - Selecionar o Step desejado;**

**3 - Selecionar o Cod. Motivo;**

**Step Alteração de Seção:**

**1- Selecionar o parâmetro desejado;**

**2 - Selecionar o Step desejado;**

**3 - Selecionar o Cod. Motivo;**

**Setp Promoção**

**1- Selecionar o parâmetro desejado;**

**2 - Selecionar o Step desejado;**

**3 - Selecionar o Cod. Motivo;**

## **03. DEMAIS INFORMAÇÕES**

ATENÇÂO

Caso o parâmetro ***"ATUALIZAR LIMITE DE FUNCIONÁRIOS NO QUADRO DE LOTAÇÃO"***, localizado em **Folha de pagamento| Configurações| Parametrizador| Orçamento| Parâmetros Gerais Orçamento**, esteja marcado e os steps informados em ***"ALTERAÇÃO DO QUADRO DE LOTAÇÃO"***localizado em **Folha de pagamento| Configurações| Parametrizador| Orçamento**, o sistema terá os seguintes funcionamentos para cada Step:

Ao informar os motivos da movimentação nos Steps do Orçamento, seguirá as regras descritas no parâmetro, conforme citado no exemplo abaixo:

**Admissão**

* ***Motivos para atualizar o limite de funcionário no Quadro de Lotação (Aumenta)***

+ ***Aumento de Quadro;***

**Demissão**

* ***Motivos para atualizar o limite de funcionário no Quadro de Lotação (Diminui)***

+ ***Redução de Quadro;***

**Transferência**

* ***Motivos para atualizar o limite de funcionário no QL (Diminui na origem/Aumenta no destino)***

+ ***Substituição;***

**Mudança de Função (Promoção)**

* ***Motivos para atualizar o limite de funcionário no QL (Diminui na origem/Aumenta no destino)***

+ ***Mudança de Função;***

**Mudança de Seção**

* ***Motivos para atualizar o limite de funcionário no QL (Diminui na origem/ Aumenta no destino)***

+ ***Mudança de Seção.***
Demais Informações Orçamento

Para mais informações sobre o orçamento e o comportamento do mesmo junto ao quadro de lotação no sistema:

* [Dados do Orçamento](https://tdn.totvs.com/display/public/LRM/Orcamento+Folha+de+Pagamento)
* [Parametrização - Parametrizador](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452718732)
* [Outros links sobre Orçamento](https://tdn.totvs.com.br/pages/viewpage.action?pageId=266981335)
* [Gestão de Pessoas - Quadro de lotação - (Histórico de limite de vagas - Quadro de lotação)](https://tdn.totvs.com/pages/viewpage.action?pageId=441821507)
* [Orçamento - Inclusão via DataServer](https://tdn.totvs.com/pages/viewpage.action?pageId=549499868)
