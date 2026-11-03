---
article_id: 1500004974762
category: RH - Folha de Pagamento
content_hash: 4b8089aa447febbf8d0bee5f9c2ad499679cbafd77bdcbdbc633dfcf8571081f
fetched_at: '2026-06-28T22:44:15.064828+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Mensalidade Sindical para colaborador Horista Jornada
  Variável
type: support-article
updated_at: '2025-08-11T21:19:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004974762-RH-Linha-Protheus-GPE-Mensalidade-Sindical-para-colaborador-Horista-Jornada-Vari%C3%A1vel
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26335372609943)** Tempo aproximado para leitura: **00:01:00 min**  
**Ocorrência**Não é calculado desconto da Mensalidade Sindical para colaborador **Horista Jornada Variável** **(RA\_HOJORVA = 1-"SIM" ).**  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**O funcionário horista com Jornada Variável é aquele cuja quantidade de horas trabalhadas no mês sofre variações de acordo com a necessidade de suas atribuições, desta forma, o salário referência utilizado para o pagamento deverá ser obtido através da média das horas apuradas dos 12 últimos meses.

A Mensalidade Sindical do Horista Jornada Variável, utilizará como base a média das horas apuradas dos 12 últimos meses. Quando calculada sobre o **Tipo Salario = 1 - "BASE"** **(Cadastro de Sindicato > pasta / Mens Sindical).**

Quando a Mensalidade Sindical não encontra as médias para compor a BASE de calculo, a verba não é calculada na folha de pagamento para o horista Jornada Variável.   
  
**Solução**Em **Cadastro de Verbas (GPEA040),**aba **Outras Informações**, campo **Grupo Verba** (**RV\_GRPVERB**) todas as verbas que estiverem agrupadas com "0" serão consideradas como verbas de salário, ou seja, aquelas que serão consideradas na composição das médias salariais para pagamento do Horista jornada variável.

Caso o funcionário seja Horista (**RA\_CATFUNC = "H"**) e o campo **Jor.Variavel (RA\_HOJORVA)** tenha o conteúdo **1-Sim,**mas no cadastro de verbas nenhuma verba esteja no **GRUPO 0 (RV\_GRPVER = "0")** a média salarial não será calculada. consequentemente o desconto do valor de Mensalidade Sindical não será calculado.  
  
**1.** Localize a verba que ira compor o calculo das Medias para pagamento do horista jornada variável  
  
**2.** Clique em Alterar, aba Outras Informações, selecione o campo Grupo Verba, Marque "GRUPO 0"

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26335347469975)

Recalcule a folha de pagamento e efetue a conferencia do desconto sindical.

**Saiba mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento) **<https://tdn.totvs.com/display/public/PROT/TVMEN0_DT_Horistas_com_Jornada_Variavel>**
