---
article_id: 23670622559511
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 2fa9b1e17b0650a4aa753d701b9985fc9aad3db4caf9bca6684559a28a5061c8
fetched_at: '2026-06-28T22:42:05.026430+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Como gerar os
  Registros M110, M115, M510 e M515, referentes aos ajustes do Bloco M do EFD Contribuições.
type: support-article
updated_at: '2024-05-22T18:42:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23670622559511-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-os-Registros-M110-M115-M510-e-M515-referentes-aos-ajustes-do-Bloco-M-do-EFD-Contribui%C3%A7%C3%B5es
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23670615708695) Tempo aproximado para leitura: **00:05:00 min.** **Dúvida**Como gerar os Registros **M110, M115, M510 e M515,** referentes aos ajustes do **Bloco M** do **EFD Contribuições**.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões

**Solução**

Os registros **M110, M115, M510 e M515** do **EFD Contribuições** tratam as **Devoluções de Compras** com **PIS** e **COFINS**, quando a **Nota Fiscal**, devolvida for do período anterior à nota de devolução.  
Quando a **Nota Fiscal** de **Devolução** é no mesmo período da **Nota Fiscal** devolvida, as informações serão demonstradas nos **Registros C100/C170 (informação individualizada)**, seja nos **Registros C190** **e filhos** **(informação consolidada)**.  
  
As **Devoluções de Compras** devem ser configuradas conforme o link abaixo:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016325831-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Devolu%C3%A7%C3%A3o-de-compra-dentro-e-fora-do-per%C3%ADodo-de-emiss%C3%A3o-da-Nota-Fiscal-de-origem-no-Regime-N%C3%A3o-Cumulativo?source=search>

*Print* tela Apuração:

![kcs devolucao compra.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/23671921644695)

Importante:  
- Você pode **clicar 2 vezes** sobre o **valor do Ajuste** para visualizar a **origem do Ajuste**.  
- O **valor do Ajuste** será gerado na **Apuração**, sempre que existir **valor de crédito** dentro do **mesmo período** para abater.  
- Após confirmar a **Apuração** as **Tabelas CLA** **(Registros M110 M510)** e **tabela CL4 (Registros M115 M515)** serão gravadas.  
- Com as informações corretas nas tabelas **CLA e CL4** os Registros **M110, M115, M510 e M515,** serão gerados no **Arquivo txt**, referente ao **Ajuste da Devolução**.
