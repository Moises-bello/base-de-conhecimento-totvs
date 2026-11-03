---
article_id: 38337391739159
category: SIGAACD - Automação e Coleta de Dados
content_hash: f66d672ce796883c5a2e3c38bf6a97bf653ae50f154ed7eaeed26cf376fdb30a
fetched_at: '2026-06-28T22:39:12.594184+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Como gerar Ordem de
  Separação Parcial na rotina ACDA100.
type: support-article
updated_at: '2026-02-11T20:38:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38337391739159-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Como-gerar-Ordem-de-Separa%C3%A7%C3%A3o-Parcial-na-rotina-ACDA100
---

O parâmetro MV\_CBOSPRC no TOTVS Protheus define se o sistema permite gerar Ordens de Separação parciais para Ordens de Produção. Quando .F., não há separação parcial; se .T., permite separar apenas itens com saldo disponível, mantendo pendências para futuras separações quando houver reposição de estoque.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38337391732375) Tempo aproximado para leitura: **00:2:00 min**  
  
**Dúvida**  
O Parâmetro MV\_CBOSPRC permite ou não gerar Ordens de Separações parciais (ACDA100)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**  
Define o comportamento do sistema quanto à geração parcial de Ordens de Separação (OS) originadas de Ordens de Produção (OP).

Este parâmetro determina se o módulo ACD deve bloquear a geração da OS quando o saldo físico disponível no endereço/lote é inferior à quantidade solicitada no empenho da OP, ou se deve permitir a geração de uma ordem com a quantidade disponível no momento.

* Quando configurado como **.F.** (Falso) - Comportamento Padrão

O sistema adota uma validação restritiva ("Tudo ou Nada").

**Comportamento**: Ao processar a Ordem de Produção, a rotina lê a quantidade necessária no empenho (tabela SD4) e a compara com o saldo disponível no endereço/lote. Se a necessidade for **maior** que o saldo, o sistema aciona um bloqueio imediato e aborta a inclusão deste item na Ordem de Separação.

**Consequência**: O item é ignorado no processamento.

* O item é ignorado e **nenhum registro** é gravado na tabela de itens da separação (CB8).
* É gerado um registro de **Erro** no Log de Ocorrências da rotina com a mensagem: *"O produto [...] não possui saldo endereçado suficiente"* ou *"não encontra-se empenhado"* .
* A produção não recebe material parcial para evitar inconsistências no kit de montagem.

* Quando configurado como **.T.** (Verdadeiro)

O sistema habilita a Separação Parcial.

**Comportamento**: O sistema ignora a validação de saldo total. Caso o saldo seja insuficiente, o item é ignorado na geração atual, mas a Ordem de Separação é criada normalmente com os demais itens que possuem saldo.

**Consequência**: A Ordem de Separação é gerada com sucesso.

* + A Ordem de Separação é gerada com sucesso contendo apenas os produtos/quantidades disponíveis no momento.
  + **Gestão de Pendência:** A diferença (seja o saldo restante de um item parcial ou o item inteiro que não tinha saldo) permanece pendente na Ordem de Produção. O sistema não baixa o empenho original (`SD4`) totalmente, permitindo que uma nova execução da rotina gere uma nova OS complementar assim que o estoque for reposto.

|  |  |  |  |
| --- | --- | --- | --- |
| **Parâmetro** | **Tipo** | **Valor Padrão** | **Descrição** |
| MV\_CBOSPRC | Lógico | .F. | Permite gerar OS parcial para OP (Sim/Não).   * MV\_CBOSPRC = .F. : Não permite Separação Parcial * MV\_CBOSPRC = .T. : Permite a Separação Parcial |

## **Exemplo de Utilização**

Considere o Produto Acabado (PA): PAACD0001 com a seguinte estrutura:

```
PAACD0001 - PRODUTO ACABADO ACD | UN | Qtde: 1  
│  
├── PIACD0001 - PROD INTERMEDIÁRIO 01 ACD | UN | Qtde: 1  
│   │  
│   └── MPACD0001 - MAT PRIMA 01 ACD | UN | Qtde: 1  
│  
└── PIACD0002 - PROD INTERMEDIÁRIO 02 ACD | UN | Qtde: 1  
    │  
    ├── MPACD0002 - MAT PRIMA 02 ACD | UN | Qtde: 1  
    └── MPACD0003 - MAT PRIMA 03 ACD | UN | Qtde: 1
```

