---
article_id: 21850891688087
category: RH - Dissídio
content_hash: 78d344bc42863c6e2a3aad953d74733f6e363044ace7ffffd538e263d18ccb80
fetched_at: '2026-06-28T22:43:43.475457+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Acidente de trabalho incorreto no Cálculo de dissídio
  para funcionários que possuem exposição a agentes nocivos
type: support-article
updated_at: '2025-09-09T12:19:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21850891688087-RH-Linha-Protheus-GPE-Acidente-de-trabalho-incorreto-no-C%C3%A1lculo-de-diss%C3%ADdio-para-funcion%C3%A1rios-que-possuem-exposi%C3%A7%C3%A3o-a-agentes-nocivos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21850891677719) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Acidente de trabalho incorreto no Cálculo de dissídio para funcionários que possuem exposição a agentes nocivos  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Quando se trata da verba de Acidente de trabalho incorreto no Cálculo de dissídio para funcionários que possuem exposição a agentes nocivos (leve, médio ou grave), a rotina de dissídio considerando a possibilidade de alterações que podem ocorrer no tipo de exposição durante o período de contrato do colaborador valida essa informação na tabela SR9 (Histórico de Alteração de Funcionários). 

1) No cadastro do funcionário, aba funcionais, o campo %Acid.Trab está configurado com 9%

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21851542188055)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21851549099927)

2) Vamos verificar como está o histórico de Dados do Funcionário:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21851549110551)

Note que o histórico está divergente com o cadastro de funcionário:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21851549114135)

Possibilidades da divergência:

a) Erro na implantação/migração;  
b) Data Base do sistema incorreta no momento que foi realizada alteração  
c) Alterações realizadas via banco de dados  
  
**Observação:** A folha de pagamento é calculada corretamente pois a rotina considera o cadastro do funcionário (tabela SRA). Já para o cálculo do dissídio , a rotina precisa olhar para o histórico para seguir a ordem cronológica   
  
3) Para correção será necessário ajustar as informações na ordem correta ou deletar informações que não compõe a ordem cronológica das alterações.

**Saiba Mais:**  
[Página Centralizadora do Dissídio](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio)
