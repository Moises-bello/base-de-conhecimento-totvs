---
content_hash: c97ea964eb1124e2377670d732b083d01fada5daa400bf149ab92d6e269a1663
fetched_at: '2026-06-29T00:05:50.969358+00:00'
page_id: '1046427837'
product: rm
source: tdn-rm
title: Novo Resíduo - Componente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1046427837
version: 10
---

### Sumário

1. **Conceito do Resíduo Anual**
2. **Objetivos da Funcionalidade**
3. **Quando Utilizar**
4. **Vantagens e Desvantagens**
5. **Pré-requisitos para Utilização**
6. **Fluxo Completo do Processo**
7. **Passo a Passo Operacional**
8. **Exemplo Prático**
9. **Perguntas Frequentes**
10. **Glossário**

01Conceito |

### t

### 1. Conceito do Resíduo Anual

O **Resíduo Anual** é um mecanismo financeiro utilizado em contratos de financiamento imobiliário que possuem cláusula de reajuste periódico (geralmente anual). Durante o período de 12 meses entre um reajuste contratual e outro, podem ocorrer correções monetárias intermediárias (mensais, por exemplo) que geram diferenças entre o valor original da parcela e o valor corrigido.

O resíduo é exatamente o **acúmulo dessas diferenças** ao longo do período. Em vez de cobrar essas diferenças imediatamente a cada mês, o sistema as acumula até o seu **próximo aniversário** e consolida em uma **única parcela extra** ao final do ciclo de 12 meses ou **distribui** nas próximas parcelas em aberto.

**Características principais:**

* Período de acumulação: 12 meses
* Geração:

  + Parcela única ao final do período
  + Distribui nas próximas parcelas em aberto
  + Esses valores podem sofrer novos reajustes e incidir juros de contrato
2Objetivos |

### t

### 2. Objetivos da Funcionalidade

A funcionalidade de Resíduo Anual foi desenvolvida para:

* **Manter a estabilidade mensal:** Evita que o mutuário tenha que arcar com pequenas variações mês a mês, mantendo as parcelas mensais com valores previsíveis.
* **Automatizar cálculos complexos:** O sistema realiza automaticamente todos os cálculos das diferenças acumuladas, eliminando erros manuais.
* **Garantir a aderência contratual:** Assegura que todas as correções previstas em contrato sejam aplicadas corretamente, mesmo que em momento distinto do pagamento mensal.
* **Facilitar a gestão de contratos:** Se utilizar a opção de gerar uma única parcela o ajuste anual, simplificará a administração de contas a receber.
2Quando Utilizar |

### t

### 3. Quando Utilizar

Esta funcionalidade é recomendada para:

| Cenário | Aplicabilidade |
| --- | --- |
| Contratos com reajuste anual de parcelas | ✅ Altamente recomendado |
| Financiamentos com correção monetária mensal | ✅ Necessário para compatibilização |
| Contratos onde o componente Principal é do tipo Modelo Padrão | ✅ Obrigatório |
| Vendas que utilizam modalidade específica para Resíduo | ✅ Obrigatório |
| Contratos com periodicidade de correção diferente de 12 meses | ❌ Não aplicável |

2Vantagens |

### t

### 4. Vantagens e Desvantagens

### Vantagens

| Aspecto | Benefício |
| --- | --- |
| **Para o Cliente** | Previsibilidade orçamentária mensal, sem oscilações inesperadas |
| **Para a Administradora** | Garantia de aplicação correta de todos os reajustes contratuais |
| **Operacional** | Processo automatizado, reduzindo trabalho manual e erros |
| **Financeiro** | Transparência no acúmulo e cobrança das diferenças |
| **Contábil** | Rastreabilidade completa de todos os cálculos realizados |

### Desvantagens

| Aspecto | Desafio |
| --- | --- |
| **Para o Cliente** | Impacto financeiro concentrado na parcela de resíduo |
| **Comunicação** | Necessidade de explicação clara ao cliente sobre o mecanismo |
| **Liquidez** | Pode exigir do cliente um planejamento financeiro anual |
| **Operacional** | Exige parametrização correta desde a origem do contrato |

2Pré-requisitos |

### t

### 5. Pré-requisitos para Utilização

Antes de iniciar o processo de Resíduo Anual, verifique se todos os requisitos abaixo estão atendidos:

### Cadastros Básicos

* Componente de Resíduo cadastrado com a opção **"Na Geração do Plano de Financiamento"**
* Modalidade de venda específica parametrizada para Resíduo Anual
* Componente Principal configurado preferencialmente como **Modelo Padrão**

### Condições de Venda

* Flag **"Reajuste sobre o Resíduo da Parcela Quitada"** marcada
* Periodicidade dos componentes de correção: **mensal**
* Ciclo de correção: **12 meses**
2Fluxo |

### t

### 6. Fluxo Completo do Processo

2Passo a Passo |

### t

## 7. Passo a Passo Operacional

### Etapa 1: Parametrização Inicial

**1.1 Cadastro do Componente de Resíduo**

