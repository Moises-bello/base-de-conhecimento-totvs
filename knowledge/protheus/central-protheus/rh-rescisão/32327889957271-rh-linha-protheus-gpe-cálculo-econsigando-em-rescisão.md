---
article_id: 32327889957271
category: RH - Rescisão
content_hash: 0aeee798aaff907cc2d6fd6e338cdd450888f7c634c43c25bdd106477c74ace6
fetched_at: '2026-06-28T22:43:48.548862+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo eConsigando em rescisão
type: support-article
updated_at: '2025-11-05T15:06:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32327889957271-RH-Linha-Protheus-GPE-C%C3%A1lculo-eConsigando-em-rescis%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32327889928599) Tempo aproximado para leitura: **00:02:30 min**  
  
**Dúvida**  
Como conferir cálculo eConsignado em rescisão?  
  
**Ambiente**  
TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução**

Para realizar o cálculo da rescisão com empréstimo consignado referente ao programa de Crédito do trabalhador, realize os seguintes passos:

1. Realizar a importação da parcela para valores futuros ou realizar o lançamento da verba de natureza 9253, para saber como realizar a importação do arquivo acesse a aba "Importação do Arquivo";  
   ![](https://tdn.totvs.com/download/attachments/944703898/image-2025-5-15_12-41-48.png?version=1&modificationDate=1747398217187&api=v2)
2. Após a verba de natureza 9253 ser lançada nos valores futuros, realize o cálculo da rescisão;  
   ![](https://tdn.totvs.com/download/attachments/944703898/image-2025-5-15_12-37-48.png?version=1&modificationDate=1747398217007&api=v2)

   Observação

   No cenário apresentado, foi descontado o valor total da parcela pois não atingiu o limite de 35%.  
     
   Para o correto funcionamento do cálculo limitando o valor da margem consignável, os mnemônicos P\_PERCONS e P\_LIMECONS deverá estar configurados.

   Desconto na Rescisão

   Diferente do tratamento dispensado aos outros empréstimos consignados, onde a quitação é feita na rescisão (limitada ao percentual definido no mnemônico P\_PERCONS), o consignado relativo ao Programa Crédito do Trabalhador não será quitado na ocasião da rescisão, sendo descontada apenas a parcela do mês, limitada ao percentual definido no P\_PERCONS se configurado.

**Importante**

Caso tenha sido feito cálculo de **adiantamento antes** do cálculo da rescisão, e nele foi feito o **provisionamento** do **eConsignado**, é necessário **fechar** o **ADI** para que na rescisão seja devolvido o valor provisionado.   
Caso não seja possível fechar o roteiro ADI, a verba de ID 1975, deve ser lançada manualmente no calculo da rescisão.  
Certifique-se que a configuração das verbas de provisionamento no adiantamento estejam configuradas corretamente conforme [documentação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32292447017239-RH-Linha-Protheus-GPE-Como-cadastrar-as-verbas-de-Provisionamento-nas-F%C3%A9rias-e-Adiantamento-referente-ao-eConsignado-Programa-Cr%C3%A9dito-do-Trabalhador) **antes** de realizar o fechamento do ADI.

**Saiba Mais**

Central de Faq's [eConsignado (Crédito do Trabalhador)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/32292829000215-eConsignado-Cr%C3%A9dito-do-Trabalhador)  
Manual Protheus [Crédito do Trabalhador](https://tdn.totvs.com/pages/viewpage.action?pageId=944703898)
