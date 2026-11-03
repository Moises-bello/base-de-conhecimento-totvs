---
article_id: 4407450836887
category: RH - Cadastros
content_hash: df0ba3a39de05bcd5f4353d804080491867efd19cd421b6cb0aa281070fb1d03
fetched_at: '2026-06-28T22:44:52.702259+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON -  Como utilizar o cadastro de evento do ponto eletrônico
type: support-article
updated_at: '2025-12-29T12:25:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407450836887-RH-Linha-Protheus-PON-Como-utilizar-o-cadastro-de-evento-do-ponto-eletr%C3%B4nico
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35178207070743) Tempo aproximado para leitura: 00:02:00 min**  
  
**Dúvida**  
Como utilizar o cadastro de evento do ponto eletrônico?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
**01. VISÃO GERAL**  
Este **cadastro** é **utilizado** para **apurar os eventos ocorridos no Ponto Eletrônico**, como hora extra, falta, atraso, atrasos meio período, saída antecipada, acréscimo noturno, entre outros.  
  
Com base nos **Identificadores do Ponto** deverão ser cadastrados os eventos e vinculados aos identificadores. Veja mais sobre os identificadores: [RH - Linha Protheus - PON - Principais Apontamentos e Identificadores de Ponto do Módulo de Ponto Eletrônico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015532691-RH-Linha-Protheus-PON-Principais-Apontamentos-e-Identificadores-de-Ponto-do-M%C3%B3dulo-de-Ponto-Eletr%C3%B4nico)  
O caminho da rotina no módulo 16-SIGAPON: **Atualizações > Cadastro do Ponto > Eventos**  
  
Para os eventos de horas extras, como não possuem identificadores, são associados aos tipos de horas extras, conforme documentação: [RH - Linha Protheus - PON - Regras importantes para o cadastro dos Tipos de Horas Extras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060489314-RH-Linha-Protheus-PON-Regras-importantes-para-o-cadastro-dos-Tipos-de-Horas-Extras)  
  
Sobre os eventos podem ser utilizados os seguintes controles:  
• **Identificadores de Ponto** - Para apurar os resultados dos apontamentos das marcações;  
• **Exportação do evento para Folha de Pagamento**, através do código da verba;  
• **Cálculo do Desconto do DSR** - Descanso Semanal Remunerado, onde o número de horas atribuídas ao evento será utilizado para este cálculo;  
• **Cálculo do DSR** - Desconto Semanal Remunerado, onde o número de horas atribuídas ao evento será utilizado para este cálculo;  
• **Controle de Acumulado do Banco de Horas**, calculando o percentual de horas a ser creditado em folha de pagamento.  
  
Os **eventos podem ser classificados** como:  
• **Provento**: Tudo o que for recebido pelo funcionário, como por exemplo faltas ou atrasos abonados, salários, benefícios, etc.  
• **Desconto**: Tudo o que for descontado do funcionário, como por exemplo faltas e atrasos não autorizados.  
• **Base**: Tudo o que não for pagamento e não for desconto para o funcionário.  
  
**02. PRINCIPAIS CAMPOS**  
**I. Pasta Geral:**  
  
**Código pra Folha (P9\_CODFOL)**  
Neste campo deve ser informado o código que será utilizado para definir quais eventos **irão ou não para a Folha de Pagamento ou para a Exportação**. Caso este campo esteja preenchido com um código válido, e independente do evento ser autorizado ou não autorizado, será enviado para a Folha de Pagamento, quando houver Integração com o ambiente Gestão de Pessoal.  
  
**Contador (P9\_EVECONT)**  
Informe neste campo o código do evento que conterá a quantidade de ocorrências do evento corrente.  
Por exemplo:  
Se o evento corrente refere-se a **Faltas**, é possível informar um **evento contador** para apurar o número de dias em que o trabalhador ausentou-se.  
Um evento contador é um evento como outro qualquer, o que significa dizer que ele poderá ser enviado para o banco de horas ou para a folha de pagamento. Desse modo, é importante ser criterioso na configuração de um evento contador para não gerar resultados incoerentes.  
Uma vez informado o evento contador num evento o calculo mensal do ponto vai assumir as configurações dele, não sendo necessário informar nada nos campos código pra folha ou banco de horas do evento que recebe o evento de contador.  
  
