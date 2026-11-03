---
content_hash: 6cc2949c62cc0e6f9dad9678ceaf362865b89e0a1c240b2d2d3f948399d3e963
fetched_at: '2026-06-28T21:35:19.344881+00:00'
page_id: '201743454'
product: fluig
source: tdn-fluig
title: IDE - É possível alterar a matrícula para importar de outro sistema integrado
  com o Identity?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201743454
version: 8
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**TOTVS Fluig Plataforma integrado ao TOTVS Identity

**Versão:** 1.5.0 ou superior

# Ocorrência

Ao integrar a plataforma Fluig com o Identity na versão 1.5 e marcar o campo 'Provisionamento Just in Time', a matrícula do usuário é gerada com base no seu e-mail. É possível alterar a matrícula para que seja importada de outro sistema que também é integrado com o Identity?

# Solução

O Identity é capaz de realizar uma ponte entre a plataforma Fluig e outros sistemas, mas o campo matrícula de cada sistema é isolado e não é considerado pelo Identity para realizar a integração entre eles. Desta forma, matrículas diferentes na plataforma ou nos demais sistemas não irão impedir a integração. No caso de ser necessário que a matrícula na plataforma Fluig seja a mesma de um outro sistema, será necessário deixar o parâmetro 'Provisionamento Just in Time' desmarcado e então incluir os usuários manualmente no cadastro de usuários, assim o campo matrícula poderá ser preenchido com o valor desejado.

# Observações

Se a inclusão manual não é uma solução viável, entre em contato com nossa equipe de serviços através do e-mail propostas@fluig.com.
