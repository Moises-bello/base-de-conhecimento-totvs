---
article_id: 4409629552663
category: eSocial - Gerar XML/ Integração Evento
content_hash: 6adc1baad90269f3604fd4ef4494d48b5eba9a39c163066533f4b891e5d6b12c
fetched_at: '2026-06-28T22:47:13.182803+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Verbas rescisórias de funcionários sem vínculo empregatício
type: support-article
updated_at: '2026-01-09T11:53:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409629552663-RH-RM-FOP-eSocial-Verbas-rescis%C3%B3rias-de-funcion%C3%A1rios-sem-v%C3%ADnculo-empregat%C3%ADcio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19152495717143) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Em qual evento devem ser geradas as verbas rescisórias de funcionários sem vínculo após a simplificação?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**  
A simplificação do eSocial trouxe uma importante alteração referente a geração das verbas rescisórias de funcionários sem vínculos: a partir do leiaute S-1.0, o grupo **verbasResc** (verbas rescisórias) do evento **S-2399** só deverá ser gerado para funcionários de categoria **721- Contribuinte individual - Diretor não empregado, com FGTS**. Para os demais funcionários sem vínculo, deve-se enviar o **S-2399** sem o grupo **verbasResc** e, as devidas verbas rescisórias serão geradas no **S-1200**/**S-1202**.

Abaixo segue trecho do Manual de Orientações do eSocial da versão S-1.0 sobre o evento S-2399 (página 226):

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409797505303)

Não é necessária nenhuma configuração adicional para geração das verbas nos corretos eventos. O sistema já irá gerar corretamente o grupo **verbasResc** no S-2399 somente para a categoria **721** e irá gerar o S-1200/S-1202 para as demais categorias.  
  
**Saiba mais**  
Para mais informações, acesse:  
     - [Documentação Técnica (Governo)](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)
