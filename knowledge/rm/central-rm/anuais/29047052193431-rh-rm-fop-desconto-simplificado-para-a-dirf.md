---
article_id: 29047052193431
category: Anuais
content_hash: da120ef5f7db2ba6815583809ba610986d2da265e377e56eeabc8a98f424eae3
fetched_at: '2026-06-28T22:46:51.013263+00:00'
product: rm
section_id: 1500000861142
source: central-rm
title: RH - RM - FOP - Desconto Simplificado para a DIRF
type: support-article
updated_at: '2025-01-07T20:36:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29047052193431-RH-RM-FOP-Desconto-Simplificado-para-a-DIRF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29047025149847) Tempo aproximado para leitura: **00:01:30 min****Dúvida**Como validar as tratativas no produto **TOTVS Folha de Pagamento** para garantir o preenchimento e validação correta dos campos **Desconto Simplificado**  
  
**Ambiente**

* 12.1.2402.262
* 12.1.2406.213
* 12.1.2410.139 ou superiores

**Solução**

Foram realizadas diversas tratativas no produto **TOTVS Folha de Pagamento** para garantir o preenchimento e validação correta dos campos **Desconto Simplificado**. As melhorias incluem:

**1)** **RM Atualizador**

Após a liberação da versão será necessário executar os scripts de adequação das tabelas e campos do sistema através do sistema **RM.Atualizador.exe.**

![image-2024-7-10_19-21-57.png](https://tdn.totvs.com/download/attachments/862114556/image-2024-7-10_19-21-57.png?version=1&modificationDate=1723119694740&api=v2)

**2)****Processo Atualiza Campo Desconto Simplificado:**

* O processo passou a preencher automaticamente os campos **Desconto Simplificado Caixa** (aplicável à Folha e 13º Salário) com os valores:
  + - **2:** Não simplificado
    - **3:** Simplificado
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

* + Para mais detalhes, consulte o TDN: [Atualiza Campo Desconto Simplificado](https://tdn.totvs.com/display/LRM/Atualiza+Campo+Desconto+Simplificado)

**3)** **Geração da DIRF:**

* + Durante o processo de geração da DIRF, o sistema agora executa internamente o processo **"Atualiza Campo Desconto Simplificado"** caso os campos **Desconto Simplificado Caixa** apresentem valores diferentes de 2 ou 3. Nessa situação, será emitida a seguinte mensagem:

![](https://tdn.totvs.com/download/attachments/893433673/image-2024-12-27_17-29-38.png?version=1&modificationDate=1735331378777&api=v2&effects=border-simple,shadow-kn)

**ATENÇÃO:**Mesmo que seja apenas para um funcionário a mensagem sempre será exibida.

Caso deseje utilizar o recurso de **Agendamento** de tarefas, você pode parametrizar para que a geração da DIRF / Atualização do Desconto Simplificado ocorra automaticamente, sem a necessidade de interação do usuário, tornando o processo mais dinâmico e produtivo. Isso funciona com o JobServer configurado para execução em modo 3 Camadas. Para mais informações sobre a configuração, clique [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=270085915).

![](https://tdn.totvs.com/download/attachments/893433673/image-2024-12-17_11-59-21.png?version=1&modificationDate=1734447561337&api=v2)

**4)** **Acesso ao produto TOTVS Folha de Pagamento: (Somente a partir do dia 20/01/2025)**

* + Ao acessar o **TOTVS Folha de Pagamento**, os usuários com permissão para o processo **DIRF** visualizarão uma mensagem informativa sobre a obrigatoriedade de executar o processo **"Atualiza Campo Desconto Simplificado"**.
  + Além disso, o sistema apresentará o processo diretamente na tela para facilitar a execução.
  + Para mais detalhes, consulte o TDN: [Atualiza Campo Desconto Simplificado](https://tdn.totvs.com/display/LRM/Atualiza+Campo+Desconto+Simplificado)

## **05. DEMAIS INFORMAÇÕES**

[DIRF 2024 - Dedução Simplificada quando tem Férias e Folha no Mês](https://tdn.totvs.com/pages/viewpage.action?pageId=828006415)
