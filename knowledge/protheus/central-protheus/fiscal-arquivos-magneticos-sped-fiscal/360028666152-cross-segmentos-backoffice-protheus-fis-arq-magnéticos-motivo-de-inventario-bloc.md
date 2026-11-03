---
article_id: 360028666152
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 6818873349863207f3a6cd2ead90bb6dfa0a7dc4094dd53cfc2e753ba6e4d160
fetched_at: '2026-06-28T22:42:00.960934+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Motivo de Inventario
  Bloco H SPED Fiscal
type: support-article
updated_at: '2024-06-19T18:14:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028666152-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Motivo-de-Inventario-Bloco-H-SPED-Fiscal
---

**Dúvida**Disponível na rotina **Motivo de Inventario (FISA120)** para cadastro de período, data de fechamento e motivo de inventario para bloco H do arquivo magnético SPED fiscal.  
  
 **Ambiente**  
Protheus – Livros – A partir da versão 11.80  
  
**Solução**Disponível na rotina Motivo de Inventario (FISA120) para cadastro de período, data de fechamento e motivo de inventario para bloco H do arquivo magnético SPED fiscal.

Registro H005 deve ser apresentado para discriminar os valores totais dos itens/produtos do inventário realizado em 31 de dezembro de cada exercício, ou nas demais datas estabelecidas pela legislação fiscal ou comercial .

Neste sentido, em regra geral, o arquivo com entrega no mês de fevereiro com a posição do inventário em 31 de dezembro de cada exercício irá conter o código de motivo do inventário 01 (No final no período).

