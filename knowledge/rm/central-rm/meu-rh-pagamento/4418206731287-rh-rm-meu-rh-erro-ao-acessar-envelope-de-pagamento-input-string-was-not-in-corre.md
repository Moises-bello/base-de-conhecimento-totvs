---
article_id: 4418206731287
category: Meu RH - Pagamento
content_hash: 49bead55ee4d1fb48dd9ccabc2f112527e4215e7de1532a9db09de43df5ec158
fetched_at: '2026-06-28T22:47:33.889567+00:00'
product: rm
section_id: 1500000835221
source: central-rm
title: RH - RM - Meu RH - Erro ao acessar envelope de pagamento, input string was
  not in correct format
type: support-article
updated_at: '2025-02-03T19:45:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418206731287-RH-RM-Meu-RH-Erro-ao-acessar-envelope-de-pagamento-input-string-was-not-in-correct-format
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29721341501847) Tempo aproximado para leitura: **00:01:50 min****Ocorrência**Quando acessar a tela de envelope de pagamento no Meu RH, é retornada a mensagem : **Ocorreu um erro ao efetuar a leitura da visão: Input string was not in a correct format.**

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas as versões  
  
**Causa**  
Esse incidente ocorre, pois está utilizando um separador diferente  **; ( ponto e virgula )** no campo "não visualizar o demonstrativo de pagamento nos seguintes períodos, dentro dos parâmetros demonstrativos de pagamento no grupo de quiosque. 

![erro.jpeg](https://centraldeatendimento.totvs.com/hc/article_attachments/7938864173463)  
  
**Solução**

Para solucionar essa ocorrência, realize o procedimento:

Acessar Folha de pagamento | Configuração | Parametrizador | RM Portal | Editar o grupo de quiosque do colaborador | Demonstrativo de pagamento | Verifique o campo "não visualizar o dem.de pagamento nos seguintes períodos, se está utilizando o separador ; ( ponto e virgula ) **caso esteja utilizando em outro formato, deve ser alterado.**

![](https://p23.zdusercontent.com/attachment/888110/swBSe69Bs94Q7owMhNRI7dLsq?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..AU3hVoM0Ylq4eJhKPi4JNA.mGwfPrR3erpB-7noQ8xKo5N1GBt5NGirUBcvqDxqvmU8AuCRIrHW9vIe_CwykWZlI0aOH8WmMYbKx7tEXfAEXgAWAvGVoQq6AT_vLuJ5VBBJATcpq2wESNeHyo7x_0xxFBfW0_Ss_ZbE7lWhYLk6atDT2gAXftbi6NOmSpkVWtYpwcAPX0Gw9wMXY-ifXN0T94keWq2sb-S70ZPa1goTaRQGEWBdNDrpKz0pwDnBRdBvYYfxU89QYgL3hK-YR8HKgy_8oTxfuOq68pAsF_CnqPZr3bokRnI8OXCxnr7u7gw.K3FCxZHjvbORPbzXDUdpCQ)
