---
article_id: 1500011019962
category: Financeiro - Aplicação / Emprestimos
content_hash: a547359b9f9f36196e42c4925ce2126784978f12fe52c01ced8b20fd7ff4cb03
fetched_at: '2026-06-28T22:37:59.438758+00:00'
product: protheus
section_id: 1500001550542
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA716 - Contabilização
  offline de Resgate, Pagamento e Empréstimo
type: support-article
updated_at: '2024-10-28T16:56:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011019962-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA716-Contabiliza%C3%A7%C3%A3o-offline-de-Resgate-Pagamento-e-Empr%C3%A9stimo
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20444662155031)*T**empo aproximado para leitura: **00:06:00 min**

**Dúvida**Realizar a contabilização offline de Resgate, Pagamento e Empréstimo?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA716 - Todas as versões  
  
**Solução**  
Para realizar a contabilização do **Resgate, Pagamento e Empréstimo** (FINA716) temos o lançamento padronizado 585.

**ATENÇÃO:** As informações abaixo são apenas exemplos para ponto de partida e **não** devem ser copiadas **(ctrl+c / ctrl+v)** diretamente para seu **Lançamento padrão**, visto que eventualmente algum caracter incorreto gerado pela copia, poderá causar inconsistencias no processo final.

**Exemplos****LP 585 – Resgate de Aplicação/Empréstimo**

Seq. 01

Valor do LP: SEH->EH\_VALJUR

Histórico: If(SEH->EH\_APLEMP=”APL”, “Juros de Aplicação financeira”, “Juros de Empréstimo bancário”)

Seq. 02

Valor do LP: SEH->EH\_VALIOF

Histórico: If(SEH->EH\_APLEMP=”APL”, “IOF de Aplicação financeira”, “Juros de Empréstimo bancário”)

Seq. 03

Valor do LP: If(SEH->EH\_APLEMP=”APL”,EH->EH\_VALIRF,0)

Histórico: If(SEH->EH\_APLEMP=”APL”, “IR sobre Aplicação financeira”, “”)

**LP 586 – Estorno de Resgate de Aplicação/Empréstimo**

Seq. 01

Valor do LP: SEH->EH\_VALJUR

Histórico: If(SEH->EH\_APLEMP=”APL”, “Estorno de Juros de Aplicação financeira”, “Estorno Juros de Empréstimo bancário”)

Seq. 02

Valor do LP: SEH->EH\_VALIOF

Histórico: If(SEH->EH\_APLEMP=”APL”, “Estorno de IOF de Aplicação financeira”, “Estorno de Juros de Empréstimo bancário”)

Seq. 03

Valor do LP: If(SEH->EH\_APLEMP=”APL”,EH->EH\_VALIRF,0)

Histórico: If(SEH->EH\_APLEMP=”APL”, “Estorno de IR sobre Aplicação financeira”, “”)

**Saiba Mais**  
[Exemplo de contabilização de Aplicação e Empréstimo](https://tdn.totvs.com/pages/releaseview.action;jsessionid=4FC87CF51878186F503B65C08DEBB9DD?pageId=236430682)  
[FIN0007\_LPAD\_Lançamento\_padrão\_financeiro](https://tdn.totvs.com/pages/releaseview.action?pageId=235585410)  
<https://tdn.totvs.com/pages/releaseview.action?pageId=392500138>
