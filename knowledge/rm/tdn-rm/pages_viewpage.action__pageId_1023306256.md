---
content_hash: 27d0ec776191bfcb5b9e5870198dce66ec30d9bf9a259c27d96588b53da8da56
fetched_at: '2026-06-29T00:05:48.144344+00:00'
page_id: '1023306256'
product: rm
source: tdn-rm
title: Reforma Tributária - Regra Redutora
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1023306256
version: 8
---

## **Regra Redutora**

## Cadastro de Redutores da Base de Cálculo do IVA

### Objetivo

Para atender às exigências da **Reforma Tributária**, o TOTVS Construção Gestão de Imóveis disponibiliza um cadastro específico para os **Redutores da Base de Cálculo do IVA**, permitindo o correto controle, aplicação e auditoria dos benefícios fiscais previstos para o setor imobiliário.

### Funcionalidade

O sistema disponibiliza:

* Uma **tabela dedicada** para armazenamento dos redutores;
* Uma **interface de manutenção** para inclusão, alteração, consulta e exclusão dos registros.

Esses dados serão utilizados automaticamente nos cálculos do IVA, conforme a legislação vigente e o tipo de contrato vinculado ao movimento.

### Tipo de Contrato

O redutor deverá ser cadastrado considerando o **tipo de contrato** ao qual será aplicado:

* **Venda**
* **Aluguel**
* **Condomínio / Empreendimento**

Essa informação é fundamental para que o sistema aplique corretamente o redutor nos cálculos fiscais correspondentes.

### Informações Cadastradas

No cadastro de redutores da base de cálculo do IVA, deverão ser informados os seguintes campos:

* **Tipo de Contrato**  
  (Venda, Aluguel, Condomínio ou Empreendimento)
* **Tipo de Redutor**

  + **Social – Imóveis Residenciais**  
    Utilizado para aplicação de benefícios fiscais previstos para **operações com imóveis residenciais de caráter social**, abrangendo **venda e locação**, conforme legislação vigente.
  + **Ajuste** é um valor calculado por empreendimento e depois distribuído a cada unidade de forma proporcional por fração ideal
  + **Outros**  
    Utilizado para demais reduções legais da base de cálculo do IVA que não se enquadram como redutor social.
* **Valor do Redutor**  
  Percentual ou valor definido conforme a legislação aplicável.
* **Data (Competência)**  
  Mês e ano de vigência do redutor.
* **Índice / Moeda**  
  Índice ou moeda utilizada para atualização do valor, quando aplicável.
* **Defasagem**  
  Período de defasagem considerado para aplicação do índice informado.

### Aplicação no Cálculo do IVA

As informações cadastradas neste parâmetro são utilizadas automaticamente pelo sistema para:

* Reduzir corretamente a base de cálculo do IVA;
* Garantir aderência às regras da Reforma Tributária;
* Evitar inconsistências fiscais nos documentos emitidos.

#### 🧮 Passo 1: Como calcular o Redutor de Social

A Reforma Tributária estabeleceu **três redutores sociais claros** para o setor imobiliário, todos corrigidos pelo IPCA:

1. **R$ 100 mil** para imóveis residenciais novos (apartamentos e casas)
2. **R$ 30 mil** para lotes residenciais
3. **R$ 600 mensais** para locações residenciais

#### 🧮 Passo 2: Como calcular o Redutor de Ajuste do Empreendimento

Para um empreendimento que está em construção em **31 de dezembro de 2026**, o redutor de ajuste total é a soma de três componentes básicos, todos corrigidos pelo IPCA até a data da venda :

1. **Valor do Terreno:** O custo de aquisição do terreno, devidamente atualizado pelo IPCA até 31/12/2026 .
2. **Custos Incorridos:** Todos os bens e serviços adquiridos e contabilizados como custo de produção **até 31/12/2026**. Isso inclui materiais de construção, mão de obra, projetos, etc., desde que comprovados por documentação fiscal idônea .
3. **Custos de Transação e Contrapartidas:** O valor do **ITBI** pago na aquisição do terreno, bem como **contrapartidas urbanísticas ou ambientais** pagas ou entregues ao poder público (ex: outorga onerosa, áreas doadas) .

> **Fórmula básica:**  
> **Redutor do Empreendimento** = (Valor do Terreno atualizado) + (Custos incorridos até 2026) + (ITBI + Contrapartidas)

**Exemplo prático :**

* Terreno adquirido em 2025: R$ 2 milhões
* ITBI pago: R$ 100 mil
* Obra realizada até 31/12/2026: R$ 5 milhões
* **Redutor total do empreendimento:** R$ 7,3 milhões (atualizado pelo IPCA)
* **Aplique o percentual da fração ideal** de cada unidade sobre o redutor total e proporciona esse valor por parcela financeira.

### Controle e Auditoria

Todas as operações realizadas no cadastro de redutores — **inclusões, alterações ou exclusões** — são registradas em **log de auditoria**, garantindo:

* Rastreabilidade das informações;
* Transparência nos ajustes fiscais;
* Atendimento às exigências de fiscalização e auditoria tributária.

### Disponibilidade

Esta funcionalidade está disponível a partir da versão:

**12.1.2502 – TOTVS Construção Gestão de Imóveis**

> **Importante**  
> As configurações devem ser realizadas com atenção, pois impactam diretamente o cálculo do IVA nos contratos e movimentos fiscais do sistema.
