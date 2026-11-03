---
content_hash: bfc6f66f8b2847298ec15f420a924ec017b5cb6986fb6e62a53039336f581a19
fetched_at: '2026-06-29T00:08:27.436583+00:00'
page_id: '271411899'
product: rm
source: tdn-rm
title: Alterando o Layout de Campos no Metadados
type: documentation
url: https://tdn.totvs.com/display/LRM/Alterando+o+Layout+de+Campos+no+Metadados
version: 27
---

# Índice

---

.\*ndice:

# Objetivo

---

       O objetivo deste documento é demostrar como alterar o layout de campo(s) de um Metadados.

# Configuração

---

       Depois de gerado um Projeto de Metadados, para que o tamanho de cada campo seja modificado, altere as propriedades “SizeConstraintsType” para Custom e With e Heigh da MaxSize, conforme o desejado.

       ***Exemplo***: Utilizaremos o formulário abaixo como exemplo.

falseMetadadostrueProcessoEditando SizeConstraintsType

       Selecione a tela do Metadados e clique em "Definir Leiaute".

       No formulário seguinte selecione a aba “***Árvore de Organização***”. Escolha a campo desejado e altera o valor propriedade “***SizeConstraintsType***” para “***Custom***”.

trueProcessoEditando MaxSize

       Selecione a tela do Metadados e clique em "Definir Leiaute".

       No formulário seguinte selecione a aba “***Árvore de Organização***”. Escolha a campo desejado e expanda a propriedade “***MaxSize***”. Nas sub-propriedades "Width" e "Height" atribua os valores desejados.

trueProcessoResultado

       Confirme que o campo teve a sua largura alterada.

# Posicionamento de campos

---

       Algumas propriedades dos componentes da tela de metadados tem o valor herdado de acordo com o componente pai.

No exemplo acima o componente Coligada é único para preencher toda a tela horizontalmente. Portanto, ao tentar diminuir o valor do width não será aplicado, uma vez que é necessário que esse componente preencha toda a linha horizontal.

Podemos posicionar os componentes lado a lado ou simplesmente coloca-los acima ou abaixo de outro componente. Para isso basta apenas selecionar o componente e arrastá-lo. Veja os exemplos a seguir:

falsePosição de camposAcimaAcimaAcimaPosicionando o componente Cliente acima do componente Coligada.AbaixoAbaixoAbaixoPosicionando o componente Cliente abaixo do componente Coligada.Ao lado direitoAo lado direitoAo lado direito

Posicionando o componente Cliente ao lado direito do componente Coligada.

Ao lado esquerdoAo lado esquerdoAo lado esquerdo

Posicionando o componente Cliente a esquerda do componente Coligada.

Desse modo, considerando o posicionamento do componente Cliente ao lado do componente Coligada vamos ter o seguinte resultado visualmente.

Nesse caso, temos dois componentes para preencher um espaço horizontalmente. Assim podemos alterar o valor ***Width*** de um componente e o restante da tela será preenchido pelo outro componente.

falseExemploExemplo 1 - Editando o valor WidthExemplo 1 - Editando o valor WidthExemplo 1 - Editando o valor WidthExemplo 2 - Editando o valor WidthExemplo 2 - Editando o valor WidthExemplo 2 - Editando o valor Width

Ilustrando o exemplo ao alterar a propriedade ***Height*** do campo observação, que é do tipo memorando, e pode ter esse valor alterado. Mas nem todos os componentes podem ter o valor height alterado.

falseExemplo HeightExemplo 1 - Editando o valor HeightExemplo 1 - Editando o valor HeightExemplo 1 - Editando o valor HeightExemplo 2 - Editando o valor HeightExemplo 2 - Editando o valor HeightExemplo 2 - Editando o valor Height

# Ocultamento/Exibição de campos

---

       Os componentes podem ser ocultos ou exibidos, de acordo com a necessidade. Assim sendo, não necessariamente um componente cadastrado no projeto aparecerá inicialmente na visão de inclusão do formulário.

Podemos ocultar ou exibir os campos movendo os entre a aba principal e a aba de **Itens Ocultado**. Veja os exemplos a seguir:

false

O componente **TESTE** na imagem abaixo, está oculto e não aparece no formulário.

* Visão de Personalização:

* Formulário:

* Agora, caso arrastemos o campo para o layout principal, dessa forma:

* Podemos notar que automaticamente o formulário passa a exibir o campo:

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Metadados

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
