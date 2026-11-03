---
article_id: 360036289934
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 3c0adecef38870a06d0ea1dc752753b9b7aa7ec91df7227458d4f2fdef1a9bef
fetched_at: '2026-06-28T22:38:28.597338+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Mensagem: AO4_CODUSR:
  Código de usuário não existe - Verifique o código informado'
type: support-article
updated_at: '2023-08-23T20:57:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036289934-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Mensagem-AO4-CODUSR-C%C3%B3digo-de-usu%C3%A1rio-n%C3%A3o-existe-Verifique-o-c%C3%B3digo-informado
---

**Dúvida**

Por que toda vez que altero um cadastro ocorre a mensagem informando que o **AO4\_CODUSR** é inválido?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT -Todas as versões.  
  
**Solução**

Ao confirmar a alteração de um cadastro o sistema apresenta a mensagem:

Id do formulário de origem: []  
Id do campo de origem: []  
Id do formulário de erro: [AO4DETUSR]  
Id do campo de erro: [**AO4\_CODUSR**]  
Id do erro: [USR\_EXIST ]  
Mensagem do erro: [ **Código de usuário não existe**.]  
Mensagem da solução: [Verifique o código informado.]  
**Valor atribuído: [000084]**  
Valor anterior: [ ]

A tabela **AO4** do sistema controla as **Permissões de acesso** aos registros, toda vez que um registro é inserido é incluída uma linha com o código do registro, a tabela, a filial e o usuário responsável pela inclusão.

Ao realizar a manutenção deste registro, o sistema verifica se o **usuário**, que está efetuando a alteração, possui alguma **restrição de acesso**.

A mensagem acima ocorre quando o **usuário registrado**, no campo **AO4\_CODUSR**, **não existe** no cadastro de usuários do **Configurador**, isso pode ocorrer caso o usuário registrado na tabela tenha sido deletado da tabela de usuários diretamente pelo banco.

**Para solucionar o problema**, verifique se este **código de usuário** apresentado na mensagem em “**Valor atribuído**”, existe nas tabelas **AO3 ou AO4** do sistema, caso exista é necessário que exista também no cadastro de usuários no configurador para que a mensagem não seja mais apresentada.
