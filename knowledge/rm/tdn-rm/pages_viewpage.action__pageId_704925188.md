---
content_hash: ece6241f2bd100646867812a2bfa64d77829c568f0da7449dad3d59d6b6b5816
fetched_at: '2026-06-29T00:11:22.457639+00:00'
page_id: '704925188'
product: rm
source: tdn-rm
title: DT Registro Online padrão AutBank
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=704925188
version: 14
---

# Registro Online padrão AutBank

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Backoffice BH* |
| **Módulo:** | **TOTVS Gestão Financeira** |
| **Requisito/S****tory/Issue:** | FINANCEIRO01-21261; DRMGR-1084 |

## Descrição

Esta implementação tem como objetivo preparar o TOTVS Gestão Financeira para utilizar o serviço de registro online de cobrança registrada para os bancos que utilizam o padrão da AutBank.

Bancos homologados para esse padrão: "Banco Crefisa" e "Banco b.Uni".

**Obs.:** Recurso disponível a partir da versão 12.1.2209 Banco Crefisa e 12.1.2302 Banco b.Uni.

## Procedimento para Configuração

No TOTVS Gestão Financeira, menu *Movimentações Bancárias | Controle Bancário | Convênio,* devem ser feitas as configurações do convênio para o registro de cobrança online:

* **Permite registro online*:*** Define se o convênio permite utilizar o registro de cobrança online.
* **Integração com os serviços da AutBank:**Define que o banco utiliza o padrão da AutBank para o registro online de boletos.
* **Ambiente**: Define o ambiente que será feito o registro de cobrança no banco.
* **URL do serviço de registro de cobrança**: Deve ser informada a URL do serviço de registro de cobrança disponibilizada pelo banco.
* **URL de homologação do serviço de registro de cobrança**: Deve ser informada a URL de homologação do serviço de registro de cobrança disponibilizada pelo banco. Veja mais em...
* **Usuário**: Usuário de acesso ao sistema autorizador fornecido pelo banco.
* **Senha**: Senha de acesso ao sistema autorizador fornecido pelo banco.

Pode ser utilizado o [Cadastro de Layout do Registro Online](http://tdn.totvs.com/pages/viewpage.action?pageId=311625508), para enviar dados de forma flexível para o registro online dos boletos para o banco. Para isso deve ser feito o [Cadastro de associação de fórmulas e campos do registro online](http://tdn.totvs.com/pages/viewpage.action?pageId=307835775) no cadastro do convênio utilizado para o registro online.

O cadastro do layout do registro online deve ser feita de acordo com o manual de cobrança online do banco, da seguinte maneira:

* Exemplos:

        numContaHeader  
        campoLivre  
        mensagem1  
        mensagem2  
        mensagem3  
        mensagem4  
        mensagem5  
        codDesconto1  
        vlrDesconto1  
        txDesconto1  
        dataDesconto1          
        codDesconto2  
        vlrDesconto2  
        txDesconto2  
        dataDesconto2          
        codDesconto3  
        vlrDesconto3  
        txDesconto3  
        dataDesconto3          
        codMulta  
        dataMulta  
        txMulta  
        vlrMulta          
        codMora  
        dataMora  
        txMora  
        vlrMora          
        possuiAgenda  
        tipoAgendamento  
        criterioDias  
        numDiasAgenda          
        codIndice          
        indPagtoParcial  
        qtdPagtosParciais          
        tipoVlrPercMinimo  
        vlrPercMinimo  
        tipoVlrPercMaximo  
        vlrPercMaximo          
        tipoAutRecDivergente          
        codColigadaContaCreditar  
        codAgenciaContaCreditar  
        numContaCreditar  
  
        **codColigada** (Campo obrigatório para utilização do serviço de alteração de Data de Vencimento - **Não é a coligada do RM**)  
        **cobrarTarifa** (Campo obrigatório para utilização do serviço de alteração de Data de Vencimento)

**Importante:**

* Para os campos de valores ou percentual deve seguir o formato de acordo com o manual disponibilizado pelo banco. Ao definir um valor fixo ou formula deve ser retornado um string com o separador decimal '.' (ponto).   
  Exemplo:   
  2.49 (com duas casas decimais)
* Para campos destinados a data deve ser utilizado o separador '/' (barra).  
  18/01/2023 (data no formato DD/MM/YYYY)
