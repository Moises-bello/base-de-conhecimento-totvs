---
content_hash: 3eba8ba34ef35a9c34dbdfcb76c5befc09574b2357f3cab035b55e0c97f09a3e
fetched_at: '2026-06-29T00:12:03.437819+00:00'
page_id: '910022357'
product: rm
source: tdn-rm
title: DT - Ajuste no Cadastro de Lote
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+Ajuste+no+Cadastro+de+Lote
version: 3
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Gestão de Pessoas |
| Função: | RM - SST |
| País: | Brasil |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | JIRA0c783de1-186e-383b-975c-a1acd7d76cb5DRHSSTPT-135 |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2502

## **03.****SITUAÇÃO/REQUISITO**

*O campo de identificador do cadastro de lote esta sendo editável, gerando problema na pesquisa usada pela LIB.*

## **04. OBJETIVO**

*Garantir a integridade dos dados ao impedir a edição do campo chave do identificador do lote, prevenindo inconsistências nas pesquisas realizadas pela LIB.*

## **05. VALOR GERADO**

*A correção assegura a consistência das informações e elimina falhas que antes comprometiam a confiabilidade das pesquisas utilizadas pela LIB.*

## **06. CONTEXTO**

*O campo de identificador do cadastro de lote anteriormente permitia edição, possibilitando a modificação de um valor chave. Essa vulnerabilidade afetava a integridade dos dados e causava inconsistências nas pesquisas realizadas pela LIB.*

*Com a correção aplicada, o campo agora está devidamente protegido contra alterações indevidas.*

## **07. SOLUÇÃO IMPLEMENTADA**

*- O campo identificador do lote foi desabilitado para edição na tela de inclusão de novos lotes de EPIs.*  
*- O campo identificador do lote também foi bloqueado na janela de edição para evitar qualquer modificação.*

## **08. REQUISITOS E PRESSUPOSTOS**

*- O cadastro do catálogo de EPIs deve estar previamente existente no sistema.*  
*- O campo de identificador é um valor chave e não pode ser alterado após sua criação.*

## **09. CRITÉRIO DE ACEITE**

*- O campo identificador do lote deve estar bloqueado para edição em todas as telas pertinentes.*  
*- Merge relacionado: 2402, 2406, 2502.*  
*- A documentação foi atualizada conforme necessário.*

## **10. DOCUMENTAÇÃO**

*- As instruções para os usuários finais foram atualizadas para refletir a nova restrição.*

## **11. CONCLUSÃO**

*A implementação foi concluída com sucesso. Após os testes, foi validado que o campo identificador do lote agora está bloqueado para edição, garantindo a integridade dos dados e eliminando os problemas previamente identificados.*
