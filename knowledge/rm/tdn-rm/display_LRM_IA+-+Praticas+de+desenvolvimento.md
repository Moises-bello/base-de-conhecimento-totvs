---
content_hash: 098f314b0d2072f69a32bc6d5a19ed69c5681341f1741150e894427061e49f42
fetched_at: '2026-06-29T00:05:54.228234+00:00'
page_id: '1076453645'
product: rm
source: tdn-rm
title: IA - Praticas de desenvolvimento
type: documentation
url: https://tdn.totvs.com/display/LRM/IA+-+Praticas+de+desenvolvimento
version: 3
---

## 🎯 Objetivo

Este documento formaliza as práticas que tenho desenvolvido para usar o GitHub Copilot de forma eficiente, garantindo código de qualidade e aderência à arquitetura do projeto.

---

## 🔄 Fluxo de Trabalho Recomendado

### 1. 📋 Entendimento Prévio (Modo `Ask`)

**Sempre comece com o modo `Ask`** antes de qualquer implementação.  
text

```
Prompt: "Entenda a seguinte funcionalidade: [descrição detalhada]. 
Descreva a lógica, identifique as classes envolvidas, o fluxo principal 
e possíveis casos de borda. Não gere código ainda."
```

**Por que fazer isso:**

* Força o modelo a raciocinar sobre o problema antes de codificar
* Reduz alucinações e código incorreto
* Alinha o entendimento entre você e a IA antes da implementação

---

### 2. 🧪 Testes Primeiro (Modo `Agent`)

**Crie a classe e o primeiro método vazio ou com esqueleto**, depois peça para gerar os testes.  
text

```
Prompt: "Com base no entendimento anterior, primeiro crie os testes unitários 
para o método [NomeDoMetodo] da classe [NomeDaClasse]. 
Siga o padrão de testes do projeto (xUnit/PHPUnit/Jest). 
Cubra casos felizes, casos de borda e exceções."
```

**Por que fazer isso:**

* Os testes definem o comportamento esperado antes da implementação
* Força a pensar em casos de borda desde o início
* O código gerado já nasce com cobertura de testes

**Exemplo prático:**  
csharp

```
// 1. Você cria o esqueleto
public class OrderService 
{
    public decimal CalculateDiscount(Order order) 
    {
        // TODO: Implementar
        throw new NotImplementedException();
    }
}

// 2. Pede para o Copilot gerar os testes
// 3. Depois pede para implementar o método
```

---

### 3. 🏗️ Implementação Guiada (Modo `Agent`)

Após os testes, peça a implementação com regras claras.  
text

```
Prompt: "Agora implemente o método [NomeDoMetodo] na classe [NomeDaClasse]. 
Regras obrigatórias:
- Mantenha cada método com no máximo 10-15 linhas
- Use early returns (evite else desnecessário)
- Máximo de 2 níveis de aninhamento
- Use injeção de dependência (se aplicável)
- Siga os padrões de nomenclatura do projeto
- Gere código limpo, sem explicações adicionais (a menos que solicitado)"
```

**Importante:** O Copilot Corporativo já explica o que fez, então você pode pedir para ele **não** explicar se quiser apenas o código, ou pedir explicações específicas depois.

---

### 4. 🔍 Revisão e Ajustes

Após a implementação, peça para revisar o próprio código.  
text

```
Prompt: "Revise o código implementado. Identifique possíveis:
- Violações de princípios SOLID
- Complexidade ciclomática alta
- Oportunidades de refatoração
- Problemas de performance

Sugira melhorias mantendo a mesma funcionalidade."
```

---

## 🧠 Prompt Templates por Situação

### Para Nova Funcionalidade

text

```
[Ask] Entenda o problema: [descrição].
Descreva a solução em alto nível.

[Agent] Agora:
1. Gere os testes unitários para [método/classe]
2. Implemente a classe seguindo a arquitetura [MVC/DDD/Repository]
3. Mantenha complexidade baixa (max 2 níveis de aninhamento)
4. Siga o padrão de código do projeto
```

### Para Refatoração

text

```
[Ask] Analise este código: [cole o código].
Identifique problemas de complexidade, violações de boas práticas 
e oportunidades de melhoria.

[Agent] Refatore o código para:
- Métodos com no máximo 10 linhas
- Remover duplicação
- Usar early returns
- Manter a mesma funcionalidade
```

### Para Correção de Bug

text

```
[Ask] Este é o erro: [descrição/stacktrace].
Qual a causa provável?

[Agent] Corrija o erro e:
1. Adicione um teste que reproduza o problema
2. Implemente a correção
3. Mantenha o código simples e legível
```

---

## ✅ Checklist do Desenvolvedor

Antes de finalizar uma tarefa com o Copilot, verifique:

* Usei o modo `Ask` para entender a lógica primeiro?
* Gerei os testes antes do código?
* Defini regras claras de complexidade no prompt?
* Pedi para seguir a arquitetura do projeto?
* Revisei o código gerado criticamente?
* O Copilot explicou o que fez (quando necessário)?
* A complexidade ciclomática está baixa?
* Os testes passam e cobrem casos de borda?

---

## ⚠️ O Que EVITAR

| ❌ Evite | ✅ Faça |
| --- | --- |
| Aceitar sugestões sem revisão | Revise cada linha criticamente |
| Pedir "crie um sistema de..." | Divida em partes menores |
| Deixar o contexto vazio | Use `@workspace` para dar contexto |
| Ignorar os testes | Testes são prioridade |
| Prompt vago ("corrija o erro") | Seja específico sobre o erro |

---

## 📌 Resumo dos Benefícios

* **Redução de bugs**: Testes primeiro e revisão automatizada
* **Código consistente**: Instruções por linguagem/arquivo
* **Baixa complexidade**: Regras explícitas de simplificação
* **Time alinhado**: Padrões definidos e replicáveis
* **Eficiência**: Menos tempo de revisão e retrabalho

---

## 🔗 Links Úteis

* [Documentação oficial do Copilot](https://docs.github.com/pt/copilot)
* [Padrões de prompt para desenvolvimento](https://github.com/features/copilot#best-practices)
