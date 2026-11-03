---
content_hash: aca04aa09c02f56e776b1e94da5e600812fd9e09c870e5bbc9e56af56f34d31d
fetched_at: '2026-06-29T00:12:10.105910+00:00'
page_id: '950277578'
product: rm
source: tdn-rm
title: DT - Integração RM X Ahgora - Adequação da Matrícula na Transferência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=950277578
version: 5
---

## **01. DADOS GERAIS**

| Produto: | TOTVS |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: |  |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Integração RM X Ahgora - Adequação da Matrícula na Transferência |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-13808](https://jiraproducao.totvs.com.br/browse/DRHROTRM-13808 "View this issue") |

## **02. LIBERAÇÃO**

**Lembrando que, será a partir dos patches:**

* 12.1.2406.283
* 12.1.2410.244
* 12.1.2502.153 e superiores

## **03. SITUAÇÃO/REQUISITO**

Ao gerar a integração entre a Folha de Pagamento RM e o Ponto Web (Ahgora) para um funcionário com mais de um histórico de transferência, o sistema deve sempre considerar os dados da **última coligada de origem** para compor as informações da transferência.

Ao integrar um funcionário que foi transferido entre coligadas, é apresentada a mensagem de erro: **"1 - O CPF informado é diferente do cadastrado para o funcionário no Pontoweb."**

Esse erro ocorre devido à forma incorreta de geração do campo **matrícula**. O sistema está concatenando o **prefixo da coligada de destino** com a **chapa da coligada de origem**, resultando em uma matrícula inválida no PontoWeb.

**Exemplo:**

* + Coligada de origem: 1 e Chapa: 010106132
  + Coligada de destino: 2 e Chapa: 020104908

**Valor incorreto enviado no campo matrícula:** `2010106132`  
(Coligada destino + chapa da coligada de origem)

**Valor correto esperado:** `1010106132`  
(Coligada origem + chapa da coligada de origem)

## **04. SOLUÇÃO**

Para tratar essa situação, foram adicionados ao produto os campos `CODCOLIGADAANTERIOR`, `CHAPAANTERIOR` e `CODFILIALANTERIOR` na tabela **PINTEGRACAOENVIOAHGORA**.

Com isso, na **primeira integração após a transferência de um funcionário**, as informações da coligada e filial de origem serão enviadas corretamente, conforme exigido para o registro de alteração no sistema **Ponto Web (Ahgora)**.

falseIMPORTANTE:

Para habilitar os novos campos na tabela, é necessária a execução do **RM.Atualizador.exe**.

## **05. DEMAIS INFORMAÇÕES**
