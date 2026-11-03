---
content_hash: 13df39f9d1d8a4670e0505cf9b826cec1b1961d9def4f9ee09f7627e132e0ac6
fetched_at: '2026-06-28T21:35:23.080021+00:00'
page_id: '243657927'
product: fluig
source: tdn-fluig
title: BPM 053 - Como manter os anexos visíveis durante a movimentação de solicitações?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243657927
version: 6
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**fluig

**Versão:** 1.5.8 e anteriores

# Ocorrência

Foi implementado em um processo uma validação para que o usuário seja obrigado a preencher o campo "Observação" antes de movimentar a solicitação. Porém, quando o usuário anexa arquivos à solicitação e movimenta o processo sem preencher o campo, a validação funciona corretamente, mas ocorre erro ao enviar os anexos.

# Causa

O erro ocorre pois, quando a solicitação é movimentada, os arquivos anexados são movidos da pasta temporária para serem anexados à solicitação. Quando ocorre a interrupção do processo de movimentação pelo desenvolvimento que valida o preenchimento de campos, os arquivos já foram removidos. Desta forma, na próxima movimentação, a pasta está vazia e os arquivos não são localizados.

# Solução

Atualizar o fluig para a , onde tal situação foi corrigida ou, caso não seja possível, instruir os usuários a remover os anexos e selecionar os arquivos novamente.
