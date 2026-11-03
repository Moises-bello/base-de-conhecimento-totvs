---
content_hash: 8ceee550b539625719c2787465b68f98d8e71910b92c451e77c8ffee22f4cccf
fetched_at: '2026-06-29T00:05:58.405811+00:00'
page_id: '185760122'
product: rm
source: tdn-rm
title: COMO FAZER - Atualização Saldo FGTS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=185760122
version: 13
---

**PROCESSO DE ATUALIZAÇÃO DO SALDO DO FGTS**

**Release:****Versão: 11.8X ou superiores**

1. Acessar o menu Administração Pessoal | Cadastros | Moedas e criar uma moeda com as especificações abaixo:

2. Acessar o caminho Administração Pessoal | Cadastros | Cotações. E mensalmente, deverá cadastrar os fatores de atualização do saldo de FGTS. A cotação deverá ser criada observando as especificações abaixo:

A data do índice deve ser sempre o primeiro dia da competência anterior à atual. Atualmente, a Caixa Econômica Federal. libera os índices com a data do dia 21, mas na Folha de Pagamento o cadastro deve ser feito com a data do dia 01.

**Exemplo:**

* + - Caixa Econômica Federal.: 21/01/2025
    - Folha de Pagamento:  01/12/2024

3. Após cadastrar a Moeda e a Cotação, verifique se os campos abaixo estão preenchidos corretamente. Se já houver valores, eles devem corresponder ao valor calculado pela Caixa Econômica Federal. Para confirmar os dados, entre em contato com a Caixa Econômica Federal. Econômica Federal e solicite o último extrato que contenha o saldo de FGTS do funcionário, datado do dia 10 da competência.

* **Última atualização de saldo FGTS**
* **Saldo FGTS na CEF**
* **Saldo FGTS Fins Rescisório**

**ATENÇÃO:**  
Para que o sistema calcule os valores a partir da data de admissão, configure o campo "**Última atualização de saldo FGTS**" com a data de admissão e mantenha os campos "**Saldo FGTS na CEF**" e "**Saldo FGTS Fins Rescisório**" zerados. Para que este calculo traga valores corretos o funcionário a ser calculado não pode ter dados na ficha financeira complementar.

4. Com a base parametrizada, a rotina poderá ser processada através do menu Administração Pessoal | Alteração Cadastrais | Atualização do Saldo FGTS.

Para entender melhor a regra, segue abaixo um exemplo de como o sistema efetua o cálculo de atualização.

**Exemplo:**

* + - Mês de competência: 01/2025.
    - Última atualização de saldo FGTS: 10/12/2024
    - Saldo FGTS na CEF: R$2.658,78
    - Saldo FGTS Fins Rescisório: R$2.646,19

Memória do cálculo:

Após atualização do Saldo de FGTS do funcionário com o índice do dia 10/01/2025 :

* + - Última atualização de saldo FGTS: 10/01/2025
    - Saldo FGTS na CEF: R$2.953,24
    - Saldo FGTS Fins Rescisório: R$2.940,65

**IMPORTANTE:**

O saldo do FGTS na folha de pagamento pode apresentar divergências em relação ao saldo do FGTS na Caixa Econômica Federal., pois, periodicamente, a Caixa Econômica Federal. distribui o item "**C****RED DIST RESULTADO ANO BASE**".
