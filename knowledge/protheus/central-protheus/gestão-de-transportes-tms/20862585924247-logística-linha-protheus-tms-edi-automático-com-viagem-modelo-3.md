---
article_id: 20862585924247
category: Gestão de Transportes (TMS)
content_hash: 6395ecaadab54477fe6f6210de87b5ab144d01d26a06e3cf76565a9063714be9
fetched_at: '2026-06-28T22:45:27.657803+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - EDI Automático com viagem modelo 3
type: support-article
updated_at: '2024-01-26T12:46:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20862585924247-Log%C3%ADstica-Linha-Protheus-TMS-EDI-Autom%C3%A1tico-com-viagem-modelo-3
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20862551140375) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como configurar o **EDI** ***-*** **Electronic Data Interchange Automático** para gerar **Viagem Modelo 3**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Implementada melhoria no módulo **Gestão de Transportes - SIGATMS** na rotina **EDI Automático - TMSAE75** com a geração de **Viagem Modelo 3** quando agrupado por placa de veículo.  
  
A execução do **EDI Automático - TMSAE75** com a geração de **Viagens Modelo 3** depende exclusivamente da configuração do **Perfil do Cliente - TMSA480** nos campos **Viag. EDI Aut - DUO\_EDIVGE** **= 1 - Gera Viagem** e **Lote EDI Aut - DUO\_EDILOT** conforme exemplos abaixo.  
  
Acesse **Perfil do Cliente - TMSA480,** campo **Lote EDI Aut - DUO\_EDILOT:**

1. **Por processamento -** O Sistema vai gerar uma viagem para todos os documentos na execução do **EDI automático - TMSAE75**.
2. **Por destinatário** - O Sistema vai gerar uma viagem por destinatário. Se houver destinatários iguais, eles serão agrupados na mesma viagem.
3. **Por Placa Veiculo** - O Sistema gera viagens agrupando ou não os documentos conforme a placa informada no campo **Placa Veíc. - DE5\_PLACA**. Se este campo estiver vazio, o Sistema terá o mesmo comportamento da opção **1 - Por processamento**.

**Saiba mais**  
[Melhoria - EDI Automático (TMSAE75 - SIGATMS)](https://tdn.totvs.com.br/pages/releaseview.action?pageId=624779781)  
[DT Melhorias no EDI](https://tdn.totvs.com/display/public/PROT/DLOGTMS02-16662+DT+Melhorias+no+EDI)
