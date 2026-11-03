---
article_id: 360052213513
category: RH - Calculo Autonomo/Prolabore
content_hash: 4a77e76c796f33dbd2a9a9f5d365c79e090753ad106f38ac847af8d8ec45cd98
fetched_at: '2026-06-28T22:43:15.259445+00:00'
product: protheus
section_id: 360011983113
source: central-protheus
title: RH - Linha Protheus - GPE - Como configurar o INSS Parte Empresa de Pro-labore/Autônomo
  quando o percentual for diferente de 20%
type: support-article
updated_at: '2025-04-15T17:53:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052213513-RH-Linha-Protheus-GPE-Como-configurar-o-INSS-Parte-Empresa-de-Pro-labore-Aut%C3%B4nomo-quando-o-percentual-for-diferente-de-20
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25141141430551)**Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Como configurar o INSS Parte Empresa de Pró-labore/Autônomo quando o percentual for **diferente de 20%?**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão Pessoal -  A partir da Versão 12.1.17  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

1. Para os Tipos de Contrato 1 e 2 é utilizado a **Tabela S037**, onde informamos os percentuais e configurações conforme a necessidade da empresa.  
  
 2. Quando o cálculo é referente à Pro-Labore ou Autônomo, o sistema atribui o percentual cadastrado na verba de identificador **0221**. 

![image2018-1-17_14-38-24.png](https://tdn.totvs.com/download/attachments/331845588/image2018-1-17_14-38-24.png?version=1&modificationDate=1516207640000&api=v2)  
  
 3. O sistema sempre respeitará o percentual informado na verba quando for diferente de 0 ou 100.

![image2018-1-17_14-45-4.png](https://tdn.totvs.com/download/attachments/331845588/image2018-1-17_14-45-4.png?version=1&modificationDate=1516207640000&api=v2)

Base de Calculo: R$ 1800,00 x 22,5% = R$ 405,00 (Parte Empresa)  
  
**Obs.:** Se por ventura tiver diferentes percentuais de acordo com suas empresas/filiais, o cadastro de verbas deverá ser exclusivo por empresa/filial. Além disso, caso a empresa seja do Simples ou por qualquer particularidade interna entenda que não deve gerar a verba de INSS Empresa, **deixar o percentual da verba como 0.**

**Saiba Mais:**

[RH - Calculo Autonomo/Prolabore](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983113-RH-Calculo-Autonomo-Prolabore)
