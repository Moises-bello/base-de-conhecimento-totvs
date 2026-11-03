---
article_id: 38583282605847
category: Financeiro - Cadastros
content_hash: 841c5079e3fbc92bf92c89f917b02ae601a312a09dbf93f7d1f13bfcb695a046
fetched_at: '2026-06-28T22:37:53.132399+00:00'
product: protheus
section_id: 1500001550722
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA010 - HELP: NATISON2'
type: support-article
updated_at: '2026-03-25T20:16:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38583282605847-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA010-HELP-NATISON2
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38583282584343) Tempo aproximado para leitura: **00:07:00 min**  
  
**Dúvida**  
![natison2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38583314038807)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - Todas as versões  
  
**Solução**

O erro **NATISON2** ocorre quando o Protheus está configurado para **não** utilizar estrutura hierárquica, mas o usuário (ou processo) tenta cadastrar uma natureza informando características de hierarquia (como informar um "Pai" ou defini-la como um agrupador).

No módulo Financeiro do Protheus, a separação do tipo de natureza dita como ela se comporta no sistema:

* **Natureza Sintética (Tipo 1):** Atua como um nível totalizador ou agrupador. O seu objetivo é estrutural e gerencial, servindo para somar os valores das naturezas que estão "abaixo" dela.

  **Atenção:** Uma natureza sintética não pode receber movimentações diretas ou títulos.
* **Natureza Analítica (Tipo 2):** É a natureza de nível transacional. É ela que efetivamente recebe os lançamentos, os títulos a pagar/receber e as movimentações bancárias do dia a dia.

O responsável por ditar se o sistema vai usar o conceito de hierarquia é o parâmetro **MV\_NATSINT**:

* **Conteúdo = 1:** Habilita a Natureza Estruturada. O sistema passa a exigir a árvore hierárquica, permitindo que naturezas analíticas tenham um "pai" (sintética).
* **Conteúdo = 2:** Desabilita a estrutura. O sistema ignora hierarquias, exigindo que todas as naturezas sejam de nível final (Analíticas) e independentes.

**Validações necessárias para solucionar o erro:**

**Se o conteúdo do** **parâmetro** **MV\_NATSINT** **for 2:** Acesse a alteração/inclusão da Natureza no módulo Financeiro e certifique-se rigorosamente de que o campo "Tipo" (`ED_TIPO`) está preenchido com **2** (Analítico) e limpe qualquer informação, incluindo espaços, do campo "Cód. Pai" (`ED_PAI`).

**Se a empresa necessitar de hierarquia:** altere o parâmetro **MV\_NATSINT** para **1**. A partir desse momento, cadastre primeiro as naturezas de tipo Sintético e, em seguida, as Analíticas, informando no campo `ED_PAI` a qual grupo sintético elas pertencem.

**Ponto de atenção:**

**O Help NATISON2 será acionado se pelo menos uma destas condições for verdadeira quando a estrutura está com parâmetro** **MV\_NATSINT = 2****:**

* **Condição 1:** O campo **ED\_PAI** não está vazio.
* **Condição 2:** O campo **ED\_TIPO** é diferente de "2" (Analítico).

Como o operador é um "OU", basta uma dessas regras ser violada para o Protheus bloquear a operação.

Verifique se o campo **ED\_TIPO está vazio, se estiver, preencha para tipo Analítico.**

![ed_tipo-vazio.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38583314039575)

Saiba mais: [Naturezas - FINA010 - Financeiro - P12](https://tdn.totvs.com/display/PROT/Naturezas+-+FINA010+-+Financeiro+-+P12)
