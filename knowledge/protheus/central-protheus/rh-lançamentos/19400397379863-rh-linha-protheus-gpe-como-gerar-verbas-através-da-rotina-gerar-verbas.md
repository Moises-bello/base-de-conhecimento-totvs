---
article_id: 19400397379863
category: RH - Lançamentos
content_hash: 7c298f496b065846c0e7c75d2bda19007f4249871090073ab4d5f48425a7a950
fetched_at: '2026-06-28T22:43:31.199399+00:00'
product: protheus
section_id: 360010781734
source: central-protheus
title: RH - Linha Protheus - GPE - Como gerar verbas através da rotina Gerar Verbas
type: support-article
updated_at: '2026-03-27T17:33:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19400397379863-RH-Linha-Protheus-GPE-Como-gerar-verbas-atrav%C3%A9s-da-rotina-Gerar-Verbas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19400388384535) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como gerar verbas em Lançamentos por Funcionários ou Valores Futuros através da rotina Gerar Verbas?  
  
**Ambiente**  
TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução**  
Na rotina Gerar Verbas é possível gerar verbas nas rotinas Lançamentos por Funcionários ou Valores Futuros, para isso, acesse a rotina pelo menu **Miscelânea > Cálculos > Gerar Verbas (GPEM170)**, e preencha os parâmetros abaixo conforme necessidade de geração:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19400407893783)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19400410507927)

Na pergunta **Informe a Verba**, coloque a verba que será gerada nesse exemplo é a verba 013:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19400388394903)

**Base Cálculo Sobre:** pode escolher as opções de Hora, Valor, Percentual ou Dias  
**Percentual Sobre:** pode escolher as opções de Verba ou Salário Base  
**Sobre Salário:** Pode escolher Base ou Composto, mas essa pergunta terá funcionalidade somente se a pergunta anterior estiver com Salário base  
**% Sobre Qual Verba:** Informe as verbas que deseja compor o percentual se a pergunta Percentual Sobre estiver com Verba

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19400407902999)

**Gerar Verbas:** Pode escolher Mensais (RGB) ou Futuros (SRK)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19400397322775)

**Obs.:** A rotina possui filtros padrões como Centro de Custo e Matrícula, não é possível adicionar novos parâmetros.   
  
Após confirmar, sistema apresentará a tela abaixo de acordo com a pergunta **Base de cálculo sobre**, sendo:  
  
-**Hora**, tela será conforme abaixo para informar a quantidade de horas e filtrar pela faixa salarial  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19400420459671)  
  
-**Valor**, tela será conforme abaixo para informar o Valor e filtrar pela faixa salarial:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19400407914903)  
  
-**Percentual**, a tela será conforme abaixo para informar o percentual, filtrar pela faixa salarial e escolher um valor mínimo e máximo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19400410527767)  
  
-**Dias**, a tela será conforme abaixo para informar a quantidade de dias e filtrar pela faixa salarial:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19400420469655)  
  
Preencha de acordo com a sua **necessidade** e confirme, sistema gerará conforme parâmetros informados, no **exemplo** abaixo foi gerado **30%** sobre o **salário base** em Lançamentos por Funcionários:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19400407923991)

**Saiba Mais**  
[RH - Lançamentos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010781734-RH-Lan%C3%A7amentos)  
[RH - Linha Protheus - GPE - Como excluir as verbas geradas pela rotina Geração de Verbas (GPEM170)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047431794-RH-Linha-Protheus-GPE-Como-excluir-as-verbas-geradas-pela-rotina-Gera%C3%A7%C3%A3o-de-Verbas-GPEM170)  
[RH - Linha Protheus - GPE - É possível importar arquivo em excel com lançamentos de verbas em folha de pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409361989655-RH-Linha-Protheus-GPE-%C3%89-poss%C3%ADvel-importar-arquivo-em-excel-com-lan%C3%A7amentos-de-verbas-em-folha-de-pagamento)
