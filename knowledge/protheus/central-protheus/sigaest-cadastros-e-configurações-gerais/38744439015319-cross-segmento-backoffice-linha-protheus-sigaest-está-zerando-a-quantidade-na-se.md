---
article_id: 38744439015319
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: ef18ced6c90b71802926de943db125f77244d5b95168f8ce594c8b6e638d8d73
fetched_at: '2026-06-28T22:39:09.802840+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento – Backoffice (Linha Protheus) – SIGAEST – Está zerando a quantidade
  na segunda UM quando não há fator de conversão
type: support-article
updated_at: '2026-03-19T17:40:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38744439015319-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Est%C3%A1-zerando-a-quantidade-na-segunda-UM-quando-n%C3%A3o-h%C3%A1-fator-de-convers%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38744439002135) Tempo aproximado para leitura: **00:02:13 min**  
  
**Ocorrencia**  
Ao informar manualmente a quantidade na **Primeira Unidade de Medida (1ª UM)** e, em seguida, preencher a **Segunda Unidade de Medida (2ª UM)**, o sistema zera automaticamente a quantidade anteriormente digitada.

O comportamento ocorre da seguinte forma:

* Quando o produto **não possui fator de conversão cadastrado**, ao preencher a **2ª UM**, o sistema preenche automaticamente com **0** o campo da **1ª UM**.
* Da mesma forma, ao preencher a **1ª UM**, o sistema preenche automaticamente com **0** o campo da **2ª UM**.

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Causa**

O sistema realizava tentativa de conversão entre unidades de medida mesmo quando o produto não possuía fator de conversão informado, resultando na anulação da quantidade digitada na outra unidade.

**Solução**  
O programa foi ajustado para **não efetuar a conversão de unidade de medida quando o produto não possuir fator de conversão cadastrado**.

A partir da aplicação da correção:

* As quantidades informadas na **1ª UM** e na **2ª UM** permanecerão conforme digitadas pelo usuário.
* Não ocorrerá mais o preenchimento automático com valor zero.

### **Pacote de Atualização**

Aplicar o pacote correspondente à sua versão:

* **12.1.2310**: <https://r.totvs.io/p/1238526>
* **12.1.2410**: <https://r.totvs.io/p/1238524>
* **12.1.2510**: <https://r.totvs.io/p/1238525>

### **Documentação da Solicitação**

Para mais detalhes técnicos, acesse a documentação oficial:

<https://tdn.totvs.com/pages/releaseview.action?pageId=1042925471>

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
