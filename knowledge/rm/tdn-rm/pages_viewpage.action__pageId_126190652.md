---
content_hash: 300c9ca4557ce6ed744f9ab7566c5b06c92d9b34e889f49f68f3eba60f02ef03
fetched_at: '2026-06-29T00:05:55.134479+00:00'
page_id: '126190652'
product: rm
source: tdn-rm
title: AVISOS AUTOMÁTICOS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=126190652
version: 7
---

**ROTEIRO****PARA****ENVIO****DE****AVISOS****AUTOMÁTICO**

O sistema permite a criação de avisos automáticos para serem enviados aos funcionários, chefes, supervisores ou

terceiros.

Segue as informações necessárias para este processo:

**1º****Passo:**

No cadastro dos usuários do aplicativo, menu Cadastros | Segurança | Usuários | aba Identificação, no campo ‘E-

mail’ deve ser informado o endereço eletrônico do destinatário que receberá a mensagem.

**2º****Passo:**

Parametrização do servidor de e-mails pelo menu Ambiente | Configuração | Parametros Globais | aba Envio de E-mails:

Parâmetros da Coligada Atual:

Informe os dados para os parâmetros que serão utilizados na coligada em uso. Estes dados irão prevalecer sobre

os dados informados nos Parâmetros Default (ao lado).

Servidor SMTP (para envio de e-mails):

Informe o nome do servidor SMTP, isto é, o servidor de correios eletrônicos a ser utilizado na empresa para o

envio dos e-mails nesta coligada.

Exemplo: servidor.empresa.com.br

**Atenção:**

Este campo deve ser preenchido com o nome do servidor de correio eletrônico usado pela empresa (Exchange,

LotusNotes, Linux). O servidor SMTP pode ser interno ou externo.

No caso de servidor interno, consulte o administrador interno da rede para se informar do nome do servidor SMTP.

No caso de servidor externo, o nome do servidor SMTP deve ser informado pelo provedor da empresa.

Exige autenticação do servidor de e-mails:

Se esta opção estiver marcada será exigida do servidor a autenticação dos e-mails, isto é, será necessário que o

servidor valide o usuário e a senha do usuário que está enviando o e-mail.

Usuário:

Informe o nome do usuário que será utilizado para se realizar uma conexão com o servidor SMTP.

Observações:

O usuário que será utilizado não precisa ser necessariamente o usuário de acesso à base de dados, mas sim o

usuário da rede que tem acesso e permissão para realizar o envio de e-mails no servidor de e-mails que estiver

informado no campo Servidor SMTP (para envio de e-mails).

Senha:

Informe a senha do usuário que será utilizado para se realizar uma conexão com o servidor SMTP (campo não

obrigatório).

Número de e-mails:

Informe o número de e-mails que serão enviados de cada vez, quando for disparado automaticamente o envio dos

e-mails. Um número alto indica que o sistema, ao disparar o envio de e-mails, demorará mais tempo realizando a

operação, mas a fila será esvaziada mais rapidamente. Um número baixo indica que o sistema, ao disparar o

envio de e-mails será mais ágil (em vista de um número pequeno de e-mails a enviar), mas a fila será esvaziada

de maneira mais lenta.

Intervalo (minutos):

Informe de quantos em quantos minutos a aplicação irá enviar os e-mails que estão na fila.

Testar parâmetros para envio de e-mail's               :

A função deste botão é verificar se as configurações feitas para envio de e-mail estão funcionando corretamente.

Parâmetros Default

Informe os dados para os parâmetros que serão utilizados por todas as coligadas quando estes não forem

informados nos Parâmetros da Coligada Atual.

Observações:

Os parâmetros são os mesmos para a Coligada Atual.

Se todas as coligadas possuírem o mesmo servidor, basta preencher os campos dos Parâmetros Default. Se

apenas uma coligada possuir um servidor diferente, para esta coligada, preencha apenas os campos dos

Parâmetros da Coligada Atual. Se cada coligada possuir um servidor diferente, preencha para cada coligada os

campos dos Parâmetros da Coligada Atual e não preencha os campos dos Parâmetros Default.

**3º****Passo:**

Outros parâmetros para o Envio de e-mail são encontrados no menu Configurações | Parametrizador | Avisos Automáticos:

Avisos Automáticos

Ativar envio de avisos automáticos:

Selecionando esta opção, o sistema ativará o envio de Avisos automáticos que estão programados no menu

Utilitários | Avisos Automáticos.

Ativa log do aviso automático:

Selecionando esta opção o sistema habilitará o log de execução dos Avisos Automáticos. Este log será criado na

pasta onde se encontra instalado o sistema.

