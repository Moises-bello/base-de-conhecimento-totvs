---
article_id: 360007004031
category: Ativo Fixo - Cálculo, Descalculo e Simulação de Depreciação e Depreciação
  acelerada
content_hash: f4f3d021015d914e48baa3299b6407d50a0996acd66ed35224c28bd5f5c261f4
fetched_at: '2026-06-28T22:41:43.300188+00:00'
product: protheus
section_id: 1500001536401
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF Qual o procedimento para
  informar depreciação total em um ativo?
type: support-article
updated_at: '2021-10-25T11:50:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007004031-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-Qual-o-procedimento-para-informar-deprecia%C3%A7%C3%A3o-total-em-um-ativo
---

**Dúvida**Qual o procedimento para informar depreciação total em um ativo?  
  
**Ambiente**

# Cross Segmento - Backoffice Linha Protheus - SIGAATF  – A partir da versão 11.80

**Solução**  
- Informar no bem a taxa de depreciação anual que falta para o bem depreciar total.

- Para informar a taxa utilizar a rotina: Alteração da taxa de depreciação (ATFA230)

(O programa tem o objetivo de alterar as taxas de depreciação conforme parâmetros definidos, podendo ser apena um bem ou mais)

- Na quinta pergunta "?" deve informar a taxa que deseja para o bem, na moeda que irá selecionar.

Exemplo:

- Ativo de valor X

- Para que ele deprecie em um mês a taxa deve ser 1200%

Como a taxa de depreciação é anual uma taxa de 100% depreciaria em um ano.

Para chegar nos 1200%, eu multiplico 100% pelo numero de mês que irei adiantar à depreciação \*12

Conclusão: Para uma depreciação total de um bem no mês, preciso de uma taxa de 1200% (que equivale ao ano)

**Observação**

Se a pergunta referente a taxa "?" não tiver suportando o tamanho 9999,9999 ajuste via SIGACFG.

Acessando : Base de dados -> Dicionário -> Base de dados -> Perguntas.

Pesquisar o grupo de perguntas = AFA230 e editar.

Na pergunta referente a taxa "?"  ajusta:

Tamanho = 9

Decimal = 4

Formato = @E 9999.9999

***Faça backup se precisar de ajuste na SX1.(grupo de perguntas)***
