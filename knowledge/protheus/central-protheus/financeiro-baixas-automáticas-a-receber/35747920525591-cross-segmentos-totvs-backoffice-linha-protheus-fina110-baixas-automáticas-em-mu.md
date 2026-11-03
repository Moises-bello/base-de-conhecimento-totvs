---
article_id: 35747920525591
category: 'Financeiro - Baixas Automáticas a Receber '
content_hash: c575f0acb0b16a1023af7d4eee66496a2aaeea17a43651713b340fcc339da591
fetched_at: '2026-06-28T22:37:38.769430+00:00'
product: protheus
section_id: 35057325714199
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - FINA110 - Baixas automáticas
  em Multi-Filiais
type: support-article
updated_at: '2026-03-04T17:09:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35747920525591-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-FINA110-Baixas-autom%C3%A1ticas-em-Multi-Filiais
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35747920516631) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como funciona a baixa automática no processo de multifiliais? Como são apresentadas as filiais?  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
A rotina de **Baixa Automática (FINA110)**, ao exibir a seleção de filiais, apresenta todas as filiais vinculadas à empresa logada e, num ambiente com **SA6 com exclusividade**, apresentará somente os títulos da filial selecionada no momento da baixa antes da marcação, pois existe exclusividade de empresa ou unidades de negócios entre **SA6/SE5/FK5.**

Assim, caso a estrutura corporativa seja composta por **Empresas / Unidades de Negócio / Filiais**, ao acessar o sistema pela **empresa 01**, serão listadas somente as filiais associadas a essa empresa — não sendo exibidas as filiais pertencentes a outras empresas, como a **empresa 02**, por exemplo.

Para que sejam exibidas as filiais da empresa responsável pelo recebimento, é necessário **alterar para a empresa correspondente** antes de executar o processo, utilizando a **troca de módulo**.

Nos ambientes configurados para operação apenas por **filiais (Ambiente FF)**, o sistema apresentará **todas as filiais pertencentes ao grupo de empresas**.  
  
**Saiba mais**  
[FINA110 -Baixa Automática de Títulos a Receber](https://tdn.totvs.com/pages/releaseview.action?pageId=312167132)
