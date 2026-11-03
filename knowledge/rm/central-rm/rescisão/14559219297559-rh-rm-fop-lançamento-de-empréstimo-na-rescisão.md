---
article_id: 14559219297559
category: Rescisão
content_hash: ef3a266a0a127f703f64eef4734f1dda96e349766d4a2a891b6e8596c4f85802
fetched_at: '2026-06-28T22:46:54.240734+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: RH - RM - FOP - Lançamento de Empréstimo na Rescisão
type: support-article
updated_at: '2024-06-17T15:08:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14559219297559-RH-RM-FOP-Lan%C3%A7amento-de-Empr%C3%A9stimo-na-Rescis%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24231522273687) Tempo aproximado para leitura: **00:03:50****Dúvida**Como realizar o desconto do empréstimo na rescisão do funcionário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Deverá acessar **Administração de pessoal | Fórmulas** e criar uma formula que retorne 30% sobre o salário líquido do funcionário. Abaixo temos uma fórmula exemplo:

**Exemplo de Fórmula que calcula 30% de desconto do empréstimo na Rescisão**

|  |
| --- |
| `DECL SaldoTot;`  `DECL TotEmp;`  `DECL ItemEmp;`  `DECL Retorno;`  `DECL SalLiq;`  `DECL MaxEmp;`  `DECL saldodist;`  `DECL aDistribuir;`    `SetVar(ItemEmp,0);`  `setvar(MaxEmp,0);`  `setvar(SalLiq, 0);`  `SetVar(aDistribuir,0);`  `SetVar(Retorno,``''``);`  `SetVar(saldodist,0);`    `SetVar(SaldoTot, InfEmp(-2,``'codigo'``));`  `SetVar(TotEmp, InfEmp(-1,``'codigo'``));`  `setvar(SalLiq, L);`  `setvar(MaxEmp, SalLiq*0.3);`    `Se TotEmp > 0`  `Entao`  `Se MaxEmp >= SaldoTot`  `Entao`  `repita`  `SetVar(ItemEmp,ItemEmp + 1);`  `SetVar(aDistribuir, InfEmp( ItemEmp,``'SALDODEVEDOR'` `) );`  `SetVar(aDistribuir,val( str(aDistribuir,``'999999999,99'``)));`  `SetVar(Retorno, Concat(Retorno, InfEmp( ItemEmp,``'CODIGO'` `)));`  `SetVar(Retorno,Concat(Retorno,``':'``));`  `SetVar(Retorno, Concat(Retorno, str(aDistribuir,``'999999999,99'``)));`  `SetVar(Retorno,Concat(Retorno,``';'``))`  `Ate ItemEmp = TotEmp`  `Senao`  `repita`  `SetVar(ItemEmp,ItemEmp + 1);`  `Se ItemEmp = TotEmp`  `Entao`  `SetVar(aDistribuir,MaxEmp-saldodist)`  `Senao`  `SetVar(aDistribuir,  (MaxEmp / SaldoTot ) * InfEmp( ItemEmp,``'SALDODEVEDOR'` `) );`  `SetVar(aDistribuir,val( str(aDistribuir,``'999999999,99'``)))`  `FimSe;`  `SetVar(saldodist, saldodist + aDistribuir);`  `SetVar(Retorno, Concat(Retorno, InfEmp( ItemEmp,``'CODIGO'` `)));`  `SetVar(Retorno,Concat(Retorno,``':'``));`  `SetVar(Retorno, Concat(Retorno, str(aDistribuir,``'999999999,99'``)));`  `SetVar(Retorno,Concat(Retorno,``';'``))`  `ate ItemEmp = TotEmp`  `FimSe`  `FimSe;`    `Retorno` |

2. Nos parâmetros da rescisão, deverá marcar a opção abaixo que te atende e informar o código da fórmula cadastrada:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14558780751639)  
  
3. Após o cálculo da rescisão, o valor do empréstimo será lançado na ficha financeira do funcionário.

**Saiba Mais**[Lançamento de Empréstimo na Rescisão - Fórmula](https://tdn.totvs.com/pages/releaseview.action?pageId=540889290)
