---
content_hash: 45f171f8f546f92a9914bf98d348b737bbe12735655c567eca2885a115885d93
fetched_at: '2026-06-29T00:11:45.783684+00:00'
page_id: '821579264'
product: rm
source: tdn-rm
title: Leiaute S-1.2 - Nota Técnica 02/2024
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=821579264
version: 9
---

false

**A partir das Versões:**

# Objetivo:

---

Adequamos o produto TOTVS Folha de Pagamento para atender ao leiaute S-1.2, conforme as alterações descritas na [Nota Técnica 02/2024](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-tecnica-s-1-2-02-2024.pdf)[,](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-tecnica-s-1-1-01-2023.pdf)  do eSocial, publicada em 10/01/2024, referentes aos itens 3.1.

1true3Alterações com entrada em produção 01/02//2024 Alterações com entrada em produção 01/02//2024

1)**S-1000 - Informações do Empregador/Contribuinte/Órgão Público**

Acrescentado opção, alterada descrição da tag <indDesFolha> e ajustada validação

| DE | PARA |
| --- | --- |
| Indicativo de desoneração da folha. Valores válidos: 0 - Não aplicável 1 - Empresa enquadrada nos arts. 7º a 9º da Lei 12.546/2011 Validação: Pode ser igual a [1] apenas se classTrib = [02, 03, 99]. Nos demais casos, deve ser igual a [0]. | 0 - Não aplicável 1 - Empresa enquadrada nos critérios da legislação vigente 2 - Município enquadrado nos critérios da legislação vigente Validação: Pode ser igual a [1] apenas se classTrib = [02, 03, 99]. Pode ser igual a [2] apenas para as naturezas jurídicas iguais a [103-1, 106-6, 124-4, 133- 3]. Nos demais casos, deve ser igual a [0]. |

Ajustado no cadastro do empregador em eSocial | Informações do Empregador | Aba Informações do Empregador

Adicionado opção, alterada descrição e ajustada validação. Campo **PESOCIALEMPREGADOR**.**INDDESFOLHA**

Criada validação para as naturezas diferentes 103-1, 106-6, 124-4, 133-3
