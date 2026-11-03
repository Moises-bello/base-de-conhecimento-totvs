---
content_hash: 690295a07dde7e7ccdbaf1cae01fe652bcd3ab53c12933451551e8d13dbccfdc
fetched_at: '2026-06-29T00:11:32.871191+00:00'
page_id: '750393605'
product: rm
source: tdn-rm
title: 1o. Momento Inovação TOTVS RH - Linha RM (16/03/2023)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=750393605
version: 11
---

## **PPT Apresentação:**

250

## **Gravação:**

## 

## **FAQ**

Material criado com o objetivo de compartilhar os principais questionamentos realizados no evento **1o. MOMENTO INOVAÇÃO RH RM**, realizado no dia 16 de Março de 2023.

1. **Relatório de Conferência INSS Patronal**
2. **TAE - TOTVS Assinatura Eletrônica**
3. **Dashboard de Marcação de Ponto**
4. **Outras Perguntas**

## **01.****RELATÓRIO DE CONFERÊNCIA INSS PATRONAL**

**1.2.** **O Relatório servirá tanto para clientes Middleware quanto para quem usa o TAF Full?**

O Relatório está disponível tanto para os clientes que utilizam o Middleware ou o TAF. Porém a utilização é dentro do RM. Veja detalhes no TDN: <https://tdn.totvs.com/pages/viewpage.action?pageId=714242305>.

**1.2.** **O Relatório está disponível a partir de qual versão do RM?**

Está disponível a partir da 12.1.2209, veja a partir de quais patches acessando o TDN: <https://tdn.totvs.com/pages/viewpage.action?pageId=714242305>.

**1.3.** **É necessário parametrizar o Relatório Empresa?**

Sim. Veja os detalhes no tdn: <https://tdn.totvs.com/pages/viewpage.action?pageId=714242305>

**1.4.** **No meu RM não aparece a opção patronal. Como faço?**

O relatório está disponível no menu eSocial | Conferência de Conferência de INSS Patronal. 

Veja os detalhes no TDN <https://tdn.totvs.com/pages/viewpage.action?pageId=714242305>, nessa página menciona os patches e explica as configurações necessárias.

**1.5.** **Para os clientes que usam SmartSocial, tem acesso ao relatório no próprio RM? Pergunto pois ao acessarmos o relatório, informa que necessita informar conexão do APP e API’s nos parâmetros de integração com Middleware.**

Sim, o acesso é no produto TOTVS Folha de Pagamento. Veja os detalhes da configuração no TDN: <https://tdn.totvs.com/pages/viewpage.action?pageId=714242305>

**1.6.** **Na geração do lançamento financeiro, existe a quebra pelo tipo de receita?**

A quebra segue de acordo com a já existe na GPS. Porém caso haja necessidade em sua empresa, poderá solicitar uma melhoria na central colaborativa.

## **02.** **TAE - TOTVS ASSINATURA ELETRÔNICA**

**2.1.** **Em relação a integração do TAE a partir de qual versão estará disponível no RM?**

O TAE já está disponível para a Folha de Pagamento e Automação de Ponto nas versões de mercado. 

Para o MEU RH está disponível a partir da 12.1.2302.

**2.2.** **Como está o processo de monitoramento, para assinatura "pendente", existe alguma recorrência de cobrança automática para o funcionário, ou algum monitoramento no produto ou TAE?**

No TAE é possível filtrar por status de assinaturas, e realizar reenvios de cobranças em documentos pendentes.

**2.3.** **Reenvio de documentos pendentes é individual?**

Pela plataforma do TAE sim. Pelo monitor de documentos do RM é possível selecionar vários e reenviar.

Estamos desenvolvendo no TAE uma automação para configurar de quanto em quanto tempo será enviado e-mails de cobranças.

**2.4.** **A assinatura do TAE é gratuita?**

O TAE trabalha com pacotes de documentos. É possível testar o trial da ferramenta por 30 dias gratuitamente, sem limite de documentos, usuários e signatários. Após o teste a empresa pode adquirir o plano com a quantidade de envelopes mensais que vai atender à necessidade dela.

Existe uma calculadora no nosso site, que ao digitar a quantidade necessária ele mostra o plano que melhor se adapta à necessidade.

