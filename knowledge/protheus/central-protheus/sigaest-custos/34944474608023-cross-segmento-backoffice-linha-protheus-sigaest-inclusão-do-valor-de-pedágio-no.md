---
article_id: 34944474608023
category: SIGAEST - CUSTOS
content_hash: 853718b9cd79b4d332e703d2c47f70bce6eb4118141b3fd2fff4f22664c9281c
fetched_at: '2026-06-28T22:39:00.476950+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST -Inclusão do valor de
  pedágio no custo do produto da nota fiscal F1_VALPEG
type: support-article
updated_at: '2025-11-17T13:37:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34944474608023-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Inclus%C3%A3o-do-valor-de-ped%C3%A1gio-no-custo-do-produto-da-nota-fiscal-F1-VALPEG
---

No padrão do TOTVS Protheus, o valor do pedágio (campo F1\_VALPEG) não compõe o custo do produto na nota fiscal, a menos que o campo F4\_AGRPEDG esteja configurado como 2 ("Agregar o valor do pedágio, somente no total da NF"). Caso contrário, o valor do pedágio não impacta diretamente o custo do item. Para incluir o pedágio no custo, pode-se usar o campo de Despesas na nota fiscal ou implementar o ponto de entrada A103CUST para manipular o custo de entrada.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34944474595351) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**

É possível incluir o valor do pedágio (campo F1\_VALPEG) no custo do produto da nota fiscal?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

No padrão, o valor informado no campo **F1\_VALPEG** não compõe o custo do produto ao lançar a nota fiscal.

Somente irá compor esse valor no custo do produto quando o campo **F4\_AGRPEDG** estiver com conteúdo como 2 "Agregar o valor do pedágio, somente no total da NF".

Pois no padrão esse campo na TES vem com conteúdo como 3 = **"Não considera o valor digitado".** E com isso o valor não entra no custo do produto.

O pedágio, assim como os demais componentes do grupo **Comp**, integra o valor total da prestação de serviços (**vPrest**). Dessa forma, entende-se que os componentes listados possuem caráter apenas exemplificativo e não impactam diretamente o custo do item.

[CT-e - Campo CST - Valor do Pedágio ou Vale Pedágio](CT-e%20-%20Campo%20CST%20-%20Valor%20do%20Ped%C3%A1gio%20ou%20Vale%20Ped%C3%A1gio)

Caso seja necessário que o valor do pedágio componha o custo do produto, há duas alternativas quando não puder preencher esse campo da TES  **F4\_AGRPEDG** = 2:

* Utilizar o campo de **Despesas**, disponível na aba **Descontos\Fretes\Despesas** da nota fiscal;
* Implementar o ponto de entrada **A103CUST**, que permite manipular o custo de entrada.

  [A103CUST - Manipula Custo de Entrada](https://tdn.totvs.com/display/public/PROT/A103CUST+-+Manipula+Custo+de+Entrada)

  Criar regra via configurador de tributos: [Central de Conteúdo | Reforma Tributária e Configurador de Tributos](https://tdn.totvs.com/x/FMhZO)

***Saiba mais:***

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)
