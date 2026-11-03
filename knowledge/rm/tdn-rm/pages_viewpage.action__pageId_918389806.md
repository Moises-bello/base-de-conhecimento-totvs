---
content_hash: 98ec190bdc3ab841a8186c1798ca71d32022c8b33b8ede32ed77b2c97e7f99de
fetched_at: '2026-06-29T00:12:06.910789+00:00'
page_id: '918389806'
product: rm
source: tdn-rm
title: DT - Integração RM x Feedz - Concatenação de Coligada - Inclusão campo Matricula
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=918389806
version: 3
---

## **1. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Integração RM x Feedz - Concatenação de Coligada - Inclusão campo Matricula |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-12583](https://jiraproducao.totvs.com.br/browse/DRHROTRM-12583) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2406.241
* 12.1.2410.178
* 12.1.2502.105 e superiores

## **03. SITUAÇÃO/REQUISITO**

Permitir o envio do mesmo TOKEN para diversas coligadas sem que os dados dos funcionários sejam sobrescritos, mesmo que a chapa seja a mesma em mais de uma coligada.

## **04. SOLUÇÃO**

O sistema foi alterado para incluir a "Matrícula" no parâmetro, que agora se chama **"Concatenar o Código da Coligada no Cargo / Departamento / Unidade / Matrícula"**.

Com essa modificação, o sistema também concatenará a matrícula, permitindo que a empresa utilize o mesmo TOKEN para várias coligadas sem sobrescrever informações. Ao ativar esse parâmetro, o código da coligada será adicionado ao campo  "Registration" (Chapa do funcionário), garantindo uma distinção clara entre as coligadas.

### Passo 1:

* Acesse o menu Configurações | Parametrizador | Integrações | Feedz e marque o parâmetro **'Concatenar o Código da Coligada no Cargo / Departamento / Unidade / Matrícula'**.

**Passo 2:**

* Acesse o menu Administração de Pessoal | TOTVS RH Performance e Meta / Feedz e realize o envio das informações.

**Passo 3:**

* Demonstração do recebimento das informações na plataforma Feedz: a Matrícula agora é enviada com o código da coligada.
* No exemplo abaixo, o código da coligada é 1 e a chapa 90008 no TOTVS Folha de Pagamento. Ao enviar para a Feedz ficará 1-90008.

**ATENÇÃO:** Caso já esteja integrado os dados com a Feedz, não é recomendado marcar este parâmetro sem alinhamento prévio com o suporte da Feedz. A marcação irá gerar novos códigos (ID's) e podendo danificar a base de dados.

## **05. DEMAIS INFORMAÇÕES**

[Integração RM X Feedz](https://tdn.totvs.com.br/pages/releaseview.action?pageId=785614408)
