---
article_id: 360018632072
category: Contabilidade Gerencial - Visão Gerencial
content_hash: 282da2d3bbf830d1b6a82883284c8ea27faf67885a3b0f3a75e8404f3cfb61c8
fetched_at: '2026-06-28T22:40:50.574176+00:00'
product: protheus
section_id: 1500001548642
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA161 - Expressões
  especiais para o campo Fórmula
type: support-article
updated_at: '2023-01-04T14:41:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018632072-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA161-Express%C3%B5es-especiais-para-o-campo-F%C3%B3rmula
---

**Dúvida**Quais as expressões especiais da Visão Gerencial?

**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.  
  
  
**Solução**

Está disponível o recurso de fórmula para o cadastro em que há situações de retorno de valor condicional, ou cálculos específicos de saldo/movimento ao gerar relatório com visões gerenciais.É possível preencher o campo **Fórmula** com a função que realiza o tratamento condicional de retorno do valor da linha de detalhe da entidade analítica.

As expressões suportadas atualmente pelo campo **Fórmula** da visão gerencial são:

**1- Expressão “ROTINA=”**

* **Sintaxe**: ROTINA=FUNCAO()

Com o conteúdo **ROTINA=**, o retorno da função especificada serve como uma base ou fator de multiplicação a ser aplicado sobre os saldos originais, ou seja, o saldo correspondente ao intervalo de entidades definida na linha da entidade/visão gerencial multiplicado pelo retorno da função especificada (se o retorno for zero o saldo por conseqüência passa a ser zero no relatório).

**Observação**

O retorno da expressão **ROTINA=** atualiza apenas o saldo atual da entidade gerencial analítica, e é repetido para a coluna de saldo anterior, se for parametrizada para exibição em função do processamento do relatório ou consulta.

**2- Expressão "SALDO"=**

* **Sintaxe**: SALDO=FUNCAO()

Com o conteúdo 'SALDO=', o retorno da função especificada é o valor do saldo apresentado no relatório, de maneira independente do intervalo de entidades informado da linha da entidade visão/gerencial.

**Observação**

O retorno da expressão **SALDO=** atualiza apenas o saldo atual da entidade gerencial analítica, e será repetido para a coluna de saldo anterior, se for parametrizada para exibição em função do processamento do relatório ou consulta.

**3-Expressão “TEXTO=”**

* **Sintaxe**: ("texto\_definido\_pelo\_usuário ").

Com o conteúdo ‘TEXTO=’, a string especificada entra aspas (“”) é impressa na geração da visão gerencial como uma linha de comentário / descrição para o relatório gerado, substituindo a descrição da entidade gerencial.

**4-Expressão “ENTIDADE=”**

* **Sintaxe**: ENTIDADE=Código\_da\_entidade

 Com o conteúdo ‘ENTIDADE =’, o retorno é o valor do saldo da entidade especificada, apresentado no relatório de maneira independente do intervalo de entidades informado da linha da entidade visão/gerencial.

 A expressão ‘ENTIDADE =’utiliza a função padrão GETSLDENT() de uma forma mais simples e completa, pois atualiza todos os valores de saldos referentes a entidade gerencial especificada.

**Observação**

A entidade gerencial informada na expressão **ENTIDADE=** deve pertencer a mesma visão gerencial que contém a entidade gerencial analítica que utilizou esta expressão

A expressão **ENTIDADE=** atualiza todos os saldos utilizados pelo processamento da visão gerencial, inclusive o saldo anterior, sendo a sintaxe adequada para relatórios demonstrativos como o DFC – Demonstrativo de Fluxo de Caixa, pois o mesmo exige a impressão da coluna de saldos anteriores.

**5- Expressão “VISAO=”**

* **Sintaxe**: VISAO=Código\_da\_visão

Com o conteúdo **VISAO =**, o retorno é o valor do saldo da entidade definida com **Resultado da Visão** especificada, apresentado no relatório de maneira independente do intervalo de entidades informado da linha da entidade visão/gerencial.

A expressão ‘VISAO =’ utiliza a função padrão GETSLDVIS() de uma forma mais simples e completa, pois atualiza todos os valores de saldos referentes a entidade gerencial especificada.

**Observação**

A expressão **VISAO=** atualiza todos os saldos utilizados pelo processamento da visão gerencial, inclusive o saldo anterior, sendo a sintaxe adeaquada para relatórios demonstrativos como o DFC – Demonstrativo de Fluxo de Caixa, pois o mesmo exige a impressão da coluna de saldos anteriores.

**6-Expressão “VARIACAO=”**

* **Sintaxe**: VARIACAO=Código\_da\_entidade

Com o conteúdo 'VARIACAO =’, o retorno é o valor da variação entre o saldo anterior e o saldo atual da entidade especificada, apresentado no relatório de maneira independente do intervalo de entidades informado da linha da entidade visão/gerencial.

A expressão ‘VARIACAO =’ utiliza a função padrão GETVARENT() de uma forma mais simples e completa, pois atualiza todos os valores de saldos referentes a entidade gerencial especificada.

