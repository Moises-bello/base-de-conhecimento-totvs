---
content_hash: c02e2d735c7927facdd52b525c9a54a54308c9dfe556789a13cc5c2f712aa7ef
fetched_at: '2026-06-29T00:06:00.142656+00:00'
page_id: '194512125'
product: rm
source: tdn-rm
title: ER_Calculo_Rotas
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_Calculo_Rotas
version: 17
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Pessoas | **Módulo** | RHU |
| **Segmento Executor** | RHU – DESENVOLVIMENTO RHU006 | | |
| **Projeto1** |  | **IRM1** | PCREQ-1939 |
| **Requisito1** | PCREQ-1940 | **Subtarefa1** | PDR\_RHU\_RHU006-47 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** |  | **Réplica** |  |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** |  | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Criação de estrutura de cadastros necessária para armazenamento de informações de rota e valor de transporte das pessoas no TOTVS Gestão de Pessoas. Neste mesmo contexto, também fornecer um serviço configurável de integração para popular esta estrutura por meio de serviços de um sistema externo.

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Acompanhamento | Alteração | Acompanhamento > Pessoas | - |
|  |  |  |  |

**Integração: Sistema Externo de Rotas/Transporte**

Será criado uma integração entre o TOTVS Gestão de Pessoas com o Web Service Sat Rotas para obtenção de informação de rotas e transportes. Essa integração será realizada através do TOTVS Gestão de Pessoas, onde será criado uma parametrização específica para configuração de serviços de roteirização.

\*Será criado um script padrão para configurar a integração utilizando o webservice da empresa SAT Rotas, para atender os requisitos do projeto participativo.

Para ativar a integração é necessário acessar o sistema TOTVS Gestão de Pessoas e em seguida o caminho **Configurações > Parametrizador > 07.00.12 - Roteirização > Roteirização**. Feito isso será exibido uma tela de parametrização onde será possível habilitar a integração com Sat Rotas e preencher as informações de URL do webservice, usuário do webservice, senha do webservice e código da empresa para uso do serviço de roteirização **(Protótipo 1 – Parametrizador de roteirização)**.

O SAT Rotas como fornecedor da solução de roteirização, deverá manter a assinatura da mensagem que faz parte desse escopo de integração, para que o serviço permaneça sempre em funcionamento. Caso este serviço necessite de atualizações ou modificações, uma nova versão da mensagem deverá ser desenvolvida mantendo a anterior em funcionamento para clientes legados.

As configurações sobre os parâmetros de conexão para o fornecedor do serviço de roteirização são de responsabilidade do departamento técnico do cliente. Estas poderão ser configuradas sempre que necessário, de acordo com o **Protótipo 1** informado neste documento.

**Processo: Solicitar Cálculo de Rotas**

Criar um processo denominado “Solicitar Cálculo de Rotas”, que deverá ser localizado através do menu **Planejamento e captação> Painel de Seleção> Perfil da vaga> Etapas da seleção> Anexo> Candidatos da Etapa > Processos > Solicitar Cálculo de Rotas**. Este processo tem por objetivo gerar um registro de solicitações de informação de Transporte e Rota de uma pessoa (Cód. Informação), a partir da integração “TOTVS Gestão de Pessoas x Serviço de Rotas e Transportes”. Este processo poderá ser executado em quaisquer etapas do processo seletivo e mais de uma vez, caso necessário.

O usuário deverá primeiramente selecionar os candidatos que deseja solicitar as rotas no Anexo “Candidatos da Etapa” **(Protótipo 2 - Anexo Candidatos da Etapa)** e então executar o processo Solicitar Cálculo de Rotas, conforme demonstrado no Protótipo 4 - Processo Solicitar Cálculo de Rotas. O assistente desse processo **(Protótipo 4 - Assistente do Processo Solicitar Cálculo de Rotas)** deverá localizar automaticamente os endereços de cada candidato previamente selecionados, individualmente, de acordo com o informado no cadastro de pessoas destes candidatos, ou seja, buscar os endereços de origem, para que sejam geradas as informações via integração. Ao executar o assistente, será disponibilizado uma tela contendo a listagem de seções para escolha, conforme apresentado no protótipo 5. Os endereços das seções deverão estar cadastrados no sistema, de forma que ao selecionar alguma seção, o endereço desse seja encontrado. Após selecionar as seções, o processo deverá ser executado e as informações enviadas via web service para o SAT Rotas, de forma a roteirizar um candidato por vez e por destino, de acordo com a sequência de envio.

Exemplo:

• Candidatos selecionados: José e Maria

• Seções selecionados: Alegria e Lapa

Resultado do processo:

1. Cód 001 – Rota do Endereço José versus Endereço Seção Alegria  
2. Cód 002 – Rota do Endereço José versus Endereço Seção Lapa  
3. Cód 003 – Rota do Endereço Maria versus Endereço Seção Alegria  
4. Cód 004 – Rota do Endereço Maria versus Endereço Seção Lapa

