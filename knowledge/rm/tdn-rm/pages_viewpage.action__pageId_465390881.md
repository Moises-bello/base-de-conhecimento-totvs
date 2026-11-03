---
content_hash: ebd9478782821cb4304134fe2e052b768bc60242c0a5e2ed71a8ab24e9c46801
fetched_at: '2026-06-29T00:10:15.952644+00:00'
page_id: '465390881'
product: rm
source: tdn-rm
title: DT Securitização - Contrato de Securitização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=465390881
version: 21
---

| **Linha de Produto** | **RM** |
| --- | --- |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Incorporação |
| **Rotina:** | Cadastro de Contrato de Securitização - ImbVendaContratoSecuritizacaoData |
| **Cadastros Iniciais:** | N.A. |
| **Parâmetro(s):** | N.A. |
| **Pontos de Entrada:** | N.A. |
| **Tickets relacionados:** | N.A. |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | TINPAD001-5404 / TINPAD001-5406 / TINPAD001-5420 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Tabelas Utilizadas:** | XSECURITIZACAO / XSECURITIZACAOCOMPL |
| **Sistema(s) Operacional(is):** | Windows |

A securitização é o processo realizado pelas companhias securitizadoras que adquirem créditos imobiliários para lastrearem títulos imobiliários (Certificados de Recebíveis Imobiliários – CRIs) que serão negociados no mercado de capitais. Os certificados de recebíveis Imobiliários são títulos de crédito nominativos, escriturais e transferíveis, lastreados em créditos imobiliários. Estão previstos na Lei 9514/97, que disciplina o sistema de financiamento imobiliário.

Securitizar é transformar direitos creditórios - como os provenientes das vendas a prazo nas atividades comerciais, financeiras ou prestação de serviços - em títulos negociáveis no mercado. O Certificado de recebível imobiliário, assim, é uma securitização de direitos creditórios originados nos financiamentos imobiliários. A securitização pode ser estruturada em diferentes formatos. Em uma possível forma, o processo se inicia com um financiamento imobiliário, em que determinado cliente assume a obrigação de uma dívida. Essa dívida origina direitos creditórios à instituição financiadora. Em seguida, cria-se uma estrutura de securitização, como uma companhia securitizadora (os Fundos de Investimento em Direitos Creditórios também têm sido utilizados).

Essa funcionalidade tem por objetivo securitizar títulos a receber, provenientes de contratos de vendas ou alugueis do TCGI.   
- O contrato de securitização poderá contemplar títulos a receber de vários contratos de venda.  
- O campo vencimento, preenchido determina que irá gerar o lançamento com o valor total do contrato de securitização, quando o contrato for efetivado, os dados utilizados para a geração do lançamento a receber da securitizadora virão do campo "Parâmetro de Integração Financeira - Securitização". A Situação após o processo: Securitizado  
- Os títulos a receber provenientes dos contratos de venda que foram securitizados, poderão sofrer alteração da sua situação, caso haja a necessidade, as situações existentes hoje é: securitizado, repasse em atraso, recompra e devolução).

- Para que os títulos modifiquem a sua situação temos os seguintes processos e as descrições da aplicação de cada um deles dentro do sistema:  
  
**1 - Apuração Mensal Lançamentos em Atraso:**  
     - Situação após o processo: Repasse Em Atraso  
     - O objetivo do processo "Apuração Mensal Lançamentos em Atraso" é permitir que os títulos que se encontram em atraso possam ser recomprados pela incorporadora, ainda que já tenham sido enviados boletos para os compradores responsáveis pelo pagamento com informações bancarias de boleto da securitizadora. Essa funcionalidade permite manter os títulos em atraso sobre controle da incorporadora, sendo devolvidos pela securitizadora.   
    - Caso o título recomprado por motivo de atraso, já tenha sido enviado a banco pela securitizadora, a incorporadora pode efetuar o processo de "Apuração Mensal dos Lançamentos em Atraso" e, em seguida, utilizar o processo "Devolução do Valor Pago a Securitizadora".  
    - Este processo utiliza do campo "Parâmetro de Integração Financeira - Apuração" para preenchimento dos dados necessários na geração do título a pagar para a securitizadora.  
  
**2 - Devolução:**  
     - Situação após o processo: Devolução  
     - A devolução será utilizada para gerar título a receber da securitizadora, com o intuito de aguardar o recebimento de um título que foi recomprado pelo processo de apuração mensal, mas que quem irá receber o mesmo ainda será a securitizadora e assim que receber, irá pagar a incorporadora.  
      - Este processo utiliza do campo "Parâmetro de Integração Financeira - Devolução" para preenchimento dos dados necessários na geração do título a receber da securitizadora.  
  
