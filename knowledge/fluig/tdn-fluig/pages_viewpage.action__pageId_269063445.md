---
content_hash: 31ee9b51f14c4ba80138ff469acf2176fa9cecb0b0cf2209058b365bcf6b5a7b
fetched_at: '2026-06-28T21:35:24.217028+00:00'
page_id: '269063445'
product: fluig
source: tdn-fluig
title: Identity | Produção
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269063445
version: 777
---

.\*ndice

Nesta sessão listamos as novidades e correções que estão disponíveis em nosso ambiente de produção ([fluigidentity.com](http://app.fluigidentity.com/)).

oculto

## Junho

---

 Disponível em

* Ajustado o fluxo SAML para garantir a compatibilidade e identificação correta via sAMAccountName.

YellowDESTAQUES

 Disponível em

* Implementado o fluxo *headless* para autenticação WebAuthN, permitindo uma integração mais flexível e desacoplada da interface nativa.
* Disponibilizadas novas interfaces para listagem, edição e exclusão de credenciais WebAuthN (**passkeys**), permitindo o gerenciamento completo de dispositivos cadastrados pelo usuário.

Saiba mais

Para mais detalhes, consulte a documentação abaixo:

* [Identity | Guia de Implementação e uso do WebAuthN](https://tdn.totvs.com/pages/viewpage.action?pageId=1062879926)
* [Identity | Fluxo de Acesso com Certificado (WebAuthn)](https://tdn.totvs.com/pages/viewpage.action?pageId=1074606288)

* Implementado no Accounts o uso do escopo genérico `groups`. Quando informado, o `IDToken` (JWT) passa a incluir uma *custom claim* com ID e Nome dos grupos do usuário, obtidos a partir do endpoint `/me` do Identity.
* O endpoint `/me` agora permite retornar os grupos do usuário (ID e Nome) mediante parâmetro específico. Para tokens Accounts V2, o retorno exige a validação do escopo `groups.`
* Ativada a tela da Launchpad do Administrador: 
  + O administrador deverá conseguir administrar a Launchpad, incluindo adição de aplicativo e acesso do aplicativo adicionado na Launchpad, além disso, também deverá poder filtrar pelo aplicativo específico na tela.
* Ajustada a validação do campo `expires_in` na autenticação de usuários TOTVS e TOTVSAPPS para garantir o tempo de expiração correto.

## Maio

---

GreenCORREÇÕES

 Disponível em

* Ajustada a lógica de desativação de usuários integrados ao AD. A partir de agora, a desativação suspende apenas a emissão de tokens de acesso, preservando os vínculos com grupos e aplicações.
* Ajustado o carregamento da interface para ocorrer apenas após o retorno das APIs, evitando inconsistências visuais.

 Disponível em

* Implementado ajuste técnico na interface de configurações do Provedor Genérico para garantir a persistência dos dados no campo Self Registration. Com esta correção, as edições realizadas pelo usuário são salvas corretamente na base de dados, assegurando que as permissões de auto-registro reflitam as configurações definidas em tela.
* Substituído o algoritmo de validação TOTP (baseado em tempo) pelo modelo OTP Dinâmico (baseado em estado). O objetivo é eliminar o bloqueio de reutilização de códigos e a latência de expiração que tornavam a API de validação temporariamente indisponível após o primeiro envio.

Disponível em

* Adicionada API para validação de autenticação multifator (MFA) via e-mail, com envio e verificação de códigos de segurança.

Saiba mais

Para mais detalhes, consulte a documentação abaixo:

* Implementada a validação por padrão dos ACRs padrão do SAML.

## Abril

---

YellowDESTAQUES

 Disponível em

* **Liberado o Fluxo de Primeiro Acesso**
  + Ao selecionar **"Primeiro acesso"**, o usuário será redirecionado para a tela de verificação. Diferente do "Esqueci minha senha", o **e-mail será recuperado automaticamente via `queryParam`** (enviado pelo ERP), dispensando a necessidade de identificação manual. Para concluir, o usuário deve informar o **token de 6 dígitos** enviado por e-mail e realizar o **cadastro da nova senha**.

Saiba mais

Para mais detalhes, consulte a documentação abaixo:

* [Identity | Fluxo de Primeiro Acesso](https://tdn.totvs.com/pages/viewpage.action?pageId=1057971225)

* Implementação do suporte experimental a **WebAuthn**, habilitando a gestão de chaves via API e autenticação via botão dedicado no login.

GreenCORREÇÕES

 Disponível em

* Correção na captura do IP de origem para logs de auditoria em acessos via aplicativos mobile.
* Adicionada verificação de tamanho para upload de logo (200x60px) e ícone (50x50px), garantindo a padronização visual do portal.
* Implementação de cabeçalhos (Security Headers) no Portal de Autenticação para mitigar vulnerabilidades e reforçar a proteção contra ataques e interceptações.

## Março

---

YellowDESTAQUES

Disponível em

**Estabelecimento de Níveis de Autenticação via ACR e Auditoria por AMR.**

Saiba mais

Para mais detalhes, consulte a documentação abaixo:

**Adicionada a capacidade de logar com usuários vinculados a múltiplas empresas para garantir que o `environmentName` seja identificado e validado corretamente em diferentes contextos.**

Saiba mais

Para mais detalhes, consulte a documentação abaixo:

* Os ícones dos aplicativos globais do Identity foram atualizados para refletir a nova marca TOTVS.
* Os ícones do Identity foram atualizados para refletir a nova marca TOTVS.

GreenCORREÇÕES

* Corrigida a aplicação dos filtros no relatório de acessos por aplicativo, garantindo a precisão dos dados exibidos.
* Ajustado o redirecionamento automático para a Launchpad ao acessar aplicativos Fluig vinculados a grupos.

## Fevereiro

---

YellowDESTAQUES

Disponível em

**Foi liberada a integração do Okta como provedor de login no TOTVS Identity.**

Saiba mais

Para mais detalhes, consulte a documentação abaixo:

**Atualizada a tela de termo de consentimento: a visualização direta do PDF foi substituída por um botão de download.**

Saiba mais

Para mais detalhes, consulte a documentação abaixo:

**MFA por E-mail: Nova Alternativa de Autenticação Multifator**

Para aumentar as possibilidades na autenticação multifator, disponibilizamos uma nova configuração que permite o envio do token MFA diretamente para o e-mail do usuário. Esta opção é ideal para facilitar o acesso de colaboradores que não possuem dispositivos móveis corporativos para o uso de aplicativos autenticadores.

**Como configurar**

O administrador deve acessar o menu de **Segurança** e selecionar a opção **Autenticação multifator**. No topo da página, basta marcar a caixa de seleção para habilitar o recurso em toda a empresa.

Após habilitar o recurso globalmente, o administrador pode gerenciar quais grupos terão a autenticação multifator como obrigatória. Ao ativar a chave para o grupo **"EVERYONE"**, a regra será aplicada a todos os usuários cadastrados na plataforma.

Por se tratar de uma alteração crítica de segurança que impactará o acesso de todos os usuários, o sistema solicitará a confirmação da senha do administrador para validar a operação.

Saiba mais

Para mais detalhes, consulte a documentação abaixo:

* [Identity | Multi-Factor Authentication](https://tdn.totvs.com/display/fluig/Identity+%7C+Multi-Factor+Authentication)
* [Simplifique a gestão de senhas e MFA com o TOTVS Identity](https://tdn.totvs.com/pages/viewpage.action?pageId=851312277)

* Liberada a sincronização de permissões (excluir, desativar e ativar usuários) entre a empresa *partner* e suas associadas após atualizações cadastrais.

Disponível em 

* Foi adicionada a propriedade autocomplete="one-time-code" no campo de código de MFA.
* Corrigida inconsistência que afetava a aplicação do filtro de restrição de IPs.
* Corrigida inconsistência no redirecionamento de usuários após a inclusão do token de autenticação multifator (MFA).

## Janeiro

---

Disponível em 

* Efetuada correção para que o acesso ao Fluig pelo Launchpad seja realizado com o mesmo usuário que fez o login no Identity, mesmo com a configuração do Desktop SSO no ambiente.
* Correção realizada no recurso de desativação temporária do usuário.
* Ajuste efetuado para que o login no aplicativo My Approval seja realizado corretamente mesmo que a senha pessoal esteja desabilitada nas configurações da empresa.
* Tratamento realizado para reforço de segurança na API de recuperação de senha.

## 2025

---

YellowDESTAQUES

Disponível em

**Mais destaque para o login social**

Com o login social, você consegue escolher um provedor como o Google, o Facebook, o Linkedin ou outros, para que a autenticação no TOTVS Identity ocorra por meio das contas dos usuários nesses aplicativos. 

Esse recurso foi aprimorado, agora você pode definir se os campos de e-mail e senha devem ser apresentados na tela de login da sua empresa. Ao marcar a opção **Ocultar campos de login com Identity**, ao digitar o endereço da empresa, os campos de Usuário e senha não serão mais apresentados, forçando os usuários a realizarem o login pelo botão referente ao provedor configurado. 

**Troca de senha do AD**

#ebecf0**Essa melhoria foi uma sugestão enviada pela Central colaborativa!**

No mês de abril atualizamos o recurso **Esqueceu sua senha** para trazer mais segurança na troca de senha. Agora trazemos outra melhoria para facilitar seu login: no momento do reset de senha é possível selecionar se a troca será da **senha pessoal** ou da senha do **Active Directory**. Lembrando que a senha pessoal, quando alterada, vale para acesso em todas as empresas. Já a senha do Active Directory, se o usuário estiver vinculado a mais empresas, precisa escolher para qual empresa a nova senha deve ser aplicada.

Acesse a [Central colaborativa](https://centraldeatendimento.totvs.com/hc/pt-br/community/topics/360001941754)**,** confira as sugestões e compartilhe suas ideias por lá também!

**100%true5%**

Saiba mais

Para mais detalhes, consulte as documentações abaixo:

Disponível em 

**Ajustes em APIs**

Incluída *flag* **send-events**nas APIs de adição de usuário em aplicativo e de atribuição e remoção de papéis:

Quando o **send-events** for enviado como **true**, os eventos devem ser enviados para a fila de provisionamento. Uma vez estando o send-events como **false**, os eventos não serão adicionados a fila.

 Disponível em  

**Mais segurança na recuperação de senha pessoal**

Agora, ao clicar em **Esqueceu sua senha?** você receberá um código por e-mail, e esse código deve ser informado na tela de troca de senha. Essa melhoria busca trazer mais facilidade e segurança quando você precisa fazer o reset de senha do TOTVS Identity.

**100%true5%**

**Atenção!**

Para os clientes que customizaram o antigo template de reset de senha, será necessário refazer as alterações no novo template, da mesma forma que foi feito no antigo. Para facilitar este processo, o template antigo ficará disponível para consulta no menu de Notificações via E-mail do Identity, bem como o novo também estará disponível para as eventuais alterações, no mesmo menu do Identity. 

Saiba mais

Para mais detalhes, consulte as documentações abaixo:

 Disponível em  

**Novo plugin TOTVS Identity**

Disponibilizamos uma nova versão do [plugin TOTVS Identity](https://chromewebstore.google.com/detail/totvs-identity/jbfaabmhpholbikmmgimfaabndonejpk?hl=pt-BR) na Chrome Store. Essa nova versão conta com reforços importantes de segurança, e requer a alteração na configuração do aplicativo do tipo plugin. Os ajustes a serem realizados são:

* Os campos **Campo Nome do Usuário,** **Tipo de Nome do Usuário,** **Campo Senha,** **Tipo de Senha** e**Nome do Formulário de Login** passam a ser obrigatórios.
* O campo **Javascript Customizado** não precisa ser preenchido, caso estiver, passa a ser ignorado durante o uso deste novo plugin.

Saiba mais

Para mais detalhes sobre a configuração do aplicativo, consulte a documentação .

Disponível em  

**Gerencie seus grupos com facilidade**

Dando continuidade ao movimento de atualização das telas do TOTVS Identity, o *layout* da tela de grupos foi reformulado, está mais simples e intuitivo, mas sem perder nada em funcionalidade. Configure seus grupos de usuário diretamente por essa tela ou importe os seus grupos já configurados do Active Directory.

novagruposTela de gruposTela de visualizaçãoSaiba mais

Para mais detalhes, consulte a documentação do recurso:

GreenCORREÇÕES

Disponível em 

* Correção de inconsistência no reenvio de e-mail de convite para usuários convidados.
* Foi otimizada a busca de usuários para associação a grupos, eliminando o travamento durante a digitação pausada. Agora, a pesquisa responde de forma mais ágil, melhorando a experiência do usuário ao buscar nomes.

Disponível em 

* Foi ajustado o processo de sincronização de usuários do AD, permitindo agora a importação correta de e-mails com domínios que possuem até 10 caracteres na segunda parte do domínio.

Disponível em 

* Correção de inconsistência na configuração de aplicativo do tipo Plugin.
* Realizada correção para que a troca de logo dos aplicativos ocorra com sucesso.
* Correção de inconsistência no registro de alterações de Perfis de usuários no relatório de Auditoria.
* Foi resolvido um problema que impedia a exibição completa dos requisitos da política de senha na tela de redefinição de senha ao acessar pelo link enviado ao administrador que cadastrou a empresa no Identity.
* Efetuada correção para possibilitar o envio de arquivo XML para configuração do Azure Active Directory.
* Ajustes realizados no recurso de desativação temporária, para que a desativação do usuário seja realizada com sucesso e registrada corretamente no relatório de auditoria.
* Correção de inconsistência no redirecionamento da autenticação SSO no Identity.

Disponível em 

* Tratamento implementado no processo de reset de senha para garantir que não haja distinção entre letras maiúsculas e minúsculas no e-mail fornecido.

Nota para desenvolvedores

O swagger da v2 mudou de endereço, o novo endereço é: <https://app.fluigidentity.com/rest/doc/#/>

Para mais detalhes, consulte as documentações abaixo:

Disponível em 

* Correção realizada no recurso de aceite do Active Directory, para que o usuário aceito do AD, após ser removido na aba de Usuários e ressincronizado, seja então apresentado na aba de Rejeitados, possibilitando ser aceito novamente. Considera-se a ressincronização quando é realizada uma pequena edição do usuário no AD para forçar a sincronização.

Disponível em 

* Correção de inconsistência que impedia o login ao utilizar o Fluig com Eclipse.
* Inclusão de mensagem avisando ao usuário sobre o login do ERP via TOTVS Identity. Essa mensagem será apresentada somente no login OIDC dos ERPs TOTVS.
* Ajuste realizado no [plugin TOTVS Identity](https://chromewebstore.google.com/detail/totvs-identity/jbfaabmhpholbikmmgimfaabndonejpk?hl=pt-BR) para buscar os IDs corretos dos campos e que estão na configuração.

Disponível em 

* Corrigida inconsistência que impedia a gravação de filtro de usuários ou de grupos do Active Directory com mais de 255 caracteres.
* Correção no formato de data apresentado na desativação temporária do usuário.

Disponível em 

* Correção de falha que impedia a configuração de MFA no login de novos usuários para autenticação no dispositivo Android.

Disponível em 

* Correção de inconsistência na apresentação dos grupos e aplicativos associados ao usuário convidado na tela de Dados do usuário.
* Corrigida inconsistência que acontecia com usuário sincronizado no AD e com acesso ao aplicativo pelo vínculo de grupo, para que, ao exclui-lo do AD, seja feita a exclusão do grupo e seja retirado o acesso ao aplicativo.

Disponível em 

* Ajustes realizados nos cenários de criação, visualização, edição e exclusão de aplicativos, para que os eventos apareçam corretamente no relatório de auditoria.

Disponível em 

* Efetuados ajustes para que um usuário que já tinha sido aceito, foi excluído pelo AD e adicionado novamente com o mesmo *e-mail*, também pelo AD, seja exibido novamente na lista de usuários pendentes de aceite no Identity.
* Correção realizada na ação de exclusão de grupos do usuário, para que o usuário perca o acesso aos aplicativos vinculados aos antigos grupos.
* Adicionada mensagem de aviso para casos em que é feita a exclusão de usuário da empresa porém esse usuário está vinculado a grupos com muitos aplicativos, o que torna o processo de exclusão mais demorado.

Disponível em 

* Ajustes de layout no preenchimento dos campos de usuário e senha acessando a tela de login com dispositivo IOS.
* Ajustes realizados no processo de troca de empresa no TOTVS Identity.

Disponível em 

* Ajuste realizado para o que usuário seja direcionado à escolha de uma nova empresa favorita, caso venha a ser removido da empresa favorita atual.

Disponível em 

* Inclusão do campo **Alterar senha do Aplicativo no Provedor (ClientSecret)** na tela de edição do , para a necessidade de alteração da senha do aplicativo no provedor do login social.
* Ajuste realizado para que fique visível o nome do provedor (*tooltip*) na tela de login.
* Correção de inconsistência que impedia a associação de aplicativos diretamente a usuários com status convidado.

Disponível em  

* Realizada melhoria de layout na tela de , para ficar mais aderente ao que é praticado em outras telas do TOTVS Identity.

Disponível em 

* Correção aplicada na mensagem que deve ser apresentada no caso de ser informada uma senha incorreta na alteração de senha pessoal.

Disponível em 

* Ajustes para que seja apresentada corretamente a tela de adicionar papéis ao usuário, por meio do aplicativo atribuído.
* Ajustes realizados para que seja apresentado corretamente o papel adicionado ao grupo, por meio do aplicativo atribuído.
* Correção para que seja gerado o evento de *provisioning* caso o usuário venha a ser recriado, após ter sido excluído anteriormente.

Disponível em 

* Correção de inconsistência na busca por usuário ou por e-mail no relatório de aceite do termo de consentimento.
* Ajuste realizado na tela de "Filtrar acesso por IPs externos", para que apresente corretamente a opção de remover o IP adicionado.
* Correção realizada na funcionalidade de criação de usuário como convidado em um cenário onde o mesmo usuário já está cadastrado e tem uma senha temporária em outra empresa. Ao criar um usuário como convidado, ele aparece sem a senha temporária na nova empresa.
* Ajuste realizado na autenticação com sincronização pelo AD, para que seja efetuado corretamente ao informar o e-mail incompleto (somente o nome de usuário, sem o @ e o nome do domínio).
* Correção realizada na edição de imagem para ser apresentada na tela de login (logo da empresa).
* Ajuste realizado para que a imagem de logo do provedor tenha o tamanho máximo de 1MB. Essa alteração visa a padronização de tamanho de imagem de ícones customizados no TOTVS Identity.
* Ajuste realizado na ação de excluir grupo, para que seja registrada corretamente no relatório de auditoria.

Disponível em 

* Correção realizada para que novos usuários incluídos no grupo do AD sejam provisionados no TOTVS Identity e vinculados nos grupos de acesso.

## 2024

---

Yellowdestaques

Disponível em 

**Acesso direto na empresa desejada**

Trazendo mais praticidade ao dia-a-dia dos seus usuários, agora a tela de login oferece a possibilidade de escolher em qual empresa o login será direcionado. Isso se aplica para qualquer usuário que esteja vinculado a mais de uma empresa, e que esteja habituado a acessar pelo endereço genérico [app.fluigidentity.com](http://app.fluigidentity.com). Além disso, oferecemos a possibilidade de salvar a escolha para os próximos logins, e então o acesso já será direcionado, pulando diretamente do login para a empresa favorita.

Mas não se preocupe! Mesmo escolhendo a empresa no login, continua sendo possível a mudança de contexto pela opção Meu perfil, assim como o acesso direto a cada empresa pelo domínio definido (exemplo: [suaempresa.fluigidentity.com](http://suaempresa.fluigidentity.com)). 

Saiba mais

Para mais detalhes, consulte as documentações abaixo:

Disponível em  

**Login social com imagem personalizada**

#ebecf0

**Essa melhoria foi uma sugestão enviada pela Central colaborativa!**

No ano passado lançamos a configuração de provedores, para possibilitar o login no Identity por meio de redes sociais diversas. Esse recurso está ainda mais completo, pois agora conta com a opção de cadastrar a imagem do provedor, nos casos em que o provedor é genérico.

O cadastro de uma imagem personalizada visa facilitar a identificação de qual o provedor utilizado no momento do login, trazendo melhor usabilidade para os usuários finais do sistema.

Acesse a [Central colaborativa](https://centraldeatendimento.totvs.com/hc/pt-br/community/topics/360001941754)**,** confira as sugestões e compartilhe suas ideias por lá também!

**100%true5%**

Saiba mais

Para mais detalhes, consulte a documentação [Identity - Provedores](https://tdn.totvs.com/x/RRTlLQ).

**Mais facilidade no desbloqueio de usuários**

Nas configurações da política de senha, existe a possibilidade de definir uma quantidade máxima de tentativas de *login* para os usuários de sua empresa. Caso a quantidade estabelecida seja excedida, o usuário que tentou autenticar-se sem sucesso será bloqueado.

Para não onerar os administradores, o próprio usuário que foi bloqueado agora consegue realizar o desbloqueio de sua conta e voltar a acessar o Identity em poucos instantes. Isso ocorre por meio da opção **Esqueci a senha** na tela de login. Confira como funciona:

**100%true5%**

Saiba mais

Para mais detalhes, consulte as documentações abaixo:

Disponível em 

**Bloqueio de acessos - uma segurança adicional para os seus usuários**

Agora os administradores da empresa podem configurar uma quantidade máxima de tentativas de *login* para os usuários de sua empresa. Funciona assim: caso a quantidade estabelecida seja excedida, o usuário que tentou autenticar-se sem sucesso será bloqueado e só conseguirá acessar o sistema novamente após o desbloqueio realizado por um administrador. Esse é mais um reforço de segurança a ser habilitado na política da empresa, para evitar ataques como o de força bruta e proteger a segurança dos seus usuários.

**Acompanhe os usuários que foram bloqueados**

Recentemente lançamos o recurso de exportar usuários, o que já agilizou o trabalho dos administradores para terem uma visão completa de seus usuários. Com esse novo recurso de limitação das tentativas de acesso e o bloqueio de usuários, é possível filtrar pela situação Bloqueados e acompanhar no relatório apenas os usuários que estão impedidos de acessar o sistema.

**Tela de usuários atualizada e mais funcional**

Além das novidades acima, o *layout* da tela de usuários foi totalmente reformulado, está mais simples, intuitivo e voltado às suas necessidades. Confira!

Saiba mais

Para mais detalhes, consulte as documentações:

Disponível em

**Launchpad mais simples e funcional**

O launchpad é o espaço inicial do Identity, a partir de onde são realizados os acessos a todos os aplicativos que foram atribuídos.

Pensando em facilitar ainda mais o uso do launchpad, trouxemos um layout mais moderno e simplificado, para que você encontre as opções e configurações de maneira rápida e fácil. Além disso, o launchpad pessoal foi vinculado ao launchpad corporativo, e você pode escolher os aplicativos que irão aparecer nessa tela, a partir da lista de aplicativos navegáveis.

Aproveite essa facilidade e configure seus aplicativos!

Saiba mais

Para mais informações, consulte as documentações abaixo:

Greencorreções

Disponível em 

* Correção de inconsistência na configuração de MFA obrigatório por grupo.

Disponível em 

* Ajuste realizado na ação de desativar usuário, para que seja registrada corretamente no relatório de auditoria.

Disponível em 

* Implementada melhoria na busca de usuário, agora é possível pesquisar tanto por parte do e-mail ou login em um único campo.
* Trazendo mais usabilidade para o Identity, foram liberadas algumas atualizações de layout nas telas de [Customização](https://tdn.totvs.com/pages/viewpage.action?pageId=273980170), [Notificações via E-mail](https://tdn.totvs.com/pages/viewpage.action?pageId=273980172) e nos .

Disponível em 

* Ajustes para possibilitar que usuários sem e-mail possam incluir um e-mail válido em seu perfil. Com isso, passam a realizar a recuperação de senha pessoal e a autenticação no Identity tanto pelo novo e-mail quanto pelo nome de usuário.

Disponível em 

* Ajuste realizado para sanar inconsistência na primeira autenticação de usuário como convidado.
* Correção de inconsistência ao habilitar provisionamento no aplicativo Fluig.

Disponível em 

* Ajuste aplicado para que seja possível a autenticação quando a senha do AD é exatamente igual à senha pessoal.
* Correção de inconsistência na autenticação com username (primeira parte do e-mail) a partir do endereço URL da empresa definida.
* Correção no recurso de troca de e-mail que acabava impossibilitando a autenticação do usuário alterado.
* Correção de inconsistência na criação de usuários no Identity via API.

Disponível em 

* Ajustes realizados para sanar inconsistência no acesso ao aplicativo Fluig pelo Launchpad.

Disponível em  

* Correção realizada para permitir a edição de aplicativo SAML.
* Ajuste realizado para que somente usuários administradores tenham permissão para utilizar a função **Esqueci a senha**, quando a empresa tiver desabilitado o login com senha pessoal.

Disponível em 

* Correção de inconsistência na criação de usuário, que acabava afetando a autenticação do usuário no Identity.

Disponível em 

* Alteração na restrição de quantidade de caracteres no campo Usuário (login sem e-mail), que agora passa a aceitar até 150 caracteres. Para mais detalhes, consulte a documentação .
* Correção realizada para que seja apresentado o botão de login com o provedor genérico cadastrado.

Disponível em 

* Ajuste realizado na criação e edição de aplicativo do tipo GoodData, para salvar corretamente ao marcá-lo como navegável.
* Correção realizada no tempo de expiração do login do Identity quando configurada a integração com a plataforma Fluig.
* Correção de inconsistência identificada na criação de conta trial do Collab por empresas que já são clientes TOTVS.

Disponível em 

* Ajuste na opção "Aceitar Todos os Usuários Pendentes" para que a importação de usuários do Active Directory ocorra corretamente.
* Correção realizada na busca de aplicativos para associar ao usuário.
* Correção realizada na busca de grupos para associar ao usuário.
* Correção de inconsistência na busca pelo e-mail do usuário na opção Atribuir Usuários ao Grupo.
* Correção realizada para que seja possível editar a informação de Definir login SAML nos aplicativos.
* Pequenos ajustes de layout na nova tela de Dados do usuário.
* Correção de inconsistência apresentada na autenticação de usuário convidado após a configuração de política de senha.

Disponível em 

* Correção realizada na busca de usuários para associar ao grupo.

Disponível em 

* Correção de inconsistência que causava lentidão na busca de usuários do Identity.
* Conforme divulgação anterior, foi realizada a alteração do atributo SameSite do cookie do Identity para LAX para as empresas que estiverem com este atributo com o valor NONE. Para saber os impactos, consulte a [notícia divulgada](https://suporte.totvs.com/portal/p/10098/suporte-fluig-noticias?id=1079) no portal do cliente.

Disponível em 

* Ajuste de parâmetros para permitir excluir usuários corretamente.
* Correção de inconsistência no nome da empresa apresentado no Launchpad.

Disponível em 

* Ajuste realizado no menu Segurança no item "Controle de Segurança do Token", para que novas empresas tenham o padrão LAX.
* Ajustes na regra de armazenamento da senha do AD em cache. O Identity agora passa a apagar o cache do usuário de AD caso sejam informadas credenciais inválidas.

Disponível em 

* Correção realizada no login SAML com Azure AD.
* Correção de inconsistência no login quando a empresa estava configurada com o CAPTCHA obrigatório.
* Correção de inconsistência no relatório de Acessos bem sucedidos, para que o IP seja apresentado em todos os registros.
* Correção realizada no recurso de desativação temporária, para que o usuário fique com o status inativo durante o período estabelecido.
* Corrigida inconsistência no botão Entrar da tela de login.
* Correção de inconsistência no login quando a senha do AD era exatamente igual a senha pessoal.

Disponível em 

* Correção realizada para evitar que usuários ou grupos sem o aplicativo Fluig vinculado tenham acesso ao Fluig Plataforma diretamente pela URL.

Disponível em 

* Ajuste realizado para que aplicativos que estão com a URL de acesso direto habilitada utilizem captcha invisível.
* Correção realizada para apresentar a credencial do usuário ao clicar em credenciais no aplicativo no novo launchpad.
* Correção de inconsistência ao desassociar grupo everyone de aplicativo.

Disponível em

* Correção de inconsistência no login com senha temporária.

## 2023

---

Yellowdestaques

Disponível em 

**Mais segurança para sua empresa e seus usuários**

Por padrão, o TOTVS Identity já tem uma série de critérios que os usuários devem respeitar na hora de trocar a senha. A novidade é que os requisitos de complexidade de senha podem ser personalizados, permitindo que se definam requisitos específicos para que a senha informada seja considerada válida. Confira alguns deles:

PoliticaComplexidade de senha

O tamanho da senha que os usuários devem informar, bem como os caracteres exigidos para a formação da senha (números, letras maiúsculas, letras minúsculas e caracteres especiais) agora podem ser personalizados para atender melhor ao cenário de cada empresa.

Segurança da senha

Para forçar a troca de senha dos usuários de tempos em tempos, a política de senha também abrange a configuração um prazo de validade para a senha. E os usuários podem ser alertados por e-mail quando a senha estiver próxima de expirar.

Senhas proibidas

Além de definir se a reutilização de senhas deve ser bloqueada, várias outras combinações podem ser restringidas na política de senha da empresa: combinações com números ou letras sequenciais, senhas contendo o nome ou e-mail do usuário, ou até mesmo senhas que perpassam a cultura da empresa (por exemplo: SuaEmpresa!123) podem ser incluídas em uma lista de bloqueios.

Saiba mais

Para mais informações, consulte as documentações abaixo:

**Simplificamos as configurações de usuário**

As opções de perfil dos usuários básicos e administradores estão com um novo visual, agora agrupadas na tela de Configurações do usuário. Por meio dessa tela, você consegue alterar suas informações pessoais, alterar as configurações de autenticação multifator e acessar os links para obter os plugins e aplicativos que você necessita.

Acesse suas configurações de usuário e confira!

configuracoes-pessoaisInformações pessoaisAutenticação multifatorPluginsSaiba mais

Para mais informações, consulte a documentação abaixo:

Disponível em 

**Exportar usuários**

A página de usuários recebeu uma novidade: agora o Identity permite que você exporte a lista de usuários da empresa. O recurso é muito prático, você solicita a exportação e recebe um link no seu e-mail, para concluir o download do arquivo CSV com os dados dos usuários.

Saiba mais

Para mais informações, consulte a documentação abaixo:

Disponível em 

**Acompanhe os usuários que aceitaram o termo de consentimento**

O termo de consentimento é um documento escrito com o objetivo de apresentar as cláusulas para garantir que o usuário esteja ciente de suas responsabilidades e das responsabilidades da empresa, das regras de uso do sistema, da privacidade dos seus dados pessoais, entre outras informações.

Agora, além de configurar um termo de consentimento no TOTVS Identity, você pode consultar os usuários que ainda não deram aceite nesse termo configurado, e também pode consultar o momento em que um usuário específico aceitou o termo. Tudo isso por meio de um relatório, que também pode ser exportado para melhor acompanhamento.

Saiba mais

Para mais informações, consulte as documentações abaixo:

Disponível em 

**Novas opções de provisionamento e autenticação**

Agora você pode permitir o login com redes sociais (Linkedin, Google, Facebook, etc) para os usuários de sua empresa. Aproveite e confira também a nova tela de Segurança, muito mais organizada e fácil de usar.

**Nova tela de configurações de segurança**

Localizar uma determinada configuração de segurança da empresa no Identity era uma tarefa difícil? Agora está muito mais fácil! O layout da tela de Segurança foi aprimorado e os recursos de configuração aparecem todos organizados à esquerda, basta escolher o recurso e somente suas opções serão apresentadas.

**Já pensou... logar no Identity com suas redes sociais?**

Que tal acessar o Identity com sua conta no Linkedin, Google, Facebook...? E permitir que os usuários de sua empresa criem uma conta no Identity a partir dessas redes? Esse novo recurso veio para facilitar muito a autenticação dos seus usuários.

**Inúmeras opções de provedores**

Você escolhe as redes sociais que serão utilizadas para login na sua empresa. Além do Linkedin, do Google e do Facebook, você pode incluir os provedores que desejar, basta ter acesso à documentação do provedor, que o cadastro é realizado em poucos passos, com o preenchimento de alguns campos.

Mais informações

Para saber mais, consulte as documentações abaixo:

Greencorreções

Disponível em 

* Resolvida inconsistência no provisionamento de usuários do Identity para o Protheus, que causava duplicação do usuário no Protheus.
* Correção de inconsistência no reenvio de e-mail de convite.

Disponível em 

* Correção de inconsistência no acesso ao aplicativo do tipo plugin.
* Atualização do recurso de captcha para usar reCAPTCHA invisível, melhorando a usabilidade ao executar o processo de validação.
* Correção de inconsistência no login com captcha ativado.
* Realizada a correção dos aplicativos duplicados no cadastro do usuário.
* Correção realizada no login após a alteração de senha.

Disponível em 

* Correção de inconsistência no provisionamento de novos usuários ao aplicativo.

Disponível em 

* Ajuste realizado para que, ao atribuir o aplicativo do Fluig Plataforma no grupo Everyone**,** os usuários sejam criados corretamente quando o modo de provisionamento está ativado.

Disponível em 

* Corrigida inconsistência para que os usuários não fiquem com status de convidado após serem inseridos diretamente pelo grupo.
* Correção de inconsistência na criação de usuários e migração de grupos do Identity para o Protheus.

Disponível em 

* Realizada correção para que, ao excluir um usuário no painel administrativo dos apps, esse usuário também seja excluído do Identity.
* Correção de inconsistência ao carregar a tela de cadastro de usuário no painel administrativo.
* Realizada correção para excluir o aplicativo do usuário quando não existir mais vínculo com grupo.

Disponível em 

* Ajuste efetuado para que os aplicativos vinculados aos grupos de usuário sejam apresentados corretamente.

Disponível em 

* Ajuste realizado para que seja preenchido automaticamente o e-mail do usuário ao definir o login SAML no aplicativo.
* Correção de inconsistência ao acessar a tela de aplicativos por usuário.
* Corrigida inconsistência na regra de MFA para que seja exigido no momento de autenticação, quando for obrigatório para um grupo no qual o usuário faça parte.

Disponível em 

* Correção de inconsistência ao tentar remover usuário de grupo com MFA configurado.

Disponível em 

* Ajustes na tela de login para que a aplicação leitora identifique os textos no reset de senha.

Disponível em 

* Realizadas melhorias na sincronização de usuários entre o Identity e o Manager, para melhorar a performance nos casos de empresas com muitos usuários.
* Inclusão de parâmetro nas configurações gerais do Active Directory, para escolher se deve ser bloqueada a autenticação com senha pessoal para usuários importados do Active Directory.
* Desenvolvimento de API para possibilitar o cadastro de campos customizados da empresa e dos usuários.

Disponível em 

* Realizada correção para possibilitar o login no aplicativo My Fluig com o MFA ativo.

Disponível em 

* Realizada correção do redirecionamento do aplicativo SAML.
* Inclusão de campos na , para que seja possível alterar o nome das propriedades nome, sobrenome e e-mail no SAMLRequest permitindo a integração com aplicações que requerem um nome específico nessas propriedades.
* Ajustes na tela de login para que seja adaptada para aplicações leitoras. O objetivo é tornar o sistema mais acessível, e em breve outras telas devem receber a adaptação também.

Disponível em 

* Realizada correção para permitir que seja cadastrado um novo termo de consentimento.

Disponível em 

* Adicionadas as imagens dos aplicativos na Launchpad.
* Realizada melhoria na apresentação dos logs do SmartSync.

Disponível em 

* Correção de inconsistência na autenticação com senha pessoal.
* Correção de inconsistência no login após a recuperação de senha.
* Correção realizada na exportação de registros de relatório, onde a quantidade de registros estava inconsistente com o que era apresentado em tela.

Disponível em 

* Incluída configuração para alterar o subdomínio da empresa. Para solicitar a alteração, entre em contato com o nosso atendimento em [suporte.totvs.com](https://suporte.totvs.com). Quando for feita a alteração do subdomínio, os usuários devem realizar as autenticações no novo domínio.

Disponível em 

* Incluída configuração para alterar o atributo Same Site dos tokens gerados. Para mais detalhes, consulte a [documentação do recurso](https://tdn.totvs.com/x/a1vhKw).

## 2022

---

Disponível em 

* Correção de inconsistência detectada ao excluir o cadastro de um usuário.

Disponível em 

* Realizados ajustes no layout da tela de Meu perfil.

Disponível em 

* Ajuste realizado para que, na inclusão de um novo usuário, seja apresentado um informativo caso seja inserido um e-mail já existente na empresa.
* Corrigida a inconsistência no momento do login de usuário do Azure AD.

Disponível em 

* Realizada melhoria no menu Relatórios, que agora acessa diretamente os relatórios disponíveis no sistema. Os dashboards disponíveis agora passam a ser acessados pelo ícone  no canto superior direito da tela.
* Ajustes nas mensagens de sucesso e de erro ao informar as credenciais na tela do Launchpad.
* Correção de inconsistência na tela de cadastro do recurso de segurança.
* Ajuste realizado para que o token MFA seja solicitado no momento da troca de empresa, quando esta empresa tiver configuração de MFA habilitada.

Disponível em 

* Realizado ajuste para que usuários com e-mail inválido não sejam sincronizados do AD para o TOTVS Identity. Além desse ajuste, caso já exista no Identity algum usuário aceito que foi criado no AD com e-mail inválido, será possível ter a visão do cadastro desse usuário, porém, esse usuário não conseguirá autenticar-se.
* Ajustes realizados na criação de APIs para manipulação e busca de ligações entre usuários e aplicações.
* Correção de inconsistência que ocorria no primeiro login de usuários criados pelo Azure AD.

Disponível em 

* Implementado uma nova API para que os endereços de e-mails com letras maiúsculas no cadastro do CAS sejam transformados automaticamente em letras minúsculas, evitando assim, inconsistências ao realizar o login no CAS.

Disponível em 

* Ajustes realizados na criação de uma API para definir as credenciais do usuário no TOTVS Identity.

Disponível em

* Implementado o recurso do [Certificado SAML RSA 2048](https://tdn.totvs.com/x/BwefKQ), para que o usuário possa obtê-lo em seu contexto criado no Fluig Identity. O novo certificado se destaca pelo nível de segurança de sua criptografia, contando com uma chave de 2048 bits.

Disponível em 

* Ajustes realizados ao efetuar o login do TOTVS Identity em um dispositivo móvel, para que a tela seja apresentada devidamente alinhada ao usuário.

Disponível em 

* Corrigida inconsistência para que seja possível a correta visualização dos grupos configurados para as empresas no TOTVS Identity.
* Realizado ajustes no layout de algumas telas do TOTVS Identity, para que sejam apresentadas corretamente aos usuários.
* Corrigida inconsistência no layout da tela de login do TOTVS Identity.
* Correção realizada para que o usuário consiga [trocar a logo do aplicativo](https://tdn.totvs.com/pages/viewpage.action?pageId=331856582#Identity|Configura%C3%A7%C3%B5esdeaplicativospadr%C3%A3o-Trocarlogodoaplicativo) no TOTVS Identity.
* Ajustes realizados para que o usuário consiga [remover um aplicativo](https://tdn.totvs.com/pages/viewpage.action?pageId=331856582#Identity|Configura%C3%A7%C3%B5esdeaplicativospadr%C3%A3o-Removeraplicativo) no TOTVS Identity.
* Realizado ajustes ao excluir um aplicativo, para que após a exclusão os usuários sejam redirecionados para a tela de listagem dos aplicativos.

Disponível em 

* Ajustes realizados para [Autenticação CAS](https://tdn.totvs.com/x/JfgGDg)[.](https://tdn.totvs.com/x/JfgGDg) Implementado campos para preenchimento do nome, sobrenome e e-mail.
* Ajustes realizados ao realizar o login no CAS. Implementado uma  demonstrando o motivo da falha no login, caso o e-mail esteja inserido incorretamente.
* Corrigida inconsistência para que o *logout* seja realizadocorretamente, após um período de inatividade da tela do TOTVS Identity.
* Ajustes realizados no processo de recuperação de senha do TOTVS Identity.
* Ajustes realizados ao [criar um novo aplicativo do tipo SAML](https://tdn.totvs.com/x/8v04E). O ajuste promoveu a criação do campo "Enviar grupos pelo SAMLResponse" para que quando marcado, este enviará as tags "GroupId" e "Groupname" na requisição SAML, as quais conterão os IDs e os nomes dos grupos que o usuário está associado no TOTVS Identity.

Disponível em 

* Realizado ajustes no token de acesso ao realizar o login no TOTVS Identity.

Disponível em 

* Ajustes realizados reforçando a correta funcionalidade do sistema ao disparar eventos.
* Ajustes realizados para efetuar o *logout* do usuário ao alterar a empresa no TOTVS Identity. O *logout* do usuário será efetuado de uma empresa sem AD para uma empresa com AD.
* Ajustes realizados na descrição do parâmetro de [habilitar senha pessoal](https://tdn.totvs.com/pages/viewpage.action?pageId=544182961&preview=/544182961/684009665/Credenciais%20do%20usu%C3%A1rio.JPG). O ajuste também promoveu a implementação da seguinte mensagem: *"Não é possível adicionar usuários quando a senha pessoal está desativada. Verifique as configurações do menu**[Segurança](https://tdn.totvs.com/x/BptUE)."*
* Corrigida inconsistencia ao configurar um aplicativo para navegável no TOTVS Identity.
* Ajustes realizados reforçando os níveis de segurança do TOTVS Identity.
* Corrigida inconsistencia para que o usuário consiga tornar uma [empresa como parceira.](https://jiraproducao.totvs.com.br/secure/attachment/1394526/Evid%C3%AAncia%2002.png)
* Ajustes realizados reforçando a segurança do TOTVS Identity.
* Corrigida inconsistencia ao realizar login no Identity.
* Ajustes realizados para que um usuário com status desativado não consiga realizar o login no Identity.

Disponível em 

* Corrigida inconsistência ao exportar relatório de auditoria no **TOTVS Identity.**

Disponível em 

* Corrigida inconsistência para realizar login no aplicativo do gmail aos usuários que consta apóstrofo no nome.
* Ajustes realizados para [exportar dados pessoais](https://tdn.totvs.com/pages/viewpage.action?pageId=317306108#Identity|Gerenciarusu%C3%A1rio-Exportardadospessoais) do usuário no **TOTVS Identity.**
* Realizado atualização das libs para segurança. Para mais detalhes, [clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417433731351-Vulnerabilidade-Produtos-TOTVS).

Disponível em 

* Ajustes realizados para apresentar a [autenticação multifator (MFA)](https://tdn.totvs.com/display/TIdentity/Identity+%7C+Login#Identity|Login-Fazerlogincomautentica%C3%A7%C3%A3omultifator(MFA)) ao acessar o link direto do aplicativo.
* Ajustes realizados após aceitar o [termo de consentimento](https://tdn.totvs.com/x/MQxpHw) do **TOTVS Identity.** Com os ajustes, uma animação de *loading* será apresentada enquanto a requisição está sendo processada.
* Corrigida inconsistência apresentada ao [gerar senha temporária](https://tdn.totvs.com/pages/viewpage.action?pageId=317306108#Identity|Gerenciarusu%C3%A1rio-Gerarsenhatempor%C3%A1ria) de um usuário sem e-mail.
* Ajustes realizados ao consultar informações do Active Directory no [Dashboard](https://tdn.totvs.com/x/q4HtEw). Com os ajustes, será apresentado as informações dos AD's cadastrados para empresa, independente se houver sincronização ou não com o SmartSync.

Disponível em 

* Ajustes realizados ao [adicionar usuário](https://tdn.totvs.com/x/1AqbEg) no **TOTVS** Identity. Com os ajustes, o novo usuário cadastrado será vinculado somente aos aplicativos que estão no grupo Everyone.
* Corrigida inconsistência ao [adicionar usuário](https://tdn.totvs.com/x/1AqbEg) no **TOTVS** Identity com um e-mail já cadastrado para outro usuário. Com a correção, retornará a seguinte mensagem: *"Já existe outro usuário com o mesmo endereço de e-mail na empresa."*
* Correção de inconsistência no contador de usuários de um determinado [grupo](https://tdn.totvs.com/x/1wiWHQ) do **TOTVS Apps.**
* Ajustes realizados ao [adicionar usuário](https://tdn.totvs.com/pages/viewpage.action?pageId=496371921#Administra%C3%A7%C3%A3o|Usu%C3%A1rios-Adicionarusu%C3%A1rioadicionar) no manager sem associá-lo a um grupo. O ajuste contempla que o novo usuário adicionado, seja apresentado na listagem, sem a necessidade de atualizar a página.
* Liberada nova versão 4.1.15 do SmartSync. Essa versão atualiza a API que comunica com o Active Directory para o reset de senha, compatibilizando com versões mais recentes do Windows Server.

Disponível em 

* Correção de inconsistência apresentada ao tentar [adicionar](https://tdn.totvs.com/x/1AqbEg) e [excluir](https://tdn.totvs.com/pages/viewpage.action?pageId=317306108#Identity|Gerenciarusu%C3%A1rio-Excluirusu%C3%A1rio) usuários na página do **TOTVS Identity.**
* Realizado ajustes ao [adicionar e importar](https://tdn.totvs.com/x/0QiWHQ) registros de usuários que contenham acentuação.
* Correção de inconsistência apresentada ao realizar o aceite do [termo de consentimento.](https://tdn.totvs.com/x/MQxpHw) Após realizado o aceite, o usuário será redirecionado para a página de [Launchpad](https://tdn.totvs.com/x/8ppUE). 4789

Disponível em 

* Ajustes realizados na página do aplicativo **TOTVS Tasks.**Com os ajustes, ao selecionar um [responsável da tarefa,](https://tdn.totvs.com/x/W1TvH) os usuários inativos não serão apresentados na busca.

Disponível em 

* Realizado ajustes na mensagem apresentada antes de [remover um grupo](https://tdn.totvs.com/display/fluig/Identity+%7C+Grupos?draft=true#Identity|Grupos-Removergrupo) no **TOTVS Identity**. Com o ajuste, a mensagem passa a informar a quantidade de usuários e aplicativos associados ao grupo a ser excluído.
* Correção de inconsistência apresentada na tela de validação do captcha. A correção promoveu a correta visualização dos caracteres do captcha, ao tentar redefinir ou desbloquear a senha através do [Credential Provider.](https://tdn.totvs.com/x/1oRbDQ)

Disponível em 

* Corrigida inconsistência ao acessar um aplicativo da plataforma **TOTVS Apps**. Com a correção, o nome do aplicativo passa a ser apresentado na página de login do **TOTVS Identity**.
* Correção de vulnerabilidade no **TOTVS Identity**. A correção promoveu a alteração dos cookies "IDMELB" e "JSESSIONID" para não permitir que sejam atribuídos na resposta retornada os mesmos valores arbitrários enviados na requisição.

Disponível em 

* Corrigida inconsistência ao [gerenciar a autenticação multifator](https://tdn.totvs.com/display/TIdentity/Identity+%7C+Multi-Factor+Authentication#Identity|Multi-FactorAuthentication-Gerenciaraautentica%C3%A7%C3%A3omultifator) na aba [segurança](https://tdn.totvs.com/x/BptUE). A correção promoveu a correta funcionalidade da ativação e desativação obrigatória do MFA, para os grupos desejados.
* Correção de inconsistência ao sincronizar usuários em grupos do [Active Directory](https://tdn.totvs.com/x/W55UE)  para o **TOTVS Identity**.

Disponível em 

* Corrigida inconsistência ao buscar registros de relatório de auditoria do tipo papéis. A correção promoveu que ao filtrar as buscas com o campo responsável vazio, todos os registros existentes passaram a ser apresentados.

Disponível em 

* Corrigida inconsistência ao acessar o Login do **TOTVS Identity**.
* Corrigida inconsistência no processo de exclusão de usuários do app **TOTVS**Learning, quando estes eram excluídos do Identity.
* Realizado ajuste no processo de desativação de usuários no Identity, para que no provisionamento dos usuários para o Protheus, seja possível reconhecer se deve ou não provisionar o usuário.
* Ajustes realizados na tela [Importar Usuários](https://tdn.totvs.com/pages/releaseview.action?pageId=496371921) do **TOTVS** Identity, o nome do produto passa a ser apresentado com o seguinte texto *"[Importar usuários](https://tdn.totvs.com/pages/viewpage.action?pageId=496371921) para o Manager é muito simples".*
* Ajustes realizados no texto da tela de [assinatura](https://tdn.totvs.com/x/hSc9I) do manager, quando o usuário possui o Identity e não possui nenhum aplicativo No-Code. O novo texto *"Sua empresa não possui nenhum aplicativo TOTVS Apps"* passa a ser apresentado na tela de aplicativos e no gerenciar conta do TOTVS Identity.
* Correção de inconsistência na tela de Filtrar Registros dos Relatórios.

## 2021

---

Disponível em 

* Realizada melhoria na segurança nos retornos de API.

Disponível em 

* Corrigida inconsistência na sincronização de usuários vinculados a grupos no [Active Directory](https://tdn.totvs.com/pages/viewpage.action?pageId=317306108#Identity|Gerenciarusu%C3%A1rio-Provisionarusu%C3%A1rionoActiveDirectory), cujo nome contenha o caractere espaço (" ").
* Corrigido intercorrência no círculo de perfil ao acessar o primeiro login ou a troca de empresa no **TOTVS Identity**. Com a correção o elemento passou a ser exibido no layout.

Disponível em 

* Inconsistência corrigida na aba [Segurança](https://tdn.totvs.com/x/BptUE) do TOTVS Identity. O usuário que possui acesso a mais de uma empresa e caso tenha termo de consentimento para aceitação, será realizado *logout* para que no próximo login, seja apresentado o  para aceitação ou não.
* Corrigida inconsistência apresentada nos dados dos usuários ao utilizar o TOTVS Identity com ativação do
* Correção de inconsistência ao aceitar um usuário no *Active Directory*. Com a correção o usuário aceito do  no Identity passa a ser exibido no manager.
* Corrigida inconsistência apresentada na tentativa de acesso do usuário ao aplicativo [Fluig Analytics.](https://tdn.totvs.com/x/8ppUE)
* Realizado ajustes na tela de alteração da parametrização do SAML. Com os ajustes, uma mensagem solicitando a confirmação das alterações será apresentada.
* Inconsistência corrigida ao importar usuários à plataforma e sincronizando-os ao aplicativo TOTVS Learning.
* Correção realizada ao atualizar o campo global **Nome do Executável ou Atalho**, na aba **Entrar** em configurações do [a](https://tdn.totvs.com/x/2RK4Ew)[plicativo Protheus](https://tdn.totvs.com/x/2RK4Ew). Com a correção o valor pessoal do usuário também é atualizado de acordo com as informações do campo global.
* Corrigidos pontos de instabilidade no login AD do Identity.
* Corrigida inconsistência ao fazer o provisionamento de usuários no aplicativo Fluig.

Disponível em 

* Corrigida inconsistência apresentada ao adicionar um Usuário em . Com a correção, ao cadastrar um usuário no manager que já possui e-mail associado à alguma conta do Identity, a mensagem a seguir será apresentada: "*Identificamos que este usuário já está vinculado a uma conta TOTVS Identity. Para acessar o sistema, será necessário utilizar a senha cadastrada".*
* Melhoria realizada ao executar o processo de . A melhoria alterou a mensagem de provisionamento AD quando as configurações de integração com AD estiverem incorretas ou quando houver problema de comunicação entre Smartsync e Identity.
* Realizado correção no link encontrado no rodapé do produto.  Ao clicar neste link a página do  será apresentada.
* Ajustes realizados nos cards da tela [Gerenciar Conta](https://tdn.totvs.com/x/d62iHQ). Com esses ajustes, todos os cards passaram a ser clicáveis.

Disponível em 

* Ajustes realizados no redirecionamento ao acessar a URL do Identity. A correção alterou o Serviço de Autenticação Central (CAS) para desconsiderar os *endpoints* ao realizar o login na página do Identity.
* Melhoria na comunicação entre produto e base de dados visando melhoria na segurança.
* Corrigida inconsistência apresentada ao acessar o aplicativo Educação Empresarial - EAD.

Disponível em 

* Alteração no relatório de [Auditoria](https://tdn.totvs.com/x/HTLNI), referente aos dados de papéis:
  + Adicionado ao filtro parâmetro que permite o usuário filtrar por Responsável ou Afetado.
  + Incluído nome e e-mail do usuário afetado no registro de eventos de remoção e adição de usuário em papéis.

Disponível em 

* Correção de inconsistência ao clicar no botão "Aceitar todos os grupos pendentes" de um AD.
* Ajuste realizado na tela de configurações do Active Directory, para que o sistema só aceite um novo comando após o primeiro ser concluído.

Disponível em 

**A troca de logo dos aplicativos ficou mais prática!**  
Ajustar a logo dos seus aplicativos está muito mais fácil. A nova interface agora permite redimensionar a imagem escolhida, dar zoom, girar ou rotacionar, tudo isso para que a imagem seja posicionada da melhor forma possível.

Aproveite a novidade e dê uma renovada na logo dos seus aplicativos.

Saiba mais

Para mais detalhes, consulte a documentação de .

Disponível em 

* Corrigida inconsistência na ativação do usuário por API, onde o usuário não era ativado no AD, mesmo estando habilitada a opção de "Sincronizar mudanças no estado usuário do Identity para o Active Directory".
* Correção de inconsistência na sincronização de usuários do TOTVS Identity para os aplicativos.

Disponível em 

* Correção realizada para trazer os eventos de inclusão, alteração e remoção de papéis dos usuários, no relatório de auditoria.
* Ajustes para que a desativação do usuário funcione corretamente quando a opção de "Sincronizar mudanças no estado usuário do Fluig Identity para o Active Directory" estiver habilitada.

Disponível em 

**Mais autonomia para os seus usuários!**  
Neste ano trouxemos novidades incríveis na configuração do recurso de autenticação multifator do Identity. Dando continuidade nessas melhorias, liberamos uma solução que vai trazer mais autonomia para seus usuários que tenham MFA configurado, em caso de troca do aparelho ou exclusão da conta no aplicativo.  
A solução consiste em alguns códigos de recuperação exclusivos, que devem ser armazenados pelo usuário em lugar seguro no momento da configuração de MFA, para serem utilizados caso seja necessário restaurar a configuração.  
Isso garante que os usuários consigam realizar a restauração sem precisar recorrer à administração da empresa.

CódigosConfigurações de segurançaCódigos de recuperaçãoRestauração da configuração de MFA no login

Para mais detalhes, acesse as documentações de  e .

**Correções**

* Corrigida inconsistência que fazia os aplicativos serem desvinculados do usuário.
* Correção de inconsistência no relatório de auditoria.

Disponível em 

* Correção realizada para que a autenticação ocorra normalmente para usuários com samAccountName maiúsculo no documento de AD.

Disponível em 

* Ajustes no layout da tela Meu Perfil do usuário comum, que aparecia desconfigurada.
* Correção de inconsistência na criação de usuários, onde o usuário não era associado ao grupo EVERYONE e por consequência ficava sem acesso aos aplicativos associados a este grupo.

Disponível em 

**Quer deixar o MFA obrigatório para algumas pessoas, e opcional para outras?**

Agora isso é possível! Você pode indicar a autenticação multifator como obrigatória para alguns grupos de usuários, e deixá-la como opcional para outros.

Essa novidade traz um enorme benefício para garantir a segurança de suas informações: você pode configurar para que apenas gestores que lidam diariamente com informações sigilosas sejam obrigados a informar um duplo fator de autenticação, protegendo suas contas e suas informações, sem afetar o login dos usuários comuns.

**Simplificamos, agora cada pessoa pode desativar seu MFA**

Para tornar a autenticação um processo ainda mais simples, cada usuário comum agora tem autonomia para desabilitar o MFA em sua própria conta, através do menu de configurações. Mas atenção: se a pessoa estiver em um grupo com MFA obrigatório, ela precisará configurar o MFA novamente para conseguir acessar.

**Acompanhamento mais completo da segurança**

Agora quem administra a empresa pode ter um relatório de usuários que tiveram seu MFA desativado, quando o próprio usuário desativou a configuração no seu perfil ou mesmo quando essa ação foi realizada pela administração da empresa (contendo uma justificativa).

Outra informação importante que será disponibilizada e pode ser consultada por quem administra é para ver os grupos que tiveram MFA obrigatório ativado ou desativado.

MFA por grupoMFA por grupoDesativar seu MFARelatório de gerenciamento do MFA

Conheça mais detalhes nas documentações de  e  

Disponível em 

* Correção de inconsistência na validação da senha ao tentar desativar o MFA do usuário.

Disponível em 

* Correção de inconsistência no download do relatório de Acessos bem sucedidos.
* Correção de inconsistência na criação de usuários, onde o usuário não era associado ao grupo EVERYONE e por consequência ficava sem acesso aos aplicativos associados a este grupo.

Disponível em 

* Correção de inconsistência na integração do TOTVS Identity com o AD da Azure.

Disponível em 

**Reset da configuração da autenticação multifator**

Melhoramos o reset da configuração da autenticação multifator dos usuários da empresa. Quem administra a empresa agora precisa informar senha e justificativa para realizar o reset de MFA de usuário, e essa informação ficará registrada em histórico e posteriormente poderá ser consultada no relatório de auditoria.

Disponível em 

* Correção de inconsistência no download do relatório de Acessos bem sucedidos.

Disponível em 

**MFA - Novidades para trazer segurança em dobro**

Você conhece o recurso de autenticação multifator (MFA) do TOTVS Identity? Trata-se de uma configuração que permite usar um segundo fator de autenticação para acessar o contexto da empresa, sendo este um código gerado pelo aplicativo  ou outro aplicativo autenticador de sua preferência.

Agora a administração da empresa pode configurar que a autenticação multifator seja obrigatória para o grupo de usuários Everyone. Mas atenção: ao habilitar o MFA obrigatório na empresa, todas as pessoas precisarão autenticar-se via interface. Se houver alguma integração que esteja fazendo login via API, esse recurso não será suportado e a integração irá parar de funcionar.

**Instruções diretamente na tela de login**Quando a opção de MFA obrigatório estiver habilitada e a pessoa que está tentando autenticar-se ainda não tiver o MFA configurado em seu perfil do Identity, na tela de login serão apresentadas orientações completas sobre o procedimento, incluindo um link para download do aplicativo My Safe id na Store e o QR code de ativação.

**Ative essa opção e mantenha os dados de sua empresa ainda mais seguros!**

#f2f2f2#f2f2f2

Consulte o passo a passo nas documentações relacionadas:

**Correções**

* Adicionado CAPTCHA de verificação ao utilizar o recurso de Auto-inscrição no TOTVS Identity.
* Correção de inconsistência no relatório de acessos bem sucedidos.

Disponível em 

**Correções**

* Ajustes no cadastro de usuários, para apresentar uma mensagem de aviso caso o e-mail informado já esteja vinculado como e-mail secundário de outro usuário da empresa.
* Correção de inconsistência no cadastro do usuário, que estava sendo criado com o status Ativado em vez de Convidado.
* Correção realizada para que a autenticação ocorra normalmente para usuários com samAccountName maiúsculo no documento de AD.

Disponível em 

**Correções**

* Correção realizada nos links **Baixar gerador de Perfil SSO para Fluig Identity** e **Baixar API de reset de senha e desbloqueio** das configurações de Segurança.
* Correção de inconsistência na autenticação quando o e-mail do usuário continha hífen.

Disponível em 

**Correções**

* Efetuados novos ajustes para prevenção de ataques e correção de falhas de segurança.

Disponível em 

**Correções**

* Efetuados diversos ajustes para prevenção de ataques e correção de falhas de segurança.
* Correção de inconsistência que impedia a troca de e-mail pela tela de perfil do usuário.
* Correção de inconsistência no relatório de acessos bem sucedidos.
* Realizado ajuste ao habilitar o CAPTCHA na autenticação do Identity, quando houver problema no login por credenciais inválidas, o CAPTCHA é recarregado para nova validação.

Disponível em 

**Correções**

* Inclusão de bloqueios de segurança para evitar ataque de enumeração de usuários.

## 2020

---

**DESTAQUES**

Disponível em 

**Login sem e-mail: mais uma possibilidade de autenticação!**

Atendendo a uma necessidade de clientes dos mais variados segmentos, agora é possível configurar para que um usuário faça seu acesso ao TOTVS Identity através de um nome de usuário, em vez do e-mail. Esse recurso é muito útil nos casos em que nem todos os colaboradores da empresa possuem seu próprio e-mail corporativo.

**Adicionando usuários sem e-mail**  
Primeiramente, é necessário solicitar ao time de atendimento, para que a liberação do login com nome de usuário seja aplicada na empresa. Depois que for liberado, o administrador poderá definir se o acesso sem e-mail será permitido, durante a inclusão de novos usuários.

**Sem e-mail, como fica a redefinição de senha?**  
Os usuários criados sem e-mail não terão como utilizar a função Esqueceu sua senha? da tela de login. Caso não se lembrem da senha informada, poderão solicitar ao administrador uma nova senha. O administrador pode acessar o cadastro do usuário, gerar uma senha temporária e repassar ao colaborador, para que ele consiga acessar o TOTVS Identity.

Confira mais detalhes nas documentações relacionadas:  e .

Disponível em 

**Novas opções no relatório de Auditoria**

No mês de maio liberamos o relatório de Auditoria, com apenas duas opções de dados. Agora esse relatório está muito mais completo, trazendo as seguintes opções de dados: **Aplicativos**, **Grupos**, **Perfis** **do usuário** e **Papéis.** Você pode filtrar os dados conforme desejar, receber os dados em seu e-mail e ainda obter o detalhamento de cada evento apresentado em tela no formato JSON. Acesse a documentação de  e saiba mais!

falseAuditoriatrueRelatório de auditoria sem registrosRegistros de auditoria encontradosMais detalhes do evento

Disponível em 

**Plugin do Identity**

Está disponível para download na **Chrome web store** o plugin **Fluig Identity**, que possibilita o login em uma ampla variedade de aplicativos na Web, a partir do Lanchpad do TOTVS Identity. Confira mais informações do plugin no [site oficial](https://chrome.google.com/webstore/detail/fluig-identity/mofhjibbjkonpgnejododmahilkbconf).

Veja a seguir o login no site Linkedin a partir do aplicativo no Identity:

Disponível em  

**Novidade! Liberamos o relatório de auditoria**

O Identity lançou agora mais um recurso para trazer segurança aos seus usuários: o relatório de auditoria. Com esse relatório, os administradores podem acessar duas opções de dados: Perfis do usuário e Papéis. 

* Perfis do usuário mostra os eventos de adição/remoção/edição/visualização de usuário.
* Papéis apresenta os eventos de criação/remoção/edição de papel, usuário adicionado/removido de papel, grupo adicionado/removido de papel.

Veja as telas abaixo:

falseRelatório de auditoriaRelatório de auditoriaJSON exportado

Confira mais detalhes na [documentação do novo recurso](https://tdn.totvs.com/x/HTLNI) e confira também os  que estão disponíveis para os administradores do Identity.

Disponível em  

**Fluig Identity agora é TOTVS Identity!**

Hoje em dia, tudo à nossa volta está em constante evolução, não é mesmo? E aqui na TOTVS não é diferente. Por isso, reformulamos nossa arquitetura de marca com o objetivo de simplificar a forma como nossos produtos são apresentados, facilitando o entendimento do nosso portfólio pelo mercado.

Isso quer dizer que, a partir de agora, o fluig Identity passa a se chamar **TOTVS Identity**: um aplicativo **by Fluig** com toda a força da marca **TOTVS**!

Dessa forma, a tela de login do Identity foi totalmente remodelada, para atender à nova arquitetura. Mas, pode ficar tranquilo! Você continua acessando com o mesmo endereço normalmente, somente o layout da tela que teve alterações. Veja como ficou:

**E tem mais...**

**Integração com o Microsoft Azure**

Para facilitar ainda mais o gerenciamento dos seus usuários, liberamos uma nova forma de integração com o Active Directory, por meio do Microsoft Azure. Em poucos passos você consegue adicionar um novo AD, diretamente pelas telas de configuração do Identity e do Microsoft Azure, sem a necessidade de aprimorados conhecimentos técnicos.

Consulte o passo a passo na documentação de  e aproveite!

Disponível em  

**O poder nas suas mãos, troca de e-mail Identity**

Pensando nas melhorias que nossos clientes nos propõem, elaboramos mais uma melhoria no fluig Identity. A troca de e-mail pelo usuário veio para facilitar ainda mais sua experiência com a gente!

Agora o administrador da empresa poderá alterar seu e-mail, conforme desejado, através do menu **Gerenciar conta**. A confirmação da alteração se dará por meio de um e-mail enviado ao novo endereço de e-mail cadastrado.

E ainda tem mais!

O administrador poderá habilitar essa opção para os usuários básicos do Identity, assim, com a permissão do administrador da empresa, cada usuário poderá fazer o controle dos seus dados.

Por meio do menu **Meu perfil** o usuário básico poderá alterar seu e-mail de acesso. Basta confirmar a alteração por meio de um e-mail enviado para o novo endereço cadastrado, e seu novo e-mail de acesso estará gravado. Fácil não? Veja as novidades:

11Alterar e-mail administrador1Alterar e-mail usuário básico

Disponível em 

**Gerenciamento de dados pessoais**

Buscando se adequar cada vez mais nos padrões da nova LGPD criamos mais uma novidade que vai facilitar ainda mais seu dia a dia na empresa. Agora, ao marcar dados como pessoal você terá a vantagem de realizar o gerenciamento destes dados. Por meio de uma lista que conterá todos os campos que foram marcados como dado sensível quando cadastrados.

Além da listagem dos campos, você poderá ordená-los conforme a necessidade, além de poder visualizar cada campo com suas respectivas informações. Também é possível realizar a edição do campo por meio do ícone de lápis. Ao abrir a edição do campo você poderá alterar a classificação e justificativa que foram usadas para aquele campo. Além de poder excluir os campos marcados como pessoal.

Eai gostou da novidade?

Disponível em  

**Novo cabeçalho Identity - mais moderno, funcional e pensado para você!**

Buscando uma melhor experiência para o nosso usuário, apresentamos o novo cabeçalho reformulado do Identity. Muito mais funcional e moderno, ele traz consigo muito mais facilidade no manuseio das informações e no modo de pesquisa. Tudo isso de forma prática e visual.

Basicamente, as mudanças realizadas permitiram que os itens do menu fossem alocados na própria barra superior, dando assim maior destaque as opções mais solicitadas. O menu de configuração ganhou seu próprio espaço, contendo agora somente itens que necessitam de configuração. No perfil, agora identificado pela inicial do usuário, estão contidas todas as informações pessoais referente a empresa e ao próprio usuário.

Confira essa novidade hoje mesmo!

**CORREÇÕES**

Disponível em 

* Correção de inconsistência na autenticação multifator (MFA).

Disponível em 

* Correção de inconsistência na sincronização de grupos do AD para o SmartSync.   
  Instalador do SmartSync versão 4.1.12
* Correção de inconsistência na inclusão de novo usuário.

Disponível em 

* Correção de inconsistência que impedia a exclusão de usuário.
* Ajustes de layout na tela de edição do **E-mail de recuperação**.

Disponível em 

* Realizado ajuste nos cookies para evitar inconsistências na renderização da widget Analytics no TOTVS Fluig Plataforma.

Disponível em 

* Realizado reforço de segurança quando a autenticação utiliza CAPTCHA.

Disponível em 

* Correção de inconsistência na exclusão de usuário convidado.

Disponível em 

* Removida da tela de Gerenciar Active Directories a exibição da quantidade de usuários e grupos pendentes. Agora é apresentada a opção Visualizar, que direciona para a tela de listagem de usuários.
* Inclusão de novo script no Desktop SSO. Com isso, houve alterações nos passos de configuração do Desktop SSO. Para consultar o passo a passo atualizado, .

Disponível em 

* Realizado ajuste para apresentar corretamente a alteração de um ícone de aplicativo customizado.

Disponível em 

* Realizado ajuste para apresentar corretamente no perfil do usuário a empresa a qual pertence.
* Correção realizada para apresentar o logo da empresa na página de login do Identity após alterá-lo na aba Customização.
* Correção realizada para abrir a lista de aplicativos navegáveis da empresa quando os usuários acionarem o botão Adicionar aplicativo.

Disponível em  

* Ajuste realizado para inserir imagens de segurança no Identity e para que a mesma seja cadastrada corretamente para o usuário selecionado.

Disponível em 

* Correção realizada para que a tela de login do Identity seja exibida corretamente em navegadores IE's.

Disponível em  

* Realizada correção na tela do Identity onde ao realizar uma solicitação de reset de senha que foi desabilitada, seja informado ao usuário um aviso em tela, de que esta ação não é permitida.
* Aplicado ajuste na tela de reset de senha, mostrando ao usuário uma mensagem caso ele não tenha atendido os requisitos para cadastro de uma nova senha.

Disponível em 

* Ajuste realizado para que ao inserir um e-mail com sintaxe inválida no Identity, uma mensagem informando o usuário seja apresentada para que o mesmo insira um e-mail válido.

## 2019

---

Disponível em 

**Cadastro de dados pessoais seguro!**

Pensando nas vigências de segurança para as empresas que utilizam o fluig Identity. Apresentamos o novo cadastro de campos customizados com dado pessoal.

Agora, ao adicionar um campo customizado, você terá a opção de definir este campo como um campo que receberá um dado pessoal ou sensível.

Essa melhoria visa a segurança da empresa no Identity, como também a segurança dos usuários ao informar um dado pessoal como rg ou cpf. Pois ao incluir um campo customizado com dado pessoal definido, uma classificação e justificativa terão de ser incluídos como motivo da solicitação deste dado.

Além da opção de definir se este campo será sensível ou não por meio do botão **Este dado é sensível?** O administrador tem a tranquilidade e transparência no cadastro de campos customizados para seus usuários.

**Gostou? Ainda tem mais novidade!**

Além disso tudo, toda a tela de cadastro de campos customizadas foi modernizada, trazendo mais fluidez para sua empresa.

Disponível em 

**Mais segurança para sua empresa no Identity**

Pensando na segurança dos dados da sua empresa, implementamos uma novidade!

A tela de **Cadastro de termo de consentimento** trará tranquilidade ao administrador da empresa. Por meio de um arquivo PDF contendo os requisitos e regras da sua empresa, você poderá incluir este documento que será apresentado para os usuários no momento do login.

Basta o aceite dos usuários e você garante que os dados da sua empresa estarão mais seguros.

Veja a novidade na prática!

Disponível em  

**Correções**

* Realizada correção para que as imagens de logo da empresa sejam apresentadas da tela de login do usuário de forma correta.
* Corrigida a modal de login dos aplicativos SAML.
* Implementado crop de imagem do logo da empresa exibido da tela de login do Identity, localizado no cabeçalho da página.
* Corrigida inconsistência na tela de login, para que o campo e-mail não fique em vermelho quando o usuário tentar logar com nome de logon do AD, pois é aceito igualmente.

Disponível em  

**Redesenho da tela de login**

A página de login  ganhou um novo design, mais limpo e moderno.

**Correções**

* Corrigida a descrição do relatório de MFA;
* Ajustado a tradução do botão de Download de certificado na aba segurança;

Disponível em  

**Correções**

* Incluída opção de Exportar dados pessoais para que o administrador da empresa possa exportar os dados de um usuário do Identity, a partir do perfil deste usuário. Essa opção irá considerar apenas os dados do usuário na empresa em questão. Para saber mais acesse: Exportar dados pessoais.
* A partir de 22/10/2019 a ferramenta de relatórios do Identity limitará seu período de pesquisa por data, pois o aumento de armazenamento dos logs de eventos no Elastic Search está causando impacto de consumo. Para evitar indisponibilidade iremos armazenar logs com mais de 12 meses no AWS Glacier.
* Ajuste realizado para que o grupo EVERYONE seja criado apenas uma vez e na criação da empresa.
* Ajuste realizado no S3 para que a imagem Default seja apresentada corretamente quando o parâmetro 'Usar URL de Acesso Direto ao Aplicativo' estiver habilitado no aplicativo. Dessa forma, ao abrir a página de login com a URL direta a imagem será apresentada corretamente no formato de ícone.

Disponível em

**Nova opção para exportação dos dados pessoais de usuários**

Uma nova opção disponibilizada no [perfil dos usuários](https://tdn.totvs.com/pages/viewpage.action?pageId=317306108) permite que o administrador exporte em um arquivo do tipo JSON com os dados pessoais do indivíduo cadastrados naquela empresa e/ou importados do Active Directory, como nome, sobrenome, e-mail, telefone corporativo, etc.

**Redesenho da tela de login direto por aplicativo**

A página de login direto por aplicativo ganhou um novo design, mais limpo e moderno.

Disponível em

**Correções**

* Correção no [Desktop Launcher](https://tdn.totvs.com/pages/viewpage.action?pageId=235592303) para permitir a autenticação em aplicativos desktop.

Disponível em

**Correções**

* Retirada a opção Meu Perfil do menu de Perfil dos administradores de contexto. As informações desta página ainda podem ser consultadas na página [Gerenciar Conta](https://tdn.totvs.com/display/HF/Gerenciar+Conta). Para usuários comuns, a opção permanece.

* Redesenho da tela [Adicionar Novo Usuário](https://tdn.totvs.com/pages/viewpage.action?pageId=312150740).

Disponível em

**Correções**

* Correção no processo de criação do banco de dados do SmartSync para permitir o cadastro de novos domínios do Active Directory.

Disponível em

**Novas APIs para aceitar e rejeitar usuários importados do Active Directory**

Para facilitar o desenvolvimento de soluções que utilizam os serviços oferecidos fluig Identity disponibilizamos duas novas APIs para o gerenciamento de usuários importados do Active Directory: [Aceitar usuário](https://app.fluigidentity.com/api/core/doc/#!/Core_API_V1/acceptAdUserByEmail) e [Rejeitar usuários](https://app.fluigidentity.com/api/core/doc/#!/Core_API_V1/rejectAdUserByEmail).

Para utilizar as APIs é necessário gerar um [*access token*](https://app.fluigidentity.com/api/auth/doc/#!/IDM_Auth_Api_-_V1/token) a partir das credenciais de um administrador do contexto e informar como parâmetros o token do Active Directory do qual o usuário foi importado e o e-mail. As APIs são válidas apenas para usuários importados cujo status atual é [Pendente](https://tdn.totvs.com/pages/viewpage.action?pageId=273989076).

**Correções**

* Removida a opção "*Type Ldap*" das configurações de diretório no [SmartSync](https://tdn.totvs.com/pages/viewpage.action?pageId=242387507) por conta do fim do suporte ao protocolo Open LDAP no Identity anunciado em setembro/2018. Apenas diretórios do tipo Active Directory são suportados pelo fluig Identity.

* Ajuste nas informações enviadas pelo SmartSync durante a importação dos usuários para evitar erros "(413) *Request Entity Too Large*".

* Corrigida a importação de usuários cujo cadastro do campo e-mail no Active Directory possua um espaço antes ou depois do conteúdo. O espaço é removido durante a importação para que não ocorra falha na importação ou login.

* Corrigida a exibição no navegador Internet Explorer 11 da página "Adicionar Apps" acessível a partir do Launchpad do administrador.

* Corrigida a descrição da variável REDIRECT\_URL nas opções de Notificações por e-mail do painel de Configurações.

* Removido o espaço em branco exibido no abaixo do rodapé do Launchpad do administrador quando há um grande número de aplicativos adicionados.

* Corrigido o recurso de [renovação do certificado SAML](https://tdn.totvs.com/pages/viewpage.action?pageId=351373338) um período de 10 anos.

* Ajustado o retorno da tag "totalSize" do endpoint getAllApplicationUsers para que seja transmitido o valor correto.

Disponível em

**Acesse o Office 365 a partir do Launchpad do Identity**

O fluig Identity agora suporta o *Single Sign On* (SSO) de usuários no [Office 365](https://www.office.com). Para desfrutar desse recurso, é necessário utilizar o Office 365 em um cenário de [identidade híbrida](https://docs.microsoft.com/pt-br/azure/active-directory/hybrid/whatis-hybrid-identity): *"As soluções de identidade da Microsoft abrangem funcionalidades locais e baseadas em nuvem. Essas soluções criam uma identidade de usuário comum para autenticação e autorização para todos os recursos, independentemente da localização. Chamamos isso de **identidade híbrida**."*

Nessa estrutura, os usuários criados no Active Directory local são sincronizados com o Azure AD/Office 365 através da aplicação AD Connect. A cada um desses usuários é atribuído um código de identificação chamado "[ImmutableID](https://blogs.technet.microsoft.com/latam/2017/11/30/o365-identity-sourceanchorandimmutableid/)". Esses mesmos usuários também são importados para o Identity via SmartSync, que então usa o ImmutableID para identificar e autenticar os usuários no Office 365.

Para facilitar essa configuração, disponibilizamos um novo aplicativo global chamado Office 365 no Identity e preparamos uma [documentação](http://tdn.totvs.com/pages/viewpage.action?pageId=504804383) para guiá-lo no processo de ativação.

**Correções**

* Retirados os campos Cargo, Endereço corporativo e Telefone corporativo da tela  para torná-la mais simples e enxuta. Os campos ainda estão disponíveis na tela  e também são preenchidos via integração com o Active Directory.

* Removida a integração com o LinkedIn devido à descontinuidade das APIs utilizadas pelo Identity para a importação dos dados. Os dados previamente importados para o Identity por perfis conectados ao LinkedIn foram permanentemente excluídos.

* Retirado o campo Celular do perfil dos administradores dos contextos porque esse dado não é mais utilizado por recursos da ferramenta. Os números previamente cadastrados foram permanentemente excluídos.

Disponível em

**Correções**

* Corrigido o redirecionamento ao utilizar a widget Mini Launchpad do fluig, para que o usuário seja encaminhado diretamente ao aplicativo selecionado ao invés do [Launchpad](http://tdn.totvs.com/display/HF/Launchpad) do Identity.

Disponível em

* Versão 4.1.9 do SmartSync disponível para download com correções para ambientes que utilizam mais de um Active Directory em uma única instalação.

* Incluída a opção "Excluir" na lista de usuários [Rejeitados](http://tdn.totvs.com/pages/viewpage.action?pageId=273989076). Essa opção remove todos os dados do usuário importado de um Active Directory daquela empresa no Identity.

Disponível em

**Correções**

* O tempo de sessão para usuários comuns e administradores de contextos do fluig Identity foi ajustado para que a sessão seja encerrada após 2 horas de inatividade. Ou seja, caso o usuário deixe de interagir com o Identity por mais de 2 horas, terá que informar novamente as credenciais de acesso (e-mail/senha).

* O valor do ObjectGUID dos usuários importados e aceitos a partir de um Active Directory será exibido na página [Gerenciar Usuário](http://tdn.totvs.com/pages/viewpage.action?pageId=317306108), acionando a opção **Mais Detalhes**.

 Disponível em

**Aceite automático de usuários do Active Directory**

A partir de agora o administrador do contexto poderá configurar os diretórios do Active Directory integrados ao fluig Identity para aceitar automaticamente todos os usuários importados. Basta adicionar um novo diretório ou editar um dos diretórios existentes e ativar a opção **Deseja habilitar o Aceite Automático?**.

Uma vez habilitada, os usuários criados no AD e importados pelo SmartSync, ao invés de ficarem como pendentes, serão imediatamente aceitos no contexto.

**Correções**

* Ao alterar o e-mail de um usuário no Active Directory, os aplicativos do tipo SAML a que este usuário estiver associado serão atualizados com o novo e-mail automaticamente. Essa configuração é válida apenas para apps SAML que usam o e-mail do usuário no campo Mapeamento de ID.

Disponível em

**Novo design do menu superior**

Ano novo, design novo. O menu superior das páginas do Administrador do fluig identity ganhou novos ícones e rótulos para facilitar a navegação.

**Monitore o contexto da sua empresa com os novos relatórios**

O mais novo recurso do fluig Identity oferece ao administrador do contexto quatro relatórios para monitorar a utilização e o acesso aos dados da empresa. Cada relatório oferece dados específicos como o endereço IP de origem, localização, data e hora e endereço de e-mail para que o administrador possa acompanhar e rastrear as atividades realizadas pelos usuários na empresa.

854480

Além disso, os relatórios contam com uma opção para exportá-los em um arquivo no formato CSV para que o administrador possa encaminhá-los a quem desejar.

Confira hoje mesmo a opção [Relatórios](http://tdn.totvs.com/pages/viewpage.action?pageId=416853988) no menu principal do Identity!

**Correções**

* Correção no provisionamento de usuários em projetos na GoodData através dos aplicativos.

Disponível em

**Correções**

* Melhorada a performance das consultas às atualizações em grupos do Active Directory realizadas pelo SmartSync. Para aplicar esta correção é necessário  para a versão 4.1.7.

## 2018

---

**master-185**

Disponível em

**Correções**

* Corrigida a validação de domínio nas tentativas de login originadas a partir do [Desktop Launcher](http://tdn.totvs.com/pages/viewpage.action?pageId=235592303).

O domínio da empresa no fluig Identity é informado nos campos **SSOProfileStoreRestUrl** e **UserStoreRestUrl**. Por exemplo, [https://suaempresa.fluigidentity.com.](https://minhaempresa.fluigidentity.com.)

* Ajustada a mensagem de erro da API 1.0 em situações que o login ou senha informados para autenticação no endpoint estiverem incorretos. A mensagem de retorno será sempre "Não autorizado".

**master-184**

Disponível em  

**Melhorias de infraestrutura para tornar o fluig Identity ainda mais resiliente**

A partir de agora o fluig Identity passa a ser hospedado em uma estrutura de contêineres, o que representa uma grande evolução na arquitetura da ferramenta e proporcionará melhorias de estabilidade e escalabilidade, beneficiando os nossos clientes e usuários.

**master-183**

Disponível em

**Correções**

* Corrigido o provisionamento de usuários incluídos em grupos, inclusive o Everyone, após a associação destes grupos a aplicativos.

**master-172**

Disponível em

**Correções**

* Aprimorada a mensagem de erro ao tentar [adicionar um usuário](http://tdn.totvs.com/pages/viewpage.action?pageId=312150740) com um endereço e-mail já cadastrado como [e-mail pessoal](http://tdn.totvs.com/display/HF/Meu+Perfil#MeuPerfil-Cadastrare-mailpararecupera%C3%A7%C3%A3odasenhapessoal) em outra conta na mesma empresa.

**master-165**

Disponível em

**Correções**

* Os  no idioma Espanhol foram reestabelecidos, bem como a habilidade do administrador de editá-los.

**master-163**

Disponível em  

**Correções**

* Na aba Pessoal do [Launchpad](http://tdn.totvs.com/display/HF/Launchpad), ao acionar **Adicionar apps**, os aplicativos disponíveis para inclusão neste *launchpad* serão listados automaticamente. Anteriormente era necessário clicar sobre o *link* Pessoal no canto superior direito da página para exibí-los.

**master-159**

Disponível em

**Correções**

* Habilitada a troca de contextos diretamente através da URL, sem a necessidade prévia do usuário fazer *logoff* da empresa atual. Será apresentada uma página para confirmar a troca. Lembrando que não é permitido o acesso simultâneo a mais de uma empresa na mesma sessão. Saiba mais no [Help fluig](http://tdn.totvs.com/display/HF/Troca+de+contextos).

* Corrigida a exibição da lista de usuários pela página [Gerenciar Usuários](http://tdn.totvs.com/pages/viewpage.action?pageId=311633463) quando acessada a partir do navegador Internet Explorer 11.

**master-158**

Disponível em

**Correções**

* A opção de [troca de contextos](http://tdn.totvs.com/display/HF/Troca+de+contextos), que atualmente é exibida apenas quando o usuário autentica-se no fluig Identity usando a [Senha Pessoal](http://tdn.totvs.com/display/HF/Senha+Pessoal) ou via [SmartSync](http://tdn.totvs.com/display/fluig/SmartSync), foi habilitada também para logins a partir do [Desktop SSO](http://tdn.totvs.com/display/HF/Acesso+via+Desktop+SSO). Lembrando que a troca de empresas só está disponível para perfis existentes em mais de um contexto.

* O recurso [Aceitar Todos](http://tdn.totvs.com/pages/viewpage.action?pageId=273989076) da página de importação de usuários pendentes do Active Directory foi corrigido para que, caso algum usuário não possa ser aceito devido a uma inconsistência no cadastro, o processo não seja completamente interrompido e os demais usuários possam ser aceitos normalmente.

Usuários com dados corrompidos e que não possam ser importados durante o processo de aceite serão movidos para a lista de [Rejeitados](http://tdn.totvs.com/pages/viewpage.action?pageId=273989076#AceitarUsu%C3%A1riosPendentes-lista-rejeitados).

**master-156**

Disponível em

**Renove facilmente o certificado SAML do seu contexto no fluig Identity**

Todo contexto criado no fluig Identity possui um certificado SAML que é utilizado no processo de autorização dos usuários com aplicações que suportam esse protocolo. Após um determinado período, o certificado SAML expira e deve ser renovado pelo administrador do contexto.

Contextos criados no fluig Identity antes dessa atualização possuem certificados com validade de 5 anos. Contextos criados a partir de agora receberão certificados válidos por 10 anos.

Para simplificar esse processo, a seção Certificado SAML da página de  agora exibe a data de criação ou renovação do certificado e a data de expiração. Além disso, o administrador poderá renovar rapidamente o certificado SAML por um período de 10 anos através da opção .

Não se preocupe! O fluig Identity vai te avisar quando a data de validade do certificado SAML estiver a menos de 6 meses de expirar.

Após a renovação do certificado, é necessário atualizá-lo nas aplicações SAML integradas ao Identity, como o fluig, Zendesk e ERPs TOTVS, para garantir a continuidade do acesso dos usuários.

Acesse o guia " para saber como proceder quando o certificado SAML do seu contexto estiver prestes a perder a validade.

**master-153**

Disponível em

**Itens depreciados**

* A ferramenta de mapeamento de grupos foi depreciada a partir desta versão.

**master-151**

Disponível em

**Correções**

* Determinadas informações disponíveis no [Dashboard](http://tdn.totvs.com/display/HF/Dashboard) não eram apresentadas para administradores que possuem múltiplos contextos, mas são apenas usuários básicos nas demais empresas. Essa situação foi solucionada.

**master-150**

Disponível em  

**Correções**

* O recurso [Esqueceu Sua Senha](http://tdn.totvs.com/display/HF/Login#Login-Recupera%C3%A7%C3%A3odesenhapessoal) foi corrigido para que o *link* de redefinição de senha seja gerado corretamente nas situações em que o usuário informa caracteres maiúsculos ao preencher o endereço de e-mail.

**master-149**

Disponível em

**Um novo design para a tela de login**

A era Snowflake chegou ao fim no fluig Identity. Bem vindo à atualização ! Para acompanhar as novidades da plataforma fluig, a  do Identity ganhou uma cara nova, super *clean*.

**master-148**

Disponível

**Correções**

* Incluído suporte a endereços de e-mail que utilizam as novas extensões de domínio, como ".tech", ".cafe", ".bom", entre outros, para a criação de usuários, importação, acesso ao contexto e recuperação de senha.

* Reestabelecido o [Modo de provisionamento Fluig](http://tdn.totvs.com/display/fluig/Modo+de+Provisionamento+Fluig) entre o fluig e o fluig Identity. Ao configurar esse tipo de provisionamento, a criação do usuário no fluig é realizada no momento da atribuição do aplicativo Fluig com este usuário no Identity, e não apenas no primeiro acesso.

Atenção

Essa correção é compatível apenas com a [Atualização Waterdrop (1.6.4)](http://tdn.totvs.com/pages/viewpage.action?pageId=317319910) ou superior da plataforma fluig.

**master-147**

Disponível em

**Correções**

* Corrigida a notificação de [recuperação de senha](http://tdn.totvs.com/display/HF/Login#Login-Recupera%C3%A7%C3%A3odesenhapessoal) enviada pelo fluig Identity para que seja utilizado o mesmo idioma do navegador na mensagem.

* Retirado o campo Telefone de recuperação da página  dos usuários básicos devido à descontinuação do recurso.

* Liberada nova versão do SmartSync com melhorias na conexão entre a aplicação e o fluig Identity. .

* Compatibilização da [extensão do fluig Identity](https://addons.mozilla.org/pt-BR/firefox/addon/identity-manager-addon/) com as versões Quantum (57.0 ou superior) do navegador Mozilla Firefox.

**master-140**

Disponível em

**Correções**

* Ajustes na nova página de login para aderir às especificações de *whitelabel* da marca fluig.

* Incluído novo filtro "Por e-mail" na página de [Usuários Pendentes](http://tdn.totvs.com.br/pages/releaseview.action?pageId=273989076) importados a partir de um diretório LDAP.

* Adicionados os *links* para *download* do  nas páginas  (Usuário Básico) / [Gerenciar Conta](http://tdn.totvs.com.br/display/public/HF/Gerenciar+Conta) (Administrador).

## 2017

---

**master-128**

Disponível em

**Correções**

* O recurso de provisionamento de usuário no Active Directory foi incorporado ao novo *design* da página [Gerenciar Usuário](http://tdn.totvs.com/pages/viewpage.action?pageId=317306108).

* O componente Copiar () disponível em [diversas páginas](http://tdn.totvs.com/display/HF/Gerenciar+Active+Directories#GerenciarActiveDirectories-Copiartokendeconfigura%C3%A7%C3%A3odoActiveDirectory) do fluig Identity, foi atualizado para não depender mais do plugin Adobe Flash habilitado no navegador.

* Adicionada opção para editar o caminho do arquivo no aplicativo Protheus do tipo Executável SAML. Dessa forma os usuários poderão alterá-lo para um caminho diferente daquele definido pelo administrador do contexto, o que é especialmente útil para participantes que utilizam sistemas operacionais diferentes do padrão da companhia.

**master-126**

Disponível em

**Mais proteção para a sua empresa com a Autenticação Multifator + aplicativo safe id**

A autenticação multifator (do inglês *Multi-Factor Authentication* ou MFA) é um método de segurança que pretende garantir que apenas o dono da conta possa acessá-la, mesmo que outro indivíduo venha a descobrir a senha. No fluig Identity, essa validação ocorre com o apoio do novo aplicativo **safe id** para [iPhone](https://itunes.apple.com/br/app/safe-id/id1304505629?mt=8) e [Android](https://play.google.com/store/apps/details?id=com.fluig.mfa).

800450

Para configurar, é só baixar o safe id da loja do seu smartphone, escanear o  e pronto! O acesso à empresa estará protegido por uma camada adicional de segurança, mas continuará extremamente simples: o fluig Identity irá solicitar o token gerado pelo safe id durante o [login](http://tdn.totvs.com/display/HF/Login), logo após o e-mail e senha.

Basta informar o token exibido pelo app e o acesso será liberado. Apenas o usuário tem a posse do aparelho, portanto somente ele saberá qual é o token.

Dica

Consulte as documentações do  e  em que explicamos passo a passo como ativar e configurar a autenticação multifator na sua empresa e nas contas dos usuários.

**Acessar o Identity e fazer a gestão dos usuários nunca mais será igual!**

Complementando a chegada da autenticação multifator, duas importantes páginas do fluig Identity ganharam um novo visual, mais moderno, simplificado e muito mais bonito: [Login](http://tdn.totvs.com/display/HF/Login) e [Gerenciar Usuário](http://tdn.totvs.com/pages/viewpage.action?pageId=317306108).

release-266Login

A nova tela de Login não apenas está de cara nova, como também está *bem mais rápida* que a anterior! A redução no tempo de carregamento entre o servidor e o navegador **chega a 50%**, enquanto a exibição dos elementos da página está até **27% mais ágil**.

Gerenciar Usuário

A página Gerenciar Usuário mantém todos os recursos do *design* anterior, mas reorganizados de uma forma mais acessível e fácil de usar - além de uma nova opção para redefinir a configuração MFA da conta.

**Dá uma olhada nesse *design*! Não ficou incrível?**

**Correções**

* Os filtros de usuários - disponíveis em páginas como Gerenciar Usuários, Associar Usuário ao Grupo e Usuários Pendentes - foram ajustados para que nomes ou sobrenomes com acento, til, trema, etc. sejam localizados mesmo que informados sem esses sinais.

* Adicionada opção para editar o caminho do arquivo no aplicativo Protheus do tipo Executável SAML. Dessa forma os usuários poderão alterá-lo para um caminho diferente daquele definido pelo administrador do contexto, o que é especialmente útil para participantes que utilizam sistemas operacionais diferentes do padrão da companhia.

**master-119**

Disponível em

**Correções**

* Exibição da mensagem de falha na autenticação na tela de login quando informados usuário ou senha incorretos.

* Incluído botão **Atualizar listagem** para verificar o status do SmartSync e diretórios LDAP na página Gerenciamento do . A partir de agora, os status de conexão serão atualizados apenas ao abrir ou atualizar a página, ou ao acionar o botão Atualizar listagem.

* Corrigida a sincronização de usuários cujo sobrenome possui apóstrofo, por exemplo, "Sant'Anna" com o Active Directory. Para aplicar esta correção é necessário [atualizar o SmartSync](http://tdn.totvs.com/pages/viewpage.action?pageId=242387507) para a versão 4.1.2.

**master-116**

Disponível em

**SmartSync 4.1.1: Consumo de memória *muito* mais eficiente**

O novo SmartSync 4.1.1 chegou para aliviar a pressão sobre o uso de memória do seu servidor. Com essa atualização, a importação de grandes quantidades de usuários ou grupos do Active Directory para o fluig Identity consumirá até *18 vezes* menos memória RAM em relação à versão anterior da ferramenta.

No cenário abaixo, o SmartSync está fazendo a importação de 5000 usuários + 1400 grupos com 500 usuários cada do Active Directory e é possível observar a drástica diferença no consumo de memória entre as versões 3.0.7 e 4.1.1:

memoriaSmartSync 3.0.7SmartSync 4.1.1Atenção

Clientes com dificuldade para exportar processos e formulários do fluig Studio para ambientes fluig integrados com Identity devem atualizar o SmartSync para a versão 4.1.1 para corrigir esta situação.

**Reimportação de contas do diretório LDAP com apenas um clique**

Além da melhoria em performance, o SmartSync 4.1.1 dispõe de um novo recurso para reimportação de usuários e grupos do diretório LDAP através do botão **Reimport All**.

Esta opção pode ser útil em várias situações, por exemplo, caso algum usuário cadastrado no AD não tenha sido importado no fluig Identity, o administrador pode usar este botão para forçar uma nova sincronização de usuários.

**Correções**

* Correção na listagem das licenças existentes no recurso de Licenciamento de aplicativos, que impedia a criação de novas licenças.

**master-107**

Disponível em

**Correções**

* Correção na aplicação [Fluig Identity Credential Provider](http://tdn.totvs.com/display/fluig/Fluig+Identity+Credential+Provider), utilizada em conjunto com o recurso de redefinição de senha por imagens secretas.

**master-106**

Disponível em

**Correções**

* Corrigido o provisionamento e desprovisionamento de usuários em aplicativos do RAC.

**master-104**

Disponível em

**Gerenciamento de usuários renovado**

Atendendo a pedidos, a página Gerenciar Usuários recebeu melhorias visuais e ajustes por baixo dos panos que irão aprimorar a gestão dos usuários da sua empresa no fluig Identity.

O tempo de carregamento da lista de usuários foi reduzido, especialmente em empresas com grandes quantidades de usuários, os filtros da página foram aperfeiçoados, e uma nova coluna com a função da conta (Usuário Básico ou Administrador) foi incluída para facilitar a visualização desta informação.

E o botão Desbloquear?

Se o recurso de segurança por imagens secretas for utilizado em sua empresa, fique atento: o botão [Desbloquear](http://tdn.totvs.com/pages/viewpage.action?pageId=224103298#HabilitareConfiguraroServi%C3%A7o-DesbloqueioManualdesbloqueio), que era exibido após o número de tentativas erradas ser atingido, agora é apresentado na página individual dos usuários.

**Correções**

* A validação dos acessos ao fluig Identity utilizando o atributo sAMAccountName do Active Directory foi alterada para desconsiderar se os caracteres foram informados em caixa alta ou baixa pelo usuário.

* O acesso ao fluig através da URL em ambientes integrados ao fluig Identity e com autenticação CAS foi corrigido para que o usuário seja redirecionado corretamente para a plataforma após o login, e não para o Launchpad.

**master-99**

Disponível em

**Novos aplicativos do tipo GoodData tornam a integração com fluig Analytics e o TOTVS Analytics extremamente simples**

Para tornar a configuração do acesso ao fluig Analytics e TOTVS Analytics muito, mas *muito* mais fácil, disponibilizamos uma nova categoria de aplicativos no fluig Identity específica para integrações com o serviço GoodData. Basta informar o código do projeto Analytics fornecido pelo fluig (ou pela TOTVS), aguardar a validação e salvar!

A criação dos usuários no projeto Analytics também pode ser feita diretamente pelo aplicativo do Identity. É só atribuir os usuários e grupos desejados ao aplicativo e cuidamos da criação e da associação ao projeto pra você de forma automática, rápida e eficiente.

GoodDataFluig AnalyticsTOTVS AnalyticsUsuáriosGruposOperações

Não deixe de acessar a página  para conhecer os requisitos e saber como configurar e utilizar este novo tipo de aplicativo.

**Entre sem convite: ativação de usuários importados do Active Directory agora é instantânea**

Para agilizar a ativação dos usuários sincronizados do Active Directory e tornar todo o processo de cadastro no fluig Identity mais eficiente, enxugamos o fluxo entre a importação e o primeiro acesso dos usuários ao contexto.

A partir de agora, no momento em que o administrador do contexto no fluig Identity aceitar um usuário importado, o status deste usuário torna-se imediatamente Ativo, e não mais Convidado.

Os dias de esperar o recebimento de e-mails, acessar *links* para autenticação e vasculhar a caixa de entrada por convites ficaram no passado.

Esta regra também é válida para ambiente integrados ao OpenLDAP.

**Correções**

* Para que endereços de e-mail alterados no Active Directory e sincronizados com o fluig Identity também sejam atualizados no login de aplicativos SAML, foi disponibilizada a opção **Sincronizar login SAML com e-mail do AD**. O administrador deve acessar as configurações dos aplicativos SAML cadastrados e marcar esta opção para que a atualização sincronização dos logins seja ativada.

**Itens depreciados**

* A ferramenta de pesquisa geral, localizada no cabeçalho das páginas, foi depreciada a partir desta versão.

**master-72**

Disponível em

**Mais segurança e flexibilidade com a configuração de proxy no SmartSync**

Servidores Proxy são amplamente utilizados em ambientes corporativos com o objetivo de aumentar o controle e segurança da rede dentro de uma organização. Para auxiliar nessa tarefa, a partir da atualização 3.0.7 o [SmartSync](http://tdn.totvs.com/display/fluig/SmartSync) permitirá que o administrador defina as configurações de proxy que serão utilizadas pela aplicação para conectar-se ao AD Sync.

Esta novidade garante mais flexibilidade ao administrador que, por exemplo, deseje criar regras específicas para o SmartSync dentro do proxy da rede.

[Clique aqui](http://tdn.totvs.com/x/M4pyDg) e saiba como atualizar a sua instalação.

proxyPadrão do Sistema

* **SystemDefault**: Esta opção indica que as configurações de proxy do sistema operacional devem ser utilizadas pelo SmartSync para conexão com o AD Sync.

Personalizado

* **CustomProxy**: Esta opção permite que o administrador configure manualmente os dados do proxy através dos campos *Host*, *Port*, *Username* e *Password*. Caso o proxy não exija autenticação, os campos *Username* e *Password* devem ser deixados em branco.

Nenhum

* **NoProxy**: Esta opção define que o SmartSync deve tentar conectar-se diretamente ao AD Sync sem passar por um proxy.

AD Sync?

O AD Sync é o serviço responsável pela sincronização do fluig Identity com o Active Directory. O endereço do AD Sync varia conforme o ambiente utilizado, ou seja, no ambiente de produção é [https://app.fluigidentity.com/adsync](https://app.fluigidentity.com) enquanto no ambiente de homologação é [https://app.customerfi.com/adsync](https://app.customerfi.com).

**master-70**

Disponível em

**Correções**

* Corrigido problema de redirecionamento que causava a perda dos dados da autenticação SAML. Essa inconsistência afetava o acesso direto pela URL de aplicativos como o fluig, por exemplo, o acesso ao fluig Mobile e a autenticação via Desktop SSO.

**master-66**

Disponível em

**Acompanhe as empresas associadas com os relatórios de Parceiros**

Os parceiros fluig Identity agora podem extrair relatórios sobre as empresas associadas com detalhes a respeito das licenças atribuídas a aplicativos, como o status, responsáveis e as datas em que foram realizadas alterações. Saiba mais acessando a documentação de .

**Correções**

* Para usuários que estão cadastrados em mais de uma empresa no fluig Identity, o recurso de troca de contextos foi corrigido para que se comporte de acordo com a regra de negócio:

1. O usuário autenticou-se em uma empresa com senha pessoal → Tenta acessar outra empresa, que não permite o uso da senha pessoal → Deverá informar a senha do Active Directory.
2. O usuário autenticou-se em uma empresa com senha do Active Directory →  Tenta acessar outra empresa → Deverá informar a senha pessoal (se a empresa permitir) ou a senha do Active Directory da empresa que gostaria de acessar.
3. O usuário autenticou-se em uma empresa com senha pessoal → Tenta acessar outra empresa, que permite o uso da senha pessoal → Acesso imediato, sem a necessidade de informar novamente a senha.

Aviso

Para alternar entre contextos no fluig Identity, é obrigatória a utilização do botão de seleção de empresas localizado no canto superior direito das páginas, pois a troca diretamente através da URL informada na barra de endereço do navegador não é mais suportada. Esta mudança se deve a um aprimoramento na segurança da ferramenta, que visa garantir o acesso do usuário apenas ao domínio no qual está autenticado.

Veja um exemplo deste comportamento [nesta FAQ](http://tdn.totvs.com/pages/viewpage.action?pageId=286021491).

* A atribuição de permissões em recursos do Logix através do fluig Identity foi ajustada para que as configurações aplicadas aos *roles* sejam independentes. Dessa forma, as permissões definidas para um *role* específico não serão replicadas em *roles* de outras companhias existentes no Logix.

**master-61**

Disponível em

**Gerenciamento de licenças e credenciais no aplicativo do fluig**

As novas abas Credenciais OAuth 2.0 e Licença disponíveis no aplicativo global Fluig oferecem a parceiros selecionados a oportunidade de gerenciar as chaves de autenticação OAuth e o licenciamento de seus clientes de forma simples e rápida.

Caso você já utilize o aplicativo Fluig em seu contexto no fluig Identity, não se preocupe: nada muda na forma como o fluig controla as licenças da sua aplicação. Esse recurso só é válido para as novas licenças adquiridas junto a parceiros específicos e não terá impacto para clientes que já usufruem da integração.

**master-57**

Disponível em

**Correções**

* O funcionamento da importação de usuários do Active Directory foi ajustado para que este procedimento seja realizado sempre que o serviço do SmartSync for iniciado, tanto pela aplicação (*Start*/*Stop Service*) quanto como serviço do sistema operacional. Com isso não é mais necessário alterar o nome ou sobrenome de um usuário para iniciar sua importação para o fluig Identity, basta reiniciar o serviço. Para aplicar a correção, deve-se instalar o .

**master-55**

Disponível em

**Correções**

* Após o administrador selecionar usuários pendentes para serem aceitos no fluig Identity, uma mensagem será exibida para informar quantos destes usuários estão em [processo de aceite](http://tdn.totvs.com/pages/viewpage.action?pageId=201739710). Enquanto este procedimento estiver sendo executado, os botões "Aceitar" da página serão desabilitados.

* Corrigido o contador de imagens selecionadas ao acionar a opção "Selecionar outras imagens" do recurso de [redefinição de senha por imagem](http://tdn.totvs.com/pages/viewpage.action?pageId=224101578).

**master-52**

Disponível em

**Controle o acesso externo ao seu contexto no fluig Identity**

Para complementar a segurança dos contextos no fluig Identity, está disponível o novo Filtro de Acesso por IPs Externos. Este recurso permite que os administradores definam endereços e/ou faixas de IPs externos confiáveis, liberando o acesso ao contexto apenas a partir destes locais. Todos os demais acessos oriundos de endereços IP não cadastrados pelo administrador serão bloqueados.

Saiba como configurar e habilitar esse recurso acessando a documentação [Filtro de Acesso por IPs Externos](https://tdn.totvs.com/x/2pNvI).

**Gerencie as notificações enviadas pelo recurso de redefinição de senha por imagem**

O recurso de redefinição de senhas por imagem agora permite configurar quando uma notificação será enviada por e-mail caso o usuário falhe ao tentar redefinir a senha. Para saber mais sobre este recurso e configuração, acesse .

**Correções**

* Liberação do método *clone* na API REST v2 do fluig Identity para permitir a clonagem de aplicativos. Os parâmetros necessários para a realizar a clonagem são o companyID (ID da Empresa) e o appID (Código do aplicativo).

**master-49**

Disponível em

**Correções**

* Aumento do tempo disponível para o processo de sincronização de grupos do Active Directory para o fluig Identity através do SmartSync, com o objetivo de evitar a incidência de falhas por *timeout*.

* Remoção dos campos Servidor e Autenticação que eram exibidos na aba Visão Geral de aplicativos que possuíam o provisionamento ativado.

* Correção no posicionamento da *tooltip* exibida ao clicar em aplicativos do tipo Plugin adicionados por usuários comuns e que ainda não foram configurados.

* Funcionamento do botão Cancelar, localizado nas configurações do recurso de segurança por imagens secretas, foi ajustado para que os valores dos campos Número de imagens no cadastro e  Número de imagens na seleção não sejam alterados ao acioná-lo.

* Adaptação do fluig Identity às mudanças no *response* do serviço Zendesk, corrigindo a integração deste aplicativo em ambientes com DesktopSSO.

**master-44**

Disponível em

**Comunicação nas nuvens: novo servidor de e-mails garante segurança e confiabilidade**

A partir desta *release*, as mensagens de e-mail enviadas pelo fluig Identity serão gerenciadas por um novo servidor de e-mails. Essa mudança visa garantir maior agilidade, estabilidade e segurança para os administradores e usuários da plataforma durante a utilização de recursos como o envio de convites e a recuperação de senhas.

**Correções**

* Desabilitado o preenchimento automático configurado pela opção "Lembrar e-mail" na página de cadastro acessada através do e-mail de convite.

* Suporte à criação de *templates* de e-mail com maior tamanho e quantidade de caracteres.

* Ajuste para permitir a alteração dos nomes dos grupos cadastrados no fluig Identity.

* Correção para permitir o acesso ao fluig através do aplicativo fluig Mobile para Android em ambientes integrados ao fluig Identity.

* Atualização das páginas de login personalizadas.

**master-43**

Disponível em

**Destaques**

* Agora a autenticação SAML do fluig Identity é compatível com aplicativos que não exigem assinatura do *Assertion.*Nas configurações do aplicativo adicionamos uma nova opção que você possa definir se o *Assertion* será assinado ou não.

* Os endereços de e-mail listados na página Gerenciar Usuário agora são clicáveis e direcionam o administrador para o perfil do usuário selecionado.

**Correções**

* Ajuste para que os recursos de menu apresentem melhor performance na renderização.

* Inclusão de registros adicionais nos logs da ferramenta para melhor rastreamento de inconsistências no carregamento dos itens de menu.

* Adaptação da página Home do fluig Identity para melhor exibição nos navegadores de dispositivos móveis, quando a opção de "Permitir Auto-inscrição" estiver habilitada na empresa.

* Correção no procedimento de criação de usuários que tenham sido previamente removidos de uma empresa no fluig Identity.

* Preenchimento automático dos campos Nome e Sobrenome de usuários que tiverem sido importados do Active Directory com valor nulo ou perdidos devido a uma inconsistência com o valor *"Autofix"*.

Caso a situação descrita acima ocorra na empresa, o administrador poderá ajustar o nome e o sobrenome através da página de gerenciamento do usuário.

**master-35**

Disponível em

**Correções**

* Ajuste para que o nome da empresa seja exibido dentro do cabeçalho do fluig Identity, mesmo quando possuir muitos caracteres.

* Exibição de uma barra de rolagem na lista de empresas para facilitar o acesso ao botão "Sair" para usuários cadastrados em um grande número de empresas.

* Centralização da caixa que contém os campos de autenticação (E-mail/Senha) exibida na página personalizada de login SAML.

* Correção do recurso "Lembrar E-mail" disponível na tela de autenticação do fluig Identity para que funcione corretamente em todos os navegadores homologados.

* Nova mensagem informativa ao tentar instalar o *plugin* do fluig Identity através do Microsoft Edge. O usuário será alertado de que este navegador ainda não é suportado pelo *plugin*.

## 2016

**master-34**

Disponível em

**Destaques**

* Página de exibição dos grupos aprimorada com paginação para tornar o carregamento e visualização de grandes quantidades de grupos mais simples e ágil.

**Correções**

* Ajuste no campo para inclusão do celular no perfil do usuário para que sejam aceitos números com o 9º dígito em todos os códigos DDD em que esse formato foi implementado. Além disso, o funcionamento do botão de confirmação do número foi corrigido.

* Aplicado melhoria no mecanismo que garante a inclusão de todos os usuários da empresa no grupo *EVERYONE***.**

* Correção no método de validação de token OAuth (*getToken*) para retornar código de erro 401 quando informações de autenticação estiverem incorretas.

* Inclusão do rodapé em todas as páginas do fluig Identity – tanto usuário comum quanto administrador - com os dados da versão do Identity.

**master-32**

Disponível em

**Correções**

* Em ambientes com autenticação via fluig Identity e apenas uma empresa cadastrada no fluig, o aplicativo mobile apresentará a tela de login do fluig Identity para a inclusão das credenciais do usuário. Assim, clientes que utilizam CAS serão direcionados para essa forma de autenticação.

$("b:contains('oculto')").parent().parent().hide();
]]>
