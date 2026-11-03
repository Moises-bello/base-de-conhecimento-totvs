---
article_id: 360020257371
category: RH - Dissídio
content_hash: a745e5eccdd34603e447b0283d32e9191cc53040b903c9e61ab482c100a5fbfc
fetched_at: '2026-06-28T22:43:44.282934+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - No cálculo do dissídio retroativo não é demonstrada
  verba vinculada ao ID 0031
type: support-article
updated_at: '2025-08-20T14:30:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020257371-RH-Linha-Protheus-GPE-No-c%C3%A1lculo-do-diss%C3%ADdio-retroativo-n%C3%A3o-%C3%A9-demonstrada-verba-vinculada-ao-ID-0031
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34317203502999) Tempo aproximado para leitura: 00:00:30 min**

**Ocorrência**Ao solicitar o cálculo de **dissídio retroativo** para funcionários **mensalistas** com lançamentos acumulados corretos na SRD e configurações de verbas corretas para cálculo da diferença a pagar, o sistema não gera lançamentos para o **ID 0031** (salário).   
  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17  
  
**Causa**Inconsistência nos lançamentos dos históricos salariais. Não é informado o conteúdo do campo categoria do funcionário.  
  
**Solução**Necessário validar as seguintes informações:  
**1.** Acessar a rotina de históricos salariais (cabeçalho tabela **SR7**) e confirmar se as informações do funcionário estão corretamente informadas. Se a categoria do funcionário não estiver cadastrada, o sistema irá calcular o novo valor referente ao ID 0031, mas não irá gravar no dissídio.  
**2.** Conferir conteúdo do parâmetro **MV\_CALCINF.** Se este estiver com "S" o sistema somente irá considerar o ID 0031 se este estiver como informado nos lançamentos acumulados.  
  
  
  
**Saiba mais**Pacote acumulado RH: <https://suporte.totvs.com/portal/p/10098/download#000006>

[Página Centralizadora do Dissídio (GPEM690)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio)
