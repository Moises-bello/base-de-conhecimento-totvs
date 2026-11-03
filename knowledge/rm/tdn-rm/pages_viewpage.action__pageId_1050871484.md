---
content_hash: 0ef1eb54711d489ee75e5ea326ce572ab6b104631bbad48c892363d4a09a2365
fetched_at: '2026-06-29T00:05:51.523109+00:00'
page_id: '1050871484'
product: rm
source: tdn-rm
title: Integração - OQDigital - PI
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1050871484
version: 7
---

# Integração RM (ERP TOTVS) ↔ OQ Digital

**Arquitetura de Integração e Transformação do Processo Comercial**

---

# 1. Objetivo Estratégico

Este documento define o modelo de integração entre o **ERP RM (TOTVS)** e a **plataforma OQ Digital**, estabelecendo os fluxos técnicos necessários para sincronização de dados comerciais e ativação de inteligência de vendas.

O objetivo final da integração é **transformar o processo de vendas do mercado imobiliário**, utilizando tecnologia, engajamento e dados para aumentar performance comercial.

Resultados esperados com a utilização da plataforma OQ Digital integrada ao RM:

**Reduzir até 90% no custo por lead**  
**Aumentar a taxa de conversão para até 12,7%**  
**Acelerar as vendas em até 33%**

Esses resultados são alcançados através de:

* melhor qualificação de leads
* maior engajamento da rede de corretores
* uso de **gamificação e ranking comercial**
* acompanhamento contínuo da evolução de vendas

A integração permite que os dados comerciais gerados no RM alimentem a plataforma OQ Digital, criando um **ecossistema de inteligência e performance comercial**.

---

# 2. Modelo de Governança de Dados

A integração adota o princípio de **Source of Truth (Sistema Mestre)**.

### RM (ERP TOTVS)

Responsável pelos dados corporativos e comerciais:

* Corretores
* Imobiliárias
* Empreendimentos
* Leads
* Evolução comercial
* Aquecimento de leads
* Evolução de vendas

O RM também será responsável por **enviar continuamente para a OQ Digital as evoluções comerciais** dos corretores e de seus leads.

---

### OQ Digital

Responsável pelas funções de:

* geração de landing pages
* captação de leads
* engajamento da rede de corretores
* ranking e gamificação
* análise de performance comercial

A plataforma utiliza os dados recebidos do RM para **estimular comportamento comercial e aumentar a produtividade da força de vendas**.

---

# 3. Arquitetura de Integração

A comunicação entre os sistemas ocorre através de:

* **API REST**
* **Webhooks**

Fluxos de comunicação:

```
RM → OQ Digital
```

Envio de:

* corretores
* evoluções comerciais
* aquecimento de leads
* evolução de vendas

```
OQ Digital → RM
```

Envio de:

* leads capturados
* atualizações de leads
* eventuais atualizações de corretores

Todos os registros integrados devem possuir um **ExternalId imutável**, garantindo rastreabilidade entre as plataformas.

---

# 4. Fluxo Macro da Integração

```
RM (ERP / CRM)
   │
   │ Sincronização de dados
   ▼
OQ Digital
   │
   │ Captação de Leads
   ▼
Webhook
   │
   ▼
RM (Gestão Comercial)
```

Esse fluxo permite que a OQ Digital se torne uma **camada de aceleração comercial sobre o CRM do RM**.

---

# 5. Bootstrap da Integração (Carga Inicial)

Antes da operação contínua será realizada uma **sincronização inicial completa de dados**.

Objetivo:

Garantir que ambas as plataformas iniciem a operação com bases alinhadas.

---

## 5.1 Carga Inicial de Corretores

Fluxo:

```
RM → OQ  
OQ → RM
```

Objetivos:

* disponibilizar os corretores existentes
* habilitar campanhas e ranking de corretores

Corretores não devem ser removidos da integração, apenas **desativados quando necessário**.

---

## 5.2 Carga Inicial de Leads

Após a sincronização de corretores será realizada a sincronização inicial de leads.

Fluxo:

```
RM ↔ OQ  
OQ → RM
```

```

```

Objetivos:

* evitar duplicidade de registros
* preservar a jornada do cliente

---

# 6. Operação Contínua da Integração

