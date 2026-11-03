---
article_id: 360051642154
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 44c8cdaf27f115f11c10bb4fa661ab67028c806a945702a72ae04f2aa6954708
fetched_at: '2026-06-28T22:39:58.586931+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - TSS: Rejeição
  1 - {ERRO} Problemas durante a transmissao dos dados (Lençóis Paulista)'
type: support-article
updated_at: '2021-10-06T19:08:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051642154-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-TSS-Rejei%C3%A7%C3%A3o-1-ERRO-Problemas-durante-a-transmissao-dos-dados-Len%C3%A7%C3%B3is-Paulista
---

**Ocorrência**Ao realizar a transmissão de um RPS para a prefeitura de Lençóis Paulista ocorre a rejeição abaixo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082943953/mceclip0.png)  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Causa**Esse erro ocorre por conta do parâmetro **MV\_SEQ** na **SPED000** da entidade em questão possuir um conteúdo inválido (carácter), onde de acordo com a prefeitura **deverá ser numérico**.  
  
Se observar o conteúdo completo da rejeição através do XML\_RET da SPED053 terá a seguinte mensagem:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082946013/mceclip1.png)  
  
*Obs.: Utilizado o parâmetro MV\_SEQ = W para o teste acima, onde ocorre a rejeição.*  
  
**Solução**Verificar se não possui um conteúdo **carácter** dentro do parâmetro MV\_SEQ, caso tenha, solicitar junto a prefeitura qual deverá ser a próxima **numeração** correta a ser utilizada e corrigir o campo.  
Detalhes: [clique aqui (Página 69)](https://apl2.lencoispaulista.sp.gov.br/nfs/Downloads/WebService-V1.1.pdf)
