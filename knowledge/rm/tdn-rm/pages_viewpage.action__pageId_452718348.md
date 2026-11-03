---
content_hash: 184c80f514ec549ef45692f1924278cde7597199f18dad2c888aaa464c4d4d5f
fetched_at: '2026-06-29T00:09:59.420878+00:00'
page_id: '452718348'
product: rm
source: tdn-rm
title: Grupo de Benefícios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718348
version: 2
---

**Grupo de Benefícios**

O cadastro de grupos de benefícios possibilita relacionar os benefícios existentes por meio de regras para elegibilidade específicas. Estas regras serão utilizadas para validar as solicitações de adesão efetuadas através do Portal.

**Observação**

- Uma vez que o grupo de benefícios foi salvo não é possível mais alterar o tipo do grupo nem o campo Benefício de Referencia.

- O campo cota ficará habilitado somente após a seleção do tipo "Exclusividade". Para seu preenchimento correto não são válidos valores negativos nem valores que sejam maiores que o total de benefícios vinculados ao grupo.

- O Campo Benefício de Referencia lista todos os benefícios cadastrados no RM Vitae não possui valor default e ficará habilitado somente após a seleção do tipo "Dependência".

- Um mesmo benefício pode fazer parte de vários grupos com tipos de elegibilidade distintos, as regras de cada grupo serão validadas ao lançar o benefício através do Assistente de Lançamento de Benefícios.

- Todos os lançamentos realizados através do Assistente de Lançamento de Benefícios terão como data de referência para a validação do grupo de benefícios, a data informada para o início do período.

Pelo cadastro é possível controlar:

**Benefícios de Exclusividade**

- A elegibilidade exclusiva significa que a escolha feita por um determinado benefício limitará a escolha de outro benefício com base no critério de cota de grupo.

- A cota do grupo estabelece um valor inteiro que pode variar de 0 (zero) até a quantidade total de benefícios vinculados ao grupo.

- Um benefício não pode ser vinculado ao mesmo grupo mais de uma vez.

- A elegibilidade do benefício não será verificada individualmente, a cota do grupo será única para o funcionário e seus dependentes.

- Quando o benefício for extensível a dependentes e o mesmo estiver lançado para o Funcionário e para o Dependente somente uma ocorrência do benefício deverá ser levada em consideração na quantidade da cota.

**Benefícios de Dependência**

- A elegibilidade por dependência significa que a escolha feita por um determinado benefício obrigará a adesão ao benefício de referência e, ao efetivar o benefício de dependência serão vinculados todos os benefícios do grupo.

- Um grupo de dependência é constituído por um único benefício de referência e um ou vários benefícios dependentes.

- O benefício de referência é exigido como pré-requisito sempre que for solicitada adesão a qualquer outro benefício dependente do grupo.

- Um benefício não pode ser vinculado ao mesmo grupo mais de uma vez, seja como um benefício de referência, seja como um benefício dependente.

- A elegibilidade do benefício será verificada individualmente, seja para validar uma solicitação para funcionário, seja para validar uma solicitação para seus dependentes.
