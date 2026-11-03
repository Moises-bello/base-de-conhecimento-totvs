---
content_hash: 8930f847be1de02af3b2eb5151e5bfa02359eaa420577ad58277f93e8ce3c32e
fetched_at: '2026-06-28T21:35:30.369863+00:00'
page_id: '849549543'
product: fluig
source: tdn-fluig
title: Logs em personalização do Fluig
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=849549543
version: 1
---

## Índice

true.\*ndicenone

# Objetivo

---

O objetivo deste guia é descrever como criar logs em eventos globais, de formulário, processo e datasets.

# Pré-requisitos

---

Antes de iniciar, é importante que leia a documentação sobre o  e tenha experiência com desenvolvimento usando Javascript ou Java.

# LOGs

---

Os logs são registros que ajudam a entender o funcionamento de um código. Eles desempenham um papel crucial no monitoramento, manutenção e resolução de problemas. No Fluig, o desenvolvedor pode criar logs informativos (info), de alerta (warn), de erro (error) e depuração (debug). Escolher corretamente o tipo de log, ajuda na visualização rápida de problemas no log bem como no controle que permite evitar logs excessivos.

## log.info

---

O log do tipo 'info' é o mais comum de ser utilizado e deve ser usado para registrar alguma informação que é esperada e que pode ajudar a entender o que está sendo executado ou os valores que estão relacionados à execução

jsjsImprimindo conteúdo de uma variáveljsRegistrando o valor de um campo de formulário

## log.warn

---

O log do tipo 'warn' deve ser usado para registrar situações que não interrompem o fluxo normal da aplicação, mas que indicam a ocorrência de algo fora do esperado, que pode requerer atenção futura. São úteis para monitorar possíveis problemas que, se não tratados, podem se tornar erros mais graves.

jsjs

## log.debug

---

O log do tipo 'debug' deve ser utilizado para registrar informações detalhadas e de baixo nível sobre a execução do sistema. Esses logs são essenciais durante o desenvolvimento e a depuração de software, pois ajudam a entender o comportamento interno da aplicação, permitindo a identificação precisa de bugs e problemas. Por padrão, o Fluig não exibe os logs de debug que devem ser habilitados conforme essa documentação. Isso ajuda a evitar logs excessivos no Fluig ao mesmo tempo que permitem logs detalhados caso seja habilitado.

jsjs

## log.error

---

O log do tipo 'error' deve ser usado para registrar eventos que causaram falhas na execução do sistema ou que impedem a conclusão de uma tarefa. Esses logs são críticos para identificar e resolver problemas que afetam a funcionalidade da aplicação, fornecendo detalhes sobre o que deu errado e onde.

js

## log.dir

---

O log do tipo 'dir' é utilizado para registrar a estrutura e o conteúdo de objetos de dados em um formato fácil de ler. Ele é especialmente útil para inspecionar e entender a composição de objetos complexos durante a execução, proporcionando uma visualização clara das propriedades e valores internos desses objetos.

jsjs

Colocar um print do log deste código
