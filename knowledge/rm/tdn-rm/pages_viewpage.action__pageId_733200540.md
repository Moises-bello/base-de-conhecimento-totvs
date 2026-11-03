---
content_hash: bb280040cab6b2485a05bf1003f2527b3358ed21e2a16272d631bab59b8b5ec3
fetched_at: '2026-06-29T00:11:28.819194+00:00'
page_id: '733200540'
product: rm
source: tdn-rm
title: RPT00048 - Imprimir rodapé de Detalhe em todas as páginas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=733200540
version: 1
---

# Índice:

---

.\*ndice:

# Introdução

---

Este documento tem como objetivo explicar o funcionamento da propriedade "**Repete em todas as páginas**" da banda de rodapé de detalhe, a qual permite imprimir os campos contidos nessa banda em todas as páginas do relatório.

# Utilizando a funcionalidade

---

Ao selecionar uma banda de rodapé de detalhe, na **Grade de Propriedades**, em **Diversos,** estará disponível a propriedade **Repete em todas as páginas** que, por padrão, é desabilitada (check-box desmarcado), conforme mostrado abaixo:

Ao ativar essa propriedade (marcar o check-box), os campos e elementos presentes no rodapé de detalhe serão impressos em todas as páginas do relatório.

Conforme mensagem mostrada ao marcar o check-box, **a utilização dessa propriedade possui algumas limitações**, como detalhado no próximo item.

# Limitações

---

Em função da ordem de execução das bandas e dos controle, conforme detalhado em , a utilização da propriedade **Repete em todas as páginas não deve ser utilizada quando a banda de rodapé de detalhes possuir controles do tipo:**

* **Totalizador;**
* **Expressão\***

A utilização desses controles em conjunto com a propriedade **Repete em todas as páginas** pode resultar na impressão de resultados inesperados.

\*

Expressão que apenas espelha um campo da base poderá ser utilizada normalmente.

Para realizar cálculos de totalização dos campos, é possível utilizar a funcionalidade de **Sumário**, conforme demonstrado nos próximos itens.

## Diagnóstico de uso

---

Caso um relatório esteja utilizando um controle do tipo totalizador ou expressão no rodapé de detalhe e a propriedade Repete em todas as páginas esteja habilitada, ao gerar o diagnóstico do página será exibido o erro conforme demonstrado abaixo:

# Totalizadores com Repete em todas as páginas

---

Caso seja necessário realizar cálculos totalizadores em campos existentes no rodapé de detalhe com a propriedade **Repete em todas as páginas** habilitada, deve-se utilizar a propriedade **Sumário**.

No layout de relatório abaixo, é exemplificado essa utilização. Nesse caso, deseja-se imprimir em cada página a quantidade de funcionários e o salário total:

Os campos a serem totalizados estão na banda de rodapé de detalhe e a propriedade **Repete em todas as páginas**foi habilitada, permitindo a impressão em todas as páginas. Para utilizar a propriedade **Sumário,** deve-se selecionar o campo e, na grade de Propriedades, em Sumário, escolher onde o resumo irá correr (grupo, relatório ou página) e em seguida escolher o tipo da função (Média, Soma, Contar, etc).

Nesse exemplo, como queremos que os totalizadores sejam por página, a configuração será feito conforme mostrado abaixo:

1-ConfigsTotalizar Contagem de Chapas (funcionários)Totalizar Soma de Salários

O resultado final do relatório é:

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.2209

false

**Processo:** Impressão de relatório

falsefalse

**Status:** Concluído

false

**Data:**

false

**Autores:**
