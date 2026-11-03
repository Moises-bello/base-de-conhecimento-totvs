---
article_id: 360025161134
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: c6194ce64611cce9fc460de7c6733658de7c77fdfa7e06400c69a48fee00162e
fetched_at: '2026-06-28T22:42:43.269194+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Finalidade do recurso alternativo e
  secundário
type: support-article
updated_at: '2021-08-18T10:53:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025161134-Manufatura-Linha-Protheus-SIGAPCP-Finalidade-do-recurso-alternativo-e-secund%C3%A1rio
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:30 min**  
**Dúvida**Qual o objetivo do cadastro de **recurso alternativo e secundário** existente no **MATA610 - Cadastro de Recursos** e **MATA632 - Cadastro de operações**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Os recursos determinados como alternativo ou secundários no **MATA610** ou **MATA632** serão utilizados ao executar o **MATA690 -  Carga Máquina** quando o recurso relacionado com a operação não puder ser alocado. Para isso devem ser especificados quais os recursos, qual a sua eficiência em relação ao recurso principal e se o mesmo é identificado como secundário ou alternativo.  
  
Durante a alocação das operações pelo **MATA690**, caso não exista disponibilidade de alocação no recurso principal a rotina procura alocar as operações nos recursos alternativos e por último nos recursos secundários, considerando primeiramente os recursos alternativos determinados no **MATA610**, em seguida os recursos alternativos determinados no **MATA632**, em seguida os recursos secundários determinados no **MATA610** e por fim os recursos secundários do **MATA632.**Sendo assim, mesmo que um recurso secundário tenha melhores condições de executar uma operação, prevalece a disponibilidade do recurso principal e de acordo com ela a operação é alocada, o recurso determinado como secundário recebe a operação somente se não existe disponibilidade de execução pelo recurso principal e seus alternativos.
