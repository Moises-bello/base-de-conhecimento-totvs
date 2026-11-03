---
article_id: 13164889191703
category: eSocial - Gerar XML/ Integração Evento
content_hash: 80b5e59c0d715268889ff48e8dc0be6207e1120008199dbf243d604a1a5fafc3
fetched_at: '2026-06-28T22:47:13.098137+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Parametrização de IRRF para envio ao eSocial
type: support-article
updated_at: '2026-05-27T21:18:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13164889191703-RH-RM-FOP-eSocial-Parametriza%C3%A7%C3%A3o-de-IRRF-para-envio-ao-eSocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40782407956119) Tempo aproximado para leitura: **00:02:30 min**  
  
**Dúvida**  
Quais alterações e configurações necessárias para o envio de informação de IRRF ao governo?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões.  
  
**Solução**  
O **Imposto de Renda Retido na Fonte** (IRRF) é enviado para o eSocial, desde o início da sua obrigatoriedade, através da *tag* **codIncIRRF**. Na simplificação do eSocial, iniciada com a liberação do leiaute **S-1.0** o eSocial alterou alguns códigos de incidência de IRRF, passando a trabalhar nessa *tag* com a **Tabela 21 - Códigos de Incidência Tributária da Rubrica para o IRRF**. Além disto, também no **S-1.0** foi descontinuado o retorno do evento totalizador S-5012.

Com a entrada do novo leiaute **S-1.1**, o governo continuou seguindo com o uso da **Tabela 21**, inseriu informações de **Rendimentos Recebidos Acumuladamente** (RRA) em eventos de remuneração e voltou a retornar o evento totalizador **S-5012**.

Abaixo segue documentação sobre os itens supracitados:

* **codIncIRRF** - Códigos de Incidência Tributária da Rubrica para o IRRF  
  [Nota Orientativa nº 06/2021 - Ajuste de incidências de IRRF conforme Tabela 21](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6351933093527-RH-RM-FOP-eSocial-Nota-Orientativa-n%C2%BA-06-2021-Ajuste-de-incid%C3%AAncias-de-IRRF-conforme-Tabela-21?source=search)
* **RRA** - Rendimentos Recebidos Acumuladamente   
  [Rendimentos Recebidos Acumuladamente (RRA)](https://tdn.totvs.com/pages/releaseview.action?pageId=715818269)

**![aten__o_amarelo_02.png](https://centraldeatendimento.totvs.com/hc/article_attachments/13235409234839) A partir da competência (período de apuração) de Maio/2023, ou seja, os eventos enviados até 15 de junho de 2023, o sistema da DCTFWeb realizará a composição dos valores devidos para o IR.**

Para esclarecimento de informações relacionadas a **DCTFWeb**, sugerimos que seja feito contato com o suporte do Governo pelo [Fale Conosco.](https://www.gov.br/esocial/pt-br/canais_atendimento/contato)

**Saiba mais**  
Acesse os *links* abaixo para mais informações:

     - [Espaço Legislação - eSocial](https://espacolegislacao.totvs.com/esocial/)  
     - [Alterações S-1010](https://tdn.totvs.com/pages/releaseview.action?pageId=605863561)  
     - [Webinar Layout S-1.1 - Imposto de Renda + RRA - Documentação PDF](https://espacolegislacao.totvs.com/wp-content/uploads/2023/03/eSocial-IRPF_RM.pdf)  
     - [Webinar Layout S-1.1 - Imposto de Renda + RRA - Vídeo do evento](https://www.youtube.com/watch?v=9dt6-FWYw-k&list=PLXa8l0dq5zRkxpHqPKL7ZVYHt3urJ9VeM&index=1)
