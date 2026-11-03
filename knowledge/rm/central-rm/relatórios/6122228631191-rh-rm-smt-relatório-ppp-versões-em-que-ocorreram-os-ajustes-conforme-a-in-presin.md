---
article_id: 6122228631191
category: Relatórios
content_hash: 41f457527267becc55c340d7ae38a9d8730b0e2fa5ed68470b52d3e59e7668ea
fetched_at: '2026-06-28T22:47:43.437883+00:00'
product: rm
section_id: 1500000861522
source: central-rm
title: 'RH - RM - SMT - Relatório PPP: Versões em que ocorreram os ajustes conforme
  a  IN PRES/INSS  Nº 128, DE 28 DE MARÇO DE 2022 e  Nº133, DE 26 DE MAIO DE 2022'
type: support-article
updated_at: '2025-05-07T16:39:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6122228631191-RH-RM-SMT-Relat%C3%B3rio-PPP-Vers%C3%B5es-em-que-ocorreram-os-ajustes-conforme-a-IN-PRES-INSS-N%C2%BA-128-DE-28-DE-MAR%C3%87O-DE-2022-e-N%C2%BA133-DE-26-DE-MAIO-DE-2022
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16036417337751) Tempo aproximado para leitura: **00:01:40 min** **Dúvida**Em quais versões ocorreram a liberação dos ajustes realizados no relatório PPP, referente as instruções normativas PRES/INSS Nº 128, DE 28 DE MARÇO DE 2022 e IN133, DE 26 DE MAIO DE 2022?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Segurança e Saúde Ocupacional - 12.1.33.268 e superiores  
  
**Solução**

A liberação ocorreu, nas seguintes versões:

* **12.1.33.268** e superiores
* **12.1.34.168** e superiores
* **12.1.2205.109** e superiores

*Rotina: PPP (PERFIL PROFISSIOGRÁFICO PREVIDENCIÁRIO)*

*[Ticket: 14401126 / DRHHCM-3884] Realizado ajuste e nova liberação do relatório PPP para atender à Instrução Normativa 133.*  
*Arquivo: RM.Smt.Relatorio.Data.dll*

*Rotina: PPP (PERFIL PROFISSIOGRÁFICO PREVIDENCIÁRIO)*  
*[Ticket: 13965001 / DRHHCM-3311] Adequação estrutural do PPP para adequação à IN 128.*  
*Arquivos: RM.Smt.Relatorio.Intf.dll; RM.Smt.Relatorio.Data.dll*Lembrando que além de realizar a atualização da release e/ou patch, deve ser executado os scripts intermediários. Para executar os scripts, acesse a documentação abaixo:

[Framework - Framework RM - BD - Scripts Opcionais/Intermediários RM.Atualizador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007553911-Framework-Framework-RM-BD-Scripts-Opcionais-Intermedi%C3%A1rios-RM-Atualizador)  
  
Após realizar a atualização da aplicação é necessário importar a nova estrutura do relatório que estará disponível no book de relatórios. Acesse o RM | Guia Gestão | TOTVS Compartilhamento e procure pela estrutura **RHUREL0004 - PPP.** Baixe a estrutura e salve no disco para importá-la em seguida.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26639142593687)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26639142596119)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26639142598423)

Antes da importação, é necessário que seja feita a exclusão do relatório disponível na base de dados através do Gestão | RM Reports.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26639158013079)

Em seguida, siga os passos da documentação abaixo para importar a nova estrutura:

[RH - RM - SMT - Importação de relatórios](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409650455703)

**Saiba mais:**Para maiores informações, acesse:

- [RH - RM - SMT - PPP: Campos Alterados: INSTRUÇÃO NORMATIVA PRES/INSS Nº 128, DE 28 DE MARÇO DE 2022 e Nº 133, DE 26 DE MAIO DE 2022](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6118735378967)- [INSTRUÇÃO NORMATIVA PRES/INSS Nº 133, DE 26 DE MAIO DE 2022](https://www.in.gov.br/web/dou/-/instrucao-normativa-pres/inss-n-133-de-26-de-maio-de-2022-403670931)

- [INSTRUÇÃO NORMATIVA PRES/INSS Nº 128, DE 28 DE MARÇO DE 2022](http://www.normaslegais.com.br/legislacao/Instrucao-normativa-inss-128-2022.htm)

- [INSTRUÇÃO NORMATIVA PRES/INSS Nº 128, DE 28 DE MARÇO DE 2022 - parte 2](http://www.normaslegais.com.br/legislacao/parte2-instrucao-normativa-inss-128-2022.htm)

- [RH - RM - SMT - Como gerar o Relatório PPP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000240188)
