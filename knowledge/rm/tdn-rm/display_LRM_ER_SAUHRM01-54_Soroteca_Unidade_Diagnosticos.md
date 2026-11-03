---
content_hash: 2e18552cc436af4bc388a3a00a4dc1e2ec5bfafc9641e939ff9d0d87e96e1495
fetched_at: '2026-06-29T00:08:12.755513+00:00'
page_id: '243648280'
product: rm
source: tdn-rm
title: ER_SAUHRM01-54_Soroteca_Unidade_Diagnosticos
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_SAUHRM01-54_Soroteca_Unidade_Diagnosticos
version: 4
---

|  |  |  |  |
| --- | --- | --- | --- |
| Especificação |  |  |  |
| Produto | GESTÃO HOSPITALAR - RM | Modulo | Unidade de Diagnostico |
| Segmento Executor | Saúde |  |  |
| Projeto¹ | SAUHRM01 | IRM¹ | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM01-39 |
| Requisito¹ | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM01-54 | SubTarefa¹ | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM01-270 |
| Chamado² |  |  |  |
| Release de Entrega Planejada | Não definido | Réplica | Não necessário |
| País | ( X ) Brasil  (  ) Argentina  (  ) México  (  ) Chile  (  ) Paraguai  (  ) Equador   (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. |  |  |
| Outros |  |  |  |

\_Toc355276661\_Toc355276662

# Objetivo

Quando um paciente realiza qualquer tipo de exame que exige coleta, as amostras são enviadas para a análise. Ao término desse procedimento, alguns tipos de materiais precisam ser armazenados para futuras conferências ou estudos formando uma espécie de acervo com prazo de validade de alguns dias ou semanas, dependendo do tipo de amostra.   
 Esse armazenamento é chamado de **soroteca** e evita que o paciente precise refazer todas as etapas para um novo exame, caso necessário. Isso proporciona mais agilidade nos processos, evitando geração de novos custos e dando mais credibilidade às unidades laboratoriais.   
 O Cliente solicita que este controle seja implementado ao Sistema de Gestão Hospitalar RM.  
 \_Toc355276664

# Definição da Regra de Negócio

**RN001** – Criação de tela de cadastro de Racks de amostras (Ver protótipo tela 1.1). Nesta tela serão incluídas as informações de linhas e colunas para localização das amostras. Os campos serão;

* Nome do RACK – Descrição do local de armazenamento das amostras;
* Número de Linhas – Quantidade linhas do rack. A partir da quantidade de linhas o sistema irá implementar automaticamente a quantidade até o limite informado.
* Inicia em – O sistema irá implementar a sequência a partir desta informação. Campo alfanumérico (Pode iniciar com uma letra ou número);
* Número de colunas – Quantidade de colunas do rack.A partir da quantidade de colunas o sistema irá implementar automaticamente a quantidade até o limite informado.
* Inicia em – O sistema irá implementar a sequência a partir desta informação. Campo alfanumérico (Pode iniciar com uma letra ou número)
* Nome do Armazenamento – informação que terá sua origem a partir do cadastro de local de armazenamento do Rack.

**RN002** – Criação de tela de cadastro de Local de armazenamento do Rack – Esta tela servira para complementação do cadastro de Rack. (Ver protótipo tela 1.2)  
 **RN003**– Criação de tela para gestão da soroteca.Nesta tela será possível a consulta, inclusão e exclusão de amostras de um determinado Rack. (Ver protótipo tela 2.1);  
 **RN004** – Criação de Log de exclusão quando uma amostra for excluída do Rack. Indicando a Justificativa da Exclusão.  
 Este log servirá para descarte das amostras vencidas nos racks.  
 O Mesmo deve conter as seguintes informações;

* Data Hora;
* Usuário da exclusão;
* Motivo exclusão;
* Número Amostra;
* Número Pedido;
* Linha e coluna do Rack;
* Rack da amostra;
* Data Validade da amostra.

**RN005** –Criação de novo status de exames. Exames que forem incluídos na sorotéca terão seu status alterado no sistema. O mesmo ficará com status "S" Soroteca. ((Ver protótipo tela 3);

|  |  |  |
| --- | --- | --- |
| Rotinas Envolvidas |  |  |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** |
| Rack - Soroteca | Inclusão/alteração/consulta/Exclusão | Cadastros/Unidades de diagnósticos |
| Local de Armazenamento Rack | Inclusão/alteração/consulta/Exclusão | Cadastros/Unidades de diagnósticos |
| Gestão da Soroteca | Inclusão/Consulta/Exclusão | Unidades de diagnósticos/Soroteca |
|  |  |  |

# \_Toc355276665Escopo Negativo

Não fazem parte deste escopo relatórios e estatísticas;

# Protótipo de Telas

As imagens de telas destacadas a seguir são consideradas apenas protótipos, as mesmas poderão sofrer alterações em função da atualização de componentes utilizados no sistema, devem ser utilizadas apenas para exemplificar a forma de iteração que os usuários possuirão ao acessar o HIS, o fluxo de negócio e a forma em que os dados e informações serão manipuladas.   
 Tela 1 – Menu com as opções de Cadastro de Rack e Local de armazenamento do Rack.   
   
   
   
 Tela 1.1 – Cadastro de Rack - Soroteca   
   
   
   
   
   
   
 Tela 1.2 – Cadastro de Local de Armazenamento do Rack  
   
   
   
   
   
   
   
   
   
   
   
   
 Tela 2 – Menu de acesso a Gestão de Soroteca;   
   
   
   
   
   
   
 Tela 2.1 – Gestão de soroteca  
   
   
   
   
   
 Tela 3 – Envio para Soroteca registrado no Histórico do Pedido de Exame.   
  
   
   
   
   
   
 \_GoBack

|  |  |
| --- | --- |
| \_Toc355276666**A** |  |
| **RI-001** | **Tela 1.**   **Incluir nesta tela os menus : sinalizados em vermelho. Rack- Soroteca disparará a tela 1.1.**   **Local de Armazenamento do Rack disparará a tela 1.2.** |
| **RI-002** | **Tela 1.1**   **Nome:** **Nome do dispositivo que irá armazenar as amostras. Exemplo: Bandeja Laranja ou RACK – Laranja. O nome pode ser cadastrado identificando a cor do item de armazenamento.**   **Número de Linhas****: Representa o número de linhas que o armazenador terá. Ao informar o número, o sistema criará automaticamente a quantidade de linhas conforme o valor informado. Assim, o usuário não precisará criar várias vezes o registro.**   **Número de colunas**: **É a quantidade de colunas que o armazenador terá, exemplo, uma planilha Excel com linhas e colunas. O sistema criará automaticamente a quantidade de linhas conforme o valor informado. Assim, o usuário não precisará criar várias vezes o registro.**   **Linha Inicia em:** **Valor de início da implementação automática. Exemplo: Se o cliente colocar que inicia em "1" o sistema irá implementar automaticamente a sequência até a letra "10" inclusive. Então as linhas serão "1,2,3,4,5,6,7,8,9,10".**   **Coluna Inicia em:** **Valor de início da implementação automática. Exemplo: Se o cliente colocar que inicia em "A" o sistema irá implementar automaticamente a sequência até a letra "J" inclusive. Então as linhas serão "A,B,C,D,E,F,G,H,I,J". Serão 10 vezes para cada letra, pois são dez linhas (conceito de Matriz).**   **Nome do Armazenamento:** **Nome dado ao local que irá armazenar o Rack. Este será oriundo do cadastro de Local de Armazenamento do Rack.** |
| **RI-002** | **Tela 1.2** Cadastro do Local de Armazenamento do Rack. Pode ser um freezer ou outro local qualquer. |
| **RI-003** | **Tela 2**   **Incluir nesta tela o menu sinalizado em vermelho. Este disparará a tela 2.1.** |
| **RI-004** | **Tela 2.1**   **Inclusão:** **Nesta opção o usuário escolherá o Rack em que a amostra será armazenada.**   **Este deve ser um rack valido.**   **Após o sistema validar o rack o próximo campo será o "Código de barras" onde o cliente utilizará o leitor de códigos de barras na etiqueta da amostra.**   **Somente permitir a inclusão de amostras no rack quando o status dos exames estiverem em situação de liberado "L". Do contrário não permitir.**   **Após leitura o próximo campo será a "Data de Validade" onde o cliente informará o tempo de validade da amostra.**   **Após informar esta, o sistema salvará automaticamente o registro e o sistema irá se posicionar novamente no campo "Código de barras". Repetindo as operações posteriores.**   **As informações destas entradas de amostras serão refletidas ao lado esquerdo (em amarelo).**   **As informações conterão os seguintes dados:**   **N.do pedido****;**   **N.da Amostra****;**   **Validade da Amostra** **(Campo digitado após leitura do código de barras);**   **Exames** **– Mnemônico dos exames da amostra**   **Data e hora da coleta do exame;**   **Data e hora da Liberação do exame****;**   **Responsável técnico** **- Quem liberou o Exame**   **Nome do paciente;**   **Idade;**   **Prontuário;**   **Atendimento;**   **Médico responsável pelo atendimento;**   **Convênio;**   **Data de entrada do paciente;**   **Clinica;** |
| **RI-005** | **Tela 2.1**   **Pesquisa:**   **Nesta tela será possível a pesquisa das amostras Por:**   **Rack;**   **Nome do paciente;**   **Pedido.**   **Por RACK – O sistema trará todas as amostras catalogadas no RACK;**   **Por Nome do paciente: trará todas as amostras catalogadas para o paciente;**   * **Se existirem para o paciente amostras catalogas em mais de um rack, ao clicar no quadro Linha x coluna o sistema mostrará no topo o número do Rack e as informações destas no quadro a esquerda.**          **Por Pedido: O sistema trará todas amostras do pedido.** * **Se existirem para o paciente amostras catalogas em mais de um rack, ao clicar no quadro Linha x coluna o sistema mostrará no topo o número do Rack e as informações destas no quadro a esquerda. (Mesma situação da tela acima.**     **Caso existam amostras com a data de validade vencida o sistema mostrará esta em destaque.**   **Exemplo:** |
| **RI-006** | **Tela 2.1**   **Exclusão**   **Nesta tela será possível efetuar a exclusão das amostras de um determinado Rack;**   * **A exclusão poderá ser feita por RACK, onde todas as amostras do Rack serão excluídas;** * **A exclusão poderá ser feita por amostra onde o cliente poderá selecionar via leitura de código de barras.**   **Ao selecionar a amostra para exclusão o sistema deverá solicitar uma justificativa e gerar um log com os dados da amostra, usuário e data / hora da operação.** |
| **RI-007** | **Tela 3**  **Quando amostras do pedido de exame forem enviadas para a Soroteca será registrado no o envio no histórico de controle do pedido de exame.** |

# \_Toc355276667Fluxo do Processo

# Dicionário de Dados

Não necessário para o desenvolvimento deste requisito.

# Grupo de Perguntas

Não necessário para o desenvolvimento deste requisito.

# **Consulta Padrão**

Não necessário para o desenvolvimento deste requisito.r

# Estrutura de Menu

Não necessário para o desenvolvimento deste requisito.
