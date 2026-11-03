---
article_id: 29289226473751
category: Gestão de Transportes (TMS)
content_hash: 671177ea7166ef43433d7c40737b88db8691b4b2d6e0a0b67acf232149782f6b
fetched_at: '2026-06-28T22:45:27.705523+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Encerramento de MDFe em viagem de transporte
type: support-article
updated_at: '2025-01-17T16:59:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29289226473751-Log%C3%ADstica-Linha-Protheus-TMS-Encerramento-de-MDFe-em-viagem-de-transporte
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29289226446359) Tempo aproximado para leitura: **00:01:05 min** **Dúvida**Como funciona o encerramento de **MDFe - Manifesto de Documento Fiscal eletrônico** em viagem de transporte entre filiais?   
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Conforme **Manual de Orientações do Contribuinte** com os padrões técnicos de comunicação do **MDFe**, o evento de encerramento do **MDFe** deve ser feito pelo emitente no final do percurso.  
  
Sendo assim, no caso de viagem de transporte, onde o transporte inicia em uma filial e finaliza em outra filial, o **MDFe** deve ser encerrado pela filial de origem. Para isso, a filial de destino deve solicitar o encerramento para a filial de origem quando a viagem chegar na filial de destino.   
  
Caso deseje automatizar este encerramento do **MDFe**, temos o processo de manifesto automático, que pode encerrar o **MDFe** de forma automática com o parâmetro **MV\_MDFEENC**.  
  
**Saiba mais**Documentação sobre o Manifesto automático: [MDF-e Automático - Automação do Manifesto](https://tdn.totvs.com.br/pages/releaseview.action?pageId=532049649)Exemplos de Automação do Manifesto: [DT Automação do Manifesto - Cenários MDF-e Automático](https://tdn.totvs.com.br/pages/releaseview.action?pageId=461918037)
