---
article_id: 38295859046551
category: Financeiro - Smart View
content_hash: ceb759a32d52914350b32e79e872564c074f36b9e77f872e026351ba6d04421d
fetched_at: '2026-06-28T22:37:44.678189+00:00'
product: protheus
section_id: 32632656432151
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - FINSV007 - Alguns filtros não
  funcionam no relatório Movimento do Caixinha
type: support-article
updated_at: '2026-02-10T13:48:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38295859046551-Cross-Segmentos-Backoffice-Linha-Protheus-FINSV007-Alguns-filtros-n%C3%A3o-funcionam-no-relat%C3%B3rio-Movimento-do-Caixinha
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38295806383639) Tempo aproximado para leitura: **00:04 min**  
  
**Dúvida**  
Ao clicar no ícone de busca (lupa) "De Caixinha / Até Caixinha" no relatório de Movimentos do Caixinha (FINSV007), o sistema não apresenta a lista de opções de dados como ocorre em outros campos do Protheus.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38295806385175)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release  12.1.2210.  
  
**Solução:**

O relatório **FINSV007** utiliza o grupo de campos **'FINR560'**, componente do dicionário de dados padrão desde as versões legadas em ADVPL.

O comportamento observado no campo de busca deste relatório é uma característica específica de sua implementação:

* Diferente de outros campos onde a lista é carregada ao clicar na lupa, neste relatório a busca avançada deve ser acionada **diretamente na caixa de pesquisa**.
* O sistema realiza a validação dos dados consultando a existência de registros na tabela **SEU** (Movimentos do Caixinha) e o saldo atualizado na tabela **FIJ** (Saldos Bancários/Caixinha).

Portanto, o funcionamento está **conforme o esperado**, não se tratando de uma inconsistência, mas de uma particularidade na interface de filtragem deste relatório específico.

![finsv007 (1).gif](https://centraldeatendimento.totvs.com/hc/article_attachments/38295883057431)

**Saiba Mais**

[TDN - Movimento Caixinha](https://tdn.totvs.com/display/public/PROT/Smart+View+-+Movimento+Caixinha)
