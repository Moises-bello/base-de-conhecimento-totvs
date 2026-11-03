---
article_id: 360007057091
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 75b802a855a17a076aaa24fb968848b84c1f52a2977513aee91c840bdaba4cc0
fetched_at: '2026-06-28T22:38:54.133355+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Quais os significados
  dos códigos dos tipos de Movimentos Internos RE/DE?
type: support-article
updated_at: '2026-05-27T19:36:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007057091-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Quais-os-significados-dos-c%C3%B3digos-dos-tipos-de-Movimentos-Internos-RE-DE
---

O campo Tipo RE/DE/PR/ER nas movimentações internas do estoque, presente na tabela SD3, identifica o tipo de movimentação interna: RE para requisição (saída), DE para devolução (entrada), PR para produção e ER para estorno de produção. Cada código detalha a natureza da movimentação, como manual, automática, transferência, entre outros. Os códigos 499 e 999 são reservados para uso interno do sistema e não podem ser cadastrados manualmente.

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28806987802391)** Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**  
O que significa o campo **Tipo RE/DE/PR/ER** nas movimentações internas do estoque?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

O campo tipo **RE/DE** é referente ao controle de movimentações internas do estoque, este campo faz parte da tabela **SD3(D3\_CF)**, que é exclusivamente dedicada ao registro de movimentações internas do estoque. É importante ressaltar que este campo **não está presente nas tabelas de notas fiscais de entrada (SD1) ou de saída (SD2)**, uma vez que seu propósito específico é o controle de movimentações puramente internas.

A principal função deste campo é identificar e categorizar o tipo específico de movimentação que está ocorrendo dentro do estoque da empresa.

O código gravado no conteúdo deste campo identifica o tipo de movimentação interna registrada no estoque, sendo que esses códigos representam:

* **RE?**= Requisição (quando ocorre um movimento de saída do estoque)
* **DE?** = Devolução (quando ocorre um movimento entrada no estoque).

**A seguir, apresentam-se as especificações para o preenchimento do campo D3\_CF (Tipo DE/RE):**

**Movimentações de saida RE:**

**RE0 -** Requisição manual.  
**RE1 -** Requisição automática.  
**RE2 -** Requisição automática de material de apropriação indireta.  
**RE3 -**Transferência em geral.

**RE3\* -**Requisição ao Armazém de Processo ([MV\_LOCPROC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020688571-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-e-usabilidade-de-Apropria%C3%A7%C3%A3o-Indireta-MV-LOCPROC))  
**RE4 -** Requisição por transferência.  
**RE5 -** Requisição informando OP na nota fiscal de entrada.           
**RE6 -** Requisição valorizada / Requisição do Armazém de Qualidade ([MV\_CQ](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025518774-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Rotina-MATA175-Instru%C3%A7%C3%B5es-padr%C3%B5es-sobre-Controle-de-Qualidade-no-Estoque))/Requisição do Armazém de Transito([MV\_LOCTRAN](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021874551-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Configura%C3%A7%C3%A3o-e-Inclus%C3%A3o-de-Documento-de-Entrada-em-Tr%C3%A2nsito-MV-LOCTRAN)) / Movimento de [ativo Fixo](https://tdn.totvs.com/x/DM4kJg)  
**RE7 -**Requisição para transferência de um para “N”.  
**RE9 -**Requisição para OP sem agregar custo.

**REA -** Reavaliação de custo médio (Requisição de valor final para período).

**Movimentações de entrada DE:**

**DE0 -**Devolução manual.  
**DE1 -** Devolução automática - estorno da produção.  
**DE2 -** Devolução automática de material de apropriação indireta - estorno da produção.  
**DE3 -**Estorno de transferência para local de apropriação indireta.

**DE3\***- Devolução do Armazém de Processo ([MV\_LOCPROC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020688571-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-e-usabilidade-de-Apropria%C3%A7%C3%A3o-Indireta-MV-LOCPROC))  
**DE4 -** Devolução de transferência entre locais.  
**DE5 -** Devolução de material apropriado em OP – (exclusão de nota fiscal de entrada).  
**DE6 -** Devolução valorizada / Devolução ao armazém destino oriundo do Armazém de Qualidade ([MV\_CQ](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025518774-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Rotina-MATA175-Instru%C3%A7%C3%B5es-padr%C3%B5es-sobre-Controle-de-Qualidade-no-Estoque))/Devolução do Armazém de Transito([MV\_LOCTRAN](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021874551-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Configura%C3%A7%C3%A3o-e-Inclus%C3%A3o-de-Documento-de-Entrada-em-Tr%C3%A2nsito-MV-LOCTRAN))  
**DE7 -**Devolução de transferência de um para “N”.  
**DE9 -**Devolução para OP sem agregar custo.

**DEA -** Reavaliação de custo médio (Devolução de valor final para período).

**Existe também movimentos do tipo PR e ER:**

**PR0 -**Produção manual.  
**PR1 -** Produção automática.

**ER0 -** Estorno de produção manual.  
**ER1 -** Estorno de produção automática.

**Código dos movimentos automaticos:**

**499 -** Devolução automática. (reservado do sistema)  
**999 -** Requisição automática. (reservado do sistema)

* Exemplo: Inventario processado, Transferencia entre Armazens RE4/DE4.

**Principais rotinas que usam os tipos de movimentos:**

**MATA241 -** Movimentação multipla  
**MATA261 -** Transferência multipla  
**MATA242 -** Desmontagem

**Onde eu posso cadastrar o codigo para o meu tipo de movimento?**

Rotina MATA230(Internas), localizada em:

**Atualizações > Cadastros > Movimentações > Internas**

**Eu posso cadastrar os códigos 499 e 999?**

Os codigos **499** e **999** são reservados, portanto o cadastro desses códigos não é permitido, caso tente cadastrar sera apresentado o help **MA230RESER** **"O código 499 e o 999 são de uso exclusi-vo interno do sistema."**  
Essa é uma validação padrão contida no campo **F5\_CODIGO**, caso voce consiga digitar o codigo e salvar, sugerimos validar com o responsvel que cuida da estrutura de dados do ambiente, pois existe uma validação padrão no campo para que isso não ocorra.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
