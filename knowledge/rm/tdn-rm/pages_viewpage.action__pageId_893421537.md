---
content_hash: 1b965529c0aa489f50c63e23311fabf659eab1858537cd6ee1d630e17eb12bef
fetched_at: '2026-06-29T00:12:01.303900+00:00'
page_id: '893421537'
product: rm
source: tdn-rm
title: DT - Fórmula Visual - Função ISFVISUAL - Evento Programado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=893421537
version: 6
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Fórmula Visual |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado): | [DRHROTRM-11767](https://jiraproducao.totvs.com.br/browse/DRHROTRM-11767) |

## **02.** **VERSÕES**

Lembrando que, será a partir dos patches:

* 12.1.2402.249
* 12.1.2406.195
* 12.1.2410.127 e superiores

## **03.** **SITUAÇÃO/REQUISITO**

Ao tentar incluir um evento programado o sistema apresenta o seguinte erro: "**Existe restrição por centro de custo na segurança estendida.**"

## **04.** **SOLUÇÃO**

O processo de **Segurança Estendida** foi descontinuado a partir das versões listadas no TDN, conforme detalhado no link: [TDN - Segurança Estendida Descontinuada](https://tdn.totvs.com/pages/releaseview.action?pageId=271169850).

Essa mudança está causando erros no **DataServer FopEventoProgramadoData**, afetando o funcionamento esperado.  
  
Para corrigir o problema, foi criada a função **ISFVISUAL**. Para garantir que os registros sejam gravados corretamente, é necessário incluir a função **ISFVISUAL** na estrutura da Fórmula Visual.

O ajuste pode ser feito de forma simples, preenchendo o campo **"Dados do Usuário"** nas opções **"Cadastrar Registro"** e **"Salvar Registro"** com a função **ISFVISUAL**.

Para facilitar esse processo, preparamos alguns prints que mostram o passo a passo.

**Passo 1**: Atividade que lê os registros aqui no exemplo nomeada **cadastroRegistro**

É necessário preencher o campo "Dados do Usuário" com valor "ISFVISUAL" na atividade "Ler Registro".

**IMPORTANTE:** A função **ISFVISUAL** só funcionará para o datasever **FopEventoProgramadoData**

**Passo 2**: Atividade irá salvar os dados nomeada **SalvarRegistro**

É necessário preencher o campo **"Dados do Usuário"** com valor **"ISFVISUAL"** na atividade **"Salvar Registro".**

Após salvar, basta executar a fórmula que os dados serão gravados corretamente.

## **05.****DEMAIS INFORMAÇÕES**
