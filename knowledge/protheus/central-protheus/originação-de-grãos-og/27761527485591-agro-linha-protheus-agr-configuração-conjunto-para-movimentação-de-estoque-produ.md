---
article_id: 27761527485591
category: Originação de Grãos (OG)
content_hash: 35977e660fc735bb73daa6c2a3f2356b0941b9346f6700247fbc67ecf9a3bd1a
fetched_at: '2026-06-28T22:45:37.732150+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Configuração Conjunto para Movimentação de Estoque
  Produto Pluma - UBA
type: support-article
updated_at: '2025-07-12T10:53:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27761527485591-Agro-Linha-Protheus-AGR-Configura%C3%A7%C3%A3o-Conjunto-para-Movimenta%C3%A7%C3%A3o-de-Estoque-Produto-Pluma-UBA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27761546661655) Tempo aproximado para leitura: **00:02:30 min****Dúvida**  
Como realizar **Configuração Conjunto para Movimentação de Estoque Produto Pluma - UBA**?  
  
**Ambiente**TOTVS Agro – TOTVS Agro – Comercialização (Linha Protheus) - Originação de Grãos (OG) – Versão 12  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
  
**Visão Geral:**No cadastro de conjunto quando configurado para gerar movimentação de estoque do produto **pluma**, pode ser configurado para trabalhar com a requisição automática via a estrutura do produto, ou requisição manual conforme definido no conjunto.  
  
**Exemplo de Utilização:**Segue abaixo duas orientações de como cadastrar, parametrizar o conjunto com relação as movimentações do produto **pluma**.  
Neste exemplo vamos considerar que para compor o **fardinho**, teremos a **pluma, o saco e o arrame**.  
  
**Configuração 01:**Parâmetro **MV\_AGRB002 igual a .T., ativo**.  
No cadastro de conjunto, este parâmetro atualiza a estrutura do produto pluma que gera produção conforme os itens adicionais incluídos no conjunto. Os ajustes feitos nos itens adicionais serão **salvos/atualizados** na estrutura do produto.  
A requisição dos itens será de forma automática conforme a estrutura do produto **Pluma**. Assim a estrutura do produto precisa ser a mais próxima possível do **fardinho**.  
  
**Exemplo**: A prensa utilizada gera **fardinhos com peso médio de 200KG**. Assim na estrutura para o **algodão pluma será considerado 200KG** o peso base, e para compor a estrutura deverá usar a **pluma** intermediária, mais o **saco e o arrame** neste exemplo.  
Usando a requisição automática, poderá haver divergências, pois o peso do **fardinho** pode variar um pouco, mas os valores deverão ficar próximos do real.  
  
**Abaixo segue exemplo deste cenário:**

![BAU.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27761949343383)

**Configuração 02:**Parâmetro **MV\_AGRB002 igual a .F., desativado**.  
Com este parâmetro desativado, não será atualizado a estrutura da **Pluma** com os dados dos itens adicionais do conjunto.  
Os itens adicionais do conjunto não deverão ser cadastrados na estrutura da **pluma**, pois a requisição será manual gerado pelo encerramento do **fardão** conforme a quantidade de **fardinhos** gerados no beneficiamento.  
Na estrutura da pluma deverá ser cadastrado somente a **pluma** intermediaria neste cenário.  
Usando a requisição manual, a movimentação dos itens adicionais será conforme a quantidade de **fardinhos**.  
  
**Abaixo segue exemplo deste cenário**:

![BAU1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27761949349015)
