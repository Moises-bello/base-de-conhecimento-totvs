---
content_hash: 6d33619a76e533fcda33fdd5a4a469c07ef1ee5f856af0b8815c0e0a904cf845
fetched_at: '2026-06-29T00:10:39.062086+00:00'
page_id: '545646594'
product: rm
source: tdn-rm
title: RM - 05 Webinar Apresentação Reinf
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=545646594
version: 10
---

Foi realizado nos dias 30 e 31/03/2020 o Webinar de apresentação da nova opção de transmissão da EFD-Reinf através Backoffice da linha RM. O Evento contou com a participação de muitas empresas e foi um sucesso.

Abaixo estão as principais perguntas realizadas pelos clientes durante o Evento.

## Clique [aqui](https://www.youtube.com/watch?v=t43fylk42wg) para acessar o vídeo.

## É possível verificar quais filiais foi enviado o R-1000?

O R1000 é enviado para a Filial selecionada no contexto. Contudo, conforme regras da EFD-Reinf, o mesmo pode ser transmitido somente para Filial Matriz ou Filiais SCP.

## Como conferir valores se não foi colocado campo de valores?

Junto ao Patch são disponibilizadas consultas SQL que funcionam como um relatório anexo ao Evento. Para maiores informações consulte nossa documentação [https://tdn.TOTVS.com/pages/viewpage.action?pageId=525811211](https://tdn.totvs.com/pages/viewpage.action?pageId=525811211)

## O RM está agrupando o Evento por Data? e não pelo período todo? 1 a 30 do mês.

Cada Evento tem sua regra própria de agrupamento que é definida pelo manual da EFD-Reinf. Em nosso documentação é possível identificar qual a regra de acordo com o tipo do Evento. [https://tdn.TOTVS.com/pages/viewpage.action?pageId=506387475](https://tdn.totvs.com/pages/viewpage.action?pageId=506387475)

## Como ficarão as retificações?Temos clientes que retificam  12 meses para trás. Os lançamentos fiscais estão no RM. Como eu faria pra enviar um registro de retificação?  o XML já é gerado com o tipo ALTERAÇÃO automaticamente?

Os Eventos transmitidos por outro aplicativo devem ser retificados no aplicativo que foram transmitidos. Contudo, no manual da Reinf é destacado que todas as transmissões devem ocorrer até o 15º do mês subsequente, neste caso deve ser verificado junto à área fiscal qual o procedimento a se tomar.

## Se o Evento tiver sido transmitido pelo TAF, como eu faço para retificar pelo RM? Temos alguma forma de gerar o lançamento fiscal com o tipo ALTERAÇÃO/RETIFICAÇÃO?

Neste caso a retificação deve ser transmitida pelo próprio TAF.

## Tem alguma divisão por filial , no evento periódico ?

não, conforme consta no manual da EFD-Reinf, existirá apenas um período de Eventos por Filial Matriz e os eventos de todas as demais filiais serão transmitidos dentro deste mesmo período. Contudo cada filial terá o seu próprio evento e o código da filial de origem pode ser visualizado através da Aba Origem do Evento disponível em cada Evento gerado.

## Como ficam os protocolos que ficaram no TAF ?

Os dados dos Eventos que estão no TAF permanecem no TAF e não serão importados no RM.

## Esse envio já faz de todas as filiais?

Sim, ao gerar os Eventos através da Filial Matriz os Eventos das demais filiais também são gerados juntos, exceto Filiais SCP que neste caso deve ter o processo gerado especificamente para elas.

## Se o cliente encerrar o período de apuração e enviar o fechamento da Reinf e chegar uma NF sem INSS não é possível inserir nesse mesmo movimento?

Se o cliente Encerrar o Período da Reinf e o Período de Apuração, ao incluir uma nova nota que não afeta a Reinf será necessário reabrir somente o período de apuração.

## E sobre migrar os protocolos? Será necessário?

não, mas os dados presentes no TAF devem ser preservados pelo período fiscal vigente (no caso 5 anos)

## O sistema não permite gerar eventos periódicos enquanto todas as filiais não estiverem com seu período de apuração encerrado

não, os Eventos podem ser gerados com o período de Apuração Aberto, porém o recomendado é que sejam gerados após a virada do mês para evitar retrabalho de retificações.

## Pra fazer uma reabertura, hoje pelo TAF eu consigo reabrir um período da Reinf, por exemplo  01/2020, sem precisar reabrir meus períodos 02/2020 e 03/2020. No RM funciona dessa forma também?

Sim, não foi implementado nenhuma trava para impedir esta reabertura. Contudo, deve-se observar os possíveis impactos nos períodos subsequentes e ajustar quando houver necessidade.

## Para prospect, onde será feita a migração de protocolos de outros ERPs?

não será realizada a migração de dados de outros aplicativos. A empresa deverá encerrar as transmissões nos demais aplicativos e iniciar um novo período no backoffice.

## No TAF a gente informava os dados da empresa (ERP) responsável pelo envio. Informávamos o nome da TOTVS, telefone e responsável. E agora onde vamos informar isso no RM? não me lembro disso no RM.

não é necessário, estas informações serão adicionadas automaticamente pelo processo de geração de Eventos com os dados da TOTVS.

## Dentro do TOTVS Fiscal (RM Liber), na tela dos eventos Reinf que são gerados automaticamente, poderemos editar alguma informação nós mesmos, antes do envio para Receita?

não, a tela de Evento da Reinf Exibe o XML que foi gerado com base nos cadastros de origem (Lançamento Fiscal, Movimento etc.). Neste caso o cadastro de Origem deve ser editado e então o Evento deve ser excluído e gerado novamente.

## A nova versão 12.1.27, onde a transmissão dos eventos R-2060 é realizada diretamente pelo TOTVS Gestão Fiscal (RM Liber), como farei para que o sistema gere a informação das devoluções de vendas no campo de exclusão de receita para dedução da base do CPRB?

## Faço esta pergunta por que atualmente estamos integrando com o TAF, e dentro do TAF, de forma manual, estamos adicionando a informação das devoluções de vendas no campo que reduz a base do imposto (R-2060).

Esta informação deve pode ser consultada na documentação especifica de cada tipo de Evento [Eventos Periódicos (Reinf) - Linha RM - TDN](https://tdn.totvs.com/pages/viewpage.action?pageId=506387451)

## Configuração do TSS para quem é Cloud, posso utilizar o mesmo caminho da configuração do TAF?

Esta informação deve ser verificada diretamente com a equipe de Cloud

## Qual será a justificativa para finalizar o R1000 no TAF? Já que não houve alteração na filial.  A receita pode questionar, pois os dados da software house não mudaram

O R1000 não precisa ser transmitido somente quando houver alteração de dados. Neste caso ele está sendo transmitido devido a mudança de aplicativo

## Para quem já está trabalhando com o TAF, como fica?

não muda nada, a Reinf transmitida pelo TAF ainda continuará funcionando normalmente.

## não tem como conferir as informações geradas antes do envio?

Tem sim, após gerar o Eventos os dados de origem assim como o xml do Evento já ficam disponíveis para conferência.

## Preciso informar meu R-1000 novamente?

Ao iniciar as transmissões da Reinf no RM será necessário encerrar as transmissões em outros aplicativos e iniciar um novo R1000 no RM

## Consigo reenviar apenas uma Nota Fiscal quando houver inconsistência?

Sim, basta selecionar o Evento referente a esta nota e executar o processo de transmissão

## Como eu consigo ver o que tem dentro de cada evento?

Acessando o anexo de origem ou o relatório da consulta de SQL.

## Consigo fazer algum evento manual por exemplo R-2060 não uso apuração do liber fazemos manual no TAF

não consegue gerar Eventos manualmente, mas cada Evento é gerado a partir de uma origem e é possível cadastrar a origem manualmente. No caso do R-2060 basta digitar as informações no período de Apuração.

## Estes campos são somente para filial ou para matriz também?  Fazendo esse processo dentro do sistema não será mais necessário usar o TAF  para integração?

Os Eventos são gerado para a matriz com os dados de todas as filiais conforme definido pela Reinf. Para os clientes que optarem por transmitir a Reinf pelo backoffice não será necessário a utilização do TAF para estas transmissões.

## Clientes em Cloud já podem usar essa funcionalidade? o URL será o mesmo da NF-e?

Podem sim. A Url do TSS deve ser verificada junto a equipe do Cloud.

## Como consigo verificar o que eu transmiti de R-1000? Somente no XMl nos anexos do cadastro? --> Me refiro aos dados enviados.

não, você pode verificar no cadastro de origem, no caso do R-1000 ele é gerado com base nos dados da Filial. Em nossa documentação é possível relacionar cada campo da Reinf com o campo do cadastro

## Eu posso excluir o evento se não tiver transmitido?

Sim, mas somente os eventos que estiverem com Status “não Transmitido”, “Inconsistente” ou “Rejeitado”.

## Antes de realizarmos a transmissão conseguimos conferir se todas as notas foram para os respectivos registros?

Sim, quando os Eventos estiverem com Status “não Transmitido” todos os relatórios/Anexos funcionarão corretamente para conferência dos dados.

## Como corrigir um evento rejeitado e como gerar novamente somente este ao ser corrigido?

Neste caso, basta realizar a correção no cadastro de origem, Excluir o Evento com Status de Rejeitado e gerá-lo novamente

## A transmissão da Reinf RM pelo TAF vai ser desconsiderada?

não, permanece no TAF normalmente.

## O pedido de exclusão pode ser feita em qualquer evento?

não, conforme as regras da EFD-Reinf, somente nos Eventos Periódicos Autorizados.

## Terá algum relatório sobre totalizador dos eventos , ou impostos?

Junto ao Patch são disponibilizadas consultas SQL que funcionam como um relatório anexo ao Evento. Para maiores informações consulte nossa documentação [Consulta SQL para conferência dos valores gerados na Reinf - Linha RM - TDN](https://tdn.totvs.com/pages/viewpage.action?pageId=525811211)

## Se uma nota foi enviada pelo REINF, usuário consegue fazer manutenção?

Sim, os cadastros de origem não ficam travados, porém o usuário deve ficar atento à necessidade de Atualizar o Evento na Reinf

## Se tiver notas novas, o processo de reabertura e envio da nova nota é o mesmo?

Sim, basta reabrir o período da Reinf e gerar os Eventos novos.

## Na exclusão de um evento não é necessário informar o ID da nota a ser excluída?.

não, basta selecionar o Evento que será Excluído.

## O envio e será um R-5011 por filial?

Por Matriz ou SCP.

## É possível manter uma coligada pelo TAF e as demais migrar para o envio direto pelo RM?

Sim.

## Quando tratar-se de filiais diferentes a transmissão se dará filial por filial e o consolidado será apresentado na matriz?

O Evento R-5011 estará somente na Matriz ou SCP, mas os Eventos R-20xx anexo ao R-5011, são de todas as filiais e agrupados conforme regra da Reinf.

## Vocês estarão demonstrando a apuração do Imposto? Tipo temos R-2050 como será feita a apuração?

não, isso pode ser consultado na documentação específica do R-2050. [Layout dos Eventos Periódicos - Linha RM - TDN](https://tdn.totvs.com/pages/viewpage.action?pageId=506387475)

## Quem já está entregando normalmente pelo TAF vai precisar enviar o R1000 novamente?

Sim. É necessário Encerrar o R-1000 no TAF e iniciar um novo no RM.

## como o sistema vai somar a receita bruta para o evento ?

Isso pode ser verificado na regra de cada Evento [Layout dos Eventos Periódicos - Linha RM - TDN](https://tdn.totvs.com/pages/viewpage.action?pageId=506387475).

## Existe a necessidade de configurar algum parâmetro de certificado digital ou configuração com o TSS?

Sim, no TOTVS Gestão Fiscal é necessário configurar a URL do TSS, Versão da Reinf, ambiente de transmissão e o certificado digital. [Parâmetros de Integração Reinf (TSS) - Linha RM - TDN](https://tdn.totvs.com/pages/viewpage.action?pageId=517126127)

## Como faço para ter acesso a base de teste da receita?

não tem como, é necessário excluir o ambiente de teste e iniciar um novo.

## Tenho TAF no smart - não mais vou precisar, mas os dados que estão salvos lá. Como farei?

Os dados do TAF devem ser preservado pelo período fiscal legal, no caso 5 anos.

## Como eu encerro um período?

Basta selecionar o período (R-5011) e transmitir o Evento R-2099 para o período em questão. [R-2099 Fechamento dos Eventos Periódicos - Linha RM - TDN](https://tdn.totvs.com/pages/viewpage.action?pageId=521640172)

## Necessitará de uma cópia da base de dados do tss para realizar a homologação?

Sempre que for montado um ambiente de teste, a base do TSS também precisa ser de teste, porém não é necessário ser um backup da base oficial.

## No ambiente para geração dos eventos ele será conforme a emissão ou a competência?

Será respeitada a regra da EFD Reinf para cada Evento. [Layout dos Eventos Periódicos - Linha RM - TDN](https://tdn.totvs.com/pages/viewpage.action?pageId=506387475)

## A partir de que versão está disponível esse novo sistema de entrega do REINF?

12.1.27

## Os protocolo da Reinf são gerados em PDF?

Os dados dos Eventos podem ser impressos, mas não disponibilizamos nenhum relatório padrão com tal finalidade

## O Reinf centraliza as informações da folha?

não, os registros da folha ainda são transmitidos pelo e-Social.

## Fiquei sabendo que o TAF não seria mais usado, mas ainda deve ser instalado para que seja feita a transmissão mesmo que em Background. Como isso vai funcionar?

Para a Reinf, o TAF não precisa ser instalado em Background. É necessário apenas o TSS.

## Para realizar a retificação, basta solicitar a geração do evento novamente?

Isso, primeiro deve ser excluído o Evento incorreto e em seguida gerado um novo Evento com os dados Atualizados.

## Como vai funcionar as retificações de períodos que enviamos utilizando o TAF?

Os dados transmitidos no TAF não são incorporados ao RM, neste caso a retificação deve ser realizada no TAF.

## Fiz encerramento do mês janeiro e em março recebeu NF de janeiro, foi lançada com competência março e emissão janeiro, conseguirei retificar janeiro?

Normalmente. Basta reabrir o período e gerar os devidos Eventos.

## Quantos clientes estão utilizando esta funcionalidade?

A cada dia novos clientes solicitam informações para aderirem a nova funcionalidade. Contudo, antes da liberação oficial este processo foi utilizado em clientes estratégicos a fim de zelar pela qualidade.

## Em caso de alteração de dados da filial, como por exemplo, informações do contador. Qual o procedimento para alterar as informações no R1000?

Neste caso encerra o R-1000 no período anterior e inicia-se um novo RM com os dados atualizado.

## Existe alguma rotina ou orientação para que eu posso começar o envio via RM e não mais no TAF? Ou é somente começar a gerar e transmitir por essa nova rotina?

É necessário encerrar o R-1000 no período anterior no TAF e em seguida iniciar as transmissões do novo período no RM.

## Como recuperar os dados enviados pelo TAF no modelo antigo e colocar no TOTVS Gestão Fiscal?

## As informações que antes era feita pelo TAF manterá no RM? Caso não irá vim, para o RM é possível fazer uma cópia de segurança no TAF.

Os dados não serão importados no RM. Seria o caso de fazer um backup do ambiente do TAF e manter para futuras consultas.

## Vários clientes já tem o evento R1000 transmitido e autorizado. Para iniciarmos a transmissão aqui pelo Liber, obrigatoriamente será necessário retransmitir o R1000 ?

Sim, pois no RM iniciará um novo ambiente que afetará somente os novos Eventos.

## Ainda teremos que fazer a instalação/atualização dos pacotes do TAF. Pelo que foi dito não teria mais necessidade, mas parece que sim.

Para fins de Reinf, considerando os novos Eventos que serão transmitidos pelo RM o TAF não será utilizado não sendo necessário atualizar o ambiente.

Será necessário alguma customização do sistema?

Somente se a funcionalidade padrão não atender alguma especificidade da empresa.

## Qual o processo deve ser feito passo a passo para adotar essa nova forma de envio?

Os passos estão disponíveis em nossa documentação [EFD-Reinf RM - Linha RM - TDN](https://tdn.totvs.com/display/public/LRM/EFD-REINF+RM) e [EFD Reinf - Transmissão via RM](https://tdn.totvs.com/pages/releaseview.action?pageId=527392889)

## Eu posso continuar com as 2 formas de transmissão pelo RM ou pelo TAF ou só uma?.

Para mantermos a integridade dos dados as transmissões de um mesmo período devem ocorrer em apenas um dos aplicativos.

## Em que momento é definido o ambiente? Homologação ou Produção

Através dos parâmetros do Módulo Fiscal  [Parâmetros de Integração Reinf (TSS) - Linha RM - TDN](https://tdn.totvs.com/pages/viewpage.action?pageId=517126127)

## Sobre o envio do R-1000. E quem estava fazendo pela Tela do e-CAC, tenho que enviar o R1000, também ? As últimas que enviei foi tudo pelo e-CAC

Sim.

## Existe a possibilidade de liberação de script para utilizar na versão 12.1.26?

Já está disponível a partir da 12.1.27.

## Eu consigo gerar a partir de março já pelo RM Backoffice ou ainda vou ter que enviar a Reinf de março pelo TAF

Consegue sim, a implementação já está disponível a partir da versão 12.1.27, basta instalar o último patch disponível no portal

## Nós tem que manter o TAF ? Se migrar para o Backoffice RM ?

Somente para consulta dos dados já transmitidos.

## Se eu não transmite nada de março ainda, pelo TAF, posso enviar 03/2020 pelo RM?

Sim.

## Comenta por favor, sobre a situação do cliente que encerrou o TAF, precisar retificar um evento que foi enviado no TAF. como proceder?

A retificação deve ser feita pelo TAF, o procedimento seria reabrir o período R-5011 e transmitir a retificação. De acordo com a RFB o ambiente está preparado para retificar um período anterior sem impactar no período atual.

## O TAF Client será desativado a partir de quando?

não será desativado. Estamos disponibilizando uma nova opção para os clientes que não desejam utilizar o TAF.

## No caso do evento 2060, como o RM busca as informações. No caso do TAF poderia fazer a inclusão do evento informando os dados. Pergunto isso porque em uma mesma empresa pode haver receitas de atividades passíveis da inclusão na CPRB e outras não

Os Eventos são gerados com base em cadastro de origem e não podem ser digitados, porém o cadastro de origem pode sim. No caso do 2060 basta incluir um registro no período de apuração.

## Como se comporta os eventos para SCP aqui?

A Filial SCP terá o mesmo comportamento da Filial Matriz, porém gera somente os dados dela mesma.

## Vou precisar retificar o período de 11/2019, todos os dados estão no RM e o envio foi feito pelo TAF sem nenhuma interação manual dos dados.  Nesse caso a retificação deverá ser feita pelo TAF? Ou consigo retificar pelo RM?

Deverá ser realizada no TAF, pois lá estão os protocolos de transmissão originais.

## Os registros do R-2010 quando vinculados a um CNO, eu precisava lançar estes documentos diretamente no Reinf da Receita, pois o TAF não tinha o recurso, o Backoffice terá?

Deve ser verificado em nossa documentação [Mapeamento da Origem dos Dados - Linha RM - TDN](https://tdn.totvs.com/display/LRM/Mapeamento+da+Origem+dos+Dados)

## Será implementado no cadastro da filial matriz, quando tivermos situações tributárias diferenças ? Exemplo a matriz é considerada indústria e algumas filiais são consideradas produtores rurais.

Deve ser observado qual a orientação da RFB.

## Como funciona envio do período sem movimentação?

De acordo com a Reinf deve ser enviado um Evento de Encerramento do período normalmente.

## não há como realizar edições nos registros antes do envio?

Do Evento em si não, deve ser editado a origem do dado (Lançamento, Movimento, Cliente etc.).

## Posso fazer um R-5011 por ano? A cada virada de ano, fazer um novo cadastro R-5011?

De acordo com o Manual da Reinf o R5011 deve ser mensal mesmo sem movimentação.

## Seria um Evento-5011 para cada SCP?

Seria um R-1000 e um R-5011 para cada SCP conforme orientação da RFB

## Pelo que eu entendi, a data fim no cadastro será enviado só depois que o mês foi encerrado, até o evento R 2099 enviado para a receita?

não exatamente, cada Evento tem a sua própria definição para a data. Consulte a nossa documentação. [Mapeamento da Origem dos Dados - Linha RM - TDN](https://tdn.totvs.com/display/LRM/Mapeamento+da+Origem+dos+Dados)

## Peguei o evento a partir das 11:00 hs, mas gostaria de deixar uma pergunta conceitual, qual é o motivo de ter investido tempo nesse envio pelo RM, uma vez que o nascimento do TAF é a forma de unificação dos processos legais...

Tentando sempre superar as expectativas dos clientes com soluções aderentes e robustas, a TOTVS optou por flexibilizar a EFD-Reinf atendendo assim diversos perfis de empresas e agregando mais valor ao negócio do nosso cliente.

## rejeitado ele criar um id, caso excluir possa ser que ele informe que já existe um iD anterior no próximo arquivo gerado?

Ao gerar um novo Evento o ID será diferente

## Perdi uma parte da explicação....dentro de um evento tem uma nota com problema, com isso o evento fica rejeitado, como identifico essa determinada nota dentro desse evento?

Será necessário verificar o anexo origem ou anexo de consulta SQL para identificar as notas.

## Ao corrigir a nota continuamos tendo que regerar todo evento para nova transmissão?

Sim, Mas o processo pode ser automatizado através de Job.

## Se tiver gerado alguma guia de algum imposto no RM e precisar fazer alguma alteração, será necessário estornar as guias?.

não, somente se for relevante para o caso em questão.

## Se eu precisar alterar um lançamento e retificar a Reinf e o meu período de apuração já estiver encerrado e as guias ja estiverem geradas e quitadas? Será necessária exclusão de baixa de guia?

Se você não transmitisse a Reinf o que teria que fazer? A Reinf não alterou nada no processo, você continuará fazendo o que fazia antes, porém agora também é necessário retificar a Reinf.

## Como faço com as notas de meses anteriores que chegaram agora e a contabilidade já encerrada e  precisam ser informadas no REINF?

O RM não implementou nenhuma trava a respeito, basta verificar a orientação da RFB

## Se eu tiver uma alteração / inclusão após transmissão do Reinf o Evento gerado será somente complementar ou o arquivo irá com todas as notas do período?

De acordo com as regras da RFB o Evento deve ser transmitido de forma completa e não apenas os dados complementares.

## Somos uma construtora e pelo taf nós temos que informar o CNO/CEI em cada nota, na TOTVS não informamos em nem um campo,no lançamento da nota, como vai essa informação do CNO/CEI?

Deve ser verificado em nossa documentação [Mapeamento da Origem dos Dados - Linha RM - TDN](https://tdn.totvs.com/display/LRM/Mapeamento+da+Origem+dos+Dados)

## Eu não sei se alguém já perguntou, mas pode alternar a remessa um mês pelo TAF e outro mês pelo RM , ou quando troca não tem como mudar

Sim, pode Alternar. Contudo, a cada mudança de aplicativo um novo R-1000 deve ser transmitido.

## Eu posso continuar o mesmo ambiente do TSS hoje utilizado pelo TAF, como as mesmas bases de dados ??? Temos base para e-Social /Reinf e uma base do TSS eSocial/Reinf ?

O TSS não teve nenhuma alteração neste sentido e pode ser mantido.

## No ambiente de teste, eu utilizado o TSS e envio para receita estes eventos ou gero no teste , mas não envio?

Mesmo no ambiente de teste todos os Eventos são transmitidos para a receita e validados pela mesmo. Contudo, a receita também utilizará um ambiente de testes.

## Qual o Patch da 27 que já temos esse envio nessa modalidade?

Ao iniciar os testes é aconselhável utilizar o ultimo patch disponível.

## Então deverá haver um TSS para homologação? não pode ser usado o mesmo usado em produção?

Sim, esta recomendação é para qualquer processo que utilize o TSS(NF-e, NFS-e, TAF etc.)

## Se o Esocial utilizar um TSS e a movimentação de NFs for em outro pode?

Sim.

## Meu certificado é único para todas as filiais, mesmo assim tenho que configurar todas as filiais?

não, apenas para a filial Matriz ou SCP responsável pela transmissão

## Se eu fizer uma exclusão de Contribuinte em testes, e estiver usando uma base convertida para testes, na qual é alterado o CNPJ para 11111..., poderá gerar problemas, já que qualquer outra pessoa poderá estar fazendo testes e vai virar uma bagunça. confere?

Você conseguirá executar vários testes, mas a receita não irá autorizar os Eventos porque ela não irá reconhecer o CNPJ fictício com o assinante do xml.

## Consigo testar a conexão URL do TSS de produção sem enviar ou gerar registros? sou cliente Cloud, e por segurança eu gostaria de testar a conexão no ambiente de produção.

não pelo sistema, mas a URL pode ser testada em qualquer navegador web. No sistema as configurações necessária no TSS serão realizada no momento da transmissão e a cada nova transmissão estas configurações são revalidadas.

## O TSS da Reinf é diferente do TSS de Nota fiscal ?

não, trata-se do mesmo aplicativo, porém alguns clientes utilizam ambientes separados.
