---
content_hash: 4c9e57ccec5dc5a8053de588faadf4aa36212c6b4b677d56f01dff7c489e29d9
fetched_at: '2026-06-29T00:09:13.530282+00:00'
page_id: '421366983'
product: rm
source: tdn-rm
title: Aplicação Financeira - Perguntas e Respostas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421366983
version: 19
---

A aplicação que desejo lançar é suportada pelo sistema?

**RESPOSTA**

O sistema hoje suporta os seguintes tipo de aplicação financeira:

* Fundos de Investimento de Renda Fixa (DI)
* Poupança (para Pessoas Jurídicas identificadas como Entidades sem Fins Lucrativos)
* CDB Prefixado
* CDB Pós Fixados

Obs: Destaco como **NÃO** suportados todas as modalidades de CDBs que tenham taxas variáveis em função do tempo da aplicação.

[Resgate] - Valor bruto ou valor líquido, qual informar?

**RESPOSTA**

A maioria dos extratos de aplicações financeiras trazem apenas o valor líquido do resgate, porém alguns extratos são mais detalhados, trazendo o valor bruto do resgate, os impostos (IR, IOF) e o valor líquido.

Para atender todos os cenários, no sistema deve ser informado o **valor líquido** do resgate. Muitas vezes o usuário se confunde e informa o valor bruto, gerando inconsistência.

[Resgate] - Dois resgates no mesmo dia, como registrar no sitema?

**RESPOSTA**

Nos casos onde foram realizados dois resgates no mesmo dia, é necessário somar o valor líquido dos resgates e incluir um único resgate no sistema.  
No exemplo abaixo, incluir um resgate no dia 22/05/2025 no valor de R$1.316.473,89 (R$17.670,89 + R$1.298.803,00)

[Encerramento] - O encerramento do mês anterior do extrato coincide com o saldo inicial do extrato mensal?

**RESPOSTA**

O encerramento mensal da aplicação financeira oferece um ótimo ponto de referência para avaliar a integridade do cálculo até aquele ponto. O valor do encerramento mensal, e a quantidade de cotas (no caso de fundos de investimentos) podem ser confrontados com o saldo inicial do extrato da aplicação financeira.

[Ajustes] - Ajuste Positivo/Negativo de valores, quando usar e até que valor?

**RESPOSTA**

O módulo de Aplicação Financeira dentro da Linha RM, tem o objetivo de chegar o mais próximo possível do valor calculado pelo banco, mas como a regra de cálculo e as formas de arredondamento não são públicas, temos ciência que podem existir sim diferenças de valores.  
Estas diferenças são ainda mais comuns nos fundos de investimento, onde podem existir várias aplicações em aberto, e um resgate atingir as cotas de várias aplicações.

Nesse momento cada empresa deve avaliar qual o limite de diferença que entende como aceitável. O mais importante é, mesmo considerando como aceitável, o ajuste deve ser realizado, pois são considerados nos cálculos futuros.

[Fundo de Investimento] - Será que está faltando algum lançamento?

**RESPOSTA**

Se no extrato trouxer o saldo de cotas em cada operação, é possível avaliar se a quantidade de cotas está correta em qualquer instante. Basta executar um resgate total na data, a quantidade de cotas disponível corresponde à soma da quantidade de cotas do Resgate, IR e IOF.

[Fundo de Investimento] - As cotações informadas estão corretas?

**RESPOSTA**

As cotações de fundos de investimento podem ser coletadas no site da CVM. O acesso é facilitado se tiver em mãos o CNPJ do fundo de investimento, mas também é possível buscar pela informação com parte do nome do título.

<https://cvmweb.cvm.gov.br/swb/default.asp?sg_sistema=fundosreg>

[Fundo de Invetimento] - Como e quando identificar se devo marcar a opção "Rendimento do último dia do período come-cotas não será considerado no come-cotas posterior"?

**RESPOSTA**

A [Lei L14754](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/L14754.htm) alterou a base de cálculo do come cotas em fundo de investimento, para que no dia do cálculo do come cotas, a cotação a ser considerada seja d-1 (dia útil).