**Importante:**  
Os eventos contadores sempre serão informados para a folha de pagamento em quantidade de ocorrências diárias: ou seja, o **"Tipo"** da verba será **"Dias"** e o campo "**Horas Lanc."** conterá a quantidade de ocorrências do evento.  
  
Veja a documentação sobre: [RH - Linha Protheus - PON - Como utilizar a funcionalidade de contador de Faltas no Ponto Eletrônico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015852071-RH-Linha-Protheus-PON-Como-utilizar-a-funcionalidade-de-contador-de-Faltas-no-Ponto-Eletr%C3%B4nico)  
  
**Identificador de Ponto (P9\_IDPON)**  
Os resultados apurados pela rotina de apontamento estão ligados a códigos internos que não são gravados nos arquivos do ambiente de Ponto Eletrônico. A gravação é feita no código do evento criado pelo usuário. Sendo assim, este campo deve armazenar o **código de Identificador do Ponto** (código interno) relacionado ao evento criado pelo usuário.  
  
**Desconto de DSR (P9\_DESCDSR)**  
Este campo permite identificar com **"S"** ou **"N"** se a ocorrência do evento em questão será considerada para desconto de DSR - Descanso Semanal Remunerado. Quando este campo for mantido em branco, o evento não será considerado. Normalmente utilizado como **“Sim”** nos eventos de Faltas e Atrasos.  
  
**Divergência (P9\_DIVERGE)**  
Selecione neste campo a opção **"Sim"** para classificar o evento em cadastro como uma divergência, uma vez marcado **“Sim”** o apontamento do evento aparecerá sinalizado na rotina **“Lançamentos > Integrados”** facilitando a manutenção, pois o usuário não precisa entrar em todos os dias para observar se tem alguma divergência para ajustar.  
  
**II. Pasta Banco de Horas:**  
  
**Percentual (P9\_BHPERC)**  
Neste campo deve ser definido o percentual de **valorização** do evento e deve ser utilizado para guardar horas valorizadas. Exemplo: Para uma hora extra 60%, deve ser informado 160.00.  
  
**Agrupam. B. H. (P9\_BHAGRU)**  
Define se os eventos serão **agrupados**, ou seja, se o resultado de todos os proventos ou descontos serão incluídos no Banco de Horas em forma de grupos e não evento a evento. É necessário respeitar os campos "Horas De/Horas Até".  
  
**Tp. Apuração (P9\_BHVAL)**  
Este campo define o tipo de apuração para Banco de Horas, que pode ser: **Total - Entra para o Banco de Horas quando as horas estiverem exatamente dentro dos campos "Horas De/Horas Até". Parcial - Será acumulado do Banco de Horas apenas as horas que ficarem fora do intervalo.**  
  
**Perc. B.H. e Perc. Folha Pgto. (P9\_PBH e P9\_PFOL)**  
Usuários que trabalham com hora extra definida por percentual devem estipular nestes campos **qual será o percentual que será enviado para o Banco de Horas e qual será enviado para a Folha de Pagamento**, respectivamente. Este campo também pode ser usado para quando a empresa deseja fazer um regime de apuração misto, onde parte das horas apontadas vão para o banco, parte para a folha de pagamento. Neste caso, o evento, além de estar com **“Sim”** para banco deve estar também com **“Código para a folha”** informado, desta forma de acordo com o preenchimento do campo.  
  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[Leitura e Apontamento de Marcações](https://tdn.totvs.com/x/yTezJQ)   
[RH - Linha Protheus - PON - Como cadastrar os eventos para Folha de Pagamento ou Banco de Horas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013459532-RH-Linha-Protheus-PON-Como-cadastrar-os-eventos-para-Folha-de-Pagamento-ou-Banco-de-Horas)  
[RH - Linha Protheus - PON - Como gerar eventos Autorizados ou Não Autorizados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406010444567-RH-Linha-Protheus-PON-Como-gerar-eventos-Autorizados-ou-N%C3%A3o-Autorizados)  
[RH - Linha Protheus - PON - Separação do Acréscimo Noturno do Evento de Adicional Noturno](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010333062-RH-Linha-Protheus-PON-Separa%C3%A7%C3%A3o-do-Acr%C3%A9scimo-Noturno-do-Evento-de-Adicional-Noturno)
