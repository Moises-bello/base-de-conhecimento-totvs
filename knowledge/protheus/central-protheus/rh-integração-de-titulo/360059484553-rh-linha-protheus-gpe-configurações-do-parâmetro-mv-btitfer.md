---
article_id: 360059484553
category: RH - Integração de Titulo
content_hash: a696312e43e3628e531ca2acdd055af40ebdc96f0f87ac632073499542ad960c
fetched_at: '2026-06-28T22:43:36.291396+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Configurações do parâmetro MV_BTITFER
type: support-article
updated_at: '2025-07-29T18:50:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059484553-RH-Linha-Protheus-GPE-Configura%C3%A7%C3%B5es-do-par%C3%A2metro-MV-BTITFER
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33799323080599) Tempo aproximado para leitura: **00:01:00 min****

**Dúvida**Configurações do parâmetro MV\_BTITFER  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**

Realizado ajuste para que antes do início da ação de excluir ocorra uma verificação de registro na tabela RJ1 (Detalhes de Títulos Def. Usuário para Roteiros’), caso encontre o registro exiba a seguinte mensagem para o usuário :

* [MV\_BTITFER = 0](https://tdn.totvs.com/pages/releaseview.action?pageId=557336263#tabs-A)
* [MV\_BTITFER = 1](https://tdn.totvs.com/pages/releaseview.action?pageId=557336263#tabs-B)
* [MV\_BTITFER = 2](https://tdn.totvs.com/pages/releaseview.action?pageId=557336263#tabs-C)
* [Fluxograma do Processo](https://tdn.totvs.com/pages/releaseview.action?pageId=557336263#tabs-D)

Quando o parâmetro **MV\_BTITFER**estiver configurado com**0**:  
Não irá realizar nenhuma validação sobre a existência de títulos e irá prosseguir com a ação.

**Importante**  
Tais validações não ocorrerão sobre dados de Férias geradas através de Férias Coletivas/Programadas. Também não serão executadas na rotina de Férias Coletivas/Programadas.

**Saiba Mais**  
[DRHGCH-20451 DT Integração Títulos Financeiros com Roteiros (Dicionário)](https://tdn.totvs.com/x/3mMxIQ)  
[DRHGCH-20134 DT Integração Títulos Financeiros com Roteiros (Geração Títulos)](https://tdn.totvs.com/pages/viewpage.action?pageId=556890394)  
[DRHGCH-20410 Integração Títulos Financeiros com Roteiros (Rescisão)](https://tdn.totvs.com/pages/viewpage.action?pageId=557325755)  
[DRHGCH-20409 Integração Títulos Financeiros com Roteiros (Folha e Adiantamento)](https://tdn.totvs.com/pages/viewpage.action?pageId=557683476)
