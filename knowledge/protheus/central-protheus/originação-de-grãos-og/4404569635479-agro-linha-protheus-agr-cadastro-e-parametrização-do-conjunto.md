---
article_id: 4404569635479
category: Originação de Grãos (OG)
content_hash: 2325f10d03e2779e2c6b4c29ff0afedaba4eea6dd1ddbd86dbcecf17f424f8cc
fetched_at: '2026-06-28T22:45:37.399782+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Cadastro e Parametrização do conjunto
type: support-article
updated_at: '2025-06-23T15:55:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404569635479-Agro-Linha-Protheus-AGR-Cadastro-e-Parametriza%C3%A7%C3%A3o-do-conjunto
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20118714942999)** Tempo aproximado para leitura: **00:03:20 min****Dúvida**  
Como efetuar um cadastro sobre parametrização do conjunto para **Movimentação de Estoque Produto Pluma**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - A partir da versão 12  
  
**Solução**Neste exemplo vamos considerar que para compor o **fardinho**, teremos a pluma, o saco e o  
arame.  
  
**Configuração 01**:  
Parâmetro **MV\_AGRB002 igual a .T., ativo**.  
No cadastro de conjunto, este parâmetro atualiza a estrutura do produto pluma que gera produção com os itens adicionais incluídos no conjunto. Os ajustes feitos nos itens adicionais serão **salvos/atualizados** na estrutura do produto.  
A requisição dos itens será de forma automática conforme a estrutura do produto Pluma.  
Assim a estrutura do produto precisa ser a mais próxima possível do **fardinho**.  
  
**Exemplo:** A prensa utilizada gera **fardinhos** com peso médio de 200KG. Assim na estrutura para o algodão pluma será considerado 200KG o peso base, e para compor a estrutura deverá usar a pluma intermediária, mais o saco e o arame neste exemplo.  
Usando a requisição automática, poderá haver divergências, pois o peso do **fardinho** pode variar um pouco, mas os valores deverão ficar próximos do real.  
  
Abaixo segue exemplo deste cenário.

![CADAST.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6792353238935)

**Configuração 02**

![CADAST_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6792390132631)
