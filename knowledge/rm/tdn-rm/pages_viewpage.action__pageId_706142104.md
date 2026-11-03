---
content_hash: 66f19695d1eb6d58d21781ff28e908f62d460ac7c3c93180bb344bb411d50ff8
fetched_at: '2026-06-29T00:11:23.035480+00:00'
page_id: '706142104'
product: rm
source: tdn-rm
title: Configuração de Consulta SQL como Objeto de Negócio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=706142104
version: 31
---

# Introdução

---

O objetivo dessa página é mostrar como tornar uma **Consulta SQL** em um **Objeto de Negócio** de forma a fornecer dados para o **Smart View**.

Configuração - Smart Client

Para ambientes **Smart Client,**pode ser necessário configurar o DNS externo no RM.exe via atributo nas configurações:

xml
]]>

# Etapas

---

**Primeiro passo:** Na listagem de *Consultas SQL (Visões de Dados)*, clique com o botão direito sobre a **Consulta SQL** que se deseja associar a um Objeto de Negócio. Então selecione o menu "*Outras Informações*" e em seguida clicar em "*Objetos de Negócio de Consulta SQL*":

Outra forma é selecionar a Consulta SQL e em seguida clicar em *"Anexos/Objetos de Negócio de Consulta SQL"*:

Apenas perfis com permissão à edição de Consultas SQL possuem acesso à criação/edição de **Objetos de Negócio de Consulta SQL**.

Logo então, o módulo de **Objeto de Negócio de uma Consulta SQL** será exibido, possibilitando a edição ou criação de um novo *Objeto de Negócio* a partir daquela *Consulta SQL*

false

Este processo é realizado em 3 partes, sendo:

1. **Preenchimento das informações do Objeto de Negócio;**
2. **Confirmação dos tipos de dados do esquema e dos parâmetros da Consulta SQL;**
3. **Seleção dos perfis para permissão de acesso ao Objeto de Negócio;**

Em todas as etapas é exibido o status do Objeto de Negócio. **Inicialmente ele é criado como inativo**, sendo ativado apenas após a confirmação do esquema e dos parâmetros da Consulta SQL.

Caso a *Consulta SQL* seja editada e seus parâmetros ou campos sejam modificados, o Objeto de Negócio será desativado e não aparecerá mais para uso no **TReports** enquanto não for acessado o módulo **Objeto de Negócio de uma Consulta SQL** e validada a etapa de **Esquema e Parâmetros**

## Informações do Objeto de Negócio

---

Ao acessar a interface de criação de objeto de negócio serão exibidos os campos para preenchimento das informações:

* **Nome** -  Nome do Objeto de Negócio - Este é o nome que será exibido no **TReports** para seleção do Objeto de Negócio
  + **Preenchimento obrigatório**
  + **Mínimo de caracteres:** 4
  + **Máximo de caracteres:** 64
* **Descrição** - Descrição do Objeto de Negócio
  + *Preenchimento opcional*
  + **Máximo de caracteres:** 1024

