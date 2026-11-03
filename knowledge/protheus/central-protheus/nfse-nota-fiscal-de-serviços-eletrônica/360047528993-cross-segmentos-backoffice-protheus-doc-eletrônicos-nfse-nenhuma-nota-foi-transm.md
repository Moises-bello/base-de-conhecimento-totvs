---
article_id: 360047528993
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: aec7997c9cb94d998ebf067b9d1578837181149a5446484fc0cd8d11da8569c1
fetched_at: '2026-06-28T22:39:56.248201+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE -  Nenhuma
  Nota foi Transmitida (Entrada)
type: support-article
updated_at: '2025-07-18T13:45:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047528993-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Nenhuma-Nota-foi-Transmitida-Entrada
---

**Ocorrência**No módulo **Faturamento**, ao tentar realizar a transmissão de uma **NFTS (Nota de Entrada)** pela rotina **FISA022**, é apresentado uma mensagem de erro "**NENHUMA NOTA FOI TRANSMITIDA**".  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Causa**Esse incidente ocorre geralmente por erros cadastrais, onde alguns dados não são levados corretamente para alguns campos e consequentemente o XML da nota não é gerado.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Verifique se a nota gerou registros nas tabelas CD2, SF3 e SFT, caso não tenha gerado revise o TES usado, se houver dúvidas na configuração do TES, verifique com o suporte fiscal;  
  
2. Verifique se gerou o documento com a espécie igual à NFS;  
  
3. Verifique se o campo B1\_CODISS está preenchido e se alimentou os campos D1\_CODISS e F3\_CODISS;  
*(Se mesmo com B1\_CODISS preenchido os demais campos CODISS estiverem em branco, verifique com o suporte fiscal).*  
  
4. Verifique se o campo F4\_CF está preenchido com um código que inicia com 4 ou inferior, para caracterizar uma nota de entrada;  
  
5. Verifique se há carácter especial no conteúdo da nota, principalmente na discriminação.  
  
**Importante:**  
Se todos os itens acima estão corretos e a mensagem "Nenhuma Nota Transmitida" persiste, existe a possibilidade dessa nota já ter sido transmitida.  
Para confirmar isso acesse o monitor dessa nota, se o status estiver pendente é necessário aguardar o processamento ou verificar se ocorre algum erro no Console do TSS.  
Se apresenta a mensagem "Retransmita o ID", é necessário verificar no botão histórico o motivo da rejeição, realizar a correção e em seguida retransmitir a nota.
