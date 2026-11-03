---
content_hash: d984c352fee346b182ebec6f858226a80ca98156aedd2cd302832d27e90412b8
fetched_at: '2026-06-29T00:08:39.818489+00:00'
page_id: '286022051'
product: rm
source: tdn-rm
title: RMFIN00005_E_Funcional_Emissão/Geração de Boletos utilizando dados de conta
  de cobrança (conta transitória)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286022051
version: 4
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Financeira |
| **Versões:** | 12.1.18 |
| **Ocorrência:** | N/A |
| **Ambiente:** | RM |
| **Passo a passo:** | N/A |
| **Observações:** | N/A |

## Objetivo

Na geração e emissão de um boleto, buscar os dados para composição do nosso número/código de barras da conta transitória (conta de cobrança) , sendo que a baixa/retorno ocorrerá na conta normal (conta movimento). 

## Definição da Regra de Negócio

Eu, como analista financeiro, preciso utilizar uma conta transitória (conta de cobrança) para emissão/geração de boletos, sendo que a baixa ocorrerá na conta normal (conta movimento). Essa conta transitória precisa estar relacionada ao convênio, pois pode haver mais de uma conta cobrança associada à mesma conta corrente no banco.

1. **Necessidade prática**:

Algumas empresas por exemplo do ramo de construção/incorporação iniciam o empreendimento e conseguem empréstimos/financiamentos junto aos bancos, os recursos destes empréstimos serão liberados de acordo com o recebimento da carteira de cobrança deste empreendimento. Com a separação em conta de cobrança, os bancos conseguem separar a movimentação, identificando os valores  para que possa realizar o controle dos seus processos internos vinculados ao financiamento. 

Atualmente, as empresas que necessitam deste tipo de conta configuram o layout de remessa de cobrança para envio dos dados corretamente informando a conta de cobrança (conta transitória), porém se necessitar emitir/gerar um boleto os dados existentes no convênio são referentes à conta movimento e desta forma os dados serão gerados impressos incorretamente, por este motivo existe a necessidade de gerar/emitir o boleto buscando os dados da conta de cobrança (conta transitória).

24
incomplete
**Critérios de aceitação**:

* Para um convênio onde a conta transitória for utilizada, ao gerar o nosso número e o código de barras, os dados utilizados deverão ser da respectiva conta transitória.
* Deverá ser disponibilizada a documentação desta funcionalidade: documento técnico e help.
* As equipes devem ser capacitadas na nova funcionalidade (video how to).
* Deverá ser disponibilizado na versão 12.1.18.

25
incomplete
**Funcionamento deste tipo de conta descrito pelo banco:**

