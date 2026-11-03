---
article_id: 360028834211
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: e8edc187b75bbfc25de4c5f43443bfc2ebdecf43264752b906f7f518f6747714
fetched_at: '2026-06-28T22:42:44.406968+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem A690NAOCA1
type: support-article
updated_at: '2021-09-28T18:33:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028834211-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-A690NAOCA1
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:12 min****Ocorrência**Ao executar a rotina **MATA690 - Carga Máquina** é apresentada a mensagem **A690NAOCA1**.  
  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
 **Causa**A mensagem **A690NAOCA1** surge quando a pasta na qual o **MATA690** irá gravar e manipular arquivos não existe no ambiente, a mensagem surge também quando **o roteiro** não é encontrado.   
  
 **Solução**Para solucionar essa dúvida, realize os seguintes passos:  
 1. Dentro da pasta **Protheus\_Data**, crie uma subpasta para uso da rotina;  
 2. Edite o parâmetro **MV\_DIRPCP - Drive e diretório padrão que o Carga Máquina utiliza para a criação de arquivos de trabalho** e preencha com o nome da pasta criada;  
 3. Edite o parâmetro **MV\_PROCPCP - Drive e diretório onde serão processados os arquivos binários utilizados na Carga Máquina** e preencha com o nome da pasta criada;  
4. Informe um roteiro válido do produto no campo **C2\_ROTEIRO - Roteiro**.
