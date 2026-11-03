---
article_id: 360042773193
category: eSocial - Gerar XML/ Integração Evento
content_hash: 842e907b4095de25d5874a24b566ec78d57bc6946519356864a09ad5492906dd
fetched_at: '2026-06-28T22:47:13.190194+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RM - eSocial - Erro na validação do campo vrPgTit (v.2.5)
type: support-article
updated_at: '2021-05-24T14:47:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042773193-RM-eSocial-Erro-na-valida%C3%A7%C3%A3o-do-campo-vrPgTit-v-2-5
---

**Ocorrência**  
Ao gerar o XML S-1200 ocorre erro na validação do campo **vrPgTit**: **Soma dos valores do Histórico Assistência Saúde não pode ser maior que o valor do evento no envelope**.  
  
**Ambiente**RM - eSocial - Todas as versões.  
  
**Causa**Este erro ocorre pois o lançamento do valor de assistência saúde está divergente entre o envelope do funcionário e o histórico de assistência à saúde.  
  
**Solução**Para correta geração do evento **S-1200** siga os passos abaixo:  
1. Acesse **Folha de Pagamento | Administração de Pessoal | Funcionários,** selecione o funcionário e acesse **Anexo | Históricos | Histórico de Assistência Saúde**. Verifique o valor que foi lançado no histórico para o período de apuração com erro na geração do evento **S-1200**;2. Acesse **Folha de Pagamento | Administração de Pessoal | Funcionários,**selecione o funcionário desejado e depois selecione **Envelope.** Verifique o valor de assistência saúde lançado;  
3. Constatando a divergência dos valores, ajuste o histórico ou o lançamento do envelope para o valor devido.  
  
**importante**  
Documentação válida somente para leiaute eSocial anterior à versão S-1.0
