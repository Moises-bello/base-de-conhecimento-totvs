---
article_id: 8589364871575
category: Fiscal Arquivos Magnéticos - Ressarcimentos
content_hash: d497fc29b23c6cbcdf327fb2ac34619b50bd1bdc94e16ce3c93b4f12d98d1e35
fetched_at: '2026-06-28T22:42:12.603741+00:00'
product: protheus
section_id: 1500001546642
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS -   Arq. Magnéticos -  Como gerar
  o arquivo de Ressarcimento do Estado do Amazonas
type: support-article
updated_at: '2024-05-03T19:02:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8589364871575-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-o-arquivo-de-Ressarcimento-do-Estado-do-Amazonas
---

**Dúvida**

Ressarcimento Estado do Amazonas.   
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.25**  
  
**Solução**

Com base na **resolução Nº 005/2019-GSEFAZ** institui o **"Sistema de Pedido Eletrônico de Ressarcimento do ICMS retido por substituição tributária ou recolhido por antecipação com encerramento da fase de tributação – Ressarcimento Eletrônico”.** Essa resolução solicita ao **contribuinte do Estado do Amazonas** o envio dos pedidos de **Ressarcimento**, através de arquivos de Lista de Pedidos e Lista de Produtos no **formato XML**, onde será enviado através do acesso ao portal <https://online.sefaz.am.gov.br/inicioDte.asp>.

![image2020-2-22_11-50-52.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8589430348183)

Para atender a legislação acima, foi implementado a rotina **FISA235 - DT-e Ressarcimento ICMS ST**, para a geração de 2 arquivos no **formato XML** onde o contribuinte precisa enviar através do **portal DT-e.**

Como premissa o envio de pedido precisa ter seus registros de ressarcimentos do **SPED ICMS IPI**  gerado e entregues.

No **Protheus** a geração do registro de ressarcimento pode ser realizados de 3 formas:

1. Utilizando a rotina de Ressarcimento de **ICMS ST (FISA132);**
2. Utilizando o ponto de entrada **MATUCOMP** para realizar alterações automáticas nos complementos dos documentos fiscais após a emissão dos documentos de saída;
3. Utilizando a Rotina de Complemento de Ressarcimento (**MATA926**).

Segue *link* com documentos de referencia para geração os Registros:

* <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010169092-REGISTRO-C176-C177-C178-e-C179>
* <https://tdn.totvs.com/pages/releaseview.action?pageId=539532642>
* [FIS0009\_Manual\_Utilização\_SPEDFISCAL](https://tdn.engpro.totvs.com.br/pages/viewpage.action?pageId=238035285)
