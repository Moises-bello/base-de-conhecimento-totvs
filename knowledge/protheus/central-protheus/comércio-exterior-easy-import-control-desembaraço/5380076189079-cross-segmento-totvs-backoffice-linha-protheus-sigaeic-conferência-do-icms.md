---
article_id: 5380076189079
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: c56f669956304520ac81e3f98aad92ce0af4a67f4d68f1757115843a25aa1bc2
fetched_at: '2026-06-28T22:39:51.399204+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus -SIGAEIC - Conferência do
  ICMS
type: support-article
updated_at: '2022-04-26T12:18:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5380076189079-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Confer%C3%AAncia-do-ICMS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como realizar a conferência do ICMS?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - *Easy Import Control* - Todas as versões  
  
**Solução**

**ICMS**É calculado da seguinte forma:

```
ICMS'= [(CIF + II + IPI) /(1-Alíquota ICMS) ] – II – IPI – CIF  
Base ICMS = (CIF + II + IPI + PIS + COFINS + Desp Base ICMS) /(1 – Alíquota ICMS)
```

Para o ICMS pode ser apresentado divergência de valores de duas formas, na **base de ICMS** ou no **valor do ICMS**, sendo assim deve ser verificado as seguintes configurações para:

**1.0 - Divergência Base de ICMS**

* Todas despesas base de ICMS e configuradas corretamente conforme documentação: [Cross Segmento - TOTVS Backoffice Linha Protheus -SIGAEIC - Como configurar despesa base de ICMS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5379525211031)
* Redução , Diferimento e Crédito Presumido de ICMS - Caso possua redução, diferimento ou credito presumido para o ICMS, verifique se a mesma encontra-se configurada de acordo com a documentação: [Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Redução de ICMS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026774631)

**Observações**

* A **alíquota da ICMS** informada no CFO será considerada para cálculo do processo, verificar se a mesma esta coerente com a informação da D.I. (Declaração de Importação);
* O campo despesas base de icms (WN\_DESPICM) contém o somatório do rateio das despesas base de icms para o item da nota fiscal.
* São consideradas todas as despesas configuradas com base de ICMS (YB\_BASEICM) = “SIM” e que esteja configurada no mesmo cadastro para ser base de ICMS no estado do importador ("YB\_ICMS\_XX", onde XX é o estado do importador YT\_ESTADO), rateadas conforme os critérios de rateio de despesas na nota de importação. O valor calculado pelo sistema pode ser modificado através da tela exibida pelo botão "Altera Item". Não é recomendado o uso desta tela, a não ser que seja necessário algum ajuste de centavos.  
  ![cadastro_icms.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5527491522711/cadastro_icms.gif)

**2.0 - Divergência do Valor de ICMS**

* **Alíquota de ICMS:** Informada no cadastro de NCM. Verifique em Atualizações\Tabelas\N.C.M, posicione na NCM e selecione Alterar.  
  ![CONFERENCIA_NCM.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5525281617303/CONFERENCIA_NCM.gif)
* **Rateio de Despesas base de ICMS:** Antes é necessário verificar de que forma o despachante realizou o rateio das despesas Base ICMS (Peso: ‘Sim’ ou ‘Não’), para que uma vez definido o parâmetro permaneça para os demais processos. A configuração do rateio da despesa é informado na rotina Cadastro de Despesas.  
  ![cadastro_despesa.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5525332024983/cadastro_despesa.gif)

* **Divergência de rateio ou valor da Taxa Siscomex:** [Cross Segmento - TOTVS Backoffice Linha Protheus -SIGAEIC - Configuração da taxa siscomex](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5525115202327)
* **Cálculo de ICMS (“Por dentro”) -** **ICMS em sua própria base de cálculo:** Conforme estabelecido no art 6 § 1 do RICMS o cálculo de ICMS por dentro refere-se a inclusão do ICMS em sua própria base de cálculo. Caso seja utilizando este cálculo necessário configurar o parâmetro **MV\_ICMS\_IN** deve estar igual a T (habilitado) para calcular o ICMS com a nova regra cálculo;
* Configuração do parâmetro [**MV\_EIC0028**](https://tdn.totvs.com.br/pages/releaseview.action?pageId=107940014)  para determinar na rotina Receb. Importação (EICDI154), se o **cálculo do ICMS** deve considerar/compor os valores de **PIS e COFINS (.T.) ou não (.F.)**.
* Configuração do parâmetro [**MV\_EIC0051**](https://tdn.totvs.com.br/pages/releaseview.action?pageId=181961413) para desconsidera o valor da despesa quando configurado Base Imposto =SIM e Base ICMS=NÃO da Base de ICMS ao Gerar a NF,Valores .T. ou. F.
