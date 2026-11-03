---
content_hash: 693f1bc8a3764f8256a2f1e8f4b2f1ea6a6ecfd5f9c878277ff21fdb0ddde160
fetched_at: '2026-06-29T00:09:29.173303+00:00'
page_id: '423938828'
product: rm
source: tdn-rm
title: Parâmetros por Filial (CT-e OS - Conhecimento de Transporte Eletrônico para
  Outros Serviços)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938828
version: 4
---

Para enviar CT-e OS (Conhecimento de Transporte Eletrônico para Outros Serviços) é necessário parametrizar os dados fiscais da filial.  
No Totvs Gestão de Estoque, Compras e Faturamento acessar a opção Ambiente | Parâmetros e selecionar o item Gestão de Estoque, Compras e Faturamento.   
Acesse o caminho Integrações | Fiscal | Dados Fiscais e clicar e selecione Avançar.   
Após isso acessar o item Parâmetros por Filial e selecionar a filial que deseja configurar.

**Certificado Digital 2/2**

**Tipo do Certificado Digital**: Informar o formato do certificado.

**Certificado Digital**: Informar o caminho onde o certificado se encontra

**Senha da Private Key**: Preencher esse campo com a senha do certificado

**Ambiente CT-e OS**

Essa tela contém três campos:

1. **Ambiente de Envio**: Indica para qual ambiente da SEFAZ será enviado o CT-e OS (Produção ou Homologação);
2. **Modalidade de Operação**: indica em qual modalidade o CT-e OS será emitido. As possíveis modalidades são:
   1. **Normal**: CT-e OS emitido normal
   2. **Contingência Offline FS-DA**: Indica que o CT-e OS foi emitido sem comunicação com a SEFAZ. Contingência SVC - RS: Indica que o CT\_e OS será emitido para a SEFAZ Virtual do Rio Grande do Sul.
   3. **Contingência SVC - SP**: Indica que o CT\_e OS será emitido para a SEFAZ Virtual de São Paulo.

**Versão do CT-e OS**: Indica qual a versão do layout do CT-e OS. Atualmente conterá valor fixo 3.00.