<https://www.totvs.com/assinatura-eletronica/>

**2.5.** **Como atualizar a situação das assinaturas dos documentos no Monitor de Relatórios do TAE?**

Temos um parâmetro para essa atualização automática e também um processo na tela de Monitor de Relatórios. Veja:<https://tdn.totvs.com/pages/releaseview.action?pageId=607864794>

**2.6.** **É possível fazer o agendamento da atualização do status de documentos integrados?**

Para este processo não é possível fazer o agendamento. Neste caso o mesmo poder configurado para ser atualizado manualmente. Mais informações:<https://tdn.totvs.com.br/pages/releaseview.action?pageId=607590599>

**2.7.** **Onde acesso a documentação de configuração do TAE?**

<https://tdn.totvs.com.br/pages/viewpage.action?pageId=745122002>

<https://tdn.totvs.com/pages/viewpage.action?pageId=733186927>

**2.8.** **Assinatura no treinamento para comprovar a presença, tem alguma coisa?**

É possível criar um relatório, contendo os campos CODCOLIGADA e CHAPA e enviar para os participantes assinarem.

**2.9.** **Ele envia o link de acesso ao TAE para o funcionário por qual canal de comunicação (email, sms, whatsapp, etc)?**

Hoje os links dos documentos são enviados via e-mail. Mas temos em roadmap no TAE outras formas de envio como SMS e Whatsapp.

**2.10.** **No caso de e-mail, qual campo do cadastro ele utiliza para buscar o e-mail do funcionário?**

Ele busca o e-mail cadastrado para os funcionários.

**2.11.** **É possível enviar o documento para algum dispositivo móvel para que o funcionário assine?**

O TAE possui aplicativos nativos para Iphone e Android. Além do portal web ser responsivo. Então a assinatura por parte dos funcionários pode ser feita via Computador Pessoal, Celulares ou Tablets.

**2.12.** **Previsão do roadmap a médio ou a longo prazo?**

A expectativa é que esse recurso esteja disponível até o final do ano. Acompanhe nosso roadmap no link:<https://produtos.totvs.com/produto/totvs-rh/totvs-rh-linha-rm/>

**2.13.** **Já utilizamos o TAE para a assinatura do ponto, porém ainda não conseguimos enviar os relatórios de admissão que são 10 arquivos, arquivos esses que não são enviados de forma global, ou seja, todos no mesmo arquivo, isso já é possível?**

É possível criar Grupo no Tipo de Relatórios (com todos os relatórios a serem enviados) e enviar para cada funcionário de uma só vez.

**2.14.** **É possível utilizar outra plataforma de assinatura eletrônica ou o envio pode ser feito somente com o TAE?**

A integração dos módulos de RH da linha RM são apenas com o TAE.

