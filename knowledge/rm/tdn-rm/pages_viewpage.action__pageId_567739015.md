---
content_hash: 31837cff1426a92e2a6738862646db026bafc66bd5fc654c67f7eaaf4597f97e
fetched_at: '2026-06-29T00:10:51.393060+00:00'
page_id: '567739015'
product: rm
source: tdn-rm
title: 6- Ocorrência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=567739015
version: 58
---

Nesta tela, o professor poderá visualizar e cadastrar ocorrências para os alunos de uma determinada turma/disciplina.

Permissão de acesso

Para acessar a funcionalidade, o perfil do professor deverá ter a permissão em:

**Serviços Globais | Segurança | Acesso | Perfil | Sistema: Educacional | Educacional (Portal) | Professor | Diário de classe | Cadastro de ocorrências.**

**Serviços Globais | Segurança | Acesso | Perfil | Sistema: Educacional | Currículo e Oferta | Acadêmico | Auxiliares | Grupo de Ocorrências.**

**Serviços Globais | Segurança | Acesso | Perfil | Sistema: Educacional |"Seleciona o Perfil"| Anexo | Parâmetros Educacionais | Ocorrências  - (marcar os grupos desejados)**

Configurar o quadro de ocorrências

Para configurar quais a colunas serão exibidas no quadro de ocorrências o usuário deve selecionar a engrenagem no canto superior direito em relação a tabela, conforme a imagem abaixo:

Um *sidebar* será aberto, aonde o professor(a) poderá visualizar as colunas disponíveis e, da esquerda para a direita, botões para:

* **Ocultar a coluna;**
* **Fixa-la;**
* **Posiciona-la previa ou posteriormente a outra coluna;**

Visualizar a ocorrência

Para visualizar as ocorrências cadastradas para um determinado aluno, deve-se clicar no ícone de expansão (seta para baixo) localizado ao final de cada linha.

Nessa tela, o professor poderá visualizar todos os dados das ocorrências cadastradas, como: **Grupo, Tipo, Data/Horário, Etapa, Descrição e Anexo**.

Os campos **(1.1) Descrição** e **(1.2) Anexo** possuem uma particularidade: o professor poderá clicar sobre eles para visualizar todo o conteúdo.

**1.1. Visualizar a descrição da ocorrência**

> Para visualizar o conteúdo do campo **Descrição**, o professor poderá acessar uma **prévia** ou **visualizar todo o conteúdo** da ocorrência.

**Prévia:**

> Para visualizar a prévia da descrição, basta posicionar o cursor do mouse sobre o link da descrição da ocorrência.

**Visualizar todo o conteúdo:**

> Para visualizar todo o conteúdo da descrição, basta clicar no link da descrição da ocorrência.

**1.2. Visualizar a relação e o conteúdo dos anexos cadastrados na ocorrência**

> Para visualizar a relação de anexos cadastrados na ocorrência, basta clicar no símbolo correspondente. Ao clicar, será exibida uma tela com a lista dos anexos associados à ocorrência.

Ainda nessa tela, o professor tem a opção de **realizar o download ou excluir os arquivos anexados**.

Para realizar o download, o professor deverá clicar no ícone . Ao clicar, será exibida uma **barra de progresso indicando o andamento do download do arquivo**.

Para excluir um arquivo, o professor deverá clicar no ícone . Em seguida, será exibida uma mensagem de confirmação. Após confirmar, o arquivo será excluído com sucesso.

Coluna de "Responsável ciente" - Ensino básicofalse

**Disponível apenas para o Contexto Ensino Básico**

A coluna de ciência do responsável é exibida apenas no contexto de Ensino Básico.

Cadastrar uma ocorrência

Para cadastrar uma nova ocorrência, preencha os campos **Grupo, Tipo** (este campo é carregado de acordo com o grupo selecionado), **Data, Etapa** e **Detalhes**, além de selecionar **um ou mais alunos** na listagem. Também é possível enviar **um ou mais arquivos anexos**. Para isso, clique no botão **Selecionar arquivo** e escolha o(s) arquivo(s) desejado(s). Após o preenchimento das informações, clique no botão **Salvar** para concluir o cadastro da ocorrência.

Tipo de Ocorrência

**Configurações importantes para a correta exibição dos Tipos de Ocorrência**

**1 – Configuração da permissão de visualização dos Grupos de Ocorrência**

> É necessário garantir que os **Grupos de Ocorrência** correspondentes estejam habilitados na tela **Parâmetros Educacionais > Ocorrências**.

**2 – Configuração de Status do Tipo de Ocorrência**

> Para que um **Tipo de Ocorrência** possa ser utilizado no cadastro, é necessário que **ambos os checkboxes de Status** estejam marcados.

Parametrização necessária para arquivos

No cadastro de uma ocorrência, o professor pode incluir arquivos. Para que isso seja possível, **duas configurações** precisam ser realizadas:

**1 – Configuração do tamanho máximo do arquivo**

> O tamanho máximo permitido para os arquivos das ocorrências do aluno é definido pelo parâmetro:  
> **Configurações > Parâmetros > Secretaria > Geral 1/7 > Tamanho máximo dos arquivos das ocorrências do aluno**.

Upload de arquivos grandes

Caso a instituição permita uploads no portal com tamanho superior ao tamanho padrão **30mb** do **IIS(Internet Information Services)**será necessário realizar algumas configurações adicionais. Saiba mais em

**2 – Extensões aceitas**

> Para definir os tipos de arquivos que podem ser anexados nas ocorrências, utilize o parâmetro: **Configurações > Parâmetros > Secretaria > Geral 6/7 > Extensões de arquivos permitidos**.

**3 – Armazenamento de arquivos**

> Os arquivos anexados durante o cadastro de uma ocorrência são armazenados diretamente na **base de dados**.

Configuração no ISS para suportar o envio de arquivo em lote.

É necessário verificar a configuração do **ISS** para que o portal do professor suporte o envio de arquivos para **vários alunos simultaneamente**. Para mais detalhes, consulte a seção [5- Configurar tempo de timeout do portal](https://tdn.totvs.com/pages/viewpage.action?pageId=837434579)

Editar a(s) ocorrência(s)

A partir da **listagem de ocorrências do aluno**, o professor pode **editar pontualmente** uma ocorrência. Para isso, clique nos **três pontinhos** na última coluna da linha da ocorrência e selecione a opção **Editar**.

Após clicar em **Editar**, o portal exibirá uma tela contendo todas as informações da ocorrência selecionada.

Excluir a(s) ocorrência(s)

**1. Excluir uma ocorrência individual:**

> Para excluir uma ocorrência, clique nos **três pontinhos** na última coluna da linha correspondente e selecione a opção **Excluir**.

**2 – Excluir múltiplas ocorrências**

> Para excluir mais de uma ocorrência, selecione os **checkboxes** correspondentes na listagem ou utilize o **checkbox do topo da tela** para selecionar todas as ocorrências visíveis.  
> Em seguida, clique no botão **Excluir**.

Ocorrência com aceite do responsável do aluno - Ensino básicofalse

**Disponível apenas para o Contexto Ensino Básico**

Se o responsável do aluno já tiver dado ciência da ocorrência e o professor não possuir a permissão **'Permitir alterar ou excluir ocorrências com aceite do responsável'** em seu perfil, a exclusão não será permitida.
