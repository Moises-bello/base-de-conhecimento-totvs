---
article_id: 360014441032
category: RH - Cálculo Adiantamento
content_hash: 974c203320e6d32403593d984ef7896af6e8ad49277866085be862023d575a14
fetched_at: '2026-06-28T22:43:14.238649+00:00'
product: protheus
section_id: 360011983213
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular adiantamento salarial sobre salário
  + adicionais
type: support-article
updated_at: '2025-04-14T19:37:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014441032-RH-Linha-Protheus-GPE-Como-calcular-adiantamento-salarial-sobre-sal%C3%A1rio-adicionais
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24787929222295) Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Como calcular adiantamento salarial sobre salário + adicionais (Periculosidade, insalubridade, adicional por tempo de serviço, confiança e transferência) ?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12  
  
**Conceito**O adiantamento salarial por si próprio consiste no adiantamento de parte do salário do empregado de forma antecipada ao recebimento do montante salarial.

Os **adicionais padrões**: Periculosidade, insalubridade, adicional por tempo de serviço, confiança e transferência são consideradas verbas indenizatórias e não fazem parte do salário do empregado, sendo assim, ao realizar o cálculo do **adiantamento salarial** o sistema não apresentará uma verba que represente o adicional e outra verba que apresente o adiantamento, ou seja, apenas a verba de adiantamento será apresentada com base no salário do empregado vezes o percentual de adiantamento salarial informado no cadastro do empregado.

Porém, no sistema existe uma opção através do cadastro de verbas onde poderá ser informado se as verbas de adicionais deverão ou não incorporar o salário do empregado. Informando sim no campo Incorpora Salário, esta verba passará a ser utilizada como base de cálculo para todos os fins.  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
  
**1. GPEA160**: **Atualizações > Definições de cálculo > Roteiros** - ADI:  
Verifique nos roteiros de cálculo do adiantamento salarial, se a coluna habilitado está igual a **SIM** para todas as sequências e fórmulas padrão do sistema.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24787929229847)  
  
**2.** **GPEA300**: **Atualizações > Definições de Cálculo > Mnemônicos**:  
Os valores dos adicionais serão considerados na verba de provento do adiantamento (ID 0006). Assim para calcular adiantamento com adicionais, o mnemônico **P\_SOMAINC** deve estar habilitado. Conteúdo igual a **.T.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24787943051927)

3. **GPEA040**: **Atualizações > Definições de Cálculo > Verbas**:  
A verba de provento do adiantamento **(Id 0006)** deve estar com campo base de cálculo (**RV\_BASCAL**) = **Salário incorporado**, assim o cálculo será feito sobre o salário + todos os adicionais do funcionário que estejam incorporando ao salário (campo RV\_INCORP) = Sim.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24787929239191)  
  
**Saiba Mais**  
Veja um exemplo pratico utilizando o adicional de periculosidade: <http://tdn.totvs.com/x/sCUtE>

[RH - Cálculo Adiantamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983213-RH-C%C3%A1lculo-Adiantamento)
