---
content_hash: ca83fbc433ae303775fe2ab3cc5ac2a1e8e196f7f3d266cb414c1e7e1421f4b6
fetched_at: '2026-06-29T00:10:02.546820+00:00'
page_id: '452718953'
product: rm
source: tdn-rm
title: Atualização de Saldo de FGTS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718953
version: 13
---

O módulo de Atualização de Saldo de FGTS é a funcionalidade onde o usuário poderá atualizar os saldos de FGTS depositados no banco, aplicando os índices de correção monetária disponibilizados pela Caixa Econômica Federal. Esse saldo poderá ser utilizado no cálculo das rescisões dos funcionários com demissão sem justa causa, na emissão da GRFC, e nas provisões contábeis.

Antes de realizar a operação, alguns itens devem observados:

1. No cadastro do(s) funcionário(s) envolvido(s) no processo, o último saldo conhecido, depositado na Caixa Econômica Federal, deverá ter sido informado.
2. No cadastro de Moedas e Índices deverá existir uma moeda com símbolo "FGTS".
3. No cadastro de cotações deverão conter todos os índices de atualização disponibilizados pela CEF (pelo menos desde a data de admissão do(s) funcionário(s) que está(ão) sendo demitido(s)).

A fórmula utilizada no cálculo da atualização do saldo de FGTS segue o roteiro abaixo:

Se tivermos:  
**S - Saldo de FGTS do Mês Anterior; D - Depósito de FGTS da Última Competência; F - Fator de Atualização de FGTS;**  
Então:  
Saldo de FGTS Atualizado = **S + (S x F) + D**

**OBSERVAÇÃO:** O sistema sempre processa a atualização até a competência anterior. Isso porque precisa que todos os dados estejam cadastrados no sistema para que o cálculo fique correto.

**EXEMPLO:**

* Mês de competência: **08/2010**
* Última atualização de saldo FGTS do funcionário: **10/07/2010**
* Valor do último saldo atualizado: **R$1.000.00**
* Valor de FGTS depositado no mês 07/2010: **R$****40.00**
* Fator de Atualização de FGTS em 01/07/2010: **0.01500**

Após atualização do Saldo de FGTS o valor atualizado será **R$****1.055,00**.

Memória do cálculo:

* + 10/07/2010 = R$1.000,00
  + 10/07/2010 = R$15,00 (índice de correção: 0.015)
  + 30/07/2010 = R$40,00 (deposito do mês 07/2000)
  + 10/08/2010 = R$1.055,00 (Total corrigido até esta data)

Aplicando a fórmula:

* + - S = R$1.000,00
    - D = R$40,00
    - F = 0,015000
    - R$1.000,00 + (R$1.000,00 x 0,015000) + R$40,00 = R$1.055,00.

Quando o parâmetro Utiliza Manutenção de FGTS está marcado, em Opções | Parâmetros | RM Labore | Outros Parâmetros | Parâmetros III, é possível incluir informações de resgate de saldo. Dessa forma o cálculo sobre uma pequena alteração, descrita abaixo:

Se tivermos: **S - Saldo de FGTS do Mês Anterior; D - Depósito de FGTS da Última Competência; F - Fator de Atualização de FGTS; R1** **- Resgate de Salgo de FGTS**feito antes do dia 10.

\* R2 - Resgate de Salgo de FGTS feito depois do dia 10;\*  
\*\* Verificar na legislação vigente em quais casos o resgate é permitido.\*

Então...

Saldo de FGTS Atualizado = **S + ((S - R1) x F) + D - R2**  
Dessa maneira calcula-se o saldo real de FGTS, ou seja, o saldo que ainda permanece depositado na CEF, e não o saldo que deverá ser considerado no cálculo rescisório. Para fins rescisórios o montante considerado para o cálculo da multa rescisória desconsidera os valores de resgate. Nesse caso o sistema utiliza o cálculo acima para a apuração da correção monetária do mês e a adiciona ao montante total de FGTS. Ao final, os dois valores (Saldo Real e Saldo p/ Fins Rescisórios) serão demonstrados no cadastro do funcionário.

**OBSERVAÇÃO**: Para um processo de atualização mais preciso é aconselhável a execução desse módulo todos os meses. Porém, isso não é uma necessidade. Caso a atualização não tenha sido executada nos últimos meses, será possível atualizar o saldo desde a data do último saldo conhecido, com a única desvantagem da necessidade de atualização retroativa das cotações.
