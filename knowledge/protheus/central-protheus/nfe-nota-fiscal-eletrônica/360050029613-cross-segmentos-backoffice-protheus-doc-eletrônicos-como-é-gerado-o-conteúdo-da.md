---
article_id: 360050029613
category: NFe - Nota Fiscal Eletrônica
content_hash: 0aeae101d30eeefce2d14367c120fb73018d8e2da1719751140f2e763a38124c
fetched_at: '2026-06-28T22:40:00.294232+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  Como é gerado
  o conteúdo da TAG uCom '
type: support-article
updated_at: '2021-08-23T19:44:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050029613--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-%C3%A9-gerado-o-conte%C3%BAdo-da-TAG-uCom
---

**Dúvida**Como é gerado o conteúdo da TAG UnCom   
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1- Para gerar a unidade comercial na TAG uCom preencher no cadastro de produto o campo **B1\_UM "Unidade"**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073659854/mceclip0.png)

* **Saiba mais:**

Diferente disso para que o XML e o Danfe atenda sua necessidade temos**três opções de processos** a ser seguido:  
  
1- Esses casos devem ser customizados o **NFESEFAZ .**  
  
[MP - NFE - Documentos Eletrônicos NFe / NFSe / MDFe / MDe](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043005493-MP-NFE-Documentos-Eletr%C3%B4nicos-NFe-NFSe-MDFe-MDe-?source=search)

**Rdmake disponível no link acima.**

Esse campo no fonte do **NFESEFAZ:**  
  
 **aProd[8] =** B1\_UM

A quantidade comercial  será gerada no fonte do **NFESEFAZ:**  
  
**aProd[9]**  
  
  
  
Temos o **ponto de entrada:**  
  
Ponto-de-Entrada: PE01NFESEFAZ **- Manipulação em dados do produto**

* Conforme o **link abaixo:**

<https://tdn.totvs.com/pages/viewpage.action?pageId=274327446>

2- Segunda opção pode ser aberto melhoria na Central Colaborativa:  
  
[Central Colaborativa TOTVS.](https://centraldeatendimento.totvs.com/hc/contributions/posts?locale=pt-br)  
**Para saber como criar uma sugestão de melhoria clique [AQUI.](https://centraldeatendimento.totvs.com/hc/pt-br/community/topics)**  
  
  
3- Para que seja atendido no padrão é necessário que a empresa tenha alguma legislação na qual informe a obrigatoriedade de gerar conforme deseja.  
  
Havendo a legislação abra um ticket no suporte e nos encaminhe que será compartilhado junto a consultoria tributária da TOTVS e posteriormente ao produto.

* Para gerar a **Segunda unidade de medida no XML e no Danfe  há o link abaixo:**

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar Segunda unidade de medida no XML ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044212253)
