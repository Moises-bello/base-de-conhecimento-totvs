---
content_hash: dc25bfd0deb550e10b0268348d386cbfd091f133d13fdc271b6b5e51ee965023
fetched_at: '2026-06-29T00:09:53.844367+00:00'
page_id: '442045440'
product: rm
source: tdn-rm
title: Como gerar os eventos S-1200 e S-1210 para autônomos cadastrado no módulo de
  Gestão Financeira que tem desconto ISS?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=442045440
version: 13
---

false

**A partir das Versões:**

* + 12.1.22.221
  + 12.1.23.148
  + 12.1.24.000
  + 12.1.25.000

Para realizar a geração dos eventos S-1200 e S-1210 para autônomos do fluxus discriminando o valor de ISS, o usuário deve realizar as seguintes parametrizações:

1.Acesse  RH | Folha de Pagamento | Configurações | Parametrizador | eSocial | Configurações Gerais | Autônomos e Externos e informe o evento previamente cadastrado:

Códigos de calculo para o evento de Desconto ISS:

* [389 - ISS](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.ISS.aspx)

2. Acesse o cadastro de Cliente/Fornecedor e informe os dados do autônomo:

**Observação: a partir da versão 12.1.25.00, será disponibilizado o anexo do eSocial, que irá substituir o item Integrações | eSocial**

3. Acesse Backoffice | Gestão Financeira | Ambiente | Parâmetros | TOTVS Gestão Financeira  | 02.01.01 - Manutenção de Lançamentos | Integração Labore

Vincule qual valor opcional representa o desconto de ISS

3. Antes de realizar a geração dos eventos S-1200 e S-1210, verifique se os lançamentos estão baixados com os valores que serão informados nos respectivos eventos:

4. Execute o processo de Gerar XML com o parâmetro Gerar Autônomos Fluxus/Externos marcado:

Serão gerados os eventos S-1200 e S-1210:
