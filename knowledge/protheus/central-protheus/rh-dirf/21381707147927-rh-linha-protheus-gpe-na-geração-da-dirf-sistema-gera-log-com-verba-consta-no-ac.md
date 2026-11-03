---
article_id: 21381707147927
category: RH – DIRF
content_hash: b90f6839a947dfe02a933269a8bf12f8521dc21b23129904bdb2395c2c65684a
fetched_at: '2026-06-28T22:44:07.063802+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: 'RH - Linha Protheus - GPE - Na geração da DIRF sistema gera log com: Verba
  consta no acumulado, mas não consta no cadastro de verbas'
type: support-article
updated_at: '2024-02-16T11:24:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21381707147927-RH-Linha-Protheus-GPE-Na-gera%C3%A7%C3%A3o-da-DIRF-sistema-gera-log-com-Verba-consta-no-acumulado-mas-n%C3%A3o-consta-no-cadastro-de-verbas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21381698523415) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Na geração da DIRF sistema gera log com: Verba consta no acumulado, mas não consta no cadastro de verbas:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21381707134231)  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Causa**No cadastro de beneficiários existe verba relacionada que não consta no cadastro de Verbas.  
  
**Solução**Na execução da rotina Gerar Arquivo, verifique qual a ultima matricula executada pela barra de processamento:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21381698526871)

Entre na rotina **Beneficiários** pelo caminho **>Atualizações >Funcionários >Beneficiários**, posicione na última matricula processada na rotina Gerar arquivo, clique em **Alterar**, e verifique em todos os campos de verbas, se as verbas relacionadas existem no cadastro de Verbas.  
Caso exista um código que não existe no cadastro de verbas, informe um código válido:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21381707135895)

**Saiba mais**  
Para adquirir maior conhecimento acesse o *link* abaixo  
[RH - Linha Protheus - GPE - Passo a Passo para gerar dados/gerar Arquivo DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020437012)
