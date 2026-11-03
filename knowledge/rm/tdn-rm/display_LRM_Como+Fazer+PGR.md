---
content_hash: 96c5a07d47c69f31a3c3b3bf78c4ffed04e5717de000e937e33ad3c92373d681
fetched_at: '2026-06-29T00:10:58.755880+00:00'
page_id: '606429825'
product: rm
source: tdn-rm
title: Como Fazer PGR
type: documentation
url: https://tdn.totvs.com/display/LRM/Como+Fazer+PGR
version: 20
---

Programa de Gerenciamento de Risco é um relatório decorrente das alterações na [NR01](https://www.gov.br/trabalho-e-emprego/pt-br/acesso-a-informacao/participacao-social/conselhos-e-orgaos-colegiados/comissao-tripartite-partitaria-permanente/normas-regulamentadora/normas-regulamentadoras-vigentes/NR01atualizada2024II.pdf) conforme [Portaria MTE nº 1.419](https://www.gov.br/trabalho-e-emprego/pt-br/assuntos/inspecao-do-trabalho/seguranca-e-saude-no-trabalho/sst-portarias/2024/portaria-mte-no-1-419-nr-01-gro-nova-redacao.pdf), de 27 de Agosto de 2024.   
Tem como Objetivo gerenciar os riscos existentes na empresa.

**Como Fazer PGR**

Como padrão, o sistema disponibilizará alguns modelos de PGR baseado em Seção, Local de Trabalho ou Lotação, lembrando que cada empresa deve adaptar este modelo a sua própria realidade.

No book de relatórios do sistema, serão disponibilizados os itens que compõem os modelos:

* Oracle
  + RHUREL0027 - PGR(por Seção) - NR01 - ORACLE.TotvsReport
  + RHUREL0030 - PGR(por lotação) - NR01 - ORACLE.TotvsReport
  + RHUREL0032 - PGR(por local de trabalho) - NR01 - ORACLE.TotvsReport
* SQL Server
  + RHUREL0028 - PGR(por Seção) - NR01 - SQL.TotvsReport
  + RHUREL0031 - PGR(por lotação) - NR01 - SQL.TotvsReport
  + RHUREL0033 - PGR(por local de trabalho) - NR01 - SQL.TotvsReport

E  para correta geração do mesmo, estes deverão ser importados para o sistema pelo menu  **Gestão| RM Reports | Processos | Importar Estrutura de Relatório.**

**Criando o relatório:**

Para criar o relatório de PGR será necessário primeiramente definir o "Tipo de Relatório" a ser desenvolvido, para isso o usuário deverá acessar **Relatórios | Tipos de Relatórios**, e incluir um relatório do tipo: "**PGR**".  
Para geração do modelo de PGR, com o relatório selecionado clicar em: **Processos | Gerar Modelo de PGR**.   
Caso o cliente deseje alterar o modelo de PGR disponibilizado pelo sistema, na aba "Itens do Relatório" será possível incluir itens do tipo texto, onde ao clicar no botão "Editar Texto", será exibido um editor de texto para o usuário digitar suas informações.  
Na mesma aba, o usuário poderá incluir um relatório a partir do RM Reports. Neste caso, basta selecioná-lo no Lookup de relatórios e selecionar o relatório desejado.

**Gerando o relatório -**Para gerar o relatório de PGR, o usuário deverá acessar o menu **Relatórios | Relatórios PGR**.   
Ao selecionar o tipo de relatório a ser gerado serão habilitadas a abas:

* Identificação:
  + Preencher com as informações devidas conforme relatório importado ou conforme a parametrização estabelecida em caso de adequação dos mesmos à realidade da empresa.  
    Pode definição é obrigatório o preenchimento de um código, um período (início e fim), uma descrição, um tipo de relatório (direcionado ao tipo PGR criado) e em seguida o(s) parâmetro(s) conforme modelo utilizado:

    - Quando for utilizado o modelo Seção, deverá ser preenchido o Lookup de Seção
    - Quando for utilizado o modelo Local de Trabalho, deverá ser preenchido o Lookup de Local de Trabalho
    - Quando for utilizado o modelo Lotação, deverão ser preenchidos os Lookups de Seção e Função.
* Parametrização:  
  + Nessa aba, serão exibidos os parâmetros do relatório utilizado e quando preenchidas as informações na aba de identificação corretamente, todos os parâmetros desta aba estarão preenchidos.
* Gerar/Visualizar:
  + Nessa aba há dois botões:
    - Gerar Relatórios: Ao clicar nesse botão o sistema irá realizar o processamento dos dados e montagem do relatório final do PGR.  
      Obs.: Os dados obtidos a partir dos itens de relatórios que estão relacionados ao RM Reports serão gerados como imagem e não poderão ser editados.
    - Visualizar Relatório: Ao clicar nesse botão será aberta uma tela de opção escolher onde será salvo o arquivo do relatório e após salvar o relatório será aberto.

**Importante:**

* Relatório disponível a partir da versão: 12.1.2406
* A emissão do relatório já está adequada à [Portaria MTE nº 1.419](https://www.gov.br/trabalho-e-emprego/pt-br/assuntos/inspecao-do-trabalho/seguranca-e-saude-no-trabalho/sst-portarias/2024/portaria-mte-no-1-419-nr-01-gro-nova-redacao.pdf), já trazendo os riscos Psicossociais.
