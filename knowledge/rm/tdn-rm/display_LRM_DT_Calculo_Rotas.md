---
content_hash: 4e9931512efb5ca8dc081d58e0a401433664976e2a60f7aef352bccc3a933209
fetched_at: '2026-06-29T00:06:06.150965+00:00'
page_id: '201728650'
product: rm
source: tdn-rm
title: DT_Calculo_Rotas
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Calculo_Rotas
version: 15
---

# CALCULO DE ROTAS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão de Pessoas* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Acompanhamento* | *Armazenamento de informações de rota e valor de transporte das pessoas* | |
| **Versões/Release:** | *12.1.7* |

## Descrição

Pelo TOTVS Gestão de Pessoas é possível armazenar informações de rota e valor de transporte dos funcionários. Neste mesmo contexto, também fornece um serviço configurável de integração para popular esta estrutura por meio de serviços de um sistema externo.  
 

## Procedimento para Utilização

Para ativar a integração é necessário acessar o sistema TOTVS Gestão de Pessoas e em seguida o caminho **Configurações / Parametrizador / 07.00.12 - Roteirização / Roteirização**. Feito isso será exibido a tela de **Parametrização do serviço de cálculo de rotas do SatRota**s onde será possível habilitar a integração com Sat Rotas e preencher as informações de URL, usuário e senha do webservice e o código da empresa para uso do serviço de roteirização.

O SAT Rotas como fornecedor da solução de roteirização mantém a assinatura da mensagem que faz parte do escopo de integração para que o serviço permaneça sempre em funcionamento.

As configurações sobre os parâmetros de conexão para o fornecedor do serviço de roteirização são de responsabilidade do departamento técnico do cliente. Estas poderão ser configuradas sempre que necessário.

O caminho para**Solicitar Cálculo de Rotas** está no menu **Planejamento e captação / Painel de Seleção / Perfil da vaga / Etapas da seleção / Anexo / Candidatos da Etapa / Processos / Solicitar Cálculo de Rotas**. Este processo tem por objetivo gerar um registro de solicitações de informação de Transporte e Rota de uma pessoa (Cód. Informação), a partir da integração “TOTVS Gestão de Pessoas x Serviço de Rotas e Transportes”. Este processo poderá ser executado em quaisquer etapas do processo seletivo e mais de uma vez, caso necessário.

O usuário deverá primeiramente selecionar os candidatos que deseja solicitar as rotas no Anexo**Candidatos da Etapa** e então executar o processo **Solicitar Cálculo de Rotas**

O assistente desse processolocalizará automaticamente os endereços de cada candidato previamente selecionados, individualmente, de acordo com o informado no cadastro de pessoas destes candidatos, ou seja, buscar os endereços de origem, para que sejam geradas as informações via integração. Ao executar o assistente, será disponibilizado a tela para **Solicitar Cálculo de Rotas** contendo a listagem de seções para escolha.

Os endereços das seções deverão estar cadastrados no sistema, de forma que ao selecionar alguma seção, o endereço desse seja encontrado. Após selecionar as seções, o processo deverá ser executado e as informações enviadas via *web service*para o SAT Rotas, de forma a roteirizar um candidato por vez e por destino, de acordo com a sequência de envio.   
   
 É possível elaborar filtros para o usuário filtrar somente seções que representem sites. Também é possível criar fórmulas visuais que não permitam a execução do processo para seções que não sejam sites.

Exemplo:

• Candidatos selecionados: José e Maria  
• Sites selecionados: Alegria e Lapa

Resultado do processo:

1. Cód 001 – Rota do Endereço José versus Endereço Site Alegria  
 2. Cód 002 – Rota do Endereço José versus Endereço Site Lapa  
 3. Cód 003 – Rota do Endereço Maria versus Endereço Site Alegria  
 4. Cód 004 – Rota do Endereço Maria versus Endereço Site Lapa

Após a execução do assistente, o sistema gavará os identificadores dos pedidos de solicitação de cálculo de rotas (ID Rota), de acordo com a quantidade de destinos selecionados - um registro por endereço de destino distinto.

\*Importante: Poderão ser criados filtros por perfil para demonstrar no assistente apenas seções referentes à uma praça determinada, de acordo com o perfil do usuário.   
 Para o caso de reprocessamento, as informações previamente geradas deverão ser substituídas pela última roteirização.

O processo para **Informações de Rota e Transporte** que permite a visão de Pessoas é localizado através do menu **Acompanhamento / Pessoas / Anexo / Informações de Rota e Transporte**ou analogamente através do menu**Planejamento e Captação / Painel de Seleção / Perfil da vaga / Etapas da seleção / Anexo / Candidatos da Etapa / Anexo / Informações de Rota e Transporte**. Este anexo tem por objetivo armazenar os registros de informação de rotas (origem e destino da pessoa em relação ao local de trabalho) e transportes (linhas de coletivos e valor do transporte).

