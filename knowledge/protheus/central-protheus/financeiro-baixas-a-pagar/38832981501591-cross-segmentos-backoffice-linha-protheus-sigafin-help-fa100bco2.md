---
article_id: 38832981501591
category: Financeiro - Baixas a Pagar
content_hash: ac72f8616a488046b0d4dcd706b1e47133dd3e1f79c574a1bc34c4ae2442a2bf
fetched_at: '2026-06-28T22:42:13.603972+00:00'
product: protheus
section_id: 38310054605975
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Help: FA100BCO2'
type: support-article
updated_at: '2026-03-05T19:38:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38832981501591-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Help-FA100BCO2
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38832981483543) Tempo aproximado para leitura: **00:05:00 min**  
  
**Ocorrência**  
Ao tentar realizar a baixa de um título em moeda 2 (Dólar) utilizando um banco estrangeiro configurado com moeda 3 (Euro), o sistema apresenta o alerta **Help FA100BCO2**.

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/38832953768087)](https://centraldeatendimento.totvs.com/hc/article_attachments/38832953768087)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.2310  
  
**Causa**

Este help ocorre porque o parâmetro **MV\_MOEDBCO=.F.** está desabilitado.  O parâmetro **MV\_MOEDBCO** permite a baixa de título em moeda estrangeira num banco de outra moeda estrangeira. Exemplo: baixa de um título em Euro num banco de moeda Dólar.

**Solução**

Para que a operação seja permitida e os títulos possam ser baixados em um banco estrangeiro de moeda diferente da operação, é necessário alterar o comportamento padrão do sistema habilitando o parâmetro **MV\_MOEDBCO = .T.**

**Saiba mais**

[**TDN - Utilização do parâmetro MV\_MOEDBCO**](https://tdn.totvs.com/pages/releaseview.action?pageId=638725960)
