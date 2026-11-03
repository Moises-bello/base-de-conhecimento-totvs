---
content_hash: 2bd9c8f714270823dc105a2763a4e4e3d1e2fc8ab20d0195e3dad8e1cae9a0f0
fetched_at: '2026-06-29T00:10:47.957729+00:00'
page_id: '56132760'
product: rm
source: tdn-rm
title: Erro ao Regerar saldos e custos – “Arithmetic overflow error converting numeric
  to data type numeric”
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=56132760
version: 4
---

| Produto | RM |
| --- | --- |
| Versões | 11.20 a 1182 |
|  |  |
| Sintoma | Este Documento tem por finalidade auxiliar na correção do erro no processo “Regerar Saldos e Custos”, onde a mensagem apresentada é:  “Não foram regerados os dados do produto 01.01 – Mensagem original: Arithmetic overflow error converting numeric to data type numeric.” |
|  |  |
| Causa | Algum campo da tabela TRELSLD (CUSTO MÉDIO ou TOTAL SALDO) está com o numero de dígitos maior que a quantidade máxima que o campo suporta. Sendo que no momento da execução do processo o sistema tenta realizar o INSERT/UPDATE neste campo, que tem tamanho máximo de 15 casas, contando com o sinal – (negativo) separador de casas decimais (.) e as casas decimais, o erro será apresentado.  Abaixo veja o exemplo de uma ficha física-financeira emitida após o erro da regeração. Na ficha o campo com o erro não será apresentado,  pois o mesmo sequer pode ser incluído no banco (visto que este é o problema a ser corrigido)    Porque este erro ocorre?  Vejamos os motivos mais comuns:  \* Alteração na parametrização do(s) tipo(s) de movimento(s);  \* Alteração na fórmula do Valor financeiro dos movimentos de entrada;  \* Falta de movimentação de entrada para abastecer o estoque, deixando-o negativo sempre ou quase sempre;  \* Entrada/Saída de movimentos com data retroativa;  \* Cancelamento/Exclusão de movimentos com data retroativa;  \* Etc. |
| Solução | Será preciso uma análise cautelosa da situação, para avaliar onde está ocorrendo a falha da parametrização/processo, e a partir deste ponto gerar os acertos que podem ser:    \* Alterar/Corrigir a parametrização do tipo de movimento que está ou não está afetando o estoque indevidamente.  Ex.: Movimento 2.2.02 está afetando o estoque, porém não deveria afetar. Logo, basta acessar os parâmetros deste tipo de movimento e tirar a parametrização que está afetando o estoque    \* Alterar a fórmula do valor financeiro do(s) movimento(s) de entrada, de modo que afetem o financeiro corretamente, não gerando discrepância entre os valores reais.  Ex.: Na imagem acima a fórmula do valor financeiro é a seguinte:  *SE  TABPRDLOC ('CUSTOMEDIO' , 'V') >0*  *ENTAO  KQT\*KPU \*TABPRDLOC ('CUSTOMEDIO' , 'V')*  *SENAO KQT\*KPU\*7.5*  *FIMSE*  O que está incorreto, pois o valor do custo médio do produto irá aumentar gradativamente, gerando o erro.  Neste caso alterando a fórmula pelo conteúdo abaixo:  *KQT\*KPU*  O erro não foi mais apresentado, apesar do saldo negativo ainda existir.      ***\*\*Lembrando que a fórmula pode ou não está errada, conforme todas as outras opções que podem estar ocorrendo ou não.***  \* Incluir um movimento de acerto de estoque com data retroativa, para compensar o saldo negativo que está sendo gerado. (Falha de processo que mais ocorre e faz com que este erro seja apresentado)    Ex: A partir da última imagem, foi identificado que no dia 01/05/2011 foi dada uma saída de 11.350,00 itens, que deixou o estoque negativo em 2.981,00 unidades. Para a correção, geramos uma movimentação de entrada 30/04/2011 com quantidade 2.981,00.    Após regerar saldos e custos foi identificado que no dia 02/10/2011 foi dada uma saída de 55.137,00 itens, que deixou o estoque negativo em 52.871,00 unidades. Para a correção, geramos uma movimentação de entrada 01/10/2011 com quantidade 52.871,00.    Após regerar saldos e custos foi identificado que no dia 02/05/2013 foram dadas 3 saídas com o total de  98.708,00 itens, que deixou o estoque negativo em 90.832,00 unidades. Para a correção, geramos uma movimentação de entrada 01/10/2011 com quantidade 90.833,00.    Assim a ficha não ficará mais incorreta, e a regeração de saldos e custos não irá gerar o erro. |
| Observações |
