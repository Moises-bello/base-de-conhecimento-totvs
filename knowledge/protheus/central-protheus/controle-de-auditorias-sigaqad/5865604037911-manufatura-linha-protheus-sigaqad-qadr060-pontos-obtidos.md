---
article_id: 5865604037911
category: Controle de Auditorias (SIGAQAD)
content_hash: 8fb006c47472d0880f6d6861a4331378e49f4fef1487f8b594ef05f5500027df
fetched_at: '2026-06-28T22:42:30.892675+00:00'
product: protheus
section_id: 360005876634
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQAD - QADR060 - Pontos Obtidos
type: support-article
updated_at: '2022-05-05T11:47:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5865604037911-Manufatura-Linha-Protheus-SIGAQAD-QADR060-Pontos-Obtidos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:20 min** **Dúvida**Qual o critério utilizado para cálculo do campo **Pontos Obtidos** na listagem do relatório **QADR060 - Listagem de Auditorias**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Auditorias (SIGAQAD) - Todas as versões  
  
**Solução**Na listagem do **QADR060**, o campo **Pontos Obtidos** será listado com base no conteúdo do campo **QUB\_PONOBT - Pontos Obtidos**.  
Este campo é calculado pela rotina **QADA100 - Auditorias**, levando em consideração as seguintes informações:

* Quando a questão é adicional, ou seja, o campo **QUD\_TIPO - Tipo Item** for igual à **2 - Adicional**, serão considerados os dados de **Faixa inicial**, **Faixa final**, **peso** e **alternativos** informados na rotina **QADA120 - Questões Adicionais**. E quando o peso informado for **0-zero**, consideramos o valor de 1 para cálculo, caso contrário, será considerado o peso informado.  
  **QUE\_FAIXIN - Faixa inicial**  
  **QUE\_FAIXFI - Faixa final**  
  **QUE\_PESO - Peso**  
  **QUE\_USAALT - Alternativo**
* Quando a questão é padrão, ou seja, o campo **QUD\_TIPO** for igual à **1 - Padrão**, serão considerados dos dados de **Faixa inicial**, **Faixa final**, **Peso** e **Alternativos** informados na rotina **QADA030 - Questionários**. E quando o peso informado for **0-zero**, consideramos o valor de 1 para cálculo, caso contrário, será considerado o peso informado.  
  **QU4\_FAIXIN - Faixa inicial**  
  **QU4\_FAIXFI - Faixa final**  
  **QU4\_PESO - Peso**  
  **QU4\_USAALT - Alternativo**
* O conteúdo do parâmetro **MV\_QADQZER - Indica se a Faixa Inicial de uma questão do tipo Alternativa, será considerada como nota igual a Zero, caso seja respondida como não-conforme** também é considerado:
  + Se estiver com conteúdo igual à **.T.** ou em **branco**, e se a nota informada na questão for igual à faixa inicial, a nota da questão será sugerida como **0-Zero** para efeito de cálculo.
* Com estes dados, o seguinte cálculo é realizado pela rotina **QADA100** para obter o valor do campo **QUB\_PONOBT**:  
  **QUB\_PONOBT = (((Nota \* Peso)\*100)/Max)**  
     
  **Onde**:  
  **Nota** = **Faixa inicial** calculada à partir do conteúdo do parâmetro **MV\_QADQZER**  
  **Peso** = Peso informado para a questão. Se o peso informado na questão for **0-zero**, será considerado como 1.  
  **Max** = **Faixa Final** informada na questão  
    
  E quando a auditoria estiver com legenda igual à **3 - Liberada para Encerramento**, o conteúdo do campo **QUB\_PONOBT** é atualizado, onde será dividido pela somatória dos pesos de todas as questões.
