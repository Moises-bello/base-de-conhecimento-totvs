---
content_hash: 99e027c7ca3c4a1ef4281052b521f2144f64ee72392ca1914fc65d1b4b844ed7
fetched_at: '2026-06-29T00:08:45.350319+00:00'
page_id: '311625925'
product: rm
source: tdn-rm
title: DT Login com o facebook no eduCONNECT
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Login+com+o+facebook+no+eduCONNECT
version: 1
---

# LOGIN COM O FACEBOOK NO eduCONNECT

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Gestão Educacional |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Login | Login no Facebook com no eduConnect |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | N/A | N/A | |  |  | |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [PORTALMOBILE01-913](http://jiraproducao.totvs.com.br/browse/PORTALMOBILE01-913) |
| **País(es):** | BRA |
| **Banco(s) de Dados:** | SQL e Oracle |
| **Tabelas Utilizadas:** | NA |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

O Facebook para desenvolvedores permite medir, entender e otimizar as interações das pessoas. Inicialmente o eduCONNECT usará o perfil público, lista de amigos e endereço de e-mail caso o aluno permita para que seja utilizando em futuras implementações para ajudar na comunicação e adição de novos recursos na plataforma .

Para realizar a configuração do acesso único ao eduCONNECT via Facebook, serão necessárias as seguintes ações abaixo:

**1º-** Acesse o website aos desenvolvedores do Facebook ([http://developers.facebook.com](http://developers.facebook.com/)).

Atenção: será necessário que a instituição tenha um cadastro válido na plataforma do Facebook;

**2º-** Acesse o menu “Meus Aplicativos” em seguida o item “Adicionar um novo aplicativo”;

**3º-**Crie um novo aplicativo Facebook, informando o “Nome de exibição” (Nome do aplicativo) e um “E-mail de contato” com o responsável pelo aplicativo. Para efeitos de explicação poderemos usar para os campos os valores “Portal do Aluno Login Facebook”;

**4º-**  Ao criar o aplicativo, será exibido todos os serviços que o Facebook disponibiliza para acesso externo via aplicativo. Em nosso exemplo iremos escolher “Login do Facebook” e em seguida clique em “Começar”.

**5º-** Será exibido as configurações do login do Facebook. Nesta etapa, deve ser realizado as configurações de OAuth do cliente conforme imagem:

**6º-**Clique no menu lateral na opção “Configurações”. Nessa seção, é possível definir configurações adicionais como Logo da empresa, URL da política de privacidade, URL de Termos de Serviço e etc (que são opcionais para o funcionamento do serviço desejado, mas recomendável que a instituição faça seu preenchimento).

**7º-** Uma vez definida todas as configurações necessárias para funcionamento do aplicativo de Login via Facebook, precisaremos de alguns dados para fazermos a ligação do aplicativo com o sistema RM. Para isso, acesse o menu “Painel”, onde estão as informações necessárias para fazer essa integração. Anote os dados destacados conforme a imagem abaixo;

**8º-** Acesse o RM, em seguida vá na aba “Gestão”, localize o grupo “Comunicação” e em seguida clique no menu “Aplicativos Externos”. Caso o mesmo não esteja disponível, será necessário aplicar permissão para o usuário nas configurações de perfis de acesso do sistema de Serviços Globais;

**9º-** Crie um novo registro na visão de aplicativos externos. Neste registro deverão ser incluídas todas as informações destacadas no passo 7. Atenção, no campo “Provedor do Aplicativo” deveremos selecionar o valor “1 - Facebook”.

**10º-**Ao cadastrar todas as configurações no aplicativo como também no sistema RM, deveremos ativar a exibição do botão, acessando **Configurações |Parâmetros|EduCONNECT|eduCONNECT 2/3.**

Nesta etapa, basta marcar "Adicionar botão de login com o Facebook do app" e informar o aplicativo do Facebook criado no passo anterior.

**11º-** Por último, será necessário publicar o aplicativo Facebook para habilitar seu funcionamento se tornar público. Acesse o menu “Revisão do Aplicativo”, e ative “sim” para o item “Tornar [NOME DO APLICATIVO] público?”.
