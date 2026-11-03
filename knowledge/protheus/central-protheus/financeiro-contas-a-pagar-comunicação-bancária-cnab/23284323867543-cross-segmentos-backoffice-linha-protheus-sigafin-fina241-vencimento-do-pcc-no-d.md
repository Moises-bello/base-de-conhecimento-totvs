---
article_id: 23284323867543
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: e0321dde6a7cef150df99cff08fdbf1976bace107a0d66ca13de29f6fc08e4c0
fetched_at: '2026-06-28T22:37:56.218044+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA241 - Vencimento
  do PCC no dia 20 do mês subsequente ao vencimento real da Nf
type: support-article
updated_at: '2024-05-06T14:53:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23284323867543-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA241-Vencimento-do-PCC-no-dia-20-do-m%C3%AAs-subsequente-ao-vencimento-real-da-Nf
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23284323834519) Tempo aproximado para leitura: **00:05:00min** **Dúvida**Como gerar os títulos do PCC pela rotina FINA241 com data do vencimento no dia 20 do mês subsequente ao vencimento real da NF?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - A partir da release 12.1.33  
  
**Solução**Para geração do PCC com vencimento no dia 20 do mês subsequente, considerando a data do vencimento real da NF, o parâmetro **F12 da rotina FINA241 'Cálculo dos Impostos ?'**, precisa estar com conteúdo **'Vencimento Real'** e também é necessário habilitar o parâmetro **MV\_BDVCIMP.**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23284323836951)  
  
**Importante**  
Se o **MV\_BDVCIMP = .T.,** o cálculo de vencimento dos impostos **PCC/IRRF** será a partir da data de vencimento real do título (**E2\_VENCREA**).

**Exemplo:**

Nota fiscal com vencimento real 05/10/XX, incluso no borderô na data 30/09/XX, o vencimento do imposto será calculado a partir no mês de outubro, logo seu vencimento ocorrerá no mês de novembro.  
  
**Saiba mais:**[Borderô de Impostos (FINA241 - SIGAFIN)](https://tdn.totvs.com/pages/releaseview.action?pageId=312165366#Border%C3%B4deImpostos(FINA241SIGAFIN)-04.PAR%C3%82METROS)
