---
content_hash: 773759a8383f57b472638ebba878100919c5c19157fbf723e7615610389cdaa0
fetched_at: '2026-06-29T00:06:28.732013+00:00'
page_id: '233758359'
product: rm
source: tdn-rm
title: TTWEA0_DT_Periodo_Ferias_Atingindo_3Meses
type: documentation
url: https://tdn.totvs.com/display/LRM/TTWEA0_DT_Periodo_Ferias_Atingindo_3Meses
version: 119
---

# PERIODO DE FÉRIAS ATINGINDO 3 MESES CONSECUTIVOS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **Férias** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Férias* | *Cálculo de Férias* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Férias** | *Cálculo de Férias* | | **Lançamento**  *Finaliza*  *Diferença* | **Lançamento das Férias**  *Finaliza Férias*  *Diferença de Férias* | |
| **Cadastros Iniciais:** | *Cadastro de Férias.* |
| **Parâmetro(s):** | *Evento para pagamento do complemento salarial, quando período de férias atinge 3 meses.* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados Relacionados** | *TTWEA0, TSLZU5, TULQ59* |
| **Requisito (ISSUE):** | *Férias* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL Server, Oracle* |
| **Tabelas Utilizadas:** | *PFUFERIAS, PFUFERIASPER* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Implementação de recursos para atender a situação de férias que atinge 3 meses consecutivos, conforme abaixo.

Criação de 3 novos códigos de cálculo:

349 - INSS FÉRIAS NO TERCEIRO MÊS  
350 - FÉRIAS NO TERCEIRO MÊS  
351 - ADICIONAL DE 1/3 FÉRIAS NO TERCEIRO MÊS

Estes eventos serão lançados no envelope, sempre que existir o 3o. mês no período de férias.

O processo de Finalizar Férias deverá ser executado duas vezes:  
1 - No segundo mês, serão apenas lançadas as bases de cálculo, CC's 44, 78 e 131. O funcionário permanecerá na situação F - Férias.  
2 - No terceiro mês, serão lançados novamente os mesmos eventos de base, CC's 44, 78 e 131, mas demonstrando os valores deste mês. A situação do funcionário será alterada para A - Ativo, e dos dados de férias serão atualizados no cadastro do período aquisitivo.

No lançamento do segundo mês, geralmente serão lançados 28 ou 29 dias de férias, por exemplo. Neste caso será necessário lançar um complemento salarial para completar o pagamento dos 30 dias do mês ao funcionário.

Para isto, foi criada a opção do usuário informar o evento que achar mais apropriado, no Parametrizador, pasta Férias/Controle. Campo "Evento para pagamento do complemento salarial, quando período de férias atinge 3 meses". Este evento obrigatoriamente deverá ter CC 1 ou 2.

No cálculo da Diferença de Férias, serão utilizados os mesmos eventos de diferença do segundo mês, para o terceiro mês.

## Importante

*(Apenas para Microsiga Protheus, versões anteriores à versão 12)*

Antes de executar o compatibilizador informe o **nome do compatibilizador** é imprescindível:

* Realizar o *backup* da base de dados do produto que será executado o compatibilizador (diretório **PROTHEUS\_DATA\DATA**, se versão 10, **ou** **\PROTHEUS11\_DATA\DATA**, se versão 11) e dos dicionários de dados SXs (diretório **PROTHEUS\_DATA\_SYSTEM**, se versão 10, **ou** **\PROTHEUS11\_DATA\SYSTEM**, se versão  11).
* Os diretórios acima mencionados correspondem à **instalação padrão** do Protheus, portanto, devem ser alterados conforme o produto instalado na empresa.
* Essa rotina deve ser executada em **modo exclusivo**, ou seja, nenhum usuário deve estar utilizando o sistema.
* Se os dicionários de dados possuírem índices personalizados (criados pelo usuário), antes de executar o compatibilizador, certifique-se de que estão identificados pelo *nickname*. Caso o compatibilizador necessite criar índices, irá adicioná-los a partir da ordem original instalada pelo Protheus, o que poderá sobrescrever índices personalizados, caso não estejam identificados pelo *nickname*.
* O compatibilizador deve ser executado com a **Integridade Referencial** **desativada\***.

