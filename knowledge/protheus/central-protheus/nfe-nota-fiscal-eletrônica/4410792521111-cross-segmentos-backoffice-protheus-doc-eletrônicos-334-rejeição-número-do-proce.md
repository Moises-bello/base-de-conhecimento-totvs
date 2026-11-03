---
article_id: 4410792521111
category: NFe - Nota Fiscal Eletrônica
content_hash: f06b984a19dd4763679405477f7ea13bff5db2fe93b51250815bfcba9e224ec4
fetched_at: '2026-06-28T22:40:00.499324+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 334 Rejeição:
  Número do processo de drawback não informado na importação '
type: support-article
updated_at: '2021-10-15T13:56:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410792521111--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-334-Rejei%C3%A7%C3%A3o-N%C3%BAmero-do-processo-de-drawback-n%C3%A3o-informado-na-importa%C3%A7%C3%A3o
---

**Dúvida**Como solucionar a rejeição 334 Rejeição: Número do processo de drawback não informado na importação ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Para todos os itens com os CFOP 3127 ou 3211, o campo CD5\_ACDRAW deve ser preenchido na rotina de Complementos do Livro Fiscal, gerando a tag <nDraw>20140048618</nDraw> preenchida no XML. 

* **Exemplo:**

![ndraw.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4410784805015/ndraw.JPG)

1- Verifique se o CFOP da nota está correto no TES **Cod. Fiscal "F4\_CF"** Para todos os itens com os **CFOP 3127 ou 3211 realizar o procedimento abaixo.**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060423754/mceclip1.png)**

**2-** Quando **não usa integração** com o **módulo SIGAEIC é necessário que o parâmetro MV\_EASY= N**

**![20201201_145829.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360101037393/20201201_145829.gif)**

**3-** Acesse a rotina ****Livros Fiscais**-> **Atualizações**->**Movimentos**->**NF manual de Entrada**->**Outras ações**->**Complementos**->**Importação:****

****![20201201_145142.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360101036933/20201201_145142.gif)****

4 - Fazer o complemento de **importação nos Livros fiscais e preencher o campo** **CD5\_ACDRAW**

![ndraw.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4408778619927/ndraw.gif)

* **Saiba mais:**

Na **nota técnica 2020.005** o campo  passa a ser **Alfanumérico e a quantidade de caracteres permitida aumentou para até 20.**

[Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=624111487)

* Para que o campo seja **Alfanumérico é necessário realizar as atualizações do link abaixo:**

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Nota técnica 2020.005](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052495714)

* **Validação da Sefaz:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410784832919/mceclip0.png)**
