---
article_id: 16980044203415
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: b0df2eecb188a4a5eb18fa3f41af631363b396689b4a27d9b3936bb5eb25b167
fetched_at: '2026-06-28T22:42:40.897476+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Bloco K230 mostra a mensagem Somente
  pode ser informado nesse campo um valor de COD_ITEM cujo campo TIPO_ITEM do Registro
  0200 seja igual a 03 ou 04
type: support-article
updated_at: '2023-08-23T19:07:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16980044203415-Manufatura-Linha-Protheus-SIGAPCP-Bloco-K230-mostra-a-mensagem-Somente-pode-ser-informado-nesse-campo-um-valor-de-COD-ITEM-cujo-campo-TIPO-ITEM-do-Registro-0200-seja-igual-a-03-ou-04
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16980000316055) Tempo aproximado para leitura: **00:00:45 min  
  
Ocorrência**Ao gerar o arquivo do **SPED** é apresentado a mensagem **Somente pode ser informado nesse campo um valor de COD\_ITEM cujo campo TIPO\_ITEM do Registro 0200 seja igual a 03 ou 04, no K230 - Itens Produzidos**. **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**  
A mensagem é exibida quando um dos produtos produzidos relacionados à **OP - Ordem de Produção**, não são do tipo 03 ou 04, conforme indicado nos parâmetros **MV\_BLKTP03 - Tipo de produto para definição do Bloco K produto em processo** e **MV\_BLKTP04 - Tipo de produto para definição do Bloco K produto acabado**.  
  
**Solução**É preciso avaliar o produto produzido com essa **OP**, já que somente **OP's** que deram entrada no estoque de produtos do tipo 03 ou 04 devem ser listadas no **K230**.  
  
**Saiba mais**Para mais informações sobre o Bloco K230, acesse o link [Registro K230: Itens Produzidos](https://tdn.totvs.com/display/public/PROT/Registro+K230%3A+Itens+Produzidos)
