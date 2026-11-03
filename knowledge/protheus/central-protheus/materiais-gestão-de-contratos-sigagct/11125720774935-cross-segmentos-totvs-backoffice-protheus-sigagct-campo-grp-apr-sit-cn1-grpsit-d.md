---
article_id: 11125720774935
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 69bc3532cff441f88c88aa79ed2b5cb0c146c3f101279b64ff2112274b4e7342
fetched_at: '2026-06-28T22:37:21.395182+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Campo "Grp Apr Sit"
  ( CN1_GRPSIT ) do Tipo de Contrato não habilita para alteração e não permite o seu
  preenchimento
type: support-article
updated_at: '2026-04-09T12:54:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11125720774935-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Campo-Grp-Apr-Sit-CN1-GRPSIT-do-Tipo-de-Contrato-n%C3%A3o-habilita-para-altera%C3%A7%C3%A3o-e-n%C3%A3o-permite-o-seu-preenchimento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22893953915799) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Campo "Grp Apr Sit" ( CN1\_GRPSIT ) do Tipo de Contrato não permite alteração ficando somente Visualização  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões]  
  
**Solução**  
O campo "Grp Apr Sit" **(*****CN1\_GRPSIT)*** é habilitado para preenchimento, ao colocar o campo anterior "Alçada Contrato " **(*****CN1\_ALCCTR*****)** como "0-Todos" ou 1-Documento.

Caso isso não aconteça, orienta-se a verificação das configurações do campo ***CN1\_GRPSIT*** no Configurador se estão com as mesmas configurações conforme o padrão, principalmente as configurações de ***"Propriedade"*** e ***"Modo Edição"***, mas também verificando as demais configurações do campo, conforme o padrão das imagens abaixo:  
E realizar o devido ajuste caso esteja diferente.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11125302943895)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11125304471063)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11125334512279)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11125336267799)

Também é aconselhado, o ambiente estar atualizado com os pacotes mais atuais dos módulos também aplicado dos UPDDISTRs para atualização de dicionário:

- [Acumulado Gestão de Contratos](https://tdn.totvs.com/pages/viewpage.action?pageId=679961416)

- [Acumulado Compras (Alçada)](https://tdn.totvs.com/pages/releaseview.action?pageId=535861077)

***Saiba Mais:***

* [Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Tipos de Contratos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407152148631)
* [Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
