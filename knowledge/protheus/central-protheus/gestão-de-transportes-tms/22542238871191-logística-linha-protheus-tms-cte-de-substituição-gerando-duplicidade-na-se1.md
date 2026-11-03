---
article_id: 22542238871191
category: Gestão de Transportes (TMS)
content_hash: 72c4901d5cb4269ae2995b3b89f70a8d8c4016849718f2addb2c6affeb2503b3
fetched_at: '2026-06-28T22:45:27.634761+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - CTe de  Substituição gerando duplicidade
  na SE1
type: support-article
updated_at: '2025-03-26T18:17:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22542238871191-Log%C3%ADstica-Linha-Protheus-TMS-CTe-de-Substitui%C3%A7%C3%A3o-gerando-duplicidade-na-SE1
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22542296519191) Tempo aproximado para leitura: 00:01:15 min****Dúvida**Como proceder para não ocorrer duplicidade na **SE1** ao realizar um **CTe** de Substituição?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O parametro **MV\_TMSCTEA** define se o Sistema deve gerar títulos de **NCC** para fazer compensação dos movimentos gerados pelo **CTe** original. Ao utilizar os parâmetros **MV\_TMSMFAT = 1** e **MV\_TMSCTEA = F** ou em branco, o Sistema na geração do **CTe** de substituição, terá dois títulos em aberto na **SE1**.  
  
Se utilizar o parâmetro **MV\_TMSCTEA = T**, o Sistema irá gerar o título do tipo **NCC** para abater do titulo gerado pelo **CTe** original.  
  
Caso existir títulos em duplicidade na **SE1** gerados pelo **CTe** de substituição, é necessário proceder com a baixa do título do **CTe**original através do módulo **Financeiro**, utilizando o método de **DAÇÃO****.**Se necessitar de suporte em como realizar este processo, por favor, abra um ticket diretamente no módulo **Financeiro**.   
  
**Saiba mais**Mais informações poderão ser acessadas no *link*: [Manutenção de Documentos - Substituição (TMSA500 - SIGATMS)](https://tdn.totvs.com.br/pages/releaseview.action?pageId=547878594#Manuten%C3%A7%C3%A3odeDocumentosSubstitui%C3%A7%C3%A3o(TMSA500SIGATMS)-03.EXEMPLODEUTILIZA%C3%87%C3%83O%C2%A0)  
  
**Glossário**  
**CTe** - Conhecimento de Transporte Eletrônico  
**NCC** - Nota de Crédito Cliente
