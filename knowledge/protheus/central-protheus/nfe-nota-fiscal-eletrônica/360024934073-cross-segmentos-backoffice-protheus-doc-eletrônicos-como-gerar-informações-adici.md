---
article_id: 360024934073
category: NFe - Nota Fiscal Eletrônica
content_hash: ad1b40b5d5a4d2938bdb64676ca27e3ab734902d6c7470dc429e620f63f5ff0b
fetched_at: '2026-06-28T22:40:06.735743+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar informações
  adicionais do Produto no XML (TAG infadprod)  e no DANFE
type: support-article
updated_at: '2026-06-22T18:27:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024934073-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-informa%C3%A7%C3%B5es-adicionais-do-Produto-no-XML-TAG-infadprod-e-no-DANFE
---

**Dúvida**Como gerar informações adicionais do Produto no XML (TAG infadprod) e no DANFE ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as verões.

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /****Cadastros / Parâmetros** clicar em ***editar*** MV\_INFADPR:  
![](https://totvssuporte.zendesk.com/attachments/token/sIXAt2AuVGb4VOrK977GPfpiH/?name=inline675648002.png)

Exemplo se o parâmetro MV\_INFADPR = 1 será levado as informações dos campos ***C6\_INFAD.***

*Para criação dos campos na tabela **CD6 verificar o link abaixo:***

***[Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6864596640151-Cross-Segmentos-TOTVS-BackOffice-Linha-Protheus-SIGAFAT-Campos-C6-INFAD-e-C6-CODINF-no-Pedido-de-Vendas)***

2. Preencher o campo **B5\_DESCNFE "Inf. Ad. Prod"** Este campo e do cadastro de **complemento de produtos** na aba outros

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072397273)

3. Para sair no Danfe a informação da TAG **infadprod**:

Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /****Cadastros / Parâmetros** clicar em **editar** MV\_IMPADIC= .T.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071223814)

4. Após gerar a nota e transmitir **o XML e o Danfe** serão gerados conforme o exemplo abaixo:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071224054)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072397833)

* ***Saiba mais:***

Existe um parecer da consultoria da TOTVS referente as informações geradas na**TAG infAdProd:**

[Parecer da consultoria](https://tdn.totvs.com/pages/releaseview.action?pageId=361433612)

Caso os campos padrões não atenda o seu processo para que o XML e o Danfe atenda sua necessidade há**duas opções de processos** a ser seguido:

1. Primeira opção pode ser customizado o **NFESEFAZ .**  
  
[MP - NFE - Documentos Eletrônicos NFe / NFSe / MDFe / MDe](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043005493-MP-NFE-Documentos-Eletr%C3%B4nicos-NFe-NFSe-MDFe-MDe-?source=search)  
  
**Rdmake disponível no link acima.**  
  
2. Segunda opção pode ser aberto melhoria na Central Colaborativa:  
  
[***Central Colaborativa TOTVS.***](https://centraldeatendimento.totvs.com/hc/contributions/posts?locale=pt-br)  
**Para saber como criar uma sugestão de melhoria clique [*AQUI.*](https://centraldeatendimento.totvs.com/hc/pt-br/community/topics)**
