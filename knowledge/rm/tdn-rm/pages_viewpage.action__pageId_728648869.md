---
content_hash: b0600a97ffcd89fb9c85ce539f194e3b476a639d104c279d3bb4ab1f5b55c1e1
fetched_at: '2026-06-29T00:11:27.674518+00:00'
page_id: '728648869'
product: rm
source: tdn-rm
title: Release 12.1.2306 - TOTVS Gestão de estoque, compras e faturamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=728648869
version: 10
---

**Legislações**

* **NF-e - NT 2022.003 - Chave de acesso das notas****referenciadas**

Cada NF-e pode ter referência com vários outros documentos fiscais devido a vários processos como: devolução, complemento de imposto, exportação, etc. Estas referências são declaradas através do grupo <**NFref**> que permite até 500 referências por nota. Quando a nota referenciada é do Modelo 55, sua chave de acesso deve ser declarada no campo <**refNFe**> do XML.

Contudo, ao declarar a chave de acesso original da NF-e referenciada, o destinatário conseguirá consultá-la através da chave de acesso que foi declarada, gerando assim uma quebra de sigilo na operação fiscal.

Para resolver este problema a **NT 2022.003** criou a possibilidade de declarar a nota referenciada, através do campo <**refNFeSig**>, suprimindo a parte do código numérico da chave de acesso. Assim o destinário não conseguirá consultar os dados da nota referenciada.

Veja no sistema, as evolução realizadas para permitir zerar o código numérico.

* **EFD-REINF - Natureza de Rendimento**

Conforme definido no *Anexo I dos leiautes da EFD-Reinf - Tabelas versão 2.1.1*, as retenções de imposto de renda decorrentes do rendimento de trabalho devem ser enviadas pelo eSocial. No entanto, para situações específicas em que não seja possível fazer o envio pelo eSocial, a EFD-Reinf deve ser a escrituração utilizada para essa apuração.

Nestes casos, as retenções devem ser classificadas com um código da Natureza do Rendimento, conforme lista preestabelecida pela Receita Federal do Brasil.

Informações sobre o cadastro de natureza de rendimento:

Saiba como informar a natureza de rendimento no movimento:

* **EFD-REINF - Registro 1600**

Para atender os ajustes da EFD ICMS IPI, referente ao registro 1600, onde deve-se  informar todas as operações de vendas, recebidas através de meio de pagamentos eletrônicos, como Cartões de débito, crédito, de loja (private label), pix, boleto, transferência de recursos, transações eletrônicas do Sistema de Pagamento Instantâneo e demais instrumentos de pagamento eletrônicos e **identificar também a Instituição Financeira e o intermediador da transação**.

Informações sobre o cadastro de meio de pagamento (vide aba: Outros Dados):  

**Melhorias**

* Foram adicionados **botões para selecionar e remover a seleção de todas filiais/coligadas e tipos de movimentos** no assistente de cotação, melhoria disponível a partir da 12.1.2302.

* **Percentual de Comissão dos Funcionários 3 e 4**

A partir desta versão está disponível o cadastro de comissões dos funcionários 3 e 4, como já existia nas versões anteriores para os funcionários 1 e 2. 

Segue documentação