![](https://tdn.totvs.com/download/attachments/1025242674/image-2025-12-23_11-51-32.png?version=1&modificationDate=1766509674970&api=v2)

* Saldo Inicial da matéria prima com controle de endereçamento:  
  MPACD0001 - MAT PRIMA 01 ACD - Qtde: 10 | Endereço: 0001  
  MPACD0002 - MAT PRIMA 02 ACD - Qtde: 10 | Endereço: 0001  
  MPACD0003 - MAR PRIMA 03 ACD - Qtde: 7 | Endereço: 0001

![](https://tdn.totvs.com/download/attachments/1025242674/image-2025-12-23_12-1-32.png?version=1&modificationDate=1766509674880&api=v2)

* Criado Ordem de Produção (MATA650) PCP600 para o PA MPACD0001, gerando os empenhos:  
  Produto Intermediário:  
  ![](https://tdn.totvs.com/download/attachments/1025242674/image-2025-12-23_12-4-49.png?version=1&modificationDate=1766509674817&api=v2)
* Matéria Prima 01: Com composição de empenho (SDC) para o endereço: 0001  
  ![](https://tdn.totvs.com/download/attachments/1025242674/image-2025-12-23_12-8-14.png?version=1&modificationDate=1766509674657&api=v2)
* Matéria Prima 02 e 03: Somente o produto MPACD0002 com composição de empenho, pois o saldo do produto MPACD0003 é menor que a ordem de produção.  
  ![](https://tdn.totvs.com/download/attachments/1025242674/image-2025-12-23_13-47-4.png?version=1&modificationDate=1766509674457&api=v2)  
    
  Resultado dos registros entre **SC2**(Ordens de Produção), **SD4**(Requisições Empenhadas) e **SDC**(Composição do empenho):  
  ![](https://tdn.totvs.com/download/attachments/1025242674/image-2025-12-23_13-50-35.png?version=1&modificationDate=1766509674350&api=v2)

Partindo desse cenário, vamos criar as Ordens de Separação (ACDA100) com as variações do parâmetro MV\_CBOSPRC:

**MV\_CBOSPRC = .F.**

* Outras Ações → Gerar, definimos as perguntas:  
  ![](https://tdn.totvs.com/download/attachments/1025242674/image-2025-12-23_13-54-17.png?version=1&modificationDate=1766509674260&api=v2)  
    
  ![](https://tdn.totvs.com/download/attachments/1025242674/image-2025-12-23_13-54-35.png?version=1&modificationDate=1766509674183&api=v2)  
    
  ![](https://tdn.totvs.com/download/attachments/1025242674/image-2025-12-23_13-55-0.png?version=1&modificationDate=1766509674097&api=v2)
* Selecionamos as OS para cada OP gerada, conforme imagem:  
  ![](https://tdn.totvs.com/download/attachments/1025242674/image-2025-12-23_13-56-4.png?version=1&modificationDate=1766509674040&api=v2)
* Com o parâmetro MV\_CBOSPRC = .F. não é gerado a ordem de separação para MPACD0002 e MPACD0003 pois o saldo da matéria prima é inferior a ordem de produção.  
  ![](https://tdn.totvs.com/download/attachments/1025242674/image-2025-12-23_13-59-32.png?version=1&modificationDate=1766509673977&api=v2)

**MV\_CBOSPRC = .T.**

* Outras Ações → Gerar, definimos as mesmas perguntas, selecionamos as OPs para separação:  
  ![](https://tdn.totvs.com/download/attachments/1025242674/image-2025-12-23_14-4-8.png?version=1&modificationDate=1766509673900&api=v2)
* É gerada a ordem de separação (no exemplo: 000243) para o produto MPACD0002, mesmo que o produto MPACD0003 não possua saldo total para utilização.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38337391733911)

## **DEMAIS INFORMAÇÕES**

**Tabelas Relacionadas:**

SC2 - Ordens de Produção.

SD4 - Requisições Empenhadas (Necessidades).

CB7 / CB8 - Cabeçalho e Itens das Ordens de Separação.

SBF / SDC - Saldos por Endereço e Composição de Empenho.

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)

[Ordens de Separação de OP usando produto com estrutura ( ACDA100 - SIGAACD )](https://tdn.totvs.com/pages/viewpage.action?pageId=793829826)

[O Parâmetro MV\_CBOSPRC permite ou não gerar Ordens de Separações parciais (ACDA100)](https://tdn.totvs.com/pages/releaseview.action?pageId=1025242674)
