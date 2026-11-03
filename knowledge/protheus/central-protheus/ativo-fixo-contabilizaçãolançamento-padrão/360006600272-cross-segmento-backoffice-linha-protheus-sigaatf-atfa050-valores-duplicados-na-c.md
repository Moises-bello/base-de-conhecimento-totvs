---
article_id: 360006600272
category: Ativo Fixo - Contabilização/Lançamento padrão
content_hash: bd84fbbbea8c974244550401724dd8e8099dd5b62f0789674d98adbd7ef039a4
fetched_at: '2026-06-28T22:41:42.349401+00:00'
product: protheus
section_id: 1500001536421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus  - SIGAATF  - ATFA050 Valores duplicados
  na contabilização
type: support-article
updated_at: '2023-11-17T17:51:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006600272-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA050-Valores-duplicados-na-contabiliza%C3%A7%C3%A3o
---

**Ocorrência**Na contabilização do Cálculo e/ou Descalculo da Depreciação de bens do Ativo Fixo, os valores são contabilizados mais de uma vez divergindo valores gravados no ativo e na contabilidade.  
  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - Ativo Fixo - Todas as versões  
  
  
**Causa**Esta inconformidade ocorre devido ao tratamento realizado para o valor do lançamento (no campo CT5\_VLR01), onde é apontado campo da tabela SN3.  
  
  
**Solução**

A rotina de cálculo de depreciação passou por uma reestruturação para a versão 12, onde, para cada valor de depreciação gerado, no momento da contabilização o sistema passa algumas vezes por esse ponto.  
No Lançamento Padrão deverá inserir a condição para aceitar ou rejeitar, em nosso exemplo usamos o campo SN4->N4\_TIPOCNT=="4", se atente também aos tipos de saldo de seu ativo: SN3->N3\_TIPO=01 ou SN3->N3\_TIPO=10.  
Configuração básica do campo valor no lançamento padrão 820 na 12 , para não gerar  lançamento duplicado.

**IIF (SN4->N4\_TIPOCNT== "4",SN4->N4\_VLROC1,0)**

**OBSERVAÇÃO:**

A contabilização do calculo da depreciação através do LP820 deverá utilizar as informações da SN4

Não é recomendado o uso das tabelas FNG e SNG para contabilização do calculo de depreciação

"O  **Grupo de Bens é um facilitador** para preenchimento dos dados contábeis do ativo e não deve ser considerado como pré-condição para execução de uma operação"

Link relacionado ao grupo de bens

[Comportamento do campo Grupo de Bens na Transferência](https://tdn.totvs.com/pages/releaseview.action?pageId=517122324)

No link abaixo, segue informações:[CTB0087\_Contabilizacao\_descalculo\_mensal](https://tdn.totvs.com/display/PROT/CTB0087_Contabilizacao_descalculo_mensal)

[MV\_ATFCONT – Configuração do parâmetro para cálculos do Ativo Online ou Offline](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11563614676375-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-MV-ATFCONT-Configura%C3%A7%C3%A3o-do-par%C3%A2metro-para-c%C3%A1lculos-do-Ativo-Online-ou-Offline?source=search)
