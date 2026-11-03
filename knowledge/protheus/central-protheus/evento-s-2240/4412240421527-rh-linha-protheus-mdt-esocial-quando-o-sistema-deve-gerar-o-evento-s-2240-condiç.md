---
article_id: 4412240421527
category: Evento S-2240
content_hash: 9c615391a984725b868c51e28c0e2f98d3185073db54a367976299e5de62f38d
fetched_at: '2026-06-28T22:45:23.519282+00:00'
product: protheus
section_id: 8260550695703
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - Quando o sistema deve gerar o evento
  S-2240 (Condições Ambientais do Trabalho - Agentes Nocivos)
type: support-article
updated_at: '2025-03-03T18:07:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412240421527-RH-Linha-Protheus-MDT-eSocial-Quando-o-sistema-deve-gerar-o-evento-S-2240-Condi%C3%A7%C3%B5es-Ambientais-do-Trabalho-Agentes-Nocivos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30372501914775) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Quando o sistema deve gerar o evento S-2240 (Condições Ambientais do Trabalho - Agentes Nocivos)?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**O evento **S-2240** é gerado sempre que o trabalhador estiver exposto a algum risco, ou deixa de estar exposto a algum risco. Esse evento também é gerado sempre que entregue ou devolvido um **EPI** que tenha relação com o risco exposto.  
  
Como o risco do trabalhador pode estar ligado a **Centro de custo**, **Departamento**, **Função** e **Tarefa**. Qualquer alteração em rotinas ligadas a esses cadastros podem fazer com que o sistema gere um evento S-2240.  
  
**Exemplos de Casos:**

1. Trabalhador estava vinculado a um **Risco de Ruído** relacionado ao **Centro de custo** "A". E no dia 01 foi transferido para o **Centro de custo** "B" que no sistema está vinculado ao **Risco Radiações**.  
   Nesse cenário ao gerar a transferência o trabalhador deixa de estar exposto ao Risco Ruído e passa a fazer parte do Risco Radiações, então o sistema gera o S-2240.
2. Trabalhador estava vinculado a um **Risco de Ruído** relacionado ao **Centro de custo "**A". E no dia 01 foi transferido para o **Centro de custo** "C" onde **não existe exposição a Riscos**.  
   Nesse cenário ao gerar a transferência o trabalhador deixa de estar exposto ao **Risco Ruído** e **não fica exposto a nenhum Risco**, e o sistema também gera o **S-2240** com o agente **09.01.001**. Por regra do eSocial quando não existe exposição é necessario gerar um evento S-2240 com o código de agente **09.01.001** (Ausência de agente nocivo ou de atividades previstas no Anexo IV do Decreto 3.048/1999).
3. Trabalhador admitido é, e o centro de custo vinculado não está relacionado com nenhum risco.  
   Nesse cenário o sistema vai gerar o **S-2240** com o agente nocivo **09.01.001** (Ausência de agente nocivo ou de atividades previstas no Anexo IV do Decreto 3.048/1999).

**Observação**

* Os exemplos acima foram com **Centro de custo**, mas pode ocorrer com troca de **Departamento**, **Função** e **Tarefa**. Ou seja, qualquer informação que altere a situação do risco;
* O **S-2240** sempre será gerado com agente nocivo ou sem agente nocivo quando não existe exposição;
* **Não é necessario** cadastrar agente e risco com o código de agente nocivo **09.01.001**, o sistema faz essa geração de forma **automática**, já que não faz sentido criar um risco, para dizer que não existe risco;
* O evento S-2240 é um evento não periódico, ou seja, ele é gerado sempre que houver modificações, em datas diferentes, então se for **entregue** um **EPI** hoje será gerado o evento, e outro **EPI** amanhã será gerado novo evento para representar que houve uma nova inclusão em outra data;
* A geração desse evento pode ocorrer tanto através do modulo **SIGAMDT** como através do modulo **SIGAGPE** já que informações de funcionários e transferências são utilizadas nos dois módulos;
* No artigo a seguir é possível encontrar vídeos com How To de como gerar os eventos SST: **[MDT - eSocial - Existe vídeos com o passo a passo de geração dos eventos SST (Medicina e Segurança do Trabalho) no eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410314804631).**

**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
