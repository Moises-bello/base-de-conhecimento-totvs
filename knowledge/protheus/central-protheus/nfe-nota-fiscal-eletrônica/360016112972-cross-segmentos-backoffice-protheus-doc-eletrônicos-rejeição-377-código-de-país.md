---
article_id: 360016112972
category: NFe - Nota Fiscal Eletrônica
content_hash: 8445c0d149d30993c32ae28004906d413f53f33d1ac5b9ce79575ac69f2d102f
fetched_at: '2026-06-28T22:40:01.942579+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Rejeição 377:
  Código de País do destinatário Inexistente'
type: support-article
updated_at: '2021-10-11T15:35:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016112972--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Rejei%C3%A7%C3%A3o-377-C%C3%B3digo-de-Pa%C3%ADs-do-destinat%C3%A1rio-Inexistente
---

**Dúvida**Como solucionar a rejeição 377: Código de País do destinatário Inexistente  ?   
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Conforme a nota técnica 2018.003\_v\_1.00

* **Alguns Códigos de países excluídos**
* **Alguns Códigos de países incluídos**
* **Alguns Códigos de países alterados (sem alteração do nome)**
* **Alguns Alteração do Nome de País**

**Importante:**

* **Foi liberado uma nova versão da NT 2018.003\_v\_1.01**

**Prazo da Sefaz:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026409652/mceclip0.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026409872/mceclip5.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026409812/mceclip4.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026401151/mceclip1.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026409792/mceclip3.png)

* **Há uma tabela disponível no site da Sefaz:**

<http://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=Iy/5Qol1YbE=>

[Tabela de Países - Relacionada à NT 2018.003. v1.01 (atualizada em 12/04/2019)](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=FOXZNFX/p50=)

**Importante:**

Caso utilize o SIGAEIC ou SIGAECC a manutenção da tabela dos países pode ser realizada através da rotina.

Caso realize as notas pelo Compras ou Faturamento será necessário realizar a manutenção na tabela SYA.

É necessário entrar na APSDU na tabela SYA alterar os campos

* YA\_CODGI = 3 Primeiros dígitos
* YA\_SISEXP= 4 Dígitos
* YA\_DESCR =Descrição do nome do País

**Poderá verificar no site:**  
<http://www.bcb.gov.br/rex/Censo2000/port/manual/pais.asp?idpai=CENSOCE>