De: Implantação\_ItauEmpresas\_Cash <Implantacao\_ItauEmpresas\_Cash@[itaubba.com](http://itaubba.com)>  
Data: 19 de outubro de 2015 07:24  
Assunto: RENATA EMPREENDIMENTO IMOBILIARIO LTDA -COBRANÇA CONVENIADA -ID 156973 [£DA010716\_4229635 - 2938260995]  
Para: "derlane@[bspar.com.br](http://bspar.com.br)" <derlane@[bspar.com.br](http://bspar.com.br)>  
Cc: Luciana Reis De Vasconcelos Martins <luciana.martins@[itaubba.com](http://itaubba.com)>, Implantação Tecnica\_ItauEmpresas\_Cash <ImplantacaoTecnica\_ItauEmpresas\_Cash@[itaubba.com](http://itaubba.com)>

Prezados,

Bom dia!  
Informamos que o cadastro da COBRANÇA CONVENIADA foi realizado. O produto já está liberado em ambiente de teste/produção  
Abaixo as orientações referentes ao cadastro:

EMPRESA: RENATA EMPREENDIMENTO IMOBILIARIO LTDA  
CONTA COBRANÇA OU CONVÊNIO: 2938/26099-5  
CONTA MOVIMENTO: 0366/92010-6  
NÚMEROS DAS CARTEIRAS CONTRATADAS: 109;112;156;157;158

Através da **CONTA COBRANÇA** OU CONVÊNIO serão transmitidos os arquivos, recebimento dos retornos e trânsito dos boletos. Ressaltamos que a mesma deverá ser informada no arquivo remessa. Ela é transitória e por isso, não aceita nenhum tipo de movimentação (débito ou crédito).  
Através da **CONTA MOVIMENTO** serão efetuados os créditos da movimentação de títulos e débitos das tarifas, conforme prazo negociado.  
As contas estão disponíveis no Itaú Empresas na Internet. O Representante Legal deverá liberar o acesso aos demais Operadores que atuarão no produto, assim como os módulos “Cobrança de Títulos” e “Transferência de Arquivos”.

Layout de Arquivo – CNAB 400

Informamos abaixo as posições do arquivo remessa que deverão ser preenchidas com o número de agência e **conta de cobrança** conveniada. É possível obter o lay out de cobrança CNAB 400 na rota do Itaú Empresas na Internet: Outras Informações, Download Center, Manuais de Layouts de Intercambio de Arquivos.

   
REGISTRO HEADER DE ARQUIVO  
AGÊNCIA AGÊNCIA MANTENEDORA DA CONTA Posição: 027 à 030  
CONTA NÚMERO DA CONTA CORRENTE DA EMPRESA Posição: 033 à 037  
DAC DÍGITO DE AUTO CONFERÊNCIA AG/CONTA EMPRESA Posição: 038 à 038  
REGISTRO DETALHE (OBRIGATÓRIO)  
AGÊNCIA AGÊNCIA MANTENEDORA DA CONTA Posição: 018 à 021  
CONTA NÚMERO DA CONTA CORRENTE DA EMPRESA Posição: 024 à 028  
DAC DÍGITO DE AUTO CONFERÊNCIA AG/CONTA EMPRESA Posição: 029 à 029

Estamos à disposição para orientações referentes ao arquivo de cobrança, layout, testes, processamento, remessa/retorno. Caso seja necessário suporte técnico quanto ao desenvolvimento ou envio do primeiro arquivo, pedimos que entre em contato com o Rodrigo Canjerana através do email : [ImplantacaoTecnica\_ItauEmpresas\_Cash@itaubba.com](mailto:ImplantacaoTecnica_ItauEmpresas_Cash@itaubba.com)  
Caso haja interesse em efetuar protestos nesta Cobrança, será necessário que providencie a devolução da Declaração de Protestos, de acordo com as instruções enviadas anteriormente .  
À disposição para eventuais dúvidas.  
Atenciosamente,  
Daniela Cristina Bravin | Serviços Cash - Implantação Empresas  
Itaú Empresas  
Tel.: 4090.1222 - Opção 1 (Conta Corrente, Cobrança e Pagamentos) Opção: 2 (Implantação de novos Serviços de Pagamentos e Recebimentos)  
[Implantacao\_ItauEmpresas\_Cash@itaubba.com](mailto:Implantacao_ItauEmpresas_Cash@itaubba.com)

# Impacto no sistema

O impacto no sistema será na geração do nosso número e código de barras. Na geração/emissão do boleto quando um convênio possuir os dados para conta cobrança (conta transitória) informados, o sistema deverá considerar estes campos para geração do nosso número e código de barras.

Conforme detalhamento acima do banco, os campos necessários para a conta cobrança (conta transitória) são:

Agência de cobrança (conta transitória)

Conta corrente para cobrança (conta transitória)

Dígito da AG/Conta de cobrança (conta transitória)

Na geração/emissão dos boletos o nosso número/código de barras deverá levar em consideração os dados acima para composição.

# Cadastros

No cadastro do convênio disponibilizar uma nova aba por exemplo "Conta cobrança (conta transitória)" e disponibilizar os campos:

Agência de cobrança (conta transitória)

Conta corrente para cobrança (conta transitória)

Dígito da AG/Conta de cobrança (conta transitória)
