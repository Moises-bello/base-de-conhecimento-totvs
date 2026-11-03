---
article_id: 34285623915031
category: LEGAIS - BLOCO H/MATR460
content_hash: 1681191dcd9f48d52f4bfccab6b2459372bdc6dd1273c13abc38b83408c9fe34
fetched_at: '2026-06-28T22:42:15.079593+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA950 - type mismatch
  on compare on MAPASPF:PROCESSMOV(MAPASPF.PRW)
type: support-article
updated_at: '2025-08-19T12:12:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34285623915031-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA950-type-mismatch-on-compare-on-MAPASPF-PROCESSMOV-MAPASPF-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34285623912855) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao gerar o processo na rotina MATA950, ocorre o erro type mismatch on compare on MAPASPF:PROCESSMOV(MAPASPF.PRW) 07/02/2025 17:20:50 line : 2589  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Causa**  
Esse incidente ocorre, pois algum campo esta faltante para geração do processamento.

**Solução**  
Solicite ao **TI responsável** que consulte a **QUERY registrada no error.log** na **STACK** da chamada da função para validar os valores gravados nos campos **UM** e **UNMAPA**.

![Screenshot_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34286073800343)

![Screenshot_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34286073802007)

1. Verifique no **complemento de cadastro do produto** se a **Unidade de Medida** está corretamente informada, pois no erro os dados filtrados po UM e UNMAPA vão estar diferentes:
2. Ajuste o cadastro do produto, caso seja identificada inconsistência na unidade (exemplo: produto cadastrado sem unidade ou com unidade divergente).

### **Ao processar a rotina MATA950, o sistema pode apresentar o erro:**

```
THREAD ERROR ([00000], nome_do_usuario, XPTO-1) 12/08/2025 17:25:23
type mismatch on compare on MAPASPF:PROCESSMOV(MAPASPF.PRW) 07/02/2025 17:20:50 line : 2589
```

Esse erro é identificado como um **problema de comparação de variáveis** durante a execução da rotina.

**No fonte, a rotina tenta executar uma comparação (**`!=` **ou** `==`**) entre os campos:**

* **UM** → Unidade de Medida (exemplo: "KG")
* **UNMAPA** → Unidade do Mapa

**Ocorre inconsistência porque:**

* O campo **UM** vem como caractere (ex.: "KG")
* O campo **UNMAPA** vem numérico (ex.: `0`)

Essa diferença de tipos (caractere x numérico) causa o erro de **type mismatch**.

**Relacionado:**  
[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA950/MATR913 - Mapas de Controle de Produtos Químicos - Conceito e Configurações Mínimas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410036766487-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA950-MATR913-Mapas-de-Controle-de-Produtos-Qu%C3%ADmicos-Conceito-e-Configura%C3%A7%C3%B5es-M%C3%ADnimas)

**Saiba Mais:**  
[Clique aqui e veja mais artigos sobre LEGAIS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)
