---
article_id: 360059316853
category: RH - FGTS / SEFIP
content_hash: 86645c85a99d5cc6e1a38426c5958732c801529e3a46791d065dbcd608060f19
fetched_at: '2026-06-28T22:43:41.148202+00:00'
product: protheus
section_id: 360003115651
source: central-protheus
title: 'RH - Linha Protheus - GPE - Ao enviar a SEFIP apresenta o seguinte erro  100010
  : Nome do logradouro inválido, o campo está vazio'
type: support-article
updated_at: '2026-06-26T18:25:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059316853-RH-Linha-Protheus-GPE-Ao-enviar-a-SEFIP-apresenta-o-seguinte-erro-100010-Nome-do-logradouro-inv%C3%A1lido-o-campo-est%C3%A1-vazio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34708711580439) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
Ao enviar a SEFIP apresenta o seguinte erro: 100010-Nome do logradouro inválido. O campo está vazio, contém caracteres especiais, a primeira posição não é válida, existe mais de um espaço entre as palavras ou, ainda, três ou mais caracteres iguais e consecutivos.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da versão 12.1.17.

**Causa**  
Esse erro ocorre pois no cadastro da Filial o endereço está preenchido de forma errada.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500013518061)  
1. Acesse a rotina **Filial**-**CFGX032** via **Configurador-SIGACFG** pelo caminho >**Ambientes** >**Empresas** >**Filial**;

2. Clique em alterar;  
3. Na Aba **Endereço Cobrança** faça as verificações conforme a mensagem:  
**Nome do logradouro inválido. O campo está vazio, contém caracteres especiais, a primeira posição não é válida, existe mais de um espaço entre as palavras ou, ainda, três ou mais caracteres iguais e consecutivos.;**  
4. Após ajuste, gere novamente a SEFIP e importe no validador.

**Saiba Mais**  
[RH - Linha Protheus - GPE - Como gerar o arquivo da Sefip](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008703402)
