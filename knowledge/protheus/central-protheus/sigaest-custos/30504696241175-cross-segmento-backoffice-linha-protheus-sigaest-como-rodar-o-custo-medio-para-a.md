---
article_id: 30504696241175
category: SIGAEST - CUSTOS
content_hash: c7f70df62c2125cca25ff6ceda1cda9102c95e6eb861ec2fa5adebbda587e56b
fetched_at: '2026-06-28T22:39:00.786995+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como rodar o custo
  medio para apenas um produto?
type: support-article
updated_at: '2025-05-09T14:15:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30504696241175-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-rodar-o-custo-medio-para-apenas-um-produto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30504696238615) Tempo aproximado para leitura: **00:01:00 min****Dúvida**A rotina de calculo de custo médio, processa sempre todos os itens, como definir para processar apenas 1 produto?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**

No **padrão do sistema**, a rotina de recálculo do custo médio **processa todos os registros de produtos**, não sendo possível restringir o cálculo a itens específicos sem uma customização ou alteração de procedures. Esse padrão ocorre pois o custo de um produto não é afetado apenas por sua própria movimentação, sendo possível haver diversos tipo de movimentos para um único produto que possuem relação com outros produtos como por exemplo: Produção, Transferência entre Produtos ou entre Filiais, havendo assim uma relação na composição de custo desses itens.

Se o custo desses outros produtos relacionados não tiverem sido calculados, a apuração de custo do produto processado nesse momento poderá ficar incorreta, gerando assim uma falsa sensação de que o custo foi recalculado e está correto, mas na realidade isso não aconteceu. 

Hoje existe apenas como desconsiderar produtos obsoletos durante o calculo, com uso das procedures e parametro MV\_A330GRV.

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Validação dos parâmetros MV\_A330GRV e MV\_A280GRV para produtos obsoletos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062164934-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Valida%C3%A7%C3%A3o-dos-par%C3%A2metros-MV-A330GRV-e-MV-A280GRV-para-produtos-obsoletos)

Como alternativa, esse comportamento pode ser implementada por meio de:

* **Ponto de Entrada**
* **Validação direta nas Procedures do banco de dados**

#### 

#### **Considerações sobre Personalizações**

A rotina, por padrão, **deve processar todos os itens** para evitar inconsistências nos custos e na ordenação dos movimentos. Qualquer alteração nas **procedures** ou nos **pontos de entrada** para definir o cálculo de produtos específicos deve ser **cuidadosamente analisada e testada**, pois pode gerar **graves problemas no cálculo dos custos**.

#### **Alternativas para Processamento de Itens Específicos**

Normalmente, há demanda para o cálculo de um produto específico, um grupo de produtos ou operações de produção com (OP), **especialmente para fins de testes internos**. Para esses casos, é possível adotar as seguintes abordagens:

1. **Via Pontos de Entrada**

   * [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Pontos de Entrada da rotina Recálculo do Custo Médio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003970802-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Pontos-de-Entrada-da-rotina-Rec%C3%A1lculo-do-Custo-M%C3%A9dio)
2. **Via Procedures Internas**

   * Implementação em conjunto com o seu analista **DBA** responsável
3. **Via Ajuste de Dados na Base**

   * Definição de critérios para processamento seletivo dos registros, garantindo que apenas produtos com movimentação sejam recalculados
   * Alterações realizadas exclusivamente por um **consultor in loco**

### **Observação**

Como esse **não é um comportamento padrão do sistema**, não há uma **documentação oficial** sobre como deve ser feito. No entanto, as possibilidades mencionadas podem ser consideradas para **fins de testes internos**.

**Saiba mais**:

*[Clique aqui e veja mais artigos sobre a Nova Jornada de Fechamento no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/5367899706647-ACOMPANHA-CUSTOS-JORNADA-DE-FECHAMENTO-NOVO-)*
