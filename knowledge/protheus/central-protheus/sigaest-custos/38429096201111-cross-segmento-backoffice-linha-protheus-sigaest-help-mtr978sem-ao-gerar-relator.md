---
article_id: 38429096201111
category: SIGAEST - CUSTOS
content_hash: ad2261022d299434c68f979660b1d3458913e24bc8593fc7d151a458689e6f14
fetched_at: '2026-06-28T22:39:01.961455+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - HELP MTR978SEM ao
  gerar relatorio MATR978
type: support-article
updated_at: '2026-02-16T14:36:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38429096201111-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-HELP-MTR978SEM-ao-gerar-relatorio-MATR978
---

O relatório MATR978, do TOTVS Protheus, só funciona para empresas que utilizam o conceito de Custo em Partes e possuem o ponto de entrada MA330CP devidamente desenvolvido e compilado. Sem ele, o relatório não processa dados e exibe erro; para Custo Médio padrão, utilize outros relatórios.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38429087449239) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Ao tentar abrir o relatorio MATR978 exibe o HELP MTR978SEM, oque fazer?

![HELPMATR978.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38429087449495)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
Ao tentar gerar o relatório **MATR978 (Custo em Partes x Custo Médio)**, o sistema interrompe a execução e apresenta o **HELP MTR978SEM**:

**Mensagem de Erro:**

> *"Não existe regra definida para utilização do custo em partes. Favor verificar se o ponto de entrada MA330CP esta compilado em seu ambiente."*

### 

O relatório **MATR978** é uma ferramenta de conferência **exclusiva** para empresas que utilizam a metodologia de **Custo em Partes** no Protheus.

O sistema emite este alerta porque não detectou o Ponto de Entrada **MA330CP** em seu repositório (RPO). Sem esse ponto de entrada, o motor de cálculo do estoque não possui as regras de negócio necessárias para "fatiar" o custo do produto (ex: separar o que é custo de matéria-prima, mão de obra, GGF, etc.), tornando a exibição do relatório impossível.

### **O que é o Custo em Partes?**

Diferente do Custo Médio padrão, que apresenta um valor único para o item, o **Custo em Partes** permite a decomposição do valor do produto em diferentes níveis de detalhamento. Isso é essencial para empresas que precisam de uma visão analítica sobre a composição financeira de seus produtos acabados.

* **Para saber mais sobre o conceito e como ele funciona, acesse:**

  [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Custo em Partes - Conceito e Configuração](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062926213-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Custo-em-Partes-Conceito-e-Configura%C3%A7%C3%A3o)

### **Orientações**

#### A. Se você **utiliza** o Custo em Partes:

Para que o relatório funcione, é obrigatório que o Ponto de Entrada **MA330CP** esteja:

1. Devidamente desenvolvido conforme as regras de negócio da sua empresa.
2. Compilado no RPO custom do ambiente em que o relatório está sendo executado.

#### B. Se você **NÃO utiliza** o Custo em Partes:

Caso sua empresa utilize apenas o Custo Médio padrão (sem decomposição), este relatório **não se aplica ao seu ambiente**.

* O erro apresentado é um comportamento esperado, pois o relatório não possui dados para processar sem a existência da regra customizada de partes.
* Para conferência de valores de estoque, utilize relatórios padrão como o **MATR900 (Kardex)** ou **MATR260 (Posição de Estoque)**.

---

> **Resumo:** O relatório MATR978 é dependente da customização via **MA330CP**. Se você não possui o ponto de entrada, o relatório não funcionará, pois ele foi desenhado especificamente para este cenário de gestão de custos.

---

***Saiba mais:***

[*MP - SIGAEST - Custo em Partes - Wizard para Criação dos Campos*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062945273)

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)
