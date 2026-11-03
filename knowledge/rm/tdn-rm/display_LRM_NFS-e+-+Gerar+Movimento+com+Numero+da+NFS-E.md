---
content_hash: bed1f033b35eca83b315111bcbd4b998d8ae1f7ebf3878b40840e4c941008da4
fetched_at: '2026-06-29T00:11:11.457731+00:00'
page_id: '64652703'
product: rm
source: tdn-rm
title: NFS-e - Gerar Movimento com Numero da NFS-E
type: documentation
url: https://tdn.totvs.com/display/LRM/NFS-e+-+Gerar+Movimento+com+Numero+da+NFS-E
version: 4
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | NFS-e                        **Versão:***a partir 11.40* |
| **Processo** | **:** | Gerar Movimento com Numero da NFS-E |
| **Subprocesso** | **:** | Gerar Movimento com Numero da NFS-E |
| **Data da publicação** | **:** | 04/07/2013 |

**Introdução:**

Este documento tem o objetivo de mostrar os passos para configuração de um movimento para emissão de NFS-e, onde os movimentos autorizados pela prefeitura ficaram com o numero da NFS-e gerada no site da prefeitura. Assim facilitando o rastreamento das NFS-e e as integrações com Fiscal, Contábil, Financeiro etc.

Para utilizar esta funcionalidade do sistema é necessário a utilização de um movimento de pedido (2.1.xx) e um movimento de faturamento (2.2.xx), onde o movimento de pedido enviará a NFS-e para a prefeitura, e na consulta autorização será criado automaticamente um movimento com o numero da NFS-e que é retornado pela prefeitura.

**Parametrização do processo**

Atualize a biblioteca para a versão 11.40.35 ou superior

Acesse o seguinte menu: Opções | Parâmetros | RM Nucleus | Outras Movimentações | escolha o movimento a ser parametrizado e clique em parametrizar.

**Observação: Estes passos deverão ser executados para os dois tipos de movimento, 2.1.xx e 2.2.xx.**

**1. Configuração dos movimentos**

**Etapa Mov – Identificação:**

Nesta Etapa Selecione a Serie para emissão de NF-e, maiores informações sobre o [cadastro da serie](http://totvsconnect.blogspot.com.br/2012/04/como-fazer-verificar-cadastros-para.html).

**Etapa Mov – Emitente/Destinatário 1/2:**

Nesta Etapa o Emitente deverá ser “Empresa” e o destinatário “Cliente” ou “Fornecedor”

**Mov – Datas 1/2:**

Nesta etapa deverá ser selecionado “Edita” no campo “Edição da Data de Emissão”.

**Etapa Mov – Datas 2/2:**

Nesta etapa deverá ser selecionado “Edita” no campo “Edição da Data de Saída”.

**Etapa Mov – Campos Livres 2/2:**

Nesta Etapa pode ser selecionado a Edição do Histórico para Edita, este campo ira compor a TAG Discriminação do XML da NFS-e com as informações preenchidas no movimento.

**Etapa Item – Campos Livres 2/2:**

Nesta Etapa pode ser selecionado a Editar Histórico para Edita, este campo ira compor a TAG Discriminação do XML da NFS-e com as informações preenchidas no movimento.

**Etapa Fis - Tributação - Item:**

Nesta etapa deve ser incluído o ISS para o item de movimento, definindo também o seu tipo de recolhimento.

**Etapa Compra/Venda – Característica (apenas para o movimento 2.1.xx)**

Nesta Etapa marque o CheckBox “Gera Movimento de Venda”, preenchendo no campo “Movimento Gerado (Default)” com o código do tipo de movimento em que será gerado o movimento faturado (2.2.xx)

**Etapa Fis – Escrituração 1/2(Apenas para o movimento 2.2.xx):**

Nesta Etapa deverá ser marcada a opção “Gerar Escrituração” e no campo “Tipo Documento Escrituração” deverá ser selecionado o tipo de documento cadastrado para emissão de NFS-e, maiores informações sobre o[cadastro do tipo de documento](http://totvsconnect.blogspot.com.br/2012/04/como-fazer-verificar-cadastros-para.html).

**Etapa Fis - NF-e:**

Nesta Etapa deverá ser selecionado o Tipo de Envio da NFS-e Municipal (modelo Nacional), Manual ou Automático.

Avance até a ultima etapa salve os parâmetros do tipo de movimento.

Agora refaça os passos de configuração acima utilizando o movimento 2.2.xx e incluindo a etapa abaixo, para correta configuração da NFS-e.

**Etapa Mov – Outros Dados (Apenas para o movimento 2.2.xx)**

Nesta etapa desmarque a opção “Usar Copia de Movimentos por Referência”, e selecione a opção “Não Utilizar” para o campo 2º Número Sequencial.

**2. Gerando a NFS-e**

**Gerando Movimento a ser transmitido para prefeitura (RPS)**

O movimento deverá ser criado normalmente no tipo de movimento 2.1.xx e este será enviado a prefeitura. Ao finalizar a criação do movimento, o mesmo deverá estar com STATUS “A Faturar”:

**Transmitindo a NFS-E e Gerando Movimento Faturado**

Para realizar a transmissão da NFS-E, acesse o menu |UTILITARIOS | SPED | NFE-MUNICIPAL | SELECIONE O FILTRO | PROCESSOS | ENVIAR NFS-E | preenchendo devidamente todos os campos para transmissão da nota e execute o processo, após envio a NFS-e ficará como “Pendente”.

Aguarde alguns minutos e execute o processo “Consulta Autorização/Cancelamento”.

Quando a NFS-e for autorizada com sucesso será criado automaticamente um movimento no tipo de movimento 2.2.xx com o numero da NFS-e retornado pela prefeitura.

Será apresentado o log de geração do movimento juntamente com o log da consulta de autorização da NFS-E, por exemplo:

*As NFS-e foram consultadas com sucesso. Total de NFS-e consultadas: 1.*

*NFS-e Autorizada com sucesso.*

*Filial: 2, Identificador do Movimento: 2258, Número da NFS-e: 15*

-----------------------------------------------------------------

*Log do movimento gerado automaticamente: Movimento 15 gerado com sucesso*

*Total de Erros: 0*

*Total de Movimentos Gerados: 1*

-----------------------------------------------------------------

OBS: Caso o lançamento não seja gerado ou gerado com o STATUS diferente de Faturado, será apresentada a mensagem de erro com o motivo da não criação ou o não faturamento do mesmo no log da consulta Autorização/Cancelamento da NFS-E. Para esta situação, existe o menu chamado “Gerar Movimento Com Numero da Prefeitura” no menu | UTILITARIOS | SPED | NFE-MUNICIPAL | PROCESSOS | que executa o processo da criação do movimento faturado novamente, basta corrigir o erro e executar este processo.

**Para maiores informações:**

**[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)**

**COMUNIDADE **R**[@](https://totvs.byyou.com/?space=rnfe)Nfe**

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções: 2 – (Software), 2 – (Suporte Técnico), 3 - (RM), 3 - (Fiscal), 3 - (Nota Fiscal Eletrônica);
