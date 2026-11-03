---
article_id: 360045764993
category: GPE - eSocial - Não Periódicos
content_hash: 1572cfcd87d22208d3531450090abc3f9967fbff355c955bcbae2aa124c16b5c
fetched_at: '2026-06-28T22:45:04.579306+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2200 - Inconsistência do RET - 553
  - Grupo #39;Trabalhador Estrangeiro#39; nao deve ser preenchido. Verifique as condicoes
  de preenchimento no leiaute
type: support-article
updated_at: '2021-12-30T19:51:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045764993-RH-Linha-Protheus-GPE-eSocial-S-2200-Inconsist%C3%AAncia-do-RET-553-Grupo-39-Trabalhador-Estrangeiro-39-nao-deve-ser-preenchido-Verifique-as-condicoes-de-preenchimento-no-leiaute
---

**Ocorrência**Inconsistência do RET - 553 - Descrição : Grupo #39;Trabalhador Estrangeiro#39; nao deve ser preenchido. Verifique as condicoes de preenchimento no leiaute.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**Essa inconsistência ocorre porque está sendo enviado para o governo informações do cadastro de estrangeiro, porem o país de nascimento está como Brasil.  
  
Quando o país de nascimento é igual a Brasil, não pode existir informações na aba estrangeiro do cadastro do trabalhador.  
  
Abaixo destaco a parte do layout que retrata essa informação:  
  
O (**obrigatório**) (Se {**paisNac**} <> **Brasil**). N (Não nas demais situações)  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062864894/mceclip0.png)  
  
**Solução**Verifique se o trabalhador é estrangeiro no **sigagpe** acessando o Caminho: atualizações > funcionários > funcionários.  
  
Caso **não** seja a aba estrangeiro do cadastro de funcionários não deve ter informações.  
Exemplo:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063765013/mceclip2.png)  
  
Caso o trabalhador **seja** **estrangeiro** o campo **Nacionalidade** (RA\_NACIONA) não pode ser Brasil.  
Exemplo:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062865154/mceclip1.png)  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
