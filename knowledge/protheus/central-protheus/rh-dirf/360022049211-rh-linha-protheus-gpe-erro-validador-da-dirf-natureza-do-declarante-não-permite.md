---
article_id: 360022049211
category: RH – DIRF
content_hash: 89b8ee538bcf94d141a0f812797741edc64fd6a861016ab9367a58d542928f4b
fetched_at: '2026-06-28T22:44:07.904326+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: 'RH - Linha Protheus - GPE - Erro validador da DIRF: natureza do declarante
  não permite que a instituição seja fundação pública de direito privado'
type: support-article
updated_at: '2025-08-19T20:45:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022049211-RH-Linha-Protheus-GPE-Erro-validador-da-DIRF-natureza-do-declarante-n%C3%A3o-permite-que-a-institui%C3%A7%C3%A3o-seja-funda%C3%A7%C3%A3o-p%C3%BAblica-de-direito-privado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34302252266647)** Tempo aproximado para leitura: **00:01:00 min  
  
Ocorrência**Ao importar o arquivo magnético para o PGD, o validador gera o log de ocorrências informando que a **Natureza do declarante não permite que a instituição seja fundação pública de direito privado instituída pela União, pelos Estados/Distrito Federal ou pleos Municípios**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018924412)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**Esse erro ocorre porque na geração do arquivo magnético (GPEM590), a pergunta **Fund. Publ. de Dir. Privado?** Está com conteúdo **SIM,** porém a empresa não é uma Fundação Pública de Direito Privado.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o menu **Arquivo Magnético** pelo caminho **>Miscelânea >Dirf >Arquivo magnético**;  
2. Altere o conteúdo da pergunta **Fund. Publ. de Dir. Privado?** para **Não  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11182348895255)**  
3. Confirme a geração do arquivo;  
4. Importe novamente para o PGD.  
  
**Saiba mais**  
[RH - Linha Protheus - GPE - Passo a Passo para geração do Arquivo magnético da DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022076092)   
[RH - Linha Protheus - GPE - De onde o Sistema busca as informações do bloco DECPJ](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4470748266775)
