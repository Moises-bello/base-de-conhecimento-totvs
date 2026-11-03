---
article_id: 1500006358681
category: Financeiro - Serasa
content_hash: 6745e59b49e36449c04075776a2f020ae7a82a1690e3096382197df60d31d0ee
fetched_at: '2026-06-28T22:37:28.255966+00:00'
product: protheus
section_id: 35058289522071
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAFIN -FINA770 - Como a rotina
  do Serasa grava na tabela FWB as ocorrências: 1 Selecionado Serasa, 2 Enviado Serasa,
  3 Reg. Incluído'
type: support-article
updated_at: '2026-01-30T12:38:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006358681-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA770-Como-a-rotina-do-Serasa-grava-na-tabela-FWB-as-ocorr%C3%AAncias-1-Selecionado-Serasa-2-Enviado-Serasa-3-Reg-Inclu%C3%ADdo
---

**Dúvida**  
Como a rotina do Serasa grava na tabela FWB as ocorrências: 1 Selecionado Serasa ,2 Enviado Serasa,  
3 Reg. Incluído?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA770 - A partir da versão 12.0

**Solução**  
1  - Faça a preparação para gerar o arquivo de títulos do cliente ao Serasa pela rotina **FINA770**, neste momento o sistema grava na **FWB - 1 Selecionado Serasa**.  
  
2 - Depois em seguida a geração do arquivo de envio para Serasa pela rotina **FINA770**, neste momento o sistema grava na **FWB - 2 Enviado SERASA**.  
  
3 - Então deve mandar para Serasa o arquivo e depois de 1 dia, vem o retorno com a confirmação que foi aceito título deste cliente, ao efetuar baixa deste retorno pela rotina **FINA770**, neste momento o sistema vai gravar **FWB - 3 Reg. Incluído**.

Saiba mais:

[SIGAFIN - SERASA - Layouts de envio e retorno utilizando MILE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026466172-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-SERASA-Layouts-de-envio-e-retorno-utilizando-MILE?utm_source=chatgpt.com)

[SIGAFIN - Para utilizar as rotinas FINA770 e FINA771, precisa contratar os serviços do Pefin junto ao Serasa Experian para fazer a integração com o Protheus através dos arquivos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011492942-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Para-utilizar-as-rotinas-FINA770-e-FINA771-precisa-contratar-os-servi%C3%A7os-do-Pefin-junto-ao-Serasa-Experian-para-fazer-a-integra%C3%A7%C3%A3o-com-o-Protheus-atrav%C3%A9s-dos-arquivos?utm_source=chatgpt.com)

[SIGAFIN - FINA770 - HELP: F771RETMANU](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007183821-Cross-segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA770-HELP-F771RETMANU?utm_source=chatgpt.com)

[SERASA - Layouts de envio e retorno utilizando MILE](https://tdn.totvs.com.br/display/public/PROT/SERASA+-+Layouts+de+envio+e+retorno+utilizando+MILE)