| Atenção  O procedimento a seguir deve ser realizado por um profissional   qualificado como Administrador de Banco de Dados (DBA) ou equivalente!  A ativação indevida da Integridade Referencial pode alterar   drasticamente o relacionamento entre tabelas no banco de dados. Portanto,   antes de utilizá-la, observe atentamente os procedimentos a seguir:   1. No   Configurador (SIGACFG), veja se a empresa utiliza Integridade   Referencial, selecionando a opção Integridade/Verificação   (APCFG60A). 2. Se não   há Integridade Referencial ativa,   são relacionadas em uma nova janela todas as empresas e filiais cadastradas   para o sistema e nenhuma delas estará selecionada. Neste caso, E SOMENTE NESTE, não é necessário   qualquer outro procedimento de ativação   ou desativação de integridade, basta finalizar a verificação e aplicar   normalmente o compatibilizador, conforme instruções. 3. Se há Integridade Referencial ativa   em todas as empresas e filiais, é   exibida uma mensagem na janela Verificação   de relacionamento entre tabelas. Confirme a mensagem para que a   verificação seja concluída, ou; 4. Se   há Integridade Referencial ativa   em uma ou mais empresas, que não   na sua totalidade, são relacionadas em uma nova janela todas as empresas e   filiais cadastradas para o sistema e, somente, a(s) que possui(em)   integridade está(arão) selecionada(s). Anote qual(is) empresa(s) e/ou   filial(is) possui(em) a integridade ativada e reserve esta anotação para   posterior consulta na reativação (ou ainda, contate nosso Help Desk Framework   para informações quanto a um arquivo que contém essa informação). 5. Nestes   casos descritos nos itens “iii” ou   “iv”, E SOMENTE NESTES CASOS, é necessário desativar tal integridade, selecionando a opção Integridade/ Desativar (APCFG60D). 6. Quando desativada a Integridade Referencial,   execute o compatibilizador, conforme instruções. 7. Aplicado o compatibilizador, a Integridade   Referencial deve ser reativada, SE E   SOMENTE SE tiver sido desativada, através da opção Integridade/Ativar (APCFG60). Para isso, tenha em mãos as   informações da(s) empresa(s) e/ou filial(is) que possuía(m) ativação da   integridade, selecione-a(s) novamente e confirme a ativação.     Contate o Help Desk Framework EM CASO DE DÚVIDAS! |
| --- |

1. Em **Microsiga Protheus TOTVS Smart Client** (se versão 10), digite o **nome do compatibilizador** no campo **Programa Inicial**. Descreva se o compatibilizador deve ter uma data específica ou superior para que a atualização nos dicionários seja efetuada corretamente. Importante: Para a correta atualização do dicionário de dados, certifique-se que a data do compatibilizador seja igual ou superior a \_\_\_/\_\_\_/\_\_\_\_.
2. Clique em **OK** para continuar.
3. Após a confirmação é exibida uma tela para a seleção da empresa em que o dicionário de dados será modificado *ou* é apresentada a janela para seleção do compatibilizador. Selecione o programa xxxx().
4. Ao confirmar é exibida uma mensagem de advertência sobre o *backup* e a necessidade de sua execução em **modo exclusivo**.
   1. Clique em **Processar** para iniciar o processamento. O primeiro passo da execução é a preparação dos arquivos.   
      É apresentada uma mensagem explicativa na tela.
   2. Em seguida, é exibida a janela **Atualização concluída** com o histórico (*log*) de todas as atualizações processadas. Nesse *log* de atualização são apresentados somente os campos atualizados pelo programa. O compatibilizador cria os campos que ainda não existem no dicionário de dados.
   3. Clique em **Gravar** para salvar o histórico (*log*) apresentado.
   4. Clique em **OK** para encerrar o processamento.

Descreva se há algum procedimento necessário após a aplicação do compatibilizador.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *(Patch)* deste chamado.

1. Aplique o patch do chamado e execute uma vez a rotina *Informe o nome da rotina*.
2. No módulo *informe o nome do módulo* acesse *informe o caminho* e verifique que o parâmetro *informe o nome do parâmetro* é criado conforme especificações abaixo:

|  |  |
| --- | --- |
| **Nome da Variável:** | *Informe o Nome da Variável* |
| **Tipo:** | *Informe o Tipo* |
| **Descrição:** | *Informe a Descrição* |
| **Valor Padrão:** | *Informe o Valor Padrão* |

## Atualizações do Compatibilizador

*(Apenas para Microsiga Protheus, versões anteriores à versão 12)*

1. *Criação ou Alteração* de **Perguntas** no arquivo **SX1 – Cadastro de Perguntes**:

