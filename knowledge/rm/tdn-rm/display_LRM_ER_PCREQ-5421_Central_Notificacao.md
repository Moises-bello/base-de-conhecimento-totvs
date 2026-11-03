---
content_hash: 159913a28dd2f878ce29e871ad67d60675fb60ce9d94d4ceb9da15fa10e59dd4
fetched_at: '2026-06-29T00:06:07.209986+00:00'
page_id: '201735920'
product: rm
source: tdn-rm
title: ER_PCREQ-5421_Central_Notificacao
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-5421_Central_Notificacao
version: 51
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Educacional | **Módulo** | Educacional |
| **Segmento Executor** | Educacional | | |
| **Projeto1** | R\_EDU\_EDU011 | **IRM1** | PCREQ-5420 |
| **Requisito1** | PCREQ-5421 | **Subtarefa1** | PDR\_EDU\_EDU011-471 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.9 | **Réplica** | Não |
| **País** | (X ) Brasil  (  ) Argentina  (  ) México  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colômbia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 Possibilitar que sejam realizados posts em comunidades e notificações aos usuários no Fluig através de funcionalidades do TOTVS Educacional.

### Definição da Regra de Negócio

A central de notificação será composta da junção de duas funcionalidades já implementadas no TOTVS Educacional e a adição de outras duas, são elas: 

* Cadastro de Mensagens de Notificação
* Processo de Mala Direta
* Processo de Envio de Notificação e/ou Post nas Comunidades (nova funcionalidade)
* Processo de Envio de Mensagens de Notificações Temporais (nova funcionalidade)

***Cadastro de Mensagens de Notificação***

**Escopo original:**  
Funcionalidade que centraliza o cadastro dos modelos para os textos que são enviados por e-mail. Estes textos estão vinculados a determinados objetivos, como por exemplo, "Confirmar reservas de recurso" ou "Confirmar reservas de instalação" entre outros.

**Escopo após a implementação:**

* Continuará possuindo todas as funcionalidades do escopo original
* Alteração da nomenclatura de "Cadastro de mensagens para envio por e-mail" para "Cadastro de mensagens de notificação"
* Criação de quatro novos novos campos na tabela de mensagens (SMENSAGENSNOTIFICACAO):  
  + Campo "ENVIAREMAIL": para determinar se o modelo do texto cadastrado deverá ser encaminhado via e-mail  
    Valores possíveis: "S" - Sim ou "N" - Não, como padrão este campo será criado com o valor "S"  
    Os destinatários da mensagem devem possuir e-mail cadastrado
  + Campo "ENVIARNOTIFICACAOFLUIG": para determinar se o modelo do texto cadastrado deverá ser encaminhado via notificação para um usuário no Fluig   
    Valores possíveis: "S" - Sim ou "N" -Não, como padrão este campo será criado com o valor "N"  
    Se não houver integração com o FLUIG este campo deverá ficar inativo  
    Os destinatários da mensagem devem possuir um usuário cadastrado no Fluig
  + Campo "TEXTOMENSAGEMNOTIFICACAOSIMPLES": para determinar o modelo de texto a ser enviado no caso de uma notificação do Fluig, este só poderá conter texto simples (sem formatação e sem imagem).  
    O campo "TEXTOMENSAGEMNOTIFICACAO" já existente continua possibilitando o cadastro de mensagens apenas de texto ou HTML e será utilizado quando a mensagem for encaminhada por e-mail.
  + Campo "TIPOEXECUCAO": para determinar o tipo das mensagens, onde "0" - Fixas (são mensagens enviadas no momento em que alguma alteração ou processo é executado no sistema) e "1" - Temporais (são enviadas através de um processo especifico para este fim).   
    Todas as mensagens já incluídas serão classificadas como Fixas. (Este campo não pode ser alterado pelo usuário)
* A mensagem poderá ser parametrizada de tal forma que seja encaminha por e-mail e por notificação ao mesmo tempo, ou se o usuário preferir apenas para um dos mecanismos.  Neste primeiro momento apenas o TOTVS Educacional disponibilizará esta característica, ou seja, os sistemas TOTVS Gestão Bibliotecária e TOTVS Avaliação e Pesquisa continuam possibilitando apenas o envio de e-mail.
* Novos tipos de mensagem serão disponibilizados para o TOTVS Educacional: Inadimplência, pendência de matrícula, frequência, liberação de etapa de falta, liberação de etapa de nota e ocorrências.

-1
incomplete


1
incomplete
Inadimplência (Tipo da mensagem: temporal)

* + Disponibilizar as seguintes tags:  [DEMONSTRATIVODEBITO], [RA] e [NOMEALUNO]
  + A regra para definição dos valores seguirá o mesmo conceito da utilizada no quadro de avisos do Portal

2
incomplete
Pendência de matrícula (Tipo da mensagem: temporal)

* + Disponibilizar as seguintes tags:  [DEMONSTRATIVODEBITO], [DOCUMENTOSPENDETES], [BIBLIOPENDENCIA], [RA], [NOMEALUNO], [NOMECURSO], [NOMEHABILITACAO], [CODPERLET]
  + A regra para definição dos valores de débito seguirá o mesmo conceito da utilizada no quadro de avisos do Portal

