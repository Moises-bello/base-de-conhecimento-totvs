---
content_hash: a4548df5b5344bc1439a8801f65b631c3822b021bcf55e88b35e62731f2fd0d6
fetched_at: '2026-06-29T00:10:10.443794+00:00'
page_id: '452719839'
product: rm
source: tdn-rm
title: Alteração Global de Códigos Fixos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719839
version: 2
---

Neste módulo será possível alterar os códigos fixos (isto é, eventos que precisam ser lançados na folha com regularidade, como cesta básica e ticket refeição, por exemplo), para um ou mais funcionários simultaneamente.  
    
 **Incluindo um código fixo para funcionários**  
 Para incluir códigos fixos para funcionários, o usuário deverá acessar: Rotinas | Alterações Globais de Funcionários | Códigos Fixos (.Net), selecionar o funcionário desejado, definir o evento que será um código fixo, marcar o campo: "Incluisão" e avançar etapa.   
 Na próxima tela o usuário deverá informar o valor, o tipo e o número de vezes que este código fixo será lançado (tais informações poderão ser feitas através dos campos "Valor" ou "Fórmula").   
 Após incluir todas as informações basta o usuário avançar etapa para execução do processo.  
    
    
 **Adicionando valor a um código fixo já existente para funcionários**  
 Para adicionar valor a um código fixo já existente para funcionários, o usuário deverá acessar: Rotinas | Alterações Globais de Funcionários | Códigos Fixos (.Net), selecionar o funcionário desejado, selecionar o código fixo que terá seu valor alterado, marcar o campo: "Soma" e avançar etapa.   
 Na próxima tela o usuário deverá informar o valor e o número de vezes deste código fixo (tais informações poderão ser feitas através dos campos "Valor" ou "Fórmula"). Nesta ação o usuário tem a opção de informar um valor de arredondamento, caso não queira que o valor do código fixo seja "quebrado"(ou seja, caso não queira que o valor do código fixo tenha centavos). Após incluir todas as informações basta o usuário avançar etapa para execução do processo.  
    
    
 **Exemplo da funcionalidade do campo: "Arredondamento"**  
 Caso um funcionário receba uma comissão de R$10,00 com arredondamento de R$ 1,00 e tenha um aumento de 15%, assim, o valor que deveria ser lançado seria R$ 11,50, porém o arredondamento não permite este valor quebrado, por isso o funcionário passa a receber R$12,00 .  
 O arredondamento só é aplicado no campo "Valor do Código Fixo" nas seguintes situações:

**1)** Comportamento é para o processo de SOMA.

**2)** O evento do código fixo é do tipo "Valor" ou "Fórmula".  
    
 **Substituindo o valor de um código fixo já existente para funcionários**  
 Para substituir o valor de um código fixo já existente para funcionários, o usuário deverá acessar: Rotinas | Alterações Globais de Funcionários | Códigos Fixos (.Net), selecionar o funcionário desejado, selecionar o código fixo que terá seu valor substituído, marcar o campo: "Substituição" e avançar etapa.   
 Na próxima tela o usuário deverá informar o valor, o tipo e o número de vezes deste código fixo (tais informações poderão ser feitas através dos campos "Valor" ou "Fórmula").   
 Após incluir todas as informações basta o usuário avançar etapa para execução do processo.  
    
 **Excluindo um código fixo dos funcionários**  
 Para excluir o valor de um código fixo existente para funcionários, o usuário deverá acessar: Rotinas | Alterações Globais de Funcionários | Códigos Fixos (.Net), selecionar o funcionário desejado, selecionar o código fixo que será excluído, marcar o campo: "Exclusão" e avançar etapa para execução do processo.  
    
 **Exemplo de fórmula para alteração de valor**  
 CF('0009') \* 1.02

(A função CF retorna valor de código fixo. Com esta fórmula, esse valor será multiplicado por 1.02, ou seja, sofrerá um aumento de 2%).  
    
 **Exemplo de fórmula para alteração de número de vezes que o código fixo será lançado**

se  NCFIX ('0002') <> 999

então 1

senao 0

fimse

(Observe que, na fórmula, foi acrescentada a condição de o número de vezes ser diferente de '999' porque esse valor, no caso, representa infinito.O sistema irá passar o número de vezes para "1" ou somará o número "1" ao número de vezes conforme a opção de comportamento: substituir ou adicionar).