**Expressão “MOVIMENTO=”**

* **Sintaxe**: MOVIMENTO= CONTAB, CCUSTOB, ITEMCTBB,CLVLB, CONTAP, CCUSTOP, ITEMCTBP, CLVLP, ORIGEM

Com o conteúdo ‘MOVIMENTO =’, o retorno é o total do movimento das entidades definidas como bases (CONTAB, CCUSTOB, ITEMB e CLVB), sejam elas encontradas em conjunto a débito ou a crédito, com a opção de restringir as combinações com as entidades definidas como contra-partidas (CONTAP, CCUSTOP, ITEMCTBP, CLVLP, ORIGEM)

O parâmetro ORIGEM está relacionado ao campo CT2\_ORIGEM o qual pode conter uma informação definida pelo usuário, e também ser aproveitada para filtro dos movimentos a serem considerados na composição do saldo.

**Importante**:

A sintaxe movimento pode ser utilizada apenas com parte dos parâmetros definidos, como por exemplo:

MOVIMENTO=CONTA

Resultado: retorna todos os movimentos em que a conta especificada esteja a débito ou a crédito

MOVIMENTO=CONTA01,,,,CONTA02

Resultado: retorna todos os movimentos em que a CONTA01 tenha como contra-partida a CONTA02, independentemente de estarem a débito ou a crédito.

**Observação**

A utilização da SINTAXE “MOVIMENTO=” informando as entidades de contra-partida automaticamente elimina da seleção os movimentos tipo partida simples.

Se forem intercalados parâmetros da SINTAXE “MOVIMENTO=”, como demonstrado no exemplo “2. MOVIMENTO=CONTA01,,,,CONTA02, devem ser respeitadas as virgulas que indicam os parâmetros que não foram considerados

**Importante:** Ao preencher as entidades (Conta, Centro de Custo, Item Contábil e Classe Valor), não deve estar entre aspas(").

**Exemplo:**

*(Errado): MOVIMENTO="3.01.01",,,,"4.01.01"*

***(Certo): MOVIMENTO=3.01.01,,,,4.01.01***

**7-Expressão “FATOR=”**

* **Sintaxe**: FATOR=FUNCAO()

Com o conteúdo “FATOR=”, o retorno da função especificada serve como uma base ou fator de multiplicação a ser aplicado sobre os saldos originais, ou seja, o saldo correspondente ao intervalo de entidades definida na linha da entidade/visão gerencial multiplicado pelo retorno da função especificada (se o retorno for zero o saldo por conseqüência passa a ser zero no relatório).

**Observação**

O retorno da expressão “FATOR=” atualizará apenas o saldo atual da entidade gerencial analítica, e é repetido para a coluna de saldo anterior, se for parametrizada para exibição em função do processamento do relatório ou consulta.

A sintaxe **FATOR=**tem a mesma funcionalidade da sintaxe **ROTINA=** e seu objetivo é substituir o uso desta segunda, pois a mesma causava a impressão aos usuários de que o retorno seria o valor definido pela rotina, e não o fator de cálculo.

**8-Expressão “FTENTIDADE=”**

* **Sintaxe**: FTENTIDADE=Código\_da\_entidade,fator

Com o conteúdo ‘FTENTIDADE =’, o retorno é o valor do saldo da entidade especificada multiplicado pelo fator informado como segundo parâmetro, apresentado no relatório de maneira independente do intervalo de entidades informado da linha da entidade visão/gerencial.

A expressão ‘FTENTIDADE =’utiliza a função padrão GETSLDENT() de uma forma mais simples e completa, pois atualiza todos os valores de saldos referentes a entidade gerencial especificada, e combina a aplicação da função ‘FATOR=’ facilitando a demonstração de resultados que dependeriam da montagem de uma função específica utilizando este recurso.

**Observação**

A entidade gerencial informada na expressão “FTENTIDADE=” deve pertencer a mesma visão gerencial que contém a entidade gerencial analítica que utilizou esta expressão

O fator informado como segundo parâmetro deve ter o ponto decimal definido com “.” (ponto) e não com “,” virgula.

A expressão “FTENTIDADE=” atualiza todos os saldos utilizados pelo processamento da visão gerencial, inclusive o saldo anterior, sendo a sintaxe adequada para relatórios demonstrativos como o DFC – Demonstrativo de Fluxo de Caixa, pois o mesmo exige a impressão da coluna de saldos anteriores.

Saiba mais

* [Visão Gerencial - Expressões especiais](http://tdn.totvs.com/pages/releaseview.action?pageId=6068417)
* [Visão Gerencial - Uso de fórmulas](http://tdn.totvs.com/pages/releaseview.action?pageId=6068421)
* [Fórmula SALDO](http://tdn.totvs.com/pages/releaseview.action?pageId=147817088)
* [Campos\_e\_exemplos\_para\_criação\_de\_Estrutura](http://tdn.totvs.com.br/pages/releaseview.action?pageId=235569753)