Caso a empresa tenha alguma mudança na forma de tributação do ICMS ou determinação do fisco para o mesmo período que será entregue o inventario, será necessário processar mais de uma data de fechamento de estoque, apresentado dois ou mais inventários com sues respectivos códigos de motivo de inventário, Exemplo: (01 – No final no período e 02 – Na mudança de forma de tributação da mercadoria (ICMS).

Abaixo todos os motivos previstos para geração do Registro H005, conforme Guia Prático EFD-ICMS/IPI – Versão 2.0.18:

Informe o motivo do Inventário:   
01 – No final no período;   
02 – Na mudança de forma de tributação da mercadoria (ICMS);   
03 – Na solicitação da baixa cadastral, paralisação temporária e outras situações;   
04 – Na alteração de regime de pagamento – condição do contribuinte;   
05 – Por determinação dos fiscos.

No momento de gerar SPED FISCAL sera necessário alterar perguntas:

Gera Inventário - Selecione se deseja gerar os registros de inventário (bloco H).

Motivo do Inventário - Selecione qual o motivo do inventário:

01 – No final no período;

02 – Na mudança de forma de tributação da mercadoria (ICMS);

03 – Na solicitação da baixa cadastral, paralisação temporária e outras situações;

04 – Na alteração de regime de pagamento – Condição do contribuinte;

05 – Por determinação dos fiscos.

Caso existe a necessidade de gerar mais de um motivo de inventario para mesmo período, será necessário que seja utilizara rotina de motivo de inventario (FISA120) para cadastrar os demais motivos e datas de fechamento de estoque.

Procedimentos para Implementação  
Para que os próximos campos e parâmetros necessários ao processamento sejam criados automaticamente, foi disponibilizado o compatibilizador UPDFIS.

Procedimentos para Implementação  
Para que os próximos campos e parâmetros necessários ao processamento sejam criados automaticamente, foi disponibilizado o compatibilizador UPDFIS.

(Apenas para Microsiga Protheus, versões anteriores à versão 12)

Antes de executar o compatibilizador UPDFIS é imprescindível:

Realizar o backup da base de dados do produto que será executado o compatibilizador (diretório \PROTHEUS11\_DATA\DATA) e dos dicionários de dados SXs (diretório \PROTHEUS11\_DATA\SYSTEM).  
Os diretórios acima mencionados correspondem à instalação padrão do Protheus, portanto, devem ser alterados conforme o produto instalado na empresa.  
Essa rotina deve ser executada em modo exclusivo, ou seja, nenhum usuário deve estar utilizando o sistema.  
Se os dicionários de dados possuírem índices personalizados (criados pelo usuário), antes de executar o compatibilizador, certifique-se de que estão identificados pelo nickname. Caso o compatibilizador necessite criar índices, irá adicioná-los a partir da ordem original instalada pelo Protheus, o que poderá sobrescrever índices personalizados, caso não estejam identificados pelo nickname.  
O compatibilizador deve ser executado com a Integridade Referencial desativada\*.

**Atenção**

**O procedimento a seguir deve ser realizado por um profissional qualificado como Administrador de Banco de Dados (DBA) ou equivalente!**

**A ativação indevida da Integridade Referencial pode alterar drasticamente o relacionamento entre tabelas no banco de dados. Portanto, antes de utilizá-la, observe atentamente os procedimentos a seguir:**

**1- No Configurador (SIGACFG), veja se a empresa utiliza Integridade Referencial, selecionando a opção Integridade/Verificação(APCFG60A).**

**2- SSe não há Integridade Referencial ativa, são relacionadas em uma nova janela todas as empresas e filiais cadastradas para o sistema e nenhuma delas estará selecionada. Neste caso, E SOMENTE NESTE, não é necessário qualquer outro procedimento de ativação ou desativação de integridade, basta finalizar a verificação e aplicar normalmente o compatibilizador, conforme instruções.**

**3-Se há Integridade Referencial ativa em todas as empresas e filiais, é exibida uma mensagem na janela Verificação de relacionamento entre tabelas. Confirme a mensagem para que a verificação seja concluída, ou;**

**4-Se há Integridade Referencial ativa em uma ou mais empresas, que não na sua totalidade, são relacionadas em uma nova janela todas as empresas e filiais cadastradas para o sistema e, somente, a(s) que possui(em) integridade está(arão) selecionada(s). Anote qual(is) empresa(s) e/ou filial(is) possui(em) a integridade ativada e reserve esta anotação para posterior consulta na reativação (ou ainda, contate nosso Help Desk Framework para informações quanto a um arquivo que contém essa informação).**

**5-Nestes casos descritos nos itens “iii” ou “iv”, E SOMENTE NESTES CASOS, é necessário desativar tal integridade, selecionando a opção Integridade/ Desativar (APCFG60D).**

**6-Quando desativada a Integridade Referencial, execute o compatibilizador, conforme instruções.**

**7-Aplicado o compatibilizador, a Integridade Referencial deve ser reativada, SE E SOMENTE SE tiver sido desativada, através da opção Integridade/Ativar (APCFG60). Para isso, tenha em mãos as informações da(s) empresa(s) e/ou filial(is) que possuía(m) ativação da integridade, selecione-a(s) novamente e confirme a ativação.**

1-Em Microsiga Protheus TOTVS Smart Client, digite U\_UPDSIGAFIS no campo Programa Inicial.   
Clique em OK para continuar.

2- Após a confirmação é exibida uma tela para a seleção da empresa em que o dicionário de dados será modificado ou é apresentada a janela para seleção do compatibilizador. Selecione o programa U\_UPDSIGAFIS.

3-Ao confirmar é exibida uma mensagem de advertência sobre o backup e a necessidade de sua execução em modo exclusivo.

A-Clique em Processar para iniciar o processamento. O primeiro passo da execução é a preparação dos arquivos.

É apresentada uma mensagem explicativa na tela.

B-Em seguida, é exibida a janela Atualização concluída com o histórico (log) de todas as atualizações processadas. Nesse log de atualização são apresentados somente os campos atualizados pelo programa. O compatibilizador cria os campos que ainda não existem no dicionário de dados.

C-Clique em Gravar para salvar o histórico (log) apresentado.

D-Clique em OK para encerrar o processamento.  
  
**Configurações do Menu**

* No **Configurador (SIGACFG)** acesse **Ambiente/Cadastros/Menus** e inclua no *menu* do módulo **Livros Fiscais (SIGAFIS)** a opção para execução do **Cadastro**, conforme especificação a seguir:

**Menu**: Atualizações  
**Submenu**: SPED  
**Nome da Rotina**: Motivo de Inventario  
**Programa**: FISA120  
**Módulo**: 09  
**Tipo**: 01  
**Tabelas**: F0Q  
  
**Atualizações do compatibilizador:  
  
SIX - Índices  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029808052)****SX3 – Campos****:  
  
Tabela F0Q - Motivo de Inventário:  
  
Campo:**F0Q\_FILIAL **Tipo:**Caracter **Tamanho:** 2  **Decimal**: 0  
**Formato**: @!  
**Título**: Filial   
**Descrição**: Filial do Sistema  
**Usado**: Não  
**Obrigatório**: Não  
**Browse**: Sim  
**Contexto**: Real  
**Propriedade**: Alterar   
**Grupo de Campos**: 033 - Tamanho da Filial  
  
