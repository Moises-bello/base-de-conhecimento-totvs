---
article_id: 360028934251
category: Financeiro - Contas a Pagar
content_hash: 37df1bf65ff8078e6f40d0ad1ccc73ec7a7773a480b32abaab8c1ca8898ec46e
fetched_at: '2026-06-28T22:38:08.538033+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA050 - Cadastro
  de Valores Acessórios
type: support-article
updated_at: '2025-10-17T12:10:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028934251-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA050-Cadastro-de-Valores-Acess%C3%B3rios
---

**Dúvida**  
Como desabilitar função que solicita a inclusão de valores acessórios na inclusão de títulos na FINA050?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**1 - Acesse o **Configurador >** **Base de Dados** > **Dicionário** > **Base de Dados**. Segue tela abaixo:  
  
![](https://totvssuporte.zendesk.com/attachments/token/Z2qstly0vOjS3jDJBKGpHFySk/?name=inline2131726897.png)  
  
2. Selecione **Perguntas** e, na **Lupa**, destaque (em amarelo) e digite: **FIN050**, clique em **editar**:  
  
![](https://totvssuporte.zendesk.com/attachments/token/iFd7ZLnaLCh6BgGrDJXo84cDL/?name=inline-1447824709.png)  
  
3. Incluir a pergunta 11, como mostrado abaixo:   
  
![](https://totvssuporte.zendesk.com/attachments/token/Fgrga0uZZzcGHXxj6kCBtFFX1/?name=inline1493319360.png)

* Pergunta:  
  + Valores Acessórios Inclusão ?
  + ¿Valores accesorios inclusión
  + Accessory Value Inclusion ?
* Tipo: Numérico
* Tamanho: 1
* Decimal: 0
* Formato:
* Help:  
  Indique se, após confirmada a inclusão  
  do título, será apresentada tela para  
  cadastro dos valores acessórios deste.  
  Sim - Apresenta a tela para inclusão dos  
  valores acessórios  
  Não - Não apresenta.  
  Obs: Caso não seja completada a inclusão  
  de valores acessórios, é possível o  
  Cadastro destes valores via Outras Ações.  
  - Valores Acessórios.
* Objeto: 3 - Combo
* Pré-Seleção: 1
* Item 1:  
  + Sim
  + Si
  + Yes
* Item2:  
  + Não
  + No
  + No

![](https://totvssuporte.zendesk.com/attachments/token/mst3K6UyZ6T1piPzb7Tnh5Pxp/?name=inline1632334526.png)  
![](https://totvssuporte.zendesk.com/attachments/token/VHcLLrmMKh7bU4r9iLNV9q4SS/?name=inline1599401710.png)

4 - Reinicie o *Protheus. Na* rotina de **Contas a Pagar** (FINA050), selecione **F12**, verifique se a pergunta aparece na tela dos **parâmetros** e se o conteúdo está como **Não,** como mostrado abaixo:  
  
![](https://totvssuporte.zendesk.com/attachments/token/1wivXHxSV50sceY7nCSF2kxER/?name=inline-1653317119.png)
