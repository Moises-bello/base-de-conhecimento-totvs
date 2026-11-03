---
content_hash: d8ce38fab7cf66a4eeb0a4b7acf57482eb3b7e84a96c4e0a9d27f9a0bda07976
fetched_at: '2026-06-29T00:08:55.963765+00:00'
page_id: '351372555'
product: rm
source: tdn-rm
title: RMCTB00001_Não usar Valor Fixo nas Demonstrações Contábeis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=351372555
version: 6
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Contábil |
| **Versões:** | 12.1 |
| **Ocorrência:** | Opção de Valor Fixo nas Demonstrações Contábeis |
| **Ambiente:** |  |
| **Passo a passo:** | **Definição do Processo:**  A opção de Valor Fixo na ferramenta de Demonstração Contábil veio como mais um facilitador na criação das mais diversas estruturas de relatórios contábeis permitidas por este importante recurso.  No entanto para as Demonstrações que são geradas para a **Rotina Contábil ECD (Escrituração Contábil Digital)**, a opção Origem do Valor (Valor Fixo) **não poderá ser usada**.  Isso ocorre porque nas Demonstração Contábeis (DLPA e DMPL) o PGE (Programa Gerador de Escrituração) leva em consideração para sua validação o código de aglutinação,  sendo necessário neste caso informar a conta contábil para os devidos fins.  Além desta validação, temos ainda outros registros que são confrontados com as Demonstrações como é o caso do registro I155.  Neste caso, deverá ser usada outra opção para composição dos relatórios.    Abaixo segue um exemplo (DLPA) que explica as validações/conferências que são feitas pelo validador do SPED Contábil:    **Disponível em:** Menu Escrituração Contábil | Demonstração Contábil | Estrutura (Layout) | Edite a estrutura DLPA | Aba Configuração do Layout.  A conta contábil que é vinculada ao saldo inicial da DLPA será gerada no registro J210 e o seu código de aglutinação será gerada para a respectiva conta.      Ex: Em nosso exemplo, segue abaixo a conta que vinculamos no Saldo Inicial da DLPA:    Esta conta que será gerada no registro J210, veja:    O validador do SPED Contábil irá verificar se o Saldo Inicial do registro J210 mais as movimentações dos registros J215 (movimentações à débito e a crédito) coincide com o Saldo Final do registro J210.  Em nosso exemplo, o Saldo Inicial da conta contábil de Lucros/Prejuízos Acumulados é zero, mais as movimentações do registro J215 chega-se em 1425,00.  Este valor é idêntico ao saldo final do registro J210, portanto neste exemplo a DLPA está correta.  Além desta validação, repare que na linha **J210** existe o código de aglutinação “**DLPA\_1”.** Este código também será validado pelo PGE (Programa Gerador de Escrituração) para verificar se a conta vinculada ao mesmo, possui o Saldo Inicial de **0,00** e saldo final de **1425,00**.  Ex: Se pesquisarmos em nosso arquivo exemplo este código de Aglutinação se encontra na linha 168.    Acima do código de aglutinação temos o registro de plano de contas **“I050”.** Neste registro temos a conta contábil de **Lucros/Prejuízos Acumulados**.  Portanto o código de aglutinação **“DLPA\_1”** está vinculado a esta conta.  O validador do SPED Contábil irá confrontar se o saldo desta conta no registro I155 coincide com o valor apresentado no registro J210.    Em nosso exemplo, a conta contábil teve saldo inicial zerado, então a mesma possui movimentação somente em dezembro/2015, por este motivo foi gerado somente o registro do mês 12/2015.  Repare que o saldo final da conta é de **1425,00**, portanto neste exemplo a validação do PGE (Programa Gerador de Escrituração) para os saldos periódicos ocorreria com sucesso.    Devido a estas validações que demonstramos e as demais existentes no PGE do Sped Contábil, a opção de **“Valor Fixo”** e **“Expressão”** foi restringida no uso das demonstrações que são enviadas para o SPED Contábil. |
| **Observações:** |  |
