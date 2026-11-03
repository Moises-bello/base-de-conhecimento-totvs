---
content_hash: e1f9a1038e91a678c15e3465ee6abd8eb486e294c26b726b097ad03fb31cff15
fetched_at: '2026-06-29T00:05:52.786463+00:00'
page_id: '1060223682'
product: rm
source: tdn-rm
title: Faturamento no padrão TISS (Troca de Informação de Saúde Suplementar)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1060223682
version: 5
---

tissvisaoVisão Geral

Este documento tem por finalidade explicar o faturamento eletrônico no padrão TISS (Troca de Informação de Saúde Suplementar), definido pela ANS (Agencia Nacional de Saúde Suplementar), referente aos Prestadores de Saúde utilizado pelos Convênios (Operadoras de Saúde) .

O Padrão TISS abrange as trocas dos dados de atenção à saúde prestada ao beneficiário de Plano Privadode Assistência à Saúde, gerados na rede de **Prestadores** de Serviços de Saúde da **Operadora** de planos privados de assistência à saúde (Convênios).

Entende-se como rede de prestadores de serviços de saúde da operadora de planos privados de assistência à saúde: (RN 501)

* Rede de serviços de saúde contratada, referenciada ou credenciada, de forma direta ou indireta; e
* Rede própria da operadora; de entidade ou empresa controlada pela operadora; de entidade ou empresa controladora da operadora e profissional assalariado ou cooperado da operadora.

**Trocas de informações estabelecidas no Padrão TISS -****Entre operadoras e prestadores de serviços de saúde**

Entre operadoras e prestadores de serviços de saúde, os processos padronizados para troca eletrônica de implantação **obrigatória** são:

- Cobrança de serviços de saúde;

- Autorização de serviços (somente a mensagem de lote de anexos);

- Comunicação de internação ou alta do beneficiário; **(obrigatório a partir da versão 4.03.00)**

- Demonstrativos de retorno;

- Recurso de glosas;

Os processos padronizados para troca eletrônica de implantação **opcional** são:

- Verificação de elegibilidade;

- Autorização de procedimentos (exceto a mensagem de lote de anexos);

- Envio e recebimento de documentos.

**Resumo das mensagens no Padrão TISS – Origem da mensagem Prestador**

|  |  |
| --- | --- |
| **Nome da mensagem no**  **Schema TISS** | **Descrição** |
| LoteGuias | Apresentação de cobrança de consultas, SP/SADT, resumo de internação, honorários e odontologia. |
| LoteAnexos | Apresentação do anexo de situação inicial de odontologia e solicitação de autorização de tratamento de quimioterapia, radioterapia e OPME. |
| SolicitaçãoDemonstrativoRetorno | Solicitação de demonstrativo de análise de conta ou demonstrativo de pagamento. |
| SolicitaçãoStatusProtocolo | Solicita informação de lote de cobrança ou documento recebido pela operadora. |
| SolicitacaoStatusRecursoGlosa | Solicita informação sobre recurso de glosa enviado pelo prestador à operadora. |
| SolicitaçãoProcedimento | Solicitação de autorização de serviços de SP/SADT, internação, prorrogação de internação e tratamento em odontologia. |
| SolicitaStatusAutorização | Solicita status sobre pedido de autorização recebido pela operadora. |
| VerificaElegibilidade | Solicita informação sobre a elegibilidade de um beneficiário da operadora. |
| CancelaGuia | Envia solicitação de cancelamento de lote de guias, guias ou recurso de glosa. |
| ComunicaçãoInternação | Envia comunicado de internação ou alta de um beneficiário. |
| RecursoGlosa | Envia recurso sobre glosa ocorrida em um lote ou em guias do prestador. |
| EnvioDocumentos | Envia documentos complementares para a solicitação, autorização, cobrança e/ou recurso de glosa de procedimentos/itens assistenciais. |

processosTissProcessos Padronizados TISS

