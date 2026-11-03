---
content_hash: 76563e8bd2574a8b1bd2a3433e6bea4fb3a1fc0814d218fd65fcbb3bfe91467d
fetched_at: '2026-06-29T00:10:08.899192+00:00'
page_id: '452719602'
product: rm
source: tdn-rm
title: Tipos de Requisição - RHU
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719602
version: 18
---

**Tipos de Requisição**

O RM Vitae possibilita o gerenciamento dos seguintes tipos de requisições:

* Aumento de quadro;
* Alteração de dados funcionais;
* Desligamento;
* Transferência;
* Transferência com Alteração de Dados Funcionais.
* Substituição;
* Treinamento;
* - Geral.

Os tipos de requisições são classificações obrigatórias para as requisições. Têm o propósito de qualificar a finalidade da requisição e permitir configurações gerais, aplicáveis às requisições de um mesmo tipo. Estes tipos são controlados internamente pelo sistema, sendo que é possível a criação de novos tipos que serão utilizados como finalidade na Requisição Geral. Contudo, o usuário do sistema tem condições de determinar quais tipos serão disponibilizados para uso configurando-os como habilitados ou desabilitados.

Os tipos viabilizam variações no funcionamento do processo de avanço de etapa, sendo a definição do fluxo pelo RM AGILIS ou não.

**Observações**

- A exclusão de tipos não é permitida para o usuário do sistema, independentemente das permissões de acesso.

- O mapeamento de etapas de um tipo de requisição somente pode ser realizado após preenchimento dos campos grupo de atendimento e tipo de atendimento.

- O percentual de aumento pode ser configurado diferentemente para cada tipo de requisição. Seu uso restringe-se às requisições de alteração de dados funcionais e de transferência com alteração de dados funcionais.

- O percentual de aumento é utilizado estabelecer um limite de aumento salarial. Este parâmetro será verificado pelo sistema sempre que o salário proposto pela requisição solicitar um aumento superior ao máximo estipulado. Nestes casos, o sistema sempre notificará o requisitante ou o aprovador atual.

- O controle do limite percentual de aumento não substitui o Controle de Lotação por Verba, nem tem qualquer relação com as validações pertinentes a este recurso do RM Vitae. Desta forma, ainda que o salário proposto na requisição esteja abaixo do percentual de aumento definido, a requisição continua sujeita às verificações do Controle de Lotação.

**Tipos de Fluxo de Repasse das Requisições**

**Importante**

Caso não seja utilizada a , Desconsiderar o item **2 - Não usando integração com o Agilis.**

Caso seja utilizada a  e utilize o fluxo de repasse da própria hierarquia, desconsiderar o item **1****- Usando integração com o Agilis.**

Caso seja utilizada a  e não utilize o fluxo de repasse da própria hierarquia Desconsiderar o item **2 - Não usando integração com o Agilis.**

Detalhes de sobre a  estão disponíveis na página **(Disponível a partir da versão 12.1.34)**

* **1 - Usando integração com o Agilis (Fluxo Padrão)**

**- Detalhamento de Campos:**

**Pasta Identificação**

**ID Requisição -**Este campo é gerado automaticamente pelo sistema e não pode ser editado.

**Ativo** - Este campo indica se o tipo de requisição está disponível para uso no sistema. Caso o tipo esteja inativo e não tenha pendencias de requisições suas ou para análise, o tipo deixará de ser visível no Portal. Caso tenha pendências de requisições ou para a análise, o tipo será exibido no Portal mas com a opção NOVA desabilitada.

**Tipo Requisição -**Neste campo deve ser informado o nome do tipo de requisição.

**Fluxo de Etapas Grupo de Atendimento -** Neste campo deve ser informado o grupo de atendimento já cadastrado no sistema. Caso haja licença do RM Agilis pode ser criado novos grupos de atendimento para serem utilizados nas requisições.

**Tipo de Atendimento -** Neste campo deve ser informado o tipo de atendimento já cadastrado no sistema. Caso haja licença do RM Agilis pode ser criado novos tipos de atendimento para serem utilizados nas requisições.

**Relatório Gerencial -**Neste campo pode ser informado o relatório de acordo com o tipo de requisição cadastrada. Nesta pagina é possível ver a estrutura do relatório: .

**Instruções para o portal -**As informações inseridas neste campos serão exibidas no portal na janela da requisição na parte inferior da página.

**Email Customizado -**Ao manipular as requisições através do fluxo, ao inserir emails customizados, estes serão disparados nos avanços de etapas, não sendo enviado então os emails padrão do produto (enviados quando não existem emails customizados cadastrados no tipo de requisição).

