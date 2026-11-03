---
content_hash: 035eac1ce4c0428ad52278b52c4771793f2438159d4b35f6d2019f31e9147277
fetched_at: '2026-06-29T00:09:32.654942+00:00'
page_id: '425458897'
product: rm
source: tdn-rm
title: Gerar Usuários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458897
version: 20
---

### Geral

Esta funcionalidade possibilita ao usuário do TOTVS EDUCACIONAL gerar usuários para  ou  associando-os a perfis previamente cadastrados que serão os responsáveis para indicar acessos em que o Usuário terá no sistema/portal.

Em parâmetros comuns é informado os perfis de segurança comuns  para todos os tipos de usuários (aluno, responsáveis e professor). Estes perfis são: acesso de conteúdos do portal,  TOTVS CRM,  TOTVS Gestão Bibliotecária e acesso de banco de dados.

Quando a geração de usuário for para aluno o usuário tem a possibilidade de  definir se será gerado usuário apenas para o aluno, apenas para responsáveis (pai, mãe e responsável acadêmico), responsável financeiro ou para o aluno e responsáveis juntos.

Não será gerado usuário para Pais do Aluno que estejam com o status **falecido**.

Os perfis de segurança do TOTVS Educacional, TOTVS Portal e a permissão  para acessar o sistema e o portal serão definidos pelo tipo de usuário que é gerado.

### Atribuir permissão à todos os níveis de ensino matriculados

Este parâmetro tem função de permitir que sejam atribuídas as permissões para todos os níveis de ensino para os quais o aluno possui matrícula.

### **Remover caracteres especiais do código do usuário**

O parâmetro **remover caracteres especiais do código do usuário** possui a função de remover ou não caracteres especiais do código do usuário durante o processo. Essa parametrização esta disponível para a geração de código de usuários do tipo: Aluno, Professor, Pesquisador e Funcionários. Essa parametrização pode ser realizada no processo de geração de usuários ou na parametrização para a sua geração automática.

Todo e qualquer caractere especial será removido do código do usuário, somente os caracteres de **A** a **Z**e/ou **a**a **z** e/ou **0** a **9** **não** serão removidos.

### Modo de geração do código do usuário

Durante o processo é possível definir o modo de geração do código do usuário. Este código será utilizado pelo usuário para realizar o login no sistema. Este código pode ser definido a partir do código da pessoa, Registro Acadêmico para aluno, Código do professor, Coligada, ou de forma personalizada. Para os responsáveis será gerado o código da pessoa ou personalizado apenas.

As opções **personalizadas** são informadas por prioridade, ou seja, existe uma definição hierárquica para geração do código. O sistema irá tentar gerar o código do usuário a partir do primeiro item informado, caso não seja possível, o sistema tentará gerar o código do usuário conforme o segundo item selecionado.  
O sistema gerará o código do usuário sem levar em consideração caracteres acentuados.

* Abaixo está uma lista dos tipos personalizados existentes para criação de usuário: Código da Pessoa Registro Acadêmico (R.A) Coligada + RA. Primeiro Nome . Último Nome Último Nome Primeiro Letra do Primeiro Nome + Último Nome Último Nome + Primeiro Nome CPF (somente números) Primeiro Nome + Último Nome + Sequencial
* A definição da senha do usuário poder ser feita de forma fixa, gerada aleatoriamente pelo sistema ou com a utilização da data de nascimento somente a parte numérica. A senha deverá respeitar os parâmetros de segurança configurados no menu "Ambiente -> Parâmetros -> Parâmetros Globais -> Segurança".
* Poderá ser definida uma validade para a senha, além de poder definir regras para segurança tais como: forçar a troca de senha a cada quantidade de dias válidos, possibilitar a obrigação ou não da alteração da senha ao realizar o primeiro "login" e "re-gerar" senha para usuários já existentes.

### **Validação da complexidade da Senha**

