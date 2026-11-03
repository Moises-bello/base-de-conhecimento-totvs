---
content_hash: e330d7cfee26f2dbfdb1222b60c3b6cf8b9c147b1346d9cea8322884a7e571b4
fetched_at: '2026-06-28T21:35:25.277856+00:00'
page_id: '275120222'
product: fluig
source: tdn-fluig
title: Cadastro de Dados Adicionais - Chaves
type: documentation
url: https://tdn.totvs.com/display/fluig/Cadastro+de+Dados+Adicionais+-+Chaves
version: 9
---

# Índice

4true.\*ndicenone

# Objetivo

---

O objetivo deste guia é apresentar em uma única página as chaves padrões e as que poderão ser configuradas ou cadastradas nos Dados Adicionais em uma Empresa do TOTVS Fluig Plataforma. Esta página contempla apenas as principais chaves usadas para configuração, personalização e integração dos cards. Chaves relaciona as integrações com outros produtos e experiências de uso, devem ser tratadas diretamente com as equipes de atendimento (framework) responsáveis.

# Chaves

---

| Chave | Valor | Objetivo |
| --- | --- | --- |
| **dirDefault** | <Diretório do volume> | Diretório onde fica salvo a pasta de Volume da plataforma. |
| **defaultTheme** | themeecmdefault | Tema que a plataforma está utilizando. |
| **dirUpload** | <Diretórios de upload no Volume> | Diretório onde está salvo a pasta de upload da plataforma. Os arquivos são salvos temporariamente até a finalização do upload, para posteriormente serem transferidos para a pasta public. |
| **dirUploadConnect** | <Diretórios de upload do fluig Connect no Volume> | Diretório onde está salvo a pasta de upload do fluig Connect. Os arquivos carregados através do fluig Connect são salvos temporariamente neste local até a finalização do upload, para posteriormente serem transferidos para a pasta public. |
| **dirCustom** | <Diretórios de Custom no Volume> | Pasta onde ficam salvos os templates de customização de formulários. |
|  | true ou false | Habilita (true) e desabilita (false) o visualizador antigo da plataforma. Restrito a poucas extensões de arquivos. |
|  | [<](http://api.accusoft.com.br)IP ou URL de acesso> | Visualizador de documentos padrão da plataforma.  (URL de Acesso: <https://api.accusoft.com.br>). |
| **social.accsses.control.default.group** | DefaultGroup-1 | Grupo padrão onde são incluídos os usuários sem grupo definido no momento do cadastro. |
|  | <Seu código de projeto retornado pelo suporte> | Integra o fluig Analytics com a GoodData. |
| **[analytics.gd](http://analytics.gd)** | <E-mail que recebeu o convite do suporte> | Integra o fluig Analytics com a GoodData. |
| **[analytics.gd](http://analytics.gd)** | <Senha cadastrada após o convite> | Integra o fluig Analytics com a GoodData. |
| **[analytics.gd](http://analytics.gd)** | true ou false | Integra o fluig Analytics com a GoodData. |
| **chat.enabled** | true ou false | Habilita (true) e desabilita (false) o chat da plataforma. |
|  | <Título desejado para as guias> | Personaliza o título das guias de navegação (abas) da plataforma. |
|  | PROCESS:  Se você deseja que a tela inicial seja a inicialização de processos.  SOCIAL: Se você deseja que a tela inicial seja a timeline.  DOCUMENT: Se você deseja que a tela inicial seja a navegação de documentos.  TASKS: Se você deseja que a tela inicial seja a central de tarefas.  COMMUNITY:ALIAS\_DA\_COMUNIDADE: Se você deseja que a tela inicial seja uma comunidade, o parâmetro ALIAS\_DA\_COMUNIDADE deve ser preenchido e válido para direcionar para comunidade correta. PAGE:IDENTIFICADOR\_UNICO: Se você deseja que a tela inicial seja uma página, o parâmetro IDENTIFICADOR\_UNICO deve ser preenchido e válido para direcionar para página correta. | Personaliza a tela inicial do fluig Mobile. |
|  | true ou false | Habilitar/desabilita atualização automática da Timeline. |
|  | <Inserir a informação recuperada no campo App key> | Habilitar uma notificação Push utilizando a solução da Urban Airship. |