**Cód. Categoria -**Se estiver sendo criada ou editada uma requisição geral, ou seja, não seja uma requisição padrão do sistema e o parâmetro "*Considerar a nova requisição geral para o Meu RH*" estiver marcado, este campo será exibido. Neste campo deverá ser selecionada uma categoria de requisição pré-cadastrada. Esta categoria determina a qual grupo de requisições ela irá pertencer. Essa informação será utilizada nas solicitações no Portal Meu RH. Seu preenchimento é opcional.

**Subtítulo -** Se estiver sendo criada ou editada uma requisição geral, ou seja, não seja uma requisição padrão do sistema e o parâmetro "*Considerar a nova requisição geral para o Meu RH*" estiver marcado, este campo será exibido. Neste campo pode ser informado um subtítulo, contendo mais informações sobre a finalidade do tipo de requisição que será criada.  Essa informação será utilizada nas solicitações no Portal Meu RH. Seu preenchimento é opcional.

**Pasta Mapeamento Fluxo**

Esta pasta destina-se ao cadastramento, consulta e / ou alteração do mapeamento das etapas.

O mapeamento de etapas será possível quando houver integração com o RM Agilis, e existir pelo menos um fluxo de etapas pré-definido no RM Agilis.

Alterações no mapeamento de etapas serão permitidas se não existirem requisições do tipo correspondente com status "Em Andamento", já as alterações no status mapeado serão permitidas se este status não estiver em uso.

**Importante:** Ao definir através do parametrizador que se utiliza nas requisições usando integração com o Agilis **(),** caso não exista fluxo customizado no Agilis, as requisições manterem o fluxo de repasse do cadastro de chefes e supervisores, sendo necessária manutenção nas fórmulas para atender a regra de repasses da organização.

**Observação**

Os fluxos do RM Agilis são associados a cada tipo de requisição, sendo que estes fluxos são identificados, no RM Vitae, através do grupo e do tipo aos quais pertencem. As configurações que associam fluxos de aprovações com grupos e tipos devem ser realizadas no RM Agilis (Para definição deste fluxo acesse a opção: Cadastro | Atendimento | Tipos de Atendimentos | Tipos de Atendimentos | Fluxo de Tarefas).

**Pasta Parâmetros - Requisição Geral**

Os campos visualizados nessa pasta são cadastrados no RM Agilis e só serão preenchidos pelo RM Portal. No RM Agilis é definido em qual etapa um determinado campo estará disponível para preenchimento.  
  
  
**Pasta Permissões Meu RH - Requisição Geral**

Se estiver sendo criada ou editada uma requisição geral, ou seja, não seja uma requisição padrão do sistema e o parâmetro "*Considerar a nova requisição geral para o Meu RH*" estiver marcado e o usuário estiver vinculado a um perfil que tenha esta permissão habilitada, esta pasta será exibida.  
Estas permissões determinam quais perfis poderão solicitar esse tipo de requisição geral no portal Meu RH. 

* **2 - Não usando integração com o Agilis (**Fluxo da **)**

**- Detalhamento de Campos:**

**Pasta 'Identificação'**

**ID Requisição -**Este campo é gerado automaticamente pelo sistema e não pode ser editado.

**Ativo** - Este campo indica se o tipo de requisição está disponível para uso no sistema. Caso o tipo esteja inativo e não tenha pendencias de requisições suas ou para análise, o tipo deixará de ser visível no Portal. Caso tenha pendências de requisições ou para a análise, o tipo será exibido no Portal mas com a opção NOVA desabilitada.

**Tipo Requisição -**Neste campo deve ser informado o nome do tipo de requisição.

**Relatório Gerencial -**Neste campo pode ser informado o relatório de acordo com o tipo de requisição cadastrada. Nesta pagina é possível ver a estrutura do relatório: .

**Instruções para o portal -**As informações inseridas neste campos serão exibidas no portal na janela da requisição na parte inferior da página.

**Email Customizado -**Ao manipular as requisições através do fluxo, ao inserir emails customizados, estes serão disparados nos avanços de etapas, não sendo enviado então os emails padrão do produto (enviados quando não existem emails customizados cadastrados no tipo de requisição).

**Cód. Categoria -**Se estiver sendo criada ou editada uma requisição geral, ou seja, não seja uma requisição padrão do sistema e o parâmetro "*Considerar a nova requisição geral para o Meu RH*" estiver marcado, este campo será exibido. Neste campo deverá ser selecionada uma categoria de requisição pré-cadastrada. Esta categoria determina a qual grupo de requisições ela irá pertencer. Essa informação será utilizada nas solicitações no Portal Meu RH. Seu preenchimento é opcional.

