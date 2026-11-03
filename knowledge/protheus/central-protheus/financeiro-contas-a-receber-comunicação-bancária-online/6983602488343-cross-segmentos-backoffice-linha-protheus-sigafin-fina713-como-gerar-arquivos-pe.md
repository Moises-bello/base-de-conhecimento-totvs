---
article_id: 6983602488343
category: Financeiro - Contas a Receber - Comunicação Bancária Online
content_hash: e283ac2939e55cb2856e2daebbd9527d462ad1aef1eb567972feb133edb7e884
fetched_at: '2026-06-28T22:37:49.217450+00:00'
product: protheus
section_id: 26656227629847
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA713 - Como gerar
  arquivos .PEM para utilização no registro de boletos por webservice do banco Bradesco
type: support-article
updated_at: '2025-07-30T20:13:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6983602488343-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA713-Como-gerar-arquivos-PEM-para-utiliza%C3%A7%C3%A3o-no-registro-de-boletos-por-webservice-do-banco-Bradesco
---

**Dúvida**Como gerar arquivos.**PEM** para utilização no registro de boletos por API do banco Bradesco?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA713 - a partir da versão 12.1.33  
  
**Solução**Primeiramente deve solicitar ao banco que habilite o serviço de transmissão de boletos por webservice e possuir o certificado digital da empresa (arquivo .**PFX**)

No módulo **SIGACFG** devem ser gerado os arquivos .**PEM** utilizando a função **CFGX060** 

**Procedimentos**

Configurar os parâmetros:

**MV\_SIAFICA**: Caminho do certificado de autorização para acesso do Webservice do SIAFI  
**MV\_SIAFICE**: Caminho do certificado do cliente para acesso ao Webservice do SIAFI.  
**MV\_SIAFIKE**: Caminho da chave privada para acesso ao Webservice do SIAFI.

1. Clique em **Avançar**.
2. Selecione o arquivo do tipo .pfx no campo**Caminho do Certificado Digital**.
3. Informe o campo **Senha de Autorização**.
4. Clique em **Avançar**.
5. Informe o caminho dos arquivos de saída nos campos **Certificado de Autorização (CA)**, **Certificado de Cliente (CERT)**, **Chave Privada (KEY)**. Estes campos transformam o arquivo em .PEM para utilização pelo Protheus.
6. Clique em **Avançar**.
7. Verifique se os arquivos foram criados nas pastas informadas.
8. Clique em **Finalizar**.

**Documentação de referência:** [Wizard de conversão de certificado digital (CFGX060 - SIGACFG)](https://tdn.totvs.com/pages/releaseview.action?pageId=312157886)

**Saiba mais** [Registro de boletos on-line - Bradesco](https://tdn.totvs.com/display/public/PROT/Registro+de+boletos+on-line+-+Bradesco)
