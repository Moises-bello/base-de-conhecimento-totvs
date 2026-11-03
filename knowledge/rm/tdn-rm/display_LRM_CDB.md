---
content_hash: fd3e3456ba836b0053157e4b73b8333da984817663b0489da90e0ea133c87851
fetched_at: '2026-06-29T00:09:19.385041+00:00'
page_id: '421388860'
product: rm
source: tdn-rm
title: CDB
type: documentation
url: https://tdn.totvs.com/display/LRM/CDB
version: 3
---

CDB pode ser resgatado antes do vencimento e o RDB deve ser resgatado apenas no vencimento. Ambos os títulos podem ser pré-fixados ou pós-fixados.

**CDB Pós-Fixado**

O valor do resgate final da aplicação saberá somente na data de vencimento, de acordo com a variação do indexador e o percentual da taxa contratada.  
 Remuneração: Taxa de juros pré-estabelecida na data da aplicação + Taxa variável que utiliza certo índice (FatorCDI).  
 O valor do rendimento é calculado pelo saldo \* FatorCDI. Este fator CDI é disponibilizado no site [WWW.cetip.com.br](http://www.cetip.com.br/) (Estatísticas/CALCULO DE ACUMULADO ENTRE DATAS), onde será necessário preencher qual a Taxa que a aplicação de CDB utiliza.  
 Exemplo:  data 23/03/2012 a 30/03/2012 (último dia útil do mês) com uma taxa de 20%, o fator do CDI será 1,00035997.  
 O valor da aplicação em março será (valor inicial \* FatorCDI):   
 8.096.492,46 \* 1,00035997 = 8.099.406,95 Ou seja, o rendimento será 8.099.406,95 – 8.096.492,46 = 2.914,49

**Cálculo do Rendimento, IOF e IR**

Nesta modalidade de CDB o cálculo é mais complexo, portanto a regra abaixo deve ser aplicada para cada dia:  
 1.     Nº de dias: Número de dias calculado pela data de início do CDB – a Data Atual.  
 2.     Fator de Rendimento = (1+Cotacao do CDI anterior a data atual/100) elevado a (1/252) – Caso a data atual seja Sábado, Domingo ou Feriado o fator de rendimento é 1 (irá anular o rendimento).  
 3.     Saldo Inicial: Saldo da aplicação sem o rendimento da data atual  
 4.     Taxa Fixa: Taxa acertada para remuneração da aplicação  
 5.     Rendimento= (Saldo Inicial\* (Fator de Rendimento -1)\* Taxa Fixa)/100  
 6.     Saldo Atual: Saldo Inicial + Rendimento  
 7.     Ajuste: Valor Positivo ou negativo que foi incluído para corrigir distorções de cálculo  
 8.     Resgate: Valor que foi retirado da aplicação   
 9.     Alíquota de IR = Se o vencimento é anterior a 2005 a alíquota é 20%.   
 Se for posterior o cálculo é feito com uso da variável Nº de dias e a tabela regressiva de IR. Caso excepcional: Se a aplicação iniciou antes de 22/12/2004 tomar como 01/07/2004 à data de início para efeito do Nº. de dias. (Mesmo que a data de início seja anterior a 01/07/2004)  
 10.  Alíquota de IOF: Utilizar a variável nº. de dias e encontrar na tabela regressiva de IOF a alíquota.  
 11.  Rend Acum-Rendimento Acumulado: Soma dos rendimentos até a data atual (inclusive).  
 12.  Ajus Acum – Ajustes Acumulados: Soma de todos os ajustes até a data atual (inclusive)  
 13.  CDI Acum – CDI Acumulado: (Rend Acum – Acum Rend1) / (Valor Aplicado+Ajus Acum- Acum Resg1).  
 14.  CDI Acum2 – CDI Acumulado sem IOF = CDI Acum – (CDI Acum\*Alíquota de IOF)  
 15.  CDI Acum3 – CDI Acumulado sem IOF e IR= CDI Acum2 – (CDI Acum2\*Alíquota de IR)  
 16.  Resgate 1 - Resgate Sobre o Valor Principal: Resgate / (1+CDI Acum3)  
 17.  Valor IOF = Alíquota de IOF\*CDI Acum\*Resgate1  
 18.  Valor IR = Alíquota de IR\*CDI Acum2\*Resgate1  
 19.  Rend 1: Rendimento resgatado sobre o valor principal: CDI Acum\*Resgate1  
 20.  Acum Resg1: Resgate sobre o valor principal acumulado: Soma de Resgate1  
 21.  Acum Rend1: Resgate sobre o rendimento acumulado: Soma de Redn1  
 22.  Acum IOF - Pagamentos de IOF acumulados: Soma de Valor de IOF  
 23.  Para o cálculo do último resgate usaremos a fórmula do resgate líquido (já contempla a possibilidade de aplicações com rendimento em 2004 e 2005:  
 a.     Resgate Bruto: Saldo Atual no final da aplicação.  
 b.     CDI Acum: Somar o CDI Acum anterior a 2005 com o CDI Acum posterior a 2004  
 c.     CDI Acum3: Somar o CDI Acum3 anterior a 2005 com o CDI Acum posterior a 2004  
 d.     Resultado= (Resgate Bruto) / (CDI Acum+1) \* (CDI Acum3+1)  
 Os valores em marrom claro devem ser calculados separadamente durante um resgate para as aplicações que iniciam em 2004 e tem o resgate em 2005 pois os cálculos variam dependendo do ano. Ou seja, a Alíquota de IR pode ser uma em 2004 e outra em 2005, o rendimento acumulado de 2004 não deve ser misturado com o rendimento de 2005 e assim por diante para todas as demais variáveis. Note que estas variáveis são para cálculo do valor de IR e IOF e não são necessárias para o rendimento.

**Explicação sobre o Cálculo de Rendimento do CDB Pós-Fixado:**

Na data de aplicação não há rendimentos. O Rendimento é calculado em cima do saldo do dia anterior, Rendimento = Saldo Anterior \* Fator CDI.   
 Fator CDI (Valor Cotação, TaxaCDB) =   
 Caso no mesmo dia tenha havido resgates, deve se calcular o IOF e IR além de valores internos que serviram para novos cálculos, como RendResgatado e PrincResgatado. Quando o usuário desejar fazer um resgate para calcular o valor do IOF e IR podem ser usados as formulas abaixo para cálculo do imposto.

VlIR = BaseIR(ResgateSolicitado, dt) \* AlíquotaIR(dt);  
 Base IR = ResgateSobrePrincipal(ResgateSolicitado, dt) \* CDIAcumSemIOF(dt) / 100;   
 ResgateSobrePrincipal = ResgateSolicitado / FatorCDIAcumSemIr\_IOF(dt);  
 FatorCDIAcumSemIr\_IOF = CDIAcumSemIR\_IOF(Dt) / 100 + 1;  
 CDIAcumSemIR\_IOF = CDIAcumSemIOF(Dt) - CDIAcumSemIOF(Dt) \* AlíquotaIR(Dt);  
 CDIAcumSemIOF = CDIAcumulado(Dt) - CDIAcumulado(Dt) \* AlíquotaIOF(Dt);  
 CDIAcumulado = RendASerResgatado(Dt) / PrincASerResgatado(Dt) \* 100;  
 PrincASerResgatado = VlAplicacao - PrincipalJaResgatado(Dt) + AjusteAcumulado(Dt);  
 RendASerResgatado = RendimentoAcumulado(Dt) - RendJaResgatado(Dt);  
 PrincipalJaResgatado = Somatório de todos os valores de ResgateSobrePrincipal anteriores.  
 RendJaResgatado = Somatório de todos os valores de (ResgateSobrePrincipal \* CDIAcumulado(Dt)/100) anteriores.  
 VlIOF = BaseIOF(ResgateSolicitado, dt) \* AlíquotaIOF(dt);  
 BaseIOF = ResgateSobrePrincipal(ResgateSolicitado, dt) \* CDIAcumulado(dt) / 100;  
 RendimentoAcumulado = Valor de todos os rendimentos até aquela data, inclusive o da data atual

**Cálculo do Saldo Disponível para o Resgate Total**

SaldoDisponivel= SaldodaAplicacao /(CDIAcumulado(dt)/100 +1) \* FatorCDIAcumSemIr\_IOF(dt);  
 CDB Pré-Fixado: o investidor sabe, no ato da aplicação, o valor do resgate final, pois a taxa no prazo contratado é mantida até o vencimento.  
 Remuneração: Taxa de juros fixa determinada na data da aplicação, sempre referida ao ano.  
 Liquidez (rendimento): Somente no vencimento da aplicação, ao realizar resgate total.  
 Ao inserir a aplicação, importante observar os campos "Taxa Fixa" e "Data vencimento Aplicação".  
 "NumDias" = quantidade de dias que existirá a aplicação (data inicio – data vencimento).  
 Fator CDI: utilizado para calcular o saldo real. Necessário: cotação, numdiasAno, taxa fixa CDB.  
 Saldo Real: saldo para rendimento \* FatorCDI   
 Diferença entre Pré-Fixado e Pós-Fixado: ao calcular o FatorCDI, a quantidade de dias no ano para encontrar o percentual do dia é diferente em cada tipo.  
 Pós-fixado: NumDiasAno = 252;   
 Pré-fixado: NumDiasAno = 360;  
    
 **O cálculo do Rendimento, IOF e IR**

Nesta modalidade de CDB o cálculo ainda é simples e somente é feito no último mês:

1 – IOF: Não temos incidência  
 2 – Valor Aplicado: Somar a aplicação inicial com todos os lançamentos de ajustes e decrementar dos resgates  
 3 – Nº de dias: Número de dias corridos do CDB  
 4 – Taxa Fixa: Taxa acertada para remuneração da aplicação  
 5 – Fator de Rendimento = (1 + Taxa Fixa/100) elevado ao (Fator de rendimento/360)  
 6 – Saldo Atual: Valor Aplicado \* Fator de Rendimento  
 7 – Rendimento = Saldo Atual – Valor Aplicado  
 8 – Alíquota de IR = Se o vencimento é anterior a 2005 a alíquota é 20%. Se for posterior o cálculo é feito com uso da variável No de dias e a tabela regressiva de IR.        Caso excepcional: Se a aplicação iniciou antes de 22/12/2004 tomar como 01/07/2004 à data   de início para efeito do No. de dias. (Mesmo que a data de início seja anterior a 01/07/2004)

9 – Valor de IR = Rendimento \* Alíquota de IR  
 10- Resgate Final: Saldo Atual – Valor de IR
