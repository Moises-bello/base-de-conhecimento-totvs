---
article_id: 38282318934039
category: NFSE - Nota Fiscal de Serviço Nacional
content_hash: c3d34353ad4e36cfc1824c5520a1d6805b3e9bc9e39b76457a7809329cd3c954
fetched_at: '2026-06-28T22:39:54.387128+00:00'
product: protheus
section_id: 33955617231639
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Dados da
  Obra no XML (Emissor Nacional)
type: support-article
updated_at: '2026-02-12T19:47:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38282318934039-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Dados-da-Obra-no-XML-Emissor-Nacional
---

**Dúvida**  
Como gerar no XML modelo nacional as informações do bloco <obra>?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Solução**  
Atualmente dentro do bloco <obra> há três grupos: <cObra>, <inscImobFisc> e <end>, os quais só podem ser gerados de forma individual, caso contrário (de forma conjunta) ocorrem rejeições.  
  
Para monta-los, segue detalhes de cada um:  
  
**<cObra>**  
Através do preenchimento somente do campo **C5\_OBRA** no Pedido de Vendas.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/38282318900631)  
  
**<inscImobFisc>**  
Através do preenchimento somente do campo **C5\_ARTOBRA** no Pedido de Vendas.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/38282311554711)  
  
**<end>**  
Somente para essa opção, será através da configuração do parâmetro **MV\_XMLOBRA** e os campos C5\_OBRA/C5\_ARTOBRA em branco.  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/38282311556503)**  
  
O parâmetro deverá ser configurado conforme exemplo, abaixo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/38282311557399)  
  
**Tipo**: Caractere  
**Conteúdo**: {'C5\_LOGR','C5\_COMPLOG','C5\_NUMLOGR','C5\_BAIRRO','C5\_CEP',,,,,,,,,,}  
  
Onde os campos deverão ser criados na tabela SC5, todos com o tipo 'Caractere' e tamanho de acordo com cada conteúdo, exemplo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/38282311559447)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/38282318911639)  
  
Após isso, os **campos criados deverão ser preenchidos no Pedido de Vendas (SC5)** para refletir no XML transmitido.
