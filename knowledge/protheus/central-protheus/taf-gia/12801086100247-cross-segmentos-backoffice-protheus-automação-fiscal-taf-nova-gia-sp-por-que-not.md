---
article_id: 12801086100247
category: TAF - GIA
content_hash: 9c4f286cd659f9d4fed1ad7a9d79f7b2964fffc5d36acd4629ed8133329f0246
fetched_at: '2026-06-28T22:41:32.352331+00:00'
product: protheus
section_id: 1500001547982
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Automação Fiscal - TAF - Nova GIA-SP
  - Por que nota de serviço tributada pelo ISS é apresentada no arquivo da da GIA-SP?
type: support-article
updated_at: '2023-03-02T17:18:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12801086100247-Cross-Segmentos-Backoffice-Protheus-Automa%C3%A7%C3%A3o-Fiscal-TAF-Nova-GIA-SP-Por-que-nota-de-servi%C3%A7o-tributada-pelo-ISS-%C3%A9-apresentada-no-arquivo-da-da-GIA-SP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**

Por que nota de serviço tributada pelo ISS é apresentada no arquivo da da GIA-SP?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) -TAF – Nova GIA –  A partir da versão 12.1.27

**Solução**

Para solucionar essa dúvida, avalie se o ambiente está configurado conforme passos abaixo:

1. Para que uma nota de serviço não seja considerada na **GIA**, os seguintes campos das tabelas  **SF3/SFT** devem estar preenchidos corretamente:

**F3\_CFO** - CFOP de serviço.

**F3\_CODISS** - Deve estar preenchido com o código relacionado na rotina;

**F3\_TIPO** = S

**F3\_ESPECIE** - Diferente de modelo **55**.

**MATA963** e preenchido no campo **B1\_CODISS**.

Cadastro da **TES,**  tributado de ISS

Calcula ISS - **F4\_ISS** = Sim;

Livro Fiscal ISS - **F4\_LFISS** =  diferente de Não;

Obs: Para nota fiscais de ISS os livros ficais de ICMS  **F4\_LFICM**  = Não, na TES não podem está com classificação fiscal, e  Calcula ICMS **F4\_ICM** , não podem estar como SIM na TES)

Importante: Como o ISS não possui campo próprio para gravação dos valores no livro fiscal, estas informações são gravadas nos campos de ICMS, logo se o relacionamento mencionado acima não for realizado, as notas deste tipo integradas ao **TAF**, obterão o imposto igual a ICMS e não ISS.

2. Para as notas  fiscal tributado de ISS  com os CFOP \*933 só será considerado no arquivo da **GIA** quando a UF se tratar de **DF** e o modelo da nota for 55, conforme consulta realizada na Sefaz.

3. Para não levar as CFOP  final 933 o campo **F3\_ESPECIE** -  deve estar Diferente de modelo 55 **FT/F3\_ESPECIE**  = **SPED**, exemplo  espécie NFS.

As notas fiscais de serviço só será levado e demostrado no arquivo da **GIA-SP**, quando as  notas fiscais  estiverem com  modelo/espécie  55 **FT/F3\_ESPECIE**  = **SPED** quando se tratasse de CFOP 933.

Consultoria de segmentos:

<https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=367241456>

Sefaz-SP:

<https://portal.fazenda.sp.gov.br/servicos/gia/Paginas/perguntas-frequentes.aspx>

Após realizar este processo, refaça a **Apuração do ICMS**, extração e integração para o **TAF**e gere novamente o arquivo da **GIA**.

.
