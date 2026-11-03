---
article_id: 360018388551
category: Contabilidade Gerencial - Visão Gerencial
content_hash: 704e31c3a0bd7637a0886741aa26e3718a4f467bb785aa6eecbafbf9df3693fe
fetched_at: '2026-06-28T22:40:50.680141+00:00'
product: protheus
section_id: 1500001548642
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB: Qual e a funcionalidade
  da função MovConta?'
type: support-article
updated_at: '2022-07-18T19:28:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018388551-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Qual-e-a-funcionalidade-da-fun%C3%A7%C3%A3o-MovConta
---

**Dúvida**Qual e a funcionalidade da função movconta?

**Ambiente**

#### Cross Segmento - Backoffice Linha Protheus – Contabilidade Gerencial – A partir da versão 11.80 **Solução**A função MovConta() retorna o valor do movimento de uma determinada conta contábil, de acordo com as parametrizações informadas. Uso recomendado para integração básica entre o Protheus e o Microsoft Excel. Pode ser utilizado em outros pontos do Sistema, respeitando a correta parametrização da função.

Sintaxe:

MovConta() - Retorna valor de uma conta contábil ( cContadDataInidDataFimcMoedacTpSaldnQualSaldo [ nSint ] [ nImpAntLP ] [ dDataLP ] ) --> aMovimento[nQualSaldo]

Retorno:

aMovimento[nQualSaldo]

(numerico)* Ver detalhe da composição do array aMovimento

Observações

O Array aMovimento é composto das seguintes informações:

[1] Movimento Devedor  
[2] Movimento Credor  
[3] Movimento do Mes  
[4] Saldo Final

Em função do parâmetro nQualSaldo será retornada uma das possibilidades de saldos contidas no array aMovimento.

Parâmetros:

​

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Descrição |  |  | Default |  |  | Obrigatório |  |  | Referência |  |
|  | cConta |  |  | Caracter |  |  | Codigo da Conta |  |  |  |  |  | X |  |  |  |  |
|  | dDataIni |  |  | Data |  |  | Data inicial para composição do valor do movimento |  |  |  |  |  | X |  |  |  |  |
|  | dDataFim |  |  | Data |  |  | Data final para composição do valor do movimento |  |  |  |  |  | X |  |  |  |  |
|  | cMoeda |  |  | Caracter |  |  | Moeda de referência para o movimento |  |  |  |  |  | X |  |  |  |  |
|  | cTpSald |  |  | Caracter |  |  | Saldo de referência para o movimento |  |  |  |  |  | X |  |  |  |  |
|  | nQualSaldo |  |  | Numérico |  |  | Retorno desejado (ver detalhe do retorno) |  |  |  |  |  | X |  |  |  |  |
|  | nSint |  |  | Numérico |  |  | Indica se a conta é sintética (1) ou analítica (0) |  |  |  |  |  |  |  |  |  |  |
|  | nImpAntLP |  |  | Numérico |  |  | Indica se considera valores anteriores a última apuração de lucros e perdas |  |  |  |  |  |  |  |  |  |  |
|  | dDataLP |  |  | Data |  |  | Data da última apuração de lucros e perdas |  |  |  |  |  |  |  |  |
