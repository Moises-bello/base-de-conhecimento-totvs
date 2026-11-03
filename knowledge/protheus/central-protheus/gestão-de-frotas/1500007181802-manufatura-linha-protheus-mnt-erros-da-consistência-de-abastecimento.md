---
article_id: 1500007181802
category: Gestão de Frotas
content_hash: 0ae473172278a936e7eb2b1c6a249214dd592aa44eefcefea3cb92004b46b78b
fetched_at: '2026-06-28T22:42:39.401013+00:00'
product: protheus
section_id: 360012117873
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Erros da consistência de abastecimento
type: support-article
updated_at: '2021-10-29T11:29:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007181802-Manufatura-Linha-Protheus-MNT-Erros-da-consist%C3%AAncia-de-abastecimento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)** Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como são definidos os erros da rotina de **Consistência de Abastecimento - MNTA635**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Gestão de Frotas - Todas as versões  
  
**Solução**As inconsistências são definidas após ocorrerem as validações de uma importação de abastecimento, através da rotina de **Consistência de Abastecimento - MNTA635**. Quando um abastecimento está incorreto, são gerados os erros de acordo com a definição a seguir: 

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500009891762/mceclip0.png)

| Consistência | Erro | Descrição |
| --- | --- | --- |
| Validações Genéricas | 13 | Motorista não informado |
| 51 | Não foi informada data para o abastecimento |
| 52 | Não foi informada hora para o abastecimento |
| 53 | Data/Hora de abastecimento maior que a data atual |
| 55 | Combustível não informado |
| 58 | Local de estoque do tanque encontrado em várias filiais |
| Identifica Posto | 06 | CNPJ do posto não informado |
| 07 | Posto não cadastrado |
| 24 | CNPJ inválido |
| Consiste Posto | 03 | Valor do abastecimento zerado |
| 08 | Divergência do valor negociado |
| 09 | Valor negociado igual a zero |
| 11 | Não há valor negociado para este posto |
| 15 | Posto cadastrado como não conveniado |
| 16 | Posto de combustível está desativado |
| Identifica Combustível | 55 | Combustível não informado |
| 56 | Combustível não cadastrado |
| Consiste Posto Interno | 33 | Tanque não informado |
| 40 | Sem aferição para o dia |
| 57 | Data/Hora de abastecimento menor que a data de inclusão da bomba |
| Consiste Combustível + Tanque Veículo | 19 | Litragem maior que a máxima permitida |
| 32 | Combustível incompatível com tanque do bem |
| Consiste Motorista | 12 | CPF do motorista não existe no cadastro de funcionário |
| 13 | Motorista não informado |
| 21 | Motorista afastado |
| 22 | Abastecimento após demissão |
| 25 | Motorista não cadastrado |
| 26 | Motorista demitido |
| 31 | Abastecimento com a mesma data e hora que histórico do contador |
| Consiste Saldo Estoque | 43 | Saldo insuficiente na data do abastecimento |
| Identifica Veículo | 04 | Placa do veículo não informada |
| 05 | Veículo não cadastrado |
| Consiste Veículo | 01 | Km igual a zero |
| 02 | Km maior que limite do contador |
| 17 | Km menor ou igual ao Km do último abastecimento |
| 18 | Km maior ou igual ao Km do abastecimento posterior |
| 27 | Problema de variação dia |
| 28 | Abastecimento superou a autonomia do veículo |
| 29 | Data, hora e contador menor ou igual ao histórico de contador |
| 30 | Abastecimento com mesma data e hora que histórico do contador |
| 34 | Contador 2 - Data, hora e contador menor ou igual ao histórico de contador |
| 35 | Contador 2 - Km menor ou igual ao Km do último abastecimento |
| 36 | Contador 2 - Km maior ou igual ao Km do abastecimento posterior |
| 37 | Contador 2 - Km maior que limite do contador |
| 38 | Contador 2 - Problema de variação dia |
| 39 | Contador 2 - Abastecimento com a mesma data e hora que histórico de contador |
| 51 | Não foi informada data para o abastecimento |
| Consiste Transferência de Combustível | 41 | Transferência para o mesmo armazém |
| 42 | Produtos diferentes |
| 99 | Transferência inválida |
