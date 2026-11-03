---
article_id: 20118978173207
category: Originação de Grãos (OG)
content_hash: 081525e742e21a31ba4222b984ed2f189f25551c77ab3c148cc0820e19b53364
fetched_at: '2026-06-28T22:45:44.722712+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Processo para cadastro e Parametrização do conjunto
type: support-article
updated_at: '2025-06-18T14:42:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20118978173207-Agro-Linha-Protheus-AGR-Processo-para-cadastro-e-Parametriza%C3%A7%C3%A3o-do-conjunto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20118978147735) Tempo aproximado para leitura: **00:01:40 min****Ocorrência**  
No módulo **Comercialização (Linha Protheus) - Originação de Grãos (OG)**, ao realizar o processo para cadastrar uma balança é apresentada a ocorrência **Processo para cadastro e Parametrização do conjunto**.  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Causa**  
Esse incidente ocorre, pois é preciso realizar o processo para cadastro e parametrização do conjunto no Sistema.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes procedimentos:

Neste exemplo vamos considerar que para compor o **fardinho**, teremos a pluma, o saco e o  
arame.  
  
**Configuração 01**:  
Parâmetro **MV\_AGRB002 igual a .T., ativo**.  
No cadastro de conjunto, este parâmetro atualiza a estrutura do produto pluma que gera produção com os itens adicionais incluídos no conjunto. Os ajustes feitos nos itens adicionais serão **salvos/atualizados** na estrutura do produto.  
A requisição dos itens será de forma automática conforme a estrutura do produto Pluma.  
Assim a estrutura do produto precisa ser a mais próxima possível do **fardinho**.  
  
**Exemplo:** A prensa utilizada gera **fardinhos** com peso médio de 200KG. Assim na estrutura para o algodão pluma será considerado 200KG o peso base, e para compor a estrutura deverá usar a pluma intermediária, mais o saco e o arame neste exemplo.  
Usando a requisição automática, poderá haver divergências, pois o peso do **fardinho** pode variar um pouco, mas os valores deverão ficar próximos do real.  
  
Abaixo segue exemplo deste cenário.

![CADAST.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20118978150295)

**Configuração 02**

![CADAST_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20118978153495)
