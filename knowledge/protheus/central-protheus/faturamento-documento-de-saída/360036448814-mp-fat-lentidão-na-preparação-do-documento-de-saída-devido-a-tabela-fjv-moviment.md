---
article_id: 360036448814
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: a13f34263b5c181f152720c419e95ebe693c18e1fa4da71298cd681ff92e0e4e
fetched_at: '2026-06-28T22:38:45.189437+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: MP - FAT - Lentidão na preparação do Documento de Saída devido a tabela FJV
  (Movimento Analitico P/Natureza)
type: support-article
updated_at: '2021-04-28T15:13:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036448814-MP-FAT-Lentid%C3%A3o-na-prepara%C3%A7%C3%A3o-do-Documento-de-Sa%C3%ADda-devido-a-tabela-FJV-Movimento-Analitico-P-Natureza
---

**Dúvida**

Lentidão na preparação do documento de saída causada pela movimentação da tabela FJV (Movimento Analítico P/Natureza).  
  
**Ambiente**

Microsiga Protheus -  a partir da versão 12.  
  
**Solução**  
O parâmetro **MV\_FINATFN** funciona com o mesmo conceito do parâmetro **MV\_ATUSAL** utilizado na contabilidade para atualizar saldos contábeis.  
  
O parâmetro **MV\_FINATFN** informa em que momento será atualizado a tabela de saldos por natureza.   
  
Toda vez em que for realizado uma movimentação com natureza no financeiro ou Off-Line, a tabela de saldos por natureza será atualizado somente após a execução da rotina de Refaz Saldos Por Natureza (**FINA800**).  
  
É importante verificar se a empresa precisa ter os saldos por natureza atualizados on line. Caso não tenha esta necessidade, o parâmetro poderá ser configurado para ser atualizado Off-Line.   
  
A rotina de Refaz Saldos por Natureza pode ser executada em outro momento de forma manual ou até colocar em schedule e especificar um horário para a sua execução.  
  
Para efeito contábil, esta tabela não tem efeito, pois a contabilidade trabalha com suas próprias tabelas e rotinas que a atualizem seus saldos.  
  
Abaixo um link sobre o parâmetro:  
**<https://tdn.totvs.com/pages/releaseview.action?pageId=325849723>**
