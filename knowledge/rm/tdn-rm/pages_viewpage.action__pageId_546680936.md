---
content_hash: 679e035ff044e990fd32711be23c431af40a7e7928f14d504162149781f00ffe
fetched_at: '2026-06-29T00:10:41.924731+00:00'
page_id: '546680936'
product: rm
source: tdn-rm
title: Componente EXPRESSÃO
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=546680936
version: 7
---

# Índice

---

.\*ndice:

# Objetivo

---

       O objetivo deste documento é explicar o funcionamento do campo do tipo Expressão no Gerador de Relatórios Delphi, a correta configuração e alguns cenários de erro.

# Introdução

---

        O componente do tipo Expressão é utilizado para criação de cálculos e transformações envolvendo valores numéricos e datas. Para inseri-lo no relatório utilize o menu de contexto da banda:

Após inserí-lo, será exibida a tela para criação da Expressão. O campos disponíveis para utilização são mostrados na lista à esquerda.

Atenção

Note que somente campos de tipos numéricos, datas e fórmulas são listados. Isso é muito importante, pois caso uma fórmula retorne um valor não numérico ou que não seja uma data, a expressão poderá apresentar erro.

# Solução de Problemas

---

Conforme dito anteriormente, o componente de expressão não aceita entradas do tipo texto. No exemplo abaixo, veremos o que acontece ao utilizar uma fórmula que retorne o tipo texto dentro de uma expressão.

Temos uma Fórmula que retorna o valor de um campo complementar em texto. Observe o tipo "S" definindo o retorno.

O resultado dela, valor 1000, continua sendo retornado mas com o tipo "String" (texto).

Agora vamos criar um relatório que utiliza essa fórmula e um campo de expressão que calcule um percentual sobre o valor retornado da fórmula.

O relatória a seguir utiliza como Contexto os dados da tabela PFUNC, mesmo contexto utilizado na fórmula. Temos os dados necessários para execução da fórmula, CHAPA e IDENTIFICADOR DA COLIGADA. O componente de fórmula referencia a fórmula mostrada anteriormente.

Acrescentamos um componente do tipo Expressão para fazer o cálculo do acréscimo de 10%:

Ao executar o relatório, teremos o seguinte retorno, apresentando "Erro" no lugar da expressão:

Esse erro aparece pois o tipo de dado retornado da fórmula e que foi passado para a expressão não é permitido. Para solucionar esse problema devemos analisar a fórmula utilizada. Cada fórmula tem seu tipo de retorno e no caso do exemplo conseguimos mudar esse tipo para numérico utilizando um parâmetro da função de fórmula utilizada.

Assim, o relatório é gerado corretamente.

falsefalse

**Produto:** Framework

false

**Versão:** 11.82.XX e 12.1.XX

false

**Processo:** Campo do Tipo Expressão - Relatórios Delphi

falsefalse

**Status:** Em construção

false

**Data:**

false

**Autores:**
