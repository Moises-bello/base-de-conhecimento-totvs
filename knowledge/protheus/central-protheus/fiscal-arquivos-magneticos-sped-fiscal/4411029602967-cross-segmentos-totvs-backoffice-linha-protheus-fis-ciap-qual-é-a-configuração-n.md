---
article_id: 4411029602967
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 23933382b2ec0c7c1239613d487a73a077cf6847130ab82efd6153c9b8c27fef
fetched_at: '2026-06-28T22:42:03.698691+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - CIAP - Qual é a configuração
  necessária para não escriturar o Diferencial de alíquotas de ICMS no registro G125
  campo 08 do Sped Fiscal?
type: support-article
updated_at: '2024-02-27T19:10:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411029602967-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-CIAP-Qual-%C3%A9-a-configura%C3%A7%C3%A3o-necess%C3%A1ria-para-n%C3%A3o-escriturar-o-Diferencial-de-al%C3%ADquotas-de-ICMS-no-registro-G125-campo-08-do-Sped-Fiscal
---

**Dúvida**Qual é a configuração necessária para **não** escriturar o Diferencial de alíquotas de ICMS no registro **G125** campo **08** do Sped Fiscal?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais - Todas as versões  
  
**Solução**

Para não escriturar o valor de diferencial de alíquotas para o CIAPé necessário que o parâmetro**MV\_DACIAP** tenha seu conteúdo = **N** e o parâmetro **MV\_F9SKPNF** = .T.

**Parâmetro:**

Nome da Var. = **MV\_DACIAP**  
Tipo = Caractere

**Conteúdo:**

**S** - Leva o diferencial de alíquotas para o CIAP.  
**N** - Não leva o diferencial de alíquotas para o CIAP

No documento de entrada o valor de diferencial de alíquotas fica em destaque no campo próprio, conforme abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411033518359)

 No **CIAP** o valor do diferencial de alíquota é levado para o campo próprio:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411033559959)

No arquivo da **EFD ICMS/IPI** o valor do Diferencial de Alíquotas **não** será escriturado no campo **08** do Registro **G125**:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411029493783)

**Informações adicionais:**

**CIAP** – Crédito ICMS sobre Ativo Permanente:

<https://tdn.totvs.com/pages/releaseview.action?pageId=187532625>

[MP - FIS - Utilização do Parâmetro MV\_F9SKPNF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048845293-MP-FIS-Utiliza%C3%A7%C3%A3o-do-Par%C3%A2metro-MV-F9SKPNF?source=search)
