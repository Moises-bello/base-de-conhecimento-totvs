---
content_hash: c12a349b368df8f2f923a1163395c1ceeb827a665c04b2cc271c4ec2690b7b35
fetched_at: '2026-06-29T00:11:11.117162+00:00'
page_id: '645672556'
product: rm
source: tdn-rm
title: Operações Intercompany - Parametrização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=645672556
version: 3
---

De acordo com a NBC TG 36, as demonstrações contábeis consolidadas de grupos econômicos devem: 

1. Combinar itens similares de ativos, passivos, patrimônio líquido, receitas, despesas e fluxos de caixa da controladora com os de suas controladas;
2. Compensar (eliminar) o valor contábil do investimento da controladora em cada controlada e a parcela da controladora no patrimônio líquido de cada controlada
3. Eliminar integralmente ativos e passivos, patrimônio líquido, receitas, despesas e fluxos de caixa **intragrupo** relacionados a transações entre entidades do grupo (resultados decorrentes de transações intragrupo que sejam reconhecidos em ativos, tais como estoques e ativos fixos, são eliminados integralmente).

Alguns exemplos de eliminações são:

* Conta de investimento de  participação na empresa controladora em contrapartida à conta de patrimônio líquido da investida.
* Operações intercompany.
* Conta de equivalência patrimonial da empresa investidora em contrapartida da conta de resultado das empresas investidas.

O objetivo desse passo a passo é orientar a correta parametrização do sistema para a identificação das operações contábeis que deverão ser eliminadas no momento da consolidação.

---

a,b,c,d,eaConta Contábil

Criamos no Cadastro da Conta Contábil (aba Identificação) o flag “**Eliminar valores na consolidação**” que deve estar marcado caso queira que as operações dessa conta sejam eliminadas na consolidação.

Clique aqui para expandir

**Importante!**

É preciso que as Contas Contábeis estejam parametrizadas em todas as Coligadas envolvidas na operação para correta eliminação dos valores.

bLançamento Contábil

Na Partida, ao informar uma Conta Contábil que esteja com o Flag “**Eliminar valores na consolidação**” marcado, será habilitada a aba “Eliminação” onde devem ser informados a Coligada e a Conta Contábil Contrapartida da operação:

Clique aqui para expandir

**Importante!**

* Serão apresentadas apenas Contas Contábeis de Eliminação.
* Uma vez que as informações de Eliminações estão na Partida, o sistema NÃO permitirá que, em uma mesma Partida, seja informada uma Conta Contábil que está com o flag de Eliminação marcado em conjunto com outra que esteja com ele desmarcado. Neste cenário, será preciso utilizar partidas diferentes para cada conta.
* A Coligada e a Conta Contábil Contrapartida da operação devem ser informadas em todas as Coligadas envolvidas na operação.
cEvento Contábil

Assim como na Partida, no Cadastro do Evento Contábil também foram incluídos, na pasta Dados Complementares do Item do Evento, os campos “**Coligada contrapartida da eliminação**” e “**Conta contrapartida da eliminação**” com o objetivo de automatizar a inclusão dessas informações na Partida sem a necessidade de informá-las manualmente na Contabilidade.

Clique aqui para expandirdData de Corte para o novo modelo

Para fins de cálculo dos valores de eliminação, o sistema observará a data de início do uso das eliminações a partir do Lançamento Contábil. Esse parâmetro está na Etapa 01.04 - Fechamento.

**Mas, atenção!**

* **Não devem existir Lançamentos Contábeis com informações de eliminação anteriores à Data de Corte!** Caso isso ocorra, os valores ficarão duplicados no processo do Cálculo Consolidado.
* O sistema não permitirá a inclusão de valores de eliminação no Plano de Contas Paralelo a partir dessa data.

Clique aqui para expandirIMPORTANTE!

Será preciso fechar o período contábil do ano anterior à adoção do novo modelo e, após o fechamento, inserir o saldo anterior das Eliminações através do Processo "**Inserir Saldo Inicial em Conta de Eliminação**".

Isso se faz necessário para que o sistema consiga calcular corretamente os saldos nos relatórios contábeis.

Para mais informações sobre este processo, consulte nossa documentação neste .
