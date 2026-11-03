---
article_id: 19450025711255
category: GPE - eSocial - Processo Trabalhista
content_hash: 4c40d5c0a404b680883570324bad7c4906d6120a2f5667b9ccd252cecc5cbda6
fetched_at: '2026-06-28T22:45:00.542822+00:00'
product: protheus
section_id: 10604669539479
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-5503 - Como o eSocial demonstra as
  Informações do FGTS por Trabalhador em Processo Trabalhista
type: support-article
updated_at: '2023-11-30T14:39:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19450025711255-RH-Linha-Protheus-GPE-eSocial-S-5503-Como-o-eSocial-demonstra-as-Informa%C3%A7%C3%B5es-do-FGTS-por-Trabalhador-em-Processo-Trabalhista
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19450033788055) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como o eSocial demonstra as Informações do FGTS por Trabalhador em Processo Trabalhista?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Trata-se de um retorno do Ambiente Nacional do eSocial para o evento S-2500. Nele consta a totalização da base de cálculo e o valor do depósito para o FGTS de cada contrato de trabalhador (CPF) citado no evento S-2500. Este evento alimentará o sistema **FGTS Digital para geração de guias 375** com as bases de cálculo informadas.  
  
**Prazo de envio:** O retorno ocorre na medida em que o evento S-2500 – Processo Trabalhista, ou o evento S-3500 – Exclusão de Eventos – Processo Trabalhista (quando excluir o S-2500), forem processados.  
  
**Pré-requisitos:** Envio dos eventos S-2500 e/ou S-3500.  
  
**1.4** Dentro de cada período de referência, para totalizar a base de cálculo do FGTS do processo trabalhista, são retornadas as informações de remuneração com o seguinte agrupamento:   
**a) Código “71” (FGTS Origem Processo Trabalhista)** para trabalhadores com {codCateg} = [101, 102, 104, 105, 106, 111, 201, 202, 301, 302, 303, 304, 306, 307, 309, 310, 312, 721] ou não informado ou, ainda, para as categorias ([401, 410], se {categOrig} for diferente de [103, 107, 108]). A alíquota aplicada será de 8,0%;  
**b) Código “72” (FGTS Origem Processo Trabalhista - Aprendiz/Contrato Verde e Amarelo)** para trabalhadores com {codCateg} = [103, 107, 108] ou ([401, 410], se {categOrig} = [103, 107, 108]). A alíquota aplicada será de 2,0%;   
**c) Código “73” (FGTS Origem Processo Trabalhista** - Indenização compensatória do empregado doméstico) para trabalhadores domésticos ({codCateg} = [104}). A alíquota aplicada será de 3,2%.  
  
**1.5** Para a definição da categoria do item anterior, será observado:  
**a)** A categoria informada no campo {infoContr/codCateg} do evento S-2500, no caso de  reconhecimento de vínculo ({infoContr /indContr} = [N]); 376  
**b)** Para mudanças de categoria reconhecida no processo trabalhista, a informação do campo {mudCategAtiv/codCateg}, se o período de referência for igual ou superior à data do campo {mudCategAtiv/dtMudCategAtiv};  
**c)** O código existente no Registro de Eventos Trabalhistas - RET no último dia do período de referência, para os demais casos.  
  
Para mais informações sobre o evento S-5503, consulte o [Manual de Orientação do eSocial Versão S-1.2](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-2-consolidada-ate-a-no-s-1-2-04-2023.pdf).  
  
**Saiba Mais**  
Para saber mais consulte os *links*abaixo:   
[RH - Linha Protheus - GPE - eSocial - Processos Trabalhistas - Premissas para geração dos eventos do eSocial para Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13317899021847)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
  
Essa documentação também pode ser acessada 24h, através da Carolina:[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
