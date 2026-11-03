---
article_id: 35700183239319
category: Contabilidade Gerencial - Reprocessamento
content_hash: ce383cfa51316fc7ec0e4e8cf020c2aef39019fa2ef785a76590ee74093d046f
fetched_at: '2026-06-28T22:40:41.971998+00:00'
product: protheus
section_id: 1500001548742
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA102 - Ao tentar
  Alterar/Excluir um lançamento contábil é apresentado Help CTBFILA
type: support-article
updated_at: '2025-10-17T17:42:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35700183239319-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-Ao-tentar-Alterar-Excluir-um-lan%C3%A7amento-cont%C3%A1bil-%C3%A9-apresentado-Help-CTBFILA
---

**Dúvida**  
Alteração ou Exclusão do Lançamento Contábil via rotina CTBA102 apresenta help CTBFILA  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice Linha Protheus - Contabilidade Gerencial - Todas Versões

**Ocorrência apresentada: Help CTBFILA**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35700183221527)

**Solução:**

Este help ocorre devido ao lançamento contábil ainda não ter sido processado na fila de atualização de saldos.

**Para correção deve:**

#### **1 - Verificar através da rotina CTBA961 Monitor de Saldo On-line, se a fila esta sendo processada:**

[Monitor de Saldos On-line (SIGACTB)](https://tdn.totvs.com/pages/releaseview.action?pageId=852898157)

Caso a fila esta sendo processada, basta aguardar que o registro será processado e liberado para movimentação.

#### **2 - Se identificar que a fila não esta sendo processada verificar os pontos abaixo:**

* Verificar se o parâmetro MV\_CTBJOB esta igual á 1
* Verificar o agendamento da rotina via Schedule esta configurado e Ativo conforme abaixo:
* Acessar o Configurador (SIGACFG) -> Ambiente -> Schedule
* Ao ser aberta a tela do gerenciador de Schedule, verifiquei se o Smart Schedule ou Scheduler estão ativos:

  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/35700183222423)

  Verifique se o agendamento está habilitado:

  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/35700178964247)

  **Ponto importante: O cadastro do agendamento não precisa ser realizado para todas as empresas e filiais basta apenas configurar para uma empresa e filial que os saldos serão atualizados para todos, conforme abaixo:**

  **![](https://centraldeatendimento.totvs.com/hc/article_attachments/35700178965527)**
* **Verificar se as procedures de Atualização de Saldo estão instaladas e Atualizadas**

  **Acessar o Configurador (SIGACFG) -**> base de dados -> Stored Procedure

  Ao ser aberta a tela do gerenciador de procedure, selecione a empresa que esta utilizando no campo superior esquerdo, e verifique o Status das procedures 01, 06 e 23:  
    
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/35700178970647)

  + Caso esteja como **desatualizada ou incompatível**, deve realizar a atualização conforme abaixo:

    Aplique o pacote de atualização dos fontes, que acionam as procedures:

    [Pacotes de Atualização - Contabilidade Gerencial - Linha Microsiga Protheus - TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=334342777)

    Após aplicação do pacote realizar o processo de Atualização das procedures:

    Na tela de procedure:

    1° Marque grupo de empresa utilizado;

    2° Marque a procedure que será atualizada;

    3° Selecione a caixinha com a Seta Verde;  
      
    ![](https://centraldeatendimento.totvs.com/hc/article_attachments/35700178971031)

    Ao finalizar a atualização será apresentada tela que a procedure foi instalada com Sucesso:

    ![](https://centraldeatendimento.totvs.com/hc/article_attachments/35700183226775)

    E o Status será apresentado como atualizado:

    ![](https://centraldeatendimento.totvs.com/hc/article_attachments/35700183227671)

* **Após verificação dos passos acima, caso estejam todos corretos, gerar o console.log e encaminhar para o suporte para análise, conforme abaixo:**  
    
  Pare todos os agendamentos menos o da CTBA193  
    
  Interrompa temporariamente os serviços: dbaccess e do appserver  
  Antes de reiniciar os serviços, renomeie os arquivos de log abaixo:  
  \dbaccess\dbaccess.log  
  \dbaccess\dbconsole.log  
  \appserver\console.log  
    
  Adicione também as chaves no ambiente para validação dos logs:  
    
  Na seção [ambiente] insira:  
  FWTRACELOG=1  
  Na seção [GENERAL], insira:  
  consolelog=1  
    
  Inicie os serviços novamente.  
    
  Execute novamente o processo que apresentou o erro. Isso permitirá que o sistema gere os logs com os detalhes necessários para análise.  
    
  Após a reprodução, por gentileza nos encaminhe os seguintes arquivos atualizados:  
    
  \dbaccess\dbaccess.log  
  \dbaccess\dbconsole.log  
  \appserver\console.log

**Saiba mais:**  
[Cross Segmento - Backoffice Linha Protheus - SIGACTB - Reprocessamento de Saldos em Fila (CTBA193)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006706472--Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Reprocessamento-de-Saldos-em-Fila-CTBA193)

[CTBA193 Gerenciador de Saldos On-Line - P12 - Linha Microsiga Protheus - TDN](https://tdn.totvs.com/display/PROT/CTBA193+Gerenciador+de+Saldos+On-Line+-+P12?searchId=8YSVDN63Z)
