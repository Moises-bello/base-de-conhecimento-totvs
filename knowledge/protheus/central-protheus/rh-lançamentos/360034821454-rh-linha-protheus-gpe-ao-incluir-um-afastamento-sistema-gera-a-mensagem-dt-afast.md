---
article_id: 360034821454
category: RH - Lançamentos
content_hash: 0897880dc3492bf81f601b8d7043318cd900c442791b06adaebe67264b631d54
fetched_at: '2026-06-28T22:43:31.126221+00:00'
product: protheus
section_id: 360010781734
source: central-protheus
title: 'RH - Linha Protheus - GPE - Ao incluir um afastamento sistema gera a mensagem:
  Dt. Afastam. Valor inválido'
type: support-article
updated_at: '2025-04-17T18:30:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034821454-RH-Linha-Protheus-GPE-Ao-incluir-um-afastamento-sistema-gera-a-mensagem-Dt-Afastam-Valor-inv%C3%A1lido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Ao incluir um afastamento sistema gera a mensagem: **Dt. Afastam. Valor inválido**  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

Verifique o cadastro de períodos, aba Calendário - Tabela RCG e aba Período - Tabela RFQ, onde deve constar data final correta em ambas, por exemplo:

Mês de 31 dias:

Para a tabela RFQ a data fim tem que ser dia 31, caso esteja dia 30 sistema retornará a mensagem

Para a tabela RCG sistema monta o calendário. Como a data fim estava dia 30, esta tabela o último dia irá constar dia 30

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11784113388823)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11784167605783)

Faça o ajuste, excluindo o período e incluindo novamente com a data correta. Se o cadastro de períodos estiver correto, localize a tabela RCH no banco de dados, filtre o processo e o período que deseja incluir o afastamento, localize o campo RCH\_DTCORT, onde, caso tenha conteúdo deve ser limpo para depois deste processo, incluir o afastamento.

**Saiba Mais**  
[RH - Linha Protheus - GPE - Como efetuar o cadastro de período](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052262653-RH-Linha-Protheus-GPE-Como-efetuar-o-cadastro-de-per%C3%ADodo?source=search)

[RH - Linha Protheus - GPE - Como fazer para que o sistema considere o dia 31 no mês de retorno do afastamento para montagem do saldo de salário proporcional do empregado, mesmo que mensalista](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000010482-RH-Linha-Protheus-GPE-Como-fazer-para-que-o-sistema-considere-o-dia-31-no-m%C3%AAs-de-retorno-do-afastamento-para-montagem-do-saldo-de-sal%C3%A1rio-proporcional-do-empregado-mesmo-que-mensalista?source=search)

[RH - Linha Protheus - GPE - Cabeçalho das Férias não traz o campo Salário preenchido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018112252-RH-Linha-Protheus-GPE-Cabe%C3%A7alho-das-F%C3%A9rias-n%C3%A3o-traz-o-campo-Sal%C3%A1rio-preenchido?source=search)

[RH - Linha Protheus - GPE - Como configurar o parâmetro MV\_DIASPER para definir regra de calculo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059317953-RH-Linha-Protheus-GPE-Como-configurar-o-par%C3%A2metro-MV-DIASPER-para-definir-regra-de-calculo?source=search)

[RH - Linha Protheus - GPE - Funcionário preso - Afastado por Cárcere](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9928703393303-RH-Linha-Protheus-GPE-Funcion%C3%A1rio-preso-Afastado-por-C%C3%A1rcere?source=search)

[RH - Linha Protheus - GPE - Como cadastrar estabilidade após retorno de Ausência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048518013-RH-Linha-Protheus-GPE-Como-cadastrar-estabilidade-ap%C3%B3s-retorno-de-Aus%C3%AAncia?source=search)

[RH - Linha Protheus - GPE - Como informar para o sistema que o novo afastamento é sequencia do anterior](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049659234-RH-Linha-Protheus-GPE-Como-informar-para-o-sistema-que-o-novo-afastamento-%C3%A9-sequencia-do-anterior?source=search)

[RH - Linha Protheus - GPE - Lançamento de ausência, gera mensagem Limite de lançamentos do mesmo tipo para um mesmo período alcançado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039472494-RH-Linha-Protheus-GPE-Lan%C3%A7amento-de-aus%C3%AAncia-gera-mensagem-Limite-de-lan%C3%A7amentos-do-mesmo-tipo-para-um-mesmo-per%C3%ADodo-alcan%C3%A7ado-?source=search)

[RH - Linha Protheus - GPE - Funcionário afastado com situação normal no relatório da folha de pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052165074-RH-Linha-Protheus-GPE-Funcion%C3%A1rio-afastado-com-situa%C3%A7%C3%A3o-normal-no-relat%C3%B3rio-da-folha-de-pagamento?source=search)

[RH - Linha Protheus - GPE - Como informar data fim de afastamentos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006476621-RH-Linha-Protheus-GPE-Como-informar-data-fim-de-afastamentos?source=search)
