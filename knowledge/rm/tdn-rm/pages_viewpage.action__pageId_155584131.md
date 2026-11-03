---
content_hash: 0bb001a4c24054d55c70fdd53dc58beedbfc6fddae2cf5cdc080bc21eb1c62b5
fetched_at: '2026-06-29T00:05:56.886163+00:00'
page_id: '155584131'
product: rm
source: tdn-rm
title: Ao acessar a MDI o sistema direciona diretamente para uma tela específica.
  Como desativar essa opção?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=155584131
version: 1
---

| Produto | RM |
| --- | --- |
| **Sintoma** | **Ao acessar a MDI o sistema direciona diretamente para uma tela específica (ex: seção, cadastro de funcionário, etc). Como desativar essa opção?** |
| **Solução** | Essa situação ocorre pois existe uma action ativa no sistema, caminho para desativá-la, acesse no menu inicial (MDI) a opção Serviços Globais -> Aba Serviços -> Actions do Sistema -> Na coluna "ID da Action" procure por FopSecaoAction **(ou o nome da action desejada**) -> Edite a Action e desmarque as opções "Executar automaticamente após login" e "Executar para todos os usuários".  Obs.  Segue consulta para verificar qual action está ativa :    SELECT \* FROM GUSRACTIONPREF   WHERE AUTOLOAD = 1 |
