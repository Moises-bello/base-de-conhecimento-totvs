---
article_id: 360052504474
category: Contabilidade Gerencial - Procedures, Parâmetros,Campos, Gatilho
content_hash: 219b78c48ed7e4217aeda9c1a333d02d6f7547323c5d837321132a14e48ed3b8
fetched_at: '2026-06-28T22:41:01.369403+00:00'
product: protheus
section_id: 1500001537361
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB  PARÂMETROS CONTÁBEIS
type: support-article
updated_at: '2023-10-17T20:16:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052504474-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-PAR%C3%82METROS-CONT%C3%81BEIS
---

**Dúvida**

* Parâmetros utilizado pelo modulo contábil
* Parâmetros considerado que devem ser avaliados antes da  inclusão do lançamento contábeis

**Ambiente**Microsiga Protheus - Contabilidade Gerencial - A partir da versão 11.80  
  
**Solução**

|  |  |  |
| --- | --- | --- |
| **Nome do          Parâmetro** | **Descrição do Parâmetro** | **Conteúdo Padrão** |
| **MV\_AGLHIST** | Indica se considera o histórico dos lançamentos contábeis na aglutinação dos mesmos. Válido   somente para o ambiente Contabilidade Gerencial (SIGACTB). | F |
| **MV\_ALTLCTO** | Permite alterar os lançamentos contábeis de integração. No caso de não permitir a alteração de   lançamentos, e se estes tenham alguma inconsistência de valor  ou entidades contábeis não   existentes, o lançamento será obrigatoriamente gravado como pré-lançamento. | S |
| **MV\_ATUSAL** | Atualiza Saldos Contábeis Básicos durante o lançamento.  (S) para atualização ou (N) para não   atualizar. | S |
| **MV\_CONSOLD** | Código de empresa/filial destino na consolidação. Se existir mais de uma consolidação, utilizar a   barra "/" para separá-los. Ex:  Empresa 01 com filial 03 e Empresa 05 com filial 09 =>   0103/0509. | N |
| **MV\_CONTBAT** | Não permite confirmar a inclusão/alteração de um lançamento contábil quando débito não bater   com crédito. | N |
| **MV\_CONTSB** | Indica se a contabilização será feita mesmo que os valores de débito e crédito não batam. Se   estiver com "S", gravará o lançamento contábil sem verificação de valores. Caso contrário,   dependerá da configuração de MV\_CONTBAT. | N |
| **MV\_CONTSLD** | Indica se a validação de Débito e Crédito do lançamento contábil será efetuada por Tipo de   Saldo (evitando que sejam gerados lançamentos à débito e à credito em tipos de saldo   diferentes. Se não for necessário efetuar esta validação, preencher o conteúdo com “N”. | S |
| **MV\_CRITPLN** | Define se o critério de conversão utilizado no lançamento contábil será o  cadastrado no Plano   de Contas (T), ou o existente no Inicializador Padrão do campo CT2\_CONVER. | T |
| **MV\_CTASUP** | Indica se a impressão do Plano de Contas será feita por Ordem de Código da Conta, ou pela   ordem da Conta Superior. Afeta Impressão de: Balancetes de Conta e Cadastro do Plano de   Contas. | N |
| **MV\_CTB390F** | Permite que uma fórmula seja usada no cálculo dos valores de Orçamento durante o cadastro /   revisão | VALOR\*1.1 |
| **MV\_CTGBLOQ** | Parâmetro que indica quais Status do Calendário serão considerados para o bloqueio do   Reprocessamento. Se estiver em branco, nenhum Bloqueio de calendário será considerado. Se   quiser bloquear o Status 2 e 3, informe “23” no conteúdo. | M |
| **MV\_CTBQBPG** | Indica se a impressão do Diário ou Razão terão numeração de página reiniciada ou não.  U =   Quebra única, M = Múltiplas Quebras |  |
| **MV\_CTBAPLA** | Configura se, ao excluir lançamentos contábeis de integração, será efetuada limpeza dos flags   de contabilização nas tabelas de origem dos lançamentos, permitindo nova integração dos   movimentos para a contabilidade, em que:   “1” Inativo: não limpa os flags nas tabelas de origem do lançamento;   “2” Perguntar: pergunta ao usuário se deseja efetuar a remarcação de flags nas tabelas origem   de integração;   “3” Automático com alertas: remarca/limpa os flags nas tabelas origem de integração, sem   perguntar ao usuário. Exibe alertas e, caso detecte inconsistências, guarda log dos flags   remarcados e não marcados na exclusão;   “4” Automático sem alertas: remarca/limpa os flags nas tabelas origem de integração sem   perguntar ao usuário. Não exibe alertas de inconsistências, guarda log dos flags remarcados e   não marcados na exclusão.   Importante: na alteração com exclusão de linhas ou exclusão do lançamento, na pergunta   apresentada ( com o parâmetro MV\_CTBAPLA = '2' ), 'Limpar flags de contabilização nas tabelas de origem?' se respondido 'Sim' limpa os flags de origem, se 'Não' , não limpa , e se escolhido   'Não Excluir' , não exclui os lançamentos se estes foram 'deletados', mas as alterações nas   linhas serão mantidas. Estas opções são referentes as linhas excluídas na alteração ou exclusão. | 1 |
| **MV\_DIASPRO** | Número de dias para projeção da inflação. | 120 |
| **MV\_LBALABE** | Arquivo que contém o texto do Termo de Abertura do Balanço Patrimonial. | LDIARAB.TRM |
| **MV\_LBALFEC** | Arquivo que contém o texto do Termo de Encerramento do Balanço Patrimonial. | LDIAREN.TRM |
| **MV\_LDIARAB** | Arquivo que contém o texto do Termo de Abertura do Diário Geral. | DIARAB.TRM |
| **MV\_LDIAREN** | Arquivo que contém o texto do Termo de Encerramento do Diário Geral. | LDIARAB.TRM |
| **MV\_LRAZABE** | Arquivo que contém o texto do Termo de Abertura do Razão Contábil. | LRAZABE.TRM |
| **MV\_LRAZENC** | Arquivo que contém o texto do Termo de o Geral. | LRAZENC.TRM |
| **MV\_LOTECON** | Indica se o controle do número do próximo lote de lançamento contábil será feito pela tabela 09   (T), ou será gerado automaticamente pelo último disponível (U). | T |
| **MV\_MASCARA** | Definição da máscara contábil. Deverá ser informado o número de dígitos para cada nível.   Utilizada somente para impressão de relatórios e consultas. | 11123 |
| **M\_MASCCUS** | Definição da máscara de centro de custo. Deverá ser informado o número de dígitos para cada   nível. Utilizada somente para impressão de relatórios e consultas. | 1111 |
| **MV\_MASCCTD** | Definição da máscara de Item Contábil. Deverá ser informado o número de dígitos para cada   nível. Utilizada somente para impressão de relatórios e consultas. | 1111 |
| **MV\_MASCCTH** | Definição da máscara de Classe de Valor. Deverá ser informado o número de dígitos para cada   nível. Utilizada somente para impressão de relatórios e consultas. | 1111 |
| **MV\_MCONTAB** | Indica qual o ambiente contábil a ser utilizadopelo.  CTB = SIGACTB (Contabilidade Gerencial) e   CON = SIGACON (Contabilidade - até a versão Protheus 6.09). | CTB |
| **MV\_NUMLIN** | Limita o número de linhas do documento no lançamento contábil de integração | 999 |
| **MV\_NUMMAN** | Limita o número de linhas do documento no lançamento contábil manual | 999 |
| **MV\_OCRAPRV** | Indica se deve utilizar o critério de aprovação para a rotina de orçamento. Válido somente para   o ambiente Contabilidade Gerencial (SIGACTB). | S |
| **MV\_OPTNFE** | Indica se a Contabilização da Nota Fiscal de Entrada será efetuada com queries especificas. | F |
| **MV\_OPTNFS** | Indica se a Contabilização da Nota Fiscal de Saída será efetuada com queries especificas. | F |
| **MV\_ORDLCTB** | Permite que seja escolhida a ordem de contabilização nas rotinas de Lançamento Contábil Off-   Line. Para contabilizar por ordem de entrada (Recno), deixe o parâmetro como "E"; se desejar   utilizar a ordem por lançamento padrão, configure como "L". | L |
| **MV\_PRELAN** | Indica se a contabilização gera lançamentos contábeis (N) ou pré-lançamentos (S) quando   documento não bater débito com crédito ou no caso de não existirem cadastradas as entidades   contábeis envolvidas. | N |
| **MV\_REDUZID** | Indica se a digitação das entidades contábeis será feita diretamente a partir do código reduzido   (S) ou será utilizado o caracter "\*" (N) | N |
| **MV\_SLDCOMP** | Define se os Saldos Compostos serão atualizados no momento da emissão do relatório (S) ou   durante o Reprocessamento (N) | N |
| **MV\_SOMA** | Determina se o total digitado em lançamento tipo 3 (partida dobrada) será somado 1 ou 2   vezes. | 1 |
| **MV\_SUBLOTE** | Indica se será utilizado o Sub-Lote no Lançamento Contábil. Se o conteúdo do parâmetro   estiver preenchido o sistema assumirá sempre essa numeração. | 001 |
| **MV\_TPVALOR** | Indica qual o tipo de sinal será impresso nos relatórios contábeis. S = Imprimirá valores com   Sinal P = Imprimirá valores negativos entre Parenteses D = Imprimira "D" ou "C" após os   valores C = Imprimirá "C" somente dos valores Credores | D |
| **MV\_CTBAMAR** | Ativa controle de Amarração nos lancamantos contábeis. Definição 0=Não tem amarração,   1=Regra de níveis, 2=Regra de Amarração tabela CTA. | 1 |
| **MV\_CTBHENT** | Parâmetro descontinuado, não possui usabilidade no produto padrão. Sua premissa era habilitar o controle de histórico de alterações de entidades contábeis. |
