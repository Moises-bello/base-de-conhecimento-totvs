---
article_id: 27323431221527
category: SIGAEST - MOVIMENTAÇÕES
content_hash: c59c4c136e8b85c0dff76e9fca8554ce953e09328e3b8be901997a80ab54ed99
fetched_at: '2026-06-28T22:38:55.519945+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Exclusão de documento
  sob processo de cancelamento extemporaneo em periodo ja encerrado
type: support-article
updated_at: '2026-02-19T13:48:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27323431221527-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Exclus%C3%A3o-de-documento-sob-processo-de-cancelamento-extemporaneo-em-periodo-ja-encerrado
---

Para cancelar uma nota fiscal emitida em mês anterior no TOTVS Protheus, é necessário reabrir o período de apuração encerrado para permitir a exclusão do documento, garantindo a integridade dos saldos já finalizados. A alternativa de ajuste de parâmetro só é válida para empresas sem fechamento de estoque.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27323431210007) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**

Exite o processo de [cancelamento extemporaneo de nota fiscal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10017801361687--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Cancelamento-extempor%C3%A2neo-fora-do-prazo), onde é permitido excluir o documento fiscal em periodos anteriores, de acordo com a procedencia de cada estado, atualmente funciona para casos que ocorrem durante o mes vigente, porem como proceder quando o cancelamento ocorres apos a virada de saldos, ou seja NF emitida em um mes e o cancelamento precisar ocorrer em outro?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - A partir da versão 12.1.33.  
  
**Solução**

Quando realiza o Processo de Cancelamento de Nota Fiscal Fora do Prazo:

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Cancelamento extemporâneo fora do prazo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10017801361687--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Cancelamento-extempor%C3%A2neo-fora-do-prazo)

Para cancelar uma nota fiscal emitida fora do prazo, **é necessário realizar a exclusão do documento emitido**. No entanto, **se o período de apuração já estiver encerrado, será preciso reabri-lo para que a exclusão do documento fiscal seja permitida**.

Esse procedimento é essencial pois o documento já movimentou registros de estoque, financeiro e contábil. Além disso, apurações do período em questão já foram realizadas. **Qualquer alteração, inclusão ou exclusão de documentos em um período encerrado demanda a reabertura do período**, garantindo a integridade dos saldos que já foram finalizados.

Atualmente, o sistema já conta com uma rotina para a reabertura de estoque, permitindo reabrir até o período desejado para, então, prosseguir com o cancelamento ou exclusão do documento fiscal. Essa funcionalidade está disponível na release 12.1.33 em diante no no módulo Estoque Custos.

[SIGAEST - MATA038 - Processo de Reabertura de Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6420543172247-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA038-Processo-de-Reabertura-de-Estoque)

Para empresas que não possuem o processo de fechamento de estoque, **uma sugestão** é ajustar o parâmetro **MV\_ULMES** para uma data anterior à emissão do documento fiscal a ser cancelado, efetuar o processo, e depois voltar o parametro para data que ele estava.

**||--\\\*\*ATENÇÃO\*\*//--||****:** Essa alternativa do parametro, só se aplica a empresas **que não possuem o processo de fechamento de estoque**. Caso contrário, o procedimento é inválido, pois o fechamento utiliza tabelas de controle de saldos finais por período, **e somente a reabertura de período efetiva a alteração dos dados**.

**Minha empresa possui processo de fechamento, mas não posso reabrir períodos encerrados. Como proceder para cancelar a nota fiscal?**

**A única solução padrão é realizar a reabertura do período**. Caso contrário, ao tentar excluir o documento, será exibida a mensagem de ajuda "**HELP FECHTO**", indicando a necessidade de reabertura para efetuar o cancelamento da nota.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27323419825815)

Se voce não possui fechamentos, basta avalair como consta o parametro MV\_DBLQMOV, talvez a data dele esteja configurada para não permitir movimentos no periodo em questão, só alterar a data para um periodo anterior

Esse processo da apresentação do HELP em periodos ja encerrados, onde existe a necessidade de efetuar movimentações, visa assegurar que as operações sejam consistentes com os registros fiscais e contábeis, preservando a integridade dos dados no sistema e cumprindo com as exigências de controle e auditoria, em um periodo que ja foi encerrado, onde caso exista a necessidade de movimentar qualquer coisa no perido, somente mediante a reabertura do mesmo.

**Saiba mais**:

[*Clique aqui e veja mais artigos sobre a Nova Jornada de Fechamento no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/5367899706647-ACOMPANHA-CUSTOS-JORNADA-DE-FECHAMENTO-NOVO-)

[SIGAFAT - Exclusão Documento de Saída apresentado: HELP FECHTO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042322274-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Exclus%C3%A3o-Documento-de-Sa%C3%ADda-apresentado-HELP-FECHTO)
