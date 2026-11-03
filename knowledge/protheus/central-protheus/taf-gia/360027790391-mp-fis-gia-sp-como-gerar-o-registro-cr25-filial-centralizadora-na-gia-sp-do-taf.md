---
article_id: 360027790391
category: TAF - GIA
content_hash: 4d8ecb98334db91363f11569410d037cbf9be52ceb3ebf1293a6dc213243733b
fetched_at: '2026-06-28T22:41:32.396600+00:00'
product: protheus
section_id: 1500001547982
source: central-protheus
title: MP - FIS - GIA-SP - Como gerar o registro CR=25 (Filial Centralizadora) na
  GIA-SP do TAF.
type: support-article
updated_at: '2023-06-01T15:13:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027790391-MP-FIS-GIA-SP-Como-gerar-o-registro-CR-25-Filial-Centralizadora-na-GIA-SP-do-TAF
---

**Ocorrência**O registro CR=25 não esta sendo sendo gerado na GIA-SP gerada pelo TAF.  
  
**Ambiente**Microsiga Protheus - Livros Fiscais – A partir da versão 12.1.17.  
  
**Causa**Esta situação ocorre quando a Inscrição Estadual não é informada na **Apuração do ICMS** (**MATA953**) realizada no Protheus.   
 **Solução**Para solucionar este problema, siga os passos:

1. Acesse a Apuração do ICMS no Protheus;   
2. Informe os parâmetros para geração da Apuração;   
3. Posicione o cursor do mouse sobre 002.00 - Outros Débitos em: **Outras Ações -> Inc. Lin.**;   
4. Posicionado na nova linha gerada, informe o código de subitem 002.19;   
5. No campo Descrição será informada somente o número da Inscrição Estadual que saiu com o saldo credor/devedor do ICMS;   
6. No campo Valor, deverá ser informado o valor do ICMS transferido;   
7. No campo Cod de Lançamento, informe o código a ser utilizado;   
8. Confirme a Apuração do ICMS;   
9. Execute o extrator fiscal e processamento;   
10. Gere o arquivo da GIA-SP.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027462572/mceclip0.png)
