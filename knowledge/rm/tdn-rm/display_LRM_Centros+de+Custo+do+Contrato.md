---
content_hash: c071e1de2d8bbc2cde07c2ef458318a3f1683e3d07ddced2b671d2d1103f4045
fetched_at: '2026-06-29T00:09:15.415903+00:00'
page_id: '421385376'
product: rm
source: tdn-rm
title: Centros de Custo do Contrato
type: documentation
url: https://tdn.totvs.com/display/LRM/Centros+de+Custo+do+Contrato
version: 3
---

No anexo Centro de Custos do Contrato é possível realizar o cadastro do centro de custo que será utilizado para o contrato.

**Passos:**

Para realizar o cadastro basta somente informar código do centro de custo e o percentual do mesmo.

Na geração de movimentos para o RM Nucleus a partir de contratos, o rateio é enviado de acordo com o centro de custo default, mas deve ser feita a parametrização do RM Nucleus.

No menu Opções | Parâmetros | Tipos de Movimentos, pasta Valores Financeiros, subpasta Valores Extras / Fórmulas, grupo Rateios, no campo Tipo de Rateio selecione a opção 'Valor', no campo 'Centro de custo' e selecione a opção edita.

Para que o rateio seja enviado corretamente, é imprescindível que o tipo de rateio seja definido no RM Nucleus como 'Valor'.
