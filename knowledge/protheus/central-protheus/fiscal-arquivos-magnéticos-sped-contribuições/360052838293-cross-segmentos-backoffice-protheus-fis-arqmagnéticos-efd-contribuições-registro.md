---
article_id: 360052838293
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 6430445ca0a5fc41777b1ca8791e2152967d49fd28fe7fa1f0e97ae40d289970
fetched_at: '2026-06-28T22:42:05.305918+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  - Registro tipo 0120 – Identificação de Períodos Dispensados da Escrituração Fiscal
  Digital  das Contribuições.
type: support-article
updated_at: '2023-01-25T19:58:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052838293-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Registro-tipo-0120-Identifica%C3%A7%C3%A3o-de-Per%C3%ADodos-Dispensados-da-Escritura%C3%A7%C3%A3o-Fiscal-Digital-das-Contribui%C3%A7%C3%B5es
---

**Dúvida**  
Registro tipo **0120** – Identificação de Períodos Dispensados da Escrituração Fiscal Digital das Contribuições.  
  
**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**  
O registro **0120** é tratado e poderá ser lançado através da rotina **Per. Disp. EFD-Contrib.** (**FISA089**) que alimentará a tabela **CKN** (**Per. Disp. EFD-Contr**).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Nome do menu** | **Submenu** | **Nome da rotina** | **Programa** | **Tabelas** |
| **Atualizações** | **Cadastro** | **Per. Disp. EFD-Contrib.** | **FISA089** | **CKN** |

**Procedimentos de Utilização**  
  
**1.**Acessar a rotina **Per. Disp. EFD-Contrib** e realizar o cadastro do Período Dispensado da **EFD Contribuições**.  
  
**2.**Gerar o arquivo do **EFD Contribuições** e verificar o **Registro tipo 0120** – Identificação de períodos dispensados da **Escrituração Fiscal Digital das Contribuições**.

Mais Informações, segue *link* do Boletim Técnico do **EFD Contribuições**:

<https://tdn.totvs.com/pages/releaseview.action?pageId=715144991>
