---
content_hash: 51d6f2b133f364513da86df879757ec883208fbc35c55f7ace108275b62d919f
fetched_at: '2026-06-29T00:09:17.736558+00:00'
page_id: '421388633'
product: rm
source: tdn-rm
title: Fundos de Investimento | Curto Prazo e Médio Prazo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388633
version: 5
---

O Cálculo do Rendimento, IOF e IR

Para entendermos o cálculo do Rendimento nos Fundos de investimento, devemos seguir os seguintes passos, calculando as variáveis necessárias:

1.     Data Atual: Data do evento (Resgate, aplicação, Ajuste, Rendimento)  
 2.     Fator de Rendimento = Cotação do fundo na data atual   
 3.     Saldo Anterior = saldo total do último cálculo atualizando o saldo do fundo  
 4.     Rendimento= (Saldo anterior\* (Fator de Rendimento Atual – Fator de rendimento Anterior) / Fator de rendimento Anterior  
 5.     Ajuste: Valor Positivo ou negativo que foi incluído para corrigir distorções de cálculo  
 6.     Resgate: Valor que foi retirado da aplicação   
 7.     Saldo Resgate Bruto=Saldo Anterior + Ajustes + Rendimentos  
 8.     Saldo Resgate Líquido = Saldo Resgate Bruto – (IofAtual2004+IfoAtual2005) - (BaseIr2004\*0,2 + BaseIr2005\*AliqIrRegr)   
 9.     % Resgate - Em casos onde há lançamento de resgate = Saldo Resgate Liquido/ Saldo Resgate Bruto  
 10.  RA2004 - Rendimento Acumulado do Período Atual Sendo este anterior a 2005: Para entender este conceito é preciso entender que o cálculo do IR é feito dentro de um período entre o come cotas anterior e a data do próximo come cotas. Estas variáveis têm o objetivo de separar os saldos por período, acumulando-os. RA2004 = se for ano de 2004 ou anterior e ainda estiver dentro do mesmo período, somar o rendimento atual ao saldo de RA2004.  
 11.  RAR2004 – Rend. Acum. Resgatado do Período Atual, sendo este anterior a 2005: RAR2004 = se for ano de 2004 ou anterior e ainda estiver dentro do mesmo período, somar o (%Resgate\*RA2004) ao saldo de RAR2004.  
 12.  RendIrAtual2004 – Parte do Rendimento que ainda não foi resgatado no período atual. RendIrAtual2004 = No período atual acumular (RA2004-RAR2004) quando houver resgates ou rendimentos.  
 13.  RAPA2004 - Rendimento Acumulado do Período Anteriores sendo este anterior a 2005 = RA2004 do período anterior;  
 14.  RARPA2004 - Rendimento Acumulado Resgatado do Período Anterior, sendo este anterior a 2005:  
 15.  RendIrAnteior2004 = RendIrAtual2004 do período anterior.  
 16.  RA2005 - Rendimento Acumulado do Período Atual, sendo este posterior a 2004: RA2005 = Se for ano de 2005 ou posterior e ainda estiver dentro do mesmo período, somar o rendimento atual ao saldo de RA2005.  
 17.  RAR2005 - Rendimento Acumulado Resgatado do Período Atual, sendo este posterior a 2004: RAR2005 = Se for ano de 2005 ou posterior e ainda estiver dentro do mesmo período, somar o (%Resgate\*RA2005) ao saldo de RAR2005.  
 18.  RendIrAtual2005 – Parte do Rendimento que ainda não foi resgatado no período atual. RendIrAtual2005 = No período atual acumular (RA2005-RAR2005) quando houver resgates ou rendimentos.  
 19.  RAPA2005 - Rendimento Acumulado do Período Anteriores sendo este posterior a 2004: = RA2005 do período anterior;  
 20.  RARPA2005 - Rendimento Acumulado Resgatado do Período Anterior, sendo este posterior a 2004. = RAR2005 do período anterior;  
 21.  RendIrAnteior2005 = RendIrAtual2005 do período anterior.  
 22.  IOFAtual2004 = (RendIrAtual2004+RendAnteior2004) \*AliqIOF  
 23.  IOFAnterior2004 = (RendAnteior2004) \*AliqIOF  
 24.  IOFAtual2005 = (RendIrAtual2005+RendAnteior2005) \*AliqIOF  
 25.  IOFAnterior2005 = (RendAnteior2005) \*AliqIOF  
 26.  IOF = (IOFAtual2004+IOFAtual2005) \*%Resgate  
 27.  BaseIR2004 = (RendIrAtual2004 – IOFAtual2004 + IOFAnterior2004)  
 28.  BaseIR2005 = (RendIrAtual2005 – IOFAtual2005 + IOFAnterior2005)  
 29.  BaseIRComplementar2004 = (RendIrAnteior2004 - IOFAnterior2004 + IOFAtual2004)  
 30.  BaseIRComplementarPos2004 = (RendIrAnteior2005 - IOFAnterior2005 + IOFAtual2005)  
 31.  AlíquotaIRRegressiva = Calculada conforme o CDB para os resgates.  
 32.  AlíquotaIRFundo = No fundo de curto prazo é 20% e no de médio prazo é 15%.  
 33.  IR Resgate= (BaseIR2004\*0,2+BaseIR2005\*AlíquotaIRRegressiva)\*%Resgate  
 34.  IR ComeCotas=(BaseIR2004\*0,2+BaseIR2005\*AlíquotaIRFundo)\*%Resgate  
 35.  Saldo Atual = Saldo Anterior+Ajustes+Aplicacao-Resgates+Rendimento-IRComeCotas-IRResgates-IOF;  
 36.  No. Cotas= Saldo Final/Valor da Cota Atua  
    
 Rendimento diário = (cotacaoAtual - cotacaoAnterior) \* SaldoRend / cotacaoAnterior.

IR Come Cotas:

- Antecipação do IR cobrado sobre rendimentos.   
 - Recolhido no encerramento dos meses de maio e novembro a partir de 2005.   
 - Reduz a quantidade de cotas do investidor.  
 Alíquota de IR Come Cotas: Curto prazo é sempre 15%. Longo prazo é 20% antes de 2004 e 15% a partir de 2005.

**Alíquota do IR Comecotas**

**Tipo de aplicação      Alíquota %**

Curto Prazo                      15% (sempre)

Longo Prazo                     20% até 31/12/2004

Longo Prazo                     15% após 01/01/2005

A alíquota de cobrança do IOF é regressiva, podendo variar de 96% para aplicações por 1 dia até 3% para aplicações por 29 dias. A partir do 30º dia da aplicação, não haverá a incidência do IOF. Podemos concluir então que quanto mais tempo o investidor deixar o dinheiro aplicado, menos IOF vai pagar, aumentando assim a sua rentabilidade.O IOF incide sobre os resgates solicitados dentro dos primeiros vinte e nove dias da aplicação financeira, conforme determinação legal do Ministério da Fazenda.   
 O IOF sobre aplicações financeiras só será controlado se o parâmetro "Coligada Isenta de Impostos para Aplicação Financeira" estiver desmarcado (Ambiente | Parâmetros | Gestão Financeira | Controle Bancário | Aplicação Financeira | Etapa 4 – Aplicação Financeira).

O Imposto de Renda (IR) sobre aplicações financeiras só será controlado se o parâmetro "Coligada Isenta de Impostos para Aplicação Financeira" estiver desmarcado (Ambiente | Parâmetros | Gestão Financeira | Controle Bancário | Aplicação Financeira | Etapa 4 – Aplicação Financeira).

Para o cálculo e dedução do Imposto de Renda (IR) sobre aplicações financeiras é utilizada a Tabela de Imposto de Renda. As alíquotas podem variar de 22,5% para resgates de aplicações por até 180 dias a 15% para resgates de aplicações por mais de 720 dias.

**Tabela Regressiva de Alíquota de IR**

**Prazo da Aplicação    Alíquota %**

Até 180 dias                    22,5

De 181 a 360 dias           20

De 361 a 720 dias          17,5

 Acima de 720 dias         15

Os lançamentos de resgate de imposto de renda são gerados automaticamente ao realizar resgates de aplicação e no vencimento.

**Observações:**

A cobrança do IR é realizada diretamente na fonte, por isso, não será gerado extrato de caixa para os lançamentos de IR. Os lançamentos de Resgate de Imposto de Renda serão gerados somente no módulo de aplicação financeira.

Longo Prazo cadastrado como curto prazo, o saldo poderá ficar correto durantes anos, porém vai ter um dia em que o saldo não ficará mais correto. Motivo: o banco está resgatando uma aplicação 2, enquanto o sistema Gestão Financeira ainda está com saldo na aplicação 1 para resgatar (diferença na alíquota de IR Comecotas).

Não deve inserir cotações em feriados Nacionais e finais de semana.

Véspera de Carnaval é dia útil. Inserir cotação com valor IGUAL AO DIA ANTERIOR AO FERIADO, na data segunda-feira véspera do carnaval.
