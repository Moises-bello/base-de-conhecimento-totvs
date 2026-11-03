---
content_hash: 310e513cce0faa5f48e1b6b24df84b33dec18b1306852643a54ef2d94fa2f885
fetched_at: '2026-06-28T21:35:27.324598+00:00'
page_id: '543094841'
product: fluig
source: tdn-fluig
title: Plataforma ❙ Dados pessoais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=543094841
version: 30
---

.\*ndice

# Falando de dados pessoais...

---

Nessa tela são apresentados todos os dados requisitados ao usuário que utiliza o TOTVS Fluig e sinalizados como dados pessoais. Existem três tipos de dados pessoais:

* **Dados nativos**: são os campos de uso comum na plataforma como o nome, sobrenome, nome de exibição e e-mail, informados para cada usuário na tela de [Cadastro do usuário](https://tdn.totvs.com/x/c4H5DQ);

* **Dados adicionais**: são os dados informados na seção [Dados Adicionais](https://tdn.totvs.com/pages/viewpage.action?pageId=234455411#Plataforma%E2%9D%99Usu%C3%A1rios.-adicionais), para complementar o cadastro do usuário (por exemplo, o CPF ou a data de nascimento);

* **Dados de formulário**: dados requisitados pelos formulários construídos na plataforma, sejam eles , ,  e .

Os dados listados nessa tela são utilizados nas rotinas de , e também na rotina de [eventos de auditoria](https://tdn.totvs.com/x/DdMTEQ).

Nota:

Esse item se dá devido a implementação da regulamentação da **Lei Geral de Proteção de Dados Pessoais** (**LGPD** ou **LGPDP**) na organização.

Para mais informações e esclarecimentos de como a organização irá atuar mediante a conduta LGPD, [acesse aqui](https://tdn.totvs.com/x/jYupHg).

## Ver dados pessoais

---

**01.** No menu principal, clique em  **Painel de controle**.

**02**. Localize o agrupador **Segurança e acesso**.

**03**. Clique em  **Dados pessoais**.

**04**. Veja a listagem de dados pessoais.

#f2f2f2#f2f2f2

Todas as informações classificadas como dado pessoal serão apresentadas nessa lista.

adicionar

## Adicionar dado pessoal

---

trueimageVeja a imagem#0897E9INLINE

**01.** No menu principal, clique em  **Painel de controle**.

**02**. Localize o agrupador **Segurança e acesso**.

**03**. Clique em  **Dados pessoais**.

**04.** Clique em **Adicionar dado pessoal**.

#f2f2f2#f2f2f2

Será aberta a tela para inclusão das informações, já preenchida com o nome e a descrição da tabela. Esses campos não podem ser alterados.

Podem ser incluídos somente registros dos atributos dos Dados Adicionais. Para incluir campos de Formulários utilize os editores dos formulários.

**05.** Preencha as informações solicitadas.

#f2f2f2#f2f2f2

As informações solicitadas são:

**Atributo**  
Identificador do campo que armazena este dado. O atributo do dado pessoal deve ser escrito exatamente igual à chave do dado adicional.

trueimageVeja a imagem#0897E9INLINE

**Descrição atributo**  
Descrição do campo que armazena este dado.

**Tipo**Permite selecionar um tipo de dado para o campo, conforme a informação pessoal armazenada. Os tipos disponíveis são: Nome, E-mail, CPF, RG, Carteira de habilitação, Carteira de trabalho, Título de eleitor, Passaporte ou outros, dependendo do tipo de componente para o qual a privacidade está sendo configurada.

**Este dado é sensível?**Indica que o dado é classificado como sensível e que ele será informado no relatório de dados do usuário (Exportação de Dados). É considerado sensível todo dado de origem racial ou étnica, convicção religiosa, opinião política, filiação a sindicato ou a organização de caráter religioso, filosófico ou político, dado referente a saúde ou a vida sexual, dado genético ou biométrico, quando vinculado a uma pessoa natural.

**É possível anonimizar este dado?**Habilite esta opção caso o tipo de dado escolhido precise ser ocultado.  
Quando estiver com essa opção marcada, indica que o dado pode ser ocultado do banco de dados, caso o usuário, dono do dado, solicite a [anonimização](https://tdn.totvs.com/x/uOpvI). Um campo, quando anonimizado, não vai mais ter o seu valor. Se for dados do usuário, não aparecerão nos cadastros e se for dados de formulário, também não vão aparecer nos formulários. 

trueimageVeja a imagem#0897E9INLINE

O dado pessoal anonimizável geralmente será aquele a partir do qual é possível determinar quem é o titular do dado, por exemplo, um número de CPF ou título de eleitor.  
Existem dados pessoais de uma determinada pessoa que não permitem essa identificação, por exemplo, a data de aniversário, é um dado pessoal pois pertence a uma pessoa, no entanto não é anonimizável, pois a partir dessa data não é possível determinar quem é titular do dado.

**Classificação e justificativa**Especifica para que o dado está sendo solicitado e para quais fins será utilizado.

**Classificação**A classificação permite selecionar qual dos motivos gerou a necessidade de configuração da privacidade dos dados. Os tipos de classificação disponíveis são: Execução de contrato, Obrigação Legal, Consentimento, Execução de políticas públicas, Estudo por órgão de pesquisa, Exercício regular de direito, Para a proteção da vida, Para tutela de saúde, Interesse legítimo e Proteção de crédito.

**Justificativa**Permite incluir uma justificativa por extenso, do motivo pelo qual o dado é solicitado e para que ele é utilizado. Para inserir numa nova classificação e sua justificativa, acione o botão **Adicionar**, localizado ao lado do menu de **Classificação e justificativa**. Para remover, acione o ícone , localizado ao lado direito da respectiva classificação e justificativa.

**06.** Clique em **Confirmar**para gravar o dado pessoal.

## Editar dado pessoal

---

Caso seja um dado pessoal pertencente a um formulário, a edição desse dado só é permitida por meio da configuração desse formulário.

**01.** No menu principal, clique em  **Painel de controle**.

**02**. Localize o agrupador **Segurança e acesso**.

**03**. Clique em  **Dados pessoais**.

**04.** Localize o registro a ser alterado.

**05.** Clique em **Editar** , localizado na coluna **Ações**.

**06.** Altere as informações necessárias.

#f2f2f2#f2f2f2

Para mais informações sobre os campos, consulte o item .

**07.** Clique em **Confirmar**para salvar as alterações.

## Desativar dado pessoal

---

Não é possível desativar os dados pessoais nativos na plataforma.

**01.** No menu principal, clique em  **Painel de controle**.

**02**. Localize o agrupador **Segurança e acesso**.

**03**. Clique em  **Dados pessoais**.

**04.** Localize o registro a ser desativado.

**05**. Na linha correspondente ao dado pessoal, clique em **Des****ativar**, localizado na coluna **Ativo** para alternar a situação.

**06**. Na mensagem de confirmação, clique em **Desativar**.

#f2f2f2#f2f2f2

Ao desativar um dado pessoal, ele não será mais monitorado. Porém, todos os registros existentes sobre ele serão mantidos como histórico para auditoria.

## Ativar dado pessoal

---

**01.** No menu principal, clique em  **Painel de controle**.

**02**. Localize o agrupador **Segurança e acesso**.

**03**. Clique em  **Dados pessoais**.

**04.** Localize o registro a ser reativado.

**05**. Na linha correspondente ao dado pessoal, clique em **Ativar**, localizado na coluna **Ativo** para alternar a situação.

## Ver dado pessoal

---

trueimageVeja a imagem#0897E9INLINE

**01.** No menu principal, clique em  **Painel de controle**.

**02**. Localize o agrupador **Segurança e acesso**.

**03**. Clique em  **Dados pessoais**.

**04.** Localize o registro a ser visto.

**05.** Clique em **Visualizar**, localizado na coluna **Ações**.

**06**. Confira as informações desejadas.

oculto
$("b:contains('oculto')").parent().parent().hide();
]]>Fique atento!

Esta documentação é válida a partir da atualização **Voyager (2.0)**. Se você utiliza uma atualização anterior, ela pode conter informações diferentes das quais você vê na sua plataforma.
