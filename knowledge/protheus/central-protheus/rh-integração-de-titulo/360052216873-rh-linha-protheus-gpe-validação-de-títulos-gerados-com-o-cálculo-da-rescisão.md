---
article_id: 360052216873
category: RH - Integração de Titulo
content_hash: 6867cc011dd71c95b996464996e044aae1c02c044fdaf4c5fe38bc4ebb83a5a9
fetched_at: '2026-06-28T22:43:36.462596+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Validação de títulos gerados com o cálculo da Rescisão
type: support-article
updated_at: '2025-07-29T18:50:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052216873-RH-Linha-Protheus-GPE-Valida%C3%A7%C3%A3o-de-t%C3%ADtulos-gerados-com-o-c%C3%A1lculo-da-Rescis%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33797414007703) Tempo aproximado para leitura: **00:02:00 min****

**Ocorrência**Validação de títulos gerados com o cálculo da Rescisão.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12  
  
**Causa**Implementação de tratamento para validação de exclusão de rescisões que já tenham títulos gerados/integrados com o financeiro.  
Sistema precisa emitir mensagem informando que já existem títulos gerados/integrados para a rescisão em questão, alertando o usuário para necessidade de efetuar a manutenção desses títulos antes de realizar nova integração.  
  
**Solução**

Efetuada a criação da Tabela RJ1 para que sejam gravadas as rescisões referentes ao título. Criado mecanismo para verificar durante a exclusão ou recálculo da rescisão se existe algum registro da rescisão na tabela RJ1. Caso exista, será exibido o alerta abaixo, dando ao usuário possibilidade de prosseguir ou não com a operação: 

 

![](https://tdn.totvs.com/download/attachments/452706210/image2019-2-1_17-32-46.png?version=1&modificationDate=1549049566130&api=v2)  
  
Detalhes da tabela RJ1 (releases anteriores ao 12.1.25 necessária a criação via Configurador - lembrando que campos criados dessa maneira ficam marcados como campos de usuário e suas respectivas manutenções via UPDDISTR, caso necessárias, serão limitadas):   
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080974674)  
  
**Importante**O tamanho do campo RJ1\_NUMTIT deve ser igual ao do campo RC1\_NUMTIT para que a implementação funcione corretamente.

**Saiba Mais**  
[Artigos sobre Integração de Títulos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
