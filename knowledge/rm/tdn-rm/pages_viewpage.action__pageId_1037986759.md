---
content_hash: b5e1b778227ecfe015b2ba6b406b1c2523de0fd7d646e33f5fb5d5d21b6d6442
fetched_at: '2026-06-29T00:05:49.149493+00:00'
page_id: '1037986759'
product: rm
source: tdn-rm
title: Débito Automático de Diárias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1037986759
version: 3
---

## **CONTEÚDO**

**2CONTEÚDO**

SumárioVisão Geral

## **01. Visão Geral**

O Débito Automático de Diárias é uma rotina que garante o lançamento contínuo e correto das diárias na conta de pacientes internados, conforme as regras contratuais estabelecidas com cada convênio.

### Objetivo

Automatizar o lançamento diário de diárias e pacotes de diária global/isolamento, garantindo que:

* + Todos os dias de internação tenham diárias lançadas
  + As restrições contratuais sejam respeitadas
  + Autorizações sejam criadas automaticamente quando necessário
  + Os pacotes corretos sejam aplicados conforme o leito ocupado
Configuração

## **02. Configuração**

### Parâmetros da Condição Contratual

Localização: **Cadastros > Faturamento > Condições Contratuais.**

após isso, vá até a aba **Parâmetros 1****Horário limite para cálculo de nova diária:** Define o horário que será considerado para cobrança de nova diária. Utilizado em casos de mudança de leito para determinar qual diaria/pacote aplicar.

### Cadastro de Diárias

Localização: **Cadastros > Faturamento > Condições Contratuais > anexo Diárias**

Agora, devemos configurar o Pacote Diária Global e Isolamento. Para isso, vá em **Cadastro > Faturamento > Outros Cadastros > Tabelas de Procedimentos e Serviços.**Clique em incluir e a tela abaixo será aberta:  
Para decidir se a diária é um pacote Global ou Isolamento, a checkbox **"Pacote"** deve estar selecionada, assim sendo possível marcar o **Tipo Pacote**.

* + **Pacote Diária Global:** Utilizado quando o leito não está em isolamento
  + **Pacote Diária Isolamento:** Utilizado quando o leito está com status "Isolamento"

**Importante:** Os pacotes devem estar cadastrados na tabela de DTS da condição contratual.

### Configuração de Leitos

**Localização:** Cadastros > Registro e Controle > Leitos

#### Classes de Leito

O campo **"Classes de Leitos"** define a categoria do leito e deve ser amarrado ao plano do paciente:

**Exemplos de amarração:**

* + Plano Prata → Classe Enfermaria
  + Plano Ouro → Classe Apartamento

#### Diárias Configuradas

Informe nos campos:

* + **Diária de Paciente:** Código da diária que será cobrada na conta do paciente
  + **Diária de Acompanhante:** Código da diária de acompanhante (quando aplicável)

O sistema utilizará estas diárias configuradas para realizar os lançamentos automáticos.

Funcionamento da Rotina

## **03. Funcionamento da Rotina**

**Localização:** Utilitários > Débito de Diárias

### Processo de Execução

A rotina percorre todas as contas em aberto que possuem ao menos uma diária lançada e:

1. 1. Identifica dias sem diária lançada
   2. Verifica o leito ocupado em cada dia
   3. Lança o pacote configurado para aquele leito
   4. Aplica regras de divisão de cobrança quando aplicável
   5. Cria autorizações automaticamente se necessário

### Regra Fundamental

**Após o primeiro lançamento de diária, todos os dias subsequentes devem ter uma diária lançada.**

Esta regra também vale para pacotes de diária global ou isolamento.

Restrições Contratuais

## **04. Restrições Contratuais**

### Validação de Restrições

Ao executar o Débito de Diárias, o sistema verifica nas **Restrições de Contrato** se a diária está configurada como:

* + **Exige Liberação do Convênio:** Cria registro na Central de Autorizações
  + **Sem restrição:** Lança normalmente na conta

**Localização das Restrições:** Cadastros > Faturamento > Condições Contratuais > anexo Restrições de Contrato

### Comportamento

A validação contratual ocorre **independentemente da origem do lançamento**, garantindo conformidade com as regras negociadas.

Central de Autorizações

## **05. Central de Autorizações**

### Inserção Automática

