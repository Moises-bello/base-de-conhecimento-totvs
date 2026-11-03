---
content_hash: b84fefc63495534963541ca56e8819b9d459210128c1745a652e08f5e483ea35
fetched_at: '2026-06-29T00:10:44.522884+00:00'
page_id: '552598669'
product: rm
source: tdn-rm
title: Geração de encargos com dependência de valores entre os encargos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=552598669
version: 8
---

## **01. VISÃO GERAL**

A partir do release 12.1.27 foi evoluído o módulo de Geração de Encargos, possibilitando a geração dos encargos do tipo' A - Valor calculado através de fórmula' com dependência entre eles, ou seja, gerar os encargos do tipo' A - Valor calculado através de fórmula', considerando o valor de um outro encargo do tipo' A - Valor calculado através de fórmula', para compor a base de cálculo de outro encargo do tipo' A - Valor calculado através de fórmula' em tempo de execução.

Foi criado o campo "Ordem de Cálculo" para encargos do tipo "A - Valor calculado através de fórmula":

Foi criada a variável de fórmula **VALENCARGOM** para recuperar o valor do encargo calculado anteriormente em memória:

**Observação:** Para calcular um encargo do tipo A - Valor calculado através de fórmula, que utilize o valor de outro encargo do tipo A - Valor calculado através de fórmula, deverá definir a 'Ordem de Cálculo' do primeiro encargo, menor que a 'Ordem do cálculo' do segundo encargo, que será utilizado no cálculo do primeiro encargo e utilizar a variável **VALENCARGOM** para recuperar o valor calculado.

**02. EXEMPLO DE UTILIZAÇÃO**

**1º Passo:** Criar os encargos que deseja que sejam calculados com dependência:

Encargo A: Recebe o valor da variável RC e a fórmula de Valor informada retornará o valor do salário do funcionário para o Encargo A.

**Observação:** Os demais campos, pastas e parâmetros dos encargos não sofreram alterações e continuam com as mesmas formas de parametrização e funcionalidades.

Encargo B: Vai calcular 20% sobre o Encargo A. Será necessário informar na Fórmula de Valor a variável **VALENCARGOM**para buscar o valor do Encargo A em memória e calcular o valor do Encargo B.

**Observação:** Os demais campos, pastas e parâmetros dos encargos não sofreram alterações e continuam com as mesmas formas de parametrização e funcionalidades.

Veja abaixo o exemplo da Fórmula de Valor criada e informada no Encargo B. A fórmula irá pegar o valor do Encargo 011, multiplicar por 20 e dividir por cem, ou seja, calcular 20% sobre o valor do encargo A (011);

**2º Passo:**Definir  a 'Ordem de Cálculo' dos encargos em questão. No nosso caso, deverá ser calculado primeiro o Encargo A (011) e em seguida o Encargo B (012), pois o Encargo B (012) utiliza o valor do Encargo A (011) para compor seu cálculo, sendo assim ficará com a seguinte 'Ordem de Cálculo':

**Observação:**O 'Encargo A (011)' será calculado primeiro, então a Ordem de Cálculo,  será maior que a Ordem de Cálculo do 'Encargo B (012)'.

## **03. DEMAIS INFORMAÇÕES**

ATENÇÂO

O campo 'Ordem de Cálculo' estará disponível somente para encargos do tipo 'A - Valor calculado através de fórmula'.

O encargo que deverá ser calculado com prioridade sempre deverá ter a maior ordem de cálculo.

Os demais campos, pastas e parâmetros dos encargos não sofreram alterações e continuam com as mesmas formas de parametrização e funcionalidades.

Demais Informações Orçamento

Para mais informações sobre os Encargos, consulte:

* [DT - Encargos - Campo 'Ordem de Cálculo'](https://tdn.totvs.com.br/pages/viewpage.action?pageId=552594888)
* [DT- Fórmula VALENCARGOM](https://tdn.totvs.com.br/pages/viewpage.action?pageId=552598510)
* [Encargos - Folha de Pagamento](https://tdn.totvs.com.br/display/LRM/Encargos+-+Folha+de+Pagamento)
* [Geração de Encargos](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718264)
* [Fórmulas / Funções V](https://tdn.totvs.com.br/pages/viewpage.action?pageId=552598291)
