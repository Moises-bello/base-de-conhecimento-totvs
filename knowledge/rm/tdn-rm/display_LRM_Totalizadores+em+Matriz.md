---
content_hash: 4e3017adfdc127c03ad7c29f3d004bbf575dc00f76aa11b317776b0b1c6dad2e
fetched_at: '2026-06-29T00:08:47.130371+00:00'
page_id: '318609479'
product: rm
source: tdn-rm
title: Totalizadores em Matriz
type: documentation
url: https://tdn.totvs.com/display/LRM/Totalizadores+em+Matriz
version: 22
---

# Índice:

---

.\*ndice:

# Objetivo:

---

Esta página tem a finalidade de exemplificar como configurar o total de em uma matriz para que traga os valores conforme a quebra na Matriz.

# Introdução

---

Os totais de uma matriz, por padrão, somam todos os valores apresentados nas linhas acima da sua apresentação. Exemplificaremos como configurar o total em uma matriz para que seu total zere a medida que haja uma quebra de grupo.

false

*Lembramos que os componentes do Totvs Reports são desenvolvidos por terceiros e em atualizações de versões alguns comportamentos eventualmente podem sofrer alterações.*

false

***Como exemplo utilizamos uma matriz onde há informações de Coligada, Seção, Funcionários e Salário. Configuraremos o total para retornar o total por salarial por seção.***

Controle - MatrizPasso 1

Selecione a célula da matriz que será configurada como a quebra das informações. Feita a seleção da célula tecle F4 para acessar as propriedades da célula.

Ou selecione a matriz e clique na **Smart Tag** da matriz, “**Executar Gerador**”

Em sequencia selecionando a coluna onde se deseja realizar a quebra dos valores da matriz.

Nas propriedades da célula altere o valor da propriedade ***“Total Visibilidade”*** para ***“Personalizado Totais”***.

Passo 2

Na sequencia clique nas reticências da propriedade ***“Personalizando Totais”***. Carregara um novo formulário para configurações.

Neste formulário clique em ***“Adicionar”***, em diversos escolha ***“Soma”*** e em ***“Dados”*** clique sobre a reticencias e selecione o type e valor do objeto. No exemplo utilizamos int(16) e o valor 0.

Passo 3

Salve as alterações anteriormente realizadas e gere o relatório para averiguação do resultado. Em nossa simulação o resultado foi o seguinte;

false

Para que a ultima linha somasse os valores sem acumular ***o mesmo processo*** demonstrado ***foi feito para coluna CODCOLIGADA***.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.XX

false

**Processo:** Total em Matriz

falsefalse

**Status:** Em construção

false

**Data:**

false

**Autores:**
