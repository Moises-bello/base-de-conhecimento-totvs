---
article_id: 360045670593
category: Comércio Exterior - Easy Export Control - Financeiro
content_hash: f3636a15a92179dc7237b483711335083b6f5802eb9d46f26354af15396ff808
fetched_at: '2026-06-28T22:36:58.116854+00:00'
product: protheus
section_id: 1500001538221
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Configuração dos
  Parâmetros MV_AVG0214 e MV_AVG0213
type: support-article
updated_at: '2022-03-03T12:39:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045670593-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Configura%C3%A7%C3%A3o-dos-Par%C3%A2metros-MV-AVG0214-e-MV-AVG0213
---

**Dúvida**Como configurar os parâmetros: MV\_AVG0214 e MV\_AVG0213 para quebra ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões.  
  
**Solução** **Cenário 1:** Parâmetro MV\_AVG0214 habilitado e MV\_AVG0213 desabilitado.  
A rotina  cria parcelas de acordo com os valores informados.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062555274/mceclip0.png)  
  
**Cenário 2:**Parâmetro MV\_AVG0214 desabilitado e MV\_AVG0213 habilitado.  
A rotina irá manter o título no Financeiro e realizar a baixa parcialmente no mesmo título, porém na rotina Câmbio (EECAF200) irá realizar a quebra das parcela para a baixa.   
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063448273/mceclip4.png)  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062559914/mceclip5.png)  
  
A diferença de utilizar o parâmetro  MV\_AVG0214  desabilitado é que ao utilizar uma condição de pagamento com parcelas que a numeração dos títulos das parcelas serão diferentes.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062777434/mceclip0.png)

**Cenário 3:**Parâmetro MV\_AVG0214 habilitado e MV\_AVG0213 habilitado.  
A rotina irá manter o título no Financeiro e realizar a baixa parcialmente no mesmo título, porém na rotina Câmbio (EECAF200) irá realizar a quebra das parcela para a baixa.   
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063448273/mceclip4.png)  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062559914/mceclip5.png)

Mais informações acesse o link: [TFRGST\_DT\_Melhorias na Integração EEC x FIN](https://tdn.totvs.com/pages/releaseview.action?pageId=267782634)
