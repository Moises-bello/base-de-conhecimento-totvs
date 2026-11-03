---
content_hash: dbd98526949fe6b820945870b1f189deaa413d24205975a9261f19e9ba909056
fetched_at: '2026-06-29T00:10:07.959748+00:00'
page_id: '452719484'
product: rm
source: tdn-rm
title: Banco de Talentos - Importação de Currículo LinkedIn
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719484
version: 6
---

ATENÇÃO!

Integração descontinuada a partir da versão 12.1.2306

###### **TOTVS Atração de Talentos**

###### A sua instituição ainda não está utilizando?

###### A solução TOTVS RH Atração de Talentos (ATS) simplifica o processo de Recrutamento e Seleção, promovendo a diversidade e acessibilidade tanto para empresas quanto para as pessoas candidatas. [Clique aqui](https://docs.google.com/forms/d/e/1FAIpQLScPeXUPg9OnaJoDD22iFOSoyRvqOcobZ6caP8yeh2eoROCdiA/viewform) para conhecer todos os detalhes.

**Banco de Talentos - Importação de Currículo LinkedIn**

Para a utilização desta funcionalidade é preciso que as seguintes parametrizações sejam efetuadas:

• **Parâmetros Globais:**

Acessar o Totvs Gestão de Pessoas: Ambiente > Parâmetros > Globais, aba: "Proxy do Twitter". Esta configuração será utilizada para fazer a integração com o LinkedIn. Devem ser informadas as configurações de Proxy definidas pela equipe de administração de rede da empresa.

• **Parametrizador do Totvs Gestão de Pessoas:**

Acessar o Totvs Gestão de Pessoas: Configurações > Parametrizador > RM Portal > Banco de Talentos.   
O lookup "Grau de Instrução para integração com LinkedIn" deve ser preenchido com o grau que será utilizado como padrão para as formações acadêmicas que forem importadas do LinkedIn. Isto é necessário em função do LinkedIn não conter esse tipo de informação, e a mesma é obrigatória no Banco de Talentos.

**Importando informações curriculares para o Banco de Talentos:**

O usuário, ao cadastrar seu currículo no Banco de Talentos do Portal, tem a opção de importar os dados de seu currículo já cadastrado na rede de relacionamentos "LinkedIn".  
No banco de talentos, ao criar seu currículo, na opção: "Página Inicial" é exibido o link:   
   
**"LinkedIn:** **Você pode importar os dados da sua conta no LinkedIn clicando aqui."**   
   
Nas opções "Experiência Profissional" e "Formação Acadêmica", existe outro link:   
   
**"Buscar experiência profissional do meu LinkedIn"**

O usuário poderá optar por clicar para buscar as informações do seu currículo existente no LinkedIn.

Ao clicar nesse link o sistema direciona o usuário para a tela de autenticação do LinkedIn, onde, após autenticado, serão recuperadas as informações profissionais e acadêmicas e estas são transcritas para o currículo do Banco de Talentos.

O usuário pode incluir mais informações, editar as informações já importadas ou excluir uma ou mais informações, se desejar.

É necessário que o navegador WEB tenha acesso ao site www.linkedin.com e que este site esteja disponível no momento da importação, sendo que, após importados os dados, não há atualização de dados automática (caso sejam alterados ou inseridos novos dados no Linkedin estes não replicarão automaticamente para o currículo do Banco de Talentos a não ser que o usuário repita o processo de importação).

**A importação de registros de Experiência Profissional são realizadas conforme abaixo:**

**Banco de Talentos                          LinkedIn**

Nome da empresa                                           Não será preenchida Outra empresa  Nome da empresa Admissão Admissão  Desligamento   Desligamento Atividades desenvolvidas    Cargo + Descrição

**A importação de registros de Formação Acadêmica são realizadas conforme abaixo:**

**Banco de Talentos                                                   LinkedIn**

Curso                                                                                                    Não será preenchido Outro curso

Área de estudo Entidade/Escola                                                          Não será preenchido Outra Entidade/Escola

 Nome da instituição de ensino

Início em                                                                                              Período (início)

Término em                                                                                         Período (término)

Andamento do curso                                                                           Informação inexistente

Grau de instrução relacionado                                                            Informação inexistente

Possui certificado ou diploma                                                             Informação inexistente

Observações/Informações complementares                                     Atividades e grupos + Notas adicionais
