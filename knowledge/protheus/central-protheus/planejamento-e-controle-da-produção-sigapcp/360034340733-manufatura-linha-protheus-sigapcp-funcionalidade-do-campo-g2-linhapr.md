---
article_id: 360034340733
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 61b86144468cdf0207abbcfae57f1dcdc8190c384ac4ee4e7edb7591f08c24f8
fetched_at: '2026-06-28T22:42:43.296637+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Funcionalidade do campo G2_LINHAPR
type: support-article
updated_at: '2026-04-30T18:36:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034340733-Manufatura-Linha-Protheus-SIGAPCP-Funcionalidade-do-campo-G2-LINHAPR
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21910542596887)** Tempo aproximado para leitura:**00:00:50 min**  
  
**Dúvida**  
Para que serve campo **G2\_LINHAPR - Linha de Produção** no **MATA632 - Roteiro de Operações**?  
  
**Ambiente**  
Microsiga Protheus - Planejamento e Controle da Produção - Versão 12  
  
**Solução**  
A informação referente a **linha de produção** é utilizada somente na alocação dos recursos no **MATA690 - Carga Máquina**.

* Quando o **G2\_TPLINHA - Tipo de Linha** está definido como **Obrigatória**, serão utilizados os alternativos cadastrados para a mesma linha de produção;
* Se for definido como **Preferencial**, ao alocar os recursos alternativos será dada preferência aos recursos que fazem parte da mesma linha de produção;
* Se for definido como **Dependente**, os recursos alocados deverão pertencer à linha de produção do recurso anteriormente alocado no processo.
