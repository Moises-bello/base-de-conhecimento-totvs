---
content_hash: c4c656d6eaaa7c6c4fae86a4e42bbe0ecae9de56bb4c1f262c4438d912067d26
fetched_at: '2026-06-29T00:08:23.105820+00:00'
page_id: '269447847'
product: rm
source: tdn-rm
title: Erro GED_URL_USUARIO  ao sincronizar usuário com GED
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269447847
version: 1
---

Objetivo:

---

        O objetivo deste documento é trazer informações para correção do erro GED\_URL\_USUARIO ao efetuar a sincronização dos usuários do RM com GED.

 Introdução:

---

       A sincronização de usuários é a etapa responsável que envia os usuários existentes no RM para o GED.

Passo a Passo:

---

O erro GED\_URL\_USUARIO ocorre quando o campo “Grupo de Usuários” não está preenchido. Para localizar esse devemos acessar o modulo de Integração e em seguida percorrer o seguinte caminho: Ferramentas/Parâmetros/50.07 Linha RM X GED (Gerenciamento Eletrônico de Documentos)

 A sincronização do usuário ocorre através do módulo Serviços Globais no seguinte caminho: Segurança/ Usuário/Processos/” Sincronizar usuários do Corpore com o GED”.

 Como o campo “Grupo de Usuários” não está preenchido sistema apresenta o seguinte erro: “Processo finalizado com erro: Parâmetro não encontrado: GED\_URL\_USUARIO.

Para correção do erro é necessário efetuar o preenchimento do campo “Grupo de Usuários”, esse grupo de usuários está relacionado a qual grupo o usuário sincronizado irá pertencer dentro do GED.

Após informar o grupo de usuário sincronização foi realizada com sucesso.
