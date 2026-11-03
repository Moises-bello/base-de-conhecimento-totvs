---
article_id: 360029358971
category: NFe - Nota Fiscal Eletrônica
content_hash: 1fef46caa2c173ec7134129bf8fc24d1831320012b4af28fb844cf8aa8422012
fetched_at: '2026-06-28T22:40:06.894182+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NF-e - AUTONFE Transmissão,
  Monitoramento e Cancelamento Automáticos
type: support-article
updated_at: '2024-07-22T12:08:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029358971-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NF-e-AUTONFE-Transmiss%C3%A3o-Monitoramento-e-Cancelamento-Autom%C3%A1ticos
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23976386151191)*** Tempo aproximado para leitura:**00:04:00 min  
  
Dúvida**Como configurar **Transmissão**, **Monitoramento** e **Cancelamento Automáticos**?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - A partir da Versão 12.1.27  
  
**Solução**

É um facilitador que permite através da sua configuração no *Schedule*, realizar a **Transmissão**, **Monitoramento** e **Cancelamento** da **NF-e** de forma automática.

## *Schedule*

Configuração do *Schedule:*

1. Se habilitado, desabilite o antigo *Job* nfe no arquivo .ini do server do **Protheus**;  
2. No **Configurador - SIGACFG** acesse **Ambientes** > ***Schedule*** > ***Schedule;***  
3. Cadastre os agentes para o processamento das rotinas;  
4. Cadastre as rotinas que fazem o processamento de **NF-e**, informando em parâmetros a série   
considerada para o processamento.  
  
Abaixo estão as rotinas responsáveis por cada processamento:  
Rotina de **Transmissão**: **AUTONFETRANS**  
Rotina de **Monitoramento**: **AUTONFEMON**  
Rotina de **Cancelamento**: **AUTONFECANC**  
5. Para todas as rotinas informe a série a ser processada;  
6. Após conclusão e a ativação do agendamento, a rotina dará início ao processamento dos documentos;  
7. Se necessário gravar o log de processamento das rotinas, efetue a seguinte configuração no arquivo **appserver.Ini** do**Protheus: *[Environment]*AUTONFE\_DEBUG=1.**

Criando um Agent:  
1-Acessar **Configurador - SIGACFG**;  
2-**Configurador** > **Ambiente** > ***Schedule**;*  
3-Em **Agendamentos** realizar um cadastro;  
4-No campo **Rotina** informar a rotina que deseja configurar;  
5-Vá em **Parâmetros** e informe a série.

**Agent: Os agents podem estar localizados em diferentes servidores, possibilitando a distribuição da carga de execuções.**

Criando um **Agendamento**:  
1-Acessar **Configurador - SIGACFG**;  
2-**Configurador** > **Ambiente** > ***Schedule**;*3-Em **Agendamentos** realizar um cadastro;  
4-No campo **Rotina** informar a rotina que deseja configurar;  
5-Vá em **Parâmetros** e informe a série **(composta por 3 digitos (ex "5  " (5+Espaço+Espaço))**

Procedimento para **Utilização**

**Transmissão** e **Monitoramento**:  
1. Fature os **Pedido de Venda** e após concluir o faturamento, as notas são transmitidas e monitoradas automaticamente.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030596852)

**Cancelamento**:  
1. Exclua as notas desejadas. Feito isto será transmitido e monitorado automaticamente o cancelamento/inutilização;  
2. Ao optar pelo processo automático de cancelamento, o **TSS** adotará a justificativa padrão <xJust>**Cancelamento** de nota fiscal eletrônica por emissão indevida</xJust>.

**Cancelamento** processo padrão.
