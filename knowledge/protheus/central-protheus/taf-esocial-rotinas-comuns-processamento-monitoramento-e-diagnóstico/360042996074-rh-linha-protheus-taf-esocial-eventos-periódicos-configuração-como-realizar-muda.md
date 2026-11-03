---
article_id: 360042996074
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: 209b57b5947af3a6026c7dbd4fe5c3c9a19c677aaf5c9bbffd82e8bc0704bd7c
fetched_at: '2026-06-28T22:45:21.157385+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Eventos Periódicos - Configuração - Como
  realizar mudança da de amarração de 1:N para 1:1 via rotina Complemento Cadastral
type: support-article
updated_at: '2024-05-29T14:09:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042996074-RH-Linha-Protheus-TAF-eSocial-Eventos-Peri%C3%B3dicos-Configura%C3%A7%C3%A3o-Como-realizar-mudan%C3%A7a-da-de-amarra%C3%A7%C3%A3o-de-1-N-para-1-1-via-rotina-Complemento-Cadastral
---

**Dúvida**

Qual a configuração correta para o Complemento Cadastral (TAFA050) quando eu utilizo a amarração de 1:N e preciso entregar o REINF que utiliza 1:1?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Configuração - Todas as versões  
  
**Solução**

**O cliente pode utilizar o TAF para realizar a integração de diversas obrigações ao governo, como por exemplo eSocial e Reinf. No caso do eSocial se ele optou por centralizar dados de diversas filiais em uma centralizadora (N:1), e precisa entregar o REINF, o complemento deverá ser ajustado da seguinte maneira:**

Criar o parâmetro MV\_TAFCFGE e deixa-lo como .T., segue link de como cria-lo:

<http://tdn.totvs.com/pages/releaseview.action?pageId=455804537>

Na rotina de complemento cadastral, deverá ser criado um registro para cada matriz e filial existentes:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057989214)

O complemento cadastral da empresa Matriz deverá estar com o campo "Matriz" selecionado.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23701993553815)

O campo **"Cod Filial",** deverá ser preenchido com Grupo+Filial, exemplo 0107.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058876053)

**Exemplo:**

No arquivo sigamat.emp esta empresa é apresentada da seguinte maneira:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058876313)

Para maiores informações ou dúvidas, consulte a documentação abaixo no TDN:

<https://tdn.totvs.com/display/public/TAF/Complemento+de+Empresa+-+TAFA050+-+TAF+-+P12>
