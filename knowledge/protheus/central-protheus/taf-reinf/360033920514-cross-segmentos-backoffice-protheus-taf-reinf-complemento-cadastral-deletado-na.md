---
article_id: 360033920514
category: TAF - REINF
content_hash: 08672e234aad7f5583027b370920216c8564e20b15937f0346ed4b0afef793f2
fetched_at: '2026-06-28T22:41:33.787860+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Complemento Cadastral
  deletado na tabela C1E.
type: support-article
updated_at: '2023-03-31T17:03:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033920514-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Complemento-Cadastral-deletado-na-tabela-C1E
---

**Dúvida**Após rodar o extrator e o processamento para o REINF o complemento cadastral está sendo deletado.  
   
 **Ambiente**Microsiga Protheus - TAF - versão 12.1.17  
  
**Solução**

Verificar o conteúdo do parâmetro MV\_SUBTRIB , que não deve estar com duas inscrição estadual para o mesmo estado no mesmo parâmetro e sim por filial, caso esteja preenchido com duas inscrições o sistema irá gerar dois registros T001, deletando o complemento cadastral na tabela C1E.

|T001AA|SP|123456789100||  
|T001AA|SP|123456789101||

MV\_SUBTRIB = preenchido com estado + inscrição estadual (todos os estados que possuírem inscrição estadual para recolhimento do ICMS ST)

Exemplo:

MV\_SUBTRIB = Preenchido com UF + Inscrição Estadual

Exemplo: MV\_SUBTRIB=SP1234567/MG1234567
