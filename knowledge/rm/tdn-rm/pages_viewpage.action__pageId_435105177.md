---
content_hash: e3ed91d83044023a200ce2f538cde62cce24fc86b0ec81c530b4943bf622dbb5
fetched_at: '2026-06-29T00:09:48.503839+00:00'
page_id: '435105177'
product: rm
source: tdn-rm
title: Cadastros - Localização da Área do Imóvel
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105177
version: 4
---

O cadastro de localização de área permite que  uma determinada área, em específico, seja identificada dentro de um espaço físico. Através desta localização, será possível efetuar locações baseadas nas mesmas.

**Permissões necessárias:**

Para acesso a funcionalidade é necessário que o usuário esteja vinculado  a um Perfil de Usuários, com as permissões, a seguir, habilitadas:

* **03.02.01- Imóvel**
  + 03.02.01.01- Imóvel: Incluir
  + 03.02.01.02- Imóvel: Excluir
  + 03.02.01.03- Imóvel: Editar
  + 03.02.01.07- Imóvel: Alterar Situação
  + 03.02.01.08- Imóvel: Histórico

* **03.01.01.14- Localização da Área do Imóvel**
  + 03.01.01.14.01- Localização da Área do Imóvel: Visualizar
  + 03.01.01.14.02- Localização da Área do Imóvel: Incluir
  + 03.01.01.14.03- Localização da Área do Imóvel: Excluir
  + 03.01.01.14.04- Localização da Área do Imóvel: Editar

**Localização:**

* + Através do menu: [Projetos/ Incorporação/ Aluguel/ Cadastros/ Localização de Área do Imóvel]
  + Através do  Anexo de Áreas do Imóvel: [Incorporação/ Aluguel/ Imóvel/ Anexo- Área do Imóvel/ LookUp- Código da Localização da Área]
  + Através da funcionalidade Executar:

    - Titulo da Tela: Localização da Área do Imóvel
    - Action de Acesso: ImbLocalizacaoAreaImovelAction

**Vinculado aos registros:**

* + Conectado ao [Anexo- Área do Imóvel] : A conexão é feita através do campo [Código da Localização de Área]

**Ações Permitidas:**

* Incluir
* Visualizar
* Editar
* Excluir

**Campos da tela:**

* **Campo - Código**
  + Campo identificador do Registro
  + Bloqueado para preenchimento
  + Apresenta inicialmente o valor -1 quando um novo registro é solicitado
  + Gerado automaticamente pelo sistema, assim evita conflito de chaves.
  + Consegue gerar valores numéricos de até 4 dígitos
  + Preenchimento obrigatório.

* **Campo - Descrição**
  + Permite ao usuário inserir uma descrição para facilitar a identificação da Localização da Área
  + Campo de preenchimento obrigatório.
  + Permite a inserção de até 255 caracteres
