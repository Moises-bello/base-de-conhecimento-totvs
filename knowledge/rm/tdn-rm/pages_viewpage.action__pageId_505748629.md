---
content_hash: 0cd291873bdedcfb66cc34b5515a3dae1870c234f1fb69f24a2ebcdb07e63094
fetched_at: '2026-06-29T00:10:25.767268+00:00'
page_id: '505748629'
product: rm
source: tdn-rm
title: Integração - Aceleradora de carreiras
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=505748629
version: 5
---

Os passos a seguir servirão de guia para a integração com a Aceleradora de carreiras disponível no novo portal do aluno.

Para saber mais sobre a aceleradora de carreiras [clique aqui](https://dnadaeducacao.com/)

Alunos precisam estar com CPF preenchido

A chave de identificação da Aceleradora de carreiras é o RA do aluno.

**Parametrização da integração**

Nos parâmetros *Educacionais | Integração | Aceleradora de carreiras* deve ser marcado o parâmetro Utiliza integração com Aceleradora de carreiras e deve ser preenchido os dados de conexão (UserName, Token e Plataforma de acesso).

Dados de conexão

Os dados de conexão serão disponibilizados pela DNA Educação.

A URL da Plataforma de acesso deve terminar em .br

Para controle de acesso, foi criado uma permissão de acesso no perfil dentro de *Educacional | Educacional (Portal) | Acadêmico | Aceleradora de carreiras*

**Portal do aluno**

Após configuração, será exibido para o aluno o menu da Aceleradora de carreiras.

Motivos para o menu não aparecer para o aluno

Se mesmo com a integração configurada corretamente o menu não estiver aparecendo para algum aluno, valide as seguintes informações:

* O RA aluno está devidamente cadastrado na Aceleradora de carreiras;
* A URL da plataforma de acesso está cadastrada nos parâmetros sem terminar no .br (remova barras desnecessárias após o .br);
* Se a release que você estiver utilizando é a 12.1.25, certifique-se que o script de ativação da integração foi executado na base de dados.

Quando o aluno clicar no menu, será aberto uma nova aba da aceleradora de carreiras com o aluno já autenticado:
