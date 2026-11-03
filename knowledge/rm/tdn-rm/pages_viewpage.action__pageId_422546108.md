---
content_hash: a86a1131956c2ed808bd95083aab0746b9bf34330d44bf97f51fbbe48f1bdbff
fetched_at: '2026-06-29T00:09:23.719420+00:00'
page_id: '422546108'
product: rm
source: tdn-rm
title: Gerar Crédito - Operações Interestaduais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546108
version: 4
---

Este processo estará visível somente para filiais do estado de Goiás, pois o critério apurado por essa opção se fere ao estado de Goias, conforme art. 45 e 46 do anexo 8 VIII do Regime do ICMS decreto 4582-GO. Executável somente para o tributos do tipo ICMS.

* **Informações do Cálculo**

O sistema irá selecionar todos os itens dos Lançamentos de Saída da coligada e filial com status = Normal com UF diferente da filial corrente, dentro do período de apuração informado na tela de parâmetros do processo.  
 Para cada Item, o processo irá identificar o valor do crédito da última entrada do produto dentro do período de geração nas seguintes condições:  
 Lançamentos de mesmo coligada, filial que estejam associados a uma Natureza de Operação cujo tipo de ICMS é Outros e com retenção de ICMS ST. UF do Lançamento diferente da Filial corrente e itens com valor de ICMS ST maior que zero.   
 O valor do crédito será o resultado da divisão da soma dos campos  Valor do ICMS com o Valor do ICMS ST do item de entrada pela sua quantidade. O valor resultante deste cálculo é multiplicado pela quantidade de saída.  
 Será criado um lançamento de Outros Débitos e subtipo Não se aplica com a soma do cálculo de todos os itens que gerarem valor no processo no período selecionado para a execução do processo para o tributo ICMS.
