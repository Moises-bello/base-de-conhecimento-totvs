---
content_hash: 99755b27817e815e100c17bd895cd6529eb593405581d99d1b90eaad326c089c
fetched_at: '2026-06-29T00:10:35.686688+00:00'
page_id: '531027675'
product: rm
source: tdn-rm
title: Novidades 12.1.28 - TOTVS Construção Gestão de Imóveis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=531027675
version: 14
---

**Venda**

* Contrato de venda : Tipo de venda agora já vem selecionado Venda por default. Não sendo mais possível selecionar Aluguel na tela de Venda.
* Incluído o Menu Documento na tela do cadastro do Contrato de Venda.
* Disponibilizado a possibilidade de ao gerar o Financiamento  com o componente **Financiamento CEF** zerado.
* Disponibilizado Menu para manutenção do Andamento da Obra(Utilitários>>Gestão>>Andamento da Obra Portal/App).
* é calculado via média ponderada.
* Disponibilizado a consulta da contabilização no cadastro do Aditivo através do menu Anexos.
* Funções de Fórmulas - Venda - [Clique Aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=543074907)
* Disponibilizado o [modelo de relatório de termo de aceite](https://tdn.totvs.com/pages/viewpage.action?pageId=544188979), para que seja usado na rotina de renegociação no Portal do Cliente e Meu Imóvel

**Aluguel**

* Nas visões dos aditivos de [alteração de imóvel](https://tdn.totvs.com/pages/viewpage.action?pageId=435105257) e [exclusão de imóvel](https://tdn.totvs.com/pages/viewpage.action?pageId=435104951), foi disponibilizado um campo para visualizar a soma dos valores totais alterados do aditivo.
* Criação da opção de "[Realiza integração com portais externos](https://tdn.totvs.com/pages/viewpage.action?pageId=435105278)" no cadastro de imóveis;
* Disponibilização dos serviços do [XML de Imóveis e Imagens do Imóvel](https://tdn.totvs.com/pages/viewpage.action?pageId=538492830) para integração com portais externos;
* Implementado o parâmetro "[Relatório para exibição do Termo de Aceite](https://tdn.totvs.com/pages/viewpage.action?pageId=435105047)" para definição do relatório de Termo da Renegociação utilizado no aplicativo Meu Imóvel e no PdC.
* Implementado o [parâmetro "Integração Portais"](https://tdn.totvs.com/pages/viewpage.action?pageId=435105240) que definirá as informações contidas no header do [.xml de integração com portais externos](https://tdn.totvs.com/pages/viewpage.action?pageId=538492830).
* Disponibilizado o campo Classificação no [cadastro de características](https://tdn.totvs.com/pages/viewpage.action?pageId=435104890): Estas classificações (Quarto, Banheiro, Garagem, Suíte) poderão ser associadas e serão enviadas no [.xml de integração de imóveis com portais externos](https://tdn.totvs.com/pages/viewpage.action?pageId=538492830)
* Disponibilizado o campo Observação no [cadastro de Imóvel](https://tdn.totvs.com/pages/viewpage.action?pageId=435105278). Este campo deverá conter as informações pertinentes ao imóvel e será enviado no [.xml de integração de imóveis com portais externos](https://tdn.totvs.com/pages/viewpage.action?pageId=538492830)
* Melhoria nas regras de cadastro de [garantias](https://tdn.totvs.com/pages/viewpage.action?pageId=520659198) e [fiadores](https://tdn.totvs.com/pages/viewpage.action?pageId=520659200). Não será possível efetivar um contrato de locação com fiadores e garantias informados, bem como cadastrar garantias de modalidades diferentes.
* No cadastro de Empreendimento, na aba Informações foi adicionado um campo que informa quantidade de Sub-unidades disponíveis para venda.

**Portal/App**

**Meu Imóvel**

* Implementada opção ["Prefiro escolher parcelas"](https://tdn.totvs.com/pages/viewpage.action?pageId=518482641) na tela de renegociação do aplicativo Meu Imóvel;
* Disponibilizada tela de [revisão da renegociação](https://tdn.totvs.com/pages/viewpage.action?pageId=51848264), com os dados resumidos da proposta de renegociação;
* O aplicativo Meu Imóvel e o PdC, passam a exibir para o usuário [o relatório de termo da renegociação](https://tdn.totvs.com/pages/viewpage.action?pageId=518482641), na tela de resumo da renegociação;
* Disponibilizada a [notificação push de novos Comunicados](https://tdn.totvs.com/pages/viewpage.action?pageId=538493587) cadastrados.
* Os boletos gerados através do menu de [pagar parcelas atrasadas ou antecipar](https://tdn.totvs.com/pages/viewpage.action?pageId=518482641#MeuIm%C3%B3vel-Situa%C3%A7%C3%A3oFinanceira-B)Pagarparcelasatrasadasouantecipar), contarão com um botão "Copiar Código de Barras", permitindo a cópia do código de barras para pagamento em outros aplicativos.
* Disponibilizado o menu ["Ver Parcelas Pagas"](https://tdn.totvs.com/pages/viewpage.action?pageId=518482641#MeuIm%C3%B3vel-Situa%C3%A7%C3%A3oFinanceira-D)Verparcelaspagas) na visão de situação financeira.
* Os Boletos de Reembolso de Despesa serão apresentados no menu Segunda Via de Boleto.
* é calculado via média ponderada.
* Melhoria no processo de renegociação. Será possível prosseguir com a renegociação caso não exista um relatório de termo de aceite [configurado](https://tdn.totvs.com/pages/viewpage.action?pageId=435105047).
* Disponível o menu "[Ver detalhes da renegociação](https://tdn.totvs.com/pages/releaseview.action?pageId=518482641)", este menu irá listar todas as renegociações deste contrato, suas datas, valores e status da renegociação vigente.
* Ao solicitar a [renegociação](https://tdn.totvs.com/pages/releaseview.action?pageId=518482641) no aplicativo meu imóvel, além do aditivo de renegociação, será gravado também o relatório de termo de aceite, caso configurado, para que possa ser exibido ao usuário através do menu de [Documentos](https://tdn.totvs.com/pages/viewpage.action?pageId=515691276).

**PdC**

* O campo "[Texto para notificação (App Meu imóvel)](https://tdn.totvs.com/display/LRM/Portal+do+Cliente+-+PDC+-+Comunicados)" será usado nas notificações de novos comunicados que serão enviados aos clientes.
* Os Boletos de Reembolso de Despesa serão apresentados no menu Segunda Via de Boleto.
* Será exibido a situação da venda(Efetivada, Quitada, Distratada).
* é calculado via média ponderada.
* Melhoria na abertura de , caso esteja integração com o Agilis será possível utilizar o cliente online.
* Disponibilizado a possibilidade de envio de anexos no
* Melhoria no processo de [renegociação](https://tdn.totvs.com/pages/viewpage.action?pageId=435105313) do Portal do Cliente. O usuário agora poderá visualizar os detalhes da renegociação, através do relatório de termo de aceite, caso o mesmo esteja configurado.
