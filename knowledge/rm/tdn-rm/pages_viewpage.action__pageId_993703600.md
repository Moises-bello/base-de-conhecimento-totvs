---
content_hash: b2b57ae1f78b6351e4c885afe54a71f9d1adc86fdf0cad90fe39de3aacecda8f
fetched_at: '2026-06-29T00:12:16.560668+00:00'
page_id: '993703600'
product: rm
source: tdn-rm
title: API REST - recordClockMarkings/integracaobatidas (v2)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=993703600
version: 29
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | RM |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Função: | Integração de marcações em lote via API REST |
| País: | Brasil |
| Requisito/Story/Issue: | [DRHJORNRM-8632](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-8632), [DRHJORNRM-8936](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-8936)  e [DRHJORNRM-8937](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-8937) |

## **02. SITUAÇÃO/REQUISITO**

Permitir que as marcações vindas do Suricato ou PontoWeb sejam inseridas em lote na tabela **AINTEGRACAOBATIDAS**.

## **03. SOLUÇÃO**

Foi criada uma nova API: **v2/recordClockMarkings/integracaobatidas** para atender a integração de marcações em lote.

## **04. VERSÕES**

* 12.1.2510.153 e superiores.
* 12.1.2506.223
* 12.1.2502.263

## **05. UTILIZAÇÃO**

**Como realizar a chamada da API REST**

**Endpoint:**

* Deve ser configurado da seguinte forma:

  bashConfluence

  Lembrando que o ***host*** e a ***porta*** devem ser configurados de acordo com o ambiente utilizado.
* Exemplo de endpoint configurado corretamente:

  bashConfluence

11PontoWeb

**Método:**

* O método disponibilizado pela API é ***POST***, sendo obrigatório o preenchimento do corpo ***(body)***. Segue exemplo de como enviar o ***body:***

  bashConfluenceBody

**Resposta:**

* O retorno da API será em **JSON**. Segue exemplo de resposta:

  bashConfluenceResponseImportante

  Uma marcação com dados errados ou incompletos não impede que outras marcações corretas sejam integradas. O motivo do erro será retornado na resposta da chamada, na propriedade **"message"**.
2Suricato

**Método:**

* O método disponibilizado pela API é ***POST***, sendo obrigatório o preenchimento do corpo ***(body)***. Segue exemplo de como enviar o ***body:***

  bashConfluenceBody

**Resposta:**

* O retorno da API será em **JSON**. Segue exemplo de resposta:

  bashConfluenceResponse

**Mensagens de Erro:**

,,falseSparklinetruefalsetruefalsefalsefalsefalsefalse1768394070400\_1928249650falsestatus ⇧falsePoint (.)dd/mm/yyfalse365|5|8|y w d h m|y w d h mAND

| status | errorCode | message |
| --- | --- | --- |
| 200 |  | "Gravação efetuada com sucesso." |
| 400 | "00001" | "PIS em formato inválido ou inexistente no cadastro." |
| 400 | "00001" | "CPF em formato inválido ou inexistente no cadastro." |
| 400 | "00002" | "NSR duplicado. Número já foi importado na tabela" |
| 400 | "00002" | "NSR duplicado. Número já foi importado no codRep informado." **Obs: (Essa validação só é feita se o campo "CodRelogioExtChave" estiver com o valor PONTOWEB )** |
| 400 | "00003" | "NSR não foi informado e é obrigatório" |
| 400 | "00006" | "Não foi informado o campo obrigatório: CodRelogioExtChave" |
| 400 | "00006" | "Não foi informado o campo obrigatório: codFuncMsa" |
| 400 | "00006" | "Não foi informado o campo obrigatório: numHorarMarcacAces" |
| 400 | "00006" | "Código do REP é obrigatório" |
| 400 | "00006" | "Não foi informado o campo obrigatório: codUsuarExtChave" |
| 400 | "00006" | "Data da marcação é obrigatória" |
| 400 | "00006" | "Campo 'datMarcacAces' no formato incorreto. Deve ser preenchido como data." |
| 400 | "00006" | "Tamanho do campo InscrEmp inválido. O campo permite a quantia de caracteres 11 ou 14 apenas." |
| 400 | "00006" | "Campo codRelogioExtChave no formato inválido. Deve ser preenchido para o Suricato: Coligada;Código do Terminal de Coleta ou para Ahgora: PONTOWEB." |
| 400 | "00006" | "Não foi informado o campo obrigatório: InscrEmp." **Obs: (Essa validação só é feita se o campo "CodRelogioExtChave" estiver com o valor PONTOWEB )** |
| 400 | "00006" | "Tamanho do campo codCCT inválido, o campo permite no mínimo 0 e máximo 17 caracteres" |
| 400 | "00006" | "Tamanho do campo codFuncMSA inválido, esse dado permite no máximo 100 caracteres." |
| 400 | "00006" | "Tamanho do item codFuncMSA com valor *valorExemplo* inválido, esse dado permite no máximo 16 caracteres." |
| 400 | "00006" | "Tamanho do campo codUsuarExtChave inválido, esse dado permite no máximo 100 caracteres." |
| 400 | "00006" | "O primeiro valor *valorExemplo*do item codUsuarExtChave é inválido, esse valor permite no máximo 5 caracteres." |
| 400 | "00006" | "O segundo valor *valorExemplo* do item codUsuarExtChave é inválido, esse valor permite no máximo 16 caracteres." |
| 400 | "00007" | "Terminal de coleta não está cadastrado no ERP." |
| 400 | "99999" | "Erro interno na tabela. Registro não foi gravado." |

,,falseSparklinetruefalsetruefalsefalsefalsefalsefalse1768394073351\_1928249650falsestatus ⇧falsePoint (.)dd/mm/yyfalse365|5|8|y w d h m|y w d h mAND

**Exemplos de retorno da requisição com erro:**

jfx0Tamanho do campo codFuncMSA inválido, esse dado permite no máximo 100 caracteres.truejfx0Tamanho do item codFuncMSA com valor valorExemplo inválido, esse dado permite no máximo 16 caracteres.truejfx0Tamanho do campo codUsuarExtChave inválido, esse dado permite no máximo 100 caracteres.truejfx0O primeiro valor valorExemplo do item codUsuarExtChave é inválido, esse valor permite no máximo 5 caracteres.truejfx0O segundo valor valorExemplo do item codUsuarExtChave é inválido, esse valor permite no máximo 16 caracteres.true

## **06. ASSUNTOS RELACIONADOS**

**[Campos da API recordClockMarkings/integracaobatidas](https://tdn.totvs.com/display/LRM/Campos+da+API)**
