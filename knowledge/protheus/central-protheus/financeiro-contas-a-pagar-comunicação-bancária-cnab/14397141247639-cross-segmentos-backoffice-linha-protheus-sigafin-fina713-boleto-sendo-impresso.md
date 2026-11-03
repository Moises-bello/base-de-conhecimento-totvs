---
article_id: 14397141247639
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 934c71f58fcad65972b5f74171d2e53609a2e37c43d510a53a7c7039669407fb
fetched_at: '2026-06-28T22:37:56.305954+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA713 - Boleto sendo
  impresso sem código de barras e sem linha digitável
type: support-article
updated_at: '2024-01-22T15:00:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14397141247639-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA713-Boleto-sendo-impresso-sem-c%C3%B3digo-de-barras-e-sem-linha-digit%C3%A1vel
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Boleto sendo impresso sem código de barras e sem linha digitável  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**Validar credencias da configuração do banco, caso o mesmo esteja apontado para base homologação, por padrão o boleto será gerado sem **código de barras** e sem **linha digitável**.

Como validar se a configuração está apontado para base homologação do banco.

1º Opção: Acessar a rotina **Novo Gestor Financeiro** (**FINA710**) -> Comunicação Online -> **Configuração** **de Contas** -> **Posicionar no banco** -> **Editar**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14397140133143)

**Configurar Credenciais** e validar se está seleciona base **Homologação** ou **Produção**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14397205754263)

2º Opção: Validar Pelo *Json* de configuração.

Podemos validar o *JSON* de configuração da tabela **SA6,** campo **A6\_CFGBOL.** a TAG **"****environment"** irá apontar para qual base do banco está configurado.

**"environment": "2", ->** Homologação 

**"environment": "1", ->** Produção

**Exemplo** Homologação**:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14397503230615)
