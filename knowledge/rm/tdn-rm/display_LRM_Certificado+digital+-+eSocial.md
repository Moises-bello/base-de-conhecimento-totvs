---
content_hash: 11e2725e9044ec9b353089a5596326a4e2f66403a66f8f21698e05e30c7e2ac5
fetched_at: '2026-06-29T00:08:50.403504+00:00'
page_id: '334334295'
product: rm
source: tdn-rm
title: Certificado digital - eSocial
type: documentation
url: https://tdn.totvs.com/display/LRM/Certificado+digital+-+eSocial
version: 2
---

O certificado digital utilizado no sistema eSocial deverá ser emitido por Autoridade Certificadora credenciada pela Infraestrutura de Chaves Públicas Brasileira – ICP-Brasil.

Este deverá pertencer à série “**A**”. Existem duas séries às quais os certificados podem pertencer, a série “A” e a “S”. A série “A” reúne os certificados de assinatura digital utilizados na confirmação de identidade na Web, em e-mails, em Redes Privadas Virtuais – VPN e em documentos eletrônicos com verificação da integridade de suas informações. A série “S” reúne os certificados de sigilo que são utilizados na codificação de documentos, de bases de dados, de mensagens e de outras informações eletrônicas sigilosas.

O certificado digital deverá ser do tipo **A1** ou **A3**. Certificados digitais de tipo **A1** ficam armazenados no próprio computador a partir do qual ele será utilizado. Certificados digitais do tipo **A3** são armazenados em dispositivo portátil inviolável do tipo smart card ou token, que possuem um chip com capacidade de realizar a assinatura digital. Este tipo de dispositivo é bastante seguro, pois toda operação é realizada pelo chip existente no dispositivo, sem qualquer acesso externo à chave privada do certificado digital.

Os certificados digitais serão exigidos em dois momentos distintos:

**a)** Transmissão: antes de ser iniciada a transmissão de solicitações ao sistema eSocial, o certificado digital do solicitante é utilizado para garantir a segurança do tráfego das informações na INTERNET. Para que um certificado seja aceito na função de transmissor de solicitações este deverá ser do tipo e-CPF (e-PF) ou e-CNPJ (e-PJ).

**b)** Assinatura de documentos: para os empregadores pessoas jurídicas, os eventos poderão ser gerados por qualquer estabelecimento da empresa ou seu procurador, mas o certificado digital assinante destes deverá pertencer a matriz ou ao representante legal desta ou ao procurador/substabelecido, outorgado por meio de procuração eletrônica e não-eletrônica.

Para os empregadores pessoas físicas, os eventos deverão ser gerados pelo próprio empregador ou seu procurador ou, ainda, o procurador/substabelecido, outorgado por meio de procuração eletrônica e não-eletrônica, assinados, em todos os casos, por meio de certificado digital.

Para os Órgãos Públicos, os eventos poderão ser gerados pelo representante autorizado para efetuar a transmissão das respectivas unidades administrativas.

Os certificados digitais utilizados para assinar os eventos enviados ao eSocial deverão estar habilitados para a função de assinatura digital, respeitando a Política do Certificado. Está previsto para o projeto o uso de Procuração Eletrônica da RFB ou da Caixa.

Os eventos que compõem o eSocial devem ser transmitidos mediante autenticação e assinatura digital utilizando-se certificado digital válido no âmbito da Infraestrutura de Chaves Públicas Brasileira – ICP-Brasil.

Informações e normas a respeito da Certificação Digital, bem como a relação dasAutoridades Certificadoras podem ser encontradas nos links a seguir:

* <http://idg.receita.fazenda.gov.br/orientacao/tributaria/senhas-e-procuracoes/senhas/certificados-digitais/orientacoes-sobre-emissao-renovacao-e-revogacao-de-certificados-digitais-e-cpf-ou-e-cnpj>

* <http://www.certificado.caixa.gov.br/>

**Fonte: Manual de Orientação do eSocial** (Disponível em: <https://portal.esocial.gov.br/institucional/documentacao-tecnica> ).
