---
article_id: 360045209473
category: MDFe - Manifesto de Carga
content_hash: 940164eb0a9396630d8b6ffd15268565b886af6dc0912e0de2ecb49b3fa1a0fb
fetched_at: '2026-06-28T22:40:08.158153+00:00'
product: protheus
section_id: 1500001549242
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - MDFE -  Como gerar
  a TAG com código CIOT
type: support-article
updated_at: '2025-06-17T18:00:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045209473-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-MDFE-Como-gerar-a-TAG-com-c%C3%B3digo-CIOT
---

**Dúvida**Como gerar a **TAG** com código **CIOT**?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - Todas as versões   
  
**Solução**1. Acesse a rotina de **MDF-e:** Módulo ***Faturamento - SIGAFAT** > **Atualizações** > **NF-e e NFS-e** > **MDF-e - SPEDMDFE**,* após informar os filtros da tela, clicar no botão***Incluir**.*

![](https://tdn.totvs.com/download/attachments/544179262/image2020-3-16_13-44-27.png?version=1&modificationDate=1584377067876&api=v2)

2. Realizar todos os preenchimentos necessários como seleção de ***documentos, municípios de carregamento e etc.***

![](https://tdn.totvs.com/download/attachments/544179262/image2020-3-16_13-46-19.png?version=1&modificationDate=1584377179668&api=v2)

![](https://tdn.totvs.com/download/attachments/544179262/image2020-3-16_13-47-44.png?version=1&modificationDate=1584377264505&api=v2)

3. Após o  preenchimento das informações anteriores, clicar na aba **CIOT**,  informar os dados referente ao CIOT, tais como ***Número de CIOT** e **CPNJ/CPF do Contratante/Subcontratante**.* Em seguida, clicar no botão **Salvar**.

![](https://tdn.totvs.com/download/attachments/544179262/image2020-3-16_13-47-53.png?version=1&modificationDate=1584377273953&api=v2)

4. Logo após salvar o documento e realizar a transmissão do mesmo, para isso clicar em ***Outras ações / Gerenciar MDF-e**.*

![](https://tdn.totvs.com/download/attachments/544179262/image2020-3-16_13-50-57.png?version=1&modificationDate=1584377457187&api=v2)

5. Em seguida clicar em ***Outras Ações /****Transmitir.***

![](https://tdn.totvs.com/download/attachments/544179262/image2020-3-16_13-51-20.png?version=1&modificationDate=1584377480616&api=v2)

6. Informar o número do documento a ser transmitido e avançar no wizard de transmissão até sua finalização.

![](https://tdn.totvs.com/download/attachments/544179262/image2020-3-16_13-51-58.png?version=1&modificationDate=1584377518482&api=v2)

![](https://tdn.totvs.com/download/attachments/544179262/image2020-3-16_13-52-31.png?version=1&modificationDate=1584377551320&api=v2)

7. Em seguida, realizar o monitoramento do documento em **Outras Ações / Monitorar.**

![](https://tdn.totvs.com/download/attachments/544179262/image2020-3-16_13-53-7.png?version=1&modificationDate=1584377588014&api=v2)

8. Será apresentada tela com os status do documento monitorado.

![](https://tdn.totvs.com/download/attachments/544179262/image2020-3-16_13-53-35.png?version=1&modificationDate=1584377615835&api=v2)

9. Clicar no botão *Schema* para visualizar o **XML** do documento com as novas tag referentes ao **CIOT**

![](https://tdn.totvs.com/download/attachments/544179262/image2020-3-16_13-54-24.png?version=1&modificationDate=1584377664301&api=v2)

Segue trecho do **XML** com a **TAG** preenchida.

![](https://tdn.totvs.com/download/attachments/544179262/Screenshot_1.jpg?version=1&modificationDate=1584447678771&api=v2)

Pronto! No seu **MDF-e** os dados referentes ao **CIOT** foram enviados com sucesso.

**Importante**: As informações referente ao CIOT estão sendo destacadas somente no **XML.** Caso necessária sua impressão no **DAMDFE**, por favor informar o numero do **CIOT** também no campo **Informações Adicionais** presente na aba**Outros** do cadastro da **MDF-e**.

**LEMBRANDO:  NÃO vai destacar no DAMDFE campo próprio para o CIOT.**

***Conforme no Manual o mesmo não possui campo especifico no LAYOUT do DAMDFE***