Neste contexto, tem havido divergência de interpretação entre alguns Gestores de Fundos, que optam por desconsiderar o rendimento deste ultimo dia útil do peíodo do come-cotas no cálculo do próximo período.

Este parâmetro fica visível na tela de cadastro da aplicação apenas para fundos de rendimento.

Como não é possível determinar a interpretação do gestor, e essa informação também não é explícita no extrato, caso no primeiro resgate após um período de come cotas apresente difereça no valor do IR, é necessário marcar o parâmetro e refazer a inclusão do resgate, se mesmo assim ainda apresentar diferença, será necessário investigar outras causas.

[Fundo de Invetimento] - Resgate e IR Come Cotas no mesmo dia, como registrar no sitema?

**RESPOSTA**

Algumas vezes surgem demandas de clientes questionando o valor da retenção do IR come-cotas. Normalmente nestes casos ocorre do gestor do fundo de investimento ter retido o IR come-cotas como primeira operação do dia, e no mesmo dia haver também algum resgate.

Para atende este cenário, criamos um processo específico, e vamos utilizar o exemplo abaixo para exemplificar:  
No dia 30/05/2025, é necessário primeiro executar o processo "**Resgate do IR Come-Cotas**", e logo depois executar o processo de "**Resgate**".  
Nestes casos, como o come-cotas já terá sido calculado, ao realizar o encerramento, o mesmo não será calculado novamente.

Para os casos que não existe resgate no mesmo dia, apenas a retenção do IR come-cota, nada muda, basta realizar o encerramento do mês, que o come-cotas será calculado.

[Fundo de Investimento] - O que é IOF Virtual e quando marcar esta opção?

**RESPOSTA**

Quando ocorre o **come-cotas**, o sistema avalia se existem aplicações com menos de 30 dias.  
Se existirem, é calculado um valor de **IOF apenas para compor a base de cálculo do IR**, mesmo que esse IOF **ainda não seja descontado** do investidor.

No mês seguinte ao come-cotas (junho ou dezembro), ao realizar um **resgate dessas aplicações**, o IOF passa a ser efetivamente cobrado.

O problema é que **os gestores de fundos não adotam um único padrão** para esse cálculo:

* Alguns gestores recalculam o IOF usando a **tabela regressiva**, considerando os dias até a data do resgate.
* Outros gestores utilizam **o mesmo valor de IOF calculado no come-cotas**, sem recálculo.

Para permitir que o valor calculado no sistema fique igual ao valor apresentado no extrato do fundo, foi criada a opção **“Considerar IOF Virtual Integral”** no resgate.

### Exemplo prático (racional)

* Aplicação realizada em: **20/05**
* Come-cotas em: **31/05** (aplicação com 11 dias)
* IOF calculado apenas para base no come-cotas: **R$ 100**
* Nenhum IOF é descontado nesse momento.

Em **10/06**, o investidor realiza um resgate total da aplicação:

**Situação A — Gestor usa tabela regressiva:**

* Considera os dias entre 20/05 e 10/06
* IOF efetivo apurado: **R$ 40**
* Sistema padrão calcula usando R$ 40

**Situação B — Gestor usa IOF Virtual Integral:**

* Considera o IOF calculado no come-cotas
* IOF considerado: **R$ 100**
* Usuário deve marcar a opção **IOF Virtual Integral** no resgate

Resultado:  
Sem marcar a opção, o IR calculado pelo sistema será diferente do extrato do fundo.  
Marcando a opção, os valores passam a coincidir.

[CDB] - As cotações informadas estão corretas?

**RESPOSTA**

As cotações fator DI podem ser coletados no site da B3, através do menu “Market data e Índices | Índices de Segmentos e Setoriais | Índice DI”.   
Informe o período desejado e marque o checkbox “Média”.

<http://www.b3.com.br/pt_br/>

**Mais detalhes acesse o documento de referência da aplicação:**

[Aplicação Financeira](https://tdn.totvs.com/x/1uEdGQ)
