---
article_id: 360058863393
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 4046a34e0bb6403a49470c98a1bc07d2f466374d8aae801a74f3c7b5f551fdad
fetched_at: '2026-06-28T22:42:03.869462+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: MP - SIGAFIS - Redução (CST 020) a 100% - Escrituração Correta do Registro
  C190 Nota de Saída.
type: support-article
updated_at: '2021-04-28T14:24:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058863393-MP-SIGAFIS-Redu%C3%A7%C3%A3o-CST-020-a-100-Escritura%C3%A7%C3%A3o-Correta-do-Registro-C190-Nota-de-Sa%C3%ADda
---

**Dúvida**

Qual a tratativa para levar ao Sped Fiscal o preenchimento correto do campo C190 - saída, para os casos de redução (cst 020) a 100%, pois ocorre de vir preenchido somente o valor da operação e faltou o preenchimento do campo valor não tributado.  
  
**Ambiente**

Protheus – Livros Fiscais – A partir da versão 11.80

**Solução**

Procedimento passo a passo para correta escrituração do Registro C190 - Redução 100% para CST 020.

1 - Alteração dos Campos via Configurador: **F4\_BASEICM / F7\_BASEICM / CD2\_PREDBC** de 5 para 6;  
  
![](https://totvssuporte.zendesk.com/attachments/token/BaTEbOooCE5TNgXRuoUpKdhzu/?name=inline-239308046.png)  
  
![](https://totvssuporte.zendesk.com/attachments/token/OJfCVHgPwxtv1RsjqOGZVcUb0/?name=inline-2003145784.png)  
  
![](https://totvssuporte.zendesk.com/attachments/token/0RApve07tX50nC9EHGHUwuKx5/?name=inline1720617598.png)​

2 - Configuração do Parâmetro **MV\_NRPRBIC =** .T.;  
  
![](https://totvssuporte.zendesk.com/attachments/token/Q98GM2xSwFG06AS1px7MGgS2m/?name=inline1563796238.png)

3 - Configuração do **TES**;  
  
![](https://totvssuporte.zendesk.com/attachments/token/dPGIXXzKFufcL0pN98wArmLmV/?name=inline-737708374.png)​  
  
4 - Documento de entrada com exemplo, note que na aba de **impostos** só contem o imposto IRRF;  
  
![](https://totvssuporte.zendesk.com/attachments/token/gjXP4AFJTMFFdoVR9ZKL1CSg4/?name=inline639439784.png)​  
  
5 - Porem na Aba de **Livros Fiscais**, contem o **Valor Contábil** de R$1000,00 e o valor da Redução no campo **ICMS Outros**, também no valor de R$ 1000,00​​;  
  
![](https://totvssuporte.zendesk.com/attachments/token/sI9fvfM1wv9cjIsgKyzDej7kS/?name=inline455377265.png)​  
  
6 - Geração do **SPED FISCAL**;  
  
![](https://totvssuporte.zendesk.com/attachments/token/AY8KEYqB0Q3CjqhVTdqT5orjT/?name=inline-2141013997.png)​  
  
                                                                              
7 - Realizar todo o processo em **Ambiente de Homologação**, antes de realizar em **Ambiente de Produção;**
