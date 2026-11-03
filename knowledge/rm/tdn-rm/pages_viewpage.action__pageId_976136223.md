---
content_hash: a02b1251dea15fea4614c25fe73882af3edda84aaba1ce47d2172ff92b5b439e
fetched_at: '2026-06-29T00:12:15.306427+00:00'
page_id: '976136223'
product: rm
source: tdn-rm
title: Registro online padrão AutBank
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=976136223
version: 5
---

# Conteúdo:

Conteúdo:

# 1. Registro online

Esta implementação tem como objetivo preparar o TOTVS Gestão Financeira para utilizar o serviço de registro online de cobrança registrada para os bancos que utilizam o padrão da AutBank.

Bancos homologados para esse padrão: "Banco Crefisa", "Banco b.Uni" e "Daycoval" (a partir da 12.1.2506.199 e 12.1.2510.129).

# 2. Procedimento para configuração

Através do cadastro do Convênio, localizado no menu 'Movimentações Bancárias', é necessário habilitar a opção "Permite registro de boleto online" e definir os parâmetros de acordo com os dados fornecidos pelo banco.

Cards2Modelo de Registro Online v1

* **Permite registro de boleto online:**Define se o convênio permite utilizar o registro de boleto online.
* **Integração com os serviços da AutBank:**Define que o banco utiliza o padrão da AutBank para o registro online de boletos.
* **Ambiente**: Define o ambiente que será feito o registro do boleto no banco.
* **URL do serviço de registro de cobrança**: Deve ser informada a URL do serviço de registro do boleto disponibilizada pelo banco.
* **URL de homologação do serviço de registro de cobrança**: Deve ser informada a URL de homologação do serviço de registro do boleto disponibilizada pelo banco.
* **Usuário:** Usuário de acesso ao sistema autorizador fornecido pelo banco.
* **Senha:** Senha de acesso ao sistema autorizador fornecido pelo banco.

Conforme detalhado no item 3 deste documento, é possível enviar os dados de forma flexível para o banco ao registrar online os boletos. O cadastro do layout do registro online deve ser feito conforme o manual de cobrança online do banco, onde contempla a descrição de cada campo. Exemplos:

Outros exemplos de campos:

* numContaHeader
* campoLivre
* mensagem1
* mensagem2
* mensagem3
* mensagem4
* mensagem5
* codDesconto1
* vlrDesconto1
* txDesconto1
* dataDesconto1
* codDesconto2
* vlrDesconto2
* txDesconto2
* dataDesconto2
* codDesconto3
* vlrDesconto3
* txDesconto3
* dataDesconto3
* codMulta
* dataMulta
* txMulta
* vlrMulta
* codMora
* dataMora
* txMora
* vlrMora
* possuiAgenda
* tipoAgendamento
* criterioDias
* numDiasAgenda
* codIndice
* indPagtoParcial
* qtdPagtosParciais
* tipoVlrPercMinimo
* vlrPercMinimo
* tipoVlrPercMaximo
* vlrPercMaximo
* tipoAutRecDivergente
* codColigadaContaCreditar
* codAgenciaContaCreditar
* numContaCreditar
* **codColigada**(Campo obrigatório para utilização do serviço de cancelamento e alteração de Data de Vencimento - **Não é a coligada do RM**)
* **cobrarTarifa**(Campo obrigatório para utilização do serviço de cancelamento e alteração de Data de Vencimento)
* **formaCadastramento** (Campo obrigatório para utilização do serviço de cancelamento)

# 3. Customização de dados no registro online

Pode ser utilizado o [Cadastro de Layout do Registro Online](https://tdn.totvs.com/display/LRM/Layout+Registro+Online), para enviar dados de forma flexível para o registro online dos boletos para o banco. Para isso deve ser feito o [Cadastro de associação de fórmulas e campos do registro online](https://tdn.totvs.com/pages/viewpage.action?pageId=421388759) de acordo com o manual de cobrança online do banco.

**IMPORTANTE**:

* Para os campos de valores ou percentual deve seguir o formato de acordo com o manual disponibilizado pelo banco. Ao definir um valor fixo ou formula deve ser retornado um string com o separador decimal '.' (ponto).   
  Exemplo:   
  2.49 (com duas casas decimais)
* Para campos destinados a data deve ser utilizado o separador '/' (barra).  
  11/08/2025 (data no formato DD/MM/YYYY)
