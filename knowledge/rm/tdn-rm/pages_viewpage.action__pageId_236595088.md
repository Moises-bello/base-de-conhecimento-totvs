---
content_hash: 63e01943803ccfb6b7e2a757d7c312efd2c02918f9abb28145d8fedd75fd2f6d
fetched_at: '2026-06-29T00:08:06.900269+00:00'
page_id: '236595088'
product: rm
source: tdn-rm
title: 'RMCTB00003_Demonstração Contábil: Opção de Valor Fixo e suas restrições na
  DLPA/DMPL/DRE/BP para a ECD'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=236595088
version: 5
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Contábil |
| **Versões:** | 12.1.18 |
| **Ocorrência:** | Demonstração Contábil: Opção de Valor Fixo e suas restrições na DLPA/DMPL/DRE/BP para a ECD |
| **Ambiente:** |  |
| **Passo a passo:** | **Definição do Processo:**  A opção de Valor Fixo na ferramenta de Demonstração Contábil veio como mais um facilitador na criação das mais diversas estruturas de relatórios contábeis permitidas por este importante recurso.  No entanto para as Demonstrações que são geradas para a Rotina Contábil ECD (Escrituração Contábil Digital), a opção Origem valor (Valor Fixo) não poderá ser usada. Isso ocorre porque nas Demonstração Contábeis (DLPA e DMPL) o PVA da Receita Federal leva em consideração para sua validação o código de aglutinação, sendo necessário neste caso informar a conta contábil para os devidos fins.  Além desta validação, temos ainda outros registros que são confrontados com as Demonstrações como é o caso do registro I155.  Abaixo segue um exemplo que explica as validações/conferências que são feitas pelo validador do SPED Contábil.  **Exemplo de configuração da DPLA**    A conta contábil que é vinculada ao saldo inicial da DLPA será gerada no registro J210 e o seu código de aglutinação será gerada para a respectiva conta.  Ex: Em nosso exemplo, segue abaixo a conta que vinculamos no saldo inicial da DLPA    Será esta conta que será gerada no registro J210, veja:    O validador do SPED Contábil irá verificar se o saldo inicial do registro J210 mais as movimentações dos registros J215 (movimentações à débito e a crédito) coincide com o saldo final do registro J210.  Em nosso exemplo, o saldo inicial da conta contábil de Lucros/Prejuízos Acumulados é zero, mais as movimentações do registro J215 chega-se em 1425,00. Este valor é idêntico ao saldo final do registro J210, portanto neste exemplo a DLPA está correta.  Além desta validação, repare que na linha **J210** existe o código de aglutinação “**DLPA\_1”.** Este código também será validado pelo PVA para verificar se a conta vinculada ao mesmo possui o saldo inicial de **0,00** e saldo final de **1425,00**.  Ex: Se pesquisarmos em nosso arquivo exemplo este código de Aglutinação se encontra na linha 168.    Acima do código de aglutinação temos o registro de plano de contas **“I050”.** Neste registro temos a conta contábil de **Lucros/Prejuízos Acumulados**. Portanto o código de aglutinação **“DLPA\_1”** está vinculado a esta conta.  O validador do SPED Contábil irá confrontar se o saldo desta conta no registro I155 coincide com o valor apresentado no registro J210.    Em nosso exemplo, a conta contábil teve saldo inicial zerado, então a mesma possui movimentação somente em dezembro/2015, por este motivo foi gerado somente o registro do mês 12/2015.  Repare que o saldo final da conta é de **1425,00**, portanto neste exemplo a validação do PVA para os saldos periódicos ocorreria com sucesso.  Devido a estas validações que demonstramos e as demais existentes no PVA do Sped Contábil, a opção de **“Valor Fixo”** e **“Expressão”** foi restringida no uso da demonstrações que são enviadas para o SPED Contábil |
| **Observações:** |  |
