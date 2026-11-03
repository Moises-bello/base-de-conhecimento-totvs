---
content_hash: e309fde41c6f4bce0e16eab0825b64de2fa78fe8f88bca3a839f2d0ed11df5ef
fetched_at: '2026-06-29T00:12:08.369594+00:00'
page_id: '931598880'
product: rm
source: tdn-rm
title: Instituição do MEC
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=931598880
version: 33
---

# Introdução

A partir da versão **12.1.2506**, a **Instituição do MEC** passou a ser **global**.

Isso significa que a instituição **não está mais vinculada a um contexto específico** (como coligada, filial e/ou nível de ensino).

Porém, é necessário **configurar quais contextos utilizarão as instituições**, ou seja, **definir quais contextos a instituição representará**.

Após a atualização da versão, **todas as instituições serão desativadas automaticamente**. Portanto, será necessário **reativá-las (ou criar novas) e informar os contextos correspondentes**.

O local do cadastro também foi alterado. Agora, a **Instituição do MEC** pode ser acessada em:  
➡️ **Configurações | Configuração | Instituição do MEC**

# Inclusão/Contextos - Instituição do MEC

A tela **"Inclusão/Contextos"** da Instituição do MEC é utilizada para a **administração das instituições**.

Nela, é possível:

* **Incluir**, **excluir** e **editar** instituições.
* **Configurar os contextos** que a instituição representará.

Regras importantes:

* **Cada contexto** só pode ser associado a **uma única instituição**.
* Apenas podem ser incluídos **contextos que possuam o mesmo nível de ensino** da instituição.
* As Instituições de ensino superior que utilizam o **EducaCenso** devem ser vinculadas a instituições MEC de **nível básico**.
* O **Número do INEP** e o **Código E-MEC** são **únicos** e **não podem ser repetidos** em instituições diferentes.

Para acessar esta tela:  
➡️ **Configurações | Configuração | Instituição do MEC | Inclusão/Contextos**

## Processo - Ativar/desativar instituição do MEC

Este processo permite **ativar ou desativar** uma instituição a qualquer momento.

* Ao **desativar** uma instituição, **todos os seus contextos serão excluídos automaticamente**.
* **Não é possível incluir contextos** em uma instituição que esteja **inativa**.

Para acessar este processo:  
➡️ **Configurações | Configuração | Instituição do MEC | Inclusão/Contextos | Processos | Ativar/desativa instituição do MEC**

Para as instituições do MEC que possuem diretores e secretários cadastrados anteriormente à criação da Instituição Global, durante a execução do processo de ativar/desativar da instituição do MEC, será exibida a opção de definir onde esses registros serão gravados.

O usuário poderá optar por armazenar os diretores e secretários na filial (Filial|Dados Educacionais | Diretor por Filial), e/ou no cadastro de diretores da instituição de ensino, acessando Instituição MEC | Diretores por Instituição.

## Processo - Unificar instituições do MEC

Este processo permite **unificar duas ou mais instituições**.

* Ao executar a unificação, será necessário **escolher quais conjuntos de campos de cada instituição** serão utilizados para compor a **nova instituição** que será gerada.
* Os **anexos de todas as instituições** envolvidas no processo serão **movidos para a nova instituição**.
* Será preciso definir se as instituições utilizadas no processo serão **excluídas** ou **desativadas** ao final.

Regras importantes:

* **Não é permitido** unificar instituições com **níveis de ensino diferentes**.
* É necessário selecionar **pelo menos duas instituições** para realizar a unificação.
* Todos os **locais que utilizam qualquer uma das instituições envolvidas** serão **automaticamente atualizados** para utilizar a **nova instituição** gerada.

Para acessar este processo:  
➡️ **Configurações | Configuração | Instituição do MEC | Inclusão/Contextos | Processos | Unificar instituições do MEC**

Para as instituições do MEC que possuem diretores e secretários cadastrados anteriormente à criação da Instituição Global, durante a execução do processo de Unificar instituições do MEC, será exibida a opção de definir onde esses registros serão gravados.

O usuário poderá optar por armazenar os diretores e secretários na filial (Filial|Dados Educacionais | Diretor por Filial), e/ou no cadastro de diretores da instituição de ensino, acessandoInstituição MEC | Diretores por Instituição.

# Instituição do MEC

A tela **"Instituição do MEC"** permite **visualizar e alterar** todas as informações da instituição.

* **Não é possível excluir ou incluir** uma nova instituição por meio desta tela.
* O acesso será permitido **apenas à instituição que estiver configurada para o contexto logado**.
* **Todos os contextos configurados** para essa instituição **podem alterá-la**.

Para acessar esta tela:  
➡️ **Configurações | Configuração | Instituição do MEC**

No anexo [Autorização da instituição](https://tdn.totvs.com/pages/viewpage.action?pageId=602629333) foram realizadas alterações na tela a partir das versões 12.1.2502.222, 12.1.2506.169 e 12.1.2510.101.
