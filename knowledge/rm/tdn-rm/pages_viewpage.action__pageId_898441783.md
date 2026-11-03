---
content_hash: d6b14bc6438bbdc7ec74d57f93e6b3c22f716517f58b28df27cb5b58436d024b
fetched_at: '2026-06-29T00:12:01.691753+00:00'
page_id: '898441783'
product: rm
source: tdn-rm
title: 01 - Regras de comunicação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=898441783
version: 64
---

# Sumário

---

Sumário

# Objetivo

---

A **Regra de Comunicação** tem como objetivo definir políticas e comportamentos que serão aplicados ao usuário autenticado no Portal Gestão Educacional durante o envio de mensagens pela Central de Comunicação.

Essas regras podem ser configuradas para atender usuários específicos ou perfis previamente definidos.

Para que o usuário possa enviar mensagens pela Central de Comunicação, é imprescindível que ele esteja associado a uma Regra de Comunicação ou a um perfil que possua uma regra vinculada.

Recomendamos acessar a  [documentação](https://tdn.totvs.com/display/LRM/02+-+Envio+de+Mensagens) para conhecer a funcionalidade do [envio de mensagens](https://tdn.totvs.com/display/LRM/02+-+Envio+de+Mensagens) da Central de Comunicação do Portal Gestão Educacional

# Pré-requisitos

---

Para que o menu "Regras de Comunicação(PGE)" seja exibido, é necessário acessar o **Cadastro de Perfis** e conceder a permissão correspondente.

Somente os usuários autorizados terão acesso ao menu e à tela de envio de mensagens.

O cadastro da Regra de Comunicação está disponível em: **Educacional**> **Atividades Acadêmicas** >**Central de Comunicações**> **Regra de Comunicação (PGE)**.

O **cadastro de regra de comunicação** é global e não está vinculado a nenhum contexto específico (como coligada, filial ou nível de ensino).  
Seu objetivo é estruturar regras de comunicação que poderão ser aplicadas a perfis ou a usuários específicos associados ao cadastro.  
Se um usuário “X” tiver acesso ao cadastro de regra de comunicação, ele visualizará o menu correspondente em qualquer contexto no qual possua permissão.

# Regra de comunicação

---

Segue abaixo as informações que compõem o cadastro. As particularidades serão abordadas posteriormente.

Meu eduCONNECT

**Exibição da opção "Meu eduCONNECT"**

* Para que consiga utilizar a opção **Meu eduCONNECT** na Regra de Comunicação, é necessário ativar a integração com eduCONNECT (Educacional > eduCONNECT), e após isso conseguirá habilitar na **Regra de Comunicação**a opção: **Permitir enviar para todas as categorias?**.

  Habilitar validade das Categorias eduCONNECT

  **[Recurso previsto para a versão 12.1.2602]**

  Esta melhoria tem como objetivo permitir que mensagens enviadas pelo **Portal de Gestão Educacional (PGE)**, que estejam marcadas para utilizar o **Meu eduCONNECT** e tenham a categoria selecionada, possuam uma validade configurável. Essa validade define por quanto tempo a mensagem ficará disponível no aplicativo após o envio.

  ⚠️ **Importante:** Essa funcionalidade **é válida apenas para mensagens enviadas via PGE**.

  ### **Comportamento Padrão**

  + Categorias já cadastradas antes da atualização permanecem com a validade desabilitada.
  + Se o parametro **Habilitar validade** estiver **desmarcado**, o comportamento das mensagens **permanece inalterado** (sem expiração).

  ### **Validade Ativada**

  + Quando a validade estiver ativada, os campos **`Tipo de validade`** e `Duração` tornam-se obrigatórios.
  + A duração da validade é contada a partir do **momento do envio da mensagem**.
  + Mensagens expiradas **não ficarão acessíveis no app**.
Filtro predefinido

É possível configurar na **Regra de Comunicação** se ela permitirá a utilização de filtros predefinidos, bem como definir a forma de identificação desses filtros.

Os filtros predefinidos são representados por consultas SQL previamente cadastradas no sistema RM. Ao utilizar um filtro predefinido, caso o mesmo seja selecionado pelo usuário final, o sistema enviará mensagens para todos os usuários retornados pela consulta SQL associada.

É importante ressaltar que, por padrão, as consultas SQL utilizadas nos filtros predefinidos devem **obrigatoriamente retornar as colunas** `EMAIL` e `CODUSUARIO`, pois elas são essenciais para o envio da comunicação.

Além disso:

* É **obrigatório** que todas as **consultas** possuam **contexto**, composto pelas colunas: `CODCOLIGADA`, `CODFILIAL` e `CODNIVELDEENSINO`.
* Quando a comunicação for enviada **para o Meu eduCONNECT**, também é obrigatório incluir a coluna `IDCATEGORIA`.
* Outras colunas devem estar presentes conforme a necessidade de substituição de **tags dinâmicas**, como `EMAIL`, `CODUSUARIO` e demais informações personalizadas já documentadas.

**Configuração de Consultas SQL para Filtros Predefinidos**

Nem todas as consultas SQL cadastradas no sistema RM devem estar disponíveis para seleção nos filtros predefinidos. Para atender a essa necessidade, foi criada uma funcionalidade que permite identificar, por meio de **TAGS**, quais consultas poderão ser utilizadas pelos usuários no Portal Gestão Educacional.

As consultas SQL disponíveis para seleção serão apenas aquelas que contiverem no título as TAGS configuradas.

São consideradas somente consultas SQL cadastradas para o sistema TOTVS Educacional

**Definição de TAGS**

Para que uma TAG seja identificada e apresentada para seleção, ela deve ser adicionada ao título da consulta seguindo o padrão:  
**`#NOMEDATAG#`.**

Exemplo

**Considere o seguinte exemplos de Consultas Cadastradas com TAGS:**

* `#PROFESSORES# Professores do curso de Ciência da Computação`
* `#PROFESSORES# Professores do curso de Medicina`
* `#COORDENADORES# Coordenadores do turno da manhã`
* `#ALUNOS_FORMANDO# Alunos formando ano 2025`

**Considerando o exemplo acima estarão disponíveis para Seleção as TAGS:**

* `#PROFESSORES#`
* `#COORDENADORES#`
* `#ALUNOS_FORMANDO#`

**Aplicação na Regra de Comunicação**

Se a TAG **`#ALUNOS_FORMANDO#`** for selecionada em uma Regra de Comunicação, o usuário vinculado a essa regra poderá visualizar e selecionar no filtro predefinido a consulta:

* `#ALUNOS_FORMANDO# Alunos formando ano 2025`
Aprovação

Será possível configurar se a **Regra de Comunicação** exige que a mensagem passe por um processo de aprovação antes de ser enviada. Caso a aprovação seja necessária, será obrigatório identificar quais usuários serão responsáveis por realizar essa aprovação.

É possível definir mais de um usuário para ser responsável pela aprovação da mensagem.

A regra permite associar mais de um aprovador. No entanto, a mensagem será considerada aprovada assim que o primeiro aprovador realizar a aprovação, não sendo necessário que todos os aprovadores o façam.

Troca e Inclusão de Aprovadores em Regras Existentes

Considerando uma regra já cadastrada, o usuário de aprovação pode ser substituído por outro ou novos usuários podem ser adicionados. Nesses casos, são aplicados tratamentos específicos, considerando a possibilidade de existirem mensagens ainda pendentes de aprovação.

**Removendo Usuário Aprovador**

Quando um ou mais aprovadores são **removidos** de uma regra:

* As requisições de aprovação pendentes desse usuário **serão removidas** se ele **não for mais aprovador** em nenhuma outra regra que cubra o tipo de mensagem afetado.

Observação:

A aprovação pendente só será removida se o usuário excluído perder completamente a função de aprovador para aquele tipo de mensagem, inclusive em outras regras de comunicação. Isso ocorre desde que os usuários ou o perfil da regra alterada não façam parte de outra regra em que o usuário também seja aprovador, evitando, assim, que ele continue visualizando pendências que não poderá mais resolver.

**Novos Usuários Provadores (Inclusão)**

Quando um ou mais aprovadores são **adicionados** a uma regra:

* O sistema identifica todas as mensagens que **já estão no fluxo de aprovação** e se enquadram nos critérios da regra (mensagens enviadas para o mesmo tipo de comunicação da regra e que o autor seja um dos usuários ou faça parte do perfil vinculado a regra alterada).
* Para cada mensagem pendente identificada, o sistema **cria uma nova requisição de aprovação** com status **"Aprovação Pendente"** para o aprovador recém adicionado.
* Após a criação das requisições, o sistema envia **notificações internas via e-mail** para os novos aprovadores sobre as pendências que foram atribuídas a eles.

**Gestão de Mensagens – PGE**

* Se o usuário for um aprovador, poderá visualizar na Gestão de Mensagens: suas próprias mensagens, as mensagens que já aprovou e aquelas que possuem requisição de aprovação direcionada a ele.
* Se o usuário já foi aprovador, mas não é mais em nenhuma regra, poderá visualizar apenas suas próprias mensagens e as mensagens que já aprovou.
 Mudança na opção "Precisa de aprovação antes do envio?"

A opção **“Precisa de aprovação antes do envio? ”** não poderá ser desabilitada se houver mensagens pendentes de aprovação vinculadas à regra em alteração.  
Nessa situação, será exibida uma mensagem de erro orientando o usuário a cancelar ou excluir as mensagens, ou solicitar que um dos aprovadores as reprove.

Exclusão da regra

A regra não poderá ser excluída se houver mensagens pendentes de aprovação vinculadas à regra.  
Nessa situação, será exibida uma mensagem de erro orientando o usuário a cancelar ou excluir as mensagens, ou solicitar que um dos aprovadores as reprove.

Permissões

Será necessário indicar, no mínimo, um **perfil** ou **usuário** para o qual a **Regra de Comunicação** será aplicada.

Caso seja informado um perfil, é importante ressaltar que a regra será aplicada a todos os usuários vinculados a esse perfil.

Serão apresentados apenas os **perfis** e **usuários** que possuam acesso a algum contexto educacional.

Filtro avançadoPermissão "Filtro Avançado"

Os campos disponíveis na aba **"Filtro Avançado"** no cadastro da **Regra de Comunicação** ficarão habilitados somente para os usuários que possuem a **permissão específica habilitada no perfil de acesso vinculado ao seu usuário no RM**.

> 📌 **Importante:**  
> Se os campos estiverem desabilitados, verifique com o administrador do sistema se a permissão correspondente foi atribuída ao perfil do seu usuário.

Essa medida visa garantir um controle mais restrito e seguro sobre a configuração avançada das regras de comunicação.

**Visão Geral**

O **filtro avançado** permite que a instituição configure critérios específicos (filtros) para controlar quais informações serão disponibilizadas para **usuários vinculados a uma regra de comunicação**.

Em outras palavras, na **Central de Comunicação** do **Portal de Gestão Educacional**, as opções disponíveis para seleção (como coligada, curso, turno, etc.) devem respeitar os filtros definidos na regra de comunicação do usuário.

Considerações Importantes

1. O filtro avançado **não é obrigatório**

Se nenhuma regra de comunicação com filtro for configurada, a Central de Comunicação utilizará as **permissões de contexto** do cadastro do usuário (coligadas, filiais e níveis de ensino permitidos).

**Exemplo:**  
Usuário com acesso à **Coligada 1**, **Filial 2** e **Ensino Superior** verá somente as informações correspondentes a esse contexto.

2. Quando existe filtro na regra, ele **sobrepõe** as permissões de contexto

Se a regra de comunicação possuir um filtro configurado, ele será **prioritário**, e a Central de Comunicação **ignora as permissões do cadastro do usuário**.

3. Preenchimento flexível dos filtros

Não é necessário preencher **todos os campos** de filtro. O sistema permite flexibilidade conforme a necessidade da instituição.

**Exemplos de configurações válidas:**

* Coligada e Filial
* Coligada e Curso
* Coligada, Curso e Turno
* Apenas Coligada

⚠️ **Importante:** Para qualquer outro filtro (como curso, turno, habilitação, etc.), o preenchimento da **coligada** é obrigatório.

Um mesmo usuário pode ter **várias regras de comunicação vinculadas**. Quando isso acontece, **todas as regras são unificadas** e os filtros funcionam de forma **inclusiva e permissiva**.

Dicas e Exemplos

✅ 1. Quando o usuário possui regra(s) de comunicação, mas nenhum filtro está vinculado a essas regras:  
O sistema utilizará os filtros de contexto padrão definidos no cadastro do usuário (por exemplo: coligada, filial, nível de ensino, etc.).

Esse comportamento garante que, mesmo com regras configuradas, o envio respeite os acessos padrões do usuário.

✅ 2. Quando o usuário possui regra(s) de comunicação com filtros vinculados:  
Neste caso, os filtros definidos na regra de comunicação sobrepõem os filtros de contexto do usuário.

O envio de mensagens será restrito aos dados que correspondem aos filtros parametrizados nas regras.

📌 Importante:  
Se o usuário possui acesso a múltiplas coligadas e filiais no seu perfil, é recomendável que existam regras de comunicação abrangendo todas essas variações. Caso contrário, o envio será limitado apenas às coligadas/filiais configuradas nas regras.

🧩 Exemplo prático (cenário de sobreposição por filtro específico):  
Usuário João tem acesso no perfil para:

Coligada: 1

Filial: 2

Nível de Ensino: Básico

Contudo, está vinculado à seguinte regra:

Regra de Comunicação com filtro apenas para:

Coligada: 7

Filial: 3

➡ Neste caso, João poderá enviar mensagens apenas para Coligada 7 / Filial 3, pois essa é a regra ativa.  
Para que ele possa enviar mensagens também para Coligada 1 / Filial 2, é necessário incluir essas informações em uma nova regra de comunicação.

🔁 3. Prioridade entre regras da mesma coligada  
Outro ponto importante sobre a lógica de aplicação das regras:

✅ Regras com apenas a coligada configurada (sem outros filtros) têm prioridade sobre as demais regras da mesma coligada.  
📌 Exemplo de prioridade:

Regra 1: Coligada 1 (sem outros filtros)

Regra 2: Coligada 1 + Filial 2

➡ Neste caso, a Regra 1 terá prioridade e irá sobrepor as demais regras da mesma coligada, como a Regra 2.

➕ 4. Regras com múltiplos filtros são combinadas de forma inclusiva  
Quando não há uma regra exclusiva com apenas a coligada informada, os filtros das demais regras são aplicados de forma inclusiva,  
combinando as diferentes configurações de filtros para formar o conjunto final.

📌 Exemplo de combinação inclusiva:

Regra 1: Coligada 1 + Filial 2 + Nível de Ensino: Básico

Regra 2: Coligada 1 + Filial 3

➡ O usuário poderá enviar mensagens tanto para Filial 2 (Ensino Básico) quanto para Filial 3 (Qualquer nível de ensino),   
desde que ambas pertençam à Coligada 1.

Envio de Mensagens com Filtro Avançado

No envio de mensagens pela **Central de Comunicação**, quando o usuário utiliza o **filtro avançado**, a **única informação obrigatória** a ser preenchida é o **“Período Letivo”**.  
Nesse caso, o usuário pode simplesmente informar o período letivo e clicar em **Enviar**.

O sistema irá, então, identificar todas as **matrículas vinculadas** ao período letivo informado e, de acordo com o **público-alvo selecionado**, enviará a mensagem.

⚠️ Consideração Importante

Quando o usuário que está enviando a mensagem possui **filtros definidos em suas regras de comunicação**, o sistema irá considerar **implicitamente esses filtros**, mesmo que eles **não tenham sido preenchidos manualmente** na tela de envio.

Ou seja, os dados exibidos ou a mensagem enviada serão **limitados pelos filtros da regra de comunicação do usuário**, ainda que a interface mostre apenas o período letivo preenchido.

**Abaixo seguem exemplos de cenários e como as regras são aplicadas:**

Exemplos

**✅ Exemplo 1 – Sem filtro avançado configurado para o usuário**

**Contexto do usuário:**

* Coligada: 1
* Filial: 2
* Nível de Ensino: Ensino Superior

**Ação:**  
O usuário informa apenas o **Período Letivo: 2024/2** e envia a mensagem.

**Resultado esperado:**  
A mensagem será enviada para **todos os alunos** vinculados à Coligada 1, Filial 2, Ensino Superior, no período letivo 2024/2, conforme o contexto de permissão do usuário.

---

**✅ Exemplo 2 – Com filtros de regra de comunicação aplicados**

**Regra de comunicação vinculada ao usuário:**

| ID da Regra | Coligada | Filial | Nível Ensino | Curso | Turno |
| --- | --- | --- | --- | --- | --- |
| 101 | 1 | 2 | Ensino Superior | CONT | Manhã |

**Ação:**  
O usuário informa apenas o **Período Letivo: 2024/2** e envia a mensagem.

**Resultado esperado:**  
A mensagem será enviada **apenas** para os alunos do curso **CONT**, na **Filial 2**, **Turno Manhã**, no período letivo **2024/2**.  
Mesmo que o usuário tenha acesso a outros cursos ou turnos via contexto, o sistema **restringe o envio** com base nos filtros definidos na regra de comunicação.

---

**✅ Exemplo 3 – Regra permissiva por nível de ensino**

**Regras de comunicação do usuário:**

| ID da Regra | Coligada | Filial | Nível Ensino | Curso | Turno |
| --- | --- | --- | --- | --- | --- |
| 102 | 1 |  | Ensino Superior |  |  |

**Ação:**  
O usuário informa somente o **Período Letivo: 2024/2**.

**Resultado esperado:**  
A mensagem será enviada para **todos os alunos da Coligada 1** com **nível de ensino “Ensino Superior”**, independentemente do curso, turno ou filial.  
A regra é considerada **permissiva**, pois define apenas o nível de ensino e não impõe outros filtros.

---

**✅ Exemplo 4 – Múltiplas regras unificadas**

**Regras de comunicação do usuário:**

| ID da Regra | Coligada | Filial | Nível Ensino | Curso | Turno |
| --- | --- | --- | --- | --- | --- |
| 103 | 1 | 2 | Ensino Superior | CONT, 3-1 | Manhã |
| 104 | 1 | 2 | Ensino Superior | CTI, ADM | Noite |

**Ação:**  
O usuário preenche apenas o **Período Letivo: 2024/2**.

**Resultado esperado:**  
A mensagem será enviada para alunos dos cursos **CONT, 3-1, CTI e ADM**, nos turnos **Manhã e Noite**, da **Filial 2**, com **nível de ensino Ensino Superior** no período letivo indicado.  
As regras são **combinadas de forma inclusiva**, ampliando o público da mensagem.

Quando um filtro da regra de comunicação for considerado de forma implícita, o log de informações do envio da mensagem discriminará os filtros considerados, com o objetivo de tornar o processo mais transparente para o usuário final.

**Exemplo (GIF): Preenchendo o Filtro Avançado na Regra de Comunicação**

Cada campo exibirá apenas as opções válidas com base nas seleções anteriores. Segue exemplo.

**Exemplos (GIF):**

Regras de Negócio

* Uma mesma regra de comunicação pode coexistir com outras. Se um perfil ou usuário estiver vinculado a mais de uma regra, **todas serão consideradas válidas**.
* Caso **nenhum filtro seja definido**, o sistema entenderá que **não há restrições** para o envio de mensagens. Nesse caso, o usuário poderá enviar mensagens de acordo com o seu **perfil de permissões** já configurado.
Remetente

Para que os campos na aba **"Remetente"** sejam exibidos corretamente, é necessário que o script **CN.2025.09\_04** tenha sido executado.  
Caso os campos não estejam sendo apresentados, recomenda-se atualizar o sistema para o **último patch disponível** e executar o **RM Atualizador**.

Os remetentes autorizados para envio de mensagens devem ser definidos previamente na regra de comunicação.  
Ao utilizar a Central de Comunicação, o sistema apresentará para seleção apenas os remetentes configurados nesta seção.

**Tipos de Remetentes Permitidos**  
São remetentes fixos, previamente definidos, que o usuário poderá utilizar como origem da mensagem:

**Próprio usuário:** o e-mail do usuário logado será utilizado como remetente.

**Coligada:** será utilizado o e-mail da coligada na qual a mensagem está sendo enviada.

**Coligada global:** o e-mail configurado para a coligada global será usado.

**Filial:** será utilizado o e-mail da filial na qual a mensagem está sendo enviada.

**Nível de ensino:** será utilizado o e-mail configurado para o nível de ensino na qual a mensagem está sendo enviada.

**Remetentes Adicionais**  
Esta opção permite parametrizar remetentes personalizados que o usuário poderá selecionar no momento do envio da mensagem.

 Formato Aceito

Informe um ou mais remetentes no seguinte formato:

[email@dominio.com](mailto:email@dominio.com)|Nome do Remetente  
Separe múltiplos remetentes com ponto e vírgula ;.

🔍 Exemplo de preenchimento:  
[comunicacao@totvs.com.br](mailto:comunicacao@totvs.com.br)|Comunicação TOTVS;coordenacao@[totvs.com.br](http://totvs.com.br);secretaria@[totvs.com.br](http://totvs.com.br)|Secretária TOTVS

O nome do remetente é opcional. Caso não seja informado, poderá ser preenchido manualmente durante o envio da mensagem.

Caso **nenhum tipo de remetente** ou **remetente adicional** esteja parametrizado na regra de comunicação, o usuário poderá, por padrão, enviar mensagens utilizando apenas o **próprio e-mail**.

Exemplo (GIF): Passo a passo: Criando uma regra de comunicação

# Sobreposição de Regras de Comunicação

---

Quando um usuário está vinculado a múltiplas regras de comunicação, como no caso do **usuário "X"** vinculado às **regras A** e **C**, o sistema pode adotar um comportamento permissivo. Isso significa que, caso uma opção na **regra de comunicação C** permita uma ação, essa permissão irá prevalecer, sobrepondo qualquer configuração da **regra de comunicação A**.

**Exemplo:**

* **Usuário "X"** está vinculado às regras **A** e **C**.
* A **regra A** pode ter uma restrição para o envio de mensagens.
* A **regra C**, por sua vez, pode permitir o envio de mensagens.

Neste caso, como o comportamento é permissivo, a permissão da **regra C** sobrepõe a restrição da **regra A**, permitindo que o usuário **X** envie mensagens, mesmo que a **regra A** restringisse essa ação.