|  |  |
| --- | --- |
| **Pergunte** | *(X1\_PERGUNT)* |
| **Nome** |  |
| **Grupo** | *(X1\_GRUPO)* |
| **Ordem** | *(X1\_ORDEM)* |
| **Tipo** | *(X1\_TIPO)* |
| **Tamanho** | *(X1\_TAMANHO)* |

2.    *Criação ou Alteração* de tabela no arquivo **SX2– Tabelas**:

|  |  |  |  |
| --- | --- | --- | --- |
| **Chave** | **Nome** | **Modo** | **PYME** |
| **B04**  **(X2\_CHAVE)** | Dente/Região  (X2\_NOME) | C  (X2\_MODO) | N  (X2\_PYME) |

3. *Criação ou Alteração* de Tabelas Genéricas no arquivo **SX5 – Tabelas Genéricas**:

|  |  |
| --- | --- |
| **Chave** | *Ex.:* AR |
| **Descrição** | *Ex.:* Tabela de IR de Aplicações Financeiras |

4. *Criação ou Alteração (mantenha somente a instrução correspondente)*de **Campos** no arquivo **SX3 – Campos****:**

* Tabela BGD - Prod x Cob x Proc x Co-Part:

|  |  |
| --- | --- |
| **Campo** | *(X3\_CAMPO)* |
| **Tipo** | *(X3\_TIPO)* |
| **Tamanho** | *(X3\_TAMANHO)* |
| **Decimal** | *(X3\_DECIMAL)* |
| **Formato** | *(X3\_PICTURE)* |
| **Título** | *(X3\_TITULO)* |
| **Descrição** | *(X3\_DESCRIC)* |
| **Nível** | *(X3\_NÍVEL)* |
| **Usado** | *(X3\_USADO) Informe Sim ou Não* |
| **Obrigatório** | *(X3\_OBRIGAT) Informe Sim ou Não* |
| **Browse** | *(X3\_BROWSE) Informe Sim ou Não* |
| **Opções** | *(X3\_CBOX)* |
| **When** | *(X3\_WHEN)* |
| **Relação** | *(X3\_RELACAO)* |
| **Val. Sistema** | *(X3\_VALID)* |
| **Help** | *Descreva o conteúdo informado para Help de Campo no ATUSX* |

**Importante:**

O tamanho dos campos que possuem grupo pode variar conforme ambiente em uso.

5.  *Criação ou Alteração* de **Consulta Padrão** no arquivo **SXB – Consulta Padrão**:

* Pesquisa *B05PLS*:

|  |  |
| --- | --- |
| **Alias** | *(XB\_ALIAS)* |
| **Tipo** | *(XB\_TIPO)* |
| **Sequência** | *(XB\_SEQ)* |
| **Coluna** | *(XB\_COLUNA)* |
| **Descrição** | *(XB\_DESCRI)* |
| **Contém** | *(XB\_CONTEM)* |

6. *Criação ou Alteração* de **Índices** no arquivo **SIX – Índices**:

|  |  |
| --- | --- |
| **Índice** | *AA1* |
| **Ordem** | *6* |
| **Chave** | *AA1\_FILIAL+AA1\_CODVEN* |
| **Descrição** | *Cod. Vendedor* |
| **Proprietário** | *S* |

7. *Criação ou Alteração* de **Parâmetros** no arquivo **SX6 – Parâmetros**:

|  |  |
| --- | --- |
| **Nome da Variável** | *(X6\_VAR)* |
| **Tipo** | *(X6\_TIPO)* |
| **Descrição** | *(X6\_DESCRIC + X6\_DESC1 + X6\_DESC2)* |
| **Valor Padrão** | *(X6\_CONTEUD)* |

8. *Criação ou Alteração* (mantenha somente a instrução correspondente) de **Gatilhos** no arquivo **SX7 – Gatilhos**:

* Tabela ***BD5 – Contas Médicas***:

|  |  |
| --- | --- |
| **Campo** | *Informe o conteúdo do (X7\_CAMPO)* |
| **Sequência** | *Informe o conteúdo do (X7\_SEQUENC)* |
| **Campo Domínio** | *Informe o conteúdo do (X7\_CDOMIN)* |
| **Tipo** | *Informe o conteúdo do (X7\_TIPO)* |
| **Regra** | *Informe o conteúdo do (X7\_REGRA)* |
| **Posiciona?** | *Informe o conteúdo do (X7\_SEEK)* |
| **Chave** | *Informe o conteúdo do (X7\_CHAVE)* |
| **Condição** | *Informe o conteúdo do (X7\_CONDIC)* |
| **Proprietário** | *Informe o conteúdo do (X7\_PROPRI)* |

