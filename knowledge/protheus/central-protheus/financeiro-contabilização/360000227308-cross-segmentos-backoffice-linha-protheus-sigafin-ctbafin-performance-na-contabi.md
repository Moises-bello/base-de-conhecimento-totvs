---
article_id: 360000227308
category: Financeiro - Contabilização
content_hash: de6141e9f30f96ab7ae905810ef31677fe00541b5643643b7e510a22f5628f3e
fetched_at: '2026-06-28T22:38:05.225608+00:00'
product: protheus
section_id: 1500001550502
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBAFIN - Performance
  na Contabilização do Financeiro
type: support-article
updated_at: '2024-07-26T19:37:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000227308-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBAFIN-Performance-na-Contabiliza%C3%A7%C3%A3o-do-Financeiro
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25200203973655)***Tempo aproximado para leitura: **00:05:00 min**

**Ocorrência**No módulo **Financeiro**, ao tentar realizar o processo **Contabilização Off-line (CTBAFIN)** é apresentada uma lentidão.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o portal do cliente e realizar o *download* do **dicionário completo** e **diferencial** disponibilizado para a sua *release* (recomendamos sempre estar com a última *release*)

Ex.:

* 18-01-12-BRA-DICIONARIOS\_COMPL\_12\_1\_17 - Completo
* 18-01-12-BRA-DICIONARIOS\_DIF\_12\_1\_17 - Diferencial

**Importante**:  
Lembrando que em caso de dicionários para outros países, deve-se realizar o *download* do pais respectivo.

2. Ainda no portal do cliente, realizar o download do pacote de atualizações dos programas e das procedures.

3. Realizar o *backup* do seu ambiente (dicionário, dados (**SGDB**) e **RPO**)

4. Excluir os arquivos de log abaixo:

Dentro da pasta *system*:

**mpupdlog.log**  
**mpupdlog.fpt**  
**mpwizard.hlp**  
**mpwizardhlp.lck**

Dentro da pasta *Appserver*:

**mpupddistri.tsk**

5. Copie os arquivos de dicionário e *procedures* para a sua pasta **systemload**

6. Aplique o pacote de atualização em seu **RPO**

7. Realize a execução do **UPDDISTR.**

8. No **configurador**, ajuste as configurações de parâmetros abaixo:

* **MV\_FINLOG** precisa ser habilitado para .T. - [Parâmetro MV\_FINLOG](http://tdn.totvs.com/pages/viewpage.action?pageId=6070492)

* **MV\_DIRDOC** precisa ser definido para a geração do arquivo de inconsistências (verificar se está apontando para uma pasta valida do ERP ex. *System*)

* **MV\_PRELAN** precisa estar como “D” - [MV\_PRELAN - Indicador de Pre lançamento Contábil](http://tdn.totvs.com/pages/viewpage.action?pageId=284348618)

* **MV\_ATUSAL** precisa estar como “S”

* **MV\_CFINTHR** pode colocar a quantidade que o SLAVE aguentar (limitado a 30 threads) - [Contabilização Off-line com múltiplos processos – Financeiro](http://tdn.totvs.com/pages/viewpage.action?pageId=6070318)

* **MV\_CTBUPRC** deve estar como .F. - [MSERV-1074 DTparâmetro MV\_CTBUPRC](http://tdn.totvs.com/pages/releaseview.action?pageId=223930616)

* **MV\_CTBFLAG** deve estar como .T. - [MV\_CTBFLAG Controle de transação na contabilização off-line](https://tdn.totvs.com/pages/viewpage.action?pageId=541984154)

9. Habilitar o **CTBA193** (Reprocessamento de saldos em fila) - [CTB0113\_REPROCESSAMENTO\_SALDOS\_POR\_FILA\_P12](http://tdn.totvs.com/display/public/PROT/CTB113_REPROCESSAMENTO_SALDOS_POR_FILA_P12)

* No módulo configurações acessar **Ambiente** > ***Schedule*** > ***Schedule***.

* Clique no ícone da pasta *Schedule*

* Clique no botão **Iniciar todos os serviços**

* Selecione na pasta **Agent** > **Cadastro**

* Clique Adicionar **agents padrão**

* Clique na **Pasta Agendamentos**

* Selecione a opção **Incluir**

* No campo rotina, digite **CTBA193**

* Selecione as empresas e Filiais para processamento

* Selecione como **módulo o 34** – **Contabilidade Gerencial**.

* Clique no botão recorrência para configurar a periodicidade que o sistema irá acionar o agendamento (recomendamos deixar sempre ativo)

No *link* encaminhado sobre o processamento, há um vídeo *HOWTO* de como configurar passo a passo o processo.

10. Desinstalar e instalar as *procedures* atualizadas (em anexo). Se não executar este passo, provavelmente possamos ter um problema no momento de compor os saldos.

11. Inicie o processo de contabilização.

**Saiba mais**

[Contabilização Offline - CTBAFIN](https://tdn.totvs.com/pages/releaseview.action?pageId=497932563#Contabiliza%C3%A7%C3%A3oOffline-CTBAFIN-Financeiro-P12-03.PAR%C3%82METROSAPLICADOS)
