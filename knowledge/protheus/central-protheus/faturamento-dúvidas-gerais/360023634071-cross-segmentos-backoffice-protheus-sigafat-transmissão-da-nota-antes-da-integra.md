---
article_id: 360023634071
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 4f81b90d1ccd405dc67044e10acaa096e47fb1d72e964f2298b2aca671bb6695
fetched_at: '2026-06-28T22:38:29.891779+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Transmissão da Nota antes
  da integração com os demais módulos do ERP
type: support-article
updated_at: '2026-03-30T17:47:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023634071-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Transmiss%C3%A3o-da-Nota-antes-da-integra%C3%A7%C3%A3o-com-os-demais-m%C3%B3dulos-do-ERP
---

**Dúvida**  
É possível transmitir a Nota de Saída antes de gerar integração com os módulos do ERP, como Financeiro, Fiscal, Estoque, etc?

**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da release 12  
  
  
**Solução**  
A geração do Documento de Saída (**MATA461**) no ERP Protheus em relação ao Status da Nota junto ao SEFAZ são distintos.

Todo o processo de geração da nota com a geração das tabelas SF2 e SD2, necessárias para o registro do XML e geração de DANFE , ocorre antes e é neste momento que o ERP efetua as integrações Fiscais, Financeira e movimentação do Estoque, apenas Contabilização que pode ser efetuada de forma posterior, usando a Contabilização off line.

Se o usuário gera o documento de saída, para o ERP, este documento movimentará as integrações entre módulos.

já a  Transmissão e autorização dessa Nota junto ao SEFAZ é uma etapa posterior e independente, de todo o processo de geração de nota e integração com os módulos, para que seja efetuado de forma diferente seria necessário reescrever todo o sistema legado que há hoje.

Caso a NFE não seja autorizada e não tenha mais intenção de refaturar o Pedido (**MATA410**) relacionado a esta nota, deve-se excluir o Documento de saída, excluindo assim as integrações geradas por ele.  
  
Sendo assim, pelo padrão **não há como gerar o título apenas depois de o SEFAZ retornar com autorização da Nota** ou mesmo transmitir a Nota antes de gerar Financeiro, Fiscal, movimentação de Estoque entre outros.
