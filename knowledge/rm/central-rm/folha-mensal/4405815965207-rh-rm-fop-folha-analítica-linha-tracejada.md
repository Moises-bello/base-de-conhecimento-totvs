---
article_id: 4405815965207
category: Folha Mensal
content_hash: 65507a565d00e53885860d025a450797defd9674613c6dcd381ddbe356081824
fetched_at: '2026-06-28T22:46:59.371560+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Folha Analítica: linha tracejada'
type: support-article
updated_at: '2025-01-20T21:38:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405815965207-RH-RM-FOP-Folha-Anal%C3%ADtica-linha-tracejada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min****Ocorrência**Ao gerar folha analítica no total por seções e total geral, o sistema está apresentando uma linha sobre os valores referente aos eventos. 

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406015820311/mceclip0.png)**

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - **12.1.31.189** ou inferiores e**12.1.32.124** ou inferiores.  
  
**Causa**Esse incidente ocorre devido a uma inconsistência na versão do sistema.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
**1.** Verifique a versão atual do RM. Para a correção, deverá estar na versão **patch 12.1.31.190** ou superiores ou**12.1.32.125** ou superiores.  
  
Consulte abaixo o link da Central de Downloads. Orientamos aplicar a última versão disponibilizada caso seja necessário atualizar, pois os patches são cumulativos.  
  
[Downloads e Atualizações](https://suporte.totvs.com/portal/p/10098/download#company/)  
  
**2.** Após atualização da versão, é necessário atualizar o relatório Folha Analítica em PDF. Acesse: **Gestão | RM Reports**, realize a exclusão de todos os relatórios da folha analítica importados. 

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405808606103/mceclip0.png)

**3.** Logo, importe o **relatório FOPREL0009** novamente. Segue abaixo documentação para lhe auxiliar no processo.   
  
[RH - RM - FOP - RM Reports: Importação de Relatórios](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007544951-RH-RM-FOP-RM-Reports-Importa%C3%A7%C3%A3o-de-Relat%C3%B3rios?source=search)  
  
**4.** Edite o arquivo para **"Visível a todas as coligadas"**  
![](https://totvssuporte.zendesk.com/attachments/token/KoJHW9TklOJZxBf7uX0b9YFwd/?name=image.png)  
  
**5.** Após realizar os passos 1, 2 e 3 gere a folha analítica novamente.  
  
**Importante**Caso mesmo com o processo de exclusão e importação persista a inconsistência na folha analítica, por gentileza, crie um novo perfil de parâmetro da folha analítica.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405815554199/mceclip1.png)
