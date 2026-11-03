---
article_id: 1500004780941
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 5f8d5cf017e0c35adee7f564c20638f1bc426c42a676ec4b4f677b23a836bdcd
fetched_at: '2026-06-28T22:38:44.053012+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - SIGAFAT - Help: "NXTSX5Nota"'
type: support-article
updated_at: '2024-11-28T20:11:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004780941-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Help-NXTSX5Nota
---

**Dúvida**Como solucionar a mensagem: NXTSX5Nota ao faturar?

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5665451634967)

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões.  
  
**Solução**

Na rotina **MATXFUNA**, na função **ChkSX5Nota**, o sistema checa a numeração nas tabelas **SF2, SD2, SF3, SFT e SE1**, e ao tentar executar a regra abaixo, o sistema encontra inconsistência na numeração.  
  
1) Analisar o tamanho dos campos que guarda o conteúdo da numeração na SX3.

* Ver tamanho dos campos se estão iguais: F2\_DOC, D2\_DOC, F3\_NFISCAL, E1\_NUM e FT\_NFISCAL

2) Checar se a  numeração que está sendo gerada existe nas tabelas mencionadas acima, filtros a se fazer:

* F2\_DOC = 'numeração que que salvar'
* D2\_DOC = 'numeração que que salvar'
* F3\_NFISCAL = 'numeração que que salvar'
* E1\_NUM = 'numeração que que salvar'
* FT\_NFISCAL = 'numeração que que salvar'

3) Checar se na tabela SX5, campo o campo está com a numeração do mesmo tamanho dos campos do passo 1.

* Filtro: X5\_TABELA = '01' e veja o tamanho dos conteúdos do campo X5\_DESCRI.

4) Checar se não há customizações no processo

5) Checar a atualização do sistema
