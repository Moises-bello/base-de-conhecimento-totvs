---
article_id: 38098324411159
category: Reforma Tributária
content_hash: db49c502508ceabdb6398c9a1080cb878ee8249d26984cebb3592cca8d834d43
fetched_at: '2026-06-28T22:39:53.809934+00:00'
product: protheus
section_id: 34900856700439
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFE - Reforma Tributária
  – Rejeição 1155: Data de previsão de entrega anterior ao permitido'
type: support-article
updated_at: '2026-02-13T22:33:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38098324411159-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-Reforma-Tribut%C3%A1ria-Rejei%C3%A7%C3%A3o-1155-Data-de-previs%C3%A3o-de-entrega-anterior-ao-permitido
---

**Dúvida**  
Como corrigir a Rejeição 1155: Data de previsão de entrega anterior ao permitido?  
**Ambiente**   
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Solução**

Validação da Sefaz:

**Se informado data de previsão de entrega (tag: dPrevEntrega, id: B10a): - Data de previsão de entrega (dPrevEntrega) anterior a data de saída da nota (tag: dhSaiEnt, id: B10) Observação: caso a data de saída (dhSaiEnt) não esteja preenchida, considerar a data de emissão (tag: dhEmi, id: B09).**

**Obs:  A data de entrega não pode ser menor ou igual a data de emissão da nota. Caso a tag** dPrevEntrega seja igual ou superior a tag **dhSaiEnt e ainda sim ocorra a rejeição 1155, o cliente deve entrar em contato com Sefaz e verificar o motivo da rejeição.**

<dhEmi>2026-01-23T12:14:00-03:00</dhEmi>  
<dhSaiEnt>2026-01-23T12:14:00-03:00</dhSaiEnt>  
<dPrevEntrega>2026-01-23</dPrevEntrega>

Devido a nova tag **<**`dPrevEntrega`**>** — que representa a **data prevista de entrega** no cabeçalho da Nota Fiscal Eletrônica (NF-e) — introduzida pela Reforma Tributária (**Nota Técnica "NT 2025.002**"), o sistema passou a validar a **data de entrega** para a geração do documento de saídaquando o campo "**Tipo Frete (C5\_TPFRETE)**" no Pedido de Vendas está preenchido como:

* **C - CIF**
* **T - Por conta terceiros**
* **R - Por conta remetente**

Ao preparar o documento de saída pela rotina "**Documentos de Saída (MATA460A)**" temos 2 opções:

* **1 -** **Parâmetro "Data de Entrega?" em branco**: Sistema irá considerar o campo **"C6\_ENTREG"** para a geração do documento de saída e preenchimento do campo"**F2\_DTENTR**".
* **2 -** **Parâmetro "Data de Entrega?" preenchido:** Ao preencher o parâmetro "**Data de Entrega?**" no momento de preparar o documento de saída é gerada **uma única nota**, essa data é levada para o campo "**F2\_DTENTR**".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38098324406423)

Necessario estar com as atualizações abaixo para que a tag **<**`dPrevEntrega`**> seja gerada no xml** :

Criar o parâmetros abaixo no Protheus via Sigacfg,

[Documentação do parâmetro MV\_RTC55](https://tdn.totvs.com/pages/viewpage.action?pageId=1013641031)

**Protheus**  
**1. Aplicação do Pacote**

12.1.2310 <https://suporte.totvs.com/portal/p/10098/download#detail/1124963> [Somente para cliente com garantia estendida]

12.1.2410 <https://suporte.totvs.com/portal/p/10098/download#detail/1171486>

12.1.2510: <https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1224039>

**2. Aplicar o  patch e o nfesefaz do pacote liberado dia 29/01/2026.**

12.1.2310:<https://r.totvs.io/p/1235966> ;  [Somente para cliente com garantia estendida]

12.1.2410:<https://r.totvs.io/p/1235967> ;

12.1.2510:<https://r.totvs.io/p/1235968> ;

12.1.2310:<https://r.totvs.io/p/1234214> ; [Somente para cliente com garantia estendida]

12.1.2410:<https://r.totvs.io/p/1234215> ;

12.1.2510:<https://r.totvs.io/p/1234216> ; 

**TSS**  
**1.** **Arquivos de Schema:** [Download dos schemas](https://suporte.totvs.com/portal/p/10098/download?e=761857)  
Apoio caso necessário: [Procedimento: Substituir na pasta schemas do TSS.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103552-Cross-Segmentos-TSS-Transmiss%C3%A3o-de-Documentos-Eletr%C3%B4nicos-Atualiza%C3%A7%C3%A3o-dos-SCHEMAS)  
  
**2.** **Atualizar RPO do TSS:** [Clique aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981-Cross-Segmentos-TSS-Transmiss%C3%A3o-de-Documentos-Eletr%C3%B4nicos-Atualiza%C3%A7%C3%A3o-do-Reposit%C3%B3rio-RPO-do-TSS) Atualizado em 31/12/2025  
Documentação: [maiores detalhes.](https://tdn.totvs.com/pages/releaseview.action?pageId=956646956)

Para o TSS  12.1.2510 é necessario aplicar a expedição continua abaixo no rpo do TSS:

<https://suporte.totvs.com/portal/p/10098/download?e=1164047#detail/1224026> 

**Caso esteja na release 12.1.2310 sem garantia estendida, será necessário a migração para a release 12.1.2410:**  
- Veja como **migrar o TSS** [**aqui**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038065954-Cross-Segmentos-TSS-Transmiss%C3%A3o-de-Documentos-Eletr%C3%B4nicos-Migra%C3%A7%C3%A3o-para-12-1-2410-Instala%C3%A7%C3%A3o)!

Obs:  A data de entrega não pode ser menor que a data de emissão da nota.
