---
article_id: 360023797612
category: RH – DIRF
content_hash: 7904f2923aa0cf5fbb5f125233010919ed19fec32610c24d2d9f109ba7f15aaa
fetched_at: '2026-06-28T22:44:07.082912+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - O que verificar quando o Sistema não gera a verba
  de pensão 13º salário na DIRF
type: support-article
updated_at: '2025-08-19T19:31:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023797612-RH-Linha-Protheus-GPE-O-que-verificar-quando-o-Sistema-n%C3%A3o-gera-a-verba-de-pens%C3%A3o-13%C2%BA-sal%C3%A1rio-na-DIRF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34299875824791) Tempo aproximado para leitura: **00:01:30 min  
  
Dúvida**O que verificar quando o Sistema não gera a verba de pensão 13º salário na **DIRF**?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**1. Verifique se a verba está com a incidência correta para a **DIRF** na aba **Anuais** da rotina de **Verbas**, para isso, entre na rotina de **Verbas** pelo caminho **>Atualização >Definição de cálculos >Verbas:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11236865631639)**  
  
2. Verifique a verba está no **Acumulado** **(tabela SRD)**, poderá emitir a ficha financeira para conferencia pelo caminho **>Relatórios >Lançamentos >Ficha Financeira;**  
  
3. Verifique o cadastro de **Beneficiários** **(tabela SRQ)**, pelo caminho **>Atualizações >Funcionários >Beneficiários**, se a verba existe no campo **Verba 2a 13º**, caso não exista deverá informar a verba:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11236905802263)  
  
Após ajustes, execute novamente a rotina Gerar Arquivo pelo caminho >Miscelânea >Dirf >Gerar arquivo, para que o sistema alimente a rotina Manutenção de arquivo com os dados de beneficiários e seus valores.

**Saiba mais**  
[RH - Linha Protheus - GPE - Como configurar a Pensão Alimentícia para geração da DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021799651)   
[RH - Linha Protheus - GPE - Passo a Passo para gerar dados/gerar Arquivo DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020437012)

[Página centralizadora Protheus - DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF)
