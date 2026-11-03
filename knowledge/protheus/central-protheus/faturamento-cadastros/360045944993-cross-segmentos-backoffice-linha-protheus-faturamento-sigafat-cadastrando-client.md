---
article_id: 360045944993
category: Faturamento - Cadastros
content_hash: faadc1f3d2723374aa16bb26a5c842f9b1ae068c18268af4823342c2e45bdb36
fetched_at: '2026-06-28T22:38:35.384208+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Cadastrando
  Cliente Tipo Exterior
type: support-article
updated_at: '2024-01-24T13:24:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045944993-Cross-Segmentos-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Cadastrando-Cliente-Tipo-Exterior
---

**Dúvida**

Como cadastrar um cliente do tipo Exterior?  
  
**Ambiente**

Cross Segmentos - Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - A partir da versão 12  
  
**Solução**

Para realizar o cadastro, realize as configurações abaixo:

1. Estado (**A1\_EST**) = EX  
2. CEP (**A1\_CEP**) = 00000000  
3. Tipo (**A1\_TIPO**) = X - Exportação  
4. Código País (**A1\_PAIS**) - Deve ser diferente de branco e 01058  
5. Bairro (**A1\_BAIRRO**) = Informe o bairro pois é campo obrigatório (apesar de não ser validado em caso de exportação)  
6. Município (**A1\_MUN**) - Preencha com ESTRANGEIRO. O código de município 999999 pode ser incluído diretamente nas Tabelas de Municípios do IBGE (CC2)  
7. Código Município (**A1\_COD\_MUN**) = Em branco8. Insc. Estadual (**A1\_INSCR**) = Em branco9. CNPJ (**A1\_CGC**) =  Em branco **Saiba Mais:**

**<https://tdn.totvs.com/pages/releaseview.action?pageId=238035916>**