**2.15.** **Um prospect me disse que o jurídico dele orientou usar a solução de assinatura eletrônica no aviso e recibo de férias que esteja integrada com o aplicativo [Gov.br](http://Gov.br) (que possibilita qualquer cidadão realizar uma assinatura eletrônica). Algum cliente já solicitou isso? Esse processo de integração seria possível?**

Não temos essa solicitação mapeada no nosso roadmap. Mas, você pode abrir uma solicitação na central colaborativa que iremos avaliar.

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039467434-Central-Colaborativa-Como-Acessar>

**2.16.** **Em relação ao Portal RH, o relatório também vai com a assinatura?**

A integração atual é entre o MEU RH e TAE. O Portal RH não faz essa integração.

**2.17.** **conseguimos copiar o link de assinatura para passar para o WhatsApp do funcionário ou até mesmo abrir um um tablet no RH para que ele possa assinar?**

Sim, o interface do TAE é responsiva, pode ser acessada por dispositivos móveis

**2.18.** **Existe algum parâmetro para indicar qual e-mail deve ser enviado o documento? Exemplo: envio para o e-mail particular.**

Para o funcionário, Gestor ou destinatário específico configurado no cadastro de tipo de relatório é considerado o e-mail cadastrado na PPESSOA. No monitor de documentos pode colocar um e-mail definido para o papel (Assinador, Validador ou Testemunha).

**2.19.** **Para quem já tem a assinatura do TAE, já pode usar no RM ou tem algum tipo de ação necessária antes?**

O TAE possui integrações nativas com várias linhas de produtos TOTVS. Para começar a usar basta seguir com as parametrizações indicadas no link: <https://tdn.totvs.com/pages/releaseview.action?pageId=607585319>

**2.20.** **Depois que o documento foi assinado conseguimos integrar com o GED?**

O TAE oferece API's que podem ser utilizadas para construir integrações com GED's.

**2.21.** **No aviso de férias gerado é possível colocar nome da empresa ou a logo da empresa?**

Sim. Esse documento é gerado pelo RM Reports, ou seja, qualquer informação gerada no RM Reports será enviada no relatório PDF criado.

**2.22.** **Os relatórios para assinatura só podem ser enviados via e-mail?**

O aviso de recebimento do documento chega por e-mail. Ou por notificação push, caso o usuário já possua o APP do TAE. Temos em ROADMAP 2023 envios para SMS e WhatsApp

**2.23.** **Para o espelho de ponto já temos a opção do Gestor também realizar a assinatura ou apenas o funcionário?**

Apenas o funcionário consegue assinar, segue o link do TDN para mais detalhes: <https://tdn.totvs.com/pages/releaseview.action?pageId=689058315#1-2>.

**2.24.** **Se houver algum erro no relatório enviado e assinado pelo funcionário, será necessário o envio de um novo relatório já que não tem como desfazer a assinatura?**

Sim. Porém, existe a opção de rejeitar o documento. Se for detectado algo errado no documento, o autor ou destinatário pode rejeitar e informar o motivo. E um novo documento deve ser enviado corrigido.

**2.25.****É possível utilizar outra plataforma de assinatura eletrônica ou o envio pode ser realizado somente com TAE?**

Para a Folha de Pagamento e Automação de Ponto só é possível fazer a integração utilizando o TAE.

**2.26.****Em caso de cancelamento de aviso de férias, ele permite?**

Você deverá criar um documento 'Outros' e enviar para o funcionário informando o cancelamento das férias.

**2.27.****Quais são os documentos e tipos que podem ser assinados usando o TAE? Onde são armazenados os documentos assinados, banco de dados ou pastas compartilhadas na rede?**

No TAE pode ser assinado qualquer documento em PDF que a legislação permita assinaturas eletrônicas ou digitais. Todo o sistema roda em cloud.

**2.28.****Tem DataServer(REST API) do TAE para integração entre serviços?**

O TAE possui integrações nativas com várias linhas de produtos TOTVS e também APIS Restful que permitem que o TAE seja integrado com qualquer outro sistema que consuma API's .

<https://tdn.totvs.com/pages/releaseview.action?pageId=607585319>

<https://totvs-sign.readme.io/reference/gettings-started>

**2.29.****Será disponibilizado algum SDK para integração das assinaturas em aplicativos?**

O TAE possui integrações nativas com várias linhas de produtos TOTVS e também APIS Restful que permitem que o TAE seja integrado com qualquer outro sistema que consuma API's .

<https://tdn.totvs.com/pages/releaseview.action?pageId=607585319>

<https://totvs-sign.readme.io/reference/gettings-started>

**2.30.****Quero usar o TAE, com meu programa de assinatura digital (D4Sign), é possível fazer a integração?**

O TAE possui integrações nativas com várias linhas de produtos TOTVS e também API's Restful que permitem que o TAE seja integrado com qualquer outro sistema que consuma API’s.

<https://tdn.totvs.com/pages/releaseview.action?pageId=607585319>

Documentação das nossas API's: <https://totvs-sign.readme.io/reference/gettings-started>

**2.31.****É possível utilizar outra plataforma de assinatura eletrônica ou o envio pode ser realizado somente com TAE?**

O recurso disponibilizado pela Folha de Pagamento e Automação de Ponto só é possível integrar com o TAE.

**2.32.****Como posso saber se no meu contrato posso utilizar o MEU RH**

Entre em contato com seu ESN, ou pela nossa Central de Relacionamento. <https://totvscst.zendesk.com/hc/pt-br/#home>

**2.33.****Nesse caso, o cliente precisa adquirir a TAE?**

O TAE trabalha com pacotes de documentos. É possível testar o trial da ferramenta por 30 dias gratuitamente, sem limite de documentos, usuários e signatários. Após o teste a empresa pode adquirir o plano com a quantidade de envelopes mensais que vai atender à necessidade dela.

Existe uma calculadora no nosso site, que ao digitar a quantidade necessária ele mostra o plano que melhor se adapta à necessidade.

<https://www.totvs.com/assinatura-eletronica/>

**2.34.****Se entendi para assinatura de espelho de ponto pelo MEU RH teremos que inserir antes no TAE para cada funcionário?**

Sim, no momento fazendo a publicação pelo TAE para ser assinado no MEU RH, pode inserir no TAE qualquer documento.

**2.35.****Eu mandei 40.000 documentos para assinatura e não consigo atualizar os status?**

Na configuração global tem a opção para atualizar o status automaticamente. E também tem a opção de atualizar status no processo dentro do monitor de documentos.

<https://tdn.totvs.com/pages/releaseview.action?pageId=607590599&moved=true>

**2.36.****Qual a possibilidade de visualizar o documento assinado pelo TAE dentro do aplicativo do RM?**

É possível visualizar dentro do Monitor de Relatório. Após assinado será permitido baixar o documento.

**2.37.****Os arquivos/Dados (documento assinado) ficam fisicamente somente no portal do TAE (podendo ser baixado), ou ele também fica armazenado na Base de Dados da RM local?**

É possível visualizar dentro do Monitor de Relatório. Após assinado será permitido baixar o documento.

**2.38.****Esta funcionalidade é apenas para Clockin, não MEU RH?**

Se estiver falando da assinatura eletrônica, ela está disponível no APP do MEU RH.

**2.39.** **O TAE envio os cartões de ponto automático?**

Tem um parâmetro ao gerar o relatório do espelho de cartão de ponto para enviar para o TAE.

**2.40.****No RM pelo TAE só posso enviar então contracheque e férias por enquanto?**

Podem ser enviados para assinatura (Aviso de Férias, Recibo de Férias) e Outros (Documentos gerados que tenham os campos CHAPA e CÓDIGO DE COLIGADA). Pelo módulo de Automação de Ponto é possível fazer o envio do espelho do ponto.

**2.41.****Consigo enviar esses documentos do TAE em massa?**

É possível cadastrar mais de um relatório para ser enviado. E ao executar o processo de integração de relatórios poderá selecionar os funcionários.

**2.42.****Gostaria de saber se o TAE ele vai abrir para outros módulos como o de segurança do trabalho?**

O TAE possui integrações nativas com várias linhas de produtos TOTVS e também API's Restful que permitem que o TAE seja integrado com qualquer outro sistema que consuma API’s.

<https://tdn.totvs.com/pages/releaseview.action?pageId=607585319>

Demais integrações podem ser solicitadas pela central colaborativa.

**2.43.****Qual link que mostra como enviar para assinatura os documentos no RM no TDN?**

<https://tdn.totvs.com.br/pages/releaseview.action?pageId=607590599> ou<https://tdn.totvs.com/pages/releaseview.action?pageId=607864794>

**2.44.****No caso de assinaturas digitais, posso usar isso para envio de relatórios/formulários?**

Pelo portal do TAE pode ser enviado qualquer documento PDF que necessite ser assinado, e que a legislação permita assinaturas eletrônicas e digitais.

## **03.** **DASHBOARD MARCAÇÃO DE PONTO ELETRÔNICO**

**3.1.****O****Dashboard funciona com o ponto no APP via geolocalização mas sem Clockin in?**

Na batida por geolocalização feita no MEU RH integra diretamente com o Automação de Ponto.

**3.2.****No Dashboard de marcações poderia ter a funcionalidade de ao clicar em um item listar os colaboradores para identificar de forma mais fácil quem se enquadra naquele indicador selecionado?**

Teremos até o final deste primeiro semestre de 2023 melhorias no Dashboard.

**3.3.****Precisa ter o Clockin para ativar esse Dashboard?**

O Dashboard funciona para o ponto dos funcionários e possui uma raia também com as informações do Clockin.

**3.4.****O gestor vai poder visualizar o Dashboard do time, ou só o DP? Como? pelo MEU RH?**

A primeira entrega foi só para dentro do sistema mesmo. Mas temos melhorias previstas para o gestor.

**3.5.****Essa quantidade de batidas por dia é uma configuração que serve para todos os horários ou é possível para um determinado horário ter a quantidade de marcações diferentes?**

Para todos os horários. O cálculo do total de marcações é de acordo com o horário do funcionário.

**3.6.****O Clockin in seria para batidas móveis?**

O Clockin é um REP A (alternativo). Faz marcação de batidas com reconhecimento facial e geolocalização.

**3.7.****Qual a versão do RM que está o Dashboard?**

O Dashboard esta disponível a partir da versão: 12.1.2209, segue o link da documentação para maiores informações: <https://tdn.totvs.com/display/public/LRM/Dashboard++Ponto#1-1>.

**3.8.****É possível extrair relatório no Dashboard?**

Ainda não, mas teremos melhorias no Dashboard até o final deste primeiro semestre de 2023.

**3.9.****Como eu habilito essa ferramenta? Na visão que tenho hoje não aparece!**

O Dashboard esta disponível a partir da versão: 12.1.2209, segue o link da documentação com os detalhes para configuração: <https://tdn.totvs.com/display/public/LRM/Dashboard++Ponto#1-1>

**3.10.****Um exemplo: o colaborador esqueceu de marcar a saída de um determinado dia, normalmente a marcação de entrada do dia seguinte anda para o dia anterior. Seria possível identificar estas situações?**

Enquanto a batida for ímpar será considerado como ponto incompleto.

**3.11.****Preciso ter acesso ao Clockin para ter acesso a este Dashboard?**

Não precisa, segue o link da documentação com os detalhes para configuração do Dashboard: <https://tdn.totvs.com/display/public/LRM/Dashboard++Ponto#1-1>

**3.12.****Em relação ao REP - P, já foi lançado algo?**

Liberamos apenas com o Clockin, mas vamos liberar para todos os relógios.

**3.13.****No ponto noturno fica sempre errado. Necessário melhoria, urgente.** **Temos problemas com horários noturno também, e com aquela parametrização de solução de conflito para feriado também**

O sistema olha o total de batidas de acordo com o horário.

**3.15.****Podemos internamente dar manutenção ao Dashboard?**

Ele é apenas um relatório, sendo possível apenas a visualização.

## **04.** **OUTRAS PERGUTAS**

**4.1.****Onde fica essa central colaborativa?**

A central colaborativa fica dentro do portal do cliente, segue o link da página: <https://centraldeatendimento.totvs.com/hc/pt-br/community/topics>.

**4.2.Sobre o relatório de base de INSS, tem um relatório por empregado?**

Tem sim, veja os detalhes no TDN: <https://tdn.totvs.com/pages/viewpage.action?pageId=536721262>

**4.3.Conforme relatório de conferência de INSS, gostaria de saber quando será disponibilizado um relatório para a conferência do IRRF?**

Diferente do INSS, o eSocial não irá realizar o cálculo do IRRF, irá acatar o valor de IR enviado pela folha, porém existe o evento S-5012 que retorna as bases de IRRF. Estamos realizando um estudo juntos com as demais linhas de folha de pagamento da TOTVS, para construirmos um relatório onde o usuário poderá conferir essas bases de cálculo de IRRF e futuramente iremos divulgar essa novidade.

Acompanhe sua nossas liberações pelo link <https://produtos.totvs.com/produto/totvs-rh/totvs-rh-linha-rm/>

**4.4.****Quando atualizei da versão 12.1.33 pra versão 12.1.2209 a altura das linhas vieram bem largas, na demonstração de tela de vocês vi que a altura da linha está menor, qual versão é esta por gentileza?**

Tivemos uma repaginação visual extensiva do RM, veja detalhes no TDN: <https://tdn.totvs.com/pages/releaseview.action?pageId=273981623>

**4.5.****Qual o link desse RH Informa?**

O link é <https://rhinforma.totvs.com/>

**4.6.****O** **que é o clocking?**

É um REP Alternativo comercializado pela TOTVS. Que faz marcação com reconhecimento facial e geolocalização.