**Subtítulo -** Se estiver sendo criada ou editada uma requisição geral, ou seja, não seja uma requisição padrão do sistema e o parâmetro "*Considerar a nova requisição geral para o Meu RH*" estiver marcado, este campo será exibido. Neste campo pode ser informado um subtítulo, contendo mais informações sobre a finalidade do tipo de requisição que será criada.  Essa informação será utilizada nas solicitações no Portal Meu RH. Seu preenchimento é opcional.

**Pasta 'Ações dos Níveis de Hierarquia para o tipo de Requisição':**

Nesta pasta será feita a construção de como serão realizados os repasses das Requisições do tipo editado.

Neste cadastro os itens poderão ser **Incluídos**, **Excluídos** e **Editados**.

Para a construção do fluxo, os repasses serão realizados de acordo com o  e todos os níveis que participarão dos repasses das requisições precisam ter um registro incluídos na aba **'Ações dos Níveis de Hierarquia para o tipo de Requisição'.**

**Detalhamento de Campos:**

**Nível de Hierarquia:** Deverá ser informado o  que terá acesso para realizar as manipulações das requisições definidas na caixa *Ações do Nível de Hierarquia para Requisições.*

**Ativo:** Representa se a Ação do Nível está ativa ou inativa.

**Ações do Nível de Hierarquia para Requisições**

**Participa do Fluxo de Repasse das Requisições:**Primeiramente deverá ser definido se o Nível da Hierarquia informado participa do fluxo de repasses das requisições. Caso a flag seja marcada as definições abaixo serão habilitadas.

**- Encaminha Requisição para próximo aprovador:**Caso esta flag seja marcada, significa que o ***Nível de Hierarquia*** definido poderá encaminhar as Requisições para o próximo aprovador.

**- Voltar Requisição para Aprovador anterior:**Caso esta flag seja marcada, significa que o ***Nível de Hierarquia*** definido poderá retornar as Requisições para o Aprovador anterior ao recebe-la através de um repasse.

**- Aprova Requisição:**Caso esta flag seja marcada, significa que o ***Nível de Hierarquia*** definido, poderá aprovar as Requisições ao recebe-la através de um repasse.

**- Reprova Requisição:**Caso esta flag seja marcada, significa que o ***Nível de Hierarquia*** definido, poderá Reprovar as Requisições ao recebe-la através de um repasse.

**Exemplo seguindo os níveis cadastrados conforme imagem abaixo:**

**Nível de Hierarquia Analista:**

Um funcionário que estiver em uma a qual o  seja **Analista** poderá abrir uma requisição e repassa-la ao seu **Gestor**.

**Não** poderá **retornar** requisições

**Não** poderá **aprovar** requisições

**Não** poderá **reprovar** requisições

**Nível de Hierarquia Gestor:**

Um funcionário que estiver em uma a qual o  seja **Gestor** poderá abrir uma requisição e repassa-la ao seu **Diretor**.

Poderá **retornar** a requisição para o funcionário do Nível de Hierarquia Analista.

**Não** poderá **aprovar** requisições

Poderá **reprovar** requisições

**Nível de Hierarquia Diretor:**

Um funcionário que estiver em uma a qual o  seja **Diretor**poderá abrir uma requisição e repassa-la ao seu **Vice Presidente**.

Poderá **retornar** a requisição para o funcionário do Nível de Hierarquia Gestor.

**Não** poderá **aprovar** requisições

Poderá **reprovar** requisições

**Nível de Hierarquia Vice Presidente:**

Um funcionário que estiver em uma a qual o  seja **Vice Presidente**poderá abrir uma requisição e repassa-la ao seu **Presidente**.

Poderá **retornar** a requisição para o funcionário do Nível de Hierarquia Vice Presidente.

**Não** poderá **aprovar** requisições

Poderá **reprovar** requisições

**Nível de Hierarquia Presidente:**

Um funcionário que estiver em uma a qual o  seja **Presidente**poderá abrir uma requisição. (Por ser o último nível cadastrado não terá um próximo repasse)

Poderá **retornar** a requisição para o funcionário do Nível de Hierarquia Vice Presidente.

Poderá **aprovar** requisições

Poderá **reprovar** requisições

**Pasta 'Permissões Meu RH - Requisição Geral':**

Se estiver sendo criada ou editada uma requisição geral, ou seja, não seja uma requisição padrão do sistema e o parâmetro "*Considerar a nova requisição geral para o Meu RH*" estiver marcado e o usuário estiver vinculado a um perfil que tenha esta permissão habilitada, esta pasta será exibida.  
Estas permissões determinam quais perfis poderão solicitar esse tipo de requisição geral no portal Meu RH. 

**Links Importantes e Complementares:**

* [Parametrizações RHU - Portal Meu RH](https://tdn.totvs.com/display/LRM/Portal+Meu+RH)
