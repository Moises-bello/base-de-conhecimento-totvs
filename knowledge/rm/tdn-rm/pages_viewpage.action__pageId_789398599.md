---
content_hash: 6951c9558d8b3b8f5fcfa0f71921ef51bbf5ecba16e29837ab7ef887f8dbb6b6
fetched_at: '2026-06-29T00:11:39.289782+00:00'
page_id: '789398599'
product: rm
source: tdn-rm
title: 02. Parametrização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=789398599
version: 15
---

A parametrização básica do Meu eduCONNECT é realizada a partir dos parâmetros do sistema TOTVS Gestão Educacional.

O primeiro passo para que a parametrização seja concluída com sucesso é a definição de um usuário que será utilizado na parametrização do Meu eduCONNECT e que tenha permissão ao item "Permite autenticar no eduCONNECT nos parâmetros do sistema".

Como foi informado no item [01 - Pré-requisitos](http://tdn.totvs.com/x/sgEXEQ), o Meu eduCONNECT traz consigo uma integração nativa com o TOTVS Educa Mobile e o usuário citado anteriormente é utilizado para validar a conexão entre os dois produtos.

**Observe a seguir, a tela onde é apresentado o item de permissão citado anteriormente:**

**Serviços Globais | Segurança| Perfis | 'Sistema' Educacional | Acesso a Menus | Educacional | eduCONNECT| Permite autenticar no eduCONNECT nos parâmetros do sistema**

A parametrização que possibilita a sincronização do eduCONNECT com o TOTVS Educacional,  está disponível no menu **'Sistema' Educacional |****Configurações | Parâmetros| eduCONNECT**

#### **1/5 - INTEGRAÇÃO DO APLICATIVO MEU eduCONNECT COM O TOTVS EDUCA MOBILE**

**Ativar integração com o eduCONNECT:**ativa a integração entre Meu eduCONNECT, TOTVS Educa Mobile.

**Código da Instituição**: identificador único fornecido pela TOTVS mediante a aquisição do Meu eduCONNECT.

Dica

Para a definição de quantos códigos de instituição serão necessários, podemos pensar na seguinte pergunta: os contextos (filiais e níveis de ensino) são bastante distintos uns dos outros, chegando a ter identidade visual diferente como cores, banners e/ou logotipo? Nesses casos, sugerimos a criação e configuração de contas diferentes (códigos de instituição), para que sejam tratados como se fossem aplicativos diferentes, possibilitando que cada conjunto de coligada, filial e nível de ensino tenha suas configurações\*.

*\*Para mais detalhes sobre como adquirir seu código de instituição e provisionamento de conta, entre em contato com seu A.R..*

**URL de conexão com o eduCONNECT:**é o endereço do servidor responsável por gerenciar os serviços e integração do eduCONNECT com o TOTVS Educacional e TOTVS Educa Mobile. Esta URL é fornecida pela TOTVS mediante a aquisição do Meu eduCONNECT.

**URL de importação das mensagens:**essa Url tem como finalidade permitir fazer realizar a importação dos dados de mensagens do servidor do eduCONNECT para a base TOTVS RM do cliente. Essa Url é fornecida pela TOTVS no memento da criação do Código da Instituição. Para mais informação sobre a o processo de importação, clique [aqui](https://tdn.totvs.com/x/eot9Hg).

**Usuário e senha para autenticação:** nesses campos é necessário informar as credenciais do usuário atribuído ao perfil criado no início dessa seção (que deve ter a permissão ao item "Permite autenticar no eduCONNECT nos parâmetros do sistema" e "Permite acesso ao eduCONNECT"). Esses dados, em conjunto com o "Código da Instituição" constituem uma chave de segurança que garante que apenas a instituição à qual foi destinada aquele código poderá utilizar essa integração. Após informar as credenciais do usuário, é necessário clicar no botão "Autenticar" e aguardar a validação. Caso não ocorra nenhum erro, a mensagem "Token inválido. Favor autenticar novamente" será trocada para "Status: Autenticado!" e será exibida na cor verde.

Atenção

*O usuário utilizado para essa integração **não** pode ser "**Responsável (Pai, Mãe, Resp. Financeiro ou Resp. Acadêmico)**" de outros usuários no sistema, pois terá o seu acesso restrito e não será possível alterar as opções de temas do aplicativo na aba eduCONNECT 3/5 dos parâmetros.*

**URL do TOTVS Educa Mobile**

Atenção

Esta opção de configuração está disponível no Meu eduCONNECT a partir da release 12.1.19.

Durante o processo de aquisição do Meu eduCONNECT, a TOTVS solicita ao cliente algumas informações e dentre elas, a URL do TOTVS Educa Mobile. Essa URL compõe a configuração e identidade do aplicativo Meu eduCONNECT juntamente com o "Código da Instituição" com objetivo de fazer um vínculo único entre o aplicativo e o TOTVS Educa Mobile do cliente.

Com objetivo de dar mais liberdade independência aos clientes no que diz respeito à configuração do aplicativo, foi criada a opção que permite a alteração dessa URL pré-configurada, porém, é pré-requisito para essa alteração que as credenciais de um usuário com permissão de autenticação no TOTVS Educa Mobile sejam informadas.

Dica

Para que a URL possa ser alterada, tanto a nova URL quanto a URL antiga precisam estar ativas e disponíveis.

**Chave para alteração de Url:**Este campo tem como finalidade informar a senha para que seja possível alterar a Url do Educa Mobile para a autenticação do eduCONNECT.

false

A partir da versão: 12.1.28 será possível trocar a URL do TOTVS Educa Mobile.

Para alterar, basta informar a nova Url do Totvs Educa Mobile e informar a senha\*.

> ```
> * A senha é informada pela TOTVS na criação do código da instituição.
> ```

**Gerar QRCode de configuração do eduCONNECT:** este botão só será habilitado com os campos Código da Instituição e URL de conexão com o eduCONNECT preenchidos. O QRCode será gerado com a parametrização definida. Essa funcionalidade pode ser utilizada de várias formas, como por exemplo na divulgação do aplicativo, pois através do Meu eduCONNECT os usuários podem realizar a leitura desse QRCode e configurar automaticamente seu aplicativo com os padrões da instituição, sem a necessidade de digitar nenhuma informação de configuração. Para isso basta que o  usuário do eduCONNECT acione a função QRCode disponível na tela de login do aplicativo. Essa função irá acionar a câmera para  leitura do QRCode disponibilizado pela instituição e automaticamente será carregada toda parametrização de servidor, URL de conexão, tema e login com o Facebook (caso esteja configurado).

**2/5 - CONFIGURANDO O LOGIN COM FACEBOOK E GOOGLE NO TOTVS eduCONNECT**

Nessa etapa pode ser configurado o login no aplicativo Meu eduCONNECT através do Facebook e Google. Para habilitar essa configuração é necessário marcar a opção "Adicionar botão de login com o Facebook no app" e "Adicionar botão de login com o Google no app".

* No campo "Aplicativo do Facebook" deve ser informado o aplicativo do Facebook configurado previamente.
* No campo "Aplicativo do Google" deve ser informado o aplicativo do Google configurado previamente.

 Para informações detalhadas sobre como criar e configurar um aplicativo para login com Facebook no Meu eduCONNECT, clique [aqui](http://tdn.totvs.com/x/ZYb0G) e para mais informações para criar um aplicativo com Google clique [aqui](https://tdn.totvs.com/x/rMsXHw).

**3/5 - PERSONALIZANDO O MEU eduCONNECT**

Configuração da Logomarca (Modo Escuro)

Para garantir a correta exibição da logomarca no **Modo Escuro** do aplicativo, é necessário que o ambiente atenda aos requisitos mínimos de versão e siga as orientações de atualização de imagem descritas abaixo.

### Requisitos Mínimos de Sistema

| **Componente** | **Versão / Patch Necessário** |
| --- | --- |
| **Patches do RM (Release 2506)** | **12.1.2506.267** ou superior |
| **Patches do RM (Release 2510)** | **12.1.2510.187** ou superior |
| **Patches do RM (Release 2602)** | **12.1.2602.111** ou superior |
| **Aplicativo Mobile** | **08.2602.01** ou superior |

### Procedimento Importante de Atualização

Caso a imagem da logomarca tenha sido atualizada nos parâmetros do sistema **antes** do aplicativo estar na versão mínima mencionada acima, será necessário realizar o seguinte ajuste após a atualização do app:

1. Acesse as configurações onde a logomarca foi inserida.
2. **Exclua** a imagem atual.
3. **Insira novamente** o arquivo da logomarca e salve as alterações.

> **Observação:** Este passo é obrigatório para que o aplicativo processe o novo recurso de renderização para o modo escuro.

Nessa etapa as informações como nome do aplicativo, cores e imagens poderão ser personalizadas.

Nos campos de cores a opção de "Cor da fonte e ícones da barra inferior" representa a cor secundária que irá  influenciar na cor dos textos e ícones.

A  opção de "Cor do menu e da barra superior"  representa a cor primária que irá influenciar a cor dos botões e barra superior e a cor de preenchimento dos componentes. configuradas as cores do aplicativo.

Os campos **"Logo da instituição – modo claro"** e **"Logo da instituição – modo escuro"** permitem configurar, respectivamente, as imagens exibidas na tela de login do Meu eduCONNECT para cada tema do sistema.

O usuário poderá aplicar o mesmo tema definido no eduCONNECT no TOTVS Educa Mobile.

Para aplicar o template de cores definidas no eduCONNECT para o Totvs Educa Mobile, basta marcar o parâmetro: "Aplicar cores acima também no Educa Mobile",

As cores serão aplicadas no Menu Lateral, Barra superior, Mensagens de Alerta para o usuário e na seleção de contexto.

                 Menu lateral                            Barra superior                           Mensagens de alerta                    Seleção de Contexto

           

****4/5 - PARAMETRIZAÇÃO PARA ARQUIVOS DE NOTIFICAÇÃO****

O parâmetro: **"Utilizar Banner por contexto"** possibilita direcionar os banners do Meu eduCONNECT para serem exibidos apenas para os usuários que possuem matrícula no contexto em que o banner foi cadastrado.

Esse parâmetro está disponível em: Parâmetros | Configurações | eduCONNECT | 4/5 - Parâmetros do eduCONNECT  para integração com o TOTVS Educacional | Parametrização de banner do no aplicativo

Desta forma, ao marcar o parâmetro nos casos em que utiliza-se o mesmo GUID para dois ou mais contextos diferentes, só será exibido os banners que estejam configurados para o **contexto cujo o usuário logado ou os seus dependentes possuam matrícula** e cujo a situação de matrícula (Educacional |Currículo e Oferta| Situação de matrícula) na disciplina esteja com a opção **"Conta como aluno matriculado na turma (Nível de ensino básico)"** ou **"É uma disciplina em curso (Nível de ensino superior)"** marcadas.

Veja também:

**5/5 - CONFIGURAÇÃO DE FUNCIONALIDADES NO APLICATIVO**

Nesta etapa, será possível parametrizar quais as funcionalidades estarão disponíveis para os usuários no aplicativo, podendo também, alterar os seus respectivos nomes tanto em português quanto em inglês.

Quando o aplicativo está instalado em um dispositivo que esteja em inglês, os textos dos menus serão alterados.

Informação importante

Caso você possua restrições que limitem os acessos aos servidores em sua rede ou você é cliente TOTVS Cloud, atenção às recomendações abaixo:

TOTVS Educa Mobile: O servidor web deve estar público na internet, assim como todo site e com a segurança que é definida pela instituição. Sugerimos a utilização do HTTPS. Caso exista alguma restrição de acesso ao servidor, é necessário liberar as requisições da URL do eduCONNECT (aba eduCONNECT 1).

Servidor de aplicação RM (Host): O servidor onde é executado o serviço de host deve ter acesso às URL's abaixo para conseguir fazer as requisições que a solução necessita:  
• URL do TOTVS Educa Mobile;  
• URL do eduCONNECT (aba eduCONNECT 1).

O parâmetro: Exibir contexto nas funcionalidades do Meu eduCONNECT baseado na conta configurada (Guid)  para definir se a instituição utilizará o filtro por Guid nos contextos do Meu eduCONNECT e do TOTVS Educa Mobile. 

Esse parâmetro está disponível em: Parâmetros | Configurações | eduCONNECT | 3/4 - Parâmetros do eduCONNECT  para integração com o TOTVS Educacional | Contexto da Aplicação

Esse parâmetro tem como objetivo, filtrar de acordo com o Guid logado, exibir apenas o contexto configurado, ou seja, caso essa opção esteja marcada para um determinado Guid, ao entrar nas funcionalidades: Acadêmico (TOTVS Educa Mobile), Notificações, Mensagens e Agenda Infantil; o "Contexto" a ser exibido para usuário, será listado coerente ao Guid/Contexto configurado.

Exemplo: Usuário aluno de faculdade e responsável por alguém de ensino básico: Ao utilizar uma conta (Guid) específica para a faculdade, o contexto a ser apresentado ao usuário (aluno da faculdade e responsável por alguém do ensino básico) será somente o de aluno da faculdade.

Aluno Faculdade: Configurado no GUID-001)  
Aluno Responsável "Ensino Básico": Configurado no GUID-002

Ao logar no App, com o GUID-002, será exibido apenas o Contexto/Guid com o perfil de responsável no contexto Ensino Básico.

IMPORTANTE!!!

A lista de conversação das mensagens pessoais, serão exibidas todas mensagens independente do contexto, pois é uma lista global de conversas ponto a ponto.

Caso o app esteja sendo atualizado a versão antiga para a versão mais nova, os GUIDs serão mantidos de uma versão para outra.
