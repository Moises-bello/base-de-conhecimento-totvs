---
content_hash: 31f718710b830d510c91c82261a9ccd967294cfc908dd213ed10f205576ca089
fetched_at: '2026-06-29T00:12:07.372662+00:00'
page_id: '925337683'
product: rm
source: tdn-rm
title: Portal do Cliente - PDC - Boleto ( Novo PDC - Vendas )
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=925337683
version: 7
---

Novidade

### Implementação do Boleto Híbrido no PDC

Foi implementado o **boleto híbrido** no Portal do Cliente (PDC).

Com essa implementação, ao configurar nos parâmetros do portal do cliente no TCGI para utilizar o boleto híbrido, o PDC passará a gerar o boleto híbrido na tela de **Situação Financeira**. Além disso, na tela de **2ª via**, serão apresentadas, em uma única interface, duas formas integradas de pagamento:

* **Código de barras** para pagamento via boleto bancário tradicional.
* **QR code PIX** para pagamento instantâneo.

Dessa forma, o cliente tem a flexibilidade de escolher sua forma preferida de pagamento, seja pela agilidade do PIX ou pela praticidade e prazo mais longo do boleto tradicional, sem comprometer a segurança e integridade da transação.

* Para configurar o uso do **boleto híbrido** no portal, acesse: [Totvs Incorporação - Parâmetros - Portal do Cliente](https://tdn.totvs.com/pages/viewpage.action?pageId=435105047).
* Para saber mais sobre o funcionamento e vantagens do **boleto híbrido**, acesse: [Boleto Híbrido](https://tdn.totvs.com/pages/releaseview.action?pageId=908344227#0-1).

**É importante que o relatório associado à impressão deste tipo de boleto esteja parametrizado para apresentar tanto a imagem do código de barras, quanto a imagem do qr code pix.**

# Neste exemplo , segunda via de boleto de vendas.

**Segunda Via de Boleto**

A funcionalidade de **segunda via de boleto** em um **Portal de Imóveis** é essencial para garantir a comodidade e a eficiência no pagamento de compromissos financeiros, como aluguel, condomínio, parcelas de financiamento ou taxas administrativas.

#### **Benefícios Principais:**

1. **Facilidade para o Cliente**

* Evita atrasos no pagamento por perda ou não recebimento do boleto original.
* Garante que o usuário possa acessar o documento a qualquer momento, sem depender do atendimento presencial ou telefônico.

1. **Redução da Inadimplência**

* Disponibilizar rapidamente a segunda via evita que os clientes deixem de pagar por dificuldades no acesso ao boleto original.
* Facilita a regularização de pendências financeiras.

1. **Otimização do Atendimento**

* Reduz a necessidade de suporte manual para envio de boletos.
* Diminui a carga de trabalho da equipe financeira e de atendimento ao cliente.

1. **Automação e Eficiência**

* Com integração bancária, o sistema pode gerar automaticamente boletos atualizados com valores corrigidos (se houver juros ou multa).
* O uso de **código de barras, QR Code Pix ou links de pagamento** agiliza a quitação do débito.

NOVO PDC

Este novo Portal de Atendimento ao Cliente encontra-se disponível na versão 12.1.2502 em diante.

Visão de contratos mostra todos contratos ativos de qualquer coligada do Cliente logado em Vendas .

Ao ocultar os dados do Boleto , não fica visível para o cliente a quantidade de Boletos em Atraso com os valores dos mesmo.

Obs: O **campo Compensação** é utilizado para Boletos de Aluguel ( Saiba mais clicando :  [AQUI](https://tdn.totvs.com/display/public/LRM/Portal+do+Cliente+-+PDC+-+Boleto) )

Ao clicar para visualizar , mostra quantidade de Boletos em atraso e os valores das Parcelas, tanto das parcelas vencidas com as parcelas que irão vencer.

Ao clicar sobre codigo de barras do boleto no Portal , cliente pode baixar o Boleto ou copiar código de barras.

Ao baixar boleto - Virificar se o existe um bloqueador de pop up no Browser , se estiver , desativar o mesmo para o Boleto do Portal do Cliente.

Copiando código de Barras

Importante.

* Caso o usuário possua um **boleto agrupado**, cujos lançamentos pertençam a um contrato de aluguel e um contrato de venda, o mesmo boleto irá aparecer tanto na visão de boletos de aluguel, quanto na visão de boletos de venda e seu valor sempre será o valor total de todos os lançamentos que compõem o boleto, independente do contexto selecionado.
* Os Boletos de Reembolso das despesas que pertencem ao Imóvel do Locador ou Subunidade do Comprador, também deverá aparecer na visão da 2ª Via de Boleto para emissão.

Boletos para ficarem visíveis no Portal precisam estar Registrado ou com Registro Online.