Após a execução do assistente, o sistema deverá gravar os identificadores dos pedidos de solicitação de cálculo de rotas (ID Rota), de acordo com a quantidade de destinos selecionados - um registro por endereço de destino distinto. De acordo com o Protótipo 6 - Anexo Informações de Rota e Transporte - Aba Rota.

**Anexo: Informações de Rota e Transporte**

Criar um anexo denominado “Informações de Rota e Transporte” para a visão de Pessoas que ficará localizado através do menu **Acompanhamento > Pessoas > Anexo > Informações de Rota e Transporte** ou analogamente através do menu **Planejamento e Captação> Painel de Seleção> Perfil da vaga> Etapas da seleção> Anexo> Candidatos da Etapa> Anexo> Informações de Rota e Transporte**. Este anexo tem por objetivo armazenar os registros de informação de rotas (origem e destino da pessoa em relação ao local de trabalho) e transportes (linhas de coletivos e valor do transporte).

Para a tela de edição deste novo anexo, conforme pode ser visto no **Protótipo 6 - Anexo Informações de Rota e Transporte - Aba Rota**, no **Protótipo 10 - Anexo Informações de Rota e Transporte – Visão aba Transporte** e **Protótipo 11 - Anexo Informações de Rota e Transporte – Edição aba Transporte**, serão criados os seguintes campos:

Aba Rota:

- ID Rota: código do registro de transporte/rota (ID da rota solicitada);  
- Pessoa;  
- Seção;  
- ID Solicitação Integração: Código gerado pelo serviço de roteirização quando é solicitado um cálculo de rota. Este campo não será preenchido ao cadastrar uma rota manualmente;  
- Data e Horário de atualização: data e horário da última atualização do registro, de acordo com a execução do processo Solicitar Cálculo de Rotas;  
- Status: status da roteirização (Manual, Roteirizado, Não Roteirizado, Pendente);  
- Motivos: de acordo com o resultado gerado pelo processo de Buscar Resultados de Roteirização; se o processo em questão não foi executado, este campo permanecerá em branco;  
- Endereço de origem: endereço de origem da rota (CEP, logradouro, número, bairro, cidade e estado);  
- Endereço de destino: endereço de destino da rota (CEP, logradouro, número, bairro, cidade e estado);  
- Distancia total entre origem e destino.  
- Tempo de deslocamento: tempo gasto de deslocamento  
    Ida – no percurso de ida;  
    Volta - no percurso de volta;   
    Total – no percurso de ida e volta.  
- Valor (R$) gasto para deslocamento: valor gasto para deslocamento  
    Ida – no percurso de ida;  
    Volta - no percurso de volta;   
    Total - no percurso de ida e volta.

Quando os endereços de origem ou destino estiverem diferentes dos endereços dos respectivos cadastros de Pessoa e Seção deverá ser exibido uma mensagem de alerta na visão e edição de Informação de Rota e Transporte alertando que a rota traçada está desatualizada.

Aba Transporte:

- Linha: código e descrição da linha de transporte;  
- Itinerário: itinerário feito pela linha  
- Operadora: Nome da empresa operadora da linha;  
- Tempo: Duração em minutos do tempo da viagem;  
- Valor: Valor da tarifa do transporte;  
- Sentido: Indicação do sentido do transporte na rota (ida ou volta);  
- Sequência: Indicação da sequência do transporte, quando é necessário mais de um transporte coletivo para realizar um trajeto;  
- Tipo: Tipo do transporte (Municipal, Intermunicipal);  
- Cartão: Nome do cartão magnético de passagem;  
- Valor Total (R$) gasto para deslocamento: valor gasto para deslocamento no percurso de ida e volta.

**Importante:** Este cadastro não irá alimentar os cadastros de Linha e Tarifa do TOTVS Folha de Pagamento, ou seja, no momento do cadastro os dados não irão para a folha de pagamento do funcionário.

Não haverá um cadastro de linha e tarifa, portanto o ajuste de tarifa dos transportes será feito ao executar o processo “Buscar resultados de roteirização”.

 Somente registros que estejam com status ‘Manual’ poderão ter dados de informação de rota e transporte incluídos, editados ou excluídos manualmente, para todos os outros status estas operações deverão ser bloqueadas.

**Processo: Buscar Resultados da Roteirização**

Criar um processo denominado “Buscar Resultados da Roteirização”, que deverá ser localizado através do menu **Planejamento e captação> Painel de Seleção> Perfil da vaga> Etapas da seleção> Anexo> Candidatos da Etapa > Processos > Buscar Resultados da Roteirização**. Este processo tem por objetivo gerar um registro de informação de Transporte e Rota de uma pessoa, a partir da integração “TOTVS Gestão de Pessoas x Serviço de Rotas e Transportes”. Este processo poderá ser executado em quaisquer etapas do processo seletivo e mais de uma vez, caso necessário, e também do Anexo Informações de Rota e Transporte na visão de Candidatos da Etapa, a partir da Aba Rota.

