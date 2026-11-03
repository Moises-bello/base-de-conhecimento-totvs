---
content_hash: 92b70ec1ef47bf3a352088633fb9dfdc105403cf7c263476560ec8b6f9aec2d3
fetched_at: '2026-06-29T00:11:38.197744+00:00'
page_id: '781869855'
product: rm
source: tdn-rm
title: Perguntas e Respostas - Webinar
type: documentation
url: https://tdn.totvs.com/display/LRM/Perguntas+e+Respostas+-+Webinar
version: 8
---

Não consta a flag "Módulo de Caixa 2.0" na minha sessão de caixa.

**RESPOSTA**

* O Módulo de Caixa 2.0 está disponível dos patches 12.1.2302.186 e 12.1.2306.130.

Nas opções de filtro, o "Período" refere-se a qual data do sistema?

**RESPOSTA**

* Disponibilizamos as opções de filtro por Data de emissão ou Data de vencimento. Mais informações: [4.1. Pesquisa de Lançamentos](https://tdn.totvs.com/pages/releaseview.action?pageId=745132012)

O recebimento via TEF é integrado apenas ao Sitef?

**RESPOSTA**

* Sim, hoje a integração TEF é homologada à Software Express.

O recebimento via PIX tem integração com alguma API PIX de banco ou apenas com o TPI?

**RESPOSTA**

* Para recebimento via PIX através do Módulo de Caixa é necessária a contratação do TOTVS Pagamento Instântaneo (TPI) ou o TOTVS Pagamento Digital (TPD). Mais Informações:

Por se tratar de uma flag no momento da abertura da sessão de caixa, pode-se usar usuário no caixa atual e outro como caixa 2.0?

**RESPOSTA**

* Inicialmente o Módulo de Caixa 2.0 é opcional, o mesmo usuário pode optar por ora usar a versão 2.0, ora a versão 1.0 referente a mesma sessão ou um usuário usar apenas a versão 1.0 e outro usar apenas a versão 2.0.

É possível incluir parcelas extras nos contratos do Educacional na versão 2.0?

**RESPOSTA**

* Sim é possível incluir serviços extras na versão 2.0. Mais informações:

**OBS**: Esta tela está sendo repensada junto com o time do educacional, para deixarmos mais simples para o operador do caixa.

Esse módulo Caixa é mais adequado ao Educacional ou também vai atender demandas do módulo Hospitais e Clínicas?

**RESPOSTA**

* Revisitamos a experiência do recebimento físico para uma jornada que encaixa em qualquer segmento. Sabemos que segmentos específicos, como o Saúde, exigem algumas particularidades, o próximo passo é aprofundar em como atender estas particularidades.

Vai ter a opção de Reabrir o Caixa, para efetuar alguma correção, caso necessário?

**RESPOSTA**

* Não temos previsto em nossa roadmap esta possibilidade. Seria importante entender a necessidade por trás deste pedido, como por exemplo, quais tipos de ajustes são necessários? Compartilhe mais detalhes conosco através da [central colaborativa](https://centraldeatendimento.totvs.com/hc/pt-br/community/topics/360001450394-TOTVS-Backoffice-Linha-RM-Financeiro).

Essa versão da sessão vai ser disponilizada para o backoffice distribuição também ou apenas para o educacional?

**RESPOSTA**

* O Módulo de Caixa está disponivel dentro do módulo TOTVS Gestão Financeira para qualquer segmento.

A impressão do QRCode pode ser liberada em uma janela móvel (tipo em 2 monitores) ou possibilitar a impressão pela sessão de caixa? O cliente não tem acesso ao monitor do caixa para pagar via PIX com QRCode em tela.

**RESPOSTA**

* Adoramos esta sugestão, e iremos avaliar a melhor forma de entregar esta funcionalidade pra vocês. Acompanhe o TOTVS News e mantenha a sua versão sempre atualizada.

É possível abrir a sessão de caixa diretamente a partir de um atendimento particular no módulo saúde? ou só abre a partir de um lançamento financeiro?

**RESPOSTA**

* Inicialmente conseguimos acessar o recebimento via Módulo de Caixa, apenas pela visão de lançamentos. Mas estamos estudando possibilidades de integração com outros módulos. Mais informações:  no tópico "Recebimento em outros módulos".

Conseguimos baixar mais de um título ao mesmo tempo?

**RESPOSTA**

* Sim, tanto por dentro da sessão de caixa, quanto pela visão de lançamentos é possível selecionar mais de um título e realizar o recebimento.

Teria a possibilidade de abrir a sessão de caixa direto da tela de movimento sem precisar editar o movimento?

**RESPOSTA**

* Não, hoje o recurso está disponível apenas através da visão de lançamentos, depois de selecionar os títulos.

É possível incluir extrato de caixa?

**RESPOSTA**

* Não, hoje o recurso não está disponível. Mas considerando as necessidades de realizar sangria e suprimento do caixa iremos avaliar como atender estas necessidades.

Os recebimentos de mensalidade com cartão de credito estarão dentro do RM para conciliação junto a bandeira?

**RESPOSTA**

* Sim, os extratos bancários são gerados automaticamente para conciliação bancária, assim como na baixa manual por fora na sessão de caixa.

O recebimento via cartão, é integrado apenas ao Sitef?

**RESPOSTA**

* Hoje as transaçãos por meio do TEF utilizam apenas o modelo Sitef . Mais informações: [2. Configurações iniciais](https://tdn.totvs.com/pages/viewpage.action?pageId=744486589#id-2.Configura%C3%A7%C3%B5esiniciais-Etapas6e7-TEFeTEFFilial)

Implantou a reimpressão do fechamento de caixa?

**RESPOSTA**

* A reimpressão era uma necessidade grande, devido a confusão dos termos Desativar e Fechar a sessão e a proximidade dos botãos. Como mudamos esta experiência, o assunto não foi priorizado no momento, e iremos considerar durante a revisão da tela de Gerenciamento dos Caixas.

Sobre a integração com TEF, a sessão do caixa captura os dados de transação e abastece essas informação na baixa e extratos?

**RESPOSTA**

* Sim, da mesma forma que é feito nas baixas manuais por fora da sessão de caixa.

Como fica a contabilização do lançamento? É realizada no momento da baixa? Percebi que não tem mais essa etapa, onde colocamos o evento contábil da baixa.

**RESPOSTA**

* Entendemos que o operador de caixa dentro do seu contexto de atendimento, não pode ser interropido para realizar ajustes na contabilização, que é um processo importante para a empresa mas não deve impactar no atendimento ao cliente.  A contabilização do lançamento continua sendo feita de forma automática baseado nos eventos contábeis definidos como default, mas agora de forma transparente para o operador de caixa. Os lançamentos que não conseguirem localizar automaticamente os eventos ficaram com o status Baixa a Contabilizar e precisaram ser conferidos e ajustados posteriormente. Mais informações:  tópico Integração Contábil.

Utilizamos muito o ref lançamento, ele continuará nessa nova versão?

**RESPOSTA**

* Sim, os campos principais de busca continuam disponíveis. Mais informações:
