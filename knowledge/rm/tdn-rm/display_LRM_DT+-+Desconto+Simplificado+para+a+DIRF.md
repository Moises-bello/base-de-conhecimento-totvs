---
content_hash: 1687e1903eaca9b88d31701c1f35a56200df7011f99c7ddd75b1781878122065
fetched_at: '2026-06-29T00:12:01.357792+00:00'
page_id: '893433673'
product: rm
source: tdn-rm
title: DT - Desconto Simplificado para a DIRF
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+Desconto+Simplificado+para+a+DIRF
version: 52
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Desconto Simplificado para a DIRF |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-11450](https://jiraproducao.totvs.com.br/browse/DRHROTRM-11450 "View this issue") |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2402.267
* 12.1.2406.222
* 12.1.2410.153  ou superiores

## **03. SITUAÇÃO/REQUISITO**

Diante de um cenário atípico em 2024, relacionado à DIRF do ano-calendário 2023, caracterizado pela falta de clareza nas orientações governamentais sobre o campo **"Desconto Simplificado"** e pelo aumento nos acionamentos por parte dos clientes, identificamos a necessidade de desenvolver adequações no produto **TOTVS Folha de Pagamento**.

Essas melhorias têm como objetivo garantir o correto funcionamento da geração da DIRF 2024/2025, atendendo às exigências legais e assegurando a confiabilidade do processo para nossos clientes.

## **04. SOLUÇÃO**

Foram realizadas diversas tratativas no produto **TOTVS Folha de Pagamento** para garantir o preenchimento e validação correta dos campos **Desconto Simplificado**. As melhorias incluem:

**1)** **RM Atualizador**

Após a liberação da versão será necessário executar os scripts de adequação das tabelas e campos do sistema através do sistema **RM.Atualizador.exe.**

**2)** **Processo Atualiza Campo Desconto Simplificado:**

* O processo passou a preencher automaticamente os campos **Desconto Simplificado Caixa** (aplicável à Folha e 13º Salário) com os valores:
  + - **2:** Não simplificado
    - **3:** Simplificado

* Nos casos Diferença de Férias, Rescisão complementar e rescisão o processo irá gravar conforme abaixo:

                        -**Diferença de Férias:**

**8:**Não simplificado

**9:**Simplificado

                        -**Rescisão complementar:**

**6:**Não simplificado

**7:**Simplificado

                         -**Rescisão:**

**4:**Não simplificado

**5:**Simplificado

Atenção:

Segue os casos em que o **IRRF Simplificado Caixa** não é atualizado pelo processo:

* **Envelopes (PFPERFF) sem eventos na ficha financeira (PFFINANC):**  
  Quando os envelopes do funcionário não possuem registros associados na ficha financeira, o IRRF Simplificado não será atualizado.
* **Férias normais:**  
  Para situações de férias normais, o valor do **IRRF Simplificado** é retornado conforme o campo **PFUFERIASRECIBO.IRRFSIMPLIFICADO**.

* + Para mais detalhes, consulte o TDN: [Atualiza Campo Desconto Simplificado](https://tdn.totvs.com/display/LRM/Atualiza+Campo+Desconto+Simplificado)

**3)** **Geração da DIRF:**

* + Durante o processo de geração da DIRF, o sistema agora executa internamente o processo **"Atualiza Campo Desconto Simplificado"** caso os campos **Desconto Simplificado Caixa** apresentem valores diferentes de 2 ou 3. Nessa situação, será emitida a seguinte mensagem:

**ATENÇÃO:** Mesmo que seja apenas para um funcionário a mensagem sempre será exibida.

Caso deseje utilizar o recurso de **Agendamento** de tarefas, você pode parametrizar para que a geração da DIRF / Atualização do Desconto Simplificado ocorra automaticamente, sem a necessidade de interação do usuário, tornando o processo mais dinâmico e produtivo. Isso funciona com o JobServer configurado para execução em modo 3 Camadas. Para mais informações sobre a configuração, clique [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=270085915).

**4)** **Acesso ao produto TOTVS Folha de Pagamento:**

* + Ao acessar o **TOTVS Folha de Pagamento**, os usuários com permissão para o processo **DIRF** visualizarão uma mensagem informativa sobre a obrigatoriedade de executar o processo **"Atualiza Campo Desconto Simplificado"**.
  + Além disso, o sistema apresentará o processo diretamente na tela para facilitar a execução.
  + Para mais detalhes, consulte o TDN:

## **05. DEMAIS INFORMAÇÕES**
