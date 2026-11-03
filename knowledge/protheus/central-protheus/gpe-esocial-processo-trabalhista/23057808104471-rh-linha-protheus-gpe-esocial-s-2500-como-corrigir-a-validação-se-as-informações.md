---
article_id: 23057808104471
category: GPE - eSocial - Processo Trabalhista
content_hash: 0878ffab675f678d26212d587e3bf2c59669ca796f2ec84c79e7e65bd833fac4
fetched_at: '2026-06-28T22:45:00.525876+00:00'
product: protheus
section_id: 10604669539479
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-2500 - Como corrigir a validação:
  "Se as informações de identificação do contribuinte forem preenchidas, o tipo de
  contrato deve ser igual a 8 - Responsabilidade indireta"'
type: support-article
updated_at: '2024-04-25T18:17:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23057808104471-RH-Linha-Protheus-GPE-eSocial-S-2500-Como-corrigir-a-valida%C3%A7%C3%A3o-Se-as-informa%C3%A7%C3%B5es-de-identifica%C3%A7%C3%A3o-do-contribuinte-forem-preenchidas-o-tipo-de-contrato-deve-ser-igual-a-8-Responsabilidade-indireta
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23057791358615) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como corrigir a validação: "Se as informações de identificação do contribuinte forem preenchidas, o tipo de contrato deve ser igual a 8 - Responsabilidade indireta", que ocorre no campo Tipo da rotina Dados eSocial?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Ao incluir ou alterar o Contrato de Trabalho na rotina Dados eSocial (TAFA552D), o campo Tipo apresenta a mensagem: "**Se as informações de identificação do contribuinte forem preenchidas, o tipo de contrato deve ser igual a 8 - Responsabilidade indireta**".  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23057808080023)  
  
Essa validação ocorre porque na tela anterior **Identificação de Processo**, os campos **Tipo de Inscrição** e **Número de Inscrição** estão preenchidos.   
Esses dados somente devem ser informados se o processo judicial caso tenha havido **imposição de responsabilidade indireta**, onde deve-se informar a identificação do contribuinte (responsável direto).  
Caso tenha sido por responsabilidade indireta, o campo Tipo deve ser preenchido como Responsabilidade Indireta.  
  
Se o processo não for uma imposição de responsabilidade indireta, o campo deve ficar vazio. Para isso, será necessário acessar a rotina Processo (APTA100) e deletar as informações.  
**Acesse** Atualizações - Processo Trabalhista - Processos - Processos  
Clique em **alterar o processo** cadastrado e **delete** as informações dos campos **Tipo Inscrição e Numero Inscrição**.![smartclient_27vaAUmZbL.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/23057791362455)  
Após deletar, clicar em **salvar** e verificar na rotina Dados eSocial se a informação foi excluída, da aba Identificação de Processo.  
  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:  
[RH - Linha Protheus - GPE - eSocial - Processos Trabalhistas - Premissas para geração dos eventos do eSocial para Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13317899021847-RH-Linha-Protheus-GPE-eSocial-Processos-Trabalhistas-Premissas-para-gera%C3%A7%C3%A3o-dos-eventos-do-eSocial-para-Processos-Trabalhistas)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