Os processos padronizados pela TISS, utilizados pelo Prestador de Serviços de Saúde são:

listaProcessosTisscobrancaTissProcesso de cobrança de serviços de saúde

# Processo de cobrança de serviços de saúde

Através desse processo o prestador de serviços de saúde envia à operadora a cobrança dos serviços realizados. Para tanto, é necessário identificar o beneficiário, o prestador solicitante e executante e os procedimentos/itens assistenciais envolvidos. Podem ser necessários ainda esclarecimentos quanto à situação de saúde do beneficiário que deu origem  
ao atendimento realizado e cobrado.

**Cobrança de guias:** é a mensagem do prestador para a operadora de um lote de cobrança dos serviços de saúde realizados.

**Recebimento de lote de cobrança:** é a mensagem da operadora para o prestador com um protocolo de recebimento do lote de cobrança dos serviços de saúde enviado pelo prestador.

**Solicitação de status de protocolo:** é a mensagem do prestador para a operadora solicitando a situação do protocolo de um lote ou documento enviado anteriormente.

**Situação do protocolo:** é a mensagem da operadora para o prestador com a situação de um protocolo com todas as guias contidas neste.

**Cancelamento de guia:** é a mensagem do prestador para a operadora que solicita o cancelamento de um lote de guias, guias ou recurso de glosa enviados anteriormente.

**Recibo do cancelamento de guia:** é a mensagem da operadora para o prestador com a confirmação, ou não, do cancelamento de um lote de guias, guias ou recurso de glosa.

demonstrativosRetornoProcesso de emissão de demonstrativos de retorno

# Processo de emissão de demonstrativos de retorno

Através desse processo o prestador de serviços de saúde solicita os demonstrativos de pagamento e/ou análise de conta enviados à operadora.  
Para tanto, é necessário identificar o beneficiário, o prestador executante e os procedimentos/itens assistenciais envolvidos.

**Solicitação de demonstrativo de retorno:** é a mensagem do prestador para a operadora solicitando o demonstrativo de pagamento ou o demonstrativo de análise de conta de um lote de cobrança enviado. O prestador deve informar o número do protocolo, gerado pela operadora, de recebimento do lote de cobrança de guias.

**Demonstrativos de retorno:** é a mensagem da operadora para o prestador enviando o demonstrativo solicitado ou a informação que o demonstrativo ainda não está disponível.

recursoGlosaProcesso de recurso de glosa

# Processo de recurso de glosa

Esse processo é utilizado quando o prestador recorre de glosas aplicadas pela operadora a um ou mais procedimentos/itens assistenciais apresentados na conta. Para tanto, é necessário identificar o beneficiário, o prestador executante e os procedimentos/itens assistenciais envolvidos. Podem ser necessários ainda esclarecimentos quanto à situação de saúde do beneficiário que deu origem ao atendimento realizado e recursado.

**Recurso de glosa:** é a mensagem do prestador para a operadora questionando a aplicação de uma glosa em sua cobrança.

**Recebimento do recurso de glosa:** é a mensagem da operadora para o prestador com um protocolo de recebimento do recurso de glosa enviado pelo prestador.

**Solicitação de status de recurso de glosa:** é a mensagem do prestador para a operadora solicitando resposta a um recurso de glosa enviado anteriormente.

**Resposta ao recurso de glosa:** é a mensagem da operadora para o prestador acatando, ou não, o recurso de glosa ou, caso em análise, enviando um novo protocolo do recebimento do recurso.

comunicacaoAltaProcesso de comunicação de internação ou alta de beneficiário

# Processo de comunicação de internação ou alta de beneficiário

Nesse processo ocorre a comunicação sobre a internação ou alta do beneficiário. Para tanto, é necessário identificar o beneficiário.

**Comunicação de internação/alta:** é a mensagem do prestador para a operadora com a informação da data de internação ou alta de um beneficiário.

