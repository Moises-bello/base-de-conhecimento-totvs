---
content_hash: 7e7204eb506d0775ee14ab872f380487ddfac1ace311b864920caf4ad9bab391
fetched_at: '2026-06-29T00:10:35.356072+00:00'
page_id: '528481554'
product: rm
source: tdn-rm
title: Label
type: documentation
url: https://tdn.totvs.com/display/LRM/Label
version: 29
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       Este documento tem como objetivo demonstrar o uso do controle Label.

# Introdução:

---

       Arraste o item Label da Barra de Controles para o seu relatório para adicionar o controle.

       Clique duas vezes no controle para usar seu editor local e digite o texto desejado. Pressione CTRL+Enter para confirmar as alterações e sair do modo de edição.

# Propriedades:

---

1Ajustar Tamanho e Conteúdo

Altere o tamanho do controle na etapa do designer para ajustar o texto.

Selecione "**Ajustar Limites ao Texto**" para que o tamanho do controle se ajuste a seu conteúdo.

Quando a **quebra de linha** estiver habilitada, o comando exibirá o conteúdo do controle em várias linhas, a altura do controle será reduzida e a largura será ajustada ao conteúdo. Quando estiver desabilitada e o conteúdo do controle estiver parcialmente visível, o comando ajustará o tamanho do controle para exibir esse conteúdo.

Selecione "**Aj****ustar Texto aos Limites**" para que o tamanho da fonte do controle se ajuste à área.

A opção **quebra de linha** define se o texto será exibido em várias linhas ou em uma única linha.

2Expressão

É possível vincular o controle a um campo da entidade usada no relatório. Para isso, clique nas reticências para abrir o editor de expressão e na aba "Campos" selecione o campo da entidade desejada. Além disso, no editor podem ser construídas expressões complexas envolvendo dois ou mais campos.

3String de Formato de Texto

Clique nas reticências para abrir o editor do formato da string, onde há diferentes opções para o formato de saída para o texto do controle.

4Ângulo

Especifica o ângulo pelo qual o texto do controle será girado. O ângulo retornado por essa propriedade é medido em graus e no sentido anti-horário a partir da vertical.

Quando a propriedade é definida como um valor diferente de zero, as propriedades **Pode Crescer** e **Pode Diminuir** serão ignoradas.

5Tamanho Automático

Essa propriedade especifica se deve ou não ajustar o tamanho do controle ao seu conteúdo, sem limitá-lo pelas dimensões colocadas no designer.

Essa opção não afeta a largura ou a posição de **outros controles** do relatório.  
O resultado do uso dessa opção depende do valor da propriedade "**Quebra de Linha**".  
    Quando Quebra de linha estiver ativada, a largura desse controle apenas poderá ser reduzida.  
    Quando quebra de linha estiver desabilitada, a largura do controle poderá ser aumentada ou diminuída para melhor se ajustar ao conteúdo inserido.

As imagens a seguir mostram como a propriedade funciona quando é definido um alinhamento do texto.

**Alinhamento:** Esquerda

**Alinhamento:** Centralizar

**Alinhamento:** Direita

6Pode Crescer e Pode Diminuir 

Essas propriedades permitem aumentar ou diminuir a altura do controle para melhor exibição do conteúdo.

**Pode Crescer**

Quando habilitada, a altura do texto será aumentada automaticamente (se necessário) para que todo o texto seja exibido. Se houver outros controles abaixo do Texto atual, eles serão movidos para baixo para impedir a sobreposição.

**Pode Diminuir**

Quando habilitada, caso um texto não preencha completamente o tamanho do controle, sua altura diminuirá para a altura do texto. Se houver outros controles abaixo do Texto atual, eles serão movidos para cima para remover o espaço não utilizado.

7Multilinhas

Quando marcada, essa propriedade irá exibir mais de uma linha de texto no controle. Por exemplo, quando utilizado ENTER para separação de linhas no texto.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.23 ou superiores

false

**Processo:** Designer

falsefalse

**Status:** Em Construção

false

**Data:**

false

**Autores:**
