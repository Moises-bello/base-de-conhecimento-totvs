---
article_id: 360033671474
category: RH – DIRF
content_hash: a392317f662d95f5538ce69571965b4081cb484b216526b387f5a31a16b9b778
fetched_at: '2026-06-28T22:44:06.761981+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Ao importar o arquivo da DIRF no validador, é gerado
  erro BPFDEC ERRO Nome com apenas uma parte deve conter no mínimo duas letras
type: support-article
updated_at: '2025-08-06T20:46:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033671474-RH-Linha-Protheus-GPE-Ao-importar-o-arquivo-da-DIRF-no-validador-%C3%A9-gerado-erro-BPFDEC-ERRO-Nome-com-apenas-uma-parte-deve-conter-no-m%C3%ADnimo-duas-letras
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33998914337559) Tempo aproximado para leitura: 00:01:00 min**

**Ocorrência**Ao importar o arquivo da DIRF no validador, é gerado erro **BPFDEC ERRO Nome com apenas uma parte deve conter no mínimo duas letras  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21026388680855)****Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões.  
  
**Causa**  
Preenchimento incorreto no campo Nome Completo no cadastro do funcionário.  
  
**Solução**1. Identifique a linha no log que o sistema gera o erro:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21026388685207)

2. Abra o arquivo e localize a linha do erro, neste bloco teremos na seguinte sequencia: Identificador do registro (BPFDEC), CPF, nome, exemplo: **BPFDEC|CPF|nome|**

Neste momento será possível identificar se o nome esta correto, neste exemplo o campo nome consta um **"A":  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21026424883991)**

3. Entre no cadastro de Funcionários pelo caminho **Atualização / Funcionários / Funcionários**;

4. Verifique o campo **Nome Complet "RA\_NOMECMP"**, se este campo estiver com algum conteúdo, sistema buscará a informação deste campo, se necessário, faça o ajuste informando o nome completo do funcionário:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21026388695831)

5. Após ajuste, gere novamente a rotina Gerar Arquivo para a matricula em questão, assim ao gerar o arquivo magnético, a informação será gerada de forma correta.  
  
  
**Saiba Mais**  
[RH - Linha Protheus - GPE - Passo a Passo para gerar dados/gerar Arquivo DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020437012)   
[RH - Linha Protheus - GPE - Passo a Passo para geração do Arquivo magnético da DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022076092)
