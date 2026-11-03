---
article_id: 4411458210455
category: MDT - eSocial
content_hash: a3fe9b1e38ca7c423038159c0ab0604b48b1490e1c9c5f32732239a243541078
fetched_at: '2026-06-28T22:44:29.249741+00:00'
product: protheus
section_id: 360004428991
source: central-protheus
title: 'RH - Linha Protheus - MDT - eSocial - Ao tentar gerar eventos SST no modulo
  SIGAMDT o sistema apresenta o aviso: "Os funcionários abaixo não foram comunicados
  devido estarem em admissão preliminar e o leiaute ser anterior a versão S-1.0"'
type: support-article
updated_at: '2025-08-05T17:10:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411458210455-RH-Linha-Protheus-MDT-eSocial-Ao-tentar-gerar-eventos-SST-no-modulo-SIGAMDT-o-sistema-apresenta-o-aviso-Os-funcion%C3%A1rios-abaixo-n%C3%A3o-foram-comunicados-devido-estarem-em-admiss%C3%A3o-preliminar-e-o-leiaute-ser-anterior-a-vers%C3%A3o-S-1-0
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30372483486999)** Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao tentar gerar eventos SST no modulo Medicina e Segurança do Trabalho o sistema apresenta o aviso: "Os funcionários abaixo não foram comunicados devido estarem em admissão preliminar e o **leiaute ser anterior a versão S-1.0**".  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Causa**Os funcionários que estão em admissão preliminar (**S-2190**) no leiaute anterior ao **S-1.0** simplificado, não possuem **algumas informações comunicadas ao Governo**. Um exemplo é a tag <**matricula**> do evento S-2190 que não existe no **leiaute 2.5,** e como é uma tag necessária para a comunicação dos eventos de SST, não se torna possível realizar o envio. Caso o leiaute esteja definido na versão S-1.0 simplificada, o envio poderá ocorrer normalmente visto que a tag <matricula> existe para esse cenário..  
  
**Solução**

* Verifique se existe o S-2190 gerado no leiaute 2.5 (layout), caso exista será necessario gerar o S-2200 e transmitir ao governo para prosseguir com os eventos SST.
* Caso o S-2190 já tenha sido gerado no leiaute **S-1.0** (layout) esse erro não vai ocorrer.

**Observação**  
Link: **[Condições em que os Eventos de SST não serão Enviados ao Governo](https://tdn.totvs.com/x/FE9uJQ)**  
Em caso de duvidas na geração dos eventos temos vídeos de exemplo: **[RH - Linha Protheus - MDT - eSocial - Existe vídeos com o passo a passo de geração dos eventos SST (Medicina e Segurança do Trabalho) no eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410314804631)**  
 **Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