Quando os endereços de origem ou destino estiverem diferentes dos endereços dos respectivos cadastros de Pessoa e Seção deverá ser exibido uma mensagem de alerta na visão e edição de Informação de Rota e Transporte alertando que a rota traçada está desatualizado.   
  
**Importante:** Este cadastro não irá alimentar os cadastros de Linha e Tarifa do TOTVS Folha de Pagamento, ou seja, no momento do cadastro os dados não irão para a folha de pagamento do funcionário.  
Não haverá um cadastro de linha e tarifa, portanto o ajuste de tarifa dos transportes será feito ao executar o processo **Buscar resultados de roteirização**.  
Somente registros que estejam com status ‘Manual’ poderão ter dados de informação de rota e transporte incluídos, editados ou excluídos manualmente, para todos os outros status estas operações deverão ser bloqueadas.

O procedimento para Buscar Resultados da Roteirização está através do menu **Planejamento e captação / Painel de Seleção / Perfil da vaga / Etapas da seleção / Anexo / Candidatos da Etapa / Processos / Buscar Resultados da Roteirização**. Este processo tem por objetivo gerar um registro de informação de Transporte e Rota de uma pessoa, a partir da integração “TOTVS Gestão de Pessoas x Serviço de Rotas e Transportes”. Este processo poderá ser executado em quaisquer etapas do processo seletivo e mais de uma vez, caso necessário, e também do Anexo Informações de Rota e Transporte na visão de Candidatos da Etapa, a partir da Aba Rota.

O usuário deverá primeiramente selecionar os candidatos que deseja solicitar as rotas no Anexo “Candidatos da Etapa”

e então executar o processo Buscar Resultados da Roteirização.

Ao executar este processo será aberto um assistente que permita resgatar e armazenar as informações de rotas e transporte, dos candidatos previamente selecionados, fornecidas via web service do SAT Rotas. O processo deverá buscar os códigos de cada uma das rotas traçadas para aquele candidato que estejam com status ‘Pendente’, de acordo com as informações registradas na aba “Rotas”, no Anexo “Informações de Rotas e Transporte”. Todas as rotas geradas por candidato deverão ser armazenadas no TOTVS Gestão de Pessoas (RM Vitae), individualmente no Anexo proposto (Informações de Rotas e Transporte) para que permitam a avaliação e indicação das melhores rotas posteriormente. Ao término do processo de Buscar Resultados da Roteirização, o sistema emitirá um alerta indicando o resultado apurado.

Para o retorno positivo das rotas solicitadas, o campo “Motivos” da Aba “Rota” do Anexo “Informações de Rotas e Transporte”, deverá ser automaticamente preenchido com “Concluído” e o campo status deverá ser gravado como “Roteirizado”. Se ocorrer alguma falha no retorno da *web service* (Exemplo: “Departamento Técnico”) ou quaisquer outros motivos ocasionem no cadastro parcial da rota em questão, o sistema deverá permitir gravar a mensagem de retorno, com o motivo da falha da roteirização para estes casos, no campo “Motivos” da Aba “Rota” do Anexo “Informações de Rotas e Transporte”, o campo status deverá ser gravado como “Não Roteirizado”.  
   
Para auxiliar na seleção dos candidatos que desejam-se buscar as rotas traçadas, deverão ser disponibilizados novas colunas na visão de candidatos para:

• Indicar o “status da roteirização”, baseado no preenchimento do campo “Status” no Anexo Informações de Rotas e Transporte, a fim de evitar um reprocesso para um mesmo candidato.   
 • Distância entre a origem e o destino da rota;  
 • Valor dia da rota calculada.

Todas as colunas estarão disponíveis para elaboração de filtros a partir da opção de filtro da coluna (ícone de filtro disponível no título da coluna) na visão de candidatos; Também será adicionada a possibilidade de visualizar anexos de candidatos, incluindo o anexo de rotas e transportes diretamente na visão do painel de seleção.

Os status disponíveis serão:

• Manual – Registro incluído manualmente, os transportes também devem ser cadastros manualmente. Não haverá integração com serviço de roteirização para este status.  
 • Pendente – enquanto o processo “Solicitar Cálculo de Rotas” não for executado.   
 • Roteirizado – para as rotas processadas através de “Buscar Resultados de Roteirização”, que geraram os Cadastros: Linhas de Transporte/Rotas, Tarifa de Transporte/Rota e Tipo de Transporte.  
 • Não Roteirizado - para as rotas processadas através de “Buscar Resultados de Roteirização”, que geraram quaisquer tipos de falhas no retorno do web service (Ex: “Departamento Técnico”) ou quaisquer outros motivos ocasionem no cadastro parcial da rota em questão.

No parametrizador do sistema na aba Planejamento e Captação, tem um parâmetro definido ''Exibição de informações de rotas na visão de candidatos de etapa''

As seguintes opções estão disponíveis:

• Exibir informações da última roteirização;  
 • Exibir informações da última roteirização realizada com sucesso;  
 • Exibir informações da roteirização de menor valor.

O processo “Geração automática de Transporte e Rota (via integração)” somente poderá ser exibido caso a integração esteja configurada.
