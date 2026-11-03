---
content_hash: bc6d5043cf9ddfd20680215f0ffdf8c4e1c08c097996ab2699e132a446ce2852
fetched_at: '2026-06-29T00:10:04.730477+00:00'
page_id: '452719241'
product: rm
source: tdn-rm
title: Fórmulas / Funções - B
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719241
version: 6
---

**Função B:**  
Executa tabela progressiva. O retorno é do tipo valor.  
B ('CÓD. DA TABELA', VALOR A APLICAR)  
   
**Exemplo:**   
Foi criada a seguinte tabela de cálculo, com código '0004';  
       Valor            Percentual  
       360                      1  
       1200                    2  
       2400                    3  
       9999                    4  
       Fórmula:  
        B - ('0004', RC)  
       A função RC retorna salário nominal. Vamos supor RC = R$ 5.000,00  
       Neste caso, a fórmula executaria a tabela da seguinte forma:  
       360 X 1% = 3,6;  
       (1200 - 360) X 2% = 16,80;  
       (2400 - 1200) X 3% = 36,00;  
       (5000 - 2400) X 4% = 104,00.  
        Retorno: 160,40

**Função BASECALCULO:**  
Retorna a base de cálculo da incidência no mês e ano especificados.  
Base (TIPOBASE, MES, ANO, PARAMGERAIS)

**Tipo Base:**

INSS: Considera mês/ano competência  
INSS13: Considera mês/ano competência  
IRRF: Considera mês/ano caixa  
IRRF13: Considera mês/ano caixa  
IRRFFERIAS: Considera mês/ano caixa  
FGTS: Considera mês/ano competência  
FGTS13: Considera mês/ano competência   
FGTSINDENIZADO: Considera mês/ano competência   
FGTS13INDENIZADO: Considera mês/ano competência

**MES e ANO:**  
Quando informado meses anteriores o sistema executa um SELECT nas bases gravadas no período da ficha financeira (PFPERFF).  
Quando informado mês atual, os valores do período atual são buscados da memória, e caso o parâmetro 'Somente Período Atual' seja FALSO, ou seja, considere todo o mês, é executado um SELECT nas bases gravadas no período da ficha financeira (PFPERFF), para buscar valores dos outros períodos do mês especificado.  
   
**PARAMGERAIS**  
1º. Caractere = Somente Período Atual  
Informe 'S' para que o sistema considere as bases apenas do período atual, caso contrário informe 'N'.  
   
**Atenção:**  
Este parâmetro é verificado somente para o mês e ano atual.  
   
2º. Caractere = Limita ao Teto  
Informe 'S' para que o sistema limite ao teto conforme tabela de cálculo, caso contrário informe 'N'.  
   
**Atenção:**  
Este parâmetro é verificado somente quando o 'Tipo Base' é igual INSS ou INSS13.  
   
**Exemplo:**  
O usuário necessita saber a base de 'INSS folha' do mês atual limitado ao teto.  
A fórmula é: BASECALCULO ('INSS', MES, ANO,' NS')

Dica