Somente será validado a complexidade da senha na inclusão de usuário, se marcado no menu "Ambiente -> Parâmetros -> Parâmetros Globais -> Segurança" o campo "Validar complexidade de senha no cadastro". A validação somente será feita em senha fixa, ou seja, no parâmetro "Educacional | Geração de usuários" estiver marcado o campo Senha igual a Fixa. Caso a validação da complexidade de senha estiver marcado, não será permitido utilizar tipo de senha igual a data de nascimento. **Importante:** quando for parametrizado para utilizar tipo de senha "Data de Nascimento", deverá ser desmarcado nos parâmetros globais a opção de validar a complexidade da senha, pois não se aplica a este caso. Situações para validação da senha: Será aplicado nas seguintes situações, de acordo com a configuração do menu "Parâmetros Educacional | Geração de usuário":

* Caso o tipo de senha seja "Fixa": Na inclusão de usuário (automático ou manual), o sistema somente irá validar a complexidade da senha se estiver marcado para "Validar complexidade da senha no cadastro" (menu Parâmetros Globais | Segurança). Na alteração de senha para usuários já gerados, a validação da complexidade de senha sempre será realizada, caso esteja configurado um dos itens dos parâmetros Globais de Segurança (tamanho da senha, caracteres numéricos, etc).

Caso esteja marcado "Data de nascimento": na criação de usuário (automático ou manual) não será possível realizar validação da complexidade da senha, portanto deverá ser desmarcado nos parâmetros globais a opção de validar a complexidade da senha.

### **Senha aleatória**

Na geração de usuário é possível marcar para gerar senha aleatória, entretanto para tal, é necessário criar um campo complementar para que a senha gerada seja gravada nesta campo.

A partir da versão 12.1.23, todas as senhas aleatórias passa a gerar com caracteres especiais para obedecer a política de senha forte do módulo Globais. Com isso, todas as senhas aleatórias são geradas com caracteres especiais.

### **Utilização do Nome Social**

Durante a geração do usuário é possível utilizar o nome social ao invés do nome civil, para isto é necessário utilizar o modo de geração do código como Personalizado. Depois marcar a opção [Utilizar nome social no lugar do nome civil], desta forma tanto o código quanto o nome do usuário será gerado com o Nome Social informado.

### **Geração automática**

A geração de usuários poderá ser feita de forma automática durante o cadastro de alunos. Para isso basta fazer a configuração nos parâmetros gerais do Educacional.

A geração automática para responsáveis (pai, mãe e responsável acadêmico) e responsável financeiro só será feita no momento da inclusão do aluno. Além disso, a inclusão de usuários dos responsáveis também será feita no momento da inserção destes, mesmo que o aluno já esteja cadastrado.

No cadastro do aluno, ao definir o aluno, pai, mãe ou responsável acadêmico como responsável financeiro, o usuário do respectivo registro de aluno, pai, mãe ou responsável acadêmico será reutilizado como usuário do responsável financeiro. Caso o registro de cliente/fornecedor correspondente ao responsável financeiro já exista na base de dados e tenha seu próprio usuário, o usuário desse registro de cliente/fornecedor será mantido.

Vale frisar que é passível o sistema adicionar mais um perfil no responsável financeiro quando estiver parametrizado a geração automática para aluno, responsáveis e responsável financeiro e cada um com um perfil associado, ao criar um aluno e vincular um pai o usuário do aluno e do pai é gerado automaticamente. Ao clicar no botão para que o pai seja responsável financeiro, o usuário do pai é associado ao cliente/fornecedor e o perfil de acesso parametrizado para o responsável financeiro é adicionado ao usuário já criado, ou seja, o usuário do pai / responsável financeiro terá dois perfis de acesso.

Veja Também

---

[Boletim Técnico - Opção personalizada de geração de usuários para responsáveis do aluno](http://tdn.totvs.com/display/LRM/RMEDU00004_EDU_BT_Geracao_Usuarios_Responsaveis_PCREQ-5166)
