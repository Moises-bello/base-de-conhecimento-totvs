---
article_id: 1500008686801
category: RH - Folha de Pagamento
content_hash: 6d236e530a9d4fcf5f6e4c261ddc948997c845afb66bfd7c8b89726b336bbbc5
fetched_at: '2026-06-28T22:44:13.245556+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como conferir INSS salário e INSS férias em cálculo
  de folha de pagamento quando existe férias partidas e o parâmetro MV_DINSSFM = N
type: support-article
updated_at: '2025-10-07T11:15:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008686801-RH-Linha-Protheus-GPE-Como-conferir-INSS-sal%C3%A1rio-e-INSS-f%C3%A9rias-em-c%C3%A1lculo-de-folha-de-pagamento-quando-existe-f%C3%A9rias-partidas-e-o-par%C3%A2metro-MV-DINSSFM-N
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26236104275607) Tempo aproximado para leitura: **00:02:00 min**  
**Dúvida**Como conferir INSS salário e INSS férias em cálculo de folha de pagamento quando existe férias partidas (de um mês para o outro) e o parâmetro MV\_DINSSFM = N?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução**Para conferencia do INSS salário e INSS férias em cálculo de folha de pagamento quando existe férias partidas e o parâmetro MV\_DINSSFM = N, é necessário validar o valor total da Base INSS, separar o valor provento referente a salário e férias e por fim proporcionalizar o desconto de INSS com base nos valores separados.

**Exemplo:**

Cálculo das Férias

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19352831538071)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19352828898967)

**1** - Recibo de pagamento referente ao início das férias.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19352828919063)

No cálculo acima, a Base INSS total é no valor de **3.768,99**, tendo o desconto de INSS no valor de **355,32** (soma das verbas 417 e 418) conforme a tabela progressiva do INSS.

No calculo da folha de pagamento, o valor provento saldo de salário corresponde a **1.493,33** (verba 112) e o valor provento de férias corresponde a 2.275,56 (soma verbas 129 e 134).

**Deste modo o sistema realiza a seguinte proporção:**

1.493,33 \ 3.768,89 = 39,6225%

2.275,56 \ 3.768,89 = 60,3775%

355,32 \* 39,62% = 140,79 (INSS saldo salário)

355,32 \* 60% = 214,53 (INSS Férias)

**2** - Recibo de pagamento referente ao final das férias (mesmo conceito utilizado acima)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19352828930583)

No cálculo acima, a Base INSS total é no valor de 3.697,78, tendo o desconto de INSS no valor de 346,78 conforme a tabela progressiva do INSS.

No calculo da folha de pagamento, o valor provento saldo de salário corresponde a 1.706,67 (verba 112) e o valor provento férias corresponde a 1.991,11 (soma verbas 129 e 134).

**Deste modo o sistema realiza a seguinte proporção:**

1.706,67 \ 3.697,78 = 46,1539%

1.991,11 \ 3.697,78 = 53,8461%

346,78 \* 46,1539% = 160,06 (INSS saldo salário)

346,78 \* 53,8461% = 186,73 (INSS Férias)

**Importante**  
A indicação para configuração do id **0168** com **sim** para **IR** e o id **0065** com **não** para **IR.**  
Quando há o **recálculo** do INSS de férias na folha, ele pode ficar com valor **menor** que o calculado nas férias e gerar esta **diferença** de valor no id **0100** de forma **indevida.**

**Saiba mais:**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)  
[RH - Linha Protheus - GPE - Configuração do parâmetro MV\_DINSSFM](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016451652-RH-Linha-Protheus-GPE-Configura%C3%A7%C3%A3o-do-par%C3%A2metro-MV-DINSSFM)  
[RH - Linha Protheus - GPE - Conceito do cálculo de folha com Férias partidas utilizando o parâmetro MV\_DINSSFM= S](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017956652-RH-Linha-Protheus-GPE-Conceito-do-c%C3%A1lculo-de-folha-com-F%C3%A9rias-partidas-utilizando-o-par%C3%A2metro-MV-DINSSFM-S?source=search)  
[RH - Linha Protheus - GPE - Como conferir o INSS férias, quando o parâmetro MV\_DINSSFM esta com R e o funcionário teve férias partidas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019891371-RH-Linha-Protheus-GPE-Como-conferir-o-INSS-f%C3%A9rias-quando-o-par%C3%A2metro-MV-DINSSFM-esta-com-R-e-o-funcion%C3%A1rio-teve-f%C3%A9rias-partidas-?source=search)   
[MP - GPEM030 - MV\_DINSSFM = N, conferência do cálculo do INSS férias e folha](https://tdn.totvs.com/pages/viewpage.action?pageId=224449552)
