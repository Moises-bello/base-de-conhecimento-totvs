---
article_id: 38279591781015
category: SIGAEST - CUSTOS
content_hash: b10599c38b98a1014c00d6f191e7c4ef5036ca46c4240b8f83e2e4dd5502cb02
fetched_at: '2026-06-28T22:39:00.809896+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Conceito de saldos
  para produtos MOD e GGF
type: support-article
updated_at: '2026-02-09T19:45:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38279591781015-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-de-saldos-para-produtos-MOD-e-GGF
---

No TOTVS Protheus, produtos do tipo MOD (Mão de Obra Direta) e GGF (Gastos Gerais de Fabricação) podem apresentar saldos ou valores negativos no estoque, o que é conceitualmente correto, pois representam custos de serviço e não itens físicos, sendo consumidos sem entrada prévia. Isso não indica erro no sistema.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38279591771031) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Produto MOD/GGF estao ficando com saldos e valores negativos.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

## **Definição e Conceito**

No Protheus, produtos classificados com o tipo **MOD** (Mão de Obra Direta) ou **GGF** (Gastos Gerais de Fabricação) representam **custos de serviço e esforço fabril**. Diferente de matérias-primas ou produtos acabados, estes itens não possuem existência física tangível que justifique o armazenamento em prateleiras.

### **Características Principais:**

* **Natureza de Serviço:** São considerados insumos de custo para a composição do valor do produto acabado.
* **Ausência de Controle de Estoque Físico:** Por serem **imateriais**, esses produtos **não controlam "saldos"** no sentido tradicional (estoque).
* **Fluxo de Consumo:** São registrados norlmanente via requisições para Ordens de Produção (OPs) para que seu valor seja transferido ao custo do item que está sendo fabricado.

## **Comportamento de Saldos e Valores Negativos**

É extremamente comum e **conceitualmente correto** observar produtos do tipo MOD ou GGF com saldos ou valores **negativos** nas tabelas de estoque (como a `SB2`).

### **Por que o saldo fica negativo?**

1. **Requisição sem Entrada Prévia:** Como não se "compra" Mão de Obra para estocar, o sistema registra a saída (requisição para a OP) sem que tenha havido uma nota de entrada física.
2. **Apropriação de Custos:** O sistema permite a requisição desses itens para que o custo médio possa ser calculado. O saldo negativo é apenas um indicador de que o "serviço" foi consumido no processo produtivo.
3. **Interação Contábil:** Se a MOD possui integração contábil, os valores negativos na `SB2` refletem a contrapartida das apropriações de custos de produção de acordo com os lançamentos nos centros de custos do produto MOD.

## **Para que serve o produto MOD?**

O produto tipo **MOD** é utilizado para mensurar e aplicar o custo do tempo humano (ou operacional) despendido em uma etapa da produção.

* **Composição do Custo Médio:** Permite que o custo final do produto acabado inclua não apenas os materiais, mas também o valor da hora trabalhada.
* **Apuração de Eficiência:** Auxilia no rastreio de quanto tempo de mão de obra foi planejado versus o que foi efetivamente requisitado.
* **Absorção de Gastos:** Facilita a transferência de valores de centros de custo (Folha de Pagamento) para o estoque de produtos em elaboração.

## **Refaz Saldos (MATA300)**

Caso a empresa deseje zerar os saldos negativos para fins de limpeza visual ou organização de relatórios, utiliza-se a rotina **Refaz Saldos (MATA300)**.

Ao executar a MATA300, o sistema reprocessa as movimentações e, com base nos parâmetros (perguntas), pode ajustar o saldo atual conforme o histórico de entradas e saídas.

Dessa forma o produto MOD "sem integração" contabil, pode ter seu saldo zerado atualizado, saiba mais no boletim abaixo:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA300 - Refaz Saldos - Conceito e Informações](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420659401751-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA300-Refaz-Saldos-Conceito-e-Informa%C3%A7%C3%B5es)

**Não é um Erro o MOD ter saldo ou valor negativo:** Reforçamos que o saldo negativo nestes casos **não indica inconsistência de sistema**, mas sim a natureza operacional de um item que é consumido sem estoque prévio (visto que a "entrada" da MOD no custo costuma ocorrer via lançamento contábil ou integração de folha, e não via Nota Fiscal de Entrada).

**Saiba mais:**

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MOD/GGF - Conceito e Usabilidade*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402117444247)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Processo de configuração de MOD e GGF "Sem" e "Com" integração contábil*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402062082071-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Processo-de-configura%C3%A7%C3%A3o-de-MOD-e-GGF-Sem-e-Com-integra%C3%A7%C3%A3o-cont%C3%A1bil)

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)

[*MA330MOD - Customiza calculo do custo de mão-de-obra*](https://tdn.totvs.com/pages/releaseview.action?pageId=6087637)
