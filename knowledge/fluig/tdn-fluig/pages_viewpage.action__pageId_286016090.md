---
content_hash: f13d9055779e2afba1a47b8e760115f724be928a0e4da0d387d18dbdb9b9d779
fetched_at: '2026-06-28T21:35:25.569759+00:00'
page_id: '286016090'
product: fluig
source: tdn-fluig
title: BPM 094 - Quais recomendações devo seguir para reduzir a necessidade de converter
  solicitações de processos?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286016090
version: 4
---

4true.\*ndicenone

# Plataforma

**Produto:**.fluig

# Recomendações

## Transferir código de integração de eventos para datasets

**Situação**: No processo existem integrações que estão sendo realizadas em eventos ou em tarefas de serviço assíncrona. Estas integrações necessitam de manutenção constante. Como necessito realizar manutenções constantes nos processos preciso versionar os mesmos e executar a conversão das solicitações abertas na versão anterior.

**Solução:** Com o isolamento da integração através de datasets, as integrações poderão ser alteradas sem a necessidade de um novo versionamento do processo. Esses datasets deverão ser chamados nos pontos do processo onde originalmente os códigos das integrações estavam sendo chamados.  
Com isso a manutenção nos processos será bem menor. Com menos versões de processos o número de conversão de solicitações também será menor.

## Tarefa de serviço assíncrono para chamar as integrações no lugar dos eventos

**Situação**:  A conversão de solicitações executa os eventos de entrada e saída de atividades executando os códigos de integração indevidamente.

**Solução**:  Além de todas as vantagens já conhecidas da integração assíncrona como segurança, performance e outras, ao fazer esta alteração o problema de executar integrações no momento da execução de conversão da solicitações irá deixar de existir . Essas novas tarefas podem rodar os datasets indicados na primeira recomendação.

## Dividir múltiplas integrações de um evento em integrações menores distribuídas em tarefas de serviço assíncrono.

**Situação**: Existem várias integrações diferentes sendo feitas no mesmo evento, dificultando o mapeamento de problemas ocorridos nas integrações durante a execução do mesmo.

**Solução**: Separe as várias integrações em diferentes tarefas de serviço, dessa forma fica bem mais fácil gerenciar e detectar os erros na integração.

O principal objetivo dessas modificações é minimizar as dificuldades de constante na detecção dos erros de integração.

Saiba mais

Para maiores detalhes sobre conversão de solicitações, acesse a documentação [Converter Solicitações](http://tdn.totvs.com/x/a-HuDQ).
