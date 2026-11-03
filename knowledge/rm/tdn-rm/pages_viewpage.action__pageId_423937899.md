---
content_hash: 76ed5e1e121ceb82514244e038023f8889472950a1d6fad4f01b00e39f51cdfb
fetched_at: '2026-06-29T00:09:24.122306+00:00'
page_id: '423937899'
product: rm
source: tdn-rm
title: Versão 11.40.0 (TOTVS Gestão Planejamento e Controle da Produção)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423937899
version: 3
---

**11.40.0 -** **Andamento de Ordens de Produção**: O Andamento de Ordens de Produção foi migrado para plataforma .NET da Microsoft, obtendo melhorias de usabilidade, funcionalidade e performance. A nova interface permite a visualização das informações completas de cada ordem de produção com: itens de ordem, mapa da engenharia do produto acabado e/ou semiacabado, atividades da do item de ordem, apontamento múltiplo, convencional e localização de atividade e ordem de produção por código de barras.  
    
 **11.40.0 -** **[Apontamento Convencional](http://tdn.totvs.com/pages/viewpage.action?pageId=423938039)**: O Apontamento Convencional foi migrado para a plataforma .NET da Microsoft, obtendo melhorias de usabilidade, funcionalidade e performance. Com a nova interface de Controle de Apontamento da Atividade é possível visualizar as abas com as informações do apontamento agrupadas por processo. A edição de dados está mais dinâmica, sendo possível alterar dados diretamente pela grid, sem a necessidade de edição do registro.  
    
 **11.40.0 -** **[Apontamento Múltiplo por Atividades](http://tdn.totvs.com/pages/viewpage.action?pageId=423938041)**: O Apontamento Múltiplo por Atividades foi migrado para a plataforma .NET da Microsoft, obtendo melhorias de usabilidade, funcionalidade e performance. Com a nova interface é possível organizar e agrupar as colunas para obter a melhor visualização dos dados conforme necessidade. Foi implementada a funcionalidade de preenchimento automático das quantidades a apontar, a fim de agilizar o processo de inserção de dados e realização do apontamento das atividades.  
    
 **11.40.0 -** [**Apontamento Múltiplo por Estrutura**](http://tdn.totvs.com/pages/viewpage.action?pageId=423938053): O Apontamento Múltiplo por Estrutura foi migrado para a plataforma .NET da Microsoft, obtendo melhorias de usabilidade, funcionalidade e performance. Foi implementada a funcionalidade de apontamento de perda de produção através do Apontamento Múltiplo por Estrutura. Com a nova interface é possível organizar e agrupar as colunas para obter a melhor visualização dos dados conforme necessidade.  
    
 **11.40.0 -** **[Apontamento Simplificado](http://tdn.totvs.com/pages/viewpage.action?pageId=423938056)**: O Apontamento Simplificado foi migrada para a plataforma .NET da Microsoft, obtendo melhorias de usabilidade, funcionalidade e performance. A tela de Apontamento Simplificado foi reformulada e está mais intuitiva, as funcionalidades: iniciar atividade, inserir e excluir atividade opcional, e cancelar atividade estão agrupadas em forma de processo facilitando o acesso.  
    
 **11.40.0 -** **[Apontamento via Código de Barras](http://tdn.totvs.com/pages/viewpage.action?pageId=423938044)**: O Apontamento via Código de Barras foi migrado para plataforma .NET da Microsoft, obtendo melhorias de usabilidade, funcionalidade e performance. O apontamento via Código de Barras foi totalmente reestruturado e agora possibilita realizar o apontamento de todos os detalhes das atividades através de código de barras. É possível apontar por código de barras: materiais, mão de obra, equipamentos, Índices de Registro de Produção, Registro de Qualidade e Parada de Atividade.  
Foram disponibilizados novos relatórios migrados para a plataforma .NET (RM Reports) para realização de Apontamento via Código de Barras, os relatórios foram reformulados visando atender as novas funcionalidades desse tipo de apontamento.  
    
 **11.40.0 -** **[Estoque Intermediário](http://tdn.totvs.com/pages/viewpage.action?pageId=423938071)**:Foi implementada a visão de consulta ao Estoque Intermediário do Posto de Trabalho. Através dessa funcionalidade é possível visualizar todas as necessidades de materiais por Posto de Trabalho e Ordem de Produção. Também é possível consultar as quantidades atuais de materiais disponíveis e perdidos que estão no Estoque Intermediário, com seus respectivos lotes e números de séries.  
    
 **11.40.0 - Controle de Perda de Materiais:**Foi implementado o controle de perda de produção e materiais no TOTVS Planejamento e Controle da Produção. Com esse novo controle é possível informar no apontamento da ordem de produção os materiais que foram perdidos durante a execução do processo produtivo e também a produção perdida de acabados e semiacabados. Os materiais perdidos ao entrar para o estoque serão centralizados em um local previamente configurado para perda de material.  
    
 **11.40.0 - Rastreabilidade de Lote e Número de Série:**Foi implementado o controle de rastreabilidade para materiais controlados por lote e/ou número de série. Agora todas as movimentações de produtos com esses controles no TOTVS Planejamento e Controle da Produção terão seu lote e/ou número de série gravados no sistema, permitindo que os materiais utilizados no processo de produção possam ser totalmente rastreados.   
Os lotes e números de série movimentados poderão ser visualizados na tela de "Histórico de Movimentação de Estoque" em Anexos| Lotes Movimentados e Anexos| Núm. Série Movimentados.   
O sistema com o controle de rastreabilidade passa a fazer todo controle de consumo de lotes e números de série, sendo necessário informar esses dados em todo apontamento realizado, caso sejam utilizados produtos controlados por lote e/ou série.  
    
 **11.40.0 - Identificação de Lote nas movimentações:**Com a implementação do controle de rastreabilidade, as movimentações de produtos controlados por lote realizadas no TOTVS Planejamento e Controle da Produção passam a utilizar o Identificador do Lote para controle interno no banco de dados, permitindo assim que o Número do Lote possa ser alterado no TOTVS Gestão de Estoques, Compras e Faturamento, sem que se tenha perda de referência e integridade das informações.   
    
 **11.40.0 - Centro de custo na ordem de produção:**Foi implementada a utilização de centro de custo na ordem de produção.  
Quando o sistema estiver parametrizado para utilizar o Centro de Custo da Ordem de Produção, todos os movimentos gerados a partir de ordem de produção irão levar para o TOTVS Gestão de Estoques, Compras e Faturamento o centro de custo informado no item da ordem ou na ordem de produção. Com essa nova funcionalidade ao associar um pedido de venda do TOTVS Gestão de Estoques, Compras e Faturamento a uma ordem de produção será possível vincular ao item da ordem um centro de custo vindo do pedido de venda.  
    
 **11.40.0 -** **[Baixa de Materiais](http://tdn.totvs.com/display/LRM/Baixa+de+Materiais)**:A Baixa de Materiais foi migrada para plataforma .NET da Microsoft. Com isto, a baixa de materiais apresenta melhorias de usabilidade e funcionalidade. Será possível efetuar baixa de materiais para apontamento parcial, baixa por atividade apontada ou por quantidade igual, maior ou menor que o previsto. Na tela de baixa de materiais, através do botão direito do mouse sobre "Locais de Estoque/Lotes Associados", poderão ser visualizados ou editados os dados de "Informações do Lote" do produto.

**11.40.0 -** **[Solicitação de Compras](http://tdn.totvs.com/pages/viewpage.action?pageId=423937922)**: A Solicitação de Compras foi migrada para plataforma .NET da Microsoft, obtendo melhorias de usabilidade e funcionalidade. Na geração de solicitação de compra para várias ordens é possivel parametrizar se será gerado no TOTVS Gestão de Estoques, Compras e Faturamento um único  movimento para todas as ordens de produção ou um movimento para cada ordem de produção. Na promoção de várias ordens de produção serão listadas na tela de solicitação de compra as necessidades de todas as ordens selecionadas. Materiais de atividades canceladas não serão listadas na solicitação de compra.

**11.40.0 -** : A funcionalidade de Empenho de Materiais foi migrada para plataforma .NET da Microsoft. Desta forma, obteve melhorias de usabilidade e funcionalidade. Será possivel desempenhar materiais de atividades canceladas.  
    
 **11.40.0 - Outras atualizações:**Realizada melhoria na exibição e cálculo de Campos Livres na geração de ordens de produção a partir de pedidos de venda.  
 Realizada melhoria no Recálculo de Custo de OP, os Semiacabados fabricados na produção de um Acabado e não utilizados, terão seu movimentos de entrada no estoque atualizados pelo recálculo de custo quando houver alteração na composição do seu custo.
