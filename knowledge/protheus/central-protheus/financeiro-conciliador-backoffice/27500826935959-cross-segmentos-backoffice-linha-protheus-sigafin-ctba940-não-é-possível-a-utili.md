---
article_id: 27500826935959
category: Financeiro - Conciliador Backoffice
content_hash: 63a95108620a3a3eb4a025e4ec01102551c05327f3f88a76a904879e9496db0f
fetched_at: '2026-06-28T22:37:47.205850+00:00'
product: protheus
section_id: 30769054561431
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Não é possível
  a utilização desta configuração de conciliação porque não foram encontrados os seguintes
  campos de identificação única em seu ambiente: IG_MSUIDT; FK5_MSUIDT'
type: support-article
updated_at: '2025-09-11T17:42:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27500826935959-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-N%C3%A3o-%C3%A9-poss%C3%ADvel-a-utiliza%C3%A7%C3%A3o-desta-configura%C3%A7%C3%A3o-de-concilia%C3%A7%C3%A3o-porque-n%C3%A3o-foram-encontrados-os-seguintes-campos-de-identifica%C3%A7%C3%A3o-%C3%BAnica-em-seu-ambiente-IG-MSUIDT-FK5-MSUIDT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27500766263063) Tempo aproximado para leitura: **00:06 min****Ocorrência**Como posso resolver o seguinte problema: "Não é possível a utilização desta configuração de conciliação porque não foram encontrados os seguintes campos de identificação única em seu ambiente: **IG\_MSUIDT; FK5\_MSUIDT"**?  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da versão 12.1.22.10  
  
**Causa**Campos de ID com o status = **"A incluir"**  
  
**Solução:**

É importante **confirmar se o Wizard do Conciliador foi executado corretamente**.  
Para isso, reforçamos ser necessário garantir:

1. **Atualização do Backoffice** para a release vigente.
2. **Atualização do dicionário de dados**.
3. **Execução do UPDDISTR em modo exclusivo**, assegurando que todas as alterações sejam aplicadas corretamente no ambiente.

Quando o processo for concluído com sucesso, o sistema deve demonstrar no campo **“Status” = OK** na opção **“Gerar campos de ID”**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34873613943063)

**Saiba Mais**

[How To | SIGAFIN - CTBA940 - Instalação Conciliador Financeiro](https://www.youtube.com/watch?v=alUTiPi2gms)  
[Cross Segmento - Backoffice linha Protheus - SIGAFIN - CTBA940- Novo Conciliador Bancário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22896337613463)  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - How to Novo Conciliador Backoffice Financeiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23945644752279)
