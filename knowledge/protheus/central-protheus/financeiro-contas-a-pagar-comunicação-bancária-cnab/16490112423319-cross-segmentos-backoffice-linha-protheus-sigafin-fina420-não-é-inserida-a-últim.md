---
article_id: 16490112423319
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 1736dd75ccaa386ca302e26ef56232718c4189315e5abb1fdd26087cc58c6be8
fetched_at: '2026-06-28T22:37:56.232927+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA420 - Não é inserida
  a última linha do arquivo
type: support-article
updated_at: '2023-08-02T20:59:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16490112423319-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA420-N%C3%A3o-%C3%A9-inserida-a-%C3%BAltima-linha-do-arquivo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16490158715927) Tempo aproximado para leitura: **00:04:00 min****Ocorrência**  
No módulo **Financeiro -> Comunicação Bancária -> Arquivos de Pagamentos (FINA420),** ao gerar o arquivo de remessa de pagamento, não gera a última linha em branco do arquivo, gerando rejeição ao importar o arquivo no Bankline **"Tamanho do registro X inválido".**  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**Esse incidente ocorre, pois nos parâmetros de Bancos, o campo **EE\_FIMLIN** não está sendo utilizado para geração da linha final.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acessar o módulo Configurador (SIGACFG) em  Base de dados -> Localizar a tabela SEE  
2. Localizar o campo **EE\_FIMLIN** e marcar como "**Usado**"   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16490074161687)  
3. Acessar a rotina FINA130 -> Parametros de Bancos, e informa = "SIM", gerar novamente o arquivo de remessa e será gerada a última linha do arquivo.  
  
**Saiba mais**[FINA130 - Parâmetros de Bancos](https://tdn.totvs.com/pages/viewpage.action?pageId=624116777)