* Acesse: Módulo de Parametrização > Componentes
* Localize ou crie o componente de Resíduo
* No campo **Surgimento do Componente**, selecione: `Na Geração do Plano de Financiamento`

**1.2 Cadastro da Modalidade de Venda**

* Acesse: Vendas > Modalidades de Venda
* Crie/edite a modalidade com as configurações específicas para Resíduo Anual

### Etapa 2: Criação do Contrato

**2.1 Cadastrar nova venda**

* Utilize a modalidade de venda parametrizada para Resíduo Anual

**2.2 Configurar Condições de Venda**

* Na aba **Condições de Venda**, localize o componente de Resíduo
* Marque as flags do campo **Reajuste sobre o "Resíduo da Parcela Quitada"**
* Verifique a periodicidade dos componentes de correção monetária (antes e após) e Juros de contrato: devem estar com **periodicidade mensal de 12 meses**

**2.3 Gerar o Plano de Financiamento**

* Confirme a geração do plano com as configurações realizadas

### Etapa 3: Execução Mensal (repetir por 12 meses)

**Mês a mês, realize:**

1. **Reajuste Monetário** da parcela do mês
2. **Baixa da parcela reajustada** (quitação)
3. **Reajuste do Resíduo** (o sistema acumula a diferença)

### Etapa 4: Geração da Parcela de Resíduo (ao final dos 12 meses)

**4.1 Acessar a funcionalidade**

* Menu: **Contratos | Contratos de Vendas e Aluguéis**
* Selecione a venda desejada
* Clique em: **Processos | Gerar Parcela de Resíduo**

**4.2 Tela de Geração**  
Ao acessar, o sistema exibirá uma tela contendo:

* Lista de todas as parcelas da venda já quitadas
* Para cada parcela: o valor do resíduo calculado
* Campo **Parcela Resíduo**: pré-visualização da nova parcela

**Informações da nova parcela:**

| Campo | Origem |
| --- | --- |
| Valor | Soma de todos os resíduos calculados |
| Número da parcela | Gerado automaticamente pelo sistema |
| Grupo da parcela | Conforme parametrização |
| Data de vencimento | Conforme parametrização |

**4.3 Confirmar geração**

* Revise as informações
* Confirme a operação
* A nova parcela será incluída no plano de financiamento
2Exemplo |

### t

## 8. Exemplo Prático

### Cenário Ilustrativo

**Dados do contrato:**

* Parcela base: R$ 1.000,00
* Índice de correção: 1% ao mês
* Período: Janeiro a Dezembro/2023

**Mês a mês:**

| Mês | Parcela Paga | Valor Corrigido | Resíduo Acumulado |
| --- | --- | --- | --- |
| Jan | R$ 1.000,00 | R$ 1.000,00 | R$ 0,00 |
| Fev | R$ 1.000,00 | R$ 1.010,00 | R$ 10,00 |
| Mar | R$ 1.000,00 | R$ 1.020,10 | R$ 30,10 |
| Abr | R$ 1.000,00 | R$ 1.030,30 | R$ 60,40 |
| ... | ... | ... | ... |
| Dez | R$ 1.000,00 | R$ 1.115,68 | R$ 667,43 |

**Resultado final:**  
Em dezembro, o sistema gerará uma parcela de resíduo no valor de **R$ 667,43**, que representa a soma de todas as diferenças não pagas durante o ano.

2FAG |

### t

### 9. Perguntas Frequentes

### 1. O resíduo é obrigatório em todos os financiamentos?

Não. O resíduo é uma configuração específica para contratos que possuem reajuste anual e correções intermediárias. Deve ser utilizado conforme a necessidade do negócio.

### 2. O que acontece se eu não gerar a parcela de resíduo?

As diferenças acumuladas continuarão registradas no sistema, mas não serão cobradas formalmente do cliente, podendo causar inconsistências financeiras no contrato.

### 3. A parcela de resíduo também sofre reajuste?

Sim. Conforme a documentação, a parcela de resíduo "poderá sofrer reajustes monetários e de juros" após sua geração, como qualquer outra parcela do financiamento.

### 4. Posso gerar o resíduo antes de completar 12 meses?

Não. O sistema foi projetado para acumular as diferenças por exatos 12 meses. A geração antecipada não é suportada.

### 5. O que fazer se uma parcela do período não foi quitada?

O sistema considera apenas as parcelas quitadas para o cálculo do resíduo. Parcelas em aberto ou não pagas não entrarão no cálculo até sua quitação.

2 Glossário |

### t

### 10. Glossário

| Termo | Definição |
| --- | --- |
| **Resíduo** | Diferença acumulada entre o valor pago e o valor corrigido da parcela |
| **Parcela de Resíduo** | Parcela única gerada ao final de 12 meses contendo todos os resíduos acumulados |
| **Surgimento do Componente** | Parametrização que define em que momento o componente entra no plano |
| **Modelo Padrão** | Tipo específico de componente Principal necessário para o funcionamento do resíduo |
| **Reajuste do Resíduo** | Processo mensal que calcula e acumula as diferenças das parcelas |
| **Geração do Plano de Financiamento** | Momento em que o plano de pagamento é criado no sistema |

---
