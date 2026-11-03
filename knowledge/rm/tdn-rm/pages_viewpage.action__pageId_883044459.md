---
content_hash: a3a263e1b70f58a3275c9214cfb8835dd79028acb8f8319d27d4b0daa95f8753
fetched_at: '2026-06-29T00:12:00.174044+00:00'
page_id: '883044459'
product: rm
source: tdn-rm
title: DT - Integração com TOTVS RH Orçamento - Operações via Winforms
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=883044459
version: 1
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Gestão de Pessoas |
| Função: | Integração com TOTVS RH Orçamento |
| País: | Brasil |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHHCM-13909](https://jiraproducao.totvs.com.br/browse/DRHHCM-13909) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2502

## **03. SITUAÇÃO/REQUISITO**

      

       No sistema, após criar uma requisição, a mesma recebe o status de "Pendente".  
       Conforme processamento padrão, a mesma poderia ser colocada para o fluxo de repasses a aprovações através do processo "Inserir no Fluxo", porém quando se tratar de requisições do tipo Aumento de Quadro, Alterações de Dados Funcionais ou Substituição (desde que originada de uma Alteração de Dados Funcionais), estando a integração com TOTVS RH Orçamento habilitada, antes de iniciar o fluxo de repasses, a requisição será primeiramente enviada para validações de Controles e Travas do TOTVS RH Orçamento.

       Após a execução do processo, a requisição será enviada para a integração de Controles e Travas no TOTVS RH Orçamento e receberá o status de "Consultando Orçamento", representada pelo ícone azul claro.

       A requisição permanecerá nesse status até ter o retorno do TOTVS RH Orçamento com sua aprovação ou reprovação.

* Caso a requisição seja aprovada nas validações de Controles e Travas do TOTVS RH Orçamento, no RM a requisição será automaticamente inserida no Fluxo de Repasses e Aprovações.
* Caso a requisição seja reprovada nas validações de Controles e Travas do TOTVS RH Orçamento:
  + Caso não conste possibilidade de exceção no TOTVS RH Orçamento, a requisição será reprovada automaticamente no RM.
  + Caso conste possibilidade de exceção no TOTVS RH Orçamento, a requisição receberá o status de "Orçamento não aprovado" identificada pelo ícone na cor alaranjada.

       Uma vez que a requisição esteja no status de "Orçamento não aprovado", caberá ao usuário tomar a decisão do que fazer com a requisição, podendo:

* + Cancelar a Requisição - Assim a requisição será cancelada.
  + Inserir no Fluxo com Exceção - Assim a requisição irá para o Fluxo de Repasses e Aprovações.

## **04. DEMAIS INFORMAÇÕES**

      Requisições que tiverem sido reprovadas nas validações de Controles e Travas no TOTVS RH Orçamento, mas tiverem a possibilidade de exceção, terão no seu cadastro, na aba de "Integração com TOTVS RH Orçamento" a flag do campo "Permite Exceção" marcada, lembrando que este campo nunca sofrerá manipulação por parte do usuário.

## **05. ASSUNTOS RELACIONADOS**

       O envio da requisição para o TOTVS RH Orçamento bem como o retorno de aprovação ou reprovação por parte do TOTVS RH Orçamento será realizado de maneira automática, não sendo necessária nenhuma ação por parte do usuário.
