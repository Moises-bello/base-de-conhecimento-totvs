---
content_hash: 0d3a182d87201c7494d060e2803ad1a60071aa08635ef15861f4e43435c5a022
fetched_at: '2026-06-29T00:10:51.403563+00:00'
page_id: '567747957'
product: rm
source: tdn-rm
title: Permissão de acesso do enviar e-mail para funcionário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=567747957
version: 6
---

false

**A partir das Versões:**

* 12.1.27.281
* 12.1.28.196
* 12.1.29.118

# Objetivo:

---

Apresentar a nova tag filha de segurança na permissão de acesso do enviar e-mail para funcionário.

falseImportante

* Com a atualização da versão o item "mensagem livre" ficará desabilitado, sendo necessário a execução do script para habilitar a usabilidade.
11Execução do scriptExecução do script

Para a criação da nova tag filha de segurança será necessário atualizar sua base de dados através do aplicativo RM.Atualizador.exe.

true3-1Permissão de AcessoPermissão de Acesso

Acesse o menu Serviços Globais| Segurança | Perfis

Selecione o sistema Folha de pagamento, edite o perfil desejado, vá em acesso aos menus e bloquei o acesso 11.02.03.01 Opção de Envio: Mensagem Livre

Após tirar a permissão acima a opção Mensagem Livre ficara desabilitada.
