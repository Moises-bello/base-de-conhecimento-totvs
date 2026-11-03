---
article_id: 360035078174
category: RH – DIRF
content_hash: 82c2a532a45bae2506ff88d14ce0c108ef650ea5e128a7ebeb66b1e08731d982
fetched_at: '2026-06-28T22:44:06.883864+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Como gerar DIRF para encerramento de empresas
type: support-article
updated_at: '2025-08-21T12:52:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035078174-RH-Linha-Protheus-GPE-Como-gerar-DIRF-para-encerramento-de-empresas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34341474492951)**Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Como gerar DIRF para encerramento de empresas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
1. Gere os valores do ano correspondente através da rotina **Gerar Arquivo GPEM550**, pelo caminho **>Miscelânea >DIRF >Gerar Arquivo;**  
No exemplo abaixo geraremos valores de 2019.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046449413)  
  
2. Confira os valores gerados através do menu **Manutenção Arquivo GPEM560,** pelo caminho **>Miscelânea >DIRF >Manutenção de Arquivo;**  
([Clique aqui e veja exemplo de conferência dos valores](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021560272)). **![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046449553)**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045596254)  
3. No menu **Arquivo Magnético GPEM590**, pelo caminho **>Miscelânea >DIRF >Arquivo Magnético** é possível gerar o arquivo que será importado ao programa da DIRF.  
  
Para isso, é necessário atentar-se em alguns parâmetros específicos para encerramento da empresa:  
- O **Tipo da Entrega** deve ser uma **Inclusão**;- **Ano Calendário** e **Ano Referencia** devem ser **iguais**;![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046449733)  
- A pergunta **Situação da Decl**. deve ser selecionado o motivo da geração do arquivo, nesse caso devemos informar **2 - Extinção/encerramento de espólio;**- Informe também a **data do evento** (data de encerramento da empresa);  
- **Tipo de evento** nesse caso, somente se for **Saída Definitiva do Pais** ou por **Espólio**;  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045596494)  
  
Lembre de sempre manter seu ambiente devidamente atualizado.  
  
**Saiba Mais**  
[RH-DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF)
