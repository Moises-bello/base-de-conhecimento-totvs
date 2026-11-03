---
article_id: 18695137872407
category: Gestão de Transportes (TMS)
content_hash: 3ac6d0336f2f6a6561fb269503e0765fb384a068ea72904e5df4ad7775a3e26f
fetched_at: '2026-06-28T22:45:29.223123+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Gatilhos Customizados Viagem Modelo 3
type: support-article
updated_at: '2023-10-31T19:24:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18695137872407-Log%C3%ADstica-Linha-Protheus-TMS-Gatilhos-Customizados-Viagem-Modelo-3
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18695112625815) Tempo aproximado para leitura: **00:01:50 min** **Dúvida**Como definir gatilhos customizados para a viagem modelo 3 no **TOTVS Logística TMS**?   
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**A viagem modelo 3 gerencia os gatilhos da rotina internamente, não sendo possível utilizar gatilhos customizados pela tabela **SX7**, como nas outras rotinas.  
  
No caso da viagem modelo 3, caso deseje utilizar gatilhos customizados, é necessário utilizar o novo ponto de entrada **TMF60GAT**, que foi liberado na rotina **TMSAF60** **- Viagem Modelo 3** a partir da data 30/10/2023.   
  
Assim, quando o cliente fizer uso da viagem modelo 3 e desejar utilizar gatilhos customizados, deverá **criar os gatilhos customizados via ponto de entrada.**Quando não fizer o uso da viagem modelo 3, os novos gatilhos podem ser criados via tabela **SX7**, o que não protege o Sistema de um gatilho inutilizar o uso de outro. Caso o cliente fizer o uso de mais de um modelo de viagem, se faz necessária a **criação do novo gatilho tanto na SX7 quanto via ponto de entrada**, para que ambos os modelos de viagem recebam o gatilho corretamente.   
  
**Saiba mais**Documentação da inclusão do ponto de entrada **TMF60GAT** no Sistema: [18344588 DLOGTMS02-24780 DT Inclusão de Ponto de Entrada na Viagem Modelo 3.](https://tdn.totvs.com/pages/releaseview.action?pageId=801322569)  
Documentação do ponto de entrada **TMF60GAT**: [DT PE TMF60GAT Ponto de Entrada Permite a Inclusão de Gatilhos na Viagem Modelo 3.](https://tdn.totvs.com/pages/releaseview.action?pageId=801322040)  
Documentação Gatilhos de Campos **SX7**: [SX7 - Gatilhos de Campos](https://tdn.totvs.com/display/public/framework/SX7+-+Gatilhos+de+Campos)  
Pacotes da rotina **TMSAF60** **- Viagem Modelo 3 - 30/10/2023:**

* [12.1.33 - TMSAF60 - 30/10/2023](https://suporte.totvs.com/portal/p/10098/download?e=1125006)
* [12.1.2210 - TMSAF60 - 30/10/2023](https://suporte.totvs.com/portal/p/10098/download?e=1125007)
* [12.1.2310 - TMSAF60 - 30/10/2023](https://suporte.totvs.com/portal/p/10098/download?e=1125005)
