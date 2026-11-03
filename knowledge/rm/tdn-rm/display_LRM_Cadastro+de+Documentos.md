---
content_hash: 67319ca288e40385bae20c86cce248dc4e573e47e6c5b6ef5fba82befa109a55
fetched_at: '2026-06-29T00:09:31.762063+00:00'
page_id: '425458712'
product: rm
source: tdn-rm
title: Cadastro de Documentos
type: documentation
url: https://tdn.totvs.com/display/LRM/Cadastro+de+Documentos
version: 24
---

# Gerenciamento de Tipos de Documentos Solicitados pela Instituição

Esta tela permite cadastrar ou editar os dados dos tipos de documentos solicitados aos alunos pela secretaria da instituição de ensino.

Caminho no modulo Educacional :  Currículo e oferta | Auxiliares | Documentos

# Integração com Inteligência Artificial (IA)

A partir da versão **12.1.2506,** esta tela permite cadastrar ou editar os tipos de documentos solicitados aos alunos, agora com integração de inteligência artificial. A IA auxilia na validação automática e inteligente dos documentos, verificando consistência, autenticidade dos documentos.

Na lista de documentos integrados com IA, você pode selecionar um ou mais documentos para validação simultânea. Os documentos disponíveis são classificados em:

* **Documentos Conhecidos**: Modelos pré-definidos (como RG, CPF, Histórico Escolar)
* **Documentos Personalizados**: Modelos específicos da sua instituição

**Como funciona a validação múltipla:**

* Quando vários documentos são selecionados, o sistema processará a validação para todos simultaneamente
* Basta que UM dos documentos seja validado com sucesso para:

  + O status do documento do aluno ser automaticamente atualizado para "Validado"
  + O sistema considerar o processo concluído

**Pré-requisito:**

* Cadastre previamente os documentos seguindo as especificações em:  
    
  📄 **- Cadastro de Documentos Conhecidos e Personalizados**

Após cadastrar documentos do tipo Conhecido (modelos padrão) ou Personalizado (modelos institucionais), eles serão exibidos como opções no momento de:

* + Cadastrar novos documentos
  + Editar documentos existentes

Vide exemplo:

Para que o documento cadastrado possa ser validado por inteligência artificial, é necessário vinculá-lo a um **documento conhecido ou personalizado**. Essa vinculação deve ser feita selecionando, dentro da lista disponível, o documento ao qual ele estará associado para fins de reconhecimento e validação automática.

# **Documentos exigidos do Aluno**

Os documentos cadastrados nesta seção podem ser vinculados tanto ao cadastro do aluno quanto ao cadastro de seus responsáveis, conforme a necessidade da instituição.

Para utilizá-los especificamente no contexto do aluno, consulte a documentação disponível em:  

# **Processos de Validação pela Inteligência Artificial (IA)**

### Validação de documentos através do TOTVS Educacional:

A validação inteligente de documentos no TOTVS Educacional é realizada por meio de um processo automatizado , utilizando recursos de inteligência artificial para análise e classificação.

Todas as informações relacionadas a esse processo podem ser consultadas na documentação:

Para os documentos com status **Recusado**, mediante parametrização, será enviado automaticamente um e-mail, por meio da  [Central de Notificações](https://tdn.totvs.com/pages/viewpage.action?pageId=425458864) e do [eduCONNET](https://tdn.totvs.com/display/LRM/03.5+-+Cadastro+de+Mensagens), para o Aluno/Responsáveis informando quais documentos foram recusados e o motivo da recusa. Funcionalidade disponível a partir da versão 12.1.2506.128.

### Validação de documentos através da Matricula no Portal:

A validação inteligente de documentos através do portal é realizada no momento da matricula, utilizando recursos de inteligência artificial para análise e classificação.

Todas as informações relacionadas a esse processo podem ser consultadas na documentação:

### Validação de documentos  através do cadastro acadêmico no Portal:

A validação inteligente de documentos também pode ocorrer no cadastro acadêmico do aluno no portal.

Todas as informações relacionadas a esse processo podem ser consultadas na documentação:

### Motivos de Rejeição do documento:

Para as validações via portal é possível cadastrar motivos de rejeição dos documentos.

Todas as informações relacionadas e esse processo podem ser consultadas na documentação:

# **Visualização dos documentos exigidos ao aluno e status dos mesmos através do TOTVS Educacional**

O acompanhamento dos documentos exigidos para o aluno através do processo de matricula é realizado através do TOTVS Educacional.

Todas as informações relacionadas e esse processo podem ser consultadas na documentação:

Para os documentos com status **Recusado**, mediante parametrização, será enviado automaticamente um e-mail, por meio da [Central de Notificações](https://tdn.totvs.com/pages/viewpage.action?pageId=425458864)e do [eduCONNET](https://tdn.totvs.com/display/LRM/03.5+-+Cadastro+de+Mensagens), para o Aluno/Responsáveis informando quais documentos foram recusados e o motivo da recusa. Funcionalidade disponível a partir da versão 12.1.2506.128.
