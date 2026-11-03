---
article_id: 360044466554
category: Escrita Fiscal - Error.log
content_hash: 680c64ebc70547987c35c4635e2fbd442fd3fe559705f223b8598ebfaf6fa648
fetched_at: '2026-06-28T22:39:32.799072+00:00'
product: protheus
section_id: 1500001549782
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como a rotina FISA153
  "Apuração Simples Nacional" se comporta quando o Sublimite é excedido
type: support-article
updated_at: '2023-02-09T19:54:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044466554-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-a-rotina-FISA153-Apura%C3%A7%C3%A3o-Simples-Nacional-se-comporta-quando-o-Sublimite-%C3%A9-excedido
---

**Dúvida**

Como a Rotina FISA153 se comporta quando o Sublimite é excedido em mais de 20%

**Ambiente**

Protheus – Livros Fiscais – A partir da versão 12.0  
  
**Solução**

Consultar valores da apuração se foram excedidos e legendas demostrativas, **Status dos Tributos por Filial** "Img. Ex. abaixo", a legenda estará indicando as permissões de recolhimentos.

***Obs.: A Rotina não fará nenhum bloqueio ou aviso alem dos valores e legendas indicativas.***

## O que fazer quando o sublimite for excedido em mais de 20%?

Neste caso basta configurar o parâmetro **MV\_CODREG**informando a opção **2**, que significa **excesso de sublimite de receita bruta.**Uma vez efetuada esta configuração as alíquotas calculadas pela apuração deixarão de ser utilizadas no faturamento dos documentos. Conforme orientação de configuração do parâmetro [MV\_CODREG](https://tdn.totvs.com/pages/releaseview.action?pageId=346488974#FIS0094_Apura%C3%A7%C3%A3o_Simples_Nacional-mv_codreg), na hipótese de haver filiais localizadas em estados em que vigorem sublimites distintos, o parâmetro deverá ser exclusivo por filial. Neste caso a configuração para a opção **2** deverá ser efetuada somente para as filiais cujo sublimite tenha sido excedido.

<http://tdn.totvs.com/pages/releaseview.action?pageId=346488974>

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360061589573/mceclip1.png)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360061588193/mceclip0.png)
