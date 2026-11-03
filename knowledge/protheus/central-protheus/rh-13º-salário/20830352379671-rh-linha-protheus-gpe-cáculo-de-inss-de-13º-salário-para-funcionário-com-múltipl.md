---
article_id: 20830352379671
category: RH - 13º salário
content_hash: 984d5c475fed2e67f50728f7a9625b7679c4ca9ecd8a0a42fa9ae558071f40da
fetched_at: '2026-06-28T22:44:00.431631+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Cáculo de INSS de 13º Salário para funcionário
  com Múltiplos Vinculos e Categorias Diferentes
type: support-article
updated_at: '2026-06-25T11:24:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20830352379671-RH-Linha-Protheus-GPE-C%C3%A1culo-de-INSS-de-13%C2%BA-Sal%C3%A1rio-para-funcion%C3%A1rio-com-M%C3%BAltiplos-Vinculos-e-Categorias-Diferentes
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20830367284631) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
INSS de 13º Salário fica incorreto quando o funcionário é Celetista (Categoria 101)  e tem outro vínculo como Pró-Labore ou Autônomo (Categoria 722).  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Para que o cálculo do INSS de 13º salário fique correto, será necessário lançar a verba com Identificador de cálculo **1847** com o **valor da Base de INSS do Pró-Labore/Autônomo da Outra Empresa** no roteiro **132**.  
Para mais informações [Clique Aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=543096737).

Exemplo de cadastro da verba com Id de cálculo 1847:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41478229433879)

**Saiba Mais:**  
[Cálculo de 13º Salário para Múltiplos Vínculos](https://tdn.totvs.com/pages/releaseview.action?pageId=811722665)   
[RH - 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio)
