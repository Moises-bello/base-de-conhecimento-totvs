---
article_id: 20939128067479
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: d82e34aaf2da19dd03adc1660e451f13c353359cebd7d6479989add7b71f0965
fetched_at: '2026-06-28T22:37:21.708336+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Consulta padrão campo
  "Tipo" (CN0_TIPO) vazia no cadastro de Tipos de Revisão
type: support-article
updated_at: '2026-01-22T14:12:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20939128067479-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Consulta-padr%C3%A3o-campo-Tipo-CN0-TIPO-vazia-no-cadastro-de-Tipos-de-Revis%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20939144105879) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
No cadastro de Tipos de Revisão, na consulta padrão "F3" do campo "Tipo" (CN0\_TIPO), não aparecem os Tipos de Revisão par serem selecionados:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37857279323799)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Solução**  
Abaixo seguem algumas análises que podem ser relizadas na base/ambiente referente ao campo CN0\_TIPO, se o mesmo está com as configurações corretas de Consulta Padrão, bem como a consulta padrão está cadastrada corretamente conforme o padrão do sistema e também a tabela genérica "GC" cuja consulta padrão busca as opções está com as opções corretamente conforme o padrão.  
  
Abaixo seguem as imagens das configurações de um ambiente padrão para checagem e comparação e possivel ajuste no ambiente em questão.  
  
Cadastro Campo CN0\_TIPO:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37857279326615)  
   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37857279327383)  
   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37857279329303)  
 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37857279330455)

Consulta Padrão "\_GC" do campo CN0\_TIPO :

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37857285879959)

 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37857279335703)

Tabela Genérica "GC" da tabela SX5 que contém as opções buscadas pela Consulta Padrão:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37857285883799)

Por padrão os compartilhamentos da SX5  são de modo compartilhado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37857285887767)

Dessa forma o campo Filial é em Branco da tabela GC - Tipos de Revisão no padrão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37857279340951)

Caso tenha ajustado o Compartilhamento da tabela SX5 para Exclusivo verifique também se o campo X5\_FILIAL filial foi ajustado conforme o seu Compartilhamento.

***Saiba Mais:***

* [Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
