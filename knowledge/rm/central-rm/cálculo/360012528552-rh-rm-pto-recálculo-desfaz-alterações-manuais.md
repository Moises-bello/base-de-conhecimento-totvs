---
article_id: 360012528552
category: Cálculo
content_hash: 50b1668d03c5b13ac578864758cddcc2df7317aad75301b16da5b78a409daeae
fetched_at: '2026-06-28T22:46:29.268211+00:00'
product: rm
section_id: 1500000861662
source: central-rm
title: RH - RM - PTO - Recálculo desfaz alterações manuais
type: support-article
updated_at: '2025-10-28T17:57:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012528552-RH-RM-PTO-Rec%C3%A1lculo-desfaz-altera%C3%A7%C3%B5es-manuais
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16782161950743) Tempo aproximado para leitura: 00:01:00 min  
  
Dúvida**Ao realizar o recálculo selecionando parâmetros, as alterações manuais realizadas no espelho de ponto são desfeitas. O que fazer para que elas fiquem mantidas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - Todas as versões.  
  
**Solução**Para manter as alterações feitas no ponto do funcionário ao realizar o recalculo desmarque os parâmetros abaixo:  
  
**— Atualiza informações das ocorrências (Atitudes, Justificativas);**  
**— Atualiza ocorrências criticadas do período;**  
**— Atualiza jornada de referência das batidas;**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35941077021847)

**Informações****sobre os Parâmetros:**

* **Calcula Funcionários sem pendências de Cálculo -** Efetua o recálculo dos funcionários que não tiveram dados alterados.
* **Calcula Funcionários com alterações Manuais -** Efetua o recálculo para os funcionários que possuem alterações manuais.  
  **Observação -**Remove as alterações manuais e desabilita o botão "Valores alterados manualmente".
* **Atualiza informações das ocorrências -** Quando **desmarcado,** será considerada a(s) ocorrência(s) já calculada(s) e gravada(s) na tabela AJUSTFUN. Quando **marcado,** será desconsiderada a(s) ocorrência(s) já gravada(s) na AJUSTFUN e irá realizar o cálculo com base na configuração atual do produto.
* **Atualiza ocorrências criticadas do período -** Quando **marcado**, atualizará o cálculo de todas as ocorrências, inclusive das ocorrências criticadas no período. Quando **desmarcado**, e houver ocorrências criticadas no período, nenhuma ocorrência será atualizada.
* **Calcula eventos por fórmula no movimento -** Efetua o cálculo de eventos calculados por fórmula.
* **Calcula eventos por fórmula no banco de horas -** Efetua o cálculo de fórmulas do banco de horas do evento.
* **Gera arquivo de LOG técnico -** Gera o arquivo "RMCHRONUS\_CALCULO\_LOG" depois da execução do cálculo. Provavelmente na pasta C:\CorporeRM\RM.Net\ RMCHRONUS\_CALCULO\_LOG.txt
* **Gera memória de cálculo -** Gera memória de cálculo para cada jornada calculada do funcionário. Para visualizar a memória de cálculo deverá acessar Movimento/Cálculo/Jornada Calculada.  
  **Observação:**A memória de cálculo é gerada somente para uma seleção de no máximo 10 funcionários, acima disso não é gerado memória de cálculo devido ao comprometimento de desempenho do recálculo.

**Saiba mais:**[Calcular Movimentação](https://tdn.totvs.com/pages/viewpage.action?pageId=452719089)
