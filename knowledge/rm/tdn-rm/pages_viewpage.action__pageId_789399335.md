---
content_hash: 856d7cfac3947c5e5f929bf17a122e53fe4a98502f3a350bda155c8ff31b5690
fetched_at: '2026-06-29T00:11:39.711579+00:00'
page_id: '789399335'
product: rm
source: tdn-rm
title: Envio de mensagens avançado - utilizando fórmula visual
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=789399335
version: 3
---

O envio de mensagens do TOTVS Educacional para o Meu eduCONNECT pode ser realizado de duas formas: [básica](http://tdn.totvs.com/x/_2scEQ) e avançada.

Nessa documentação será possível encontrar informações sobre como enviar mensagens utilizando Fórmulas Visuais.

Informação importante

Essa opção **avançada** de **envio de mensagens** está **disponível** a partir da release **12.1.19** e traz um potencial enorme para a integração entre o TOTVS Educacional e o Meu eduCONNECT, uma vez que possibilita ao cliente uma série de acionamentos em pontos específicos do sistema de acordo com sua necessidade, seja para customizar um cadastro ou até mesmo um processo do TOTVS Educacional ou até dos Portais para que estes disparem mensagens específicas para usuários do Meu eduCONNECT a partir de alguma ação do usuário.

Para realizar a configuração, primeiramente deve ser realizada a autenticação do eduCONNECT nos parâmetros do sistema conforme citado no item "[02 - Parametrização](http://tdn.totvs.com/x/5WscEQ)", pois a atividade de fórmula visual "Notificação eduCONNECT" irá utilizar estas configurações para o envio da mensagem.

O cadastro da categoria que será utilizada, também deverá ser previamente realizado no TOTVS Educacional conforme citado no item "[03 - Configurações gerais | 03.1 - Cadastro de categorias](http://tdn.totvs.com/x/BWwcEQ)".

Para utilizar a funcionalidade de fórmula visual, deve-se acessar o cadastro de fórmula visual em TOTVS Educacional | Gestão | Fórmula Visual.

Editar o cadastro de fórmula visual (duplo clique sobre a fórmula visual que seja utilizar) ou [criar uma nova fórmula visual](http://tdn.totvs.com/x/gYZ8B) para utilização. Em seguida acessar a aba "Atividades' e depois o agrupador  "Educacional", conforme mostra a figura a seguir:

Feito isso, basta selecionar e arrastar a nova atividade "Notificação eduCONNECT" para a área de "Fluxo de Trabalho Sequencial":

A atividade possui as propriedades divididas nos grupos "01 - Contexto dos parâmetros eduCONNECT", "02 - Configuração da mensagem" e "03 - Dados da mensagem", que devem ser preenchidas conforme a necessidade e parâmetros do cliente.

Dica

Confira a seguir alguns exemplos do potencial que a utilização de fórmula visual para envio de mensagens para o eduCONNECT pode fornecer, mesmo que o gatilho do evento a ser utilizado não esteja dentro do TOTVS Educacional.

**Envio de mensagens para usuários do Meu eduCONNECT quando houver alteração de salário do funcionário:**

****Envio de mensagens para usuários do Meu eduCONNECT quando houver a**lteração da situação do curso do aluno:**

****Envio de mensagens para usuários do Meu eduCONNECT a**pós matricula em disciplina:**

****Envio de mensagens para usuários do Meu eduCONNECT com uma e**nquete após matricula em disciplina:**

****Envio de mensagens para usuários do Meu eduCONNECT quando houver a**lteração no cadastro de usuário:**

**Envio de mensagens para usuários do Meu eduCONNECT com vídeos do YouTube:**

false

Essa funcionalidade está disponível a partir da release 12.1.26 do TOTVS Educacional.

Obs: Na estrutura da mensagem a *tag* do vídeo tem que estar transformada. Isso é, o usuário tem que acessar a estrutura da mensagem e parametrizar a *tag* do vídeo do YouTube.
