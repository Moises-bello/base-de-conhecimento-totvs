---
content_hash: 86d567617ae2d61b1014d5280e456383fbb5926dc7fdc0414f20edb5847bed11
fetched_at: '2026-06-29T00:10:22.664616+00:00'
page_id: '498456507'
product: rm
source: tdn-rm
title: Como validar as bases de FGTS entre o TOTVS Folha de Pagamento e Governo?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=498456507
version: 5
---

# Objetivo:

---

       O objetivo deste documento é orientar como validar as bases de FGTS entre os valores gerados pelo TOTVS Folha de Pagamento e retornados pelo Governo.

false

**A partir das Versões:**

* + 12.1.22
  + 12.1.23
  + 12.1.24

---

Passos - Validação FGTS1º Passo - Exportação do Envelope

Realize a exportação do envelope do funcionário para um arquivo com extensão **.XLS** ou **.XLSX** (Excel).

Para isso, acesse o envelope do funcionário e selecione **Exportar dados da Visão | Exportar para XLS** ou **Exportar dados da Visão | Exportar para XLSX**.

**Importante**  
Todas as colunas referentes à FGTS  devem estar visíveis no envelope antes da extração para que constem no arquivo exportado.

2º Passo - Validação de Incidências

O próximo passo é verificar se as incidências de FGTS das verbas presentes no envelope do funcionário estão condizentes com o governo. Isso irá garantir que não houve nenhuma alteração na incidência diretamente no TAF/Governo ou que não houve alteração no RM sem que o S-1010 fosse aceito pelo RET.

Abra o arquivo exportado no passo anterior e:

- inclua duas colunas com os nomes **CodIncFGTS\_RM** e **CodIncFGTS\_RET**;  
- acesse o evento S-1010 (aceito RET) relacionado a cada uma das verbas e valide o valor da TAG **<CodIncFGTS>**. Insira a informação no arquivo na coluna **CodIncFGTS\_RM** criada;  
- acesse o eSocial Web e em **Empregador | Tabelas | Tabela de Rubricas** consulte para cada verba o valor da coluna **Incidência FGTS**. Insira a informação no arquivo na coluna **CodIncFGTS\_RET** criada.

Abaixo, exemplo do arquivo após preenchimento das colunas:

Os valores de **CodIncFGTS** devem ser iguais no RM e RET. Caso encontre divergências, será necessário encaminhar um S-1010 para ajuste. Fique atento à data de início de validade do evento, pois todos os arquivos de Folha/Rescisão já transmitidos para o RET e cujo período de apuração seja posterior ao início da validade, precisam ser retificados para que a incidência seja corretamente considerada.

3º Passo - Validação das Bases

Após garantir que as incidências no RM e RET estão idênticas, é necessário somar todas os valores do envelope relativos à cada CodIncFGTS, comparando assim com o total apresentado pelo governo.

Importante  
Caso utilize tomador de serviço, lembre-se de somar os valores presentes em cada lotação tributária exibida no eSocial Web.

Exemplo:

* Somatório das verbas do envelope do funcionário com CodIncFGTS 12 (Base de Cálculo de FGTS 13º Salário)  = **R$ 743,50**

* Somatório das Bases de Cálculo de FGTS 13º Salário no eSocial Web = R$ 82,61 + R$ 82,61 + R$ 578,28 = **R$ 743,50**

A mesma validação deverá ser realizada com os demais códigos de incidência.

Considerações

**CodIncFGTS**

O código de incidência do FGTS do S-1010 (codIncFGTS) é gerado conforme Layout do eSocial:

**Comparativo**

Está sendo estudado e planejado pela equipe de desenvolvimento um relatório comparativo para as bases de FGTS. Tal relatório ainda não possui previsão de implementação. Acesse as [Novidades da Release](http://tdn.totvs.com/display/LRM/Novidades+da+Release) para acompanhar as novas ferramentes disponibilizadas no sistema.
