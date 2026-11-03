---
article_id: 360056928654
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 48289bf5fb0d55250844a883c897e2fa80b3a132f1fc7e17f42d5faa52b3c8d2
fetched_at: '2026-06-28T22:42:05.185936+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  - Erro de Validação M100 M500 - EFD Contribuições '
type: support-article
updated_at: '2023-01-04T17:43:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056928654-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Erro-de-Valida%C3%A7%C3%A3o-M100-M500-EFD-Contribui%C3%A7%C3%B5es
---

**Dúvida**Como corrigir o erro de validação nos registros M100 e M500?  
  
**Ambiente**Microsiga Protheus -  A partir da versão 11.80  
  
**Solução**

Abaixo procedimentos para correção do erro nos registros M100 e M500:

***"Deverá existir um registro M100 - Crédito de PIS/PASEP/M500 - Crédito de COFINS para cada Tipo de Crédito e Alíquota informados nos documentos com CST de 50 a 66 (COD\_CRED = 101, ALIQ\_PIS = 1.6500,***

***ALIQ\_PIS\_QUANT = , NAT\_BC\_CRED = 12, CST\_PIS = 50)."***Realizar filtro via tabela SFT ou extrair um relatório da apuração (FISR101) referente as notas fiscais do período e realizar analise das amarrações dos campos dos códigos de credito do campo FT\_CODBCC e a CFOP que foi amarrada.  
  
Existe uma tabela disponibilizada pela Receita referente a base de credito dos registros M105/M505 - determinada pela CFOP informado no documento fiscal.  
  
O código é gravado no campo FT\_CODBCC esse campo é alimentado pela TES campo F4\_CODBCC.  
  
Se o código informado não for o correto para CFOP correta a ser utilizada a composição dos valores dos registros M105 e M505 será gerado de forma incorreta.  
  
Nome do arquivo: Tabela\_CFOPOperacoesGeradorasCreditos.xls (Link em Observações)  
  
Será a presentado o Grupo de código da base de credito e CFOP relacionadas.

**Atenção**: Após a geração da apuração as informações para geração do registro M105/M505 no TXT são buscados da tabela CL9.  
  
Após análise e ajuste dos códigos na tabela SFT por CFOP, excluir apuração do período e realizar nova apuração do período.

Gerar arquivo TXT e validar via PVA.

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/9995225390743-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Boletim-t%C3%A9cnico-Apura%C3%A7%C3%A3o-e-gera%C3%A7%C3%A3o-arquivo-txt-EFD-Contribui%C3%A7%C3%B5es?source=search>
