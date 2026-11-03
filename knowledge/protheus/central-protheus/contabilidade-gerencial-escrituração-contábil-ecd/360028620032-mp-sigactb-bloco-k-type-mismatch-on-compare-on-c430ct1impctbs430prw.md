---
article_id: 360028620032
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: f7e7076fd0dadb7ab9e143381c3252e25e6e0cba66de7990ccfb835b626ae68c
fetched_at: '2026-06-28T22:40:45.742504+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: MP - SIGACTB - BLOCO K -  type mismatch on compare  on C430CT1IMP(CTBS430.PRW)
type: support-article
updated_at: '2021-04-28T22:07:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028620032-MP-SIGACTB-BLOCO-K-type-mismatch-on-compare-on-C430CT1IMP-CTBS430-PRW
---

**Dúvida**

Ocorre erro, type mismatch on compare on C430CT1IMP(CTBS430.PRW) ao importar plano de contas para o bloco K.  
   
 **Ambiente**  
Protheus – Contabilidade Gerencial – A partir da versão 12.1.17]  
  
**Solução**

A inconsistência ocorre devido à falta de campo no pergunte da rotina, que é criado com a aplicação do último pacote, mais a execução com compatibilizador UPDDISTR, para atualizar o dicionário referente ao módulo SIGACTB.

1- Baixe o pacote referente ao ECD, [Clique aqui para baixar.](http://tdn.totvs.com/pages/releaseview.action?pageId=458762370) (Se o ambiente contabilidade gerencial não estiver atualizado, baixar também o pacote acumulado SIGACTB, [Clique aqui para baixar.](https://suporte.totvs.com/portal/p/10098/download#detail/752657)  
2- Faça backup do RPO, e aplicar o(s) patch(s) .ptm  
3 - Faça backup da pasta systemload.  
4 - Exclua da pasta systemload o arquivo sdfbra.txt, e inclua o arquivo sdfbra.txt do pacote baixado.  
  
Excluir os arquivos de log abaixo:  
Dentro da pasta system:

* mpupdlog.log
* mpupdlog.fpt
* mpwizard.hlp
* mpwizardhlp.lck

Dentro da pasta Appserver:

* mpupddistri.tsk

Realizar a execução do UPDDISTR em seu ambiente
