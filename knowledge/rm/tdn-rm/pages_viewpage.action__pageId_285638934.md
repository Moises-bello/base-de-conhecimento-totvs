---
content_hash: ed0f10081581c7da693ae8bd2c7762bfeceb5fbf0af8627ebceffa51eab605be
fetched_at: '2026-06-29T00:08:37.902574+00:00'
page_id: '285638934'
product: rm
source: tdn-rm
title: Geral 1/3
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=285638934
version: 19
---

**Utilizar responsável por candidato na inscrição?** Este serviço possibilita a inscrição de candidatos por responsável. Esta opção será bem utilizada em Instituições que trabalham com processos seletivos que envolvem menores de 18 anos e precisam de um responsável para responder por eles. Consequentemente será necessário disponibilizar em campos do candidato o responsável financeiro, Dados do Pai e Dados da Mãe.

**Obrigatório responsável pela inscrição?**Este serviço obriga a inscrição de candidatos pelo responsável, não permitindo efetuar a inscrição sem preencher corretamente os dados do responsável da inscrição e forçando o preenchimento do responsável no inicio da inscrição.  Esta opção será bem utilizada em Instituições que trabalham com processos seletivos que envolvam menores de 18 anos e precisam de um responsável para responder por eles. Esta opção somente é liberada caso a opção "**Utilizar responsável por candidato na inscrição"**estiver selecionada.

**Texto do campo Treineiro:** determina o texto do campo Treineiro. Este campo fica visível na tela de inscrições do Portal. Se este parâmetro estiver vazio, o texto padrão será: “Após a divulgação dos resultados você NÃO estará com o 2º grau concluído? Ou seja, você é Treineiro?”.

Nesta tela existe uma área de configuração exclusiva para os responsáveis. Será possível definir se serão utilizados na inscrição.  
Podem ser parametrizados por checkbox com a opção de "Desconsiderar parametrização....". Se marcados ou Desmarcados, irão afetar os parâmetros de cada campo do responsável definidos em outra aba de parametrização de dados.

O parâmetro **“Exigir preenchimento do sobrenome”** tem como objetivo não permitir um Nome sem sobrenome no momento de cadastrar uma pessoa. Se desmarcado poderá ter somente o nome no cadastro.

O parâmetro **"Gravar dados em letras maiúsculas"** tem como objetivo gravar os dados no banco tudo em letras maiúscula, mesmo sendo informados minúsculas no momento da inscrição.

Para mais informações sobre o funcionamento do parâmetro **"Utiliza preenchimento obrigatório do Responsável Legal (Responsável Acadêmico)"**, acesse: <https://tdn.totvs.com/x/6BfpIQ>

Para mais informações sobre o funcionamento dos parâmetros "**Desconsiderar parametrização de obrigatoriedade para TODOS os campos do responsável**", acesse: <https://tdn.totvs.com/x/Gvv6E>

É também possível configurar se esse processo seletivo realizará busca dos dados de um candidatos que já existem na base. Caso algum desses critérios sejam marcados, ao acessar o novo portal na página de inscrições. O mini formulário irá carregar os campos de acordo com o parametrizado, para que o candidato digite seus dados e reutilize seus dados que já havia cadastrado anteriormente.

Para saber sobre mais comportamentos [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=284883738).

Importante

Caso sejam definidos a utilização dos dados do pai, mãe ou responsável acadêmico e a validação de unicidade () do TOTVS Gestão de Pessoas esteja definido para "nome, data de nascimento, estado natal e cidade natal", é recomendado que na  do processo seletivo, sejam também definidos estes campos como visíveis e obrigatórios.

Estes campos garantem a integridade do cadastro de pessoas no momento que o aluno for matriculado, seja pela central de candidatos ou através do processo de venda online de cursos.

Caso estes campos não sejam visíveis ou obrigatórios e não forem preenchidos, caso o sistema no momento da matrícula identifique alguma possível duplicidade ou inconsistência no cadastro, o responsável será ignorado na matrícula, ou seja, não será criado no cadastro de pessoa e não será vinculado ao aluno no TOTVS Educacional.

Caminho do parâmetro no TOTVS Gestão de Pessoas:

* TOTVS Gestão de Pessoas → Configurações → Parametrizador → 07.00 - Configurações → 07.00.00 - Gerais → 07.00.00.01 - Validações → Validar unicidade de Pessoa por.
