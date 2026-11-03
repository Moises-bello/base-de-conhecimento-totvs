---
article_id: 360021560272
category: RH – DIRF
content_hash: 0fabd2a7a08676304d277658866269623c3538feccaa154ff4155966a16380ca
fetched_at: '2026-06-28T22:44:06.828630+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Como conferir os valores da manutenção da DIRF
type: support-article
updated_at: '2025-08-18T12:50:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021560272-RH-Linha-Protheus-GPE-Como-conferir-os-valores-da-manuten%C3%A7%C3%A3o-da-DIRF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34258942619159) Tempo aproximado para leitura: 00:03:00 min**

**Dúvida**Como conferir os valores gerados na manutenção da DIRF?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**1. Realize a manutenção do cadastro de verbas, informado as incidências das verbas para DIRF, para isso, entre na rotina de **Verbas** pelo caminho **>Atualizações >Definições de cálculos >Verbas;**  
  
2. Gere a ficha financeira do funcionário pelo caminho **>Relatórios >Lançamentos >Ficha financeira**, com os parâmetros conforme abaixo  
    2.1. Pergunta "Imp. Incidências?" Informe **Sim**   
    2.2. Pergunta "Incidencias a Impr:" Selecione **1** / **4**  
    2.3. Pergunta "Ficha Financeira" Informe **Data de Pagamento**    2.4. Pergunta "Roteiro" Selecione: **FOL,** **132, PLR, AUT**  
    2.5. Pergunta "Destaca ADI.?" Informe **Sim**  
Verifique na imagem abaixo da ficha financeira que está selecionado a **coluna 1**, ela mostra a **incidência para DIRF configurada no cadastro de verbas:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018566772)**  
  
3. Verifique na Manutenção do Arquivo da DIRF, conforme alguns exemplos abaixo:  
    3.1. Coluna de Rendimentos Tributáveis são os valores das verbas que estão com incidência A (Proventos - Descontos apresentados na ficha financeira e caso o regime da folha seja caixa, a verba de ID 0007 deve ser considerada como desconto de rendimento tributável, pois mesmo com incidência N, esse desconto é tratado internamente na rotina);  
    3.2. Coluna Contrib. Previd. são valores de Inss das verbas que estão com incidência B (Proventos - Descontos apresentados na ficha financeira);  
    3.3. Coluna Imposto de Renda são valores das verbas com incidência D (Proventos - Descontos apresentados na ficha financeira).  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018446471)  
  
  
**Assista o vídeo abaixo onde mostramos passo a passo com explicações de como realizar a conferencia:**-Conferencia dos valores (exceto plano de saúde):   
  
  
  
  
**Saiba Mais**[RH - Linha Protheus - GPE - Para qual coluna é carregado o valor de cada incidência da DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4442685983639-RH-Linha-Protheus-GPE-Para-qual-coluna-%C3%A9-carregado-o-valor-de-cada-incid%C3%AAncia-da-DIRF?source=search)  
[RH - Linha Protheus - GPE - Como conferir valor de adiantamento regime caixa na DIRF com a ficha financeira](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011411822)   
[RH-DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF)
