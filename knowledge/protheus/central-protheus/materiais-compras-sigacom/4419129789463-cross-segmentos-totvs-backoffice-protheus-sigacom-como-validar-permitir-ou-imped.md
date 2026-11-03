---
article_id: 4419129789463
category: Materiais - Compras (SIGACOM)
content_hash: 7067c7b8873f36ea7f6159dd90026f0392d1170748f8dd0d25f9fc5874128199
fetched_at: '2026-06-28T22:41:16.094848+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como Validar / Permitir
  ou Impedir Cadastro de Fornecedores com o mesmo CNPJ / CPF ou repetidos? HELP CGCJAINF
type: support-article
updated_at: '2023-10-19T17:29:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4419129789463-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-Validar-Permitir-ou-Impedir-Cadastro-de-Fornecedores-com-o-mesmo-CNPJ-CPF-ou-repetidos-HELP-CGCJAINF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18402064782615) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como Validar / Permitir ou Impedir Cadastro de Fornecedores com o mesmo CNPJ / CPF ou repetidos?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras - Todas as versões  
  
**Solução**O Cadastro de Fornecedores possui os parâmetros **MV\_VALCNPJ** e **MV\_VALCPF,** podendo parametrizar de modo a Notificar ou Impdir o uso de diferentes cadastros com o mesmo **CNPJ/CPF**

Configurar com um dos seguintes conteúdos:

**1** - Notificar o usuário de que o CNPJ/CPF já existe em outro cadastro, porém permitir o cadastro;

**2** - Impedir o cadastro de registros com o mesmo CNPJ/CPF. Exibindo como resultado o HELP CGCJAINF

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18402064795543)

Importante:

Esta validação não consulta se o Fornecedor cadastrado com o mesmo CNPJ/CPF está bloqueado (Campo MSBQL). Indiferente à esta informação, o parâmetro irá se comportar como indicado acima, ao identificar um registro já gravado na base com o mesmo CPF/CNPJ. Deste modo, verifique se é o caso de remover o conteúdo do campo CNPJ/CPF no cadastro bloqueado, ou se é o caso de utilizar o parâmetro com conteúdo = 1 de modo que não ocorra impedimento em novo cadastro com mesmo CNPJ/CPF.

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
