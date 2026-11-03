---
content_hash: 16efe0bbebeb950b906f40dbed4a4121d701c22c0924fcd54e3cb17d93ee8bc1
fetched_at: '2026-06-29T00:08:13.350768+00:00'
page_id: '244416744'
product: rm
source: tdn-rm
title: RPTMIG00035.1.1 - Utilização de Controles de Detalhe em Sub-Relatórios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244416744
version: 9
---

# Utilização de Controles de detalhe em Sub-Relatórios

|  |  |
| --- | --- |
| **Produto:** | TOTVS Reports |
| **Versões:** | 12.1.x |
| **Ocorrência:** |  |
| **Ambiente:** |  |
| **Passo a passo:** | Introdução  ---     Com o advento da migração do **TOTVS Reports** da **versão 11.8x** para as versões **superiores a versão 12.1.4**, muitas alterações foram feitas principalmente **na geração sobre demanda dos dados** vinculados a cada componente presente no relatório.  Em relatórios da versão **11.8x**, por exemplo, **a geração sobre demanda dos dados** era realizada no momento da impressão de cada componente, ao contrário dos das versões mais atuais **(12.1.5 ou superiores)**, onde a geração dos dados é feita através de apenas uma consulta SQL **(Fase de Preparação)**, que é gerada a partir das tabelas e consultas SQL vinculadas ao relatório. 1 - Utilização de Controles de Detalhe em Sub-Relatórios  ---     Vamos utilizar o relatório abaixo como base para a explicação da funcionalidade de **Utilização de Controles de Detalhe em Sub-Relatórios**.  **Imagem 1** - Relatório exemplo.  No relatório exemplificado acima temos um campo **IDPARCELA** e um subrelatório **SUBRELATORIO1** com o seguinte desenho**:**  **Imagem 2 -** SubRelatório1.  Esse sub-relatório contém três campos, **CCUSTO**, **DEPTO** e **RATEIO**.    Os parâmetros que serão utilizados para a geração do relatório são:   | N° | Nome do Parâmetro | Descrição do Parâmetro | | --- | --- | --- | | 1 | agente | Nome da Instituição Financeira. | | 2 | Data | Data base para rateio. |     **Imagem 3** - Parâmetros para Geração do Relatório. 1.1 - Impressão dos controles (Devex)  ---     A impressão dos controles no relatório segue a seguinte ordem:   | N° | Nome | Descrição | | --- | --- | --- | | 1 | Posição dos controles na tela. | Baseado nas coordenadas (X,Y) dos controles. Controles com posicionamento mais próximos da coordenada (0,0) são impressos primeiro. | | 2 | Binding (Ligação de dados). | Controles que não contém ligação de dados são impressos primeiro do que controles com ligação de dados. |    1.2 - Configuração do Relatório  ---     Para que o relatório seja gerado corretamente **utilizando um controle presente no Detalhe em um sub-relatório**, o controle que será utilizado no sub-relatório deverá vir com o valor da **Posição Y MAIOR** que o valor **da Posição Y** do controle de sub-relatório.  2image2016-7-20 14:39:29.png, image2016-7-20 14:38:28.png, image2016-7-20 14:41:24.png, image2016-7-20 14:42:55.png, image2016-7-20 14:43:28.png, image2016-7-20 14:51:7.pngGaleria Posição Controles  Na galeria acima, observe nas duas imagens **que a posição Y é a mesma para ambos**.  O Resultado da geração do relatório é esse: **(Relatório com o sub-relatório em branco)**  **Imagem 6 -** Relatório onde o sub-relatório é gerado em branco.  Utilizando a **posição Y** do controle de sub-relatório **MAIOR** que a do controle **IDPARCELA,** o sub-relatório é gerado normalmente**.**  1image2016-7-20 14:39:29.png, image2016-7-20 14:38:28.png, image2016-7-20 14:41:24.png, image2016-7-20 14:42:55.png, image2016-7-20 14:43:28.png, image2016-7-20 14:49:10.png, image2016-7-20 14:47:54.pngGaleria Posição Controles (2)  Na galeria acima observe que o valor da **posição Y** do controle de sub-relatório pode ser qualquer valor maior do que o valor da **posição Y** do controle **IDPARCELA.** No caso:   | N° | Nome do Controle | Valor da Posição Y do Controle | | --- | --- | --- | | 1 | IDPARCELA | 0 | | 2 | SUBRELATORIO1 | 0,1 |   O Resultado dessa modificação faz com que o sub-relatório agora seja gerado normalmente.  **Imagem 8 -** Relatório onde o sub-relatório é gerado normalmente. |
| **Observações:** |  |