ÁreaNesta etapa também é exibida a informação da **Área** do **Objeto de Negócio.** No caso de Consultas SQL, esta é definida com base no sistema a qual a Consulta SQL foi criada (no **TReports**os Objetos de Negócio são organizados por área e por isso, essa informação é buscada automaticamente.

## Esquema e Parâmetros da Consulta SQL

---

Nesta etapa é necessário  validar o mapeamento de campos e parâmetros da Consulta SQL para o Objeto de Negócio. É necessário preencher as seguintes informações para cada propriedade e parâmetro exibido:

* **Nome Amigável:** É como a propriedade será exibida no TReports. Por padrão é preenchida com o nome do campo na Consulta SQL, mas é possível personalizá-lo para aparecer de forma diferente no TReports, ao preencher essa informação.
  + Tamanho máximo de 40 caracteres;
  + **Não pode ser nulo ou vazio**;
* **Tipo:**É o tipo de dados das propriedades e parâmetros da Consulta SQL. Este campo é importante pois é ele que definirá como o dado será recebido, tratado e manipulado pelo TReports.
  + **É necessário que todas as propriedades/parâmetros tenham um tipo definido.**

Tipos de dados possíveis

O RM tentará descobrir/resolver o tipo da propriedade/parâmetro automaticamente, porém pode ser que este descobrimento não seja possível ou que o usuário deseje que o campo seja interpretado de forma diferente pelo TReports. Neste caso, é necessário que o usuário escolha o tipo compatível com a propriedade/parâmetro dentre as opções listadas abaixo:

* **Boolean**
* **Byte;**
* **DateTime**
* **Decimal;**
* **Double;**
* **Int16;**
* **Int32;**
* **Int64;**
* **Single;**
* **String;**
* **UInt16;**
* **UInt32;**
* **UInt64**
Ativando o Objeto de NegócioApós validar e salvar as propriedades e os parâmetros com os tipos definidos, o Objeto de Negócio passa a ficar **ativo**e já está pronto para ser utilizado no TReports

## Segurança

---

Um Objeto de Negócio, como todo objeto do RM, possui a segurança atrelada aos perfis que lhe foram atribuitos, e dessa forma, nesta etapa devem ser definidas as permissões de acesso ao Objeto de Negócio. Essa definição pode ser feita de duas formas:

1. **Permitir acesso à Perfis selecionados;**
2. **Permitir acesso à todos os usuários;**

Ambas as permissões são **válidas apenas para usuários que possuam perfil no Sistema em que a Consulta SQL** que deu origem ao Objeto de Negócio foi criada.

### Permitir Perfis

Para escolher os perfis que terão acesso ao Objeto de Negócio, **o switch disponível na interface deve estar na posição "Apenas selecionados"**. Com isso, em **"Perfis permitidos"** será habilitado um lookup (ícone de lupa) que abre uma tela de pop-up onde são listados os 10 primeiros perfis existentes no Sistema em que a Consulta SQL foi criada. Para visualizar os demais perfis, deve-se clicar em **"Carregar mais resultados"** até que o perfil desejado seja exibido.

Em seguida, deve-se selecionar os perfis que se deseja dar permissão e clicar no botão **"Selecionar".** Com isso o pop-up será fechado, retornando para a tela de Segurança.

### Permitir Todos

Caso deseje que todos os usuários com perfil no Sistema em que a Consulta SQL foi criada, marque esta opção. Ela não irá apagar os perfis já anexados, porém não os levará em conta e permitirá que qualquer perfil no Sistema da Consulta SQL acesse este Objeto de Negócio

Para concluir a permissão, deve-se clicar no botão **"Salvar"**ou em "**Salvar e Fechar".  
  
Ao utilizar parâmetro dinâmico no Objeto de Negócio o mesmo irá respeitar a permissão proposta, segue exemplo:**Usuário possuir permissão somente na Coligada 9:Criado Objeto com a seguinte consulta SQL:Veja que o parâmetro corresponde a coligada corrente $CODCOLIGADA.Ao executar no Smart View: **Exemplo 1:**Será apresentado lookup somente com a coligada que o usuário possui permissão ou o modulo. **Exemplo 2:**

O usuário dispõe de permissão na **Coligada 1**, no módulo **Folha**, e na **Coligada 9**, no módulo **Financeiro**.

Durante a execução da **ON**, serão consideradas exclusivamente as permissões vinculadas a cada módulo em suas respectivas coligadas. No **lookup**, será apresentada apenas a coligada correspondente ao módulo de criação.

**Observação:**  
Ao compartilhar ON's para usuário que não possuem permissão ao Objeto de Negócio o mesmo não irá ser executado, demonstrando o seguinte erro na tela:

# Apagar o Objeto de Negócio

---

Após a criação do Objeto de Negócio, já na primeira etapa, é disponibilizado um botão quer permite apagá-lo. Ao clicar nesse botão é exibida uma janela de confirmação. Caso seja confirmado através do botão "Apagar", o Objeto de Negócio será excluído e a interface de criação/edição será fechada.

Após apagar um Objeto de Negócio, não é possível recuperá-lo.

# Limitações

---

**Não é possível gerar Objeto de Negócio** de Consultas SQL que possuam:

* Fórmulas;
* Stored Procedures que utilizem parâmetros;

Na Consulta SQL, **não se deve utilizar ALIAS contendo caracteres especiais** para nomear campos, pois o Smart View suporta nomes apenas com caracteres alfanuméricos. Nesses casos podem ocorrer erros de importação ou duplicação de recursos.

Abaixo um exemplo de consulta utilizando ALIAS com caracteres especiais:

sql

No exemplo acima o ALIAS [FUNÇÃO DO FUNCIONÁRIO] irá gerar erros no Smart View.

Recomenda-se que os nomes sejam ajustados na etapa de configuração do Esquema no fluxo de criação/edição do Objeto de Negócio, onde é possível determinar o Nome Amigável de cada campo.

# Observações

---

Caso a Consulta SQL associada a um Objeto de Negócio tenha sido editada de forma a modificar seu esquema ou parâmetros, o Objeto de Negócio será desativado e será necessário validar novamente essas informações. Nesse caso, ao clicar em "Salvar" será exibida a mensagem de alerta abaixo. que possibilita o acesso à interface de edição do Objeto de Negócio:

Índicefalsefalse

**Produto:** Framework

false

**Versão:** 12.1.2302

false

**Processo:** Integração com o

falsefalseStatus

YellowEM DESENVOLVIMENTO

falseAutores
