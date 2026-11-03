---
content_hash: f23d9bf8c9f3bbeda212086aa5fcf9bee9a5f870dc28da9860a4b6d0092fb905
fetched_at: '2026-06-29T00:11:44.016255+00:00'
page_id: '808478015'
product: rm
source: tdn-rm
title: DCTFWeb - Como chegar no valor da DARF a recolher? Será possível unificar as
  DARF de INSS e IRRF?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=808478015
version: 40
---

## **Conteúdo**

Conteúdonone

## **01. Visão geral**

A **DCTFWeb** chegou com o objetivo de modernizar o cumprimento das obrigações acessórias, diminuindo a ocorrência de erros e aumentando a segurança no que é entregue.

As informações necessárias para gerar a DCTFWeb, são enviadas através do **eSocial** e da **EFD-Reinf**. O sistema recebe as informações, realiza vinculações, calcula o saldo a pagar e, após o envio da declaração, disponibiliza ao contribuinte a emissão do DARF, documento de arrecadação. 

Conforme fluxo de informações na página 10 do Manual de Orientação da [DCTFWeb](https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/declaracoes-e-demonstrativos/DCTFWeb/arquivos/manual-dctfweb-fevereiro-2023.pdf):

Nossa equipe de consultoria de segmentos criou um documento com todos os detalhes sobre a DCTFWeb, acesse e esclareça as suas dúvidas <https://espacolegislacao.totvs.com/dctfweb/>

## **02. Como faço a DCTFWeb no RM?**

A DCTFWeb é o sistema utilizado para centralizar as informações recebidas do e-Social e da EFD-Reinf, além de conciliar automaticamente as informações de outras ferramentas como Per/Dcomp, sistemas de parcelamento, entre outras, para transmiti-las e gerar os documentos de arrecadação, sua geração ocorre a partir das informações prestadas e transmitidas através da escrituração do e-Social e da EFD-Reinf. Assim não existe um processo de geração da DCTFWeb porque não é necessário realizar nenhuma entrega para o governo.

## **03. Como calcular o meu DARF?**

O contribuinte deverá acessar o portal do eCac, emitir as guias para pagamento do imposto e posteriormente acessar o RM para refletir os valores gerados no portal. Os módulos Fiscal e RH irão integrar as informações com o módulo Financeiro e este ficará encarregado de consolidar e calcular o valor final do DARF. Para ajudar no entendimento deste processo destacamos abaixo como é o processo em cada Módulo.

12FOLHA DE PAGAMENTOFOLHA DE PAGAMENTO

A folha de pagamento gera os valores tributados na folha de pagamento conforme enviado ao eSocial através dos eventos S-1200 e S-1210, de acordo com a parametrização realizada nos tipos de lançamentos financeiros: "**2****5-DCTFWeb Folha**" e "**26-Total Guia INSS DCTFWeb 13º Salário**".

Para obter mais detalhes, consulte o TDN   e [Parametrização dos Lançamentos Financeiros](https://tdn.totvs.com.br/display/LRM/Cadastros+Financeiros)

É importante gerar o relatório de conferência antes de realizar a geração do lançamento financeiro, garantindo a compatibilidade entre os valores da folha de pagamento e aqueles gerados pelo eSocial.

Veja detalhes no TDN:  e 

**ATENÇÃO:** Os montantes de retenção previstos na Lei 9.711 serão encaminhados por meio da REINF. Nesse contexto, caso a empresa pretenda deduzir tais valores na folha de pagamento, será necessário acessar tanto a DCTFWeb quanto o setor financeiro para efetuar essa configuração.

**OBSERVAÇÃO:** Qualquer dúvida referente a esse processo deverá acionar o atendimento de Folha de Pagamento.

3FISCALFISCAL

No Fiscal não foram necessárias alterações especificas para atender a DCTFWeb. Basta que as guias sejam integradas com o Financeiro onde o usuário deverá avaliar como serão agrupadas.

A partir de Fevereiro as Retenções e o IR também serão integrados a DCTFWeb através do bloco 40 da [EFD-Reinf](https://tdn.totvs.com/pages/viewpage.action?pageId=506382898), neste caso como tratam-se de tributos cujos Lançamentos Financeiros já existem, basta não executar o processo "[Geração de Guias a partir de Lançamentos Financeiros](https://tdn.totvs.com/pages/viewpage.action?pageId=431679508)" e realizar o agrupamentos das guias diretamente no Financeiro.

**OBSERVAÇÃO:** Qualquer dúvida referente a esse processo deverá acionar o atendimento do Fiscal.

4FINANCEIROFINANCEIRO

Conforme publicado pelo governo, é possível gerar a guia unificada pela DCTFWeb, veja detalhes na [publicação](https://www.gov.br/receitafederal/pt-br/assuntos/noticias/2023/marco/receita-federal-comunica-a-substituicao-de-tributos-da-dctf-pela-dctfweb#:~:text=O%E2%80%AFnormativo%E2%80%AFdefine%20que%2C%20a%20partir%20do%20per%C3%ADodo%20de%20apura%C3%A7%C3%A3o,trabalho%2C%20informado%20no%E2%80%AFeSocial%2C%20passar%C3%A1%20a%20ser%20declarado%20na%E2%80%AFDCTFWeb).

Para os clientes que integram com o produto TOTVS Gestão Financeira, é possível, através do módulo financeiro, parametrizar essa unificação. As instruções detalhadas estão disponíveis no TDN [FIN - Faturas](https://tdn.totvs.com/display/LRM/FIN+-+Faturas).

A partir dos patches mencionados abaixo, o módulo Financeiro possibilita a inclusão de faturas agrupando lançamentos de diferentes classificações tributárias. Essa funcionalidade permite agregar lançamentos faturados com diferentes classificações de tributos, tais como CSLL, PIS, COFINS, Contribuição Social, IRRFPJ, IRRFPF, IRRFLiber, INSSEmpregado, INSSEmpregador, INSSLiber, IRFolhaPag, IRRFFeriasLabore, IRRFRescisaoLabore, IRRF13SalarioLabore, IRRFTotalLabore, INSSaPagarLabore, INSS13SalarioLabore.

Nos casos de diferença de valores, por questão de arredondamento entre o sistema da DCTFWeb e o ERP TOTVS, poderá cadastrar [valores de integração](https://tdn.totvs.com/pages/releaseview.action?pageId=532041706) responsáveis pelo registro desta diferença que será visualizado na edição do vencimento da fatura durante o processo de inclusão.

**Patches**

* 12.1.2302.192
* 12.1.2306.135
* 12.1.2310.001

## **04. Vídeos de demonstração**

Segue abaixo os vídeos de Demonstração relacionados a este processos.
