---
article_id: 360038027334
category: RH - Provisão
content_hash: 4ed4f0af3a6a88d3f0a596a2658b36526ddace20fbacc8e1cc51dc2a5d9c98d0
fetched_at: '2026-06-28T22:43:56.826502+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Relatório de Provisão de Férias e 13 º Salário
  Duplicado, após Transferência do Funcionário
type: support-article
updated_at: '2025-06-17T19:40:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038027334-RH-Linha-Protheus-GPE-Relat%C3%B3rio-de-Provis%C3%A3o-de-F%C3%A9rias-e-13-%C2%BA-Sal%C3%A1rio-Duplicado-ap%C3%B3s-Transfer%C3%AAncia-do-Funcion%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32879868966807)** Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Ao Calcular as Provisões de Férias e 13º Salário e emitir os relatórios, para funcionários que foram transferidos, o sistema apresenta as Provisões Duplicadas.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Ao emitir o relatório de provisão, o sistema emite o mesmo funcionário mais de uma vez, quando houve transferência.  
No exemplo abaixo, o funcionário é apresentado três vezes no relatório, sendo uma vez com Baixa de Transferência (Centro de Custo OP0601000), e duas vezes com Entrada do valor de provisão no mês (Centro de Custo GR0103000), conforme o exemplo abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049965654)

Para solucionar este incidente, realize os seguintes passos:  
**Observação:** Realize este procedimento primeiro em base teste.

1. Acesse o **Configurador** / **Base de Dados** / **Dicionário de Dados**, e verifique se o tamanho do campo Centro Custo está igual para todas as tabelas do Grupo 004;  
2. Abra a Tabela SRE em .DBF, e conte o tamanho do campo centro de custo (origem e destino), verifique se está de acordo com o tamanho do campo que foi apurado no passo 1.   
3. Acesse o **Configurador** / **Base de Dados** / **Dicionário de Dados** / **Grupo de Campos** / Selecione o Grupo **004 - Centro de Custo**, e altere o tamanho. Por exemplo se o tamanho atual do Centro de Custo for 13, altere o tamanho para 10, e Clique em Salvar e Atualizar;  
4. Realize o mesmo Procedimento de troca do tamanho de Centro de Custo, desta vez para o tamanho correto, neste exemplo a alteração deverá ser do tamanho 10, para 13 novamente. clique em Salvar e Atualizar;   
5. Ao solicitar atualização, o sistema irá ajustar suas tabelas que estiverem incorretas no banco;  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049966214)

Após atualização do tamanho do grupo de campo, o sistema passou a apresentar o relatório corretamente:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049966354)

**IMPORTANTE:** É possível validar também para o erro apresentado se o centro de custos que ocorreu movimentação de transferência para o funcionário não possui incorretamente mais de um registro na CTT, sendo um com campo filial preenchido e outro registro com o campo filial em branco. Sendo este o cenário será necessário excluir o registro indevido na tabela para que a geração do relatório seja impressa corretamente. 

**Saiba Mais:**  
[Página Centralizadora da Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
