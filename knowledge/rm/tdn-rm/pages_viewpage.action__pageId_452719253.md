---
content_hash: a892d01b43668ebf4e77783ed7915dae604980fdaccc5bda9122edb789501ea7
fetched_at: '2026-06-29T00:10:04.796493+00:00'
page_id: '452719253'
product: rm
source: tdn-rm
title: Fórmulas / Funções – L
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719253
version: 3
---

**Função L**  
 Retorna salário líquido.

**Atenção**

As variáveis de fórmula que são relativas a movimentação do funcionário, como a L, não devem ser utilizados para fórmula de seleção. Porque no momento da seleção, o sistema ainda não executou a movimentação do funcionário. Desta forma, estas funções/variáveis irão retornar sempre "zero".  
    
    
    
 **Função LI**  
 Retorna o acumulado mensal de determinado evento, no período atual, mês e ano de competência.  
 LI ('CODIGO DO EVENTO')  
    
 **Observação:**  
  Se o evento estiver sendo calculado ele não aparece no período atual.  
    
    
    
 **Função LIMITEMAX**  
 Retorna sempre o limite máximo da tabela de cálculo.  
 LIMITEMAX ('CÓDIGO DA TABELA')  
    
    
 **Exemplo**  
 LIMITEMAX ('INSS') /\* LIMITE MAXIMO DE UMA TABELA INSS \*/  
 LIMITEMAX ('IRRF') /\* LIMITE MAXIMO DE UMA TABELA IRRF \*/   
    
    
 **Função LIQFERIAS**  
 Retorna o liquido de férias.  
 LIQFERIAS  
    
 **Observação:**  
 -Quando a variável LIQFERIAS é utilizada no recibo de férias, o retorno será o valor daquele recibo.  
 -Quando a variável LIQFERIAS é utilizada no envelope de pagamento, o retorno será o líquido do primeiro recibo de férias que está com a situação diferente de 'F-Finalizadas'.  
 -Caso não encontre nenhum período não finalizado, será retornado o líquido do último recibo de férias 'F-Finalizadas'.  
    
    
 **Função LIQFERIASDATA**  
 LIQFERIASDATA (DATA, DATA, TIPO)  
 Retorna o líquido do recibo de férias conforme intervalo de data de pagamento e tipo informado.  
 No parâmetros DATA1 e DATA2 informe o intervalo da data de pagamento a ser considerada.  
 No parâmetro TIPO informe:  
 0 = Retorna o somatório dos líquidos de todos os recibos de férias.  
 1 = Retorna o líquido do primeiro recibo de férias.  
 2 = Retorna o líquido do último recibo de férias.  
    
 **Atenção I:**  
 São considerados apenas férias com situação 'M-Marcadas ou 'P-Pagas'.  
    
 **Exemplo:**  
 O funcionário gozou férias nos períodos:  
 **Período de Gozo**                     **Data de Pagamento**    **Situação Férias           Valor Líquido**  
 06/06/2011 a 25/06/2011             03/06/2011                    P-Pagas                                  R$800,00  
 01/07/2011 a 10/07/2011             29/06/2011                    M-Marcadas                            R$400,00  
    
 Fórmula: LIQFERIASDATA(01/06/2011,30/06/2011,0), retorna R$1.200,00  
 Fórmula: LIQFERIASDATA(01/06/2011,30/06/2011,1), retorna R$800,00  