Veja exemplos do FGTS na FAQ - [Cálculo do FGTS Digital](https://tdn.totvs.com/pages/viewpage.action?pageId=839304283)

**Função BASEFGTS:**  
Retorna base de FGTS.O retorno é do tipo valor.

  BASEFGTS -> Irá retornar a soma dos FGTS Folha e FGTS Indenizado

Dica

Veja exemplos na FAQ - [Cálculo do FGTS Digital](https://tdn.totvs.com/pages/viewpage.action?pageId=839304283)

**Função BASEFGTSFF:**  
Retorna a base de FGTS de um ano e mês especificados.  
BASEFGTSFF (ANO, MÊS)

  BASEFGTSFF -> Irá retornar a soma dos FGTS Folha e FGTS Indenizado

**Exemplo:**  
BASEFGTSFF ((ANO, MÊS)  
BASEFGTSFF (2013, 04) retorna a base FGTS do movimento do funcionário no mês de abril de 2013.

Dica

Veja exemplos também na FAQ - [Cálculo do FGTS Digital](https://tdn.totvs.com/pages/viewpage.action?pageId=839304283)

   
**Função BASEINSS:**  
Retorna base de INSS do movimento atual. Retorna valor.  
   
**Observação:**  
Quando associar esta função a um evento, este evento deverá ter a maior prioridade para retornar o valor correto.  
   
**Função BASEINSSFF:**  
Retorna base de INSS de acordo com ano e mês específicos da Ficha Financeira.  
 Retorna Valor.  
 BASEINSSFF (ANO, MÊS)  
   
 **Observação:**  
O retorno das variáveis BASEINSS e BASEINSSFF é a base de INSS para cálculo da parte de segurado, portanto, este retorno será limitado ao teto cadastrado na tabela de INSS.  
   
**Função BASEINSS13FF:**  
Retorna base de INSS de acordo com ano e mês específicos da Ficha Financeira. Retorna valor.  
  BASEINSS13FF (ANO, MÊS)  
   
**Exemplo:**  
  BASEINSS13FF (2013, 12)  
  O resultado desta fórmula será o valor da base de INSS de décimo terceiro salário do funcionário no mês 12 do ano de 2013.  
   
**Função BASEIRRF:**  
Retorna base de IRRF referente ao mês anterior. Retorna valor.  
   
**Função BASEIRRFFF:**  
Retorna a base de IRRF de um ano e mês especificados.  
BASEIRRFFF (ANO, MÊS)  
   
**Exemplo:**  
BASEIRRFFF (2013, 06) retorna a base IRRF do caixa junho de 2013.  
   
**Função BASEFGTS13FF:**   
Retorna o valor da base de FGTS de décimo terceiro salário na ficha financeira.  
BASEFGTS13FF (ANO COMPETÊNCIA, MÊS COMPETÊNCIA)

  BASEFGTS13 ->Irá retornar a soma dos FGTS 13o e FGTS 13o Indenizado

**Exemplo:**  
BASEFGTS13FF (2013, 12)  
O resultado desta fórmula será o valor da base de FGTS de décimo terceiro salário do funcionário no mês 12 do ano de 2013

Dica

Veja exemplos também na FAQ - [Cálculo do FGTS Digital](https://tdn.totvs.com/pages/viewpage.action?pageId=839304283)

**Função BASEINSS13:**  
Retorna o valor da base de INSS 13º salário.  
   
**Função BASEFGTS13:**  
Retorna base de FGTS de 13º salário

  BASEFGTS13FF -> Irá retornar a soma dos FGTS 13o e FGTS 13o Indenizado

Dica

Veja exemplos na FAQ - [Cálculo do FGTS Digital](https://tdn.totvs.com/pages/viewpage.action?pageId=839304283)

**Função BINSSACTETO:**  
Retorna a base de INSS acima do teto do movimento atual. Se a base de INSS total sem considerar o teto estabelecido para base de INSS, for maior que o teto para a base de INSS, então esta variável retorna a o valor que excede o teto, senão retorna zero.  
   
**Exemplo:**  
 Base de INSS total de um funcionário = R$ 1500,00  
 Teto de INSS = R$ 1200,00  
 BINSSACTETO ==> R$ 1500,00 - R$ 1200,00 = R$ 300,00  
 Ou seja, BINSSACTETO vai retornar R$ 300,00  
   
 **Observações:**

Pela sintaxe, nenhuma dessas funções requer parâmetro. Basta escrever, por exemplo: BASEFGTS.  
-A função verifica os parâmetros "Calcula" e "Não calcula" da caixa INSS, subpasta FGTS/SEFIP/INSS, aba Registro do cadastro de funcionários.  
   
   
**Função BINSS13ACTETO:**  
Retorna a base de INSS 13º Salário acima do teto do movimento atual. Se a base de INSS 13º salário total for maior que o teto para a base de INSS (tabela de INSS), então esta variável retornará o valor que excede o teto, senão retorna zero.  
   
**Observação:**  
A função verifica os parâmetros "Calcula" e "Não calcula" da caixa INSS, pasta PARAMETROS no cadastro de funcionários.  
Caso deseje retornar o valor base de INSS 13 acima do teto no movimento do funcionário, utilize a variável **BINSS13ACTETOMOV**.Vale ressaltar que as duas variáveis só retornarão algum valor se no movimento tiver lançado o 13º salário para o funcionário.  
   
**Exemplo:**  
Base de INSS 13º Salário total de um funcionário = R$ 1500,00   
Teto de INSS = R$ 1200,00   
BINSS13ACTETO ==> R$ 1500,00 - R$ 1200,00    
= R$ 300,00  
A variável BINSS13ACTETO vai retornar R$ 300,00. Se o Teto de INSS for maior a variável retornará 0.   
   
   
**Função BASERECFER:**  
Retorna valor da base do último Recibo de Férias  
Os valores utilizados para retorno são:  
INSS – Base INSS de Férias  
IRRF – Base IRRF de Férias  
   
 **Exemplo:**  
   BASERECFER('INSS') ou BASERECFER('IRRF')  
   
**Observação**:  
  -Quando a variável for utilizada no recibo de férias o sistema irá verificar a incidência dos eventos para retornar o valor, caso contrário o sistema irá buscar as bases gravadas no Recibo de Férias.  
  -Mesmo quando o funcionário tiver férias partidas, ou seja, iniciando em um mês e terminando em outro, o sistema irá buscar o valor total da base de INSS.  
   
**Função BINSS13ACTETOMOV:**  
Retorna a base de INSS 13º Salário acima do teto do mês e ano corrente, podendo ser utilizada em eventos e relatórios.  
   
**Função BASEIRRF13:**  
Retorna a Base IRRF 13º Salário da movimentação atual. Retorna valor.   
   
**Função BASEIRRF13FF:**  
Retorna a Base IRRF 13º Salário da Ficha Financeira.  
BASEIRRF13FF (ANO COMPETÊNCIA, MÊS COMPETÊNCIA)  
   
**Função BASEIRRFFERIASFF:**  
Retorna a Base IRRF Férias da Ficha Financeira.  
BASEIRRFFERIASFF (ANO COMPETÊNCIA, MÊS COMPETÊNCIA)

**Função BANCOHORASPERIODOCHRONUS**   
Retorna o valor de saldo de banco de horas que do funcionário dentro de um intervalo informado. BANCOHORASPERIODOCHRONUS('DATA','DATA')
