---
content_hash: b2041cb015f7fb74e3e27faf584398ded54e1f2894e35333a6ecdbae757f038c
fetched_at: '2026-06-29T00:09:14.827407+00:00'
page_id: '421385271'
product: rm
source: tdn-rm
title: Exportação de Composição para o Excel 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385271
version: 4
---

**Exportação de Composição para o formato Microsoft Excel**  
 Este processo tem por finalidade realizar a exportação de composições para o formato Microsoft Excel seguindo o layout exigido pelo DNIT. Existem dois modelos de relatório nesse processo, Planilha de Composição Analítica de Preço Unitário e a Planilha de Composição de Custo Unitário. A exportação é realizada através do  menu: Nova MDI| menu Projeto | Selecionar Projeto | Acessar o menu Orçamento | Composições | Cadastro | Processos |opção: Gerar Relatório de Modelo Fixo Excel, informar os filtros de acordo com o solicitado no formulário de exportação e Executar o Processo.  
 A partir da versão 12.1.5, a exportação de composições para MS Excel poderão ser executadas independente da solução da Microsoft, ou seja, não há necessidade que a máquina em que a exportação está sendo realizada tenha o pacote office instalado.

**Formulário de Exportação**  
 Arquivo: neste campo deverá ser informado o caminho do diretório onde o arquivo exportado será salvo.    
 Considerar composições auxiliares: as composições auxiliares que estiverem associadas às composições selecionadas na visão para serem exportadas, juntamente com os recursos destas composições auxiliares serão detalhadas no relatório exportado.  
 Considerar apenas composições utilizadas no projeto: No relatório exportado, serão apresentadas somente as composições que estão sendo utilizadas no projeto e, o usuário poderá realizar um filtro selecionando o Cenário ou a Planilha que deseja exportar ou ainda se deseja considerar as Tarefas de Custo Indireto para serem exportadas no relatório.

Para o usuário filtrar o Cenário ou a Planilha que deseja exportar é necessário que o parâmetro 'Utiliza Planilha de Serviço' disponível nos parâmetros gerais do Projeto no menu Projeto | Construção e Projetos | Projetos | Planilha de Serviços esteja ativo, caso contrário está opção não será habilitada no momento de gerar o relatório.  
Planilha de Composição Analítica de Custo Unitário: No relatório exportado serão apresentadas composições do tipo CPU (Composição de Preço Unitário) com os recursos associados agrupados por Grupo DNIT, possuindo os campos: Valor Parcial, Custo Direto, B.D.I e Total.   
Planilha de Composição Analítica de Preço Unitário por Produção: No relatório exportado serão apresentadas composições do tipo produção com os recursos associados agrupados por Grupo DNIT, possuindo os campos: A-Equipamento, B-Mão de Obra, E-Materiais, F-Transporte, Custo Direto Total, Bonificação e Preço Unitário Total.   
Planilha de Composição Analítica (Todas): Ao selecionar na visão uma ou mais composições do tipo CPU e do tipo Produção, no relatório exportado serão exibidos os dois layouts (Planilha de Composição analítica de custo unitário e Planilha de composição analítica de preço unitário por produção) em conjunto, sendo exibidas todas as composições selecionadas na visão, agrupadas por Grupo DNIT.  
Selecionando na visão uma composição do tipo Unidade de Serviço e uma composição do tipo Turma Típica o layout que será exibido será o da Planilha de Composição de Custo Unitário, detalhando os recursos da composição por Unidade de Serviço e também os recursos da Turma Típica.

Os modelos de exportação irão respeitar o número de casas decimais e o tipo de tratamento valor, configurados nos parâmetros de projeto no menu Projeto | Construção e Projetos | Projetos | aba Exibição | subaba Geral. Quando exportados para o Microsoft Excel o arredondamento ou truncamento dos valores (parametrização disponível no menu Projeto | Construção e Projetos | Projetos | aba Cálculo | subaba Outros) assim como o número de casas decimais, será de acordo com a relação abaixo:   
  
 ·          Planilha de composição analítica de custo unitário  
 o    Coluna: Coeficiente   
 §   Número de casas em quantidade  
 o    Coluna: Valor Unitário e Valor Parcial  
 §   Número de casas em Monetários  
  
 ·          Planilha de composição de preço unitário por produção  
 o    A - Equipamento  
 §   Coluna: Utilização e Custo de Operação  
 ·          Número de casas em quantidade  
 §   Coluna: Custo Horário  
 ·          Número de casas em monetários  
 o    B - Mão de Obra  
 §   Coluna: Quantidade  
 ·          Número de casas em quantidade  
 §   Coluna: Salário Base e Custo Horário  
 ·          Número de casas em monetários  
 o    E – Materiais  
 §   Coluna: Consumo  
 ·          Número de casas em quantidade  
 §   Coluna: Custo e Custo Horário  
 ·          Número de casas em monetários  
 o    F – Transporte  
 §   Coluna: Consumo   
 ·          Número de casas em quantidade  
 §   Coluna: D.M.T (P), D.M.T (T), Total D.M.T, Custo e Custo Horário  
 ·          Número de casas em monetários

**Atenção:**  
Para ambiente 3 camadas ou host remoto, deverá ser informado nos parâmetros globais do projeto um caminho de rede a ser utilizado pelo módulo que deverá ser compartilhado, com permissão total de leitura e escrita, para todos os usuários da rede visto que tanto as estações de trabalho (usuários das máquinas clientes) quanto o servidor de aplicação (usuário do Host.Service) acessarão esse caminho para realização de cópia e leitura dos arquivos a serem restaurados ou gerados.  
  
Para ambiente local o Host.service localizado no serviço Windows, deverá rodar no contexto de um usuário de rede com permissão para acessar o caminho compartilhado, pois o usuário padrão ao instalar o serviço é o NETWORK SERVICE e o mesmo não possui permissão de navegar entre as pastas na rede. Os dados de "usuário" e "senha" deverão ser informados.

**Melhorias para Mercado Internacional Calculo por Rendimento Diário.**  
  
 Disponível somente para o mercado internacional, para licitações públicas que exigem o detalhamento dos serviços (composições) por rendimento.  
**Processo "Gerar relatório de modelo fixo EXCEL".**  
 "Gerar relatório de modelo fixo EXCEL" disponível nos processos de cadastro de composição. Composição/ Processos/ Gerar relatório de modelo fixo. Presente os campos: Informações de jornada, rendimento de mão de obra e de equipamentos para a composição e o campo equipe para os recursos.
