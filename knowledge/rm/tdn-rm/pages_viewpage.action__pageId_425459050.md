---
content_hash: fb8ecbea5496dba3fb72ba667028c7ef1f898845d57394609fffa63296839df3
fetched_at: '2026-06-29T00:09:33.778008+00:00'
page_id: '425459050'
product: rm
source: tdn-rm
title: Envio de post para a comunidades e notificações para usuários do fluig
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459050
version: 4
---

---

Para que este processo esteja disponível e necessário realizar a integração com fluig. Assim para ativar cadastre o código de comunicação.Este processo dispara posts em comunidades e notificações para usuários do fluig.

Ele disponibiliza as seguintes abas:

Na primeira aba são as definições relacionada a geração das informações, para post nas comunidades do fluig o sistema precisa está configurado para utilizar a funcionalidade academia social.

Na segunda aba o usuário define a lista das comunidades que serão alvo. Existe duas formas para definir os mecanismo das comunidades:

**Para Post nas comunidades:**

* Por consulta sql : Neste caso a consulta precisa conter o campo "ALIASCOMUNIDADE". Se a consulta retornar comunidades inativas na execução do processo, elas serão ignoradas.
* Via consulta as comunidades : Selecione a entidade alvo do post (curso,habilitação,turma,turma/disciplina,sub-turma e atividade ofertada), além de selecionar as comunidades que devem receber o post.

**Observação:** Apenas as comunidades que estão ativas serão listadas.

**Para notificação no fluig:**

* Neste caso define o SQL responsável por buscar a lista dos destinatários das notificações. A consulta deverá conter  obrigatoriamente  os campos "CODUSUÁRIO","Email".

Na terceira aba:

* É definida a mensagem que se quer enviar, as tags disponíveis serão todos os campos disponíveis no SQL criado pelo cliente ou na consulta exibida na seleção das comunidades.
* Nesta mensagem não a possibilidade de formatar o texto e/ou inclusão de imagens somente texto simples.

Após a realização do processo é criado um post para as comunidades ou o envio das notificações para os usuários do fluig.  

Veja Também

---

[Documento Técnico - Central de Notificação II](http://tdn.totvs.com/display/LRM/DT_Central_Notificacao)
