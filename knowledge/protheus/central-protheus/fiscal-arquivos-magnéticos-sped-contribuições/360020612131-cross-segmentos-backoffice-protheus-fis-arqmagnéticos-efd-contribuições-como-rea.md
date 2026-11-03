---
article_id: 360020612131
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 0e9d064b9f7bbae3000a6b2bd5994a3657a7fd269488d019b2e939e795c9c117
fetched_at: '2026-06-28T22:42:05.149770+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  - Como realizar o rateio por naturezas no registro F100
type: support-article
updated_at: '2023-01-04T13:18:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020612131-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Como-realizar-o-rateio-por-naturezas-no-registro-F100
---

**Dúvida**Como realizar o rateio por naturezas no registro F100 quando o Documento é lançado via Documento de Entrada?  
  
 **Ambiente**Microsiga Protheus – Livros Fiscais – A partir da versão 11.80.  
   
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
 1. Configure o parâmetro abaixo:  
MV\_MULNATP = .T. (se Contas a pagar)  
  
 2. Configure o rateio no lançamento do Documento;  
  
![rateio2.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360016508572/rateio2.gif)

3. Cadastre as naturezas de acordo com a necessidade;  
No exemplo abaixo, cadastramos a natureza 20002 para gerar o crédito no F100 e a natureza 20003 para não gerar o crédito.  
  
4. Realize o lançamento do Documento de Entrada através da rotina (**MATA103**) - **Documento de Entrada**.  
  
5. Faça a apuração da EFD Contribuições e gere o arquivo magnético.  
  
![MULT_NATUREZA.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360016560231/MULT_NATUREZA.gif)
