---
content_hash: 610f8443ccce5b9cc738a893170325dd1afc87e75d98f4cff5a78b260c427a3a
fetched_at: '2026-06-29T00:08:14.276349+00:00'
page_id: '244445620'
product: rm
source: tdn-rm
title: ER_SAUHRM01-43_Novos_STATUS_Coleta_Triagem_Nova_Coleta
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_SAUHRM01-43_Novos_STATUS_Coleta_Triagem_Nova_Coleta
version: 6
---

|  |
| --- |
| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo** **extremamente** **técnico.** |

|  |  |  |  |
| --- | --- | --- | --- |
| Especificação |  |  |  |
| Produto | TOTVS GESTÃO HOSPITALAR | Módulo | RM SAÚDE |
| Projeto | SAUHRM01 | IRM | SAUHRM01-27 |
| Requisito | SAUHRM01-43 | SubTarefa | SAUHRM01-127 |
| País | ( X ) Brasil  (  ) Argentina  (  ) México  (  ) Chile  (  ) Paraguai  (  ) Equador   (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. |  |  |

# \_Toc355276661\_Toc355276662Objetivo

Possibilitar ao cliente um maior controle sobre os pedidos de exames e suas amostras facilitando o rastreamento das mesmas desde a coleta do exame até a realização e resultados destes.   
 Para tanto, se faz necessário a implementação de novos status e controles, estes em uma mesma tela do sistema para facilitar a usabilidade do sistema.   
 Estes novos status e controles serão específicos para exames LABORATORIAIS .   
 Para não afetar o processo de outros clientes, será implementado a criação de um parâmetro que habilitará ou não este novo fluxo das Amostras.   
 Haverá o processo de gerenciamento de Recoleta de amostra onde serão informados os dados da amostra e após o processamento o sistema mudará o status da amostra para "N" = Recoleta.

# \_Toc355276664Definição da Regra de Negócio

**RN001** – Para o novo processo funcionar, será criado um parâmetro na tela de parâmetros gerais, para que o cliente escolha o processo de utilizar o fluxo com triagem da amostra..Caminho: Opções/Parâmetros Gerais/Unidades Diagnosticos/Laboratório   
 **RN002** – Os status a serem implementados são; "Saiu para Coleta", "Triado no Laboratório". Os demais status são os que já existem no sistema.  
 A Ordem cronológica dos status é a seguinte;

* "I" – Inicial, já existe no sistema , quando é feito o pedido de Exame.
* "P" – "Saiu para Coleta". Após a impressão das etiquetas das amostras;
* "S" – "Triado no Laboratório" – Será em uma tela já existente no sistema onde serão confirmadas as informações das Amostras.
* "N" – Recoleta – será em uma nova tela do sistema, onde serão informadas as amostras a serem recoletadas.
* 'D' – Digitação – Status Já existente, o mesmo ocorrerá após a retorno dos resultados via importação do protocolo de comunicação.

No comportamento atual do sistema, após o status "I"=Inicial, o proximo status é o "D"= Digitação. Com o parâmetro marcado para o novo processo, entre o "I" e o "D" entrarão os status ""P" e "T" .Para os demais status o sistema deverá seguir fluxo já existente no processo atual.   
   
 **RN003** – Status I = "Inicial" - Quando o médico faz o pedido de exames o sistema gera o status do tipo "I" (Status Inicial).  
 A Biomédica aplicará um filtro do sistema para buscar os exames que terão sua etiquetas impressas.   
 **RN004** – Status P = "Saiu para Coleta" - Quando as etiquetas forem impressas o sistema deverá gerar um novo status para o pedido/Amostra que é, "Saiu para Coleta".   
 **RN005** – Status S = "Triado no Laboratório" - Quando o material coletado chega na área de triagem o mesmo terá suas etiquetas lidas ou digitadas no sistema.Neste momento ao confirmar a triagem o sistema alterará o status de "Saiu para Coleta" para "**Triado no Laboratório".** A tela para esta confirmação já existe no sistema no menu :   
   
 A mesma será através do ícone "Tela de triagem" que será criado na tela de "Controle e pedidos de Eames". Assim, o cliente terá estas informações em uma única tela.   
 **RN006** – Status "N" = "Recoleta" - Necessidade de **recoleta** – Este processo será utilizado caso haja algum problema com a amostra já coletada, o mesmo ocorrerá no Laboratório no momento da triagem. Para as Amostras com esta necessidade será gravado um Log identificando a amostra a ser recoletada e justificativa da mesma.. ver tela3.  
 A Biomédica aplicará um filtro do sistema para buscar as amostras com status "N" para a re-impressão das novas etiqueta.   
 **RN007** - No processo de exportação dos pedidos para a execução da analise das amostras via protocolo de comunicação. O sistema deverá respeitar as seguinte regra;

* Somente permitir a Exportação quando o status estiver com tipo "S" Este filtro é para o processo quando o parâmetro "Utiliza Fluxo com Triagem de Amostras " estiver marcado.
* Se o parâmetro não estiver marcado, o filtro será pelo status será o do tipo "I"

**RN008** – O Sistema deverá registrar no log todas as mudanças de status.(Função já existente no sistema).

|  |  |  |  |
| --- | --- | --- | --- |
| Rotinas Envolvidas |  |  |  |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** |
| Preenchimento de Resultado | Alteração | Controle de pedidos de Exames/Preenchimento de resultados |
| Parãmetros Gerais | Alteração | Opções/Parâmetros Gerais/Unidades Diagnosticos/Laboratório |

# Escopo Negativo

# \_Toc355276665Protótipo de Tela

|  |  |
| --- | --- |
| \_Toc355276666**Regras da Interface** |  |
| **RI-001** | Tela 1 – Após o pedido de exames o status é "I"=Inicial.   Também serão criados dois ícones que farão as chamadas das telas de Triagem(tela2) e tela de Recoleta(Tela3).   O ícone de impressão da etiqueta já existe no sistema.   Nas , telas: 1.1, 1.2 e 1.3º exemplo das trocas de status após cada fase do processo.   * Impressão da Etiqueta o sistema trocará o status de "I" para tipo "P" – Que representa o "saiu para coleta " * Ícone – de chamada da tela de Triagem – Tela 2; * Ícone – de Chamada da tela de Reocoleta Tela 3; |
| **RI-002** | Tela 2 – Triagem de Amostra.Tela Já existente no sistema.        Solicitará o Agente de coleta. Esta informação é um cadastro pre definido no caminho: Cadastros/Unidades de Diagnostico/Agente de Coleta.   Numero do Pedido e setor – O sistema só poderá trazer os pedidos/Amostras que estiverem com status tipo "P" ;   Marcação do tipo de entrada de dados da etiqueta:   Manual ou Por código de Barras;   Processar – Após selecionar a amostras triadas efetuar o **processar** que gerará os logs deste evento.(Informações já existentes no sistema). |
| **RI-003** | Na tela 1.1 – Após Impressão das Etiquetas o sistema mudará o status para "P"; |
| **RI-004** | Na tela 1.2 – Após processo descrito na **RI-002** o sistema trocará o status para tipo "S"; |
| **RI-005** | Tela 3 – Tela Para Informar a Amostra que for recoletada e a Justificativa para a mesma. Tela que precisa ser criada, utilizar como base a tela 2;          Solicitará o Agente de coleta. Esta informação é um cadastro pre definido no caminho: Cadastros/Unidades de Diagnostico/Agente de Coleta.   Numero do Pedido e setor – O sistema só poderá trazer os pedidos/Amostras que estiverem com status tipo "P" ;   Marcação do tipo de entrada de dados da etiqueta:   Manual ou Por código de Barras;   Justificativa:Texto obrigatório para Justificar a recoleta   Processar – Após selecionar a amostras efetuar o **processar** que gerará os logs deste evento   e mudará o status do Pedido/Amostra para o tipo "N". A Etiqueta terá que ser emitida novamente. |
| **RI-006** | Na Tela 1   Ao clicar no Ícone – Troca de Informações com o Matrix   Na exportação, o sistema deverá garantir que somente os pedidos com status do tipo "T" sejam exportados para a analise. |
| **RI-007** | Na tela 1.3 – Após restorno dos resultados da analise para o sistema RM o sistema deverá trocar o status para o tipo "D", pois poderá haver a necessidade de correção manual nos resultados exportados. |
| **RI-008** | Tela 4 – Marcando o Parametro o sistema utilizartá o Fluxo com triagem de amostra. Desmarcado, o fluxo será o já existente. |

# \_Toc355276667Fluxo do Processo

\_GoBack

# Dicionário de Dados

Não necessário para o desenvolvimento deste requisito.

# Grupo de Perguntas

Não necessário para o desenvolvimento deste requisito.

# **Consulta Padrão**

Não necessário para o desenvolvimento deste requisito.

# Estrutura de Menu

Não necessário para o desenvolvimento deste requisito.
