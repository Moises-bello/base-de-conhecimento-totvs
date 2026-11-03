---
content_hash: fa1ca82beb59e59eadd2da5490fcebc0daae4ba553592f5bdbabdabe614aa908
fetched_at: '2026-06-28T21:35:22.245080+00:00'
page_id: '235327854'
product: fluig
source: tdn-fluig
title: ARQ - Como resolver o erro ORA-01536 indisponibilidade parcial de recursos
  da plataforma?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235327854
version: 9
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

**Banco de Dados:** Oracle

# Ocorrência

A plataforma sobe mas não fica funcional, apresentando inconsistências no log do servidor de aplicação. Dentre elas falha na compilação do módulo do LMS. Como resolver esta inconsistência?

# Causa

Política de permissão/cota para a base de dados utilizada na instalação.

javaEclipseserver.log

Devido ao fluxo de registro da aplicação, a estrutura de tabelas criada na base de dados consome recurso conforme alocação especificada. O dimensionamento inferior ao especificado pode impedir o registro por completo dessa estrutura, ocasionando erros secundários.

# Solução

Liberar espaço para *tablespace* seguindo os requisitos contidos no  e .

# Observações

A falta do registro da estrutura de dados da plataforma pode acarretar indisponibilidade total ou mesmo parcial, dependendo do estado que se encontrar a base de dados da aplicação.
