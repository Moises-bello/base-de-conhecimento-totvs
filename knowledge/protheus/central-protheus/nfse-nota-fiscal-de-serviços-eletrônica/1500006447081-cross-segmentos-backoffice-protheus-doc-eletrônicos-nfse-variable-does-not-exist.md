---
article_id: 1500006447081
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 62ca6b2c3895a18c4dfd4c924dcf4e0f6b92b4d8a54789e3e6da06d531f8a6d2
fetched_at: '2026-06-28T22:39:58.624818+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - variable
  does not exist C5_ENDPRES on PRESTACAO(NFSEXMLENV.PRW) DD/MM/AAAA HH:MM:SS line
  : 2141'
type: support-article
updated_at: '2025-06-10T18:39:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006447081-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-variable-does-not-exist-C5-ENDPRES-on-PRESTACAO-NFSEXMLENV-PRW-DD-MM-AAAA-HH-MM-SS-line-2141
---

**Ocorrência**Ao realizar a transmissão de um RPS ocorre o error.log: ***"variable does not exist C5\_ENDPRES on PRESTACAO(NFSEXMLENV.PRW) DD/MM/AAAA HH:MM:SS line : 2141"***  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Causa**Esse error.log é causado quando está sendo utilizado a configuração *[MP - NFSE - Dados da Prestacao: Endereço, Número, Complemento, Bairro, CEP e PAIS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026101732--MP-NFSE-Dados-da-Prestacao-Endere%C3%A7o-N%C3%BAmero-Complemento-Bairro-CEP-e-PAIS),* **porém com o parâmetro MV\_ENDPRES configurado incorretamente, geralmente sem a separação de cada campo por aspas simples ( ' ).**  
  
**Solução**Para correção, a estrutura do parâmetro deverá ser a seguinte abaixo, separado por aspas simples:  
  
{'C5\_ENDPRES','C5\_NUMPRES','C5\_COMPPRE','C5\_BAIPRES','C5\_CEPPRES','C5\_PAIS'}  
  
Feito isso, é de extrema importância **reiniciar o Protheus** para surgir efeito nas alterações.  
*Obs.: Vale lembrar que o nome dos campos poderá variar de acordo com o que foi criado e configurado através da documentação citada acima, porém a estrutura do parâmetro deverá ser padrão.*
