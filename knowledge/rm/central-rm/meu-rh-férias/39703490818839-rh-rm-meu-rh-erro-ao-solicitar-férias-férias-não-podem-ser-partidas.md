---
article_id: 39703490818839
category: Meu RH - Férias
content_hash: 740ae8c05e3169ff94268932ffdd78771cf97027c71154f654d1619195bea9e7
fetched_at: '2026-06-28T22:47:31.590371+00:00'
product: rm
section_id: 1500000835241
source: central-rm
title: 'RH - RM - Meu RH - Erro ao solicitar férias: "Férias não podem ser partidas"'
type: support-article
updated_at: '2026-04-13T13:23:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39703490818839-RH-RM-Meu-RH-Erro-ao-solicitar-f%C3%A9rias-F%C3%A9rias-n%C3%A3o-podem-ser-partidas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39703490798615) Tempo aproximado para leitura: **00:01:00min**  
  
**Ocorrência**  
Ao realizar solicitação de férias pelo Meu RH, é retornando a mensagem de erro: "Férias não podem ser partidas".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39703490799383)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) – Meu RH – Todas as versões   
  
**Causa**  
Esse erro ocorre, quando a parametrização do grupo de quiosque não está habilitado a solicitação de férias partidas.  
  
**Solução**  
Para habilitar as férias partidas, acesse o módulo **Folha de pagamento > Configurações > Parametrizador > RM Portal >** Edite o quiosque do funcionário > **Ferias II.** Realize as seguintes parametrizações:

* Marque o parâmetro: Permite cadastrar férias partidas
* n° máximo de períodos para férias partidas: **3**
* n° min. de dias de férias p/férias partidas: **5**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39703526371351)

Após realizar esta parametrização, será possível realizar a solicitação de férias partidas pelo Meu RH em até 3 períodos. Por padrão, o Meu RH irá obrigar em um dos períodos ter pelo menos 14 dias conforme as normas da reforma trabalhista.

**Saiba Mais:**  
[RH - RM - Meu RH - Como realizar solicitação de férias via app Meu RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029306971-RH-RM-Meu-RH-Como-realizar-solicita%C3%A7%C3%A3o-de-f%C3%A9rias-via-app-Meu-RH)
