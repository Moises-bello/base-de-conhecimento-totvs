---
article_id: 360049975474
category: RH - FGTS / SEFIP
content_hash: 403e65d3b4f39c89c53b9a88aa7eb64cfd3c163fd031a91d12268d5830a8991e
fetched_at: '2026-06-28T22:43:41.444250+00:00'
product: protheus
section_id: 360003115651
source: central-protheus
title: RH - Linha Protheus - GPE - O que verificar quando ocorre o erro 320611 - Código
  de movimentação inválido ou não informado na SEFIP
type: support-article
updated_at: '2025-08-14T18:28:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049975474-RH-Linha-Protheus-GPE-O-que-verificar-quando-ocorre-o-erro-320611-C%C3%B3digo-de-movimenta%C3%A7%C3%A3o-inv%C3%A1lido-ou-n%C3%A3o-informado-na-SEFIP
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34187254399511) Tempo aproximado para leitura: 00:01:30 min  
  
Ocorrência**Ao gerar o  arquivo para **SEFIP** é apresentado o erro código **320611** - Código de movimentação inválido ou não informado na SEFIP. **Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Causa**Esse incidente pode ocorrer devido as parametrizações na tabela **S043 - Tipos de Rescisão** relacionando um código de afastamento do FGTS inválido ou **Tipo de Ausência** com um Código Ausência SEFIP incorreto.  
  
**Solução**Para o erro causado por **rescisão**, faça as verificações abaixo:

**1**. Entre em Atualizações >Definições de cálculo >Manutenção de Tabelas;  
**2**. Selecione a tabela **S043-Tipos de Rescisão**, entre como alterar e verifique se na coluna **Cod. Afast. FGTS** está preenchido com o código da movimentação correta para o tipo de rescisão:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075897914)

Para o erro causado por **afastamento**, faça a verificação abaixo:  
**3.** Entre em Atualizações >Definições de cálculo >Tipos de Ausência;  
**4.** Selecione o **Tipo de Ausência** relacionado ao funcionário, entre como Alterar e verifique se o campo **Cod. Au. SEFIP** esta preenchido com o código de movimentação correto para o Tipo de ausência em questão:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002323382)

**5.** Após o ajuste gere novamente o arquivo da SEFIP para correção do problema.  
 **Saiba mais**Para adquirir mais conhecimento acesse o(s) *link*(s) abaixo:[FGTS](https://tdn.totvs.com/display/public/PROT/FGTS) 

[RH \_ FGTS/SEFIP](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003115651-RH-FGTS-SEFIP)
