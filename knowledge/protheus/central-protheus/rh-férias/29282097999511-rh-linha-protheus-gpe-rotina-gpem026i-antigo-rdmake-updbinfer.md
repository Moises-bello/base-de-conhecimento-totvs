---
article_id: 29282097999511
category: RH - Férias
content_hash: 2669525f746b231d5bb95c4b3e902b597a2b3d89f78ebf566007ac77a3401ccc
fetched_at: '2026-06-28T22:43:59.218351+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Rotina GPEM026I (Antigo Rdmake UPDBINFER)
type: support-article
updated_at: '2026-04-01T20:16:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29282097999511-RH-Linha-Protheus-GPE-Rotina-GPEM026I-Antigo-Rdmake-UPDBINFER
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29282097970711) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Rotina GPEM026I (Antigo Rdmake UPDBINFER)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**A rotina **GPEM026I (Antigo *Rdmake* UPDBINFER)** foi criada para ajustar/gerar as verbas de ID's: **1870, 1871, 1872, 1891, 1892, 1893, 1969 e 1970** **no cálculo das férias.****OBS:** A rotina só deve ser executada se o **roteiro FER estiver integrado**, portanto, a rotina não deve ser executada caso este roteiro ainda esteja aberto.  
A rotina também pode ser executada se a **Folha estiver fechada.**Para utilização da rotina, deverá ser efetuada a **[inclusão manual](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013342191-RH-Linha-Protheus-GPE-Como-excluir-ou-incluir-rotinas-no-menu)**da rotina **GPEM026I** no menu do módulo SIGAGPE, cadastrando o tipo como **Função Protheus** e criar o grupo de perguntas **UPDBINRES** caso não exista no ambiente, conforme passos abaixo:  
  
**1 -** Inclusão da rotina no menu:  
 **![](https://centraldeatendimento.totvs.com/hc/article_attachments/31609390214295)**

**OBS:** Se já existir o *rdmake* configurado, será necessário ajustar o menu no Configurador para que chame o programa **GPEM026I.  
  
  
2 -** Grupo de Perguntas **UPDBINRES:** Acesse o **Configurador > Base de Dados > Dicionário > Base de Dados > Perguntas > Incluir >** informe o grupo **UPDBINRES** e complete os campos com as informações abaixo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29282097978647)  
  
  
  
**3 -** Rotina pronta para ser utilizada:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29282493777687)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29282493782551)

**Saiba Mais:**[Rdmake UPDBINFER](https://tdn.totvs.com/display/PROT/DRHROTPRT-6153+DT+Rdmake+UPDBINFER)  
[RH - Linha Protheus - GPE - eSocial - S-1200 - O INSS, FGTS e IR ficam incorretos no eSocial (DCTFWEB) quando existe Férias no mês](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4422759630487-RH-Linha-Protheus-GPE-eSocial-S-1200-O-INSS-FGTS-e-IR-ficam-incorretos-no-eSocial-DCTFWEB-quando-existe-F%C3%A9rias-no-m%C3%AAs)  
[RH - Linha Protheus - GPE - Ao executar o Rdmake GPEM026I aparece tela para informar uma verba de diferença entres os id's 1870 e 0013, quando o MV\_DINSSFM =N](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15525837930135-RH-Linha-Protheus-GPE-Ao-executar-o-Rdmake-GPEM026I-aparece-tela-para-informar-uma-verba-de-diferen%C3%A7a-entres-os-id-s-1870-e-0013-quando-o-MV-DINSSFM-N)  
[RH - Linha Protheus - GPE - Ao realizar execução do RDMake UPDBINFER é apresentado error log - Incorrect syntax near the keyword 'IN'.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411454979735-RH-Linha-Protheus-GPE-Ao-realizar-execu%C3%A7%C3%A3o-do-RDMake-UPDBINFER-%C3%A9-apresentado-error-log-Incorrect-syntax-near-the-keyword-IN)  
[Manual de Férias](https://tdn.totvs.com/pages/viewpage.action?pageId=941247504)
