---
article_id: 360004979372
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 52d3b2a1d82bde09604eda45cae33c11e01ca0fc4061be6f2fb89e9fcd4e49a9
fetched_at: '2026-06-28T22:39:56.171560+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Como cancelar
  uma nota fiscal de serviço '
type: support-article
updated_at: '2025-06-02T12:20:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004979372-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Como-cancelar-uma-nota-fiscal-de-servi%C3%A7o
---

**Dúvida**Como cancelar (cancelamento)  uma nota fiscal de serviço  ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**Segue abaixo o passo a passo para realizar o Cancelamento de uma NFS-e:

**1.** Faça a exclusão do documento de saída através da rotina **MATA521A;  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067395113/mceclip0.png)****2.** Após isso acesse a rotina **FISA022**. Observe que a nota excluída anteriormente não será apresentada na tela;  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067395413/mceclip1.png)  
  
**3.** Vá em Outras **Ações -> Cancelamento;**  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067396013/mceclip2.png)  
  
**4.** O sistema apresenta os parâmetros abaixo para serem preenchidos:

*• Dt Inicial Canc: Informe a data inicial para busca das notas canceladas no sistema, data de exclusão do documento.*  
*• Dt Final Canc: Informe a data final para busca das notas canceladas no sistema.*  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360066333034/mceclip3.png)  
  
**5**. É apresentado um Browser com os documentos autorizados que foram excluídos no período solicitado. Selecione os documentos a serem transmitidos;  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360066333674/mceclip6.png)  
  
**6.** Clique em **Trans Canc**;  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360066333634/mceclip5.png)  
  
**7.** Quando o processamento é realizado de forma satisfatória, o sistema exibe uma tela contendo a mensagem de que a transmissão do Cancelamento foi concluída com sucesso;  
  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067396913/mceclip7.png)  
  
**8.** Após a transmissão do cancelamento, clique no X e volte para a rotina **FISA022** novamente. Feito isso, realize o monitoramento da nota através do menu **Outras Ações -> Monitor**  
  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067397673/mceclip8.png)  
  
**Observações:**- *Vale lembrar que o **Cancelamento de RPS não é disponibilizado por todas as prefeituras**.  
Poderá verificar a disponibilidade através da relação abaixo:*  
- [Municípios Homologados](http://tdn.totvs.com/pages/releaseview.action?pageId=4814340)

- Verificar se a nota autorizada foi monitorada antes de iniciar o procedimento, uma vez que **uma das premissas para transmissão de cancelamento é somente ser possível para notas previamente autorizadas.**
