---
article_id: 360018403132
category: Escrita Fiscal - Impostos - ICMS - Difal
content_hash: f6ab6cd3b4d27ad6ee36319e72405759721e9f64f98536f828cea5d28988bf16
fetched_at: '2026-06-28T22:39:19.259757+00:00'
product: protheus
section_id: 1500001549902
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS -  Diferencial na Saída
  Para Cliente Contribuinte e DIFAL Para não Contribuinte
type: support-article
updated_at: '2024-11-19T20:18:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018403132-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Diferencial-na-Sa%C3%ADda-Para-Cliente-Contribuinte-e-DIFAL-Para-n%C3%A3o-Contribuinte
---

**Dúvida**

Como Calcular na Saída Diferencial para Cliente Contribuinte e Difal para Cliente Não Contribuinte?  
  
**Ambiente**Exemplo:  
Protheus - Fiscal – A partir da versão 12.1.17  
  
  
**Solução**

O Diferencial de Alíquota na Saída para Cliente Contribuinte será o Diferencial ST*:*

Informe no **Cadastro do Produto Campo:** Solid Saída ( B1\_PICMRET) ou da **Exceção Fiscal** Campo: Margem de Lucro (F7\_MARGEM)  o percentual de ICMS-ST (MVA) estabelecido por norma legal, caso não exista, informe um percentual fictício (por exemplo 0,01) somente para possibilitar o cálculo pelo diferencial:

**TES**

* **Calcula ICMS**(F4\_ICM) = SIM
* **L. FISC. ICMS** (F4\_LFICM) = TRIBUTADO
* **Calc Dif ICM**. (F4\_COMPL) = NÃO
* **MATL CONSUMO** (F4\_CONSUMO) = SIM
* **AGREGA SOLID.** (F4\_INCSOL) = SIM
* **MKP.ICM.COMP** (F4\_MKPCMP) = NÃO
* **MARG. SOLID.** (F4\_MKPSOL) = NUNCA (Indica que o sistema deve ignorar o MVA preenchido no produto ou exceção fiscal)
* **Ded.ICM.ST (F4\_ICMSTMT)** = 1-SIM ou 2-NÃO

  Se deixar Ded.ICM.ST (F4\_ICMSTMT) = 1-SIM, ele subtrai o valor do ICMS próprio do valor do Retido

  Se deixar Ded.ICM.ST (F4\_ICMSTMT) = 2-Não, ele Não subtrai o valor do ICMS próprio do valor do Retido

**CLIENTE** (SA1) deve ser um dos tipos preenchido no parâmetro **MV\_TPSOLCF**, o **CLIENTE** deve ser de um Estado diferente do emitente (**MV\_ESTADO**) e ter a Inscrição Estadual preenchida.

**IPI na Base (F4\_INCIDE):** Este campo permite informar se valor de IPI incide na base de ICMS. Para o exemplo a seguir o IPI entrou na base de cálculo do ICMS, desta forma pode ser definido como "Consumidor Final" ou como "Sim/Não

**BASE DUPLA**

Para tratar Base Dupla deverá configurar o parâmetro **MV\_UFBDST**informe os estados que devem ter base dupla para o ST e o cadastro do cliente/pedido de venda o tipo de cliente deve ser **CONSUMIDOR FINAL.**

**Obs: caso tenha que calcular DIFAL ST base dupla, para consumidor final não contribuinte, valide o parâmetro MV\_UFPST21.**

**As UFs que estiverem no parâmetro, a base do DIFAL ST será única.**

**Para ficar base dupla, retire a UF do parâmetro conforme necessidade.**

MV\_UFPST21 = AC/AL/AP/BA/CE/DF/ES/GO/MA/MT/PA/PB/PE/PI/SE/RN/RO/RR

Indique as UF’s destinatárias para as operações enquadradas na Confaz 21/2011.

--------------------------------------------------------------------------------------------------------------------

**O DIFAL na Saída para Cliente Não Contribuinte E.C 87/2015, configurar conforme abaixo:**

Para que seja realizado calculo de diferencial de alíquota para **CONSUMIDOR FINAL "**não contribuinte" é necessário configurar no cadastro de TES os campos:

* **Calcula ICMS (**F4\_ICM******)**= SIM
* **Calc. Difal (F4\_DIFAL)**= SIM
* **Calc.Dif.ICM (F4\_COMPL)**= SIM
* **MKP.ICM.COMP** (F4\_MKPCMP) = Sim

 

Desta forma será calculado e partilhado diferencial de alíquota nas notas de saída interestadual.

 

Para cliente  **consumidor final** **não contribuinte**, no cadastro de cliente o campo  **Insc. Estadual (A1\_INSCR)** pode ser preenchido como **ISENTO,**estar em **BRANCO**, ou preenchido com a**Inscrição Estadual**, e o campo **Contribuinte (A1\_CONTRIB)** deve ser preenchido com **NÃO**.

Para tratar a Base Dupla configure MV\_UFBASDP com a UF de destino.

***Boletim - Difal - Cliente Não Contribuinte:***

https://tdn.totvs.com/pages/releaseview.action?pageId=699815598
