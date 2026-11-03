---
article_id: 360047426174
category: RH - Recibos e Cheques
content_hash: ba1b71f6d8c981269b7a4a748453356acb41a819204edc34c51eec4f7af6506e
fetched_at: '2026-06-28T22:43:29.616458+00:00'
product: protheus
section_id: 360011909573
source: central-protheus
title: RH - Linha Protheus - GPE - Impressão de recibo de pagamento em impressora
  matricial
type: support-article
updated_at: '2021-06-07T14:14:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047426174-RH-Linha-Protheus-GPE-Impress%C3%A3o-de-recibo-de-pagamento-em-impressora-matricial
---

**Dúvida**Como realizar a impressão de recibo de pagamento em impressora matricial?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução** **1.** Na rotina Recibo de Pagamento (GPER030), o campo Pre Imp/Zebrad/Mail? deve ser preenchido com Pre-Impressao conforme abaixo (as demais perguntas serão preenchidas de acordo com a necessidade de impressão do cliente):  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070387333/mceclip0.png)  
  
**2**. Na aba Impressão, parametrizar conforme abaixo e escolher a sua impressora matricial:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070387733/mceclip1.png)  
  
**3**. Confirme a impressão,, será impresso conforme abaixo:  
![](https://tdn.totvs.com/download/attachments/225950253/PRE%20IMPRESSO.jpg?version=1&modificationDate=1456827577000&api=v2)  
  
**OBSERVAÇÕES IMPORTANTES:**

* O sistema imprime em matricial, holerite modelo lab 02 em formulário contínuo padrão com ou sem carbono;
* No sistema Protheus as portas utilizadas são LPT e COM;
* Configuração da impressora via Use Net: <https://tdn.totvs.com/pages/viewpage.action?pageId=227541038>
* A matricial tem que ser obrigatoriamente com entrada paralela e não pode ser utilizado adaptador *USB;*
* Os fontes RECIBO.prx e GPER030, bem como o Binário precisam estar atualizados;
* Se houver a opção "Draft Condensado" na impressora, deverá ser escolhido este formato de impressão.

**Saiba mais:**  
Appserver: <https://suporte.totvs.com/portal/p/10098/download#000006/368/TFAPP/>  
SmartClient: <https://suporte.totvs.com/portal/p/10098/download#000006/368/TFSC/>