O usuário deverá primeiramente selecionar os candidatos que deseja solicitar as rotas no Anexo “Candidatos da Etapa” (Protótipo 2 - Anexo Candidatos da Etapa) e então executar o processo Buscar Resultados da Roteirização, conforme demonstrado no Protótipo 9 - Processo Buscar Resultados de Roteirização. Ao executar este processo será aberto um assistente (Protótipo 8 - Assistente do Processo Buscar Resultados de Roteirização) que permita resgatar e armazenar as informações de rotas e transporte, dos candidatos previamente selecionados, fornecidas via web service do SAT Rotas. O processo deverá buscar os códigos de cada uma das rotas traçadas para aquele candidato que estejam com status ‘Pendente’, de acordo com as informações registradas na aba “Rotas”, no Anexo “Informações de Rotas e Transporte”. Todas as rotas geradas por candidato deverão ser armazenadas no TOTVS Gestão de Pessoas (RM Vitae), individualmente no Anexo proposto (Informações de Rotas e Transporte) para que permitam a avaliação e indicação das melhores rotas posteriormente. Ao término do processo de Buscar Resultados da Roteirização, o sistema emitirá um alerta conforme o Protótipo 9 - Tela do Resultado da Roteirização, indicando o resultado apurado.

Para o retorno positivo das rotas solicitadas, o campo “Motivos” da Aba “Rota” do Anexo “Informações de Rotas e Transporte”, deverá ser automaticamente preenchido com “Concluído” e o campo status deverá ser gravado como “Roteirizado”. Seocorrer alguma falha no retorno do web service (Exemplo: “Departamento Técnico”) ou quaisquer outros motivos ocasionem no cadastro parcial da rota em questão, o sistema deverá permitir gravar a mensagem de retorno, com o motivo da falha da roteirização para estes casos, no campo “Motivos” da Aba “Rota” do Anexo “Informações de Rotas e Transporte”, o campo status deverá ser gravado como “Não Roteirizado”.

**Filtro por Status da Roteirização**

Para auxiliar na seleção dos candidatos que desejam-se buscar as rotas traçadas, deverão ser disponibilizados novas colunas na visão de candidatos para:

• Indicar o “status da roteirização”, baseado no preenchimento do campo “Status” no Anexo Informações de Rotas e Transporte, a fim de evitar um reprocesso para um mesmo candidato.   
• Distância entre a origem e o destino da rota;  
• Valor dia da rota calculada.

Todas as colunas estarão disponíveis para elaboração de filtros a partir da opção de filtro da coluna (ícone de filtro disponível no título da coluna) na visão de candidatos;  
Também será adicionada a possibilidade de visualizar anexos de candidatos, incluindo o anexo de rotas e transportes diretamente na visão do painel de seleção.

Os status disponíveis serão:

• Manual – Registro incluído manualmente, os transportes também devem ser cadastros manualmente. Não haverá integração com serviço de roteirização para este status.  
• Pendente – enquanto o processo “Solicitar Cálculo de Rotas” não for executado.   
• Roteirizado – para as rotas processadas através de “Buscar Resultados de Roteirização”, que geraram os Cadastros: Linhas de Transporte/Rotas, Tarifa de Transporte/Rota e Tipo de Transporte.  
• Não Roteirizado - para as rotas processadas através de “Buscar Resultados de Roteirização”, que geraram quaisquer tipos de falhas no retorno do web service (Ex: “Departamento Técnico”) ou quaisquer outros motivos ocasionem no cadastro parcial da rota em questão.

****Exibição de Informações de Rotas na Visão de Candidatos da Etapa****

Será disponibilizada no parametrizador do sistema uma aba chamada Planejamento e Captação, deverá ter um parâmetro para ser definida a "Exibição de informações de rotas na visão de candidatos de etapa" (Protótipo 12 - Exibição de informações de rotas na visão de candidatos de etapa).  
As seguintes opções estarão disponíveis:

• Exibir informações da última roteirização;  
• Exibir informações da última roteirização realizada com sucesso;  
• Exibir informações da roteirização de menor valor.

****Regras de Integridade****

- O processo “Geração automática de Transporte e Rota (via integração)” somente poderá ser exibido caso a integração esteja configurada.

## Protótipos

Protótipo 1 - Parametrizador de roteirização

Protótipo 2 - Anexo Candidatos da Etapa

Protótipo 3 - Processo Solicitar Cálculo de Rotas

Protótipo 4 - Assistente do Processo Solicitar Cálculo de Rotas

Protótipo 5 - Filtro de localização de Seção

Protótipo 6 - Anexo Informações de Rota e Transporte - Aba Rota

Protótipo 7 - Processo Buscar Resultados de Roteirização

Protótipo 8 - Assistente do Processo Buscar Resultados de Roteirização

Protótipo 9 - Tela do Resultado da Roteirização

Protótipo 10 - Anexo Informações de Rota e Transporte – Visão aba Transporte

Protótipo 11 - Anexo Informações de Rota e Transporte – Edição de Trasnporte

Protótipo 12 - Exibição de informações de rotas na visão de candidatos da Etapa

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
