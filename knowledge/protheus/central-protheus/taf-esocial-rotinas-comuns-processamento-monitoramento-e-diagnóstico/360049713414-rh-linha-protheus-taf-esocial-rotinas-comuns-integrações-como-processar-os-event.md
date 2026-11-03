---
article_id: 360049713414
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: 5b23e56a98939b3313db644a7f1e53154a33fd18961ab47401ccfb389266f15d
fetched_at: '2026-06-28T22:45:21.021835+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Rotinas Comuns  - INTEGRAÇÕES - Como
  processar os eventos e verificar os status no Gerenciador de Integração
type: support-article
updated_at: '2024-09-24T14:44:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049713414-RH-Linha-Protheus-TAF-eSocial-Rotinas-Comuns-INTEGRA%C3%87%C3%95ES-Como-processar-os-eventos-e-verificar-os-status-no-Gerenciador-de-Integra%C3%A7%C3%A3o
---

**Dúvida**

Ao realizar integração do ERP (RM ou Datasul) para o TAF (Segregado) como faço para verificar os *status* no Gerenciador de Integração no TAF?

**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Rotinas Comuns - Integrações - Todas as versões

**Solução**

1 - Acesse o SIGATAF e certifique-se que está na filial correta para realizar o processamento dos eventos, e vá nas opções do menu Miscelânea ► Integração ► Processamentos:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26588781150871)

2 - Verifica se os parâmetros do processamento estão de acordo com as premissa abaixo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076208833)

**Obs.:** Importante ressaltar que se o tipo de escopo estiver marcado como **Fiscal/Contábil**, o registro não será processado para o **e-Social**. Outro detalhe que o botão validar base no TAF foi desativado momentaneamente em consequência da transição dos layouts 2.5 para o S-1.0.

3 - Se as premissas estiverem de acordo com os parâmetros acima e a mensagem do processamento ainda estiver, "Não há registros passíveis de processamento" ou por ventura, não executar nenhuma ação, acesse o Gerenciador de Integrações;

4 - Para acessar o gerenciador de integração, utilize o menu Miscelânea ► Integração ► Gerenciador de Integração:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076209093)

5 - Selecione um período que abranja a data de envio dos eventos ao TAF, em caso de dúvida, insira a data início igual a 01/10/1900 e data fim igual a 01/01/2021 e o escopo a ser apresentado: eSocial e clique em "Confirmar":

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074999754)

6 - Na próxima janela selecione as filias e clique em "OK":

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076209133)

7 - Nessa tela clique em visão individualizada e selecione o layout do evento na direita e busque pelo numero da mensagem no TAF.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076209193)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076209253)

8 - Verifique os status deste registro e veja se o mesmo foi integrado ao TAF com sucesso;

9 - Legenda de status no Gerenciador de Integração:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7857769801751)
