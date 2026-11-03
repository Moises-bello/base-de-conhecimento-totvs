---
content_hash: aa0ee36b27b9a28b0d05db26ecc128a611c5d2c3f38374ae8da0a87e6fcc3797
fetched_at: '2026-06-29T00:10:58.331685+00:00'
page_id: '60523243'
product: rm
source: tdn-rm
title: Segurança de campos do ERP no novo Gerador de Relatórios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=60523243
version: 1
---

Segurança de campos do ERP no novo Gerador de Relatórios

A partir da versão 10.70 o novo gerador de relatórios vai obedecer à segurança de campos do ERP.

### 

É possível inibir a visualização de um campo num determinado perfil de usuários e qualquer relatório que for visualizado por qualquer um dos usuários desse perfil não mais apresentará esse campo, apesar do relatório ser gerado normalmente e todos os campos a que o usuário tem acesso serem exibidos. Essa segurança está presente tanto para relatórios elaborados utilizando campos da base quanto para relatórios utilizando sentenças SQL.

[Clique aqui para ver um vídeo exemplificando essa segurança!](http://rmnet.rm.com.br/demorm/Seguranca_Campos_Novo_Gerador/Seguranca_Campos_Novo_Gerador.htm)

Importante ressaltar que o recurso de segurança de acesso a campos do ERP RM é uma funcionalidade do módulo de Consulta SQL. Dessa forma muitos outros pontos do ERP serão beneficiados com essa novidade ! Esse recurso por enquanto está disponível apenas em banco SQL Server.
