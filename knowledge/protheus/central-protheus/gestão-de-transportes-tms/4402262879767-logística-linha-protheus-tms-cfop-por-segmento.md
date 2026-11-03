---
article_id: 4402262879767
category: Gestão de Transportes (TMS)
content_hash: 3bd056fad3e58e391db0be1885216d22e4a8b35b800b389915f9c98f1d750025
fetched_at: '2026-06-28T22:45:27.393909+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - CFOP por Segmento
type: support-article
updated_at: '2023-05-19T17:40:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402262879767-Log%C3%ADstica-Linha-Protheus-TMS-CFOP-por-Segmento
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:30 min**  
**Dúvida**Como configurar o **TOTVS Logística TMS - Gestão de Transportes** para utilizar **CFOP - Código Fiscal de Operações e Prestações** por **Segmentos**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Para utilizar o **CFOP por Segmento** devem estar preenchidos os campos:  
Em **Atualizações** -> **Cadastro** -> **Tipos de Entradas e Saídas - MATA080**O campo **F4\_CF** deve estar informado o código **99943**

![Captura_de_tela_2021-06-08_141433.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4402314020375/Captura_de_tela_2021-06-08_141433.jpg)

Em **Atualizações** -> **Cadastro** -> **Clientes - MATA030**  
O campo **A1\_SATIV1** deve estar preenchido com o segmento do cliente

![Captura_de_tela_2021-06-08_141848.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4402314142871/Captura_de_tela_2021-06-08_141848.jpg)

Em **Atualizações** -> **Doctos e Regras** -> **CFOP x Segmentos - TMSA022**  
Cadastre o **CFOP** que será utilizado por segmento

![Captura_de_tela_2021-06-08_143508.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4402314289815/Captura_de_tela_2021-06-08_143508.jpg)

Em **Atualizações -> Doctos e Regras ->** **Regras Tributação - TMSA410**  
Defina a **TES** do **CFOP** **99943** por segmento

![Captura_de_tela_2021-06-08_144123.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4402314355735/Captura_de_tela_2021-06-08_144123.jpg)

Ao gerar o documento para o cliente devedor do segmento definido, o **CFOP** utilizado será o cadastrado na rotina **CFOP x Segmentos - TMSA022**.

![Captura_de_tela_2021-06-08_144957.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4402321577623/Captura_de_tela_2021-06-08_144957.jpg)
