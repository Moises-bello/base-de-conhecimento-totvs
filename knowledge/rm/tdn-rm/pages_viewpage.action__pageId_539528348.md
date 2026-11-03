---
content_hash: cbd00888d2154133a0133aae5235e6294cdce2c23137d9b4ff21e2d65a83854c
fetched_at: '2026-06-29T00:10:37.282326+00:00'
page_id: '539528348'
product: rm
source: tdn-rm
title: Segurança nas APIs
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=539528348
version: 11
---

# Sumário

---

Sumário

Veja Também:

# Permissões

---

No trecho abaixo, será abordado as diferenças entre as permissões nas API's e as permissões no RM.

**Inversão na Lógica das Permissões**

As Permissões nas API's tem um conceito diferente das permissões no RM.

Quando um usuário não tem permissão em determinada rotina ou funcionalidade, para uma determinada coligada, usualmente o RM levanta uma exceção, onde é apresentado ao usuário o motivo do erro, através de uma janela.

**Exemplo de Folha de Permissão no RM:**

Usuário sem permissão para executar uma funcionalidade do sistema na coligada 1:

Nas Api's, a permissão em uma rotina ou funcionalidade, para uma determinada coligada, se materializa como um filtro, limitando as informações às coligadas que o usuário tem acesso.

**Exemplo de Permissão Filtrando por Coligada nas APIs:**

Um usuário que tem permissão na coligada 6 e que executar, por exemplo a API de Parâmetros, terá informação apenas da coligada 6 mais os parâmetros que forem globais, ou seja, visíveis à todas as coligadas.

Usuário tem permissão apenas na coligada 6:

# Acesso a Campos

---

A **segurança de campos** apresenta o seguinte conceito:

Quando um usuário não tiver permissão de visualização ou edição em um determinado campo de uma tabela, por restrição de um perfil associado, em uma determinada coligada, mesmo que ele tenha permissão de edição/visualização deste campo em outros perfis, esse usuário não poderá consultar ou alterar o valor do campo em questão.

**Importante:** O usuário que possuir restrição de visualização de campos não poderá utilizar estes campos em filtros. Caso o usuário faça o envio desta requisição, a API irá retornar um erro de acesso negado, com HTTP Code 403 (Forbidden). A única exceção é no filtro de Fields: nesse caso, o campo com restrição apenas não será retornado pela API.

**Exemplo:** O usuário "Teste" não pode visualizar o campo gusuario.status. Logo, qualquer requisição feita tentando passar o campo status (active) em um filtro (como em: http://{{dominio}}:{{port}}/api/framework/v1/users?active=true) a API retornará erro 403.

Nas APIs, a permissão em uma rotina ou funcionalidade, para uma determinada coligada, se materializa como um filtro, limitando as informações às coligadas que o usuário tem acesso.

**| GET:**

• Se a restrição do campo for de "Pode visualizar e não pode alterar", o campo será retornado pela API normalmente.

• Se a restrição do campo for de "Não pode visualizar e não pode alterar", apenas esse campo não será retornado pela API. Lembrete: Um erro de permissão pode ser retornado caso exista filtro utilizando o campo com restrição de visualização.

**| POST:**

• Mesmo que o usuário envie uma requisição contendo, no Body, um campo com restrição de edição, a API irá ignorar esse campo enviado.

• Caso ele possua algum valor default declarado explicitamente no seu mapeamento, o *insert* será feito com o valor default.

• Caso não possua um valor default, ele será preenchido na base com o valor default do tipo de dado. Ex.: Int = 0; String = null.

• Caso o campo com restrição seja uma PK, a chamada retornará um erro.

**| PUT e PATCH:**

 • Usuários que tenham restrição de edição de campos, conseguirão utilizar o PUT/PATCH apenas se a requisição não tentar alterar o campo com restrição.

* + Usando a propriedade **SkipCheckPropertyMapInfoForFieldLevelSecurity = False**

Internamente a Lib fará uma comparação desses valores: O valor enviado no Body e o valor persistido na base.

Para isto o mapeamento deve informar obrigatoriamente a PropertyMap, usando o método de overload map(), exemplo:

Map(e => e.Nome, **dto => dto.Name**); Em negrito esta definida a PropertyMap ou

Map(e => e.NomeFantasia, dto => dto.NomeFantasia);

Mesmo que o mapeamento não seja necessário.

* + Usando a propriedade **SkipCheckPropertyMapInfoForFieldLevelSecurity = True**

A comparação não será realizada e uma exceção será levantada para o campo com restrição.

Neste caso o mapeamento pode ser utilizado de forma mais simplificada, quando necessário, ou seja, não é obrigatório como no exemplo acima:

Map(e => e.NomeFantasia); Não é necessário informar PropertyMap

* + Existem duas formas de enviar o corpo da requisição:

• Incluindo o campo com restrição de edição no Body: Nesse caso, o valor do campo deve ser o mesmo valor salvo na base. Caso contrário, a API irá retornar um erro de acesso negado, com HTTP Code 403 (Forbidden), pois será considerado que o usuário está tentando alterar esse conteúdo.

• Não incluindo o campo com restrição de edição no Body (Apenas para PUT): Nesse caso, a API irá considerar o valor padrão do campo.  
Caso ele possua algum valor default declarado explicitamente no seu mapeamento, o PUT considerará que o valor enviado no Body é o valor default do campo.   
Caso não possua um valor default mapeado, ele será preenchido na base com o valor default do tipo de dado. Ex.: Int = 0; String = null.  
Em ambos os casos, o valor do campo deve ser o mesmo valor salvo na base. Caso contrário, a API irá retornar um erro de acesso negado, com HTTP Code 403 (Forbidden)pois será considerado que o usuário está tentando alterar esse conteúdo.

Obs: Para a propriedade **SkipCheckPropertyMapInfoForFieldLevelSecurity = False**

**| DELETE:**

 • A restrição de campos não influencia na remoção de registros. Caso o usuário possua um perfil com permissões para apagar o registro, este será removido independentemente de possíveis campos restritos ao usuário.

Versões anteriores à 12.1.2410

Este comportamento era diferente em versões anteriores à 12.1.2410:

• Usuários que possuem restrição de edição de campos não conseguirão remover o registro. Será emitido um aviso informando o campo com restrição.
