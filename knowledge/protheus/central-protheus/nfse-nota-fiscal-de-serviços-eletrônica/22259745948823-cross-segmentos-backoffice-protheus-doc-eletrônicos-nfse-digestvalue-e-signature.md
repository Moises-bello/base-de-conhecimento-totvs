---
article_id: 22259745948823
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 28e5b2fd028686d3f650677b40b01e7978b8001e7ee35de11b9f7183ee34805e
fetched_at: '2026-06-28T22:39:56.271580+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - <DigestValue>
  e <SignatureValue>
type: support-article
updated_at: '2024-03-22T12:52:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22259745948823-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-DigestValue-e-SignatureValue
---

**Dúvida**Qual é a diferença entre as tags DIgestValue e SignatureVAlue no XML de uma Nota Fiscal de Serviços  
  
**Ambiente** Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Solução**  
No XML de uma nota fiscal de serviços, as tags <DigestValue> e <SignatureValue> são utilizadas em contextos diferentes e desempenham funções distintas:

**<DigestValue>:**Esta tag é usada para armazenar o valor de hash de um elemento específico do XML. O objetivo do <DigestValue> é fornecer uma representação única e compacta dos dados contidos no elemento referenciado.  
O valor de hash é calculado usando um algoritmo de resumo criptográfico, como MD5, SHA-1, ou SHA-256, e serve como uma espécie de "impressão digital" dos dados. Ele é usado para garantir a integridade dos dados, pois qualquer modificação nos dados resultaria em um valor de hash diferente.

**<SignatureValue>:**Esta tag é usada para armazenar a assinatura digital do XML. A assinatura digital é gerada usando um par de chaves criptográficas (uma chave privada para assinar e uma chave pública para verificar a assinatura).  
O processo de assinatura digital envolve primeiro gerar um resumo criptográfico dos dados (como explicado acima), e então essa "impressão digital" é criptografada usando a chave privada do emissor. O resultado é a assinatura digital, que é armazenada na tag <SignatureValue>.  
A assinatura digital é usada para garantir a autenticidade e a integridade dos dados no XML. Ela permite que o receptor verifique se o XML não foi alterado e se realmente foi enviado pelo emissor alegado.  
  
Em resumo, enquanto <DigestValue> armazena um valor de hash para garantir a integridade dos dados, <SignatureValue> armazena a assinatura digital para garantir tanto a autenticidade quanto a integridade dos dados.
