---
article_id: 18925207587863
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: 4a999b0ef88e4c3d1d7bfc9340d3c57fe8a8e169ac742931e9e909ac407bec02
fetched_at: '2026-06-28T22:39:51.306358+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Código do Fornecedor
  se altera no Documento de Entrada após gerar a Nota Fiscal de Transferência.
type: support-article
updated_at: '2023-11-08T20:06:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18925207587863-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-C%C3%B3digo-do-Fornecedor-se-altera-no-Documento-de-Entrada-ap%C3%B3s-gerar-a-Nota-Fiscal-de-Transfer%C3%AAncia
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18925253805975) Tempo aproximado para leitura: **03:00 min** **Dúvida**Após gerar a Nota Fiscal de Transferência (**EICCO100**) dentro do SIGAEIC, o Fornecedor do item se altera durante a classificação da NF dentro do Documento de Entrada.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Easy Import Control - Todas as versões  
  
**Solução**Importante ressaltar que na Nota Fiscal de Transferência, o Importador está transferindo a posse e neste momento será gravado o Fornecedor do item informado no **Cadastro do Importador (EICA005)**.  
Caso queira que o Fornecedor seja o mesmo da Invoice, será necessário que os campos "**YT\_FORN**" e "**YT\_LOJA**" não sejam preenchidos dentro do **Cadastro do Importador (EICA005).  
  
![Importador - NFT.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/18925276382359)  
  
Saiba mais:**[**Nota Fiscal de Transferência**](https://tdn.totvs.com/pages/releaseview.action?pageId=562472978)