Quando a diária exige autorização do convênio, o sistema:

1. 1. Cria automaticamente o registro na Central de Autorizações
   2. Mantém vínculo entre a diária lançada e a autorização
   3. Permite rastreabilidade completa do processo

### Percentual de Cobertura

Se configurado percentual de cobrança nas restrições:

* + **Percentual coberto:** Lançado na conta do convênio
  + **Valor excedente:** Lançado em Gastos Particulares

Se configurado valor fixo:

* + **Valor fixo:** Lançado em Gastos Particulares
  + **Valor restante:** Lançado na conta do convênio
Pacotes de Diária Global e Isolamento

## **06. Pacotes de Diária Global e Isolamento**

### Lançamento Automático

O sistema identifica automaticamente qual pacote lançar:

```
Se Leito.Status = "Isolamento" ENTÃO
    Lança Pacote Diária Isolamento
SENÃO
    Lança Pacote Diária Global
```

### Mudança de Leito

Quando ocorre mudança de leito durante a internação:

**Exemplo:**

* + Internação: Dia 1 a 5
  + Leito A (dias 1-2): Pacote X
  + Transferência dia 3 às 10h
  + Leito B (dias 4-5): Pacote Y

**Aplicação no dia 3:**

* + Se transferência **antes** do horário limite: Pacote Y
  + Se transferência **depois** do horário limite: Pacote X

### Itens Extra Pacote

Se configurados Itens Extra Pacote e estes itens existirem lançados na conta (em qualquer grupo de gastos), serão automaticamente marcados como **"Incluído no Pacote"**.

Criação Automática de Guias

## **07. Criação Automática de Guias**

### Guia de Resumo

Quando a diária exige liberação e **não existe Guia de Resumo**:

* + Sistema cria automaticamente Guia de Resumo
  + Inclui a diária na guia criada
  + Registra a ação no log do processo

**Mensagem de log exemplo:** "Não foi localizada guia válida para autorização da diária. O sistema criou automaticamente uma guia de resumo conforme regras contratuais."

### Guia de Prorrogação

Quando já existe Guia de Resumo com data anterior:

* + Sistema cria Guia de Prorrogação
  + Data da guia = Data de execução do Débito de Diárias
  + Inclui a diária na parcial corrente

### Regras de Criação

A criação de guias ocorre **independentemente da origem do lançamento**, respeitando exclusivamente as regras contratuais.

Divisão de Cobrança

## **08. Divisão de Cobrança**

### Cenário de Aplicação

Quando paciente utiliza leito diferente da sua categoria contratada:

**Exemplo:**

* + Plano: Enfermaria
  + Leito ocupado: Apartamento (por falta de vaga)

### Responsável pela Diferença

#### Hospital Responsável

* + Lança pacote com valor da categoria contratada
  + Diferença vai para **Itens Grátis**

**Exemplo:**

```
Pacote Apartamento: R$ 3.000,00
Pacote Enfermaria: R$ 2.000,00

Lançamentos:
- Conta (Convênio): R$ 2.000,00
- Itens Grátis: R$ 1.000,00
```

#### Paciente Responsável

* + Lança pacote com valor da categoria contratada
  + Diferença vai para **Gastos Particulares**

#### Convênio Responsável

* + Lança pacote com valor integral
  + Sem lançamento de diferença

### Cálculo Automático

O sistema:

1. 1. Identifica diária de diferença informada
   2. Busca pacote vinculado à diária utilizada
   3. Busca pacote vinculado à diária de diferença
   4. Calcula e lança a diferença conforme responsável
Observações Importantes

## **09. Observações Importantes**

1. **Primeiro Lançamento:** Após a primeira diária lançada, a rotina garante lançamento em todos os dias subsequentes
2. **Validação Contratual:** Sempre respeita restrições cadastradas, independente de lançamento manual ou automático
3. **Rastreabilidade:** Mantém vínculos entre diárias, autorizações e guias para auditoria completa
4. **Log de Processo:** Registra todas as ações automáticas executadas para transparência do processo
5. **Mudança de Configuração:** Alterações em cadastros de leitos ou diárias afetam apenas lançamentos futuros
6. **Reprocessamento:** Use o processo "Reprocessamento Pacote" para ajustar lançamentos existentes após mudanças cadastrais