**Recibo de comunicação:** é a mensagem da operadora para o prestador de recebimento da comunicação de internação ou alta de um beneficiário.

envioDocProcesso de envio e recebimento de documentos

# Processo de envio e recebimento de documentos

Através desse processo o prestador de serviços de saúde encaminha documentos que possam ser necessários para os processos de solicitação, autorização, cobrança e/ou recurso de glosa de procedimentos/itens assistenciais.

**Envio de documentos:** é a mensagem do prestador para a operadora encaminhando os documentos.

**Recebimento de documentos:** é a mensagem da operadora para o prestador de recebimento dos documentos.

A mensagem de envio de documentos deve obrigatoriamente ser assinada pelo prestador conforme os requisitos técnicos da seção V – Padrão TISS (Escopo) acerca de certificado digital e da seção IX - Componente de Comunicação (Formato de Apresentação e Assinatura Digital), independentemente do tipo de documento que transporta, podendo estes,  
eventualmente ou por acordo entre as partes, serem documentos assinados pelos profissionais de saúde.

elegibilidadeProcesso de verificação de elegibilidade do beneficiário

# Processo de verificação de elegibilidade do beneficiário

Nesse processo o prestador de serviços de saúde verifica, junto à operadora, a situação do beneficiário para a realização de determinado procedimento. Para tanto são necessários os campos de identificação do beneficiário, bem como do prestador executante do procedimento.

**Elegibilidade:** é a mensagem enviada pelo prestador para a operadora solicitando a situação de determinado beneficiário junto à operadora quanto aos seus direitos contratuais.

**Resposta da elegibilidade:** é a mensagem de resposta da operadora para o prestador, informando a situação do beneficiário quanto aos seus direitos contratuais. Caso a resposta seja negativa para o processo de elegibilidade, a operadora deve identificar o motivo da negativa.

autorizacaoProcProcesso de autorização de procedimentos

# Processo de autorização de procedimentos

Nesse processo o prestador de serviços de saúde solicita autorização da operadora para que o beneficiário possa realizar um determinado procedimento. Assim, é necessário identificar o beneficiário, o prestador solicitante e executante e os procedimentos/itens assistenciais para os quais está sendo solicitada a autorização. Podem ser necessários ainda  
esclarecimentos quanto à situação de saúde do beneficiário com vistas à autorização do procedimento solicitado.

**Solicitação de autorização:** é a mensagem enviada pelo prestador para a operadora solicitando autorização para realização de algum serviço de saúde.

**Autorização de serviços:** é a mensagem de resposta da operadora para o prestador a um pedido de autorização para execução de serviço de saúde.  
Todos os procedimentos e itens assistenciais enviados na Solicitação de autorização devem constar na respectiva Autorização de serviços, inclusive aqueles que não tiverem sido autorizados.

**Solicitação de status de autorização:** é a mensagem do prestador para a operadora solicitando uma resposta a uma solicitação de autorização enviada anteriormente.

**Lote de anexos:** é a mensagem do prestador para a operadora para o envio de solicitação de autorização de procedimentos de quimioterapia, radioterapia e OPME. E ainda, o envio do anexo de situação inicial de odontologia se houver necessidade do envio deste anexo e em separado da guia principal de cobrança de odontologia.

Situação da autorização é a mensagem da operadora para o prestador informando se a autorização do serviço de saúde foi ou não concedida ou ainda se encontra em análise pela operadora.

**Recebimento anexos:** é a **mensagem da operadora** para o prestador fornecendo um protocolo de recebimento da mensagem de lote de anexos.

**Cancelamento de guia:** é a mensagem do prestador para a operadora que solicita o cancelamento de um lote de guias, guias ou recurso de glosa enviados anteriormente;

**Recibo do cancelamento de guia:** é a **mensagem da operadora** para o prestador com a confirmação, ou não, do cancelamento de um lote de guias, guias ou recurso de glosa.

##
