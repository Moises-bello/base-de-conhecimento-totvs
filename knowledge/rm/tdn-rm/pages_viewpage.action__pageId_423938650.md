---
content_hash: 4d260fd8e8ec4d1c04057fdc279e9a1d9b55b9278b1661cb8874c66a76cdb7de
fetched_at: '2026-06-29T00:09:28.072807+00:00'
page_id: '423938650'
product: rm
source: tdn-rm
title: Atualização do Campo Complementar SPED FCONT
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938650
version: 6
---

Para a geração do SPED FCONT é necessário identificar e classificar os lançamentos de expurgo e os lançamentos de ajustes (lançamentos fiscais). Antes, porém, é preciso criar o campo complementar de lançamento SPEDFCONT.  
   
Para executar este processo, selecione os lançamentos/partidas, em seguida classifique-os respectivamente com:  
   
**X** - Informar somente os lançamentos da escrituração comercial que devem ser desconsiderados para apuração do resultado em conformidade com a Lei no 6.404/76, vigente em 31.12.2007. Os lançamentos devem conter as mesmas informações da escrituração contábil, ou seja, inclusive o indicador de débito e crédito do registro I250. O FCONT se encarregará de fazer o expurgo.  
   
**F** - Informar somente os lançamentos contábeis não efetuados na escrituração comercial que devem ser considerados para apuração do resultado em conformidade com a Lei no 6.404/76, vigente em 31.12.2007.  
   
**TR** - Lançamento de transferência da diferença entre saldos fiscais e societários no caso de implantação de um novo plano de contas. Neste caso considera-se que o saldo societário da conta contábil do plano de contas extinto foi transferido por meio de um lançamento contábil para a nova(s) conta(s) contábil(eis). Este lançamento tipo TR refere-se apenas a transferência da parcela do saldo fiscal que não foi transferida pelo lançamento contábil, ou seja, transfere-se apenas a diferença entre o saldo fiscal e societário. Para efetuar esta transferência deve ser utilizado apenas um lançamento por conta contábil / centro de custo / conta referencial para cada grupo conta contábil / centro de custo extinto.  
   
**TF** - Transferência de saldo fiscal para uma conta referencial devido à extinção da conta referencial de origem.  
   
**TS** - Transferência de saldo societário para uma conta referencial devido à extinção da conta referencial de origem.  
   
**EF** - Lançamento de encerramento fiscal para ajuste do saldo fiscal sobre o saldo societário.  
   
**IF** - Lançamento para alteração do saldo inicial fiscal, quando a forma de tributação do período anterior não for por Lucro Real.  
   
**IS** - Lançamento para alteração do saldo inicial societário, quando a forma de tributação do período anterior não for por Lucro Real.

Para facilitar o entendimento, siga os seguintes passos:

**1° Passo:**  
Acessar o menu "*Lançamentos | Manutenção de Lançamentos*"

**2° Passo:**   
Filtrar os lançamentos desejados que serão enviados para o arquivo do SPED FCONT

**3º Passo:**   
Selecionar os lançamentos que terão o campo complementar classificado como por exemplo "X" - expurgo

**4º Passo:**  
Acessar o menu "*Processos | Atualização do Campo Complementar SPEDFCONT*"

**5° Passo:**  
Informar que os lançamentos terão o campo complementar atualizados com a informação "X"

**6° Passo:**   
Executar o processo

**Observação** Repita os passos anteriores para classificar também os lançamentos de ajustes informando a sua respectiva classificação.