**Campo**: F0Q\_DTFECH  
**Tipo**: Data   
**Tamanho**: 8  
**Decimal**: 0  
**Formato**: 99/99/9999  
**Título**: Dt. Fecham.  
**Descrição**: Dt. Fechamento de estoque  
**Usado**: Sim  
**Obrigatório**: Sim  
**Browse**: Sim  
**Contexto**: Real  
**Propriedade**: Alterar   
  
**Campo**: F0Q\_CODIGO  
**Tipo**: Caracter  
**Tamanho**: 15  
**Decimal**: 0  
**Formato**: @!  
**Título**: Código  
**Descrição**: Código do Produto  
**Usado:** Sim  
**Obrigatório**: Sim  
**Browse**: Sim  
**Val. Sistema**: ExistCpo("SB1")  
**Contexto**: Real  
**Propriedade**: Alterar  
**Cons. Padrão**: SB1  
  
**Campo**: F0Q\_MOTINV  
**Tipo**: Caracter  
**Tamanho**: 2  
**Formato**: @!  
**Título**: Mot Inv  
**Descrição**: Motivo do inventário  
**Usado**: Sim  
**Obrigatório**: Sim  
**Browse**: Sim  
**Opções**: 02=Mudança de tributação; 03=Baixa cadastral; 04=Alteração regime de pagamento; 05=Determinação dos fiscos  
**Contexto**: Real  
**Propriedade**: Alterar  
**Help**: Informe o motivo do Inventário  
  
**Campo**: F0Q\_DESPRO  
**Tipo**: Caracter  
**Tamanho**: 50  
**Decimal**: 0  
**Formato**: @!  
**Título**: Des. Produto  
**Descrição**: Descrição Produto  
**Usado**: Sim  
**Obrigatório**: Não  
**Browse**: Sim  
**Contexto**: Virtual  
**Propriedade**: Visualizar   
**Relação**: Iif( INCLUI , "" , Posicione ( "SB1" , 1 , xFilial("SB1") + F0Q\_CODIGO , "B1\_DESC" ) )  
  
**Campo**: F0Q\_PERIOD  
**Tipo**: Caracter  
**Tamanho**: 6  
**Formato**: @R 99/9999  
**Título**: Per.Apuração  
**Descrição**: Período de Apuração  
**Usado**: Sim  
**Obrigatório**: Sim  
**Browse**: Sim  
**Help**: Período de processamento do EFD SPED fiscal. Mês/Ano  
  
**Campo**: F0Q\_ID  
**Tipo**: Caracter  
**Tamanho**: 36  
**Formato**: @!  
**Título**: Chave  
**Descrição**: Chave  
**Usado**: Não  
**Reservado**: Sim  
**Visualização**: Sim  
**Browse**: Sim  
**Relação**: FWUUID("FISA120")  
**Help:**Período de processamento do EFD SPED fiscal. Mês/Ano

**Procedimento para Utilização**

1. No módulo Livros Fiscais (SIGAFIS), acesse Atualizações/ SPED/ Motivo Inventário (fisa120) para inserir o período, data de fechamento e motivo inventario.

Campo de período, deve ser preenchido conforme período em que fechamento de estoque cadastrado sera demonstrado no SPED FISCAL.

Exemplo:

SPED FISCAL sera processado para período de fevereiro de 2017.

Foram cadastrados dez datas de fechamentos e motivos de inventario na rotina de motivo de inventario com campo Per.Apuração (F0Q\_PERIOD) preenchido 02/2017.

Quando rotina SPED FISCAL for executada sera processado todos as dez datas de fechamento cadastradas, e impresso registros H005 para cada data de fechamento de estoque.

Importante:

Quando for informado produto nesta rotina não sera necessário alterar cadastro de complemento de produto, campo B5\_ALTTRIB para informar que produto sofreu alteração, desta forma somente para data de fechamento e período informado neste período produto sera considerado como alteração. Caso produto sofra alteração em outros períodos sera necessário cadastrar na rotina de motivo de inventario.

Obs. Quando o motivo de inventário for igual 3, 4, ou 5, não será validado o produto, considerando somente o período de fechamento do estoque.

**Tabelas Utilizadas:**F0Q – Motivo de Inventário **Rotinas Envolvidas:**SPEDFISCAL - **EFD SPED fisca  
FISA120 - Motivo Inventário**

**Link contendo os procedimentos acima:**

http://tdn.totvs.com/display/public/PROT/FIS0075\_Motivo\_de\_Inventario\_Bloco\_H\_SPED\_fiscal