**3 - Recompra:**  
    - Situação após o processo: Recompra  
    - A "Recompra de Títulos Securitizados" traz uma maior flexibilidade de gestão da carteira dos títulos securitizados, tendo como objetivo a recompra (reintegração) dos títulos para a carteira de recebíveis da incorporadora, nos casos em que julgar necessário e compensatório financeiramente.  
    - Este processo utiliza do campo "Parâmetro de Integração Financeira - Recompra" para preenchimento dos dados necessários na geração do título a pagar para a securitizadora.

No TOTVS Incorporação será possível cadastrar contratos de securitização. A funcionalidade está localizada na Aba de Recebíveis→ Contrato de Securitização.

**Contrato de Securitização**

Os seguintes campos estão disponíveis na aba Identificação:

* **Identificador**: Código incremental do contrato
* **Origem:** **1** - Aluguel / **2** - Venda
* **Contrato**: Número do contrato de securitização
* **Status**: Status do Contrato que pode ser "Em aberto", "efetivado", "cancelado" ou "encerrado".
* **Coligada** **Proprietária**: Poderá escolher qual a coligada será responsável por receber as cobranças de securitização.
* **Descrição**: Um campo para descrever os contratos de securitização.
* **Data do Contrato**: Data inicial do contrato.
* **Data efetivação**: Data da efetivação do contrato. É preenchida através do processo de efetivação.
* **Data Cancelamento**: Data de cancelamento do contrato, preenchida através do processo de cancelamento.

Dados para geração do lançamento da antecipação

* **Código Securitizadora**: Deverá ser informado o cliente/fornecedor que representa a securitizadora.
* **Parâmetro de Integração Financeira**: Informe os parâmetros financeiros para a geração dos lançamentos de securitização.
* **Valor Securitizado**: O valor securitizado é a soma dos valores das parcelas que serão geradas.
* **Valor antecipado**: Caso seja pago um valor pela securitizadora a empresa (incorporadora), este valor deve ser preenchido.
* **Data de Vencimento**: Data de vencimento do lançamento de antecipação a ser gerado.

O parâmetro de integração financeira é cadastrado em um outro menu, também na aba de recebíveis. Ao criar o parâmetro, a origem cadastrada será "Securitização".

Tipo de Responsável pela cobrança: Poderá ser escolhido o responsável pela securitização sendo a Securitizadora ou Empresa. Caso a escolha for a Securitizadora, os seguintes campos abaixo estarão disponíveis para a geração dos lançamentos:

* Conta Caixa
* Convênio

CardsCard1Permissões

**Permissões de Perfil**

As permissões de perfil do contrato de securitização estão no Produto Globais → Aba Segurança → Perfis → Sistema Incorporação.

Card2Anexos e Processos

**Anexos e Processos de Securitização**

**Anexos**

Na visão dos contratos de securitização podemos visualizar via anexo, os lançamentos do contrato que serão securitizados.

**Processos**

Para incluir os lançamentos ao contrato de localização basta acessar o processo "Inclusão de Lançamentos no Contrato de Securitização".

Na tela acima, será possível escolher quais vendas terão seus lançamentos securitizados. Para selecionar um empreendimento por completo, basta fazer um filtro de acordo com as informações do empreendimento e então, selecionar as vendas correspondentes.

Esta segunda tela, ao avançar serão mostrados todos os lançamentos correspondentes às vendas selecionadas na tela anterior. Aparecerão todos os lançamentos em aberto do tipo "A Receber". Abaixo dos lançamentos, existe o botão "Calcular Valor Securitizado" que trará a valor presente os valores somados de todos os lançamentos selecionados.

**Observação:** Caso aparecer mais de 1000 registros na tela acima, deverá ser configurado nos Serviços globais a quantidade de registros para o Dataserver (Servidor de Aplicação) FINLANDATA conforme imagem abaixo:

O campo Data Líquido trará a data do contrato de securitização automaticamente. Caso desejar trocar ou adicionar mais lançamentos, basta clicar no botão "Limpar".

O processo é executado com sucesso.

Os lançamentos securitizados aparecerão no anexo do contrato de securitização.

Repare que o campo "Valor securitizado" trará automaticamente o valor calculado do processo de inclusão de lançamentos.

**Observação:** Os lançamentos financeiros podem ser associados apenas a um contrato de securitização. Caso existir mais de um contrato para a mesma venda, outros lançamentos deverão ser selecionados.

**Efetivação de contrato**

O processo de efetivação do contrato irá bloquear as alterações no contrato, não será possível alterar os lançamentos associados, ou as datas do contrato.

Após a execução do processo. As datas e campos do contrato ficaram bloqueadas.

Card3Campos Complementares

**Campos complementares de Securitização**

Os campos complementares de securitização estão disponíveis no Menu Venda → Agrupamento Cadastros → Campos Complementares → Contrato de Securitização.

Os campos complementares aparecerão na base correspondente do contrato de securitização
