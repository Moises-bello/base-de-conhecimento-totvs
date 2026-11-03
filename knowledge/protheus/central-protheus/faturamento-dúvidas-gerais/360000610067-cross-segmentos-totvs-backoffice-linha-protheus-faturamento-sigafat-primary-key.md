---
article_id: 360000610067
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 38f7984931d6f0a01009a4d06304589042f06add23bf1228b275a00e847247a4
fetched_at: '2026-06-28T22:38:33.071798+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT)
  - Primary Key violation in SE1, please contact your administrator
type: support-article
updated_at: '2024-10-14T17:14:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000610067-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Primary-Key-violation-in-SE1-please-contact-your-administrator
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27057863315863) Tempo aproximado para leitura: 00:01:00 min**

**Ocorrência**Ao faturar é gerado o erro: **Primary Key violation in SE1, please contact your administrator on CHKE1NOTA** (MATXFUNA.PRX)

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) – Faturamento – A partir da versão 11.80  
  
**Causa**Erro exibido quando utiliza o Financeiro Compartilhado entre filiais; porém, com movimentos de Saída (contas a receber) Exclusivos.

Ou seja, possui "apenas uma SE1" para receber os títulos gerados por "n" Filiais. Chega um momento em que há duplicidade no número dos títulos (pois são gerados cada um de uma Filial).  
  
**Solução**

Há duas opções para que o problema não ocorra:

* Alterar o compartilhamento das Tabelas (**SF2, SD2, SE1, SF3, SE2, SE3**) de forma que o Financeiro e o Faturamento estejam compatíveis (ou ambos compartilhados, ou ambos exclusivos).
* Customizar a geração do Prefixo do titulo, de forma que cada Filial gere um prefixo. Assim os títulos são gerados com numeração diferente.  

  Para customizar a geração do Prefixo do titulo, de forma que cada Filial gere um prefixo diferente, deve informar um rdmake customizado chamado por U\_FUNCAO() (Ao invés de receber a expressão ADVPL SF2->SERIE) no qual contenha a regra em ADVPL para geração de prefixo.

**OBSERVAÇÃO 1:** Havendo dificuldade neste sentido, contate nosso Suporte a ADVPL do Protheus.

**OBSERVAÇÃO 2:** Caso seja alterado o comportamento padrão do sistema na gravação do E1\_PREFIXO alterando o conteúdo do parâmetro MV\_1DUPREF é necessário também tratar a Exclusão do Documento de Saída MATA521 a qual usa como referência na busca dos títulos a numeração e serie da nota, para esse tratamento sugerimos avaliar os seguintes Pontos de Entrada:

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Lista de Pontos de Entrada da rotina MATA521 - Exclusão de Documento de Saída](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000610067)

**Saiba mais:**[FAT0145 Primary Key violation in SE1 please contact your administrator on CHKE1NOTA(MATXFUNA.PRX)](https://tdn.totvs.com/x/4iv2Dw)
