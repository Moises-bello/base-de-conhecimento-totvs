---
content_hash: ffba24b6bc116a0c5f5293a45e196df8f1bd9954baed201c00266568541a73dd
fetched_at: '2026-06-29T00:09:32.718880+00:00'
page_id: '425458909'
product: rm
source: tdn-rm
title: Secretaria - Notas/faltas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458909
version: 2
---

---

**Permitir que os pontos das avaliações sejam superiores aos pontos distribuídos nas etapas**  
    
 A instituição ao fazer o cadastro da etapa determina o total de pontos distribuídos. Com este parâmetro marcado e possível que sejam vinculadas as etapas avaliações com total de pontos maior que o determinado no campo 'Total de pontos distribuídos'.  
    
  Exemplo: 

* **Parâmetro desmarcado:**

  |  |  |  |  |
  | --- | --- | --- | --- |
  | **Etapa** | **Total de pontos** | **Avaliações** | **Total de pontos** |
  | 1ª etapa de notas | 100 | Avaliação I - I Avaliação I - II  Avaliação I - III Avaliação I - IV | 25pts   25pts   25pts   25pts |
  | 2ª etapa de notas | 60 | Avaliação I - I Avaliação I - II | 20pts   40pts |

  Observe que a soma dos pontos das avaliação é equivalente ao total de pontos distribuídos na etapa.

* **Parâmetro marcado:**

  |  |  |  |  |
  | --- | --- | --- | --- |
  | **Etapa** | **Total de pontos** | **Avaliações** | **Total de pontos** |
  | 1ª etapa de notas | 100 | Avaliação I - I   Avaliação I - II   Avaliação I - III   Avaliação I - IV | 30pts   30pts   25pts   25pts |
  | 2ª etapa de notas | 60 | Avaliação I - I   Avaliação I - II | 50pts   40pts |

  Observe que neste cenário as notas das avaliações ultrapassam o total de pontos distribuídos na etapa.
