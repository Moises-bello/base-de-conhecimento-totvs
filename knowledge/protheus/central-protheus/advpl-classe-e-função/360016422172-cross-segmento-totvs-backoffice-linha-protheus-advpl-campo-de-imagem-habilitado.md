---
article_id: 360016422172
category: ADVPL - Classe e Função
content_hash: d9b238e1507904763cfd267097338ea7fd7d5fcc4bdd41e794c8cb1d1bdd0ef4
fetched_at: '2026-06-28T22:40:14.508995+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Campo de Imagem
  habilitado para edição na Visualização
type: support-article
updated_at: '2022-01-03T22:05:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016422172-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Campo-de-Imagem-habilitado-para-edi%C3%A7%C3%A3o-na-Visualiza%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Estou com erro em um campo de imagem, onde estou incluindo uma imagem que não vai ser alterada, quando acesso a opção do menu Visualizar fica disponível a edição do campo mesmo verificamos a com X3\_WHEN preenchido igual à falso também não desabilita permitido a edição.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360012611032/mceclip0.png)

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL - A partir da versão 12.1.17  
  
**Causa**O problema ocorre por utilizar a variável aRotina como ***PRIVATE***, então, o comportamento do programa que controla o campo *BITMAP* assumiu o comportamento para programas não MVC.

Apenas em funções legadas devem utilizar esta variável como ***PRIVATE***.

**Solução**Para correção do problema, deverá ser alterado o programa do cliente, sendo:

Na User Function:  
\* Retirar a linha: Private aRotina := MenuDef()  
\* Acrescentar a linha   
oBrowse:SetMenuDef( 'NOMEDOPRW' ), após a declaração do objeto FwMBrowse() e substituindo a string 'NOMEDOPRW' pelo nome do arquivo .prw que no caso possui a static function MenuDef() desejada.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360012613132/mceclip1.png)

Saiba mais sobre o método [SetMenuDef](https://tdn.totvs.com/display/PROT/FWFormBrowse)  
Sintaxe

```
obrowse:SetMenuDef(< cMenuDef >)-> NIL
```

Descrição  
Indica o programa que será utilizado para a carga do menu funcional
