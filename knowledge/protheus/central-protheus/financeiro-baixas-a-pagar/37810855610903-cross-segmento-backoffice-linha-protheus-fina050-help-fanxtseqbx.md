---
article_id: 37810855610903
category: Financeiro - Baixas a Pagar
content_hash: 4ef6cf7579f1e0fd63838cdd7e02c8835205318e7d05ba196631a1e1f066d29b
fetched_at: '2026-06-28T22:42:13.566412+00:00'
product: protheus
section_id: 38310054605975
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - FINA050 - HELP FANXTSEQBX
type: support-article
updated_at: '2026-03-04T16:45:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37810855610903-Cross-Segmento-Backoffice-Linha-Protheus-FINA050-HELP-FANXTSEQBX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37810844299159) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Como realizar o aumento do tamanho do campo E5\_SEQ (Sequência de Baixa) para evitar inconsistências no processo de baixas?  
  
  
**Solução**  
Essa mensagem é apresentada quando a quantidade de sequências geradas por uma operação ultrapassa o limite de caracteres permitido no campo **E5\_SEQ**.

Por padrão, o campo possui um tamanho limitado (geralmente 2 dígitos). Quando uma operação financeira exige a geração de registros que excedem esse limite (por exemplo, a compensação de 1 **PA** com mais de 99 **Notas Fiscais**, o que exigiria uma sequência de 3 dígitos), o sistema não consegue preencher o campo e bloqueia a operação.

A alternativa para a correção deste cenário é o aumento do tamanho do Grupo de Campos 134 (Sequência de Baixa), garantindo que o sistema suporte o volume de sequências necessárias para a operação. Atualmente, o campo pode possuir até **4 posições**.

Para que a alteração seja replicada de forma consistente em todas as tabelas relacionadas, a modificação deve ser realizada obrigatoriamente através do **Grupo de Campos** no módulo Configurador.

**Importante:** Recomendamos que a alteração seja validada primeiramente em ambiente de **homologação**. Em alguns casos, pode ser necessária a utilização da rotina auxiliar *RDMake* **FIXSEQBX** para ajuste das sequências já existentes.

Passos:

1. Acesse o módulo **Configurador (SIGACFG)**;
2. Vá em **Dicionário -> Base de Dados**;
3. No menu à esquerda, selecione **Grupo de Campos**;
4. Pesquise pelo Grupo **134** (Descrição: **Sequência de Baixa**);
5. Clique em **Alterar**;
6. Ajuste o tamanho do campo para a quantidade de posições desejada (respeitando o limite do sistema);
7. Confirme a alteração e clique em **Atualizar Base de Dados** (ícone do disquete/engrenagem) para que o sistema altere o dicionário e as tabelas físicas;

**Saiba mais**

[FIXSEQBX - Rdmake para ajuste no conteúdo dos campos \_SEQ](https://tdn.totvs.com.br/pages/viewpage.action?pageId=622668372)
