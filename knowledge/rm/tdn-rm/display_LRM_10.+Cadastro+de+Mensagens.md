---
content_hash: 0c07be7f8147ff5d5daef971eac5f9e1b23ebfc25ff434461957afb694c0e1d7
fetched_at: '2026-06-29T00:11:39.694413+00:00'
page_id: '789399100'
product: rm
source: tdn-rm
title: 10. Cadastro de Mensagens
type: documentation
url: https://tdn.totvs.com/display/LRM/10.+Cadastro+de+Mensagens
version: 27
---

O cadastro de mensagens para o eduCONNECT, tem como objetivo ter um local único para a parametrização do texto para o envio de notificações para os alunos, pais, responsáveis financeiros e acadêmicos, professores e coordenadores.

O Principal objetivo do cadastro/envio das mensagens aumentar o meio de comunicação direta entre instituição e seu público mais efetiva e centralizada.

Para parametrizar a mensagem é necessário realizar a [configuração do eduCONNECT](http://tdn.totvs.com/x/5WscEQ).

Para efetuar o cadastro da mensagem, é necessário informar a [Categoria](https://tdn.totvs.com/display/LRM/eduflow03.2+-+Cadastro+de+categorias), o texto da chamada do Push, o texto da chamada para a *Timeline*e qual a funcionalidade no Educa  Mobile que o usuário será redirecionando ao clicar na visualização da notificação.

O Usuário terá a opção de parametrizar o tipo de formatação para o envio da mensagem, nos formatos HTML e Texto.

Para efetuar o cadastro das mensagens, acesse a opção de menu **Educacional | Atividades Acadêmicas | Central de Comunicações | Mensagens**

Para cadastrar uma nova mensagem, devemos informar os principais campos do formulário:

1. **Objetivo**: *Qual é o [objetivo](https://tdn.totvs.com/x/sPxbGQ) da notificação a ser enviada.*
2. **Assunto da mensagem:** *Qual o assunto será enviado ao destinatário da notificação por e-mail.*
3. **Público-alvo**: *Para quem será destinada a notificação, tais como:*
   * Enviar para Coordenadores
   * Enviar para Professores
   * Enviar para Pais
   * Enviar para Alunos
   * Enviar para Responsável Acadêmico
   * Enviar para Responsável Financeiro do Aluno *(Cadastro do Aluno | Aba Responsáveis | Responsável financeiro)*
   * Enviar para Responsável Financeiro do Lançamento *(Contrato do Aluno | Anexo Parcela | Aba Lançamentos / Boletos da parcela | Responsável financeiro)*

false

O Público-alvo "**Enviar para Responsável Financeiro do Lançamento**" está disponível a partir da release **12.1.34** do TOTVS Educacional.

Esse parâmetro permite aos clientes enviar a notificação (comunicados e/ou cobranças) diretamente ao responsável do lançamento gerado (com situação "Em aberto" ou "Baixado parcialmente" e data de vencimento menor que a data atual - lançamento atrasado), principalmente para os objetivos de pendência financeira ("Pendências de matrícula (Financeira, Documentos, Biblioteca)", "Pendências financeiras do aluno" e "Boleto próximo ao vencimento").

## ♣ Enviar Arquivos nas mensagens de Notificação.

false

Essa funcionalidade está disponível a partir da release 12.1.26 do TOTVS Educacional / TOTVS Educa Mobile e na versão 08.26.0 no App eduCONNECT.

No Cadastro da mensagem e/ou no processo de Agendamento, será possível anexar arquivos nas mensagens de Notificação. Pode ser anexado um ou mais arquivos dos tipos: imagem, vídeo ou documento.

Os tipos de extensões, tamanho e local de armazenamento, devem ser parametrizado em: **Educacional | Configurações | Parâmetros | eduCONNECT | eduCONNECT 5/5**

false

Atenção ao definir o tamanho dos arquivos, pois pode comprometer a performance no envio da mensagem de notificação e o download pelo Aplicativo Meu eduCONNECT.

* **Cadastro da Mensagem**: A opção para inserir aquivos no cadastro da mensagem, estará disponível apenas para o objetivo: "Enviar mensagens eventuais para via e-mail, Fluig ou eduCONNECT"

Primeiramente é necessário que o usuário cadastre a estrutura da mensagem; onde após clicar em salvar, será habilitado a opção: **Anexo | Arquivos anexos do eduCONNECT.**

Ao clicar na opção: Arquivos anexos do eduCONNECT, será habilitado uma *Tab*, para que sejam inseridos os arquivos.

Após inserir os aquivos, basta clicar no botão 'OK'.

false

Não terá limitação da quantidade de arquivos inseridos na mensagem, porém, pode comprometer a performance do processo de envio da mensagem de notificação.

* **Processo envio/agendamento da mensagem**: No processo de envio/agendamento, a opção para inserir arquivos, estará disponível para todos os objetivos, isso é, os usuários poderão adicionar arquivos para os demais objetivos apenas no Processo de envio/agendamento da mensagem.

No processo de envio/agendamento, o usuário poderá Adicionar ou Remover os arquivos.

Ao final do processo, será exibido um *log* contendo a quantidade de arquivos enviado na mensagem de notificação.

No App, ao acessar a Mensagem de notificação, será exibido ao final da mensagem o item "Anexos", onde ao clicar, será exibido todos os anexos inseridos na mensagem.

Para baixar os documentos, clicar na linha referente ao arquivo.

Caso o anexo enviado possua caracteres especiais no nome, ao abrir ou salvar o anexo, os caracteres são removidos para garantir a integridade do arquivo pois a versão 26.2 do IOS apresenta algumas inconsistências para tratamento de caracteres especiais.   
Para evitar estas inconsistências o tratamento dos caracteres especiais serão feitos para todas as versões do Android e IOS.

false

Se o usuário excluir a mensagem de notificação,  os arquivos contidos no conteúdo da mesma (caso o usuário tenha efetuado o download) os arquivos serão removidos.

# HTML

Para a parametrização da mensagem em HTML, o usuário contará com a formatação de *Tags* existentes em cada categoria da mensagem, links, alinhamento, listas, parágrafo, cores. Não será possível alterar o tipo de fonte, onde por default, a fonte padrão para utilizada para o texto será Nunito Sans, a mesma fonte utilizada no *App* Meu eduCONNECT.

As mensagens parametrizadas seguem o limite máximo de caracteres no texto formatado (já com as TAG's HTML) será de 4000 caracteres. Será apresentado uma mensagem para o usuário, caso extrapole a quantidade máxima tanto na parametrização do texto ou no processo de envio de mensagens.

As mensagens parametrizadas seguem o limite máximo de caracteres no texto formatado (contando com as TAG's HTML) de 4000 caracteres. Será apresentado uma mensagem para ao usuário caso extrapole a quantidade máxima tanto na parametrização do texto como no processo de envio de mensagens.

A formatação  do texto no formato HTML, possui um limite que caracteres para não comprometer a permanece das mensagens de notificação recebidas no aplicativo 'Meu eduCONNECT'.

false

Uma vez o registro salvo com a formatação em HTML, não será possível alterar. Caso o usuário queria alterar o tipo de formatação, deverá excluir a mensagem e cria-la novamente com a formatação desejada.

**1-** Cadastro da mensagem

## ♣ Inserir vídeos do YouTube no cadastro das mensagens de notificação.

false

Essa funcionalidade está disponível a partir da release 12.1.26 do TOTVS Educacional e na versão 08.26.0 no App Meu eduCONNECT.

Para adicionar o vídeo, basta clicar no botão: Captura de vídeos do Youtube, onde será habilitado a visão abaixo.Para os textos no formato **HTML**, no conteúdo das Mensagens de notificações, será possível adicionar vídeos do youtube através do botão:

Copiar a URL do endereço do link do vídeo desejado e colar no campo: "Informe a URL do vídeo no YouTube".

Em seguida o sistema irá identificar o código do vídeo e irá gerar a *Tag* do vídeo parametrizado.

Em seguida, clicar no botão "Adicionar", o sistema irá inserir a *Tag* do vídeo conforme o print abaixo.

 Parametrização da mensagem

 Acesso a mensagem de Notificação acessando o vídeo do YouTube

Além de inserir os vídeos do Youtube na mensagem de Notificação, o usuário poderá inserir a *Tag*gerada na fórmula visual. Para mais informações, clique [aqui](https://tdn.totvs.com/x/UbmcEw).

false

Quando a mensagem não tiver imagem associada, será exibida uma imagem do tipo post-it na timeline, conforme abaixo:

Quando a mensagem não tiver imagem associada, mas, se existir uma tag de vídeo do youtube, a timeline exibirá o primeiro vídeo do youtube na listagem de mensagens da timeline.

### 

Para os dispositivos iOS, os mesmos deverão estar atualizados a partir da versão 12.4.1 ou superior.

Ao vincular o vídeo que possui direitos autorais, o detentor desse vídeo pode bloquear a exibição do mesmo no aplicativo Meu eduCONNECT.  
Com isso, foi criado um link abaixo de cada vídeo, para que seja possível visualizar através da plataforma do Youtube caso não seja possível visualizar o mesmo dentro do aplicativo.

## ♣ Copiar IPTE do boleto no cadastro das mensagens de notificação.

Quando a mensagem a ser enviada tiver como objetivo "Boleto próximo ao vencimento", será habilitada a opção da tag "[IPTE]", conforme abaixo:

Se a mensagem contiver essa tag '[IPTE]', a mesma será substituída pelo IPTE do boleto próximo ao vencimento.

Quando o usuário receber a mensagem na situação acima, será habilitado o botão inferior com a opção de cópia de IPTE conforme abaixo:

Ao clicar nesse botão "Copiar", será mostrada para o usuário uma mensagem de que o mesmo foi copiado para a área de transferência:

## ♣ Redirecionar para a tela de pagamento, com opções de cartão de crédito ou PIX, a partir do link nas mensagens de notificação

Na mensagem com o objetivo "Boleto próximo ao vencimento", também estão disponíveis as tags "[PAGTOCARTAO]" e "[PAGTOPIX]", que fazem o redirecionamento para a tela de pagamento, conforme mostrado abaixo:

Se a mensagem contiver a tag '[PAGTOCARTAO]', a mesma será substituída por um link, que ao ser pressionado, redirecionará para a tela de [Pagamento com Cartão](https://tdn.totvs.com/pages/viewpage.action?pageId=875734596). 

Se a mensagem contiver a tag '[PAGTOPIX]', a mesma será substituída por um link, que ao ser pressionado, redirecionará para a tela de [Pagamento com PIX](https://tdn.totvs.com/display/LRM/eduFlow+11.4+-+Pagamento+com+PIX).

Saiba mais

O campo ***"Funcionalidade do EducaMobile"*** serve para definir qual o atalho será exibido na mensagem enviada e que permitirá ao usuário do eduCONNECT possa abrir a funcionalidade indicada que é disponibilizada nos menus acadêmicos do EducaMobile.

Estão disponível para seleção as funcionalidades: *Agenda, Aulas, Avisos, Avaliações, Disciplinas, Financeiro, Histórico, Horários, Notas/Faltas, Ocorrências e Solicitações*.

O atalho para a funcionalidade estará disponível no canto esquerdo inferior da mensagem aberta. Uma vez que ícone seja clicado, será aberta a tela relacionada a funcionalidade vinculada a mensagem, que no caso abaixo é a **Agenda**:

  

Na mesma mensagem, também, é possível adicionar o conteúdo ao calendário do smartphone, através do botão com o ícone ***"Evento"***. Esse é recurso utiliza o aplicativo nativo de calendário do smartphone, que no caso do *Android* é a ***Agenda*** e do *iOS* é o ***Calendário***.

Essa é uma integração com o aplicativo nativo de calendário do smartphone e é necessário que o mesmo esteja instalado e configurado para seu uso.

# Texto

A parametrização do Texto, o usuário contará com a formatação simples (seguindo a mesma estrutura de parametrização nas verões inferiores a 12.12.24).

O usuário contará com a formatação de *Tags* existentes em cada categoria da mensagem.

As mensagens parametrizadas seguem o limite máximo de caracteres no texto formatado (já com as TAG's HTML) será de 4000 caracteres. Será apresentado uma mensagem para o usuário, caso extrapole a quantidade máxima tanto na parametrização do texto ou no processo de envio de mensagens.

Na parametrização do texto, o usuário tem a opção de utilizar HTML, caso tenha necessidade em utilizar um HTML, uma alternativa é utilizar a opção de texto sem formatação, adicionando a tag:

<body> TEXTO A SER ENVIADO </body>, com as marcação HTML desejada.

## Cadastro das mensagens

false

Para o cadastro da mensagem, seguir os passos

* Selecionar o objetivo da mensagem;
* Informar o Assunto da mensagem (Esse campo será o assunto do email após o envio para o destinatário;
* Selecionar o público Alvo;

false11Email

* Marcar o parâmetro: Ativar envio por email;
* Selecionar o tipo de envio HTML e/ou Texto;
* Inserir o texto e em seguida clicar no botão: Salvar.
2eduCONNECT

* Marcar o parâmetro: Ativar envio de mensagens para o eduCONNECT;
* Selecionar o tipo de envio HTML e/ou Texto;
* Informar a Categoria;
* Informar o Assunto;
* Informar o texto da chamada para o push
* Informar o texto para a chamada da Timeline;
* Selecionar a funcionalidade do Educa Mobile;
* Clicar no botão: Editar mensagem do eduCONNECT;
  + Neste momento, o usuário será redirecionado para a tela de edição de texto, informar o texto e em seguida, clicar no botão Salvar.

# Parametrização das mensagens do Tipo "Enquete".

false

Se o tipo da mensagem for "Enquete", não será possível a parametrização da mensagem HTML, o sistema irá configurar automaticamente o tipo da mensagem como:Texto.

As mensagem do tipo enquete, são mensagens utilizadas para realizar uma votação (escolha) de uma determinada opção.

A estrutura da mensagem é aplicada apenas para o Tipo: **Texto**.

Para estruturar a mensagem, o usuário deve:

1) Informar o objetivo da mensagem;

2) Informar o Assunto da mensagem;

3) Informar a categoria;

4) Informar o texto da chamada para o Push;

5) Informar o texto da chamada para a Timeline;

6) Informar o texto da mensagem;

7) Selecionar a aba: "Opções da enquete".

Em seguida, marcar o checkBox: "Enviar como Enquete"

Essa tela é exclusiva para que seja informado as opções de enquete, que deverão ser separados por ponto e vírgula conforme a opção abaixo.

Em seguida, clicar no botão: "Salvar".

false

Após clicar em salvar, o usuário não terá a opção para editar as opções da enquete, apenas o texto da mensagem.

## Exclusão das mensagens

Para que a mensagem seja excluída, a mesma poderá ser excluída clicando no botão de exclusão no detalhamento da mensagem.

Após clicar no botão de exclusão, será exibido um diálogo de confirmação para conclusão do processo ou cancelamento.
