---
content_hash: 26d56cfe7d71d4c884c481c2116841e248c6fdab274b69fb3a830e6ad8600ccb
fetched_at: '2026-06-29T00:09:18.545849+00:00'
page_id: '421388721'
product: rm
source: tdn-rm
title: FIN - Remessa de Custódia de Cheques
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388721
version: 8
---

O processo Custódia de Cheque a Bancos consiste em repassar a guarda dos cheques recebidos às Instituições Financeiras, que assumem a responsabilidade pelos mesmos, depositando-os e compensando-os na data correta. A transação ocorre por envio de arquivos de remessa e de retornos, garantindo segurança e agilidade na gestão financeira. O processo Custódia de Cheques a “Filiais” não requer geração de arquivos de remessa. Trata-se de controle manual dos Cheques Custodiados.

Exemplo:

A empresa tem N filiais e a gestão necessita controlar o recebimento de cheques de suas filiais.

* Cada filial fará o envio físico desses cheques e para controle interno fará o processamento no RM de "Custódia por Filial".
* A matriz mediante recebimento do cheque físico fará o processamento no RM da "Custódia por Banco" de todos os cheques recebidos das filiais para o banco credenciado.

Para um serviço de Custódia de Cheques é necessário firmar um Convênio específico entre o Banco e o Cliente.

**Entidades participantes do Processo**

* Conveniado: Pessoa física ou jurídica, que tem um contrato para utilização dos serviços de Custódia de Cheques de um Banco.
* Banco Conveniado: Banco que disponibiliza os serviços de Custódia de Cheques para o Cliente.
* Banco do Emitente:  Banco do Emitente do Cheque.

**Etapas do Processo**

Atualização dos cadastros: Bancos, Agencia, Conta Corrente, Conta Caixa e Convenio

O Conveniado remete os cheques para depósito à vista e/ou pré-datados a serem custodiados no Banco Conveniado, acompanhado de instruções para as ações (comandos) que o Banco deve tomar.

O Banco Conveniado, de posse das informações e instruções, envia os cheques para compensação na Data para Depósito, e disponibiliza o crédito, conforme contrato de prestação de serviços firmado entre o Banco e o Conveniado.

O Banco fornece informações ao Conveniado sobre os cheques compensados e devolvidos, bem como sobre valores e taxas relativas às operações de empréstimo (desconto), para que o mesmo possa conferir a sua Carteira de Cheques Custodiados no Banco.

**Cadastro de Remessa Custódia de Cheque**

O cadastro da remessa é realizado através do menu Movimentações Bancárias | Integração Bancária | Cadastro Bancário | Cadastro Custódia Cheque ou durante o processo Remessa de Custódia.

**Procedimento:**

Acesse o menu Movimentações Bancárias / Integração Bancária / Remessa Bancária / escolha o Processo e inclua uma nova.  
Os dados solicitados são requeridos nos respectivos arquivos de remessa.
