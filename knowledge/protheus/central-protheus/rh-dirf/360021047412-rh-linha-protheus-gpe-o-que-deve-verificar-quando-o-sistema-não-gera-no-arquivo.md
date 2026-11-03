---
article_id: 360021047412
category: RH – DIRF
content_hash: cbeb776b80ea58cf92206caaa6353d64542284c7ce1a3bc570fb9f1d80079d15
fetched_at: '2026-06-28T22:44:07.913913+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - O que deve verificar quando o sistema não gera
  no arquivo magnético da DIRF todos os funcionários
type: support-article
updated_at: '2025-08-04T19:04:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021047412-RH-Linha-Protheus-GPE-O-que-deve-verificar-quando-o-sistema-n%C3%A3o-gera-no-arquivo-magn%C3%A9tico-da-DIRF-todos-os-funcion%C3%A1rios
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21066279586967)** **Tempo aproximado para leitura: 00:02:00 min****Dúvida**O que verificar quando o sistema não gera no arquivo magnético da DIRF todos os funcionários?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Temos dois mnemônicos no Sistema que definem a partir de qual valor os rendimentos devem ser carregados para o arquivo magnético:

- **P\_VLLIMDIRF** define o valor mínimo dos rendimentos a serem considerados para a geração do arquivo magnético da DIRF para beneficiário de trabalho assalariado. Seu valor padrão é R$ 17989.80.

**- P\_VLLIMOUT** define o valor mínimo dos rendimentos a serem considerados para a geração do arquivo magnético da DIRF referente a rendimentos sem vínculo empregatício, de aluguéis e de royalties. Seu valor padrão é R$ 6000.00.

Como esses mnemônicos que definem o valor mínimo de rendimento tributável para ser gerado no arquivo magnético, se o P\_VLLMDIRF estiver preenchido com R$ 28.559,70, somente os funcionários que tiveram rendimentos tributáveis acima deste valor na soma total do ano de calendário serão gerados no arquivo magnético.  
  
Caso queira levar **todos os funcionários ou rendimentos sem vínculos empregatícios,** deixe os mnemônicos preenchidos com 0.00 ou 0.01 **(importante que seja utilizado ponto e não vírgula para separação dos centavos)**.  
  
**IMPORTANTE:** Ao executar a Geração de Arquivo (GPEM550), serão apresentadas todas as matrículas na rotina de Manutenção do Arquivo que tenham verbas no ano calendário configuradas para a DIRF, independente de ter ou não o rendimento mínimo acumulado durante o ano-calendário definido nos mnemônicos. Os mnemônicos serão considerados somente para a Geração do Arquivo Magnético (GPEM590).

**Observação:** Se houver recolhimento de IRRF para o beneficiário, mesmo que o rendimento tributável seja inferior ao valor informado nos mnemônicos P\_VLLIMDIRF e P\_VLLIMOUT, o beneficiário será gerado no arquivo magnético da DIRF.

**Saiba Mais:**[RH - DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF)
