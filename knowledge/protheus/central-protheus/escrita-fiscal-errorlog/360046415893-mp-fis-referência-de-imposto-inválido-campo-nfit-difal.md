---
article_id: 360046415893
category: Escrita Fiscal - Error.log
content_hash: fa5e8e4ecdbc121a1ecb0b4684ac80f41b4cb226230896792b24cb260f72775e
fetched_at: '2026-06-28T22:39:32.937992+00:00'
product: protheus
section_id: 1500001549782
source: central-protheus
title: 'MP - FIS - Referência de Imposto Inválido - Campo NFIT_DIFAL '
type: support-article
updated_at: '2021-04-28T15:43:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046415893-MP-FIS-Refer%C3%AAncia-de-Imposto-Inv%C3%A1lido-Campo-NFIT-DIFAL
---

**Dúvida**  
Referência de Imposto Inválido - Campo NFIT\_DIFAL   
  
 **Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**O erro ocorre pois há alguma campo na estrutura SX3 com a validação incorreta, conforme demonstrado no erro: NFIT\_DIFAL   
  
Esta referência é inválida, sendo validas apenas NF\_DIFAL ou IT\_DIFAL.  
  
Será necessário efetuar um filtro na SX3 filtrando pelo campo X3\_VALID ou X3\_VLDUSER contendo a expressão NFIT\_DIFAL e verifique qual é o campo e qual a validação correta dele conforme a documentação abaixo que foi enviada pelo módulo específico:

<https://tdn.totvs.com/pages/releaseview.action?pageId=464972839>

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360065641193/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360064654674/mceclip1.png)
