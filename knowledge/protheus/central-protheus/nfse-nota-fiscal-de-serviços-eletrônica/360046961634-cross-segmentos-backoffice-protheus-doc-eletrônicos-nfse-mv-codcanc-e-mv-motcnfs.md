---
article_id: 360046961634
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 9508580a93061b1ea726edafba8d9be493be8e573d388318a267f1909e767811
fetched_at: '2026-06-28T22:39:57.554445+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - MV_CODCANC
  e MV_MOTCNFS (Códigos de Cancelamento)
type: support-article
updated_at: '2025-05-23T13:14:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046961634-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-MV-CODCANC-e-MV-MOTCNFS-C%C3%B3digos-de-Cancelamento
---

**Dúvida**Qual a função dos parâmetros MV\_CODCANC e MV\_MOTCNFS?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - Todas as versões  
 **Solução**Ambos os parâmetros tem a finalidade de informar o **Código de Cancelamento no XML** para quando é feito a transmissão de cancelamento de uma nota.  
  
A diferença é que habilitando apenas o **MV\_CODCANC**, será apresentado na rotina algumas opções padrões (chumbadas no fonte), que são as seguintes:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27651324267927)  
  
Caso seja necessário acrescentar manualmente um código e a sua descrição para que seja uma opção à ser selecionada nessa janela, deverá também habilitar o **MV\_MOTCNFS**, exemplo abaixo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27651308012695)  
  
Vale lembrar que os dois parâmetros **apenas irá salvar o Código de Cancelamento (campo CODCANC na SPED051)**. Já o motivo/descrição, servirá apenas como um apoio visual, onde o campo MOTCANC será sempre chumbado como 'Cancelamento de nota automatico', exceto quando configurado um outro parâmetro (MV\_INFXJUS), utilizado para definir o Motivo do Cancelamento.  
  
**Configuração dos parâmetros:** **Nome da Var**: MV\_CODCANC  
**Tipo**: 3 - Lógico  
**Conteúdo**: .T. (.F. para desabilitar a tela)  
**Descrição**: "Habilita a tela para selecionar o código de cancelamento da NFS-e"  
  
**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360069106693)**

**Nome da Var**: MV\_MOTCNFS  
**Tipo**: 1 - Carácter  
**Conteúdo**: Código "-" (Traço) Descrição do código, separados por "|" (Pipe)  
**Descrição**: "Código e descrição do motivo do cancelamento"  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/27651308013975)****Obs.: A rotina FISA022 deverá estar atualizada para contemplar essa configuração.**[- Clique aqui para baixar o pacote de atualização.](https://tdn.totvs.com/pages/releaseview.action?pageId=525010692)Mais detalhes:  
- <https://tdn.totvs.com/pages/releaseview.action?pageId=501481434>
