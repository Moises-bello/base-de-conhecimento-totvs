---
article_id: 41100086329623
category: TOTVS RH (Linha RM)
content_hash: b8aadf875aa5b0df29ecf48a9d40eabd649c646e2fd15e798c2d35e5ce498113
fetched_at: '2026-06-28T22:46:21.748365+00:00'
product: rm
section_id: 360011673474
source: central-rm
title: RH - RM - FOP - Contabilização de Provisão gera valores negativos para funcionários
  transferidos no mês
type: support-article
updated_at: '2026-06-10T13:16:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41100086329623-RH-RM-FOP-Contabiliza%C3%A7%C3%A3o-de-Provis%C3%A3o-gera-valores-negativos-para-funcion%C3%A1rios-transferidos-no-m%C3%AAs
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41100086320919) Tempo aproximado para leitura: **00:02:56 min**  
  
**Dúvida**  
No módulo **Folha de Pagamento,** por que a contabilização das provisões de férias e 13º salário gera valores negativos para funcionários que foram transferidos entre filiais ou coligadas na mesma competência?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento -Todas as versões   
  
**Solução**  
Esse comportamento é esperado e ocorre devido ao tratamento realizado pelo sistema nos processos de transferência entre filiais ou coligadas.

Quando ocorre uma transferência, especialmente nos casos sem ônus para o cedente, o sistema realiza o estorno dos valores de provisão que já haviam sido apropriados na filial ou coligada de origem. Dessa forma, as provisões acumuladas são baixadas na origem para evitar duplicidade de saldos contábeis.

Como os avos já provisionados anteriormente não são transportados para o novo vínculo na filial ou coligada de destino, a unidade de destino passa a provisionar apenas o avo correspondente à competência atual, enquanto a unidade de origem efetua o estorno do saldo acumulado até a data da transferência.

Em determinadas situações, o valor estornado na origem pode ser superior ao valor provisionado no mês, resultando em lançamentos contábeis com valores negativos. Esse comportamento tem como objetivo garantir o correto encerramento das provisões na unidade de origem e manter a consistência dos saldos contábeis entre as unidades envolvidas.  
  
**Passos**

Caso a empresa não deseje que os encargos de provisão sejam contabilizados com valores negativos, é possível utilizar o parâmetro que inibe a reversão dos valores de provisão.

Para configurar:

1. Acesse **Configurações**;
2. Selecione **Parametrizador**;
3. Acesse **Folha Normal** > **Contabilização**;
4. Marque a opção **"Inibe reversão de valores na provisão mensal de férias"**.  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/41113400425623)
5. Ao habilitar esse parâmetro, o sistema passará a contabilizar apenas o valor do avo adquirido na competência, evitando a geração de valores negativos e a inversão das contas contábeis relacionadas às provisões.

   **Importante**

   Caso o Histórico de Provisões já tenha sido gerado para a competência em questão antes da alteração do parâmetro, será necessário excluir e gerar novamente o histórico para que a nova parametrização seja considerada.

   **Saiba Mais**

   [RH - RM - FOP - Provisão de Férias e 13 Salário](https://tdn.totvs.com/pages/releaseview.action?pageid=519715154)

   [RH - RM - FOP - Transferência entre filiais ou coligadas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020186252-RH-RM-FOP-Transfer%C3%AAncia-entre-filiais-ou-coligadas)
