---
content_hash: 65760015eaf3aa15ae8c00b0ae91cf9bee17cc98b1c1526cb3bc048bc5c99d54
fetched_at: '2026-06-29T00:09:02.513443+00:00'
page_id: '379317617'
product: rm
source: tdn-rm
title: Visualizador de Relatórios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=379317617
version: 12
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       O objetivo deste documento é demonstrar as funcionalidades básicas da tela de Visualizador de Relatórios. Esta tela será utilizada por aplicações de terceiros a qualquer momento que desejarem visualizar o relatório.

# Parâmetros/Filtros:

---

       É possível alterar os parâmetros e filtros do relatório clicando no botão "Parâmetros/Filtros" no canto superior da tela.

Fonte de Dados2Parâmetros

Nesta aba, é possível alterar o valor dos parâmetros para geração do relatório. Para isso, basta clicar em "Editar" e modificar o valor do parâmetro.

******Exemplo prático abaixo:******

3Filtros

Nesta aba, é possível adicionar, remover ou alterar o valor dos filtros para geração do relatório.

Ativo?

Caso essa opção esteja marcada (Sim), o filtro será aplicado à Entidade . Caso contrário (Não), o filtro será desativado e os dados da respectiva tabela não serão filtrados.

******Exemplo prático abaixo:******

# Funcionalidades:

---

1- Seleciona qual página do relatório será exibida.

2- Move para a página seguinte / move para a ultima página

3- Adiciona uma barra de rolagem e mostra todas as páginas na tela

4- Controle do zoom da página

5 - Imprime o relatório

6- Imprime somente a página atual do relatório

7- Exporta para o formato selecionado: (PDF, XLS, XLSX, TRF, DOCX, MHT, HTML, Text, CSV ou Imagem)

8- Realiza uma busca no relatório.

# Integração de terceiros:

---

       Aplicações de terceiros podem utilizar o relatório integrado ao seu sistema. Para isso deve-se realizar uma implementação que possibilite essa integração. Um código exemplo está disponível em [treports-viewer-sample](https://github.com/totvs/treports-viewer-sample).

Existe também a opção de abrir somente o visualizador de um report de forma externa através de uma URL específica em qualquer navegador.

http://{URL\_TReports}/reportsviewer/external/{GUID\_ReportRequest}?access\_token=\{TokenValido} 

* URL\_TReports: endereço onde está hospedado a aplicação treports
* GUID\_ReportRequest:  UID retornado ao se enviar os parâmetros de execução do relatório no endpoint

* TokenValido: Token válido com permissão no relatório pretendido. Pode ser feito utilizando as APIs do TRac [Recuperando o AccessToken](https://tdn.totvs.com/x/Np-lG#Integra%C3%A7%C3%A3oProdutoxTReports-RecuperandoAccessToken:).

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Visualizador de Relatórios

falsefalse

**Status:** Pendente

false

**Data:** 08/07/2018

false

**Autores:**
