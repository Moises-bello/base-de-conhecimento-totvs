---
article_id: 360050573653
category: Escrita Fiscal - Error.log
content_hash: d748dbd0b426ce60778ef70b6d2d486fa130676de25803bffbe9937bc7770b73
fetched_at: '2026-06-28T22:39:32.849491+00:00'
product: protheus
section_id: 1500001549782
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Error.log ao solicitar
  a rotina MATR927
type: support-article
updated_at: '2021-07-08T13:25:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050573653-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Error-log-ao-solicitar-a-rotina-MATR927
---

**Ocorrência**

Error.log ao solicitar a rotina MATR927

variable does not exist F4\_MALQPIS on \_DEPRECATIVO(FISXATF.PRX)  
  
**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 12  
  
**Causa**

Descontinuidade dos relatórios;

* **MATR906 - Relatório Pis/Cofins.**
* **MATR946 - Extrato Pis/Cofins.**
* **MATR927 - Crédito de Pis/Cofins na depreciação do Ativo Imobilizado.**

**Solução**Os relatórios abaixo foram descontinuados e substituídos pelo relatório de conferência da EFD Contribuições (**FISR101**), portanto, não serão mais realizadas manutenções e/ou correções nestas rotinas:

* **MATR906 - Relatório Pis/Cofins.**
* **MATR946 - Extrato Pis/Cofins.**
* **MATR927 - Crédito de Pis/Cofins na depreciação do Ativo Imobilizado.**

Boletim técnico:  
  
<http://tdn.totvs.com/pages/releaseview.action?pageId=185736236>  
  
Com relação ao error log o campo F4\_MALQPIS está influenciando por não possuir no seu banco de dados ou não estar marcado como usado.  
  
O erro está parando no fonte da equipe de ativo fixo (FISXATF), porém como o relatório não é mais utilizado será corrigido em versões futuras.  
  
  
Atenciosamente,
