---
article_id: 360043508233
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: 4c0d1331bf749e480a824e63bbcfc34ed5eba7c2100b8cf6d77c5e058e18cc19
fetched_at: '2026-06-28T22:45:21.138327+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Configuração - Como realizar a amarração
  pela rotina do Complemento Cadastral  - Amarração 1:1
type: support-article
updated_at: '2024-05-29T14:13:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043508233-RH-Linha-Protheus-TAF-eSocial-Configura%C3%A7%C3%A3o-Como-realizar-a-amarra%C3%A7%C3%A3o-pela-rotina-do-Complemento-Cadastral-Amarra%C3%A7%C3%A3o-1-1
---

**Dúvida**Qual a configuração correta para o Complemento Cadastral (TAFA050) quando é utilizado a amarração de 1:1?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Configuração - Todas as versões

**Solução**

O cliente pode utilizar o TAF para realizar a integração de diversas obrigações ao governo, como por exemplo eSocial e Reinf.   
  
No caso do cadastro de complemento ser novo, o cliente deverá utilizar a amarração de 1:1.

A amarração de 1x1 atende o e-Social e o REINF, e deverá ser configurada conforme exemplo abaixo:

**Exemplo com 1 empresa matriz:**

A Matriz e filiais devem ser cadastradas no complemento cadastral.

**Grupo de empresas: 01**

Acesse o complemento cadastral da empresa Matriz e verifique se o campo "Matriz" está selecionado.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057987274)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057987334)

Quando existe somente uma empresa Matriz, a aba "Outras Filiais" não deve ser preenchida.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058890793)

**Exemplo com 2 empresas Matriz e filial:**

**Grupo de empresas: 01**

No complemento Empresa são cadastradas todas as Empresas/Filiais, no cadastro da Empresa Matriz é marcado o campo “Matriz”, e na aba outras filiais deve ser informado somente o código da Empresa/filial selecionada.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058890313)

Para maiores informações ou dúvidas, consulte a documentação abaixo no TDN:

<https://tdn.totvs.com/display/public/TAF/Complemento+de+Empresa+-+TAFA050+-+TAF+-+P12>
