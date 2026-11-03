---
article_id: 38388551687447
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 8164ade59373f6d99ec97e039bf20bb221e3e640c0f2bc5b85636c272ec7daa6
fetched_at: '2026-06-28T22:38:55.638798+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Limite maximo de linhas
  na geração da SCP e numeracao
type: support-article
updated_at: '2026-02-16T14:40:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38388551687447-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Limite-maximo-de-linhas-na-gera%C3%A7%C3%A3o-da-SCP-e-numeracao
---

No Protheus, o campo de numeração de itens na tabela SCP utiliza um sistema alfanumérico de dois dígitos, permitindo centenas de registros por documento. Após o item 99, a numeração segue com combinações como 9A, 9B, até ZZ, otimizando o espaço sem aumentar o campo. Esse comportamento é nativo e não indica falha no sistema.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38388551681047) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Qual o limite maximo de digitações de itens dentro da tabela SCP?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**  
Esta documentação visa esclarecer o funcionamento do campo de numeração de itens na tabela **SCP**. No sistema Protheus, para otimizar o espaço de armazenamento e permitir um maior volume de registros dentro de um mesmo documento, a numeração dos itens utiliza um sistema **alfanumérico**.

### 

### **Lógica de Incremento (Range de 2 decimais)**

O campo de item na tabela SCP é limitado a **2 decimais**. Para expandir a capacidade de registros sem aumentar o tamanho do campo, o sistema adota a seguinte lógica:

1. **Sequência Numérica Inicial:** O sistema inicia a contagem de forma decimal padrão: `01, 02, 03...` até o item `99`.
2. **Transição Alfanumérica:** Ao atingir o limite numérico de dois dígitos (`99`), o sistema inicia o uso de caracteres alfanuméricos para manter o range de 2 posições.
3. **Sequência Após 99:** A numeração passará a ser gravada como `9A, 9B, 9C... 9Z`, e posteriormente seguindo para outras combinações alfanuméricas disponíveis (ex: `A0, A1... ZZ`).

### **Comportamento Padrão**

É importante ressaltar que este comportamento é **nativo e esperado** do ERP Protheus.

* **Integridade de Dados:** A gravação de letras na numeração do item não representa uma falha de sistema ou corrupção de banco de dados.
* **Capacidade Expandida:** Esta lógica permite que uma única Solicitação de Compras contenha centenas de itens, respeitando a estrutura de dicionário de dados de 2 decimais.

### 

### **Suporte e Análise de Erros**

O sistema está preparado para gerenciar essa numeração automaticamente em todas as rotinas padrão

> **Atenção:** Se durante a transição da numeração numérica para alfanumérica for apresentado qualquer erro de "Index Out of Range", "Type Mismatch" ou falha na gravação do registro:
>
> 1. Verifique se existem **gatilhos (Triggers)** ou **Pontos de Entrada** customizados na tabela SCP que forcem a conversão para numérico.
> 2. Caso o ambiente esteja padrão e o erro persista, entre em contato com o **Suporte Técnico** enviando:
>
>    * Print do erro (*Error Log*).
>    * Exemplo do número do item que causou a interrupção.
>    * ID da Central de Diagnóstico para validação de atualizações.

**Saiba Mais:**

[*Clique aqui e veja mais artigos sobre Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