Utilizar e-mail do seguinte cadastro

Funcionário:

Marcando esta opção, o sistema considerará como o endereço eletrônico do funcionário aquele informado em seu

cadastro no menu Cadastros | Funcionários | aba Identificação, no campo e-mail;

Usuário:

Marcando esta opção, o sistema considerará como o endereço eletrônico o do usuário do funcionário aquele

cadastrado em Cadastros | Segurança | Usuários, no campo e-mail.

Intervalo geração dos avisos

Digite o intervalo de tempo (em minutos) em que o sistema irá gerar e enviar os avisos automáticos.

Observação 1:

Para usuários que possuem uma base maior deverão usar um tempo menor, para que assim o sistema envie as

mensagens com maior rapidez.

Observação 2:

Para melhor desempenho, considere na definição do intervalo de tempo de geração dos avisos os parâmetros

estabelecidos em Opções | Globais | aba Envio de e-mails | quadro Parâmetros da Coligada atual .

E-mail do remetente

Digite o endereço eletrônico de quem está enviando a mensagem.

**Observação:**

Se este parâmetro não for definido, avisos de forma de envio por e-mail não serão gerados.

**4º****Passo:**

Verifique se foram cadastrados os chefes e os supervisores para as seções existentes na empresa. O cadastro é

efetuado pelo menu Administração de Pessoal | Chefes  e Sueprvisores | Cadastro de Chefe/Supervisor :

Caso não tenha chefes ou supervisores cadastrados, deverá fazê-lo, pois se desejar enviar os avisos automáticos

a chefes e supervisores o sistema fará a consideração deste cadastro.

**5º****Passo:**

Incluir os avisos automáticos pelo menu Configurações | Avisos Automáticos .

Aba Parâmetros da Programação:

Aviso

Descrição:

Informe a descrição do Aviso automático.

Tipo:

Serão definidos os tipos de avisos conforme constados no campo \*.

\* Tipos de Aviso:

**1****-****Escala****de****ferias**

Será enviado um aviso automático pelo TOTVS Folha de Pagamento toda vez que um (ou mais) funcionários estiverem para tirar férias (início de gozo próximo).

Este aviso tem como finalidade notificar os chefes da devida falta que aquele funcionário possa fazer e possivelmente, providenciar mudanças

estruturais para minimizar o impacto (caso necessário). O número de dias de antecedência que será enviado o aviso é controlado pelo Nro.

Dias Referência.

**2****-****Término****de****Contrato****de****trabalho**

Será enviado um aviso automático pelo TOTVS Folha de Pagamento toda vez que um (ou mais) funcionários estiverem com contratos a vencer (data de término

de contrato próxima). Este aviso tem como finalidade notificar os chefes com antecedência de modo que estes possam se preparar para a

contratação ou demissão do(s) funcionário(s) em questão. O número de dias de antecedência que será enviado o aviso é controlado pelo Nro.

Dias Referência

**3****-****Férias****em****dobro**

O TOTVS Folha de Pagamento enviará um aviso automático sempre que um ou mais funcionários estiverem próximos do vencimento de suas férias em dobro. O aviso será disparado conforme a parametrização do campo "Nro. Dias Ref". A regra de disparo é baseada na data atual do sistema e a data limite de início do gozo das férias.  
Se a data limite de início do gozo das férias estiver dentro do intervalo de dias parametrizados no "Nro. Dias Ref" ou já tiver passado, um e-mail será enviado para notificar os chefes de que eles deverão pagar as férias dobradas ao funcionário, caso ele não tire as férias imediatamente.  
  
**Exemplo:**

* Data atual: 30/07/2024
* Data limite de início do gozo das férias: 30/08/2024
* "Nro. Dias Ref": 31 dias

Neste cenário, um e-mail será enviado informando que o vencimento do limite de início do gozo está próximo, sendo passível de pagamento de férias em dobro. Se o "Nro. Dias Ref" estivesse configurado para 40 dias, o e-mail também seria enviado. No entanto, se estivesse configurado para 29 dias, o e-mail não seria enviado.

**4****-****Alteração****de****Salário**

Será enviad8 um aviso automático pelo TOTVS Folha de Pagamento toda vez que um (ou mais) funcionários tiverem o salário alterado. Este aviso tem como

finalidade notificar os chefes das alterações de salário e avisar aos funcionários o novo salário.

**5****-****Alteração****de****Função**

Será enviado um aviso automático pelo TOTVS Folha de Pagamento toda vez que um (ou mais) funcionários sofrerem alteração na função. Este aviso tem como

finalidade notificar os chefes qualquer alteração da função do funcionário alocado na empresa.

**6****-****Demissão**