3
incomplete
Frequência Diária (Tipo da mensagem: temporal)

* + Disponibilizar as seguintes tags: [DEMONSTRATIVOFREQUENCIA], [PERCLIMITEFREQUENCIA],[RA] e [NOMEALUNO]
  + A regra para calcular o percentual de frequência do aluno será a mesma utilizada para gerar o aviso de frequência do portal do aluno. No entanto, só será enviada a mensagem para os alunos que estiverem excedido o limite de faltas ou estiver próximos do limite de faltas (80% do limite de faltas)
  + O parâmetro "% Limite de Faltas" que atualmente se encontra em "RM Portal -> RM Portal - Gerais -> RM Portal - Geral 2/6" será transferido para a parametrização de secretária
  + Para utilização dessa mensagem, é necessário que a instituição esteja fazendo uso de um dos dois parâmetros referentes ao Limite de faltas disponíveis em "Secretaria -> Parâmetros gerais - Geral 4/7", que são: "Utilizar a etapa final da turma/disciplina para consultar a frequência mínima" e "% Limite de Faltas".

4
incomplete
Ocorrências (Tipo da mensagem: fixa)

* + Para o contexto de ensino básico esta mensagem deve ser encaminhada para o aluno, responsável acadêmico e os pais do aluno.
  + Para o contexto de ensino superior esta mensagem deve ser encaminhada apenas para o aluno
  + Apenas ocorrências que possuírem o campo "Visível no Portal" marcado no cadastro do tipo de ocorrência devem disparar o envio.
  + Disponibilizar as seguintes tags: [RA], [NOMEALUNO], [DESCRICAOOCORRENCIA], [DTOCORRENCIA], [GRUPOOCORRENCIA] , [NOMEGRUPOOCORRENCIA], [TIPOOCORRENCIA] e [NOMETIPOOCORRENCIA]

5
incomplete
Liberação de etapa de Falta e Liberação de etapa de Nota (Tipo das mensagens: fixa)

* Quando o parâmetro "Permitir a visualização das notas e faltas da etapa somente após a liberação do professor" estiver desmarcado, ao salvar a digitação de nota ou falta o sistema pode disparar uma notificação se os parâmetros relacionados ao envio da notificação e/ou e-mail estiverem marcados no cadastro da mensagem de notificação.
* Quando o parâmetro "Permitir a visualização das notas e faltas da etapa somente após a liberação do professor" estiver marcado a notificação e/ou e-mail só serão disparados após a liberação da etapa pelo professor. Mesmo neste cenário os parâmetros de envio definidos no cadastro da mensagem de notificação são verificados.

* Os tipos de mensagens já existentes no TOTVS Educacional deverão passar a possibilitar o envio de notificação para os usuários do Fluig. Nos casos em que a mensagem estiver parametrizada para os dois tipos de saída a mensagem deverá ser encaminhada com os dois formatos.
* Esta funcionalidade agora será agrupada em um novo item de menu, denominado "**Atividades Acadêmicas ->****Central de Notificação -> Mensagens de Notificação"** e sairá do local **"Currículo e Oferta -> Auxiliares -> Mensagens de Notificação"**
* Os parâmetros do TOTVS Educacional que determinavam o envio do e-mail com a mensagem de notificação serão excluídos, desta forma o que permitirá este controle serão os novos campos "Enviar e-mail" e "Enviar notificação para o Fluig" disponíveis no cadastro das mensagens de notificações.

***Processo de Mala direta***

* Esta funcionalidade agora será agrupada em um novo item de menu, denominado "**Atividades Acadêmicas ->****Central de Notificação -> Mala Direta"** e sairá do local **"Atividades Acadêmicas -> Assistentes -> Mala Direta"**

***Processo de envio de Notificação e/ou Post nas comunidades***

* Este processo só estará disponível se houver integração com o Fluig. A integração será entendida como ativa quando o parâmetro código de comunicação estiver preenchido.
* O processo será semelhante ao da mala direta, no entanto, deve possibilitar o disparo de posts em comunidades e notificações para usuários do Fluig. Este processo disponibilizará as seguintes abas:

* + Primeira aba: conterá as definições relacionadas ao mecanismo de geração das informações.  
    Campo: "Executar como"
    1. Post nas comunidades do Fluig (esta opção só estará disponível se o sistema estiver integrado com a parte Social do Fluig, ou seja, o TOTVS Educacional deve estar configurado para utilizar a funcionalidade "Acadêmia Social")
    2. Notificação no Fluig
  + Segunda aba:   
    1. Se o campo executar for: "Post nas comunidades" o usuário deverá definir a lista das comunidades alvo. Mecanismos para definição das comunidades:
       1. Definição de SQL:
          1. A sentença deverá conter obrigatoriamente o campo "ALIASCOMUNIDADE".
          2. Se a sentença retornar comunidades inativas na execução do processo essas deverão ser ignoradas
       2. Definição via consulta as comunidades:   
          1. Definir a entidade alvo do post (curso, habilitação, turma, turma/disciplina, subturma e atividade ofertada)
          2. Selecionar as comunidades que devem receber o post
          3. Apenas comunidades ativas devem ser listadas
    2. Se o campo executar for: "Notificação no Fluig":
       1. Definição do SQL responsável por buscar a lista dos destinatários das notificações.
       2. A sentença SQL deverá conter obrigatoriamente os campos "CODUSUARIO" e "EMAIL".
  + Terceira aba:
    1. Definição da mensagem que se quer enviar, as tags disponíveis serão todos os campos disponíveis no SQL criado pelo cliente ou na consulta exibida na seleção das comunidades.
    2. Restringir a mensagem a utilização de texto simples, não possibilitando formatação do texto e/ou inclusão de imagens
  + Ao executar o processo o mesmo terá como resultado final a criação do post nas comunidades ou o envio das notificações para os usuários do Fluig.

