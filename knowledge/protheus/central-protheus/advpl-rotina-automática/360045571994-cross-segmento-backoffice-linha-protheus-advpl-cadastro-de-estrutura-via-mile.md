---
article_id: 360045571994
category: ADVPL - Rotina Automática
content_hash: 84010939b0c8910276335fb56808a4c4949d1a8ced6c421b2d9048dea2a8eab6
fetched_at: '2026-06-28T22:40:23.928195+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - ADVPL - Cadastro de Estrutura
  via MILE '
type: support-article
updated_at: '2026-06-03T00:46:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045571994-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Cadastro-de-Estrutura-via-MILE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:03:00 min  
  
Dúvida**Como configurar o Layout para inclusão de estrutura (MATA200) via Acelerador MILE

**Ambiente**Protheus – ADVPL – A partir da versão 12.1.25  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
1. **Passo 1**;

Faça a configuração do layout de acordo com a documentação [MILE - Model Integrator Layout Engine](https://tdn.totvs.com/display/framework/MILE+-+Model+Integrator+Layout+Engine)

Para rotina Mata200 é necessário definir o Tabela Princiopal: SG1, Adapter : Mata200 e o Tipo do Adapter :MsExecauto conforme imagem abaixo

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063703494/mceclip3.png)

Defina o tipo do os separadores

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063702034/mceclip2.png)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063705474/mceclip4.png)

O Tipo de Execauto vai depender da estrutura da rotina que no caso da Mata200 é o modelo 2.

Opçoes:

1= **Modelo 1** (Tabela simples)  
2= **Modelo 2** (1 Tabela com cabeçalho/ítens)  
3= **Modelo 3** (2 Tabelas diferentes cabeçalho/ítens)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063713174/mceclip6.png)

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063714334/mceclip7.png)

Faça a inclusão do canal

**Botão** **Incluir**: Inclui um novo canal.

**ID Saída**: Identifica o destino dos dados.

Se o tipo de adapter for rotina automática (MSExecAuto), deve ser MASTER ou DETAIL conforme o modelo do rotina automática 

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063717034/mceclip8.png)  
2. **Passo 2.**

Definir os campos do Canal MASTER

Em especifico na Mata200 devem conter os campos G1\_COD, G1\_QUANT, NIVALT, ATUREVSB1

Neste caso em especifico é necessário a utilização das variáveis que serão adicionadas como campo NIVALT, ATUREVSB1

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063729374/mceclip9.png)  
3.  **Passo 3**.

inclua o Canal Detail e os campos da tabela G1\_FILIAL, G1\_COD, G1\_COMP, G1\_TRT, G1\_QUANT, G1\_PERDA (obs.: essa campos são os principais para permitir a inclusão)

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063729714/mceclip10.png)

4. **Passo 4**

Importação do arquivo Txt ou Csv.

**![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063797214/mceclip11.png)**

Exemplo de Csv.

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360064800993/mceclip12.png)
