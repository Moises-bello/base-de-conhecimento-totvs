---
article_id: 360021721132
category: RH – DIRF
content_hash: 8faa3a0ab5a2bf04bf7c72087c736fb6d9d98b182ae0e0b186152486adb8787f
fetched_at: '2026-06-28T22:44:06.991414+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Erro validador DIRF 2021 "Registro não está de
  acordo com o leiaute do arquivo de importação"
type: support-article
updated_at: '2025-08-22T18:50:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021721132-RH-Linha-Protheus-GPE-Erro-validador-DIRF-2021-Registro-n%C3%A3o-est%C3%A1-de-acordo-com-o-leiaute-do-arquivo-de-importa%C3%A7%C3%A3o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34376739500695) Tempo aproximado para leitura: **00:01:00 min*****

**Ocorrência**Ao importar o arquivo magnético da DIRF 2021 para o validador, o seguinte erro é apresentado:  
**Registro não está de acordo com o leiaute do arquivo de importação - Não foi encontrada sequencia valida de registros DIRF + RESPO + DECPJ + ou DECPF no inicio do arquivo.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018763452)**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**  
O problema ocorre pois o ambiente não esta atualizado para a DIRF 2021, dessa forma, no arquivo magnético é gerado o identificador de estrutura de *layout* de anos anteriores, e ao importar no PGD 2021, o erro é apresentado.  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
1. **Aplique** o pacote de atualização para DIRF;  
2. Gere a DIRF novamente no menu **GPEM550**;  
3. Gere novamente o arquivo magnético na rotina **GPEM590**;  
4. Verificar na linha 1 se o registro passou a ser **VR4QLM8**;  
5. No arquivo magnético a primeira linha deve ficar **DIRF|2021|2020|N||VR4QLM8|**  
  
**Saiba Mais**Para baixar o pacote de atualização e mais informações sobre a **DIRF 2021** acesse a página centralizadora:   
[DIRF - Declaração do Imposto de Renda Retido na Fonte | Protheus.](http://tdn.totvs.com/pages/viewpage.action?pageId=329035626)

**Saiba Mais:**

[RH-DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF?page=2#articles)