***Processo de envio de mensagens de notificações temporais***

Este processo respeitará as seguintes regras:

* Definição do público alvo:
  1. Utilizando os seguintes seletores para definição do público alvo:
     + Período Letivo
     + Código do Curso
     + Código da Habilitação
     + Código da Turma
  2. Utilizando uma sentença SQL
     + Deve possuir obrigatoriamente os campos CODCOLIGADA, RA, CODUSUARIO e EMAIL para todas as notificações temporais e para a notificação de pendência de matrícula ainda deverá conter os campos "IDHABILITACAOFILIAL", "CODCURSO", "NOMECURSO", "CODHABILITACAO" e "NOMEHABILITACAO".
* Seleção de um ou mais tipos de notificação temporal que devem ser executadas
* Se a mensagem de notificação temporal estiver parametrizada para envio por e-mail todos destinatários que não possuírem um e-mail definido serão ignorados.
* Se a mensagem de notificação temporal estiver parametrizada para notificação no Fluig:
  + Parâmetros Educacional: deve possuir a definição da conta de comunicação
  + Todos destinatários que não estiverem cadastrados no Fluig serão ignorados.
* O log final do processo deve detalhar as mensagens enviadas com sucesso e as que por algum motivo não puderam ser enviadas.

***Requisito restritivos***

* Não será implementada ou alterada nenhuma funcionalidade do Portal Educacional e EducaMobile.

***Pontos de atenção***

* A integração com as notificações do Fluig poderá requerer implementações na LIB para chamada da API do Fluig, como também a necessidade de evolução da própria API.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Mensagens de Notificação | Alteração | Currículo e Oferta -> Auxiliares -> Mensagens de notificação | - |
| Mala Direta | Alteração | Atividades Acadêmicas -> Assistentes -> Mala Direta | - |
| Processo de envio de mensagens de notificações temporais | Inclusão |  | - |
| Processo de envio de notificações e/ou post nas comunidades | Inclusão |  |  |

***Tabelas Utilizadas***

* SMENSAGENSNOTIFICACAO

## Dicionário de Dados

|  |  |
| --- | --- |
| **Campo** | ENVIAREMAIL |
| **Tipo** | VARCHAR(1) |
| **Tamanho** | 1 |
| **Valor Inicial** | S |
| **Mandatório** | Sim (X ) Não (  ) |
| **Descrição** | Mensagem de notificação será enviada por e-mail |
| **Título** | Mensagem de notificação será enviada por e-mail |
| **Picture** |  |
| **Help de Campo** |  |

|  |  |
| --- | --- |
| **Campo** | ENVIARNOTIFICACAOFLUIG |
| **Tipo** | VARCHAR(1) |
| **Tamanho** | 1 |
| **Valor Inicial** | N |
| **Mandatório** | Sim (X ) Não (  ) |
| **Descrição** | Mensagem de notificação será enviada por notificação no Fluig |
| **Título** | Mensagem de notificação será enviada por notificação no Fluig |
| **Picture** |  |
| **Help de Campo** |  |

|  |  |
| --- | --- |
| **Campo** | TEXTOMENSAGEMNOTIFICACAOSIMPLES |
| **Tipo** | TEXT |
| **Tamanho** |  |
| **Valor Inicial** |  |
| **Mandatório** | Sim ( ) Não ( X ) |
| **Descrição** | Descrição da mensagem a ser enviado via de notificação para o Fluig |
| **Título** | Descrição da mensagem a ser enviado via de notificação para o Fluig |
| **Picture** |  |
| **Help de Campo** |  |

|  |  |
| --- | --- |
| **Campo** | TIPOEXECUCAO |
| **Tipo** | SMALLINT |
| **Tamanho** |  |
| **Valor Inicial** | 0 |
| **Mandatório** | Sim (X ) Não (  ) |
| **Descrição** | Tipo da execução das mensagens 0 para Fixo (são mensagens enviadas no momento em que alguma alteração é realizada no sistema) e 1 para Temporais (são enviadas através de um processo especifico para este fim). |
| **Título** | Tipo da execução das mensagens 0 para Fixo (são mensagens enviadas no momento em que alguma alteração é realizada no sistema) e 1 para Temporais (são enviadas através de um processo especifico para este fim). |
| **Picture** |  |
| **Help de Campo** |  |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
