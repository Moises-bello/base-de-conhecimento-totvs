---
article_id: 360038729513
category: RH - Contabilização
content_hash: 73312d13bfb2ec9f1ff8af20f88cfc2636b1e8dc8691e1d1ecfa7a271caeb8e8
fetched_at: '2026-06-28T22:43:45.918159+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Contabilização da folha de pagamento com histórico
  aglutinado
type: support-article
updated_at: '2025-07-17T13:16:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038729513-RH-Linha-Protheus-GPE-Contabiliza%C3%A7%C3%A3o-da-folha-de-pagamento-com-hist%C3%B3rico-aglutinado
---

**Dúvida**Como gerar a contabilização com histórico aglutinado apresentando descrição de verbas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Para gerar a contabilização com histórico aglutinado apresentando a descrição das verbas, configure de acordo com os seguintes passos:   
  
1. Acesse via configurador **Base de Dados -> Dicionário -> Base de Dados -> Parâmetros**:   
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360050162854)

2. Configure os seguintes parâmetros:  
**MV\_AGLHIST** (tipo lógico) com conteúdo = .T.  
Descrição: Indica se considera o histórico dos lançamentos contábeis na aglutinação dos mesmos.  
**MV\_CPOSSRV** (tipo caractere) com conteúdo = S  
No processo de Contabilização da Folha (GPE) posicionar o SRV na verba que está sendo contabilizada.   
**MV\_CPOSLCP** (tipo caractere) com conteúdo = S  
No processo de Contabilização da Folha (GPE) posicionar o arquivo de Lançamento padrão no Lançamento que esta sendo processado  
  
3. Considerando que o lançamento padrão está apontando para as mesmas contas, itens contábeis, basta informar uma expressão no campo "Histórico" para identificação da verba à qual refere-se o lançamento, como por exemplo:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360050163614)  
**Campo Histórico:** "VR REF. " + Alltrim(Posicione("SRV",1,xFilial("SRV")+SRZ->RZ\_PD,"RV\_DESC"))

4. Abaixo , um processamento contábil realizado sem a configuração citada acima e outra configurada para geração das verbas com histórico aglutinado:  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360051063873)  
  
A) Veja que o histórico Lançamento sem a configuração, aglutina todas as verbas do mesmo centro de custos e contas contábeis em 1 único lançamento perdendo a descrição: ![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360050166794)

B) Após a configuração , verificamos que os lançamentos contábeis mantém o mesmo valor para cada centro de custo indicado, porém preserva a descrição de cada lançamento:  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360051063773)

**Saiba Mais:**  
[RH-Contabilização](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109092-RH-Contabiliza%C3%A7%C3%A3o)
