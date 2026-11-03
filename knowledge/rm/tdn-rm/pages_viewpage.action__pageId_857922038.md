---
content_hash: e5bc6606a86df5031b0a6a48b0db53ef213d6d4f5ee4422b08d7bea9760dcf9b
fetched_at: '2026-06-29T00:11:54.816250+00:00'
page_id: '857922038'
product: rm
source: tdn-rm
title: DT - S-2206 - Geração do gatilho de alteração do término de contrato (tag <tpContr>)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=857922038
version: 6
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | **RM** |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento - eSocial |
| Função: | S-2206 - Geração da tag <tpContr> |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-75](https://jiraproducao.totvs.com.br/browse/DRHROTRM-75) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2310.236
* 12.1.2402.186
* 12.1.2406.119 e superiores

## **03.****SITUAÇÃO/REQUISITO**

Após analisarmos as "Perguntas Frequentes" do eSocial, identificamos que a transformação do contrato de experiência em contrato por prazo indeterminado ocorre automaticamente no dia seguinte ao término do contrato. No entanto, observamos que no eSocial Web, a informação de "contrato indeterminado" só será exibida após o envio do evento S-2206. Esse evento deve ser enviado com a data de alteração no dia seguinte ao término do contrato para que os dados sejam exibidos corretamente no eSocial Web.

## **03.****SOLUÇÃO**

Para atender à orientação do eSocial de atualizar o contrato de experiência do funcionário para "Indeterminado" após o término do contrato, foi criado o novo parâmetro "**Gerar gatilho para Final do Contrato**" no processo eSocial | Outros Processos | Gerar Gatilho em Lote.

Ao marcar esse parâmetro, serão gerados apenas gatilhos para o evento S-2206. O sistema avaliará a data de término do contrato registrada no cadastro do funcionário e gerará um gatilho para o dia seguinte ao término do contrato, conforme o campo **"Data Final do Contrato"** existente no menu Cadastros | Funcionários | Aba Registros | Dados do Contrato (PFUNC.FIMPRAZOCONTR).

**Exemplo:**

Acesse o menu eSocial | Outros Processos | Gerar gatilho em lote e marque o parâmetro "Gerar gatilho para Final do Contrato".

Selecione  a coligada desejada.

Neste exemplo, considerando a competência 07/2024, temos um funcionário com término de contrato previsto para o dia 15/07/2024. Ao marcar o parâmetro "Gerar gatilho para Final do Contrato", será gerado um gatilho para o evento S-2206 para o dia seguinte ao término do contrato, ou seja, 16/07/2024.

Após a execução do processo, o sistema gerou corretamente o gatilho para o funcionário na data de 16/07/2024.

Após a geração do XML o sistema gerou a tag <tpContr> corretamente.

**ATENÇÃO:**

1)Ao marcar o parâmetro "Gerar gatilho para Final do Contrato", serão gerados apenas gatilhos para o evento S-2206. Caso selecione outro evento será apresentada a mensagem abaixo:

2) Apenas os términos de contrato que ocorram dentro da competência serão considerados na geração.

3) Com o recurso de **Agendamento** de tarefas, você pode programar para gerar os gatilhos automaticamente, sem a necessidade de interação do usuário, tornando o processo mais dinâmico e produtivo. Isso funciona com o JobServer configurado para execução em modo 3 Camadas. Para mais informações sobre a configuração, clique [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=270085915).

## **05. DOCUMENTAÇÃO**