## Procedimento para Configuração

*(Estes procedimentos devem ser feitos quando for necessário configurar parâmetros e/ou  rotinas no menu).*

**CONFIGURAÇÃO DE PARÂMETROS**

1. No **Configurador (SIGACFG)**, acesse **Ambientes/Cadastros/Parâmetros (CFGX017)**. Crie/configure *(mantenha somente a instrução correspondente)* o(s) parâmetro(s) a seguir:  
   *(É necessário criar uma tabela para cada parâmetro descrito no item **Parâmetro(s)**, da tabela **Características do Requisito**)*

|  |  |
| --- | --- |
| Itens/Pastas | Descrição |
| **Nome:** |  |
| **Tipo:** | *Informe o Tipo do parâmetro* |
| **Cont. Por.:** | *Informe o Conteúdo padrão* |
| **Descrição:** |  |

**CONFIGURAÇÃO DE MENUS**

2.  No **Configurador (SIGACFG),**acesse **Ambientes/Cadastro/Menu (CFGX013)**. Informe a nova opção de menu do *informe **o nome do módulo***, conforme instruções a seguir:

|  |  |
| --- | --- |
| **Menu** | *Informe o Menu em que estará localizada a rotina* |
| **Submenu** | *Informe o Submenu em que estará localizada a rotina* |
| **Nome da Rotina** | *Informe o Título da rotina* |
| **Programa** | *Informe o Fonte da rotina* |
| **Módulo** | *Informe o Nome do(s) produto(s) a ser utilizado ou “Todos”* |
| **Tipo** | *Informe a Função* |

## Procedimento para Utilização

* *Descreva os procedimentos, passo a passo (caso de uso), que serão realizados pelos usuários para que a melhoria seja visualizada identificando as seguintes informações:*
* *Localização da rotina no menu;*
* *Localização dos novos campos e/ou perguntas e respectivas pastas de cadastro que são visualizadas pelo usuário;*
* *Caso seja necessário ter algum cadastro feito previamente, faça uma observação.*

**Exemplo:**

       1.            No Plano de Saúde (SIGAPLS), acesse Atualizações / Produto Saúde / Produto Saúde (PLSA800).

O sistema apresenta a janela de produtos cadastrados.

       2.            Posicione o cursor em um produto e clique em Alterar.

       3.            Na pasta Cobertura/Carências selecione a subpasta Tipo de Prestador.

       4.            Dê duplo clique no campo TP Prestador (BCW\_TIPPRE).

O sistema apresenta a janela Tipo de Prestador – Coparticipação – Alterar.

       5.            Informe os dados conforme orientação do help de campo e observe o preenchimento do novo campo:

                      Som. p/Compra (BCW\_SOMCOM): selecione Sim para indicar se a coparticipação cadastrada será válida somente para efeito de compra de procedimentos ou Não, caso contrário.

       6.            Confira os dados e confirme.

## Vídeo

* *Vídeo hospedado no youtube e inserido no template por meio da macro **Widget Connector**.*

*\*\* Canal do youtube e software de vídeoem definição.*

|  |  |
| --- | --- |
| **Título do Vídeo:** | *Disponibilizado pelo Marketing.* |
| **Introdução:** | *Disponibilizado pelo Marketing.* |
| **Passo a Passo:** | *Capturar diretamente do sistema.* |
| **Finalização:** | *Disponibilizado pelo Marketing.* |

## Ponto de Entrada

|  |  |
| --- | --- |
| **Descrição:** | *Informe o Menu em que estará localizada a rotina* |
| **Localização:** | *Informe o Submenu em que estará localizada a rotina* |
| **Eventos:** | *Informe o Título da rotina* |
| **Programa Fonte:** | *Informe o Fonte da rotina* |
| **Função:** | *Informe o Nome do(s) produto(s) a ser utilizado ou “Todos”* |
| **Retorno:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | |  |  |  |  | |  |  |  |  | |  |  |  |  | |

Exemplo:

#Include '[Protheus.ch](http://Protheus.ch)'

User Function CN120ALT()

Local aCab:= PARAMIXB[1]

Local cTipo:= PARAMIXB[2]

If cTipo == '1'

    aCab[4][2]:= 'NF' //Validações do usuário

EndIf

Return aCab

divs
