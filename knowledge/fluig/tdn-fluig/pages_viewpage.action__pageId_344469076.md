---
content_hash: f454985b3b567aff80f985d7bae85665b37bb23c87edef27056b7e2b7bd12e0f
fetched_at: '2026-06-28T21:35:26.146220+00:00'
page_id: '344469076'
product: fluig
source: tdn-fluig
title: IDE - O Fluig Studio fica mais lento quando a plataforma está integrada ao
  Identity?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=344469076
version: 8
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**TOTVS Fluig Plataforma integrado ao TOTVS Identity

# Ocorrência

Após integrar a plataforma ao Identity, ao utilizar o Studio notamos que há uma demora maior na exportação e importação de artefatos. Por qual motivo isso acontece?

# Causa

Ao cadastrar o servidor da plataforma Fluig no Studio, o cliente optou por utilizar a senha do Active Directory ao invés da senha pessoal do Identity. Quando isso ocorre, o Fluig Studio envia as credenciais do usuário para o Identity, que confirma a validade com o Active Directory (através do SmartSync) e então realiza a autenticação na plataforma. Ao final desse processo, se as credenciais estiverem corretas, a importação/exportação de artefatos é iniciada.

A velocidade desse procedimento pode variar dependendo das condições de rede, infraestrutura e internet dos servidores em que o Studio, o SmartSync e a plataforma Fluig estão instalados.

# Solução

Utilizar a [senha pessoal](https://tdn.totvs.com/pages/viewpage.action?pageId=274828593) do administrador no cadastro do servidor no Fluig Studio. Dessa forma, é eliminado a consulta ao Active Directory, subtraindo uma fonte de lentidão em potencial.
