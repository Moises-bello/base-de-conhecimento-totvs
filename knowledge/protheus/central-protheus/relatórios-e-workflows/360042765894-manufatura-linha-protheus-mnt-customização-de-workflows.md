---
article_id: 360042765894
category: Relatórios e Workflows
content_hash: 51e1bdea50c614205d6f972cead9b1aa428fb7343edeca762b3244c8451c9ec1
fetched_at: '2026-06-28T22:42:31.667896+00:00'
product: protheus
section_id: 360010992394
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Customização de Workflows
type: support-article
updated_at: '2021-06-11T11:47:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042765894-Manufatura-Linha-Protheus-MNT-Customiza%C3%A7%C3%A3o-de-Workflows
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png) Tempo aproximado para leitura:**00:02:00 min**  
**Dúvida**Como realizar a customização do *layout* e informações que são apresentadas nos *Workflows*?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Relatórios e Workflows - Versão 12  
  
**Solução**Para realizar a remoção ou inclusão de informações que não dependem da execução da rotina ou campos da base, o usuário deve acessar o diretório definido no parâmetro **MV\_WFDIR** - **Diretório de trabalho do *Workflow****,* onde estão armazenados os arquivos **.htm** para o envio dos *workflows,* e customizar o arquivo correspondente ao *workflow* que deseja modificar. Estes arquivos estão no formato **HTML - Hypertext Markup Language**e podem ser customizados e atualizados de acordo com a necessidade do usuário. Após a atualização deste, a próxima execução do *workflow* será de acordo com a definição contida no arquivo customizado.  
  
Já para as customizações que dependem de registros gerados pela rotina ou campos de usuário, além da customização do arquivo **.htm** como citada acima, é imprescindível a utilização do ponto de entrada **NGTWFPro**. Este ponto de entrada permite o preenchimento de quaisquer campos contidos no arquivo de *layout* do *workflow*.  
  
**Importante**O processo de customização do *layout* de *workflows* por meio do ponto de entrada **NGTWPro** se restringe a algumas rotinas neste primeiro momento, que são:

* **MNTA693 - Transferência de Bens**
* **MNTW025 - Workflow de Inclusão de S.S**
* **MNTW040 - Workflow de Distribuição de S.S**
* **MNTW060 - Workflow de Inclusão de Multa**
* **MNTW061 - Workflow de Inclusão de Notificação**

**Saiba mais**Para informações complementares a respeito do ponto de entrada **NGTWPro**, acesse o *link* [NGTWFPro.](https://tdn.totvs.com/x/vIUfGg)
