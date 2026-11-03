---
content_hash: 6e229594c38add78e4147b6af5354a560deedade1027dd2ab9b0bb68fb4abae0
fetched_at: '2026-06-29T00:05:56.358698+00:00'
page_id: '149881523'
product: rm
source: tdn-rm
title: Utilizando a atividade "Expressão"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=149881523
version: 5
---

## **ÍNDICE**

42ÍNDICEcircle

---

## **OBJETIVO**

Permitir que o usuário consiga alterar campos de uma outra atividade ou contexto.

---

## **COMO UTILIZAR**

Arraste a atividade "**Expressão**" para o fluxo de trabalho sequencial:

---

## **PROPRIEDADES**

Três propriedades alteram a maneira de funcionamento da atividade de expressão:

### EXPRESSÕES

Nesta propriedade é possível digitar o valor a ser calculado pela expressão.  
Pode ser um valor literal ("3", por exemplo) ou qualquer outra expressão C# válida, como na figura abaixo:

### VALOR CALCULADO

Contém o campo que receberá o valor da expressão que foi definido na propriedade "Expressões".   
No exemplo abaixo será colocado o valor "3" no campo **Message** da atividade **rmsThrowActivity1** (atividade de gerar exceção):

### **CONCATENAR VALOR NO CAMP CALCULADO**:

É um campo booleano (verdadeiro ou falso), o qual indica se o valor do campo **Expressões** será concatenado no caminho do campo **Valor Calculado** a cada execução da expressão.

No exemplo acima, a expressão está dentro de um *rmsForEachActivity* ([Para Cada](https://tdn.totvs.com/pages/viewpage.action?pageId=149881513), iterando sobre o resultado da leitura da visão de coligadas).  
No campo Expressões, está o valor do *Nome Fantasia* da coligada da iteração atual.  
Já no campo de Valor Calculado, está o *value* da Expressão 1, no qual armazenaremos o resultado deste loop.

Observando o campo alvo do Valor Calculado, com a opção de Concatenação ativa, obteremos os seguintes resultados:

Já com ela desativada, obteremos, então, somente o valor da última iteração da expressão:

**Para mais informações sobre expressões, acesse****:** **<http://tdn.totvs.com/x/kJi2C>**

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/GLB/GLB.Perfis.aspx)

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Framework |
| **Processo** | **:** | Fórmula Visual |
| **Subprocesso** | **:** | Utilizando a atividade "Expressão" |
| **Data da publicação** | **:** | 22/09/2014 |
