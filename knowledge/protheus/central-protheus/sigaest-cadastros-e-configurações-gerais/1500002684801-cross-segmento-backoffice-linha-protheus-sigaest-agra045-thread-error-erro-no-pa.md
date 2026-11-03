---
article_id: 1500002684801
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 727691f5c444f6d9b6ca250485f23a69c7bdc9b55692612597d2584864957c0c
fetched_at: '2026-06-28T22:39:09.761898+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST- AGRA045 - THREAD ERROR
  - Erro no parâmetroFWFormGridModel: A linha 0 é inválida !!! on FWFORMGRIDMODEL:GETVALUE(FWFORMGRIDMODEL.PRX)'
type: support-article
updated_at: '2025-12-18T19:16:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002684801-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-AGRA045-THREAD-ERROR-Erro-no-par%C3%A2metroFWFormGridModel-A-linha-0-%C3%A9-inv%C3%A1lida-on-FWFORMGRIDMODEL-GETVALUE-FWFORMGRIDMODEL-PRX
---

O erro "THREAD ERROR - Erro no parâmetroFWFormGridModel" ao clicar em "Altera" no Cadastro de Locais de Estoque (AGRA045) é resolvido alterando o campo X3\_RELACAO da tabela SGQ no campo GQ\_DESCLOC, substituindo a fórmula antiga pela nova com FBUSCACPO. É necessário backup e homologação, e o armazém deve estar cadastrado na tabela NNR.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37126957919767) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Ao clicar no botão "Altera" no Cadastro de Locais de Estoque (AGRA045) ocorre o seguinte error.log: "*THREAD ERROR - Erro no parâmetroFWFormGridModel: A linha 0 é inválida !!! on FWFORMGRIDMODEL:GETVALUE(FWFORMGRIDMODEL.PRX)*"

O que fazer para resolvê-lo?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) -Estoque/Custos - Todas as versões.  
  
**Solução**

Para resolver este problema, altere o campo **X3\_RELACAO** da tabela **SGQ**do campo **GQ\_DESCLOC** com este conteúdo abaixo:

*DE:*

**If(!INCLUI,Posicione("NNR",1,xFilial("NNR")+FwFldGet("GQ\_LOCAL"),"NNR\_DESCRI"),"")**

*PARA:*

**IIF(!INCLUI,FBUSCACPO("NNR",1,XFILIAL("NNR")+SGQ->GQ\_LOCAL,"NNR\_DESCRI")," ")**

**Observações**

- Efetue sempre um Backup do seu repositório (RPO) antes da aplicação e realize o ajuste primeiramente em ambiente de homologação;

- É importante ressaltar que o armazém precisa também estar cadastrado na tabela NNR.

**Saiba mais:**

[*MP - SIGAEST - AGRA045 - Como bloquear armazém para movimentações?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022132132-MP-SIGAEST-AGRA045-Bloquear-Armaz%C3%A9m-para-movimenta%C3%A7%C3%A3o-)

[*Clique aqui e veja mais artigos sobre Cadastros no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIShttps://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
