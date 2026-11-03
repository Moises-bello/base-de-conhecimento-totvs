---
article_id: 360034280553
category: MDFe - Manifesto de Carga
content_hash: abb7a13ca14de3214f3edb8260ba9dfe655f2b33807242cbec0b8f2e2ccb865f
fetched_at: '2026-06-28T22:40:08.268653+00:00'
product: protheus
section_id: 1500001549242
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - MDFE - DAMDFE não
  imprime chaves das notas fiscais
type: support-article
updated_at: '2025-06-17T18:14:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034280553-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-MDFE-DAMDFE-n%C3%A3o-imprime-chaves-das-notas-fiscais
---

**Dúvida**Como imprimir as chaves de referencia no DAMDFE?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - Todas as versões

**Solução**As notas fiscais relacionadas ao MDFE são mostradas apenas no XML, através de suas respectivas chaves. Somente quando o MDFE é transmitido em contingência as chaves nas notas relacionadas aparecem no DAMDFE.

* **Segue exemplo de como fica no XML:**  
  **<infNFe>**  
  **<chNFe>00000000000000000000000000000000000000000000</chNFe>**  
  **</infNFe>**  
    
  Segue link do Portal do MDFE da SEFAZ, baixe o [Manual de Orientações do Contribuinte, versão 3.00 de Outubro de 2016](https://mdfe-portal.sefaz.rs.gov.br/Site/Documentos#)  
    
  [https://mdfe-portal.sefaz.rs.gov.br/Site/Documentos#](https://mdfe-portal.sefaz.rs.gov.br/Site/Documentos)  
    
  Verifique a página 125, onde mostra que a Impressão Normal não informa que deve apresentar a nota relacionada ao MDFE. Porém para a Impressão em Contingência a SEFAZ criou o campo "Informações dos Documentos Fiscais Relacionados ao Manifesto" onde é destacada a chave da nota relacionada.  
    
  A TOTVS se baseia nos Manuais e Notas Técnicas PADRÕES da SEFAZ para a impressão dos documentos eletrônicos.  
    
  **Se preferir, o fonte DAMDFE é aberto para customização, onde você pode adequá-lo a sua maneira.**  
    
    
  ![](https://totvssuporte.zendesk.com/attachments/token/MXXpcgz9BPQYNdVpzB24fViAU/?name=inline-645995189.png)​  
    
  ![](https://totvssuporte.zendesk.com/attachments/token/hgZIdq47yR2dl9gURxOF4Leac/?name=inline-1474591753.png)​
