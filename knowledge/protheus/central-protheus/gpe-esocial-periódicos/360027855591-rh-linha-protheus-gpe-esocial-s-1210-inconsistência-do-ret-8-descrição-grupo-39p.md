---
article_id: 360027855591
category: GPE - eSocial - Periódicos
content_hash: 34c967cea025ef20062c267c38eed29a297328f7440aa17f76537e269b39106a
fetched_at: '2026-06-28T22:45:08.979544+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-1210 - Inconsistência do RET - 8 -
  Descrição: Grupo #39;Pensao alimenticia#39; deve ser preenchido. Verifique as condicoes
  de preenchimento no leiaute.'
type: support-article
updated_at: '2025-05-08T14:12:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027855591-RH-Linha-Protheus-GPE-eSocial-S-1210-Inconsist%C3%AAncia-do-RET-8-Descri%C3%A7%C3%A3o-Grupo-39-Pensao-alimenticia-39-deve-ser-preenchido-Verifique-as-condicoes-de-preenchimento-no-leiaute
---

**Ocorrência**Inconsistência do RET - 8 - Descrição: Grupo #39;Pensao alimenticia#39; deve ser preenchido. Verifique as condicoes de preenchimento no leiaute.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Causa**A inconsistência é retornada pelo RET (Governo) quando no evento S-1210 existe alguma Verba/Rubrica com Natureza ou código de incidência de Pensão Alimentícia e não existem informações do Beneficiário da Pensão Alimentícia.   
  
**Solução**Para gerar o valor da **Pensão Alimentícia** no evento **S-1210** é necessário que a verba esteja com as informações abaixo no cadastro de verbas do SIGAGPE. *Caminho: atualizações > definições de calculo > verbas > aba esocial.*

Campo Natureza deve ser igual a **9213.**Campo Cd. Inc. IRRF deve ser igual a **51, 52, 53, 54, 55.**  
  
A informações do Beneficiário da Pensão Alimentícia são preenchidas de acordo com as informações do cadastro de Beneficiário GPE onde também é parametrizado as regras do cálculo do valor da Pensão Alimentícia.  
  
Segue abaixo o Print da informações e validações previstas no leiaute do eSocial versão 2.5.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027623512/mceclip0.png)  
  
Se você informar manualmente a Pensão Alimentícia no cálculo do GPE também deverá informar manualmente as informações no evento S-1210 no TAF.  
  
Se o seu Trabalhador não tem cálculo de Pensão Alimentícia, mas o RET (Governo) retorna tal inconsistência é devido haver alguma outra Verba/Rubrica no evento S-1200 e/ou no evento S-1210 com a Natureza e/ou o código de incidência indevido.  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[MP - GPE - eSocial - S-1010 - Como configurar a Natureza e Código de Incidência Tributária das Verbas/Rubricas?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023121291)  
[S-5001 - Como ajustar incidência e validade de rubricas no governo, TAF e GPE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024360512)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)