Fórmula: LIQFERIASDATA(01/06/2011,30/06/2011,2), retorna R$400,00  
    
    
    
 **Função LIQUIDOFF**  
 Função que apresenta o líquido do funcionário em um determinado ano, mês e período  
 LIQUIDOFF (VALOR, VALOR, VALOR)   
 Onde:  
 1º parâmetro é o ano  
 2º parâmetro é o mês   
 3º parâmetro é o período.   
    
    
 **Exemplo**  
 LIQUIDOFF (2013, 8, 2) O sistema apresentará o líquido do funcionário do período 2 de 08/2013.  
    
 **Observação:**  
 Caso o usuário deseja o líquido de todos os períodos, deve-se informar o valor 0 (zero) no 3º parâmetro da função.  
    
    
    
 **Função LIQPERIODOS**  
 Retorna valor líquido do movimento da ficha financeira  
 LIQPERIODOS (VALOR, VALOR, STRING)  
 Onde:  
 **Valor** = Mês  
 **Valor** = Ano   
 **String** = Período   
    
    
 **Função LIQPROVFER**  
 Retorna o liquido da provisão de Férias.   
 Esta função deverá ser utilizada exclusivamente no processo de provisão, em qualquer outro processo o retorno será zero.  
 O ideal é utilizá-la é nos eventos adicionais, devido os eventos adicionais serem calculados somente no final, ou seja, após o cálculo da provisão do período vencido e do período proporcional.   
 A ordem de cálculo dos eventos adicionais segue a prioridade do evento, que irá influenciar também no valor retornado por esta função.  
    
 Segue a ordem de cálculo da provisão:  
 1º.    Calcula o valor das férias do(s) período(s) vencido(s), considerando férias, médias e 1/3 de férias.  
 2º.    Calcula o valor das férias do período proporcional, considerando férias, médias e 1/3 de férias.  
 3º.    Calcula os eventos adicionais de férias.   
 Para este cálculo o sistema primeiro busca os eventos adicionais informados no cadastro de férias do funcionário e os eventos adicionais dos parâmetros globais de férias e em seguida ordena pela prioridade do evento. Possibilitando ao usuário definir quais eventos adicionais deverão compor o valor da variável LIQPROVFER.   
 Caso o evento adicional que contém a fórmula com a função LIQPROVFER tenha a prioridade menor do que os demais eventos adicionais, nenhum dos outros eventos entrarão para o cálculo do valor.   
 Caso o evento adicional que contém a fórmula com a função LIQPROVFER tenha a prioridade maior do que os demais eventos adicionais, todos os outros eventos serão considerados no cálculo do valor.  
    
 **Atenção:**  
 Os eventos adicionais são provisionados somente uma vez, independentemente do número de períodos aquisitivos. Exceto quando o parâmetro "Proporcionalizar conforme dias direito" está marcado, neste caso o valor dos eventos adicionais será proporcionalizado pelos avos totais de todos os períodos.   
    
 **Exemplo:**   
 O Funcionário tem 12/12 avos vencidos e 8/12 avos proporcionais, o cálculo será (valor dos eventos adicionais / 12 \* 20).  
    
    
 **Função LIQPROV13**  
 Retorna o liquido da provisão de 13º Salário.   
 Esta função deverá ser utilizada exclusivamente no processo de provisão, em qualquer outro processo o retorno será zero.  
 O ideal é utilizá-la é nos eventos adicionais, devido os eventos adicionais serem calculados somente no final, ou seja, após o cálculo da provisão.   
 A ordem de cálculo dos eventos adicionais segue a prioridade do evento, que irá influenciar também no valor retornado por esta função.  
    
 Segue a ordem de cálculo da provisão:  
 1º.    Calcula o valor do 13º salário.  
 2º.    Calcula os eventos adicionais de 13º salário.   
 Para este cálculo o sistema busca os eventos adicionais dos parâmetros globais de 13º salário e em seguida ordena pela prioridade do evento. Possibilitando ao usuário definir quais eventos adicionais deverão compor o valor da variável LIQPROV13.   
 Caso o evento adicional que contém a fórmula com a função LIQPROV13 tenha a prioridade menor do que os demais eventos adicionais, nenhum dos outros eventos entrarão para o cálculo do valor.   
 Caso o evento adicional que contém a fórmula com a função LIQPROV13 tenha a prioridade maior do que os demais eventos adicionais, todos os outros eventos serão considerados no cálculo do valor.  
    
    
 **Função LINHAVTCORRENTE**  
 Retorna a Linha de Vale transporte corrente.   
 LINHAVTCORRENTE (STRING)   
 Onde:  
 **String** é um campo da tabela de LINHAVTCORRENTE

**Observação**

A função só funciona no processo "Gerar compra de vale transporte".  
    
    
 **Função LTRANS**  
 Retorna código da linha de transporte utilizada pelo funcionário.  
 LTRANS(VALOR)  
 Onde o valor é o número de ordem de cadastramento da linha para o funcionário.

**Exemplo**

DECL k, Linha, Res;   
 SETVAR(k, 1); SETVAR(Res, 0);   
 REPITA SETVAR (Linha, LTrans(k));   
 SE Linha <> '' ENTAO SETVAR(Res, Res + NVD(Linha) \* VlrVale(Linha) ) FIMSE; SETVAR (k, k + 1) ATE Linha = '';   
 MIN(RC \* 0.06, C('0032')) + Res \* N('0008');
