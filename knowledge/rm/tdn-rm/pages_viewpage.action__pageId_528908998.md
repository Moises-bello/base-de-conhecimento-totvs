---
content_hash: 48611cafe133b46104b648473d8eabf525d425c180fc670defd01d95520b11f5
fetched_at: '2026-06-29T00:10:35.369634+00:00'
page_id: '528908998'
product: rm
source: tdn-rm
title: Formatação Condicional - TReports
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=528908998
version: 25
---

# Índice:

---

[^Páginas Filhas://Índice:].\*

# Objetivo:

---

       Este documento tem por finalidade descrever a capacidade de alterar a aparência ou visibilidade de um elemento do relatório com base em uma condição lógica avaliada sobre os dados subjacentes..

# Criando uma regra de formatação:

---

       Uma Regra de Formatação pode ser definida por uma condição lógica (regra) e configurações de aparência deverão ser aplicadas aos elementos específicos do relatório quando essa condição for atendida.

       A imagem a seguir demonstra algumas das implementações possíveis da formatação condicional – os valores que forem menor que R$ 1.000,00 receberam sua cor de fundo verde, com valor maior que R$ 3.000,00 lilás, com valor acima de R$ 5.000,00 ficaram em negrito e os que forem negativos ficaram destacados na cor vermelha.

       A aparência definida pelas regras de formatação tem prioridade sobre as configurações definidas pelas propriedades e estilos de aparência do elemento de relatório.

       Para gerenciar essa coleção selecione o controle e use o Editor de Expressões de formatação, através da propriedade “Expressões”.

Expressões1Formatando Fonte

       Como exemplo vamos definir uma condição para que o controle da base de dados que retorne valores iguais ou maiores que 3.000,00 seja impresso em negrito.

       Para inserir a formatação selecione o controle onde será aplicada a condição. Na barra de propriedades selecione a propriedade “Expressões”, dentre as opções desta propriedade expanda “Aparência | Fonte” e na opção “Negrito” acesse o editor de expressões atribua a condição desejada. Salve as alterações e gere o relatório para validar o resultado.

2Formatando Cor de Fundo

       Como exemplo vamos definir uma condição para que o controle da base de dados seja impresso com o fundo de cor verde caso seu valor seja igual ou inferior a 1.000,00 e em vermelho caso igual ou maior que 3.000,00.

       Para inserir a formatação selecione o controle onde será aplicada a condição. Na barra de propriedades selecione a propriedade “Expressões”, dentre as opções desta propriedade expanda “Aparência | Cor de Fundo”, acesse o editor de expressões atribua a condição;

iif( [SALARIO] <= 1000, Rgb ( 203,239,230 ),

iif( [SALARIO] >= 3000, Rgb ( 245,220,225 ), ?))

       Salve as alterações e gere o relatório para validar o resultado.

 A tabela com o código das cores pode ser encontrado em [sites](https://site112.com/tabela-cores-html) da web.

3Formatando Valores Negativos

       Como exemplo vamos definir uma condição para que o controle da base de dados seja impresso com sua cor de frente em vermelho caso seu valor seja negativo.

       Para inserir a formatação selecione o controle onde será aplicada a condição. Na barra de propriedades selecione a propriedade “Expressões”, dentre as opções expanda “Aparência | Cor de Frente”, acesse o editor de expressões atribua a condição;

iif (( [SALARIO] - 2000 ) < 0, Rgb ( 255,0,0 ), **?** )

false

*Obs.: Na condição apenas atribuímos um valor para que algumas linhas possam retornar um valor negativo, mas esse valor fixo pode ser substituído por um campo da base onde o comportamento será o mesmo.*

       Salve as alterações e gere o relatório para validar o resultado.

---

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.23 ou superiores

false

**Processo:** Formatação Condicional

falsefalse

**Status:** Em Construção

false

**Data:**

false

**Autores:**