Será enviado um aviso automático pelo TOTVS Folha de Pagamento toda vez que um (ou mais) funcionários forem demitidos.

**7****-****Solicitação****alteração****dados****bancários**

Será enviado um aviso automático pelo TOTVS Folha de Pagamento toda vez que um (ou mais) funcionários solicitarem a alteração de dados bancários via

QUIOSQUE ou TOTVS Folha de Pagamento.net.

**8****-****Confirmação****alteração****dados****bancários**

Será enviado um aviso automático pelo TOTVS Folha de Pagamento toda vez que o usuário realizar a aprovação dos Dados em Rotinas|Aprovações de

Alterações Cadastrais ou realizar a liberação de Competência, dependendo assim do Parâmetro "Enviar direto para o cadastro de funcionários"

em opções | parâmetros | rmlabore.net | grupo de acesso ao rmlabore.net | pasta parâmetros do grupo de acesso ao rmlabore.net .

**9****-****Outros**

O tipo de mensagens "Outros" foi criado para permitir que os clientes peçam customizações do comportamento do envio de mensagens,

permitindo à equipe de desenvolvimento uma flexibilidade maior para a implementação destes códigos.

Tipo de Anotação pessoal:

Este campo determina os tipos de anotações pessoais constados no campo.

Observação:

Este campo será habilitado para usuários que optarem pelo tipo de Aviso "Anotação Pessoal"

Tipo de Funcionário (Término de Contrato):

Este campo determina os tipos de funcionários com término de contrato constados no campo.

Observação:

Este campo será habilitado para usuários que optarem pelo tipo de Aviso "Término de Contrato".

Nº dias Referência:

Este parâmetro serve para determinar o intervalo de tempo em dias que uma programação irá gerar uma

mensagem para determinado destinatário tendo como referência à data de ocorrência do evento menos o número

de dias de referência.

**Exemplo:**

Um funcionário vai tirar férias no dia 01/06/2002, se colocarmos o valor "30" no campo dias de referência, será

gerada uma mensagem para o grupo selecionado quando fizer 30 ou menos dias do dia que ele tirará férias, ou

seja, 01/05/02.

Observação:

O sistema só verifica esta data para os Avisos "Escala de Férias" e "Término de contrato".

Informa usuário responsável:

Esta opção permite identificar o código do usuário do TOTVS Folha de Pagamento que disparou o fato gerador do aviso. Dessa

forma, aparecerá no corpo da mensagem do aviso a frase "Usuário responsável pela alteração: XXX", onde XXX é

o código do usuário do TOTVS Folha de Pagamento.

Observação:

A opção "Informa usuário responsável" não estará disponível nas seguintes situações:

a) quando o tipo de aviso for "Escala de Férias", "Término de Contrato" ou "Férias em Dobro", pois o fato gerador

dessas categorias depende de circunstâncias de prazos e não da ação direta de um usuário.

b) quando a forma de montagem for outra diferente da opção "Padrão (agrupamento por funcionário)".

Ativo

Este campo permite habilitar/desabilitar um determinado aviso sem a necessidade de exclusão.

Freqüência de execução

Periodicidade

Marque qual será a periodicidade dos envios dos avisos.

Executar novamente

Informe a quantidade de dias da execução do envio.

Próxima execução:

Este campo serve para indicar qual será a próxima data (calendário) que o aviso será executado.

**Exemplo:**

Periodicidade= diária

Próxima Execução = 25/04/2008

Executar novamente = 1

O aviso será processado diariamente, e a data e próxima execução será alterada para 26/04/2008.

Periodicidade= mensal

Próxima Execução = 25/04/2008

Complemento = 1

O aviso será processado mensalmente, e a data e próxima execução será alterada para 25/05/2008.

Seleção das fórmulas

Código da fórmula para o cabeçalho:

Informe à fórmula que será executada antes dos detalhes de uma mensagem.

Código da fórmula para o detalhe:

Informe a fórmula que será executada para cada um dos funcionários encontrados dentro de um determinado

grupo.

Código da fórmula para o rodapé:

Informe a fórmula que será executada antes de terminar o e-mail

Exemplo para agrupamento de funcionários:

Fórmula para Cabeçalho: CONCAT('Prezado(a) ', TABFUNC('NOME', 'S'))

Fórmula para detalhe: CONCAT('O seu salário foi alterado para:' ,STR(RC,'0000.00'))

Fórmula para rodapé: 'Parabéns!'

Com as fórmulas acima será enviada a seguinte mensagem ao funcionário:

“Prezado(a) CARLOS VICENTINO MORAES

O seu salário foi alterado para 1000.00.

Parabéns!”

Observação:

1) - Normalmente os dizeres das mensagens são diferenciados de acordo com o Agrupamento utilizado, neste

caso deverá ser criado outros Avisos com o mesmo código alterando o Tipo de agrupamento as fórmulas e/ou os

relatórios utilizados.

Opções de envio

Forma de envio

E-Mail:

Marcando esta opção, informe um ou mais endereços eletrônicos para os quais serão enviadas as mensagens

além dos destinatários do agrupamento.

Mensagem na Tela:

Se marcada esta opção, o campo acima mudará o nome para Usuário(s) de terceiro(s). (Separado(s) por ponto e

vírgula). Informe um ou mais usuários para os quais serão enviadas as mensagens além dos usuários do

agrupamento

Forma de montagem

Esta opção irá montar a mensagem a ser enviada para o grupo de destinatários.

Padrão (agrupamento por funcionário):

O sistema enviará a mensagem padrão, cadastrada internamente no aplicativo.

Fórmula:

Os avisos automáticos serão montados de acordo com o conteúdo das fórmulas informadas nos campos, Código

da fórmula para o cabeçalho, Código da fórmula para o detalhe e Código da fórmula para o rodapé.

Gerador de Relatórios:

Os avisos automáticos serão montados de acordo com o relatório previamente criado no Gerador de Relatórios,

sendo que o relatório (menu Relatórios | Gerador) deverá ter campo Tipo do Relatório = Aviso Automático e o Tipo

de Saída = Texto.

Campos do Relatório:

No cadastro do Aviso Automático, selecionando este campo Gerador de Relatórios o sistema habilitará uma nova

pasta, denominada "Forma de montagem – Gerador de Relatórios". Interno do sistema, onde deverão ser

selecionados os filtros do relatório que poderá usar a imagem abaixo como padrão:

Destinatário(s)

Agrupado por

Funcionário:

Quando agrupado por funcionário, os e-mails serão enviados para o(s) Funcionário(s), sendo possível também o

envio de mensagens para o(s) Supervisor, Chefe e Terceiro.

**Exemplo**

"Prezado CARLOS VICENTINO MORAES, o seu salário foi alterado para R$ 1000.00."

Supervisor

Quando agrupado por Supervisor, os e-mails serão enviados para o(s) Supervisore(s) do(s) funcionário(s) de

acordo com o Cadastro da tabela de Cadastros de Chefes e Supervisores, neste agrupamento será possível

enviar a mensagem também para o Chefe.

Chefe

Quando agrupado por chefe, os e-mails serão enviados somente para o(s) Chefe(s) do(s) funcionário(s) de acordo

com o Cadastro da tabela de Cadastros de Chefes e Supervisores , e deve-se definir a quebra por chefe.

Seção

Quando agrupado por seção, os e-mails serão enviados para o(s) Chefe(s) da seção e/ou para terceiros e deve-se

definir a quebra de seção.

Enviar para

Funcionário:

A mensagem será enviada para o funcionário.

Chefe(s):

Marque esta opção para que a mensagem seja enviada também para o chefe do funcionário alem do

agrupamento definido. Esta opção só ficará habilitada quando o agrupamento for por Supervisor/Funcionário.

**Exemplo:**

Agrupamento por funcionário. A mensagem será enviada apenas para o funcionário e se marcar esta opção será

enviada também para o chefe do mesmo.

Supervisor

Marque esta opção para que a mensagem seja enviada também para o supervisor do funcionário observando o

agrupamento definido.

**Exemplo:**

Agrupamento por funcionário. A mensagem será enviada apenas para o funcionário e se marcar esta opção será

enviada também para o supervisor(s) do mesmo.

E-mail(s) de terceiro(s): (Separados por ponto e vírgula)

Informe um ou mais endereços eletrônicos para os quais serão enviadas as mensagens além dos destinatários do

agrupamento.

Quebra por Chefe

Quando o agrupamento for por chefe, deve-se definir a quebra de Chefe do(s) Funcionário(s) de acordo com a

tabela Cadastros de Chefes e Supervisores.

Quebra por Seção

Quando o agrupamento for por Seção, deve-se definir a quebra de Seção que deseja ser enviado o e-mail.

**6º****Passo:**

Envio do Aviso

Após parametrizado o envio do aviso, conforme o passo acima, o mesmo será enviado automaticamente ao

processar o tipo de aviso desejado (demissão, alteração salarial, alteração de função...) ou poderá ser enviado

acessando o cadastro do Aviso, menu Utilitários | Avisos Automáticos, e selecionando o ícone Enviar Aviso.

Após o envio do aviso por e-mail, o histórico poderá ser visualizado no menu Utilitários | Histórico de E-mails

enviados.
