---
content_hash: 6f4058433055b18d7233dd9cde82aef4e7e0d1090502d47ebba1b91d59c7680f
fetched_at: '2026-06-29T00:11:59.630051+00:00'
page_id: '874583579'
product: rm
source: tdn-rm
title: DT Registro online Banestes
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Registro+online+Banestes
version: 9
---

## **01. VISÃO GERAL**

Este recurso visa preparar o TOTVS Gestão Financeira para utilizar o serviço de registro online da carteira de cobrança registrada do Banco Banestes via webservice.

Disponível no release 12.1.2406 ou superior. Recomendamos utilizar sempre o último patch.

[Baixe aqui o manual do banco Banestes.](https://www.banestes.com.br/downloads/arquivos/layout_web_service.pdf)

## **02. CONFIGURAÇÃO**

No cadastro do convênio, na aba 'Registro Online'deve ser marcado a opção "Permite registro de boleto online"*.*

* **URL do serviço de registro do boleto**: Deve ser informada a URL do serviço de registro do boleto disponibilizada pelo Banco
  + [https://api.banestes.b.br/cobranca/v3/MetodosWebServerImp](https://api.banestes.b.br/cobranca/v2/MetodosWebServerImp)
* **URL de homologação do serviço de registro do boleto**: Deve ser informada a URL de homologação do serviço de registro do boleto disponibilizada pelo Banco
  + [https://sandbox.banestes.b.br/cobranca/v3/MetodosWebServerImp](https://sandbox.banestes.b.br/cobranca/v2/MetodosWebServerImp)
* **Usuário e senha**: Usuário e senha fornecido pelo banco para autenticar a integração

## **03. LAYOUT**

Para enviar dados de forma flexível para o registro online dos boletos para o banco, devem ser criados os campos, primeiramente via anexo "[Layout Registro Online](https://tdn.totvs.com/display/LRM/Layout+Registro+Online)" disponível no cadastro de Bancos e Agências. Os campos devem ser criados conforme manual de cobrança do Banestes. Esses campos devem ser associados a fórmulas ou valores fixos, via anexo "[Associação do Layout do Registro Online](https://tdn.totvs.com/pages/viewpage.action?pageId=421388759)" no cadastro do convênio. Alguns exemplos abaixo:

titulo.CONTA\_CORRENTE

titulo.IDENTIFICADOR\_RESPONSAVEL\_EMITIR\_BOLETO

titulo.IDENTIFICADOR\_RESPONSAVEL\_DISTRIBUIR\_BOLETO

titulo.PERCENTUAL\_MORA\_ATRASO

titulo.PERCENTUAL\_MULTA\_ATRASO

titulo.inscricaoPagador.NOME

titulo.inscricaoSacadorAvalista.BAIRRO

titulo.inscricaoSacadorAvalista.CEP

titulo.PARCELAS\_ENTRADA.VALOR\_TITULO

titulo.PERCENTUAL\_MORA\_ATRASO

titulo.PERCENTUAL\_MULTA\_ATRASO

titulo.DATA\_LIMITE\_PAGAMENTO

titulo.PARCELAS\_ENTRADA.VALOR\_DESCONTO

titulo.PARCELAS\_ENTRADA.DATA\_DESCONTO

**Importante:**

* Por padrão, o campo responsável por indicar o responsável por emitir o Boleto é 2 (Cliente). Caso o responsável seja o banco, é necessário enviar no campo "titulo.IDENTIFICADOR\_RESPONSAVEL\_EMITIR\_BOLETO" via associação de layout o valor 1, no qual representa o banco conforme o manual do banco.

* Por padrão, o campo responsável por indicar o responsável por distribuir o Boleto é 2 (Cliente). Caso o responsável seja o banco, é necessário enviar no campo "titulo.IDENTIFICADOR\_RESPONSAVEL\_DISTRIBUIR\_BOLETO" via associação de layout o valor 1, no qual representa o banco conforme o manual do banco.

* O banco espera como juros um percentual mensal, como o TOTVS Gestão financeira trabalha com juro valor fixo ou percentual diário, o que será enviado para o banco será o percentual de juros ao dia do boleto vezes trinta.  Caso queira enviar um valor diferente é possível utilizando a campo da associação de layout "titulo.PERCENTUAL\_MORA\_ATRASO". O formato deve ser 2 casas e 2 decimais separado por ponto. Ex: 1.00

* O banco espera como multa um percentual fixo, como o TOTVS Gestão financeira trabalha com multa valor fixo ou percentual diário, o que será enviado para o banco será o percentual de multa ao dia do boleto vezes trinta.  Caso queira enviar um valor diferente é possível utilizando a campo da associação de layout "titulo.PERCENTUAL\_MULTA\_ATRASO". O formato deve ser 2 casas e 2 decimais separado por ponto. Ex: 2.00

* O sacador/avalista não é obrigatório ser enviado, caso queira enviar é necessário cadastrar os campos abaixo na associação de layout registro online.
  + titulo.inscricaoSacadorAvalista.TIPO\_INSCRICAO
  + titulo.inscricaoSacadorAvalista.NUMERO\_INSCRICAO
  + titulo.inscricaoSacadorAvalista.NOME
  + titulo.inscricaoSacadorAvalista.LOGRADOURO
  + titulo.inscricaoSacadorAvalista.BAIRRO
  + titulo.inscricaoSacadorAvalista.CIDADE
  + titulo.inscricaoSacadorAvalista.UF
  + titulo.inscricaoSacadorAvalista.CEP

* A data do desconto por padrão é a data de vencimento, caso queira definir um outra data, é necessário cadastrar o campo "titulo.PARCELAS\_ENTRADA.DATA\_DESCONTO" e definir uma data no formato "yyyy-mm-dd"

* Caso queira definir uma data limite de pagamento do boleto, será necessário cadastra o campo "titulo.DATA\_LIMITE\_PAGAMENTO" e definir uma data no formato "yyyy-mm-dd"
