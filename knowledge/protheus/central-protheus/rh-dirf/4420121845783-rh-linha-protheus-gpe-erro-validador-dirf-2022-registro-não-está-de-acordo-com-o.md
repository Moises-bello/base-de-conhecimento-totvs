---
article_id: 4420121845783
category: RH – DIRF
content_hash: f5e85b7d7dd68ee25c80608c4b1cf045b8430a4d31280887ab2cc664864bc59f
fetched_at: '2026-06-28T22:44:06.996305+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Erro validador DIRF 2022 "Registro não está de
  acordo com o leiaute do arquivo de importação
type: support-article
updated_at: '2025-08-19T13:12:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420121845783-RH-Linha-Protheus-GPE-Erro-validador-DIRF-2022-Registro-n%C3%A3o-est%C3%A1-de-acordo-com-o-leiaute-do-arquivo-de-importa%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34286794837655)** Tempo aproximado para leitura: **00:01:00 min  
  
Ocorrência**  
Ao importar o arquivo magnético da DIRF 2022 para o validador, o seguinte erro é apresentado:  
Registro não está de acordo com o leiaute do arquivo de importação - **Não foi encontrada sequencia valida de registros** **DIRF + RESPO + DECPJ + ou DECPF no inicio do arquivo.**  
Conteúdo **2022/VR4QLM8.****Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da Versão 12.  
 **Causa**O problema ocorre pois o ambiente não esta atualizado para a **DIRF 2022**, dessa forma, no arquivo magnético é gerado o identificador de estrutura de *layout* de anos anteriores, e ao importar no **PGD 2022**, o erro é apresentado.  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4424825303447) **Solução**Para solucionar essa dúvida, realize os seguintes passos:  
**1.**Aplique o pacote de atualização para **DIRF;  
2.** Gere a DIRF novamente no menu **GPEM550;  
3.** Gere novamente o arquivo magnético na rotina **GPEM590;  
4.** Verifique na linha 1 se o registro passou a ser **XJFSFHB;  
5.** No arquivo magnético a primeira linha deve ficar **DIRF|2022|2021|N||XJFSFHB|**

Para acessar o **pacote de expedição continua do RH,** clique no *link*: <https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/rh_expedicao_continua>

**Saiba Mais:  
[RH-DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF?page=2#articles)**
