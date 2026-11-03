---
content_hash: 3ab704b9316fcaf3967ca4355be3b657f391be71dde9f87d0704f536c1212217
fetched_at: '2026-06-29T00:11:05.531721+00:00'
page_id: '632113829'
product: rm
source: tdn-rm
title: 'Erro código 1801: O FAP do estabelecimento não foi localizado na base'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=632113829
version: 22
---

false

**A partir das Versões:**

* 12.1.29.284
* 12.1.31.199
* 12.1.32.136
* e Superiores.

# Objetivo:

---

Mediante a [notícia publicada no site do eSocial no dia 26/07/2021](https://www.gov.br/esocial/pt-br/noticias/ajuste-no-procedimento-de-informacao-do-fap-em-s-1005-versao-s-1.0), foi realizado um ajuste no procedimento de informação do FAP no evento S-1005 para a versão S-1.0.

Conforme orientações recebidas no grupo de homologação oficial do eSocial, esse ajuste será temporário até que a situação no ambiente do governo seja regularizada, uma vez que somente deve preencher os campos GILRAT e FAP quando houver processo judicial/administrativo com decisão/sentença favorável à utilização de alíquota GILRAT ou do FAP diferentes do que é definido pela administração, nos demais casos, os referidos campos não devem ser preenchidos (ver item 3.1 no Manual de Orientação do eSocial).

É importante lembrar também que, a situação ocorre apenas para alguns CNPJs.

Diante disso, caso ao enviar o S-1005 para o governo apresente o erro "Erro código 1801: O FAP do estabelecimento não foi localizado na base. Ação sugerida: reenviar o evento informando o FAP no campo [fap]..". o usuário deverá seguir as instruções abaixo:

---

1true1Utilizando o MIDDLEWAREUtilizando o middleware

1) Acesse RH | Folha de Pagamento | eSocial | Fila de Eventos.

2) Verifique o evento na fila que foi rejeitado, conforme exemplo abaixo:

3) Clique no processo "Editar XML".

Será apresentado uma mensagem para confirmar a edição.

4) Confirme a pergunta, clicando em "Sim" para que seja apresentado o Editor de XML eSocial, encontre a tag <cnaePrep> e dê um <enter> e acrescente as tag's abaixo, em seguida clique em <Salvar>.

          <aliqGilrat>  
            <fap>1.0000</fap>  
          </aliqGilrat>

O XML será salvo com a informação do FAP.

5) Selecione o evento e faça o envio, após a atualização de status evento foi aceito com sucesso.

2Utilizando o TAF FULLUtilizando o TAF Full

1) Acesse RH | Folha de Pagamento | eSocial | Fila de Eventos.

 2) Verifique que o evento na fila foi rejeitado, conforme exemplo abaixo:

3) Acesse o TAF e o menu Atualizações > Eventos eSocial > Tabelas > Estab, Obras ou Unid. Org. Públicos.

4) Selecione o estabelecimento e clique em <Alterar>.

5) Cadastre o FAP e salve as alterações.

6) Após o cadastro faça o reenvio do evento S-1005 e atualize status novamente no RM.
