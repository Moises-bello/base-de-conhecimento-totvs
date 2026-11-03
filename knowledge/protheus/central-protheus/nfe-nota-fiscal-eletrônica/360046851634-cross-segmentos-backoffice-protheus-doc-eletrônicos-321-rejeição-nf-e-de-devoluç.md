---
article_id: 360046851634
category: NFe - Nota Fiscal Eletrônica
content_hash: be5b7f34a0c07bc3d081e13a16ba0162da31c89bfd3c3b1e90ae976b3a9ebf21
fetched_at: '2026-06-28T22:40:03.889080+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 321 Rejeição :
  NF-e de devolução de mercadoria não possui documento fiscal referenciado'
type: support-article
updated_at: '2025-06-16T16:57:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046851634-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-321-Rejei%C3%A7%C3%A3o-NF-e-de-devolu%C3%A7%C3%A3o-de-mercadoria-n%C3%A3o-possui-documento-fiscal-referenciado
---

**Dúvida**Como corrigir a rejeição 321 : NF-e de devolução de mercadoria não possui documento fiscal referenciado ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**A rejeição ocorre quando a nota gerou com a TAG **FINNFE = 4** ( devolução), porém não foi referenciado nenhum documento **NF-e, NFC-e, NF modelo 1, NF Produtor, ECF**

* **Conforme o exemplo abaixo:**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360068792173)

* **Lembrando que:**

Não se aplica esta regra para os **CFOP 1.201, 1.202, 1.410, 1.411, 5,921 e 6,921** (NT 2013/005 v 1.20)

1- Verifique se **realmente o CFOP da nota tem finalidade** de devolução:

Ao fazer **nota de devolução** ou **retorno** no sistema é gerada a TAG **FINNFE= 4 (devolução)** para qualquer**CFOP.**

 Porém, quando o **CFOP** não possui a **finalidade de devolução**é necessário gerar a TAG **FINNFE = 1 (normal).**

2. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em **editar**  **MV\_DEVCFOP:** 6910;5910;6211;5211; ***(ponto e vírgula sem espaço) com CFOPS da nota fiscal eletrônica;***

![20220418_113611.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/16593799807127)

3- Após isso, exclua a nota e gere novamente.

4 - Caso o **CFOP realmente tenha finalidade de devolução** verificar se a nota foi referenciada corretamente:

Verificar se a nota foi **referenciada ao documento**de origem corretamente:

D2\_ITEMORI, D2\_SERIORI, D2\_NFORI **(nota de saída)**

![referecia_nt_saida.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/16593774927255)

D1\_ITEMORI, D1\_SERIORI, D1\_NFORI **(nota de entrada)**

**![referecia_nt_entrada.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/16593774929559)**

**Importante:**

Lembrando que a nota só é **referenciada no XML** caso exista no sistema.

Se a mesma for referenciada manualmente deve se preencher os campos **NF . Ori , Serie Ori e Item Ori** .   
Se for preenchido automaticamente pelo gatilho **F4 (Nota de saída) ou F7 (Nota entrada)** os campos são alimentados automaticamente.

3- Verificar  se o campo na TES **F4\_AJUSTE -> Ajuste CIAP = N**, pois se estiver como Sim irá gerar **FINNFE = 3.**

![f4_ajuste_n.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/16593799817367)

4- Após isso, exclua a nota e gere novamente.

Se nota de **beneficiamento** deve ser verificado também:

Para notas que a nota de origem foi realizada como **beneficiamento TES** **poder de terceiro Remessa** e **no retorno** é necessário transmitir como **normal devido a TES ter poder de terceiro como devolução.**

Se nota de **remessa** deve ser verificado também:

Nota de origem **normal com TES poder de terceiro Remessa** ao r**etornar a nota é do tipo beneficiamento com Tes poder de terceiro devolução**.

**Saiba mais:**

É possível consultar a **nota técnica 2013.005\_v\_1.22** página 130 para saber quais são os CFOPs com finalidade de devolução.

<http://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=tW+YMyk/50s=>

5- Após isso, exclua a nota e gere novamente.

6- Caso seja **nota de anulação de frete** realizar o procedimento do link abaixo:

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como emitir nota de anulação de frete](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020130891--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-emitir-nota-de-anula%C3%A7%C3%A3o-de-frete)

7- Caso seja **devolução de importação:**

1- Se a mesma for referenciada manualmente deve se preencher os campos ****NF . Ori , Serie Ori e Item Ori**.**

Se for preenchido automaticamente pelo gatilho ****F4 (Nota de saída)** os campos são alimentados automaticamente.**

**D2\_ITEMORI, D2\_SERIORI, D2\_NFORI (nota de saída)**

2 - Acesse a rotina **Livros Fiscais** -> **Atualizações** -> **Movimentos** -> **NF manual de Saída** -> **Outras ações** ->**Complementos** -> **Exportação**

![20201117_103818.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/16593799820951)

3 - Preencher o campo **CDL\_CHVEXP**  com a chave da **nota de entrada.**

4- E configurar o parâmetro **MV\_DEVCFOP** conforme está no inicio da documentação.

* **Validação da Sefaz:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067678474)
