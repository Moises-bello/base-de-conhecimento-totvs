---
article_id: 40753244035351
category: TAF - REINF
content_hash: 4a7362dfe973e7717b5c35dce1996781024ba508ba349bb0ce31d96b35fd89b1
fetched_at: '2026-06-28T22:41:33.325777+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Automação Fiscal - Arq. Magnéticos
  - Ao realizar transmissão de um evento a rotina TAFA635, trava no Status como "Solicitado".
type: support-article
updated_at: '2026-05-27T11:57:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40753244035351-Cross-Segmentos-Backoffice-Protheus-Automa%C3%A7%C3%A3o-Fiscal-Arq-Magn%C3%A9ticos-Ao-realizar-transmiss%C3%A3o-de-um-evento-a-rotina-TAFA635-trava-no-Status-como-Solicitado
---

**Ocorrência**  
 Ao realizar transmissão de um evento a rotina TAFA635, trava no Status como "Solicitado".

![Solicitado TAFA635.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40753240060311)  
  
**Ambiente**  
Cross Segmento - TOTVS BackOffice (Linha Protheus) - A partir da versão **12.1.2410**  
  
**Causa**  
 Para normalizar o envio e a atualização dos eventos, siga os passos abaixo:

1. **Ativação do Smart Schedule:**

   * Acesse o módulo **Configurador** (SIGACFG).
   * Navegue pelo caminho: **Ambiente > Schedule**.
   * Localize a configuração do **Smart Schedule** e realize a sua ativação.

![Smart Schedule Ativo.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40753240061591)

**2****. Reenvio do Evento:**

* Após confirmar a ativação do serviço, acesse a rotina **TAFA635**.
* Selecione o evento que apresentou falha e refaça o envio do evento.

**3. Validação do Processamento:**

* Para confirmar o processamento na rotina, utilize a ferramenta de filtro.
* Filtre a visualização pela coluna de **Status** e certifique-se de que a situação do evento foi atualizada com sucesso para **"Enviado"**.

![Filtro Monitor.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40753244026007)

   A transmissão de eventos para a SEFAZ por meio da rotina TAFA635 requer a leitura do parâmetro MV\_SPEDURL. Portanto, é imprescindível assegurar que o serviço do TSS (TOTVS Service SOA) esteja ativo e devidamente parametrizado. Recomendamos a validação prévia destas configurações com base na documentação complementar disponibilizada abaixo.

<https://tdn.totvs.com/display/public/TAF/Monitor+de+Eventos+-+TAF+-+P12>
