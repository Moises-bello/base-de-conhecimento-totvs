---
content_hash: 5a7fecaefe6cfff1256b5e69ec549229f57cfc563e8a6855763080a22cbc1ca2
fetched_at: '2026-06-29T00:08:40.076718+00:00'
page_id: '286206090'
product: rm
source: tdn-rm
title: DT Dados do código de barras da pulseira
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286206090
version: 103
---

# #PEPXRM :: Dados do código de barras da pulseira / 5 certos na checagem - Revisão CHECKS Linha RM

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Informe a rotina.* | *Informe o nome técnico da rotina.* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Informe a(s) rotina(s) envolvidas*.* | *Informe o nome técnico da(s) rotina(s) envolvidas.* | |  |  | |
| **Cadastros Iniciais:** | *Relacione os cadastros necessários que precisam ser preenchidos antes da utilização desse requisito.* |
| **Parâmetro(s):** | *Informe os parâmetros utilizados.* |
| **Ponto de Entrada:** | *Informe o ponto de entrada relacionado (link).* |
| **Tickets relacionados** | *Informe o(s) chamado(s) relacionado(s).* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | *Informe o requisito relacionado (Issue).* |
| **País(es):** | *Informe o(s) Pais(es).* |
| **Banco(s) de Dados:** | *Informe o(s) Banco(s) de Dados utilizado(s).* |
| **Tabelas Utilizadas:** | *Informe as tabelas utilizadas.* |
| **Sistema(s) Operacional(is):** | *Informe o(s) sistema(s) operacional(is) utilizados.* |

## Descrição

Escreva aqui a descrição da nova implementação ou melhoria.

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

divs
