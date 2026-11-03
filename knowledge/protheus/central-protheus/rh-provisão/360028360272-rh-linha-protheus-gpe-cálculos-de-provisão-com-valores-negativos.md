---
article_id: 360028360272
category: RH - Provisão
content_hash: 595c8a5c6463c3aeb04124baa51b3c76ad5cb156f34efe9061e21e54ffe8cbff
fetched_at: '2026-06-28T22:43:55.695890+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculos de Provisão com Valores Negativos
type: support-article
updated_at: '2025-06-17T20:01:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028360272-RH-Linha-Protheus-GPE-C%C3%A1lculos-de-Provis%C3%A3o-com-Valores-Negativos
---

**Dúvida**Em Quais Momentos o Sistema poderá Apresentar Valores Negativos no Cálculo das Provisões?  
 **Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução**No Cálculo das Provisões de Férias e 13º Salário, o sistema pode Apresentar Valores Negativos na linha "No Mês"  quando há diminuição entre o Valor Atual, e o Valor Provisionado Anteriormente.  
  
A diminuição dos valores de Provisão poderá ocorrer quando:  
  
1 - Na Coluna "Valor", quando o funcionário teve Faltas e perde direito dias de Férias ou 13º Salário ou se houver uma Redução Salarial.  
**Por Exemplo**: Supondo que temos de saldo provisionado (Linha "Anter") de R$ 1.000.00, porém, neste mês tivemos um saldo Atual (Linha "Atual") de R$ 800.00, pois o funcionário Faltou mais de 06 dias e perdeu avos de Férias ou 13º Salário, então com relação ao mês anterior o seu saldo diminuiu em R$ -200,00.  
A memória de cálculo é: Atual - Anterior = No Mês.  
  
2 - Na Coluna "Adicionais", quando o funcionário perde direito à algum adicional (ATS, Periculosidade, Insalubridade, Cargo de Confiança ou Adicional de Transferência).  
**Por Exemplo**: Supondo que até 03/2020 o funcionário atuava em local Insalubre e tinha direito à um adicional de 30% sobre o Salário Base. Em 04/2020 o funcionário foi transferido e não está mais exposto ao risco, portanto não tem mais direito à este Adicional, então com relação ao mês anterior o seu saldo de Adicionais também poderá sofrer redução.  
  
3 - Na Coluna "Adicionais", quando o valor das Médias de Férias ou 13º Salário diminuir.  
Neste caso, a diminuição poderá ocorrer quando o funcionário não recebe variáveis como Bônus, Gratificações ou Horas Extras por um ou mais meses.  
**Por Exemplo:** Em 03/2020 o valor das Médias do Funcionário era R$ 300,00.  
Memória de Cálculo: Total das Médias/ Avos de Direito (900 / 3 = 300,00).  
Em 04/2020 o funcionário não recebeu nenhuma variável, portanto, os valores recebidos até 03/2020 serão proporcionalizados por mais um mês.  
Memória de Cálculo: Total das Médias/ Avos de Direito (900 / 4 = 225,00).  
Com relação ao mês anterior o seu saldo diminuiu em R$ -75,00.  
  
4 - Nas Colunas de Encargos de INSS e FGTS, quando já houver valores negativos nas colunas "Valor" e/ou "Adicionais";  
  
5 - Em toda a linha "No Mês", quando o Funcionário Perde direito ao Período Aquisitivo, por motivo de Afastamento ou Faltas.  
**Por Exemplo:** Supondo que até 05/2020 o funcionário completou mais de 180 dias de afastamento considerando o Período Aquisitivo Vigente, neste caso, o funcionário perde direito aos 30 dias de Férias, portanto na linha "No Mês", o sistema apresentará os valores provisionados até o mês 04/2020 negativos, para que o Saldo Atual das provisões de férias seja zerado.  
  
6. Quando ocorre a provisão de férias , o sistema valida férias para 30 dias e sobre esses dias os encargos. Quando o funcionário tira 20 dias de férias e 10 dias de abono, os 10 dias de abono não incidem FGTS e INSS e desta forma como já foram provisionados o sistema precisa abater no saldo contábil e por isso apresenta os valores negativos.  
  
7. Nos casos de desligamentos, quando as férias são indenizadas em rescisão, não há recolhimento dos encargos de INSS e FGTS, portanto não devem apresentar Baixas sobre os respectivos encargos, apresentando valores negativos na linha "No Mês".  
  
**Importante:** O sistema não apresenta Valores Negativos na linha "Atual".   
  
**Saiba Mais:**  
[RH - Linha Protheus - GPE - Baixa de Encargos de INSS e FGTS de Férias na Provisão não é realizada no mês de Desligamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043786654-RH-Linha-Protheus-GPE-Baixa-de-Encargos-de-INSS-e-FGTS-de-F%C3%A9rias-na-Provis%C3%A3o-n%C3%A3o-%C3%A9-realizada-no-m%C3%AAs-de-Desligamento)  
[RH - Linha Protheus - GPE - Conferência dos encargos de INSS e FGTS de Provisão de Férias com baixas de Férias e Abono Pecuniário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028640453-RH-Linha-Protheus-GPE-Confer%C3%AAncia-dos-encargos-de-INSS-e-FGTS-de-Provis%C3%A3o-de-F%C3%A9rias-com-baixas-de-F%C3%A9rias-e-Abono-Pecuni%C3%A1rio)

<https://tdn.totvs.com/pages/viewpage.action?pageId=223164872>
