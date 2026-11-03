---
article_id: 360027852531
category: Escrita Fiscal - Impostos - Cálculos
content_hash: ab4787d7e26a317ac45bd9b9fd758096f6af349269635ba4b33bdcc9a8ab0829
fetched_at: '2026-06-28T22:39:30.538814+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como gerar o crédito
  sobre o estoque  VAREJISTA - REGRA 01?
type: support-article
updated_at: '2021-07-29T14:03:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027852531-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-gerar-o-cr%C3%A9dito-sobre-o-estoque-VAREJISTA-REGRA-01
---

**Dúvida**

Como gerar o crédito sobre o estoque VAREJISTA - REGRA 01  
  
**Ambiente**

Protheus - Fiscal - A partir da versão 12.1.16.  
  
  
**Solução**

No meu exemplo usei a data de fechamento em 31/12/2018, conforme a Lei 28/02/2019

**Data do parâmetro  
MV\_ULMES =20181231  
Sb9  
  
![](https://totvssuporte.zendesk.com/attachments/token/E7RTfAUhH4nvCaBqEOCkWvDON/?name=inline18986026.png)​  
  
Cadastro do produto**Alterar o campo

B1\_clasfis = 60

No SB5 **![](https://totvssuporte.zendesk.com/attachments/token/JL5b7HPvHzyPBmkfqGwBDAL6U/?name=inline-1140614774.png)​  
Gerar o matr460  
Gerar o relatório de Registro de inventário - Modelo P7 com o parâmetro configurado como demostrado a seguir:**

1. **Gerar Exp. SPED FISCAL** =  SIM
2. **Data de fechamento de estoque** = Data do arquivo de Inventario, de quando foi fechado.
3. **Arquivo Exp. Spedfiscal**= Informe o nome do arquivo com mesma data a ser informado na **Data de fechamento do estoque** - Informe a data em que foi feito o fechamento do estoque, caso queira gerar os registros de inventário.

**Fisa116**

Somente é gerado com a regra 5 - o credito do estoque **![](https://totvssuporte.zendesk.com/attachments/token/Hx54h0T3ShgoS0hLd8tEtAwOS/?name=inline397145024.png)​  
  
![](https://totvssuporte.zendesk.com/attachments/token/30sRKGuGtp5432BucqV6XYpdN/?name=inline-1207297354.png)​  
​​  
  
Fisa196  
​![](https://totvssuporte.zendesk.com/attachments/token/5lEmc8JBuxjRVfedqgharQxld/?name=inline1433163310.png)​  
  
![](https://totvssuporte.zendesk.com/attachments/token/AheAz28kwz33AcIxLFJfpunEI/?name=inline1104392380.png)​  
![](https://totvssuporte.zendesk.com/attachments/token/BeAHd4pEPglaRmyEi8DlJKUJA/?name=inline-1948307312.png)**
