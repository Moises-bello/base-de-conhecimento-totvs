---
article_id: 9075849999383
category: TAF - eSocial -TSS
content_hash: 05bab3093b4b4bdd32e8c96edef12c392db62349891cbcdf98f18cc53ca021f7
fetched_at: '2026-06-28T22:45:21.956618+00:00'
product: protheus
section_id: 1500001536761
source: central-protheus
title: 'RH - Linha Protheus - TAF - eSocial - TSS - Erro na configuração do certificado
  digital, TOTVS Service SOA TSS CNPJ: CPF:IE: UF:SP Empresas: - IE invalida'
type: support-article
updated_at: '2024-05-24T19:43:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9075849999383-RH-Linha-Protheus-TAF-eSocial-TSS-Erro-na-configura%C3%A7%C3%A3o-do-certificado-digital-TOTVS-Service-SOA-TSS-CNPJ-CPF-IE-UF-SP-Empresas-IE-invalida
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23726188556567) Tempo aproximado para leitura: **05:00:00 min** **Dúvida**Ao realizar a configuração do certificado digital pela rotina do TAF Wizard de Configuração do TSS, ocorre o erro:

*TOTVS Service SOA TSS CNPJ: CPF:IE: UF:SP Empresas: - IE invalida*

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9075246609559)  
  
**Ambiente**RH - Linha Protheus - TAF - eSocial - Wizard de Configuração do TSS (TAFAWIZD) - Todas as versões

**Causa**

Falta de preenchimento ou preenchimento errado do campo **"Inscrição Estadual"** da empresa/filial no **Sigamat ou** **SYScompany**;

Consulte pelo módulo SIGACFG;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9075596470167)

**Solução**

Siga os passos abaixo para correção:

1. Acesse o site do **Sintegra** ([Sefaz](http://www.sintegra.gov.br/)) e selecione o estado correspondente;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23726188572183)

2. Na janela que será aberta, informe a identificação da empresa (CNPJ, IE, etc.);  
3. A partir desta consulta, conseguirá verificar qual o IE correto ou se o número do IE está errado no campo **"Inscrição Estadual"**;

4. Corrija o campo **"Inscrição Estadual"** pelo SIGACFG;  
5. Execute novamente a rotina Wizard de Configuração do TSS;