Após a carga inicial, a integração passa a operar de forma **incremental e bidirecional para corretores e leads**.

O RM enviará continuamente para a OQ Digital:

* evoluções de corretores com seus leads
* evoluções de aquecimento de leads
* evolução de vendas

Essas informações são utilizadas pela OQ para **alimentar mecanismos de gamificação, ranking e inteligência comercial**.

---

## 6.1 Sincronização de Corretores

Alterações realizadas no RM devem ser refletidas na OQ.

Fluxo predominante:

```
RM → OQ
```

A integração também permite atualização de corretores pela OQ quando necessário.  
`OQ → RM`

---

## 6.2 Recebimento de Leads

Quando um lead for capturado na OQ Digital, o evento será enviado ao RM via webhook.

Fluxo:

```
OQ → Webhook RM
```

O RM deverá:

* registrar o lead no PI
* associar o corretor responsável
* registrar a origem do lead como **OQ Digital**

---

## 6.3 Atualização de Leads

Leads podem ser atualizados por ambos os sistemas.

Fluxo:

```
RM ↔ OQ
```

O objetivo é manter consistência de dados e evitar duplicidade.

---

## 6.4 Evolução Comercial e Aquecimento de Leads

Eventos comerciais registrados no RM serão enviados à OQ Digital.

Esses eventos incluem:

* evolução de negociação
* interações comerciais
* avanço no funil de vendas
* evolução do aquecimento do lead
* fechamento de vendas

Fluxo:

```
RM → OQ
```

Esses dados são utilizados para:

* atualizar rankings de corretores
* gerar indicadores de performance
* estimular competição saudável entre corretores
* aumentar o engajamento comercial.

---

# 7. Consulta de Empreendimentos

O RM disponibilizará uma **API para consulta de empreendimentos ativos no PI**.

Diferentemente das demais entidades da integração, **os empreendimentos não serão enviados automaticamente para a OQ**.

Nesse modelo, a OQ será responsável por consultar o RM sempre que precisar obter ou atualizar informações, assim como status do empreendimento.

Fluxo:

```
OQ → API RM
```

Endpoint previsto:

```
GET /api/empreendimentos
```

A API retornará as informações necessárias para uso em campanhas, landing pages e estratégias comerciais.

---

# 8. Componentes Técnicos Necessários no RM

### Cliente de Integração

Responsável por consumir a API da OQ Digital.

Funções:

* envio de corretores
* envio de evolução de leads
* envio de eventos comerciais
* envio de evolução de vendas

---

### Endpoint de Webhook

Endpoint público responsável por receber eventos da OQ.

Exemplo:

```
POST /api/integracao/oqdigital/lead
```

Responsabilidades:

* registrar leads recebidos
* validar origem da requisição
* garantir idempotência

---

### API de Consulta de Empreendimentos

Endpoint responsável por disponibilizar empreendimentos para consulta da OQ.

---

### Exclusão de Registros

Registros integrados não devem ser removidos fisicamente.

Utilizar apenas:

* status inativo
* cancelamento de oportunidade.

---

# 10. Funcionalidades Fora do Escopo

Algumas funcionalidades da plataforma OQ não fazem parte desta fase da integração.

### Onboarding Plug-and-Play

Possibilidade futura onde o parceiro TOTVS poderia:

* criar automaticamente a incorporadora na OQ
* provisionar ambiente
* ativar a integração automaticamente

Essa automação não será implementada nesta fase.

---

### Automação de Gamificação

Possibilidade futura de automatizar:

* criação de campanhas
* definição de metas comerciais
* regras de pontuação
* ranking de corretores

Essa funcionalidade poderá ser considerada em evoluções futuras.

---

# 11. Resultado Esperado

Com a integração implantada, o processo comercial passa a operar com **inteligência e engajamento ampliados**.

Benefícios esperados:

 Redução significativa do custo de aquisição de leads  
 Aumento da taxa de conversão comercial  
 Aceleração do ciclo de vendas  
 Maior engajamento da rede de corretores através de gamificação

A integração entre RM e OQ Digital cria uma camada de **inteligência comercial e motivação da força de vendas**, transformando o processo de vendas e aumentando a eficiência da operação imobiliária.
