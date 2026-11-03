---
article_id: 21164679626903
category: RH – DIRF
content_hash: caad9d9e8c81435aea7b89db84345722427ee33c0f00ea1502f09326b3ebed8a
fetched_at: '2026-06-28T22:44:06.999984+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Erro validador DIRF 2024 "Registro não está de
  acordo com o leiaute do arquivo de importação"
type: support-article
updated_at: '2025-08-15T11:47:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21164679626903-RH-Linha-Protheus-GPE-Erro-validador-DIRF-2024-Registro-n%C3%A3o-est%C3%A1-de-acordo-com-o-leiaute-do-arquivo-de-importa%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21164679602071) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao importar o arquivo da DIRF 2024 - Ano Calendário 2023, é apresentado o erro abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21164695468439)  
**Ambiente**Totvs RH - Totvs RH (Linha Protheus) - Gestão de Pessoal - À partir do release 12.1.33  
  
**Causa**O problema ocorre quando o ambiente não esta atualizado para a DIRF 2024, dessa forma, no arquivo magnético é gerado o identificador de estrutura de *layout* de anos anteriores, e ao importar no PGD o erro é apresentado.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Verifique se o pacote da DIRF 2024 já foi aplicado em seu ambiente.  
**[Clique Aqui para Acessar a Expedição contínua do RH](https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/RH_EXPEDICAO_CONTINUA)   
VERSÃO 12.1.2310 SOMENTE PARA CLIENTES COM GARANTIA ESTENDIDA**  
2. Acesse Miscelânea / DIRF / Arquivo Magnético (GPEM590) e verifque o preenchimento das perguntas.  
Para a DIRF 2024, deve ser preenchido o Ano Calen´daio 2023 e Ano Base 2024, como no exemplo abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21164695471383)  
  
3. Verifique se na primeira linha do arquivo magnético gerado foi gerado o código B3VH8RQ:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21164679607831)  
  
4. Importe o arquivo no PGD novamente.

**Saiba Mais:**  
[RH - DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF)
